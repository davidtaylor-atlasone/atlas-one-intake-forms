# BRIEF-GHL (Run CM, 2026-09-26): workflow emails speak as the contact's Owner, every contact gets an Owner, new products, Trigger Links, how-to fact check

Terminal name: GHL. Model: Sonnet 5. GoHighLevel browser at app.ridethehightide.com, one visible tab, plus the
disk. No questions mid run; batch them at the end of the report. Log to `_BUILD-LOG/TERMINAL-GHL-live.md`,
finish with `_BUILD-LOG/RUN-GHL-report.md` (move the Run CL report sitting there to
`_to_delete/superseded-2026-09-26/run-cl-report/` first). Commit after each job, only this run's own files.
Screenshots to `_briefs/assets/run-CM/shots/`.

Written by Cowork (chat A1 GHL how-to 2) after auditing Run CL (`_BUILD-LOG/COWORK-AUDIT-run-CL-2026-09-26.md`).
David approved this plan by starting the run. Facts the plan rests on: `_BUILD-LOG/ghl-howto-facts-2026-09-25.md`
(41 workflows, sections a to e, and Job 6c: the User merge fields, From Name and From Email accept merge
fields, no Reply To field on the Send Email action).

Dead UI rule applies: start at app.ridethehightide.com/, navigate inside the app, one low stakes click first,
one Cmd+R retry, then stop with "needs Chrome restart" at the top of the report.

## Hard stops (this run)
No sends of any kind (no test emails, no "send test"), never enable SMS, never the HIPAA feature, no deleting,
no spending, never Connect or Disconnect on QuickBooks or Stripe. Do NOT assign any contact to Charity Taylor
in this run (her GHL email is unverified and her Microsoft 365 mailbox does not exist yet, so replies would
bounce). Editing and saving published workflows IS allowed in this run, only for the edits listed below.
Never touch W7 WSA handoff (Cornerstone) or the P-W7-1, 2, 3 templates.

## Job 1: every contact gets an Owner (do this first; the merge fields are blank without it)

About 2,142 of 2,155 contacts have no assigned user. A workflow email that uses `{{user.name}}` on an
unassigned contact prints blank.

a) Settings, My Staff, Charity Taylor, Roles and Permissions: record (read only) whether "only assigned data"
   is on and whether GoHighLevel assigns a contact to the user who creates it. Screenshot. Change nothing.
b) Create workflow "Owner: default to David". Trigger: Contact Created (no filter). Action 1: Wait 15 minutes
   (gives a rep time to set themselves as Owner). Action 2: Assign to user, David Taylor, with "Only apply to
   unassigned contacts" ON (record the exact option name GHL shows). No email, no notification.
   Allow re-entry OFF. Save, Publish.
c) Backfill: Contacts, filter Assigned (Owner) is empty. Record the count. Select all, bulk action "Add to
   workflow", pick "Owner: default to David" (this skips the 15 minute wait only if GHL offers "start at step";
   if not, the wait is fine). Record the count before and 30 minutes after; the after count must be 0 or tell
   us why not. If GHL offers a native bulk "Assign" action instead, use that and say so.
d) Proof: open 3 random formerly unassigned contacts and screenshot Owner = David Taylor.

## Job 2: prospect emails speak as the Owner

### 2a. Templates on disk first (the disk is the master)
Source folder `_BUILD-LOG/cadence-emails-2026-09-13/` plus the P- template source used by Runs CH/CJ/CK
(find it through `_BUILD-LOG/email-templates-map.md` and the Checkpoint 2 report it names). Make a copy of the
folder to `_to_delete/superseded-2026-09-26/cadence-emails-pre-runCM/` before editing.

In the templates listed in 2c ONLY:
- Sign off line: `David` becomes `{{user.first_name}}`.
- Signature block (the table with David Taylor, the phone and David@AtlasOneSolutions.com): replace the name
  with `{{user.name}}`, the email text and its mailto with `{{user.email}}`, and the direct phone with
  `{{user.phone}}`. Keep the 380-CALL-A1S (380-225-5217) company line and support@atlasonesolutions.com as they
  are. Keep the layout and colors. If a template uses GoHighLevel's `{{user.email_signature}}` more simply,
  do NOT switch to it; keep the branded block with the three user fields.
- Body text saying "I" stays "I". Any body line naming "David" by name (for example "David will call you")
  becomes `{{user.first_name}}`.
- Bookings stay David's: in any template in the list that links to "Book time with David" or says "book with
  David", leave the booking link as is (it is David's calendar group) and change only the words to "book a
  time".
- Run the dash guard: zero em or en dashes in any changed file.
Record a before and after diff per file in the report (lines changed only).

### 2b. Paste into GoHighLevel
For each changed template: open it in Marketing, Emails, Templates, replace the source with the disk file, then
Cmd+End and confirm the source ends exactly as the disk file does (the stray ">" rule at the top of
email-templates-map.md). Save. Use the template's own Preview (with a contact, if offered) on a contact whose
Owner is David and screenshot that the signature shows David Taylor, David's email and 385-213-7177. No send.

### 2c. Which workflows and templates change
Change (Send Email actions: From Name `{{user.name}}, Atlas One Solutions`, From Email `{{user.email}}`;
templates as in 2a):
- Audit: offer follow up (audit-offer-day20, audit-offer-day28)
- Call: not now (e0, 45-a, 45-b, 45-c, and the inline "The $70,000 audit (construction)" email; for the inline
  one edit its text in the action)
- Intake: Instant reply (intake-instant-reply)
- Intake: Send bookkeeping form (the inline Email 2B: edit its text and From in the action)
- Send PEO form on tag (new-client-welcome), Send bookkeeping form on tag (send-bookkeeping-form)
- Intake: document build (confirm-document-build), Intake: service sign up (confirm-service-signup, all 10
  branches share one template; set From on all 10 actions)
- Tool-Lead Nurture (tool-lead-nurture-1, tool-lead-nurture-2)
- W1 Inbound (P-C-2, P-C-3), W2 Warm referral (P-A-1, P-A-2, P-A-3), W3 Trigger sequence (P-B-1 to P-B-4),
  W3a Renewal calendar (P-B-120, P-B-60), W4 Cold cadence (P-D-1 to P-D-4), W5 Lost deal (P-E-0, P-E-4,
  P-E-Q1, P-E-Q2, P-E-Q3). For P- actions that use template defaults with no From set, set From Name and From
  Email on the action.
- Won: Pay Referral Partner (won-email-6, won-email-7-checklist)

Leave as David (no change): Booking: confirm and remind, Booking: after the call, Booking: client services
email, Audit: prep email (they are about a call on David's calendar), every draft workflow, W7 WSA handoff.

### 2d. Notifications and tasks follow the Owner
In the changed workflows, every Internal Notification that goes to a fixed David address: switch the recipient
to the contact's assigned user AND keep David as a second recipient (so nothing he gets today stops). Every
task action: set "Assign to" to the contact's assigned user if the option exists (record the option name).
Where an action cannot do this, leave it and list it.

### 2e. Proof without sending
For 3 workflows (Intake: Instant reply, W2, Call: not now), open one Send Email action and screenshot the From
Name and From Email fields showing the merge fields. Open the workflow's Execution Logs or Enrollment History
for the most recent real contact (read only) and record what the From name resolved to, if GHL shows it. List
every workflow saved, with the time.

## Job 3: new products (from `_BUILD-LOG/BRIEF-GHL-queued-products.md`, prices from prices.json V8)

Payments, Products, Create Product. Re-read `_INTERNAL (do not share)/tools/agreements/prices.json` first and
use its numbers if they differ from these. Type Service. Description in plain words, no vendor names.
- Payroll to GL import, run by Atlas One: $35 per payroll run (one time price, quantity per run).
- GL import plus certified payroll setup (bundle): $300 one time.
- Safety training program setup: $295 one time.
- Safety training program, up to 25 employees: $79 a month. 26 to 75 employees: $129 a month.
- COI tracking setup: $150 one time. COI tracking done for you: $49 a month (up to 15 subs), $99 (up to 50),
  $149 (up to 100).
Do not create Connecteam (no list price on file), and do not load the five COI notice templates (they need
per contact fields first). Screenshot the product list after. Record each product id.

## Job 4: Trigger Links for the forms

Marketing, Trigger Links (record the exact menu path). Create one per form, named exactly:
"Form A: PEO and quote request", "Form B: Bookkeeping", "Service Sign Up", "Build This For Me", "Audit intake",
"Onboarding documents", "Book 15 minutes". URLs are in Section 4 of
`Master_Kit/GHL How-To/GHL-How-To-Admin-Guide.md` (the booking one is
https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp). No actions attached
(tracking only). Then open a contact's email composer, Insert Link, Trigger Link, and screenshot the list
showing all seven. Discard the draft.

## Job 5: check the how-to guides against the live screens and fix them

The guides were written from the facts file. Verify these lines on the live screens (read only) and edit both
`GHL How-To/GHL-How-To-Rep-Guide.md` and `GHL-How-To-Admin-Guide.md` wherever the screen differs, in plain
words, no dashes as punctuation:
1. The exact label of the Owner box on a contact's detail page (Owner or Assigned to) and where it sits.
2. The exact pipeline names and their first stage names (all 6 pipelines).
3. Whether an estimate has a "convert to invoice" action once accepted, and its exact name.
4. The Recurring Invoice screen: the schedule fields.
5. The "only assigned data" permission name used when adding a user.
6. The service- tag each Service Sign Up branch actually adds (the facts say "the branch name"; the tag list
   says service-ai-email and so on).
7. Replace the "Named Trigger Links are being set up in Run CM" line in both guides with the steps from Job 4.
8. Replace "Once Run CM is finished" wording in the Admin Guide with the finished state.
Then rebuild the two HTML guides: `python3 "_BUILD-LOG/ghl-howto-src/build.py"` from the Master Kit folder
(read its header; it writes the HTML beside the .md files). Open each HTML at phone width and screenshot.

## Report must include
Job 1 counts before and after and Charity's permission facts. Job 2 the template diff list, the workflow list
with save times, and the three proof screenshots. Job 3 product ids. Job 4 the Trigger Link list. Job 5 every
guide line changed. Questions batched at the end.
