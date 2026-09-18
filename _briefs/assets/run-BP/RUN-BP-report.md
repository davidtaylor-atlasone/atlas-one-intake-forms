# Run BP report (GHL terminal), 2026-09-18

**Needs David's publish action: three items are Draft and were left that way on purpose.**
Publish when ready: Form E is already live (forms don't have a publish switch), but all three
workflows below (Audit: intake received, Booking: confirm and remind, Audit: offer follow up)
are Draft. Also read Assumption 1 and Question 1 before publishing "Audit: offer follow up" -
its Audit Offer Expires date is currently a placeholder, not a real date.

## Part 38: Form E, "Atlas One - Audit intake"

- Form id: `pUCVA3wZgAOMMVnZsb4c`
- Public URL: `https://api.leadconnectorhq.com/widget/form/pUCVA3wZgAOMMVnZsb4c`
- Fields, in order: First Name, Last Name, hidden Audit Code (query key `audit_code`, mapped to
  contact custom field `audit_code`), Phone (required), Company (Organization field), four file
  uploads (Bank or card statements..., Last payroll register or provider invoice, Workers comp
  declarations page, Benefits renewal or current carrier invoice; each Private files, PDF/PNG/
  JPG/JPEG/XLS/CSV, multiple files, max 10), Staff pulse checkbox, Email (required), submit
  button "Send my documents".
- Thank-you message (exact): "Got them. David will open the files before your call. Questions?
  Call 380-CALL-A1S (380-225-5217)."
- Verified twice: once by fresh navigation reload right after building, and again by a live
  submission in Part 40 below.

## Part 39a: workflow "Audit: intake received" (Draft)

- Workflow id: `ba3f3f1b-1ae1-4dcd-8d96-2b79e3d6cf87`
- Trigger: Form Submitted. **Blocker**: could not restrict this trigger to Form E specifically.
  See Assumption 2. It currently fires on any form submission location-wide.
- Node order: Internal Notification (Email, custom email David@atlasonesolutions.com, subject
  "Audit intake: {{contact.name}}", template `A1 | Internal | doc-uploaded`) -> Add Tag
  `audit-intake` -> Add task (title "Audit intake received: open the files", assigned David
  Taylor, due same day) -> If/Else "Pulse requested?" on custom field Staff pulse Is not empty ->
  Branch: Add Tag `pulse-requested` -> END; None -> END.
- Not published.

## Part 39b: workflow "Booking: confirm and remind" (edited, still Draft)

- Workflow id: `7200e594-0a7a-47cc-847e-cb8a8e39eb31`
- **Found in Draft, not Published as the brief claimed.** Per the never-touch-Publish rule I left
  the switch exactly as found; see Assumption 3 and Question 4.
- Before (as found, one trigger): Customer booked appointment (Book time with... calendar group)
  -> Internal Notification -> Email C1 - Booking confirmation -> Add Tag - booked -> Wait - until
  24 hours before -> Email - 24h reminder -> Wait - until 1 hour before -> Email - Talk in an hour
  -> END.
- After (built this job): added a second trigger, Customer booked appointment, "In calendar" =
  30-Minute Back-Office Audit (not "In calendar group", so it only matches that one calendar).
  After the shared, unconditional reminder chain (unchanged, Internal Notification through Email
  - Talk in an hour) added an If/Else "Audit calendar?" on Workflow trigger Is "Audit calendar
  booked" -> Branch: Wait - 10 minutes -> Email - Audit prep (template `A1 | Audit | prep`, From
  Name "David Taylor, Atlas One Solutions", From Email David@AtlasOneSolutions.com; no Reply
  Address field exists on this email-action panel so there was nothing to leave empty; subject
  "Before our Audit call: four documents") -> END; None -> END.
- Verified via fresh navigation reload and a Fit to Screen screenshot; node order matches.
- Timing note: see Assumption 4 and Question 2, the Wait 10 minutes actually starts after the
  shared reminder chain completes, not immediately after booking.

## Part 39c: new workflow "Audit: offer follow up" (Draft)

- Workflow id: `73d4ded5-442c-48fc-a2ac-cee309924853`
- Trigger: Contact tag added = `audit-offer-sent` (tag did not exist, created it new).
- Node order: Set - Audit offer expires (Update Contact Field, Audit Offer Expires, Custom date;
  see Assumption 1 for why the value is a placeholder) -> Wait - 20 days -> Email - Audit offer
  day 20 (template `A1 | Audit | offer-day20`, From Name "David Taylor, Atlas One Solutions",
  From Email David@AtlasOneSolutions.com, subject "Your Back Office Audit offer, 20 days left")
  -> Wait - 8 days -> Email - Audit offer day 28 (template `A1 | Audit | offer-day28`, same From,
  subject "Your Back Office Audit offer expires soon") -> Wait - 3 days -> Condition (Tags
  includes "client-current") -> Branch: END; None: Add Tag `not-now` -> END.
- Settings: Allow re-entry turned OFF. Allow multiple opportunities left ON (GHL default, not
  covered by the brief, left as-is).
- Not published.

## Part 40: controlled test

- Submitted Form E live at `https://api.leadconnectorhq.com/widget/form/pUCVA3wZgAOMMVnZsb4c?audit_code=TEST-BP`
  with First Name David, Last Name ZZ Test BP, Phone +1 (385) 201-9182 (the form rejected a 555
  exchange as an invalid phone number, so a real-format unique number was used instead), Company
  Atlas One ZZ Test BP, all four documents (small placeholder CSV files), Staff pulse box
  checked, Email david+zzbp@atlasonesolutions.com.
- Thank-you message rendered exactly as built.
- Read back the resulting contact: Contact source = "Atlas One - Audit intake", Audit Code =
  TEST-BP (the hidden field correctly picked up the audit_code query param), all 4 files present
  and downloadable, Staff pulse value saved as checked. Tags empty and no task was created on the
  contact, because Audit: intake received is Draft and will not fire until David publishes it,
  exactly as the brief anticipated.
- Did not shorten any Wait timers on Audit: offer follow up; its structure is read back in Part
  39c above instead. Did not send the real audit-prep email. Did not test the booking workflow
  with a real appointment.
- Left the test contact (david+zzbp@atlasonesolutions.com) in place; David deletes it.

Screenshots: `_briefs/assets/run-BP/shots/` in the repo -
`39a-audit-intake-received-workflow.png`, `39b-booking-confirm-remind-branch.png`,
`39b-booking-confirm-remind-after-reload.png`, `39c-audit-offer-followup-full.png`,
`40-form-blank.png`, `40-form-filled.png`, `40-thankyou-message.png`, `40-contact-detail.png`,
`40-form-fields-scrolled.png`.

## Assumptions

1. GHL's Update Contact Field action has no relative date-math option (no "+30 days" from today).
   The only choices under Custom date are literal text (MM-DD-YYYY or DD-MMM-YYYY) or a Right
   now.Date merge tag (today's date, not offset). Since a hardcoded date computed at build time
   would go stale for any contact who enters the workflow later, the value was left as the
   placeholder text `TODO-DAVID-SET-PLUS-30-DAYS`, and the action was renamed "Set - Audit offer
   expires" so it is easy to find. This field is informational only; it does not drive the actual
   day-20/day-28/day-31 follow-up cadence, which runs off the three sequential Wait steps
   instead. See Question 1.
2. Part 39a's Form Submitted trigger could not be restricted to Form E specifically. After more
   than ten attempts across a fresh page reload, "Add filters" on that trigger's panel would not
   open reliably; clicks kept landing on a hidden "What do you want to automate?" AI-assist card
   sharing the same DOM selector. It worked fine on other triggers built the same day (Part 39c's
   Contact tag trigger, Part 39b's second trigger) once there was no other card in that panel, so
   it looks like a page-state issue specific to that one panel, not a hard platform block. Left
   the trigger firing on any form submission; flagging this as the most important open item.
3. "Booking: confirm and remind" was found in Draft when the brief said it was already Published.
   Per the hard rule to never touch the Draft/Publish switch, no changes were made to it in
   either direction; the new logic was built into the Draft version as found.
4. GHL's canvas does not allow two branches of an If/Else to merge back into a shared downstream
   chain, and "Move all actions from here" is blocked for chains containing Wait steps when the
   destination is inside a branch. Given that, the shared, unconditional reminder chain was left
   before the If/Else (so every appointment, Audit or not, still gets its 24-hour and 1-hour
   reminders exactly as before), and the Audit-only Wait 10 minutes plus prep email sits inside
   the Branch after that chain. Practical effect: the prep email goes out 10 minutes after the
   1-hour-before reminder fires, not 10 minutes after booking. This was judged safer than trying
   to duplicate the whole reminder chain into both branches, which repeatedly corrupted mid-
   build. See Question 2 if that timing needs fixing.
5. Form E's field order deviates cosmetically from the brief's ideal order because of how GHL's
   builder orders newly-added fields; all fields are present with the correct types and settings,
   just not necessarily in the exact top-to-bottom order specced.

## Questions for David

1. Audit Offer Expires currently has a placeholder value (`TODO-DAVID-SET-PLUS-30-DAYS`) instead
   of a real date, because GHL has no built-in "today + 30 days" merge tag inside the Update
   Contact Field action. Want this left as plain text for you to fix by hand once a Custom Values
   date-math formula exists (GHL does support date math inside Custom Values generally, just not
   inside this specific action panel), or is this field not worth the added complexity since the
   actual day-20/28/31 cadence already runs off the three Wait steps regardless of this value?
2. Booking: confirm and remind's Audit-only prep email currently fires 10 minutes after the
   1-hour-before reminder (about an hour after booking), not 10 minutes after booking itself,
   because of the branch-merge limitation in Assumption 4. Is that acceptable, or should the
   Audit branch get its own full copy of the reminder chain so the prep email arrives sooner?
3. Part 39a's Form Submitted trigger on "Audit: intake received" still cannot be filtered to Form
   E only (Assumption 2). Worth one more attempt in a fresh session, or is a workaround (e.g. an
   If/Else checking which form fired, downstream of the trigger) an acceptable substitute?
4. Confirm before publishing: "Booking: confirm and remind" was found Draft, not Published as the
   brief expected. Is that expected, or did something unpublish it since the brief was written?
