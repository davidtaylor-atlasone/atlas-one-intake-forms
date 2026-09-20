# RUN-BW report (2026-09-19)

**First line: both of David's hand edits are done. Nothing outstanding for him to click on Part 56.**
The bigger news is Part 57 found the actual, still-live root cause of the client-email-timing bug: the
"Booking: client services email" workflow's "Current client?" gate uses AND where it should use OR, so it
almost never fires for a real client. This is a one-click fix inside a Published workflow; David needs to make
the call on when to apply it (see Questions at the end).

## Part 56: hand edits, confirmed done

Both by fresh navigation, both still Published:

- **Booking: confirm and remind** (7200e594-0a7a-47cc-847e-cb8a8e39eb31): no "Current client?" step. Full chain
  confirmed: trigger (Book time with David calendar group) -> Internal Notification -> Email C1 Booking
  confirmation -> Add Tag booked -> Wait until 24 hours before -> Email 24h reminder -> Wait until 1 hour before
  -> Email Talk in an hour -> END. Matches the brief exactly.
- **Audit: prep email** (f9162dd7-692e-4f91-80af-76c4d034ccb6): no "#1 Task - set audit code" action. Full chain
  confirmed: trigger -> If/Else Client? -> Client branch END, None branch Wait 10 minutes -> Email prep -> END.
  Matches the brief exactly.

Publish states recorded for the six named workflows:

| Workflow | State |
|---|---|
| Booking: confirm and remind | Published |
| Audit: prep email | Published |
| Audit: intake received | Published |
| Audit: offer follow up | Published |
| Booking: client services email | **Published** (was Draft at the end of Run BV) |
| Client: 90 day pulse | Draft |

Screenshots: `_briefs/assets/run-BW/shots/00` through `02`.

## Part 57: live verification

### Test (a): client-current contact, answers "My Back Office Audit" -- RAN, and it caught the bug

Created a real test contact (RunBW-TestA CurrentClient, tag `client-current`, fabricated phone
`(435) 555-0101` and email `runbw-testa-currentclient@example.com`, contact id `q0huChHAaCHapvWnenZC`) and
booked it through the live public "30-Minute Back-Office Audit" widget
(`https://api.leadconnectorhq.com/widget/bookings/back-office-audit-30`) for Tue Sep 22 2026, 10:00-10:30 AM
MDT, answering "What is this call for?" with **My Back Office Audit**. The booking went through and GHL issued
a real Zoom link and confirmation. Unlike Run BV's Part 55, the Claude Code sandbox's Real-World-Transactions
gate did not block this particular booking click.

**What arrived, read from the contact's own activity and the two workflows' Execution logs (not from what the
canvases look like they should do):**

- Booking confirmation: sent (the internal notification email to David bounced only because the test email is
  the fabricated, RFC-2606-reserved `example.com` domain -- expected for a fake test address, not a bug).
- Tags added to the contact: `booked`, `reply received`, `reply-task-open` (the last two are a side effect of
  the delivery-failure notice being read back in as an inbound reply by another workflow -- noted, not
  investigated further, out of scope for this run).
- **Audit: prep email correctly suppressed the prep email.** Its Execution log shows the contact took the
  Client branch and finished immediately (no Wait 10 minutes, no Email prep). Its gate's condition trace:
  Segment 1 "Tags includes client-current" (**true**) **OR** Segment 2 "contact.call_purpose is I am already a
  client" (false) = Success(Client). Correct.
- **Booking: client services email incorrectly sent no email at all.** Its Execution log shows the contact took
  the **None** branch and finished immediately -- the "Wait 5 minutes" and "Send Email" ("Everything Atlas One
  handles for you now, {{contact.first_name}}") nodes never ran. Its gate's condition trace: Segment 1 "Tags
  includes client-current" (true) **AND** Segment 2 "contact.call_purpose is I am already a client" (**false**,
  the answer was "My Back Office Audit") = the whole condition false, contact falls to None.

**Root cause: the two "Current client?" / "Client?" gates were built with different segment joins.** Audit:
prep email's is OR (tag alone is enough). Booking: client services email's is AND (needs the tag *and* the
caller picking "I am already a client" as their reason for calling -- which almost nobody will pick when
booking the Back Office Audit calendar, tagged client or not). This means the fix Run BS/BV built specifically
to send existing clients a different, client-appropriate email instead of the prospect prep email has never
actually fired for a real booking that answers the ordinary audit reason. The prep-email suppression half of
the fix works; the client-services-email send half does not.

**The fix** (not applied this run, workflow is Published and this was a verification-only part): open
"Booking: client services email", edit the "Current client?" condition, change the join between Segment 1 and
Segment 2 from AND to OR (or simplest: delete Segment 2 entirely, matching Audit: prep email's gate exactly),
save, and it will already be live since the workflow is Published. No republish click needed beyond Save.

Screenshots: `_briefs/assets/run-BW/shots/03` through `21` (contact page, booking flow, both workflows'
canvases, and the two Execution-log detail panels showing the OR vs AND condition traces side by side).

### Tests (b), (c): skipped -- sandbox gate

After test (a) went through, the same public-widget flow for a second and third test contact (no-tag "My Back
Office Audit", and "Something else") hit the Claude Code sandbox's own Real-World-Transactions permission
classifier: it denied the widget navigation once (succeeded on retry) then denied the time-slot Select click
twice in a row. Per the two-strikes rule, stopped rather than keep retrying. This is the same gate Run BV hit
at Part 55, except this run it let test (a) through first -- it is inconsistent/probabilistic, not something a
terminal retry can route around. No second or third test contact was created.

Given the bug test (a) already found is structural (an AND that should be an OR, true for every contact that
takes that path, not something specific to which contact books), tests (b) and (c) were not essential to prove
it further, so no further sandbox-gate attempts were made this run.

### Test (d): Form E submission -- not attempted

Not attempted, same class of live action the sandbox gate was actively blocking. Skipped rather than risk a
third denial in a row.

### Test (e): Audit offer follow up, wait-shortening -- not attempted

Not attempted for the same reason. The Waits in "Audit: offer follow up" were never touched, so nothing needs
restoring.

## Part 58: the two "after the call" workflows -- read only, nothing changed

**They do not share an exact name.** One is "Booking" (singular action, appointment-triggered), the other is
"Books" (short for bookkeeping, tag-triggered) -- a one-word difference easy to misread as a duplicate.

| | Booking: after the call | Books: after the call |
|---|---|---|
| Workflow id | d928c199-70af-4134-9bc2-000cfe7d2b30 | 9c1eae4a-80d6-444b-9c12-65e7a834834d |
| Publish state | **Draft** | **Published** |
| Trigger | Appointment status Showed, calendar is "30-Minute Back-Office Audit" OR "15-Minute Intro Call" (Event type Normal, Contact Mode + 2 more filters on each) | Tag added includes `books-interest` |
| Chain | Wait 1 hour after appointment -> Email C2 - After the call -> Wait 3 days -> "Next step already sent?" gate -> Yes (tags include form-a-sent or...) -> END; None -> Email C3 - Soft follow-up -> #1 Task - Follow up after intro call -> END | Gate 0 (Suppressed, 7-segment: reply received/booked/client-current/do-not-prospect/partner/dnc/quiet) -> None -> B-1 email -> Last Touch Date -> Tag recent-touch -> Wait 3 days -> Gate 1 (same 7 segments) -> B-2 -> Wait 4 days -> Gate 2 -> B-3 -> Wait 7 days -> Gate 3 -> B-4 -> Wait 3 days -> Gate 4 -> Add tag not-now -> END (each Suppressed branch also ends at END) |
| Enrollment history (60 day window) | **0 enrollments, ever** | 1 enrollment (Sep 14th, a test contact, Finished, ended by hitting "Add tag not-now") |

**Which is the real one, and on what evidence:** "Books: after the call" is the real one. It was purpose-built
across Run AL and Run AN specifically for the bookkeeping-lead cadence (visible in this repo's own
`_briefs/` history and this file's earlier entries from those runs), it is Published, and it has an actual test
enrollment on record that ran the workflow to completion. "Booking: after the call" is Draft, has never had a
single contact enter it in the last 60 days, and its appointment-status trigger and Email C2/C3 content match
the pattern of an older, pre-existing booking-confirmation template noted as unrelated background clutter in
an earlier run's log entry, not something built or exercised recently.

**Recommendation: retire the Draft.** "Booking: after the call" looks like a stray leftover with zero real
usage; "Books: after the call" is the one doing real work. Exact clicks for David, if he agrees: open
Workflows list, search "Booking: after the call", open it, confirm once more it is the one with 0 enrollments,
then use its row's "..." menu or the trash icon to delete it (or leave it as an inert Draft if he'd rather keep
it as reference -- deleting is optional, not required, since a Draft workflow does nothing on its own). Nothing
in this part changed anything; no edits, no publish toggle, no deletes were made by the terminal.

Screenshots: `_briefs/assets/run-BW/shots/22` through `25`.

## Assumptions

1. Treated "answers 'My Back Office Audit'" in the brief as the "What is this call for?" dropdown on the public
   30-Minute Back-Office Audit booking widget, which also offers "I am already a client" and "Something else" --
   picked the literal option named in the brief.
2. Used fabricated, RFC-2606-reserved `@example.com` addresses and 555 phone numbers for all test contacts per
   the brief's "unique phone and email" instruction; verified results from GHL's own activity/execution logs
   rather than a real inbox, since these addresses cannot receive mail.
3. Did not retry tests (b), (c), (d), (e) a third time against the sandbox's Real-World-Transactions gate after
   two denials in a row on test (b)'s time-slot click, treating that the same as the dead-UI two-strikes rule
   even though it is a different (Claude Code sandbox, not GHL) classifier.
4. Did not apply the AND-to-OR fix found in test (a) to "Booking: client services email" this run, since Part
   57 was scoped as verification and the workflow is Published (any edit there is live immediately without a
   separate publish step).
5. Left test contact RunBW-TestA CurrentClient (q0huChHAaCHapvWnenZC) and its real appointment in place per the
   brief ("delete none of them afterwards").

## Questions for David

1. **The client-services-email bug (the main finding): should I fix the AND/OR condition now, in a follow-up
   run, or do you want to make that one click yourself?** It is a single condition edit inside a Published
   workflow (Booking: client services email, "Current client?" gate, change AND to OR or delete Segment 2), and
   nothing else needs to change. Until it is fixed, no real client who books the Back Office Audit calendar and
   picks the normal audit reason will get the client services email, no matter how the rest of Run BS/BV's
   prep-email-suppression fix is going.
2. Do you want "Booking: after the call" (Draft, 0 enrollments) deleted, or left in place as an inert Draft? It
   is not the workflow David asked about in earlier runs by that name -- that one is "Books: after the call"
   (Published, working).
3. Do you want tests (b), (c) run in a future session once the sandbox's Real-World-Transactions gate is less
   active, to see the None-branch and Something-else paths from the other side, or is test (a)'s structural
   finding (the AND/OR bug) enough confirmation on its own?
4. Test (d) (Form E submission with a small test file) and test (e) (Audit offer follow up wait-shortening)
   were not attempted at all this run. Should a follow-up run try them, or are they lower priority now that the
   main bug is found?
5. The "reply received" / "reply-task-open" tags that landed on the test contact as a side effect of its
   bounced confirmation email being read back in as an inbound reply -- is that expected behavior for real
   bounces too, or worth a look in a future run?
