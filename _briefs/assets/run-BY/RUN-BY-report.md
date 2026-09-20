# RUN-BY report

**A "Something else" booking now gets nothing extra, proven from the workflow's Execution log condition trace (not the canvas): test contact ZZTest RunBY-NoTagB booked the 30-Minute Back-Office Audit answering "Something else" and, 13+ minutes later, has received only the booking confirmation email — no prep email, no client services email. David has nothing to publish from this run: both edited workflows (Audit: prep email, Booking: after the call) were left exactly as the brief required (Published / Draft, publish toggle never touched).**

## Part 63: stop "Something else" bookings getting the Audit prep email

Widened the existing "Client?" condition in Audit: prep email (`f9162dd7-692e-4f91-80af-76c4d034ccb6`, Published) by adding a third segment, joined by OR with the existing two:

- Segment 1: Tags includes `client-current`
- Segment 2: Call purpose Is "I am already a client"
- Segment 3 (new): Call purpose Is "Something else"

Renamed the branch from "Client" to "Skip prep email?" (the panel allowed the rename). Saved the action, then had to click the top-level workflow Save too — a red dot appeared on Save after closing the action panel, confirming an unsaved change existed at the workflow level as well (same lesson as Run BX Part 59, and it applies here too even though this is the same workflow). Verified via fresh navigation (root → Automation → Workflows list → reopen row): the condition panel showed all three segments and both OR joiners after reload, and the branch card on the canvas read "Skip prep email? / +2 other segments". Publish toggle was never touched; the workflow remains Published.

**Assumption 1 (numbered):** the brief said "rename it if the panel allows"; it did allow it, so the branch is now named "Skip prep email?" rather than left as "Client".

## Part 64: close the gap in "Booking: after the call" before it goes live

Added a fourth segment to the "Next step already sent?" gate in Booking: after the call (`d928c199-70af-4134-9bc2-000cfe7d2b30`, Draft):

- Segment 4 (new): Tags Includes `audit-offer-sent`, joined by OR with the existing three (`form-a-sent`, `form-b-sent`, `proposal-sent`)

The add-segment control defaulted the new segment's joiner to AND; had to explicitly change it to OR to match the brief. Saved the action. This workflow's top bar showed a plain "Saved" state with no extra top-level Save button required (unlike the Published workflow in Part 63) — Draft workflows appear to commit on the action save alone.

Verified via fresh navigation reload: all four segments present, correctly OR-joined, in the reopened condition panel. Left Draft; the Publish toggle was never touched, per the brief David publishes it himself.

**Assumption 2:** the canvas summary chip under the branch reads "+1 other segments" both before and after the reload, even though the opened panel shows the true count (4 segments: 3 existing + 1 new). This is a cosmetic display quirk in this GHL build (the canvas preview text does not always recompute after an edit) — the underlying saved condition is correct, confirmed by opening the panel itself, not by trusting the summary chip. Flagging so David isn't alarmed if he notices the same mismatch.

## Part 65: rename the 15 Minute Intro Call calendar off its em dash

Renamed the calendar "Atlas One — 15-Minute Intro Call" (id `qLdAzkruMQmYDn2ZT3UM`) to "Atlas One 15 Minute Intro Call" via Calendars → Meetings → Calendars → edit (pencil) → Basic details → Calendar name field.

Confirmed before saving that the Custom URL slug (`atlas-one-15-minute-intro-call-hoswp`) was untouched by the rename — renaming the display name does not change the slug in this builder, so the booking link in the email signature and on the website is unaffected. Did not touch the slug, availability, team members, or any other setting on this calendar, and did not touch the other three calendars (the "Atlas One — 15-Minute Strategy Session" calendar still carries its own em dash — out of scope per the brief, which named only the Intro Call calendar).

Verified via fresh navigation reload (root → Calendars → Calendar settings): the row now reads "Atlas One 15 Minute Intro Call" with the same calendar ID and an updated "Date updated" timestamp.

## Part 66: prove Parts 63 and 64

**Test (a) — PASSED.** ZZTest RunBY-NoTagA (david+zzbynotaga@atlasonesolutions.com, (385) 201-9190, no tag) booked the 30-Minute Back-Office Audit for Fri Sep 25 2026, 08:00–08:30 AM, answering "My Back Office Audit". Execution log condition trace for Audit: prep email: Segment 1 (client-current) = false, Segment 2 (I am already a client) = false, Segment 3 (Something else) = false → overall `Success(None)` → Wait 10 minutes → Email (Executed). Contact activity confirms: booking confirmation at 10:37 PM, then "Before our Audit call: four documents" at 10:47 PM (exactly 10 minutes later, matching the Wait step), tags only `booked`, no client services email. This proves Part 63's fix did not break the normal audit path.

**Test (b) — PASSED, the live proof of Part 63.** ZZTest RunBY-NoTagB (david+zzbynotagb@atlasonesolutions.com, (385) 201-9191, no tag) booked the same calendar for Wed Sep 30 2026, 11:00–11:30 AM, answering "Something else". Execution log condition trace for Audit: prep email: Segment 1 = false, Segment 2 = false, Segment 3 ('contact.call_purpose' is "Something else") = **true** → overall `Success(Skip prep email?)` → straight to "Removed by - End Of Workflow", with no Wait and no Email action ever executed. Contact activity, checked 13+ minutes after booking, shows exactly one message: the booking confirmation at 10:39 PM. No prep email, no client services email, tags only `booked`.

**Test (c) — Part 64, verified by read-back only.** No live test of Booking: after the call is possible without publishing it (it is Draft and has zero enrollments — publishing it to test would be a real, unrequested change to production). As stated in Part 64 above, the fourth segment (`audit-offer-sent`) was confirmed present and correctly OR-joined by reopening the condition panel after a fresh navigation reload. This satisfies Part 66(c) as instructed.

No sandbox permission-gate denials occurred anywhere in this run (unlike Runs BV/BW, which lost several tests to the Claude Code sandbox's own Real-World-Transactions classifier). Both bookings and every workflow edit went through cleanly.

## ZZTest contacts and test appointments — Runs BS through BY, for David to clear in one pass

| Run | Contact | Email | Phone | Tag | Appointment |
|---|---|---|---|---|---|
| BS | ZZTest RunBS-Client | david+zzbsclient@atlasonesolutions.com | (385) 201-9183 | client-current | 30-Min Audit, Sep 22 2026 |
| BV | ZZTest (Part 55, untagged before block) | david+zzbvclient@atlasonesolutions.com | (385) 201-9184 | client-current | none booked (sandbox blocked) |
| BX | ZZTest RunBX-Client | david+zzbxclient@atlasonesolutions.com | (385) 201-9185 | client-current | 30-Min Audit, Wed Sep 23 2026, 09:00 AM |
| BX | ZZTest RunBX-NoTagA | david+zzbxnotaga@atlasonesolutions.com | (385) 201-9186 | none | 30-Min Audit, Thu Sep 24 2026, 11:00 AM |
| BX | ZZTest RunBX-NoTagB | david+zzbxnotagb@atlasonesolutions.com | (385) 201-9187 | none | 30-Min Audit, Fri Sep 25 2026, 09:00 AM |
| BX | ZZTest RunBX-FormE | (Form E submission, no calendar booking) | — | audit-intake, audit-docs-received | none (form only) |
| BY | ZZTest RunBY-NoTagA | david+zzbynotaga@atlasonesolutions.com | (385) 201-9190 | booked | 30-Min Audit, Fri Sep 25 2026, 08:00 AM |
| BY | ZZTest RunBY-NoTagB | david+zzbynotagb@atlasonesolutions.com | (385) 201-9191 | booked | 30-Min Audit, Wed Sep 30 2026, 11:00 AM |

(Run BW's test contact from Part 57, id `q0huChHAaCHapvWnenZC`, and Run BX's `3rNOWopyxntI4Yg5j5qF` are the same-purpose client-current test bookings already listed above under their run labels where re-identified; earlier reports have the exact contact IDs if needed.)

## Assumptions

1. Renamed the Audit: prep email branch from "Client" to "Skip prep email?" since the panel allowed it — brief said to do this if possible.
2. The canvas summary chip under a branch ("+N other segments") can lag behind the true saved segment count after an edit in this GHL build; verified the real condition data by opening the panel, not by trusting the chip text. Applies to both Part 63 and Part 64's edits.
3. Left both edited workflows' Publish toggles untouched exactly as found (Published for Audit: prep email, Draft for Booking: after the call) — brief was explicit that David publishes Booking: after the call himself.
4. Booked test appointments on dates that don't collide with existing ZZTest appointments from prior runs (Sep 25 08:00 AM and Sep 30 11:00 AM were free slots) rather than reusing exact prior test dates.

## Questions for David

1. Now that Booking: after the call's gate has the fourth `audit-offer-sent` segment and reads correctly on a fresh reload, is there anything else you want checked before you publish it, or should the next run assume it's ready?
2. The canvas branch-summary chip ("+N other segments") appears to be a display-only quirk in this GHL build that doesn't reflect the true saved segment count after certain edits — worth reporting to GHL support, or is this already a known issue on your end?
3. Should the "Atlas One — 15-Minute Strategy Session" calendar (still carrying its own em dash) also be renamed, or is that one intentionally out of scope?
4. Eight ZZTest contacts and their test appointments (table above) are sitting live across the Sep 22–30 date range. Would you like these deleted/cancelled in one batch now, or held until a later cleanup run?
