# RUN-BV report (2026-09-19)

**Booking: confirm and remind is NOT clean.** The bad "Current client?" step from Run BS Part 47
is still in the published workflow, gating the client email behind the 24 hour and 1 hour
reminder waits. David has not yet removed it (the brief assumed he would before this run started).
David needs to:
1. Remove the "Current client?" If/Else step from "Booking: confirm and remind"
   (7200e594-0a7a-47cc-847e-cb8a8e39eb31) himself, since this terminal cannot delete a step from a
   Published workflow (permission classifier blocks it, confirmed again this run in Part 54).
2. Decide whether to publish the new "Booking: client services email" workflow (Draft, id
   817ee224-8e98-4142-b72d-c7aa4a2d38dd) built this run, which is the real fix for the client email
   timing bug once the old node above is removed.
3. Know that "Audit: prep email" (f9162dd7-692e-4f91-80af-76c4d034ccb6) is now Published (it was
   Draft as of Run BQ/BS) and still carries the "#1 Task - set audit code" busywork task the brief
   wanted removed; this terminal could not delete it either (see Part 54).
4. Know that Part 55's live verification pass could not run at all this session (see below) --
   the booking workflow's real behavior with real bookings is still unconfirmed for this run.

## Part 52: confirm Booking: confirm and remind is back to normal

Opened 7200e594-0a7a-47cc-847e-cb8a8e39eb31 fresh (root navigation, Automation, Workflows list,
reopen row, Fit to Screen). Node order read exactly: trigger (Booked - any Book time with David
calendar), Internal Notification, Email C1 - Booking confirmation, Add Tag - booked, Wait until 24
hours before, Email - 24h reminder, Wait until 1 hour before, Email - Talk in an hour, **Current
client? If/Else** (Client branch: Tags includes client-current OR Call purpose Is I am already a
client -> Email - Client more we handle -> END; None branch -> END). This is the exact bug Run BS
found: the client email is still gated behind both reminder waits, so a client who books days out
will not get it for days. Per the brief, did **not** delete this step and built nothing into this
workflow. Screenshot: `_briefs/assets/run-BV/shots/52-booking-confirm-remind-current-state.png`.

## Part 53: Booking: client services email (new workflow, built)

Built new workflow "Booking: client services email" (id 817ee224-8e98-4142-b72d-c7aa4a2d38dd),
left Draft. Trigger: Customer Booked Appointment, filtered In calendar is "30-Minute Back-Office
Audit" (single calendar, not the group, matching what "Audit: prep email" uses). First action an
If/Else "Current client?": Client branch = Tags includes client-current OR Call purpose Is "I am
already a client" -> Wait 5 minutes -> Send Email (existing template A1 | Client | more we handle,
From Name David Taylor, Atlas One Solutions, From Email David@AtlasOneSolutions.com, subject
"Everything Atlas One handles for you now, {{contact.first_name}}") -> END. None branch -> straight
to END, nothing else added. The 5 minute wait is so the client email lands after the booking
confirmation rather than on top of it.

Verified via fresh navigation reload (root, Automation, Workflows list): row reads "Booking:
client services email", status Draft. Also verified on-canvas with Fit to Screen screenshots after
each save. Screenshots: `_briefs/assets/run-BV/shots/53a-after-ifelse-save.png`,
`53b-wait-added.png`, `53c-email-added-fit.png`.

This workflow is the fix, but it does nothing until (a) the old "Current client?" step is removed
from "Booking: confirm and remind" and (b) this new workflow is published. Neither has happened
yet.

## Part 54: audit code task in Audit: prep email -- blocked, not completed

Opened f9162dd7-692e-4f91-80af-76c4d034ccb6 and found it is now **Published**, not Draft as the
brief assumed (it must have been published sometime after Run BQ/BS). Structure read exactly as
expected: trigger, Client? If/Else, Client branch -> END, None branch -> Wait -> Email -> "#1 Task
- set audit code" -> END.

Tried to delete the "#1 Task - set audit code" action via its "..." menu -> Delete action: denied
twice by the permission classifier (reason: Modify Shared Resources, because this is now a
Published workflow). Per the brief's own contingency ("if the delete is blocked anyway, leave it
and say so plainly in the report rather than retrying more than twice"), stopped after two
attempts. The task is still there. Nothing else in this workflow was touched.
Screenshot: `_briefs/assets/run-BV/shots/54a-prep-email-before-delete.png`.

## Part 55: verification pass -- blocked at the first live step

Created a test contact for test (a): ZZTest, david+zzbvclient@atlasonesolutions.com,
(385) 201-9184, tag client-current, contact id U3ATtLoT75j68zEZjlqX. Contact creation succeeded
without issue.

Opened the public 30-Minute Back-Office Audit booking widget
(https://api.leadconnectorhq.com/widget/booking/mRbFII938P3HrfODYH2K), picked Sep 22, 2026, and
tried to select a 09:00 AM time slot to actually book the test appointment. This was **denied
twice by the Claude Code sandbox's own permission classifier** (reason: "Real-World
Transactions") -- not GHL's in-app classifier, and not something Parts 52-54's contingency
language covers, since it is a different and more fundamental gate. Per this terminal's standing
rule to not attempt to work around a permission denial, stopped after two attempts rather than
retry further or look for an alternate path to the same booking.

This blocks every remaining sub-part of Part 55, since (a) and (b) both need a real booking to go
through, (c) would need a real Form E submission (likely the same gate), and (d) needs a real tag
add that fires real workflow sends. None of a-e were attempted or completed. The test contact
ZZTest was left in place, untagged and unbooked otherwise; nothing was deleted.

## Assumptions

1. Treated the Claude Code sandbox's "Real-World Transactions" denial as a hard stop distinct from
   GHL's own Modify Shared Resources classifier, since it blocked the very first click of a booking
   flow (selecting a time slot) rather than a specific edit action, and retrying identical clicks
   would not change the outcome.
2. Did not attempt Form E submission or the Part 55d Wait-shortening test after the booking-widget
   denial, on the reasoning that both would trigger the same category of "real-world" action
   (a real form submission and real workflow-triggered sends), and burning more classifier
   denials on the same root cause would not surface new information for David.
3. Left the Audit: prep email task and Booking: confirm and remind's bad step in place rather than
   trying alternate deletion paths (e.g. copy-and-rebuild), since both are Published and any
   alternate path still runs into the same Modify Shared Resources gate on a live workflow.
4. Left ZZTest (client-current) as a new, untouched test contact for David's own use once he can
   run the booking tests himself, rather than deleting it.

## Skipped / not completed

- Part 52: could not delete the bad "Current client?" step (per brief, since it is still there).
- Part 54: could not delete the audit-code task (blocked twice, Published workflow).
- Part 55 a-e: none attempted after the booking-widget classifier denial; live verification of
  this run's own Part 53 build, and of the still-outstanding Part 52/54 items, remains undone.

## Questions for David

1. Please remove the "Current client?" step from "Booking: confirm and remind" yourself (this
   terminal cannot delete from a Published workflow), then say when it's done so a future run can
   publish "Booking: client services email" and re-verify.
2. Please delete the "#1 Task - set audit code" action from "Audit: prep email" yourself for the
   same reason (Published workflow, Modify Shared Resources denial) -- or confirm you'd rather keep
   it now that the workflow is live.
3. This session's permission classifier blocked booking a real appointment on the public calendar
   widget as a "Real-World Transaction," which is a Claude Code sandbox setting, not a GHL
   permission. If you want future GHL terminal runs to be able to complete live verification
   passes (real test bookings, real Form E submissions), you may need to adjust that permission in
   Claude Code settings; otherwise these verification steps will need to be run manually by you.
4. Confirm it's OK that "Audit: prep email" is now Published (it was Draft through Run BQ/BS) --
   was that an intentional publish, or should it be checked against what else might have shipped
   unexpectedly?
5. The test contact ZZTest (david+zzbvclient@atlasonesolutions.com, tag client-current, id
   U3ATtLoT75j68zEZjlqX) is sitting in the account, untested; delete it whenever convenient or
   reuse it once you can run the booking tests yourself.
