# RUN-GHL report: Run CN part 5 and Run CO (Technology Services)

Run date: 2026-09-30, 6:46 PM to about 10:10 PM Mountain. Terminal: GHL (browser UI plus the HighLevel API connector).
Brief: BRIEF-GHL.md (RESUME 5), copied to `_briefs/BRIEF-GHL-2026-09-30.md`. Live log: `TERMINAL-GHL-live.md`. Ids: `RUN-CO-ids-working.md`.
Screenshots: `_briefs/assets/run-CN/shots/` and `_briefs/assets/run-CO/shots/`.
The earlier "needs Chrome restart" report from Run CN part 4 (Trigger Link for Form D, Insurance win probabilities, Form D test) is kept unchanged as `RUN-GHL-report-CN-part4-2026-09-30.md`.

Status in one line: everything in the brief is built and verified except Job 5 (the inbound webhook), which is only a named empty draft because GoHighLevel will not save an Inbound Webhook trigger without a captured sample request. No hard stop was crossed. Nothing was deleted. No email went to anyone except the david+ test address.

---

# Part 1. Run CN part 5

## Built and verified

**Step 0, notification check.** David and Charity each have 0 of 18 Email boxes on in Notification Settings. Nothing changed. Shots: p5-notif-david.jpg, p5-notif-charity.jpg.

**Item 1, Form D legal links.** Form D Privacy Policy and Terms links now point to `https://forms.atlasonesolutions.com/tools/text/`. Form A also had the placeholder `https://www.example.com`, so the fallback was used (Form A not touched). Read back on the public widget `widget/form/LguXr1X9YMjD4WHrJt9D`. Shot: p5-1-formd-links.jpg. (First attempt typed into the form title by mistake; I reloaded without saving and confirmed the form name and updated time were unchanged.)

**Item 2, "Intake: insurance quote"** (id 20662e2a-b623-491f-8cd7-9069b3052f5d). Read back after reopening:
- Create opportunity name is `{{contact.company_name}} insurance` (the comma is gone).
- New action "Add owner to opportunity" = Assign contact owner.
- The task "Call about insurance quote" now sits above a new If/Else "Company check" (Company name is empty, then Find opportunity, then Update opportunity name `{{contact.name}} insurance`). The old task was removed so it cannot get stuck in a branch.
- Shots: p5-2-workflow-insurance-quote.jpg and p5-2-workflow-insurance-quote-readback.jpg.

**Item 3, duplicate custom fields.** I read all 10 live forms (positive control passed).
- Business Address (vrbPdeezOwAEHWcd9uor), Years in Business (Ww1Tj2E13eZagJDvEeIA) and Business Website (iqj1ZMKtwM9tq9zyAm3o) are used by no form.
- Form D uses Business Mailing Address (vOM54PbmnHaJhxofAXei), Number of Years in Business (bZ2RgBKQUYt69IlZud1V), Company Website URL (mJ14JpKsatM5reCQ6bCJ). Form A uses none of these.
- Business Address and Years in Business hold a value on one contact (wesly faux, mObyoG4BJmWmYQrN9GUg), so both were KEPT.
- Business Website has 0 contacts and is safe to delete. The permission classifier denied the delete click and I did not retry. See Questions.

**Job 6, owner identity.**
- 6b From fields set to `{{user.name}}, Atlas One Solutions` and `{{user.email}}` and saved at the top level on: Audit: offer follow up (day 20, day 28), Call: not now (6, already set by Run CM, re-saved), Intake: Send bookkeeping form, Send PEO form on tag, Send bookkeeping form on tag, Intake: document build, Intake: service sign up (all 10 branches), Tool-Lead Nurture (5A, 5B), W1 (P-C-0 disabled, P-C-2, P-C-3), W2 (P-A-1 to P-A-3), W3 (P-B-1 to P-B-4, which had blank From), W3a (4 emails), W4 (P-D-1 to P-D-4), W5 (P-E-0, P-E-4, Q1, Q2, Q3, Q1 repeat), Won - Pay Referral Partner (Email 6, Email 7, plus two internal "Notify David" emails that had a blank From).
- 6a templates: 29 email templates written through the HighLevel API (update-email-template) so the disk HTML lands exactly. 5 spot checked live: merge fields present, no hard coded David signature. Not touched: 45-b and 45-c (the disk copies are the placeholder "READ FROM GHL"; pushing would wipe the live copy) and send-peo-form.
- 6c notifications and tasks: fixed "David Taylor" tasks switched to "Contact's Assigned User" in Call: not now (4), Intake: document build (2), Intake: service sign up (10), W1 (4, one was blank), W2 (7), W3 (5), W3a (2), W4 (6), W5 (2), Won - Pay Referral Partner (2). Intake: Instant reply internal notification now goes to Assigned owners with Cc David.
- 6d signature: "The $70,000 audit (construction)" inline signature is now `{{user.first_name}}` sign off, `{{user.name}}`, `{{user.phone}}`, `{{user.email}}` (was David Taylor, 385-213-7177). Shots: p5-6d-70k-signature-before.jpg and p5-6d-70k-signature-after.jpg. The inline text in Intake: Send bookkeeping form (Email 2B) got the same change.

## Part 1 skipped or blocked
- Delete of the test contact "TEST Form D" and its test opportunity (permission classifier denied). Left for David, listed below.
- Delete of the field Business Website (classifier denied). Left for David.
- Won - Pay Referral Partner "Notify David" x2 are Send Email actions to David's own address: From set, recipient left as is.

---

# Part 2. Run CO, Technology Services

## Job 1. Pipeline (read back through the API)
Pipeline "Technology Services", id `NzafbSwy15tKoN9sunPt`.

| Stage | Win probability | Stage id |
|---|---|---|
| Discovery | 10 | 7ee39afc-a5d1-4237-be5b-5e5d66e11bed |
| Bills Received | 20 | 4a30996b-78f2-4ddc-bb5f-559098b98599 |
| Quoting | 35 | 84b22b9f-42e6-4d71-9f51-72e5d5daf0b2 |
| Quote Presented | 50 | eedf665f-d4f3-4c53-bbcc-c7ef8d1f428f |
| Signed | 80 | ac1707bd-c648-4e4d-ba54-6c36eb734403 |
| Ordered | 90 | 798edc4c-731f-4266-a445-ff7923ea5fbd |
| Installed | 95 | 50d9dc11-286f-4cee-8887-b60914a4186b |
| Commission Verified | 100 | ad7334d8-ab73-436c-ae62-112e963c9d03 |
| Lost | 0 | 35f0c6f1-7e56-491b-8efb-f7514f4b1a87 |

## Job 2. Opportunity fields (folder "Technology Services", id DLpovRu0LkUqHasFxDrk)
| Field | Type | Id | Key |
|---|---|---|---|
| Provider | Single line | kFNX01CT4YDE3LLMGnb4 | opportunity.provider |
| Product | Single line | tVG5ASJHBZYOEBBZEkI1 | opportunity.product |
| Service category | Dropdown, 18 options | LSTxXbhGsZxi2CMfV7LQ | opportunity.service_category |
| Monthly bill | Monetary | 48dLysumwVGzSXgRwaIF | opportunity.monthly_bill |
| Term months | Number | eI1cnA9CzJMUmr1KfPAp | opportunity.term_months |
| Gross commission rate | Number | sBPfPlyi9DDX8yeCk76p | opportunity.gross_commission_rate |
| Expected monthly commission | Monetary | hM3x3EekUQKebGiF98wD | opportunity.expected_monthly_commission |
| SPIFF | Monetary | 3RrstKulkAVhRqDyYBD3 | opportunity.spiff |
| Quote number | Single line | X0xAfctbuxw2H5KNrdup | opportunity.quote_number |
| Order number | Single line | cxG5YsR9du4n9agajXTc | opportunity.order_number |
| Install date | Date | iIP3ubcL0Y7BNqr9d29I | opportunity.install_date |
| Contract end date | Date | y88yhaB3Rhl4Vsr7IgCO | opportunity.contract_end_date |

No GoHighLevel Products, prices or margins are on these deals. No vendor or distributor name appears in any label (client facing names are "Quote number" and "Order number").

## Job 3. Contact fields, Form E, Trigger Link
New contact fields (13, default contact folder): Number of locations 7DgqpbXIoijR1wW4booF; Locations, city and state for each kEF8ApxYroobfjrFsSui; Tech services of interest EzpozoxBRX6oLWmXbtXi (8 checkbox options); Current phone provider UFnsn8pjWoFslzeT7tz4; Current internet provider okp4F5CY6JDBapyqmaB0; Current cell provider Tf5eiQCNUsq3M0yDgCzY; Phone contract ends Qa6EJ6LdEnbizQ730WdI; Internet contract ends 3SQLaKodxAqxFla6RtU3; Cell contract ends welADy6gzEhqr5F1z5IW; Tech pain points 66tQ8kvbj8g1JyGIahGw; Recent phone bill GSyiYdBGTKf8zFrwilFK; Recent internet bill YRbI8rAFeoIuZUeYo3Hc; Recent cell bill d47H3XPihzrvM6L9biu9. Reused, not duplicated: Software seats or users 27G6ifDxK2miZSCTt7e7. Company uses the standard Company name field.

**Form E "Atlas One — Tech and Connectivity Intake"**, id `KhinSbtsHkyjirSHb20Q`. Share link: https://api.leadconnectorhq.com/widget/form/KhinSbtsHkyjirSHb20Q
Read back on the live widget: 20 labelled fields in the specified order, button "Send my bills for review", thank you text set, zero dashes. Required: first name, last name, email only. The test below proved the Organization element writes the contact's Company name.

**Trigger Link** "Form E: Tech and Connectivity Intake", id `KiKoUEObx3uvGH69AXkt`, merge key `{{trigger_link.KiKoUEObx3uvGH69AXkt}}`.

## Job 4. Workflows (status read from the Workflows list after the test)

| Workflow | Id | Status | Enrolled (total / active) |
|---|---|---|---|
| Tech: Intake | 60e2bd2d-813c-4d60-9fba-a511191e2ffa | Published | 1 / 0 |
| Tech: Installed | fe91dfe0-d16c-4548-8fea-9d65dfa18df8 | Published | 1 / 1 (before cleanup) |
| Tech: Re shop 120 days before contract end | 306e1fd5-da3f-4636-a84a-e36895e11e9f | Published | 0 / 0 |
| Tech: Order updates (inbound) | ba668282-1518-4014-8927-291c3069a919 | Draft, empty shell | 0 / 0 |

Form E is also a trigger on **Intake: Instant reply** (94b34c50-2ad7-4650-a42d-35a74365555b) and **W1 Inbound speed to lead** (e50ddca0-1bc1-4a4b-a706-f2d02ba27259), as its own trigger "Form E submitted (Tech)" filtered to Form E, the same way Form D was wired. Both saved and still published.

**4a Tech: Intake, read back after Cmd+R.** Trigger Form E submitted. Actions in order: Assign to user (David only, only if unassigned); Add Tag tech-services; Create opportunity (Technology Services, Discovery, name `{{contact.company_name}} Tech review`, open); Add owner to opportunity (contact owner); Internal Notification; Internal Notification; Condition with 4 ordered branches: "Bills and no company", "Bills received", "No company", "None". Each of the first three branches has Find opportunity (most recently created, Pipeline is Technology Services) and, under Opportunity Found, Update opportunity: branch 1 sets name `{{contact.name}} Tech review` and stage Bills Received; branch 2 stage Bills Received; branch 3 name `{{contact.name}} Tech review`. The read back list had every node (Assign, Add Tag, Create opportunity, Add owner, 2 notifications, Condition, 3 Find, 3 Update, END nodes, Form E trigger). Shot: job4a-tech-intake-published.jpg.

**4b Tech: Installed, read back after Cmd+R.** Trigger Pipeline stage changed, In pipeline is Technology Services, Pipeline stage is Installed. Update opportunity (Install date = `{{right_now.date}}`); Send email "Tech Installed welcome", From `{{user.name}}, Atlas One Solutions` / `{{user.email}}`, subject "Your new service is in, and we are still your first call", body exactly as in the brief; Wait 75 days; If/Else "Still installed" (Pipeline stage is [Technology Services] - Installed); on that branch Add task "Check first commission: `{{opportunity.name}}`", description as in the brief, assigned to Contact's Assigned User, due 3 days. Shot: job4b-tech-installed-readback.jpg.

**4c Tech: Re shop, preferred build, read back after Cmd+R.** GoHighLevel DOES offer an opportunity date field in the Custom Date Reminder trigger, so the fallback (copy to a contact date field) was NOT needed and no one-date-per-contact limit applies. Trigger: Custom date reminder, filter Opportunity date field = Contract end date, filter Before no. of days = 120, "match year" ticked. Action: Add task "Re shop: `{{opportunity.name}}` contract ends in 120 days", description "Open the opportunity and read the Contract end date. Pull the current bill, quote at least two options, present before the end date.", Contact's Assigned User, due 7 days. Shot: job4c-reshop-readback.jpg.

## Job 5. Inbound webhook: NOT FINISHED (see Questions 1)
"Tech: Order updates (inbound)" exists as a named Draft with no trigger and no actions.
- WEBHOOK URL: none yet. The Inbound Webhook trigger will not save without a Mapping Reference (a captured sample request): the panel says "A Mapping Reference is required for an Inbound Webhook Trigger". Until it is saved, GoHighLevel generates a new URL every time the trigger panel opens (I saw two different ones), so no URL I could paste here would be the real one.
- I did not post a sample payload to the URL, because the trigger is billed per execution and I could not confirm a captured sample is free.
- The If/Else skeleton was not built: without a saved trigger, GoHighLevel offers no opportunity fields to branch on.
- The workflow was never published.

## Job 6. End to end test (test address only)
Submitted Form E from the share link as Tech Test, david+forme-test@atlasonesolutions.com, company Tech Test Co, 2 locations (Austin, TX; Boise, ID), 10 seats, Business phones and Internet ticked, phone contract ends 2027-01-28 (120 days from today), a 399 byte test PDF as the phone bill. The phone box was cleared (the form had pre-filled a real looking number from the browser, which I removed so nothing could text or call it).

Confirmed from the API after the submit:
- Contact `aoMNDfU8MFwnlGsxJkOh` created. Owner David Taylor (vTV2wRivyR9f9XWNook3). Tags tech-services, sequence active, intake-received. Company name "Tech Test Co". Custom fields all stored, and the phone bill file is on the contact (document id 3eDuwRuXdT4t9oQ0lAza).
- Exactly one opportunity `fFi3ZcwyUJrR2d24ifXU` in Technology Services, named "Tech Test Co Tech review", owner David, created by Tech: Intake, moved to Bills Received 9 seconds later (stage 4a30996b).
- Instant reply: the only outbound message on the contact, from David Taylor / David@atlasonesolutions.com, to the test address only.
- Moved the opportunity to Installed (API): Install date stamped 2026-09-30, welcome email "Hi Tech, Your new service is installed..." sent to the test address only, Workflows list showed Tech: Installed enrolled 1, active 1 (the 75 day wait is queued). Shot: job6-workflow-list-enrollments-after-test.jpg.
- Form shots: job6-form-e-filled-before-submit.jpg, job6-form-e-thank-you.jpg.

Not verified: David's internal notification emails (his mailbox was not opened; the workflow ran without error and in app notifications were not screenshotted). Please glance at your inbox for the new tech intake alerts.

Cleanup done: contact removed from Tech: Installed (wait cleared) and from W1; opportunity marked Lost (stage Lost); tag `test-delete-me` added. The contact was NOT deleted.
Still on the contact: tag `sequence active`. The cadence that tag feeds may still be queued; its emails can only go to the test address.

## Job 7. Guides
`GHL How-To/GHL-How-To-Admin-Guide.md` and `GHL-How-To-Rep-Guide.md` updated and both HTML guides rebuilt with `_BUILD-LOG/ghl-howto-src/build.py` (footer date now 2026-09-30).
- Admin: new "never name the vendor portal" rule, 7 pipelines, Technology Services stage table (what each stage means), Installed row in the stage automation table, tag `tech-services`, `test-delete-me`, the four Tech workflows (and the new count), Form E in the forms table with its Trigger Link, Form E added to the Instant reply and W1 lines.
- Rep: Technology Services pipeline bullet and a "Technology Services deals" section.
- 390 px check on both HTML files: scrollWidth 390, no console errors, no network requests, no en or em dashes, no vendor or distributor name. Shots: GHL-How-To-Admin-Guide-390.png, GHL-How-To-Rep-Guide-390.png.
- I did not rebuild Atlas One COMMAND.html, because no tool file changed (the guides are documents).

---

# Assumptions (numbered)

1. Form D and Form A privacy and terms links: both held `https://www.example.com`, so the fallback `forms.atlasonesolutions.com/tools/text/` was used for Form D only (Form A not touched).
2. Business Address and Years in Business were kept because one contact (wesly faux) holds a value in each.
3. The 6a templates were pushed through the HighLevel API (PATCH) instead of pasting in the Marketing Emails editor, to write the disk HTML exactly and avoid the stray ">" bug. 45-b, 45-c and send-peo-form were deliberately not pushed.
4. The two internal "Notify David" email actions in Won - Pay Referral Partner had a blank From; I set them like the client emails.
5. Form D test used fictional phone 801-555-0100 because Phone is required on Form D.
6. Form E: phone is optional (Form D has it required). The SMS consent boxes and the policy links line from Form D were not carried over to Form E.
7. Drag worked in this browser for the Organization and Submit elements of Form E (the brief said it would not); I used it.
8. Tech: Intake assigns David only, and only if the contact is unassigned. A contact that already has an owner keeps that owner.
9. Branches do not rejoin in GoHighLevel, so each of the three Tech: Intake branches has its own Find opportunity and Update opportunity. The name falls back to the contact name when the company is empty.
10. Tech: Installed stamps Install date every time an opportunity enters Installed (it overwrites an older date on re-entry). I could not put a "date is empty" guard in front of it without splitting the workflow. Re-entry should be rare.
11. The welcome email was written in Quick compose, plain text, no branded frame and no logo block. It reads correctly and merge fields resolve (tested).
12. Re shop trigger "Before no. of days" in GoHighLevel is "at most 120 days", so a deal saved with a Contract end date already under 120 days away will enroll right away and get the task. That seemed right (someone should re shop it now).
13. Opportunity custom field merge tags (for example `{{opportunity.contract_end_date}}`) show as unrecognized in the task title, so the Re shop task title says "contract ends in 120 days" and the description tells the rep to read the Contract end date on the deal.
14. In the Tech: Installed 75 day check I used the "Pipeline stage is [Technology Services] - Installed" condition. A deal moved to Commission Verified before day 75 correctly gets no task.
15. Job 6 moved the opportunity with the API instead of dragging the card (same stage change event; the workflow fired normally).
16. The unused contact Date field "Tech contract end date" (id DFnjSRUkKYpsfsEu1bps, key contact.tech_contract_end_date) was created before I found the opportunity date option in the trigger. It is unused and harmless. I did not delete it.
17. I did not post a test payload to the webhook URL (possible per execution charge), so Job 5 stopped at the draft shell.
18. The Tech workflows do not send any SMS and nothing was enabled that could. Intake: Instant reply and W1 already existed and now also fire for Form E; the test contact had no phone.

# Skipped

- Job 5 beyond the empty draft shell (trigger, If/Else skeleton, workflow note, webhook URL).
- Deleting anything (hard stop).
- 45-b and 45-c templates, send-peo-form template.
- Rebuilding Atlas One COMMAND.html (no tool changed).

# Questions for David

1. **Webhook (Job 5).** GoHighLevel will not save the Inbound Webhook trigger until it has a sample request, and it only shows a final URL after saving. Do you want me to post one harmless sample payload to capture it (I think this is free but cannot prove it, and the trigger itself is billed per execution once the workflow is published), or do you prefer to wait for a real sample from the vendor? Say "go" and I will capture the sample, build the three branch skeleton and report the URL.
2. **Please delete when you choose:** contact "TEST Form D" (id Tpc33xEvGCk1sRVuWNMa, david+formd-test@atlasonesolutions.com) and its opportunity ", insurance"; contact "Tech Test" (id aoMNDfU8MFwnlGsxJkOh, david+forme-test@atlasonesolutions.com, tag test-delete-me) and its opportunity "Tech Test Co Tech review" (fFi3ZcwyUJrR2d24ifXU, Lost); the unused field Business Website (iqj1ZMKtwM9tq9zyAm3o); the unused contact field Tech contract end date (DFnjSRUkKYpsfsEu1bps).
3. **Privacy and Terms links.** Form D now uses `forms.atlasonesolutions.com/tools/text/`, and Form A still has example.com. Do you have the real Privacy Policy and Terms URLs?
4. **Tech welcome email look.** It is plain text. Do you want it in the branded email frame with the logo block like the P- templates?
5. **Install date overwrite.** Is it fine that a deal re-entering Installed gets a new Install date?
6. **Inbox check.** Did David's new tech intake alert and the Form E internal notification email arrive?
7. **45-b, 45-c, send-peo-form.** Do you want the local disk copies replaced with the live text so the next run can push the owner identity changes to them?
8. **Sequence active.** The test contact still carries `sequence active`. Do you want me to strip it and clear the cadence (it can only email the test address)?
