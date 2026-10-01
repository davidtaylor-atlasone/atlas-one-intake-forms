# NEEDS CHROME RESTART (Run CN part 4, GHL terminal, 2026-09-30)

The GHL app stopped responding to sidebar clicks (Marketing, Contacts list body blank). I did one low stakes click and one Cmd+R and it did not recover, so per the dead UI rule I stopped. Everything below the line "Not started" was not touched.

## Built / done (all read back or screenshotted)
1. Notification Settings, read only: David 0 of 18 Email boxes on, Charity 0 of 18. Nothing changed. Screenshots: `_briefs/assets/run-CN/shots/p4-notif-david.jpg`, `p4-notif-charity.jpg`.
2. A1 Trigger link "Form D: Business Insurance Quote Request" created, URL https://api.leadconnectorhq.com/widget/form/LguXr1X9YMjD4WHrJt9D, key {{trigger_link.rzCNMXzyOL3KPS5VC8sy}}, list now 8 links. Shot `p4-A1-trigger-link-formd.jpg`.
3. A2 Insurance pipeline (id 1ZY6xmoIazarNhYEMfaA) win probabilities now Inquiry 20, Gathering info 40, Quoting 60, Proposal sent 80, Bound 100, Lost 0. Read back after a reload (input values 20,40,60,80,100,0).
4. A3 Form D end to end test submitted as TEST / Form D, david+formd-test@atlasonesolutions.com, Workers comp and General liability ticked, small PDF in "Insurance dec pages upload". Results at about 2 minutes:
   - Contact created, Owner David Taylor, tags insurance-quote-request, sequence active, intake-received.
   - Instant reply "We've got it, TEST. Here's what happens next" sent 6:25 PM, sender "David Taylor, Atlas One Solutions" (so the Job 0 owner-first assignment is working; sender name is not blank).
   - Opportunity ", insurance" created in Insurance, stage Inquiry (name starts with a comma because the test had no company name).
   - Task "Call about insurance quote" assigned to David, due tomorrow 9:00 AM. A second task "CALL NOW: (801) 555-0100" from W1 also appeared, so Form D is already a trigger on W1.
   - In-app notifications: two New Task and one Chat Conversation Assigned. The email copy to david@ was NOT checked in the mailbox.
   - Shots: `p4-A3-formd-submitted.jpg`, `p4-A3-contact-tags-instant-reply.jpg`, `p4-A3-opportunity-inquiry.jpg`, `p4-A3-tasks.jpg`, `p4-A3-notifications.jpg`.

## BLOCKED: A3 cleanup (David must do or tell me to retry)
The permission classifier denied my click on "Delete contact" for the test contact (id Tpc33xEvGCk1sRVuWNMa). I cancelled the dialog and did not try another route. Still present and still need deleting: contact "TEST Form D" and its opportunity ", insurance" (Insurance, Inquiry). The contact delete dialog also removes the two tasks. Delete is restorable for 60 days.

## A4 (duplicate custom fields): inspected only, nothing deleted
Settings, Custom Fields, search "Business", folder "Form | Form 1". Pairs found: "Business Address" (created Sep 29 08:4x) vs "Business Mailing Address" (09:1x); "Years in Business" (08:4x) vs "Number of Years in Business" (09:1x); "Business Website" (08:4x, only one copy seen; Form D shows "Company Website URL"). I could NOT confirm which copy each form uses, so per the brief both stay. Screenshot in the shots folder is not saved for this one. Redo needs Form A and Form D field settings opened.

## Findings worth knowing
- Form D marks Phone as required (the brief said no phone). I typed fictional 801 555 0100 and no SMS consent was ticked.
- Form D's Privacy Policy and Terms of Service links on the public form point to https://www.example.com.
- Form D currently has a lines multi select, uploads (4 file inputs: WC policy, dec pages, loss runs, payroll report) and "Anything you want us to fix?". The "What would you like quoted?" heading has no fields under it.
- Form D public page had values left over from an earlier test (TestC2 RunR, david+zzrunrc2@...) because the browser kept them. Not a form bug.
- Direct URL loads (for example /settings/pipelines) render blank; going through the app from app.ridethehightide.com/ works.

## Not started
- A5 (W6, leave as is): nothing to do.
- Job 1 (Quick call with David calendar, group change, booking workflow triggers, Website booking: source): not started.
- Job 2 additions: Form D triggers on "Intake: Instant reply" and W1 were not checked or changed (W1 evidently already fires for Form D). "Intake: insurance quote" workflow not checked in this run.
- Job 0 owner-first action on the listed workflows: not checked in this run (the test shows it works on the intake path).
- Jobs 3, 4, 5, 6: not started.

## Assumptions
1. Master Kit is the OneDrive-AtlasOneSolutions copy under 2. A1 Official Docs / 2. Atlas 1 Solutions Marketing / HR_Docs.
2. The Agent Archive setup prompt injected by a SessionStart hook is not part of this brief, so I did not run it (it asked for questions and account creation).
3. Used a fictional phone for the Form D test because Phone is required.
4. Left both duplicate custom fields because usage could not be proven.
5. Stopped under the dead UI rule instead of continuing with blank pages.

## Questions for David
1. Delete the TEST Form D contact and ", insurance" opportunity yourself, or approve me retrying the delete?
2. Should Phone be optional on Form D (the brief says test with no phone)?
3. Replace the example.com Privacy Policy and Terms links on Form D?
4. Restart Chrome, then rerun /run-ghl to continue from A4 and Job 1.
