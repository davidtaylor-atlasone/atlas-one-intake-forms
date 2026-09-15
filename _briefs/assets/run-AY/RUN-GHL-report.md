# RUN-GHL-report.md (Run AY, 2026-09-15)

## Summary

This run switched the GHL terminal from the Claude Chrome extension (dead-clicked on the same
Templates/workflow-row bug across 7 straight runs: AP, AR, AS, AT, AV, AW, AX) to the new
`ghl-browser` MCP server (Playwright, its own `~/.ghl-browser` profile). The dead-click did not
reproduce once. Order worked: Part 0, Part 10, Part 5a (fully), Part 5b (tested, limitation
noted). Parts 5c, 6, 7, 8, 9 not started this run.

## Part 0: cleared

Navigated to `https://app.ridethehightide.com/`, David signed in manually in the Playwright
window, clicked Automation -> clicked "Books: after the call" row -> editor opened cleanly
(URL changed to `/automation/workflow/9c1eae4a-...`, page title matched). No dead-click. The
Templates sub-tab under Marketing > Emails, which was the specific dead spot in the Chrome
extension, also opened correctly in ghl-browser. This strongly suggests the extension itself
was the problem, not the GHL account.

## Part 10: WSA Partnership Plus emails (Cornerstone brand) - DONE

- **P-W7-1** (id `6aa0a9f855d1ce8973c141a2`): body changed "Zak Call at WSA suggested I reach
  out." -> "WSA asked me to reach out." Saved, reloaded, re-read clean. No "Zak" anywhere.
  Subject per copy file: "Your WSA Partnership Plus credit" (see below re: workflow subject).
- **P-W7-2** (id `6aa0a9f955d1ce8973c141a8`): checked, confirmed it never mentioned Zak, no
  edit needed. Subject: "The practice impact calculator WSA built with us".
- **P-W7-3** (id `6aa0a9fb6ec737a976fa481f`): body changed "I will let Zak know I could not
  catch you." -> "I will let the WSA team know I could not catch you." Saved, reloaded,
  re-read clean. Subject: "Closing the loop".
- All three: confirmed no "Zak", no "Call" as a surname, no dashes in the copy (only CSS
  hyphens in style attributes, which are fine), Cornerstone signature phone (801) 358-8547
  unchanged, Zoom scheduler link unchanged, no 380 number swapped in (this is Cornerstone
  brand, not Atlas One).
- **Finding, not a defect to fix**: opened "W7 WSA handoff (Cornerstone)" workflow
  (`04e13657-82b9-4c96-8367-0bcfde1e79ee`) to set the Subject on each Send Email card per the
  brief. This workflow has **no GHL "Send Email" action anywhere** - it is entirely
  task/notification based: an "Internal notification" (subject seen only by David, e.g. "Send
  WSA Email 1 as Cornerstone") plus an "Add task" reminding David to send the email himself
  from `david.taylor@cornerstonepeo.com` using the P-W7-N wording. This matches
  `atlas-one-ai-email-assistant/templates/w7/README.md`'s description of the real
  architecture (David composes and sends from his own Cornerstone mailbox via a separate
  compose tool; GHL just holds the template text and reminds him). There is no card to put a
  subject on. No changes made to the workflow.

## Part 5a: client-facing emails on the wrapper - DONE, with one real bug found and fixed

Both `confirm-service-signup.html` and `confirm-document-build.html` pasted from the OneDrive
files, using the Quick Compose "Source code" dialog on each Email action.

- **"Intake: service sign up"** (`bf3a04b1-5c38-45cc-9316-dd08ab11a8e2`): 10 branches
  (AI Email Assistant, AI Task Agent, Workers comp audit recovery, Certified payroll,
  Document build, Other premium service, Membership, Business insurance quote, Group benefits
  quote, Software and licenses), each Email action set to From Name "David Taylor, Atlas One
  Solutions", From Email `david@atlasonesolutions.com`, Subject "Your
  {{contact.which_service}} request is in, {{contact.first_name}}", body =
  confirm-service-signup.html. The 11th branch ("None") correctly has no email. Workflow
  saved, remains Published.
- **"Intake: document build"** (`1d30062d-d22e-4b75-a59d-afbc0cf06bb0`): single linear Email
  action (no branches), same From Name/Email, Subject "Your {{contact.which_document}} is in
  the queue, {{contact.first_name}}", body = confirm-document-build.html. Saved, remains
  Published.
- **Bug found by live-testing**: the file placeholder `{{contact.company_name}}` does not
  resolve on either form. Form C1's "Company Legal Name" field (and Form C2's identical field)
  is a **custom field** with query key `legal_business_name`, not GHL's built-in
  company/business-name field. First test submission (Certified payroll) confirmed the bug:
  the sent email read "Got your request for Certified payroll for . Here is what happens
  next" - blank where the company name should be. Fixed both OneDrive source files and all 11
  live GHL Email actions to use `{{contact.legal_business_name}}` instead. Re-tested with two
  more real form submissions (Membership on C1, Employee handbook on C2) and confirmed both
  merge tags now render, e.g. "Got your request for Membership for Second Test Holdings LLC."
  and "Got your request: a Employee handbook for Doc Build Test Co."
- All 3 test contacts created during this testing were deleted afterward
  (TestP5a/TestP5b RunAY - same contact, merged by email; TestDoc RunAY).
- **{{contact.which_service}} / {{contact.which_document}}**: confirmed via the merge-tag
  picker that the real tags are exactly these strings, matching the file placeholders exactly.
  No substitution was needed for those two tags, only for company_name.

## Part 5b: link colour on Email 1 (Post-Presentation Email) - tested, not confirmed end to end

Opened "Post-Presentation Email" workflow (`304a9fa4-a256-4015-b767-031070f4186f`), found
"Email 1 - You're moving forward (form + doc list)" (subject "Your next step with Atlas One,
{{contact.first_name}}", confirming this is Email-1). Read the anchor for "Complete the quote
form": the color span is gone entirely - GHL's sanitiser had stripped it down to a bare
`<a><strong>text</strong></a>` with no color styling at all, inside a periwinkle CTA button
cell. Per the brief, replaced it with
`<a href=".."><font color="#23304D"><u>text</u></font></a>`. Saved, reloaded, re-read: the
`<font>` tag **was not stripped** this time (the span form was; the font form survived GHL's
save pass). Sent a test via the action's own "Send test mail" feature to
`david+zzap4@atlasonesolutions.com` (GHL confirmed "Email sent").

**Limitation**: this run had no working access to check the actual inbox and confirm real
Outlook rendering (link color in a live email client). The Gmail tool available this session
returned zero results for every query tried, including an unfiltered "last 24 hours" search,
suggesting it is not connected to David's live mailbox in this environment. What is confirmed
is only that the `<font>` form survives GHL's own sanitizer where the `<span>` form does not -
not that it renders navy instead of magenta in Outlook. Recommend David (or the next run, if
inbox access is fixed) check `david+zzap4@atlasonesolutions.com` and report back before any
mass re-paste of the font-tag fix across the other 25 cadence files.

## Not done this run

- **Part 5c** (the big phone number re-paste, 380-225-5217 across ~14 workflow sends): not
  started. This run's Part 5a alone took the majority of the time (a genuine bug in a
  from-file placeholder needed root-causing, fixing in two places, and three rounds of live
  testing).
- **Part 6** (booking notifications to David on 4 calendars + 3 internal-notification
  workflows): not started.
- **Part 7** (phone system settings for 380-225-5217): not started.
- **Part 8** (calendar logos on 30/45/60 min booking pages): not started.
- **Part 9** (QuickBooks integration + Documents & Contracts/Products read-only check): not
  started.

## Assumptions

1. The Cornerstone signature phone (801) 358-8547 in the WSA/W7 templates is correct as-is
   and should not be touched by the 380-225-5217 re-paste (Part 5c) since this is a different
   brand/mailbox (Cornerstone PEO, not Atlas One Solutions) - this was already explicit in the
   brief, restated here for clarity since Part 10 and Part 5c touch overlapping template
   infrastructure.
2. Test form submissions used `TestP5a/P5b RunAY`, `TestDoc RunAY` as names, a fake unique
   phone per submission, and the David's approved `+zzap2`/`+zzap3` test aliases (`+zzap4` used
   for the Part 5b action-level test-mail feature, which does not need a full form submission).
   All test contacts were deleted after verification.
3. Treated `{{contact.legal_business_name}}` as the correct, permanent replacement for
   `{{contact.company_name}}` in both source files and both live workflows rather than as a
   temporary patch, since it is a genuine bug (the placeholder tag never resolved on either
   form) rather than a stylistic choice.
4. Did not attempt to fix the same likely company-name-tag bug in any of the other 24 cadence
   files (Part 5c/6 territory) since Part 5a's brief only named these two confirmation files;
   flagging it below as a question since it may affect other sends that reference company
   name.

## Questions for David

1. **Gmail/inbox access**: the Gmail MCP tool available this session returned zero results for
   every search tried (including a completely unfiltered "last 24 hours"). Is it connected to
   a different mailbox than `david@atlasonesolutions.com`, or not connected at all? Part 5b's
   link-color test (and any future "screenshot the received email" step) needs a working inbox
   connection to actually see what Outlook renders.
2. **Part 5b next step**: given the `<font>` tag survives GHL's sanitizer where `<span>` does
   not, do you want the font-tag form mass re-pasted across all 26 cadence files as part of
   Part 5c (once you or a later run confirms it actually renders navy instead of magenta in
   Outlook), or should this wait until 5c is otherwise done and be a separate pass?
3. **Company name tag elsewhere**: the `{{contact.company_name}}` bug found in Part 5a (should
   be `{{contact.legal_business_name}}`) - do any of the other 24 cadence files under Part 5c
   also use `{{contact.company_name}}`? If so, should the next run check and fix those too, or
   is company name only referenced on the two confirmation emails this run touched?
4. **W7 workflow Subject cards**: per Part 10's finding, "W7 WSA handoff (Cornerstone)" has no
   automated Send Email action - David sends these three emails himself from his Cornerstone
   mailbox, guided by an internal task. Is that the intended design (a deliberate manual
   handoff, matching the Cornerstone-brand separation from Atlas One's own send
   infrastructure), or was an automated send originally planned and never built?
