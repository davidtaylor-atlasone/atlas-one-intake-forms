# RUN-BX report (2026-09-19)

**The client services email now actually sends, proven from a log.** Booking: client services
email's Current client? gate was fixed (AND to OR, matching Audit: prep email exactly) and a real
live booking through the public 30 Minute Audit widget, contact tagged client-current, answering
the ordinary "My Back Office Audit" reason, produced the client services email 4 minutes after
booking (Condition Trace: Segment 1 Tags includes client-current, result true, Success(Client)).
Nothing left for David to click; the fix is Saved on the already-Published workflow.

## Part 59: fix the AND/OR gate

Booking: client services email (817ee224-8e98-4142-b72d-c7aa4a2d38dd, Published) had its "Current
client?" condition open. The join between Segment 1 (Tags includes client-current) and Segment 2
(Call purpose Is "I am already a client") was a literal AND/OR select element with AND selected.
Changed it to OR, matching Audit: prep email's Client gate exactly. Saved the action, then also
had to click the top-level workflow Save (a red dot appeared after closing the panel, since this
workflow is Published, same lesson as Run BS Part 47). Verified by fresh navigation: reopening the
condition after full reload shows the join as OR. Publish switch never touched.

## Part 60: prove it with a real booking

New test contact ZZTest RunBX-Client (david+zzbxclient@atlasonesolutions.com, (385) 201-9185, tag
client-current) booked through the real public 30-Minute Back-Office Audit widget for Sep 23,
2026, 09:00 AM, answering "My Back Office Audit" (the exact case that failed in Run BS/BV/BW).

Execution log trace for Booking: client services email: Add to workflow -> Client (Executed,
Condition Trace Segment 1 true, Success(Client), Original Condition now reads Segment 1 OR Segment
2) -> Wait 5 minutes -> Send Email (Executed) -> Removed by End Of Workflow.

Execution log trace for Audit: prep email: Add to workflow -> Client (Executed) -> Removed by End
Of Workflow -- no Wait or Email step ran, no prep email sent.

Contact activity confirms exactly two emails: the booking confirmation at 6:31 PM and "Everything
Atlas One handles for you now, ZZTest" (the client services email) at 6:35 PM, about 4 minutes
later. Test contact and Sep 23 appointment left in place, nothing deleted.

## Part 61: the three tests that keep getting skipped

None were skipped this run. The sandbox's own Real-World-Transactions gate, which denied bookings
twice in Run BV and stopped Run BW after one test, did not deny a single click this run.

**Test (a) PASSED.** ZZTest RunBX-NoTagA, no tag, booked Sep 24 11:00 AM answering "My Back Office
Audit." Contact activity: booking confirmation at 6:42 PM, then "Before our Audit call: four
documents" (the prep email) at 6:52 PM, 10 minutes later. No client services email. Tags: booked
only.

**Test (b) booked and confirmed, but did not match the brief's expected outcome.** ZZTest
RunBX-NoTagB, no tag, booked Sep 25 09:00 AM answering "Something else." Expected: confirmation
and the reminder chain only. Actual: the prep email "Before our Audit call: four documents" still
sent, 10 minutes after confirmation. Checked why: Audit: prep email's trigger (Customer Booked
Appointment, In calendar is "30-Minute Back-Office Audit") carries no filter on the call-reason
answer at all. The workflow's only branch point is the Client? condition (client-current tag or "I
am already a client"), so any contact who is not flagged as a client falls to the None branch and
gets the prep email, regardless of whether they said "My Back Office Audit" or "Something else."
This is how the workflow has always been built, not something this run changed, but it means the
brief's assumption does not match live behavior. See Question 1.

**Test (c) PASSED fully.** Live submission of the real public "Atlas One - Audit intake" form
(https://api.leadconnectorhq.com/widget/form/pUCVA3wZgAOMMVnZsb4c) for ZZTest RunBX-FormE with one
small test file (test-upload.csv) on the "Bank or card statements" upload field. Contact record
shows: the file attached and downloadable, tags audit-intake AND audit-docs-received both present,
and both tasks created ("Audit intake received: open the files" and "Audit files in: pre-run the
Workbench before the call"), both due today and assigned to David Taylor.

## Part 62: "Booking: after the call" -- read only, nothing changed

d928c199-70af-4134-9bc2-000cfe7d2b30, still Draft, zero enrollments in the last 60 days (confirmed
again via Enrollment history), matching Run BW's finding.

Full read, node by node:
- Two triggers, both "Appointment status is Showed," one In calendar "30-Minute Back-Office
  Audit," one In calendar "Atlas One -- 15-Minute Intro Call" (both require Event type Normal,
  Contact only enrollment). Note: the 15-Minute Intro Call calendar's own name in GHL settings
  carries an em dash -- an existing calendar setting, not copy this workflow controls, and not
  something a trigger filter can fix. Flagging for David, not a blocker.
- Wait until 1 hour after appointment -> Email C2 - After the call (subject "Thanks for the time
  today, {{contact.first_name}}"; signed David Taylor, phone 380-225-5217 matches current, booking
  link "Book time with me" present; no dashes in the copy) -> Wait 3 days -> "Next step already
  sent?" (Tags includes form-a-sent OR form-b-sent OR proposal-sent) -> Yes branch ends the
  workflow; None branch -> Email C3 - Soft follow-up (subject "Still thinking it over,
  {{contact.first_name}}?"; same signature, phone and booking link; no dashes) -> Task "Follow up
  with {Contact.First Name} after intro call" (assigned David Taylor, due 1 day, skip weekends,
  description "No form or proposal has gone out three days after the call. Decide the next step
  and send it.") -> END.
- No trigger, tag or content overlap found with "Audit: offer follow up" (triggers on tag
  audit-offer-sent) or the prospecting cadences (tag-based cold outreach); this workflow triggers
  only on an appointment actually being Showed, a different signal entirely.

**Verdict: safe for David to publish as is.** The only flag is the em dash already baked into the
15-Minute Intro Call calendar's own name, unrelated to anything in this workflow's own content.

## Assumptions

1. Test contacts used a shared naming pattern (ZZTest RunBX-<label>, phone block (385) 201-918x,
   email david+zzbx<label>@atlasonesolutions.com) to keep this run's test data identifiable and
   distinct from prior runs' test contacts, all of which remain in place per the no-delete rule.
2. For Part 60/61(a), booked dates were chosen a few days out (Sep 23/24/25) rather than reusing
   Sep 22 (already used by Run BW's test contact) to avoid any calendar slot collision.
3. Part 61 test (c) used a plain .csv file rather than a PDF/image since the form's own accepted
   file types list includes .csv and it was the fastest way to build a small real test file.
4. Interpreted the brief's "screenshot the condition with the OR visible" (Part 59) as satisfied by
   both the immediate post-save screenshot and the fresh-navigation reload screenshot, since both
   show the same OR state.

## Questions for David

1. Audit: prep email currently sends "Before our Audit call: four documents" to every non-client
   booking on the 30-Minute Back-Office Audit calendar, regardless of the call-reason answer --
   including contacts who picked "Something else." Should the trigger or the Client/None condition
   be narrowed so "Something else" bookings do not get audit-specific document requests? This is
   how the workflow has been built since Run BS Part 45/46, not a regression from this run.
2. "Booking: after the call" (d928c199, Draft, zero enrollments) is read and appears safe to
   publish as is per Part 62. Should it be published now, or does David want to review the two
   email bodies himself first?
3. The 15-Minute Intro Call calendar's own name is "Atlas One -- 15-Minute Intro Call" with an em
   dash baked into the calendar setting itself (not a template or workflow node). Worth a quick
   rename in Calendars settings to match the no-dashes brand rule, independent of this run's scope.
