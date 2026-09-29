# RESUME (2026-09-28): Run CN part 2. Jobs 0 and 1 are DONE and checked by Cowork. Do NOT redo them.
Do, in this order: Job G (Dr. Gould drafts, below, FIRST), then Job 6 (finish owner identity), Job 2 (Form D, continue from the structure map in the part 1
report, which is backed up to _to_delete/superseded-2026-09-28/run-cn-part1-report/ before you overwrite
RUN-GHL-report.md), Job 4, Job 3, Job 5. Log to TERMINAL-GHL-live.md as "Run CN part 2".

David's answers to part 1's questions:
1. Lead Source: use the existing option "Website Form" in "Website booking: source" (add an Update contact field
   action, Lead Source = Website Form, after the tag). Do not add a new picklist option.
2. Notification Email: David turns it off himself. Your first step stays the read only check of David's and
   Charity's Notification Settings. If any Email box is still ON, you may turn it OFF (never ON), save, reopen
   and screenshot. That is the only change allowed on that screen.
3. Form D: continue directly from your structure map. No review needed.

## Job G (FIRST): Dr. Gould invoice, agreement and products. DRAFTS ONLY, SEND NOTHING.

Source of truth: `A1_Sales/Dr Gould Dental/Dr_Gould_GHL_Invoice_and_Agreement_Setup_2026-09-28.md` (read it).
David decided 2026-09-28: the $495 Professional setup is WAIVED (this replaces the 09-26 decision to charge it).
Contact: Dr. Joel Gould, drjoeldgould@gmail.com; business "Joel D. Gould DDS, A Professional Corporation".

G1. Products (Payments, Products). Check first, create only what is missing, no other prices:
- Membership, Professional: $399 a month recurring (note setup $495 in the description). Reuse if it exists.
- Membership setup, Professional: $495 one time. Reuse if it exists.
- Bookkeeping with bill pay: $750 a month recurring. Description: "Monthly bookkeeping with bill pay (accounts
  payable). Accounts receivable not included, priced separately." (David confirmed this price 2026-09-28.)
- Payroll to books: this is the existing "Payroll to GL Converter: semi-monthly or bi-weekly" $75 a month and its
  $250 setup product. Do NOT create a duplicate; record the ids.
G2. The old draft INV-000002 (6ab802c4543c55f014bd6611, $894, setup charged) is now wrong. Do not delete it.
   Change only its title to "DO NOT SEND, replaced 2026-09-28" and Save. David deletes it himself.
G3. New invoice for Dr. Gould. Lines: Membership, Professional $399.00; Membership setup fee $495.00; a discount
   line or GHL "Add Discount" of $495.00 labeled "Setup fee waived"; total due $399.00. Terms: "ACH bank payment
   preferred, no fee." Processing fee OFF. Attach Dr_Gould_Professional_Membership_Inclusions_2026-09-28.pdf if the
   invoice screen allows attachments; if not, say so.
   Recurring monthly on the 1st starting October 1, 2026: use New Recurring Invoice ONLY if GHL lets you save it
   without scheduling or activating it. If saving a recurring invoice would schedule an automatic send, STOP that
   part: save a normal one time DRAFT invoice dated October 1 instead, and put the exact recurring setup steps in
   the report for David to click himself. Never click Send, Schedule or Activate.
G4. Agreement (Payments, Documents & Contracts). Find the membership agreement master in
   `A1_Sales/A1 Agreements/2026-09-15 masters/` (the files there are Atlas_One_Membership_Schedule.docx/.pdf and
   Sample_Proposal_Membership; if a file named "Atlas One Membership Agreement" exists anywhere in A1 Agreements,
   use that; otherwise use the Membership Schedule). Build it as a native text document (not a flat image), filled
   for Professional, $399 a month, $495 setup waived, with client and Atlas One signature fields and today's date
   field. Add the inclusions PDF as the itemized list (attach it, or paste its item list as a section if GHL
   documents cannot take an attachment). Attorney review: keep the flag INTERNAL. Name the draft
   "Dr Gould Membership Agreement (ATTORNEY REVIEW PENDING)" but do NOT print a review banner in the body the client
   signs. Save as draft. Never click Send.
G5. Report at the top: the link to each draft (invoice, agreement), every product id, and anything not done.

# BRIEF-GHL Run CN (GHL lane, installed 2026-09-27 after Cowork audited Run CM: PASS WITH GAPS)

Written 2026-09-27 by Cowork (chat A1 GHL how-to 2) from three queued notes written by other chats:
`BRIEF-GHL-queued-calendars-website-only.md`, `BRIEF-GHL-queued-insurance-form.md` and
`BRIEF-GHL-queued-contact-routing.md`. Those three stay where they are until this brief is installed, then move to
`_to_delete/superseded-<date>/briefs/`. Run CM was already running when they landed, so they wait for this run.

Terminal name: GHL. Model: Sonnet 5. GoHighLevel browser at app.ridethehightide.com, one visible tab, plus the
disk. No questions mid run; batch them at the end. Log to `_BUILD-LOG/TERMINAL-GHL-live.md`, finish with
`_BUILD-LOG/RUN-GHL-report.md` (move the Run CM report to `_to_delete/superseded-<date>/run-cm-report/` first).
Commit after each job, only this run's own files. Screenshots to `_briefs/assets/run-CN/shots/`.
Dead UI rule: start at app.ridethehightide.com/, navigate inside the app, one low stakes click first, one Cmd+R
retry, then stop with "needs Chrome restart" at the top of the report.

## Hard stops
Never turn on any Email box in a user's Notification Settings (Settings, My Staff, user, Notification Settings). On
2026-09-27 Run CM's bulk assign flooded David's inbox with thousands of "assigned to me" emails because those boxes
had been switched on in Run CC Part 74; David turned Email off (In-App stays on). Before ANY bulk assign, bulk task
or bulk workflow enrollment, open each user's Notification Settings read only and confirm every Email box is off;
if any is on, stop that step and put it in the questions. First action of this run: that read only check for David
and Charity, with a screenshot of each.
No sends of any kind, never SMS, never the HIPAA feature, no deleting records, calendars, forms or workflows
(removing a calendar from a group, or a field from a form copy you made, is fine), no spending. Creating and
publishing the workflows and the calendar named below IS allowed. Never change the slug, name or URL of the
calendar "Atlas One 15 Minute Intro Call" (widget/bookings/atlas-one-15-minute-intro-call-hoswp).

## Job 0 (DO FIRST, urgent): assign the Owner before any intake email

Cowork's Run CM audit found a live defect. "Intake: Instant reply" now sends with From Name
`{{user.name}}, Atlas One Solutions` and From Email `{{user.email}}`, but a brand new form lead has no Owner for
15 minutes ("Owner: default to David" waits 15 minutes), so the instant reply goes out with a blank name and
blank sender. Fix: at the very top of each of these workflows, before any other action, add "Assign to user",
David Taylor, "Only apply to unassigned contacts" ON, then the top level Save workflow button:
Intake: Instant reply; W1 Inbound speed to lead; Intake: Send bookkeeping form; Intake: document build;
Intake: service sign up; Audit: intake received; Tool-Lead Nurture; and the new "Intake: insurance quote" when
you build it in Job 2. Reopen each fresh and screenshot the first action. No bulk action in this job.

## Job 1: the 15 minute intro calendar becomes website only

David ruled 2026-09-27: every booking on the intro calendar means the BRJ website sent it. Today the group "Book
time with David" (widget/groups/book-david, the link in every signature) also contains it, so signature bookings
land there too.

a) Settings, Calendars. Open "Atlas One 15 Minute Intro Call" and record its settings (duration, Zoom location,
   availability, confirmation and reminder settings, form, redirect, widget colour). Screenshot each tab.
b) Create a new calendar "Quick call with David", 15 minutes, copying every one of those settings (Zoom, hours,
   form "Atlas One - Intro call booking" with the Promo code box, periwinkle #788DE3 widget, same redirect). Put it
   in the group "Book time with David".
c) Remove "Atlas One 15 Minute Intro Call" from the group "Book time with David" (group membership only; the
   calendar itself stays live and unchanged).
d) Booking workflows that filter on the calendar group ("Booking: confirm and remind" and any other trigger that
   says In calendar group is "Book time with David"): add a second trigger on the same event with
   In calendar is "Atlas One 15 Minute Intro Call", so website bookings still get the confirmation, reminders and
   after call emails. Check "Booking: after the call" (it filters "Showed, 15-Minute Intro Call") and add
   "Quick call with David" there as well. Save each.
e) New workflow "Website booking: source". Trigger Customer Booked Appointment, In calendar is "Atlas One 15 Minute
   Intro Call". Action: Update contact field Lead Source = Website (record the exact source field used) and add tag
   `website-booking` (create the tag). Nothing else. Publish.
f) Proof: open the group booking page https://api.leadconnectorhq.com/widget/groups/book-david and screenshot that
   it offers the new Quick call and no longer the intro call. Do not book.
g) Hand off: write the new calendar's public booking link at the top of the report, and append one line with it to
   `_BUILD-LOG/BRIEF-GHL-JOBS-queued-runCP.md` (GHL-JOBS sweeps the 53 Atlas One files that use the intro link;
   the blog pages, templates.html and the other BRJ website pages keep the intro link) and to
   `_BUILD-LOG/BRIEF-PORTAL.md` under a "Queued from GHL" heading (Book a call page).

## Job 2: Form D, Business Insurance Quote Request

Today insurance only prospects must fill Form A (42 elements). Build a short insurance form.

Build method (Claude Code's browser cannot drag): in Sites, Forms, duplicate "Atlas One — PEO / Prospect Quote
Request" and rename the copy "Atlas One — Business Insurance Quote Request". Remove from the COPY everything that is
not insurance or contact or company (payroll, benefits, census, services checklist, signature if not needed). Never
touch the original Form A. Then add missing fields by clicking them in the field list (GHL appends them); if a
field can only be placed by dragging, leave it where GHL puts it and list it in the report for David.

Fields, one page with reveals:
- Company: legal name, DBA, FEIN, address, website, industry, states operated, years in business.
- Contact: first and last name, title, phone, email, best way to reach you.
- Lines wanted (multi select, required): Workers comp, General liability, BOP, Property, Commercial auto, Cyber,
  EPLI, D and O, Professional or E and O, Umbrella, Bonds, Other.
- Reveals: Workers comp picked shows states, annual payroll by class if known, employee counts, current carrier and
  expiration. Commercial auto shows number of vehicles and drivers (keep the vehicle table from Form A if it came
  across). Property shows location count and values.
- Uploads: current dec pages, loss runs (last 3 to 5 years), payroll report.
- Renewal date per line (one date box per line, revealed with the line), and "Anything you want us to fix?".
- The same two SMS consent boxes as Form A. No HIPAA question.
Style: same header logo and colours as Form A. Save, Preview, screenshot top to bottom at phone width.

Routing:
- Add the new form as a trigger on "Intake: Instant reply" and on "W1 Inbound speed to lead" (same filter style as
  Form A and B). Save.
- New workflow "Intake: insurance quote". Trigger Form Submitted, this form. Actions: add tag
  `insurance-quote-request` (create it); Internal Notification to the contact's assigned user and to
  david@atlasonesolutions.com, subject "Insurance quote request: {{contact.name}}"; Create Opportunity in the
  pipeline whose name covers insurance (record which; if none exists, create pipeline "Insurance" with stages
  Inquiry, Gathering info, Quoting, Proposal sent, Bound, Lost, and say so), stage the first one, name
  "{{contact.company_name}}, insurance"; task to the assigned user "Call about insurance quote" due in 1 business
  day. Publish.
- Test without sending: submit the form once as "TEST Insurance Form" (email test-insurance@atlasonesolutions.com,
  no phone, Workers comp and GL picked, one small test PDF uploaded). Confirm tag, opportunity and task appear.
  Run this test BEFORE adding the form to "Intake: Instant reply" and W1, so no email goes out; add those two
  triggers after the test passes. Then remove the tag from the test contact. Leave the contact.
- Put the form id, share link and field keys at the top of the report. Append one line to
  `_BUILD-LOG/BRIEF-GHL-JOBS-queued-runCP.md`: form id for the /insurance/ redirect on forms.atlasonesolutions.com
  and the COMMAND Forms and intake card.

## Job 3: form field keys for the Scan ID tool

For every live form (A, B, D, Service Sign Up, Build This For Me, Audit intake, Onboarding documents, Intro call
booking), record the URL parameter key GHL uses for first name, last name, address, city, state, postal code and
date of birth (open the field's settings, "Query key" or the field key). Test one: open Form A's share link with
`?first_name=Test&last_name=Key` and screenshot that the boxes fill. Add a section "Prefill a form from a link" to
`Master_Kit/GHL How-To/GHL-How-To-Admin-Guide.md` with a table (form, field, key) and one example link.

## Job 4: replies go to the owning rep

GoHighLevel only sees email that comes back into its own Conversations (replies to email GHL sent). Mail sent
straight to the contact@ alias lands in David's Microsoft 365 mailbox and never reaches GHL; that half belongs to
the EMAIL lane (`BRIEF-EMAIL-queued-contact-routing.md`). Build only the GHL half:
- In "W6 Suppression and caps" (trigger Customer Replied), find its Internal Notification. Set the recipient to the
  contact's assigned user and keep David as a second recipient. If the contact has no assigned user GHL falls back
  to David; confirm that by reading the option text, and record it. Also set its "#1 Task: read and respond" to the
  assigned user.
- Record in the report: whether GHL's "Customer Replied" also fires for inbound email that is not a reply
  (read the trigger's help text only).

## Job 5: update the how-to guides and rebuild

In both `GHL How-To/GHL-How-To-Rep-Guide.md` and `GHL-How-To-Admin-Guide.md`: the "Book 15 minutes" row now points
reps to the new Quick call link (the intro calendar is website only); add Form D to the forms tables and to the
Rep Guide's form list; add the new tags `website-booking` and `insurance-quote-request` to the Admin Guide's tag
tables; add "Intake: insurance quote" and "Website booking: source" to the workflow list. Plain words, no dashes as
punctuation. Rebuild: `python3 "_BUILD-LOG/ghl-howto-src/build.py"`, screenshot both at phone width.

## Job 6: finish Run CM Job 2 (owner identity), carried over

Run CM fixed all 35 templates on disk (`_BUILD-LOG/cadence-emails-2026-09-13/` and
`_BUILD-LOG/p-templates-2026-09-23/`) but pasted only 4 into GoHighLevel (audit offer day 20 and 28, E0, 45-A)
and set From fields on only 3 workflows (Intake: Instant reply, Call: not now, W2). Do the rest exactly as the
Run CM brief said (it is in `_to_delete/superseded-2026-09-27/briefs/BRIEF-GHL-runCM.md`, Job 2):
a) Paste the other 31 templates from disk with the stray ">" check (click the last rendered line, End, check,
   Backspace only if a ">" follows the closing tag), Save, preview on a contact owned by David. List each.
b) Set From Name `{{user.name}}, Atlas One Solutions` and From Email `{{user.email}}` on every Send Email action in:
   Audit: offer follow up, Intake: Send bookkeeping form (inline Email 2B: also replace David's name and email in
   its text with the merge fields), Send PEO form on tag, Send bookkeeping form on tag, Intake: document build,
   Intake: service sign up (all 10 branches), Tool-Lead Nurture, W1, W3, W3a, W4, W5, Won: Pay Referral Partner.
   Top level Save workflow after each, reopen fresh to confirm.
c) Run CM Job 2d: in those workflows plus Call: not now and W2, Internal Notifications go to the assigned user AND
   David; tasks go to the assigned user. List any action that cannot.
d) "The $70,000 audit (construction)" inline email in Call: not now: replace the typed signature (David Taylor,
   his email, 385-213-7177) with `{{user.name}}`, `{{user.email}}`, `{{user.phone}}`; keep every other word and the
   formatting. Screenshot before and after. If the rich text editor fights you, stop on this one item and say so.
Booking workflows and W7 stay David. No sends.

## Report must include
The new calendar link and group proof, every workflow saved with the time, Form D id, link, field keys and the test
result, the prefill key table, the W6 notification change, the guide lines changed. Questions batched at the end.
