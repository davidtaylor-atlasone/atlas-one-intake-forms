# BRIEF-GHL (current run: Run CL, 2026-09-26). Job 0 FIRST: WSA Scottsdale code and UTM tagging (at the bottom). Then the stray ">" fix, hiding unused fields, and the fact capture for the GHL how-to suite.

Terminal name: GHL. Model: Sonnet 5. GoHighLevel browser only, at app.ridethehightide.com, in one tab, with
the tab visible. No questions mid run. No sends (no test emails either), no publishing or unpublishing a
workflow, no deleting, no spending, never the HIPAA feature, never Connect on QuickBooks or a payment
provider. Log to `_BUILD-LOG/TERMINAL-GHL-live.md`, finish with `_BUILD-LOG/RUN-GHL-report.md` (back up the
Run CK report sitting there to `_to_delete/superseded-2026-09-25/run-ck-report/` first). Commit after each
job, only this run's own files. Screenshots to `_briefs/assets/run-CL/shots/`.

Written by Cowork (chat A1 GHL how-to) after auditing Run CK on disk and live
(`_BUILD-LOG/COWORK-AUDIT-run-CK-2026-09-24.md`). Dead UI rule applies: start at app.ridethehightide.com/,
navigate inside the app, one low stakes click first, one Cmd+R retry, then stop with "needs Chrome restart"
at the top of the report.

## Job 1: remove the stray ">" at the very end of five templates

Cowork read the live rendered copy of all 69 email templates. Exactly the five pasted by Runs CJ and CK end in
`</table>>`: one extra ">" after the last closing table tag, which shows as a visible ">" character at the
bottom of the email. Cause: Monaco auto closes a bracket when the full HTML is filled in. The 27 cadence
templates Run CH pasted are clean.

Templates: P-BUILDER-DELIVERY `6aa370697919774ef2ed8f30`, P-MEMBER-WELCOME `6aa37036a813792f409bf1a9`,
P-W7-1 `6aa0a9f855d1ce8973c141a2`, P-W7-2 `6aa0a9f955d1ce8973c141a8`, P-W7-3 `6aa0a9fb6ec737a976fa481f`.

For each: open it, go to the very end of the source (Cmd+End), delete only that one trailing ">", confirm the
source now ends in `</table>` exactly, Save template, confirm the Saved toast. Change nothing else. The W7
templates keep the Cornerstone identity (see the guard line in email-templates-map.md). Then re-open each
fresh and confirm the last characters of the source are `</table>` with nothing after.

Standing rule to add to `_BUILD-LOG/email-templates-map.md` (one line at the top): "After pasting HTML into
the Vibe Editor, press Cmd+End and check the source ends exactly as the disk file does before saving. Monaco
adds a stray > on fill."

## Job 2: hide every unused Contact, Company and Opportunity field

The list is already decided. Use `Master_Kit/GHL How-To/GHL-Hidden-Fields-List-2026-09-24.csv`: every row
with Action HIDE gets hidden, every KEEP row stays visible. 376 contact fields, 147 company fields, 0
opportunity fields. Nearly all are the old HubSpot import of 2026-09-03 plus a test folder (Field A, B, C).
Hiding only: never delete a field or a folder, and never edit a field's values.

Contacts: Contacts, three dots at the top right of the list, Settings, tab "Customize Contact detail view".
Create a view named "Atlas One standard view", hide the HIDE fields (hiding a whole folder is fine when every
field in it is HIDE; the CSV Folder id column groups them), keep the built in fields, save, and assign the
view to both users (David Taylor and Charity Taylor). If the screen lets you hide folders but not single
fields, hide only folders where every field is HIDE and list the mixed folders in the report.

Companies and Opportunities: find the equivalent hide control (company detail page settings, opportunity
card or detail layout). If one exists, hide the Company HIDE rows the same way (Opportunity has none to
hide). If GoHighLevel has no hide control for a record type, stop on that record type after one look,
screenshot where you looked, and report it. Do not thrash.

Proof: before and after screenshots of one real contact and one real company, with a count of the fields
visible on each before and after. Then edit `Master_Kit/GHL How-To/GHL-Hidden-Fields-List-2026-09-24.md`:
change the Status line to DONE with the date, and replace the "How to bring a hidden field back" section with
the exact clicks you used for Contacts, Companies and Opportunities, in plain words (which menu, which button,
what he sees when it worked). No build jargon, no dashes used as punctuation.

## Job 3: read only fact capture for the GHL how-to suite

Write everything to `_BUILD-LOG/ghl-howto-facts-2026-09-25.md`, with a screenshot for each screen named in
it. Change nothing.

a) Every workflow (41; the API list is in COWORK-AUDIT-run-CK-2026-09-24.md): name, Published or Draft, each
trigger with its filter (which tag, which form, which field), every tag an action adds or removes, every
Send Email action (template name, From name, From email, Reply to), every Assign to user action, every
Internal Notification. One table row per action is fine.

b) Every form and survey: name, share link, which workflow it triggers, whether it has a file upload.

c) The screens a person uses to enter records, as a new user would see them: Contacts, Add Contact (every
field shown and which are required); Companies, Add Company; Opportunities, Add opportunity (pipeline and
stage pickers, fields shown). How a contact is linked to a company. How an opportunity is linked to a contact.
Close each dialog without saving.

d) How a form is sent to a contact by hand: from the contact's page (Conversations, email, insert the form
link or a Trigger link) and whatever else GoHighLevel offers. Stop before Send and close.

e) The tags list (Settings, Tags): all 71 names. Cowork found four names that appear twice:
service-ai-task, service-cert-payroll, service-doc-build, service-other. For each pair record both ids, the
exact spelling (spaces, capitals) and whether any workflow uses each one. Do not delete or merge.

## Job 4: invoices, read only walkthrough

Payments, Invoices. Record: is a payment provider connected (which one, test or live mode), the invoice
settings (business name, logo, address, from email, number prefix, default terms, tax), the products list
(Payments, Products). Walk the New invoice screen with the contact "TEST Atlas" if it exists: add a line item,
set a due date, look at the Send options, screenshot every step, then close WITHOUT saving or sending. If a
draft is saved by accident, leave it and report it. Also record where recurring invoices and payment links
live.

## Job 5: QuickBooks, read only readiness

Settings, Integrations (or App Marketplace), QuickBooks. Record whether it shows Connected or Connect, and
screenshot any options screen that appears before the Intuit login, without clicking Connect. Never type a
QuickBooks login. Record any import toggles (import existing customers, import old invoices) and their
defaults.

## Job 6: rep identity groundwork (no template or workflow changes)

a) Settings, My Staff, each user (David Taylor, Charity Taylor). Record name, email, phone, extension, role,
whether an email signature is set, the calendar link, and what the phone number is used for (call
forwarding). Do not change the user phone: David's user phone is (385) 213-7177 and it may be the call
forwarding target.

b) Set the email signature in each user's profile (the Email Signature box on My Profile or on the staff
member), exactly this text, with "Book a time" as a hyperlink only in David's. Do NOT turn on any "include
signature on all outgoing messages" toggle. Save, screenshot.

David:
David Taylor, Founder
david@atlasonesolutions.com · 380-CALL-A1S (380-225-5217) · Book a time (link: https://api.leadconnectorhq.com/widget/groups/book-david)
Atlas One Solutions · support@atlasonesolutions.com · AtlasOneSolutions.com

Charity:
Charity Taylor, Business Advisor
charity@atlasonesolutions.com · 801-787-8154
Atlas One Solutions · support@atlasonesolutions.com · 380-CALL-A1S (380-225-5217) · AtlasOneSolutions.com

c) In the email template editor, open the merge field picker and record the exact tokens it offers for the
user (name, first name, email, phone, signature, calendar link) and whether they are labelled "assigned
user". In a workflow Send Email action (open one, look, close without saving), record whether From name and
Reply to accept a merge field. Change nothing.

## Report must include
Job 1 end of source before and after per template. Job 2 counts per record type and the unhide steps you
wrote. Job 3 file path and counts (workflows, triggers, send email actions, forms). Jobs 4 and 5 what is
connected and what is missing. Job 6 the two profile records and the token list. Screenshot list. Questions
batched at the end.

## Job 0 (DO THIS FIRST, added 2026-09-26): WSA Scottsdale conference tracking

Context: claude/wsa-booth-demo-2026-09-25.md. Conference code WSA2026. The credit page
https://forms.atlasonesolutions.com/wsa/ is live, and its booking links carry utm_source=wsa-conference,
utm_medium=credit-page, utm_campaign=wsa-2026-10-15. This job is internal only (a tag and a note). The
publishing ban above does NOT apply to the one workflow built here: publish it. Nothing in it may send an
email or a text.

Already done by Cowork through the API, so do not recreate them:
- Contact custom field "Promo code", id gcAPcCMrxGTEk3Xe5JsF, key contact.promo_code, text.
- Tag wsa-scottsdale-2026, id TrsKIm6u36b9co0KLCO3.
- Form "Atlas One - Intro call booking", id jnesTr2nZpXOsGddGLka. It is a duplicate of "Atlas One - Audit
  booking" and is not attached to anything yet. Cowork's clicks inside the form builder canvas did not
  register, which is why this job exists.

a) Finish the form (Sites, Forms, open "Atlas One - Intro call booking"):
   - Add Object Fields, then Promo code. Place it just above Submit. Not required. Label: "Promo code
     (optional)". Placeholder: "Conference or promo code".
   - "What is this call for?" (the dropdown under the Privacy line): open it and record its options. If
     any option is about the audit, delete this field from THIS copy only. If the options are general,
     keep it, move it above Submit and make it not required. Never touch the original Audit booking form.
   - Save, then Preview. Screenshot the preview.
b) Attach it to the calendar: Settings, Calendars, "Atlas One 15 Minute Intro Call"
   (id qLdAzkruMQmYDn2ZT3UM), edit, Forms and Payment. Switch from the default form to the custom form
   "Atlas One - Intro call booking". Keep "Sticky contact" on and the redirect to
   https://atlasonesolutions.com/thank-you-call/ unchanged. Save. Open
   https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp and screenshot
   the booking form step showing the Promo code box. Do not book a time.
c) Workflow: Automation, Workflows, Create, Start from scratch. Name "WSA Scottsdale 2026: tag by code or
   UTM". Folder: the same folder as the other Atlas One lead workflows, if there is one.
   Triggers, all three:
     1. Customer Booked Appointment, filter Calendar is "Atlas One 15 Minute Intro Call".
     2. Form Submitted (any form).
     3. Contact Changed, filter field Promo code (so a code typed later is caught too).
   Action 1, If/Else with one branch "WSA" where ANY of these match (OR):
     - Promo code contains WSA2026
     - Promo code contains wsa2026
     - Promo code contains Wsa2026
     - the contact's UTM source (look under Attribution: "Latest/Last attribution UTM source" and
       "First attribution UTM source"; add both if both exist) is wsa-conference
     Record the exact condition names GHL offered. If GHL has a case-insensitive option, use it and
     say so.
   WSA branch: Add Contact Tag wsa-scottsdale-2026, then Add Note, text exactly:
     WSA conference: $250 Atlas One credit plus Cornerstone offer
   None branch: nothing.
   Settings: Allow re-entry OFF (so the note is added once). Save, then Publish.
d) Test it without sending anything: create contact "TEST WSA Promo" (email
   test-wsa-promo@atlasonesolutions.com, no phone), then set its Promo code to wsa2026 (lower case).
   Confirm the tag and the note appear within 2 minutes. Screenshot. Then remove the tag from the test
   contact and leave the contact (no deleting).
e) Smart list: Contacts, filter Tag is wsa-scottsdale-2026, then Save as smart list "WSA Scottsdale 2026".
   Screenshot showing the test contact in it before you remove the tag.

Report for Job 0: the form preview and booking page screenshots, the dropdown decision, the exact
If/Else conditions used, the test result, and the smart list name.
