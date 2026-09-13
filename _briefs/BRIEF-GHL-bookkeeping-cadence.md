# BRIEF-GHL-bookkeeping-cadence: build "Books: after the call" and the three seasonal inserts

Written by terminal GHL-JOBS 2026-09-13 (Run AH job 3), ready for the GHL terminal (the only session allowed in
the GHL browser UI). Copy this file to `_briefs/RUN-AH-bookkeeping-GHL.md` in the repo before starting, work from
there, record turn by turn, then close out `RUN-GHL-report.md`. Email copy source:
`A1_Sales/Email Templates/Atlas_One_Bookkeeping_Cadence_2026-09-13.md` (paste bodies verbatim through the `</>`
source dialog, triple click first, reload and re read after every save). Same rules as every GHL run: one tab,
never the in-app refresh link, unique phone plus unique plus addressed email on test contacts, delete them after,
no dashes anywhere, never enable SMS or HIPAA, never enter a password, no cold navigation to a URL.

## Hand off mode (copied from BRIEF-GHL.md Part 0, same procedure, new target)

1. Call `tabs_context` first and use an existing tab already on app.ridethehightide.com if one exists. Do not open
   a new tab until existing ones are checked.
2. If every tab shows the sign in form: stop, write `RUN-GHL-report.md` with "needs login" at the top, one line on
   which tabs were seen, and end. Never type a password.
3. Click Automation so the Workflows list shows. Do not click a row, do not reload, do not close the tab.
4. Print exactly this and wait: "David: in the Chrome tab I just opened (the Workflows list), click New Workflow
   (or the workflow named 'Books: after the call' once it exists) so its editor opens, then type ok here." When he
   types ok, screenshot, confirm the editor is open, and begin building.
5. Every time a different workflow is needed ("Call: not now", "Seasonal touches 2026-27"), go back with the
   in-app back arrow and print the same message with that name, then wait for ok. Never navigate the tab to a URL.
6. If David's own click leaves the editor hung (spinner, FirebaseError), stop, write "editor dead even for David"
   at the top of the report, and end.

## Tag to create

`books-interest`: create if missing (custom tag, no special type). Triggered by David adding it by hand after any
call where books came up, or by Form B (bookkeeping intake) submitting without a booked call (if Form B's
workflow does not already add this tag on that branch, add an Add Tag `books-interest` step to it as part of this
job, immediately after the "no call booked" branch check; do not touch any other branch of that workflow).

## New workflow: "Books: after the call"

Trigger: Tag added, `books-interest`. Re-entry: off (same as "Call: not now" and the Long Tail loop, so a contact
who already ran the sequence does not restart on a stray re-tag).

Suppression gate, used identically before every send (copy the exact same If/Else structure Run P built for the
Long Tail loop, a seven segment OR, since this sequence needs both the reply/booked exits AND the same standing
tags "Call: not now" is gated on):
`Suppressed = OR(tag "reply received", tag "booked", tag "client-current", tag "do-not-prospect", tag "partner",
tag "dnc", tag "quiet")`. Suppressed branch: END the workflow immediately. None branch: continue.

Node order:
1. Gate 0 (as above). Suppressed to END.
2. Send email **B-1** (subject: "What Atlas One bookkeeping actually looks like, {{contact.first_name}}"; body
   and button from the cadence doc).
3. Update contact field Last Touch Date = today.
4. Add tag `recent-touch`.
5. Wait 3 days.
6. Gate 1 (same seven segment check). Suppressed to END.
7. Send email **B-2** (subject: "What falling behind on the books actually costs").
8. Last Touch Date = today; Add tag `recent-touch`.
9. Wait 4 days (this lands B-2 to B-3 at day 7 total from B-1, matching the brief's "+7 days").
10. Gate 2. Suppressed to END.
11. Send email **B-3** (subject: "A proof point, no names attached").
12. Last Touch Date = today; Add tag `recent-touch`.
13. Wait 7 days (day 14 total from B-1, matching "+14 days").
14. Gate 3. Suppressed to END.
15. Send email **B-4** (subject: "Should I close your file, {{contact.first_name}}?").
16. Last Touch Date = today; Add tag `recent-touch`.
17. Wait 3 days (same pattern as the Long Tail loop's tail wait before hand off).
18. Gate 4. Suppressed to END.
19. Add tag `not-now`. This is the hand off: "Call: not now" already triggers on tag added `not-now`, so no
    further action needed here.
20. END.

If the Update Opportunity or Last Touch Date field write is ever skipped because the trigger carries no
opportunity (the same problem Run M and Run P both hit with tag triggers), do not fork the canvas; leave the tag
based `recent-touch` write in place and note the skip, exactly as Run P did.

## Seasonal inserts into "Seasonal touches 2026-27" (`52f414cb-b63e-4425-80c9-adea42a210e3`)

Same audience (`hold-45` OR `not-now` OR `quiet`, re-entry on) and the same cooldown gate pattern Run P built:
before every send, `Suppressed = OR(client-current, do-not-prospect, partner, dnc, booked, recent-touch)`.

Read the current node order first (RUN-P-report.md: YE-1 2026-11-01, YE-2 2026-11-15, YE-3 2026-12-01, YE-4
2026-12-15, then Q-1 x3 on 2027-03-01, 2027-06-01, 2027-09-01) and confirm it still matches before inserting.
Insert the three new sends as follows, each as its own Wait until date, gate, send, Last Touch Date, `recent-touch`
block, in this position in the chain:

- **BYE-1** ("January is the easiest month to start clean books"): same date as YE-1, 2026-11-01. Insert
  immediately BEFORE the existing YE-1 block (same Wait until date node reused if GHL allows two sends off one
  Wait, otherwise a new Wait node dated identically).
- **BQ-1** ("The easiest time to switch bookkeepers is right now"): same date as each Q-1 send, so it repeats
  three times, once immediately before each of the three Q-1 blocks (2027-03-01, 2027-06-01, 2027-09-01).
- **BYE-2** ("Start the year with a clean set of books"): new date 2027-01-05, inserted as its own block between
  the existing YE-4 block (2026-12-15) and the first Q-1 block (2027-03-01).

**Build note, flag for David:** because every send in this chain sets `recent-touch` and every gate checks
`recent-touch`, placing a new send immediately before an existing same date send means the second of the pair
will see `recent-touch` already set and get suppressed, so only the first email of same date pair actually goes
out. This is the same accepted behavior YE-3 already relies on (one email covers two purposes on Dec 1). Put the
bookkeeping specific version first in each pair (BYE-1 before YE-1, BQ-1 before each Q-1) since it is the newer,
more specific message; the general one is silently skipped that day by design. If David would rather both fire,
the fix is to move one member of each pair one day later (for example BQ-1 the day before Q-1) so the cooldown
gate does not catch it; that is a one line date change once he decides, so do not decide it now, ask in the report.

Annual maintenance note: same as Run P, every December the dates in this workflow (now including BYE-1, BQ-1 x3,
BYE-2) advance one year.

## Test plan

One test contact, unique phone, plus addressed email (for example `david+zzbk1@atlasonesolutions.com`). Add tag
`books-interest` by hand, with waits temporarily shrunk to 1 minute each, and confirm all four sends (B-1 to B-4)
arrive in order, Last Touch Date updates each time, and the contact ends up tagged `recent-touch` and `not-now`,
then confirm "Call: not now" picks it up (same proof pattern Run P used for the Long Tail loop hand off). Second
test contact tagged `quiet` (or `hold-45`) with one seasonal date moved two minutes ahead to prove one of the new
inserts (BYE-1 or BQ-1) fires and the paired existing send is correctly suppressed by `recent-touch`. Put every
wait and date back to production values, reload and re read each one after a full reload, delete both test
contacts, commit and push, then report: workflow id for "Books: after the call", the two Step 0 style test
results, and the same date pair question above.
