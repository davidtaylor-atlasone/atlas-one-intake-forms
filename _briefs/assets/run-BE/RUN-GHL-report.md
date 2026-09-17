# RUN-GHL-report.md (Run BE, 2026-09-16)

Scope this run: Part 24 (Dr. Gould's replies going to the lc address, the duplicate 11:19 AM email, urgent,
done first), Part 21 (the three blank lines in the new intake notice, and the CALL NOW task), Part 22 (State
and industry on Form A), Part 23 (test). Parts 1-20 were completed in prior runs and are not repeated here.

## Built

### Part 24: Dr. Joel Gould duplicate reply / lc. address issue
- **24a.** Settings > Email Services > Reply & Forward Settings: Forwarding Address was still empty on
  arrival. Set it to David@atlasonesolutions.com, saved, confirmed by full page reload it persisted. Reply
  Address and BCC Emails remain empty (only asked to report them). "Forward to assigned user" toggle
  untouched (off).
- **24b.** Read Joel Gould's Conversations thread (contact 3MBRxpll6eLI4bvtIdfh), no changes made:
  - 11:19 AM "We've got it, Joel. Here's what happens next" -- from David Taylor, Atlas One Solutions, to
    drjoeldgould@gmail.com. Correct copy: footer has 380-225-5217, David@AtlasOneSolutions.com,
    AtlasOneSolutions.com, vendor-neutral line.
  - 11:19 AM "- No Subject -" -- from David Taylor (no title), to drjoeldgould@gmail.com. Duplicate/old
    copy: same body text, footer has 385-213-7177 only, no website link, no vendor-neutral footer lines.
  - 11:30 AM "Questions" -- from Dr. Joel Gould, to David@lc.atlasonesolutions.com. Reply to the correct
    instant-reply (quoted blockquote shows the 380-225-5217 footer). Asks about membership tier, PEO/payroll
    recommendation, mentions an attached insurance proposal.
  - 11:36 AM "Insurance quote" -- from Dr. Joel Gould, to David@lc.atlasonesolutions.com, attachment
    "Index0_Firebird quote.pdf". Both replies sat only in Conversations; David never saw them in his inbox.
- **24c. Root cause found and fixed.** The duplicate 11:19 AM email is not a second node inside "Intake:
  Instant reply" (that workflow only has one Send Email action, and its execution log shows exactly one send
  for Joel Gould). It comes from a separate, older workflow, "W1 Inbound speed to lead", which has its
  own "Form A or Form B submitted" trigger (the same two forms) and, per its execution log for Joel Gould
  (11:19:47-11:19:54 am), ran: Lead Lane update, Stamp Last Touch, "Email: P-C-0 Instant reply" (the
  385-213-7177 duplicate), "#2 Task: CALL NOW", Internal Notification, Wait 4 hours, reply check, a
  longer nurture sequence (more emails/calls/cooling logic).
  Fixed per the brief: disabled (not deleted) the "Email: P-C-0 Instant reply" action, so the rest of the
  sequence (task, internal notification, nurture) still runs, only the duplicate send is skipped. Saved.
  No description field exists anywhere in GHL's workflow UI (checked Settings tab, Rename modal, list-actions
  menu, only a Name field), so as the closest equivalent to "add a note in the workflow description" the
  workflow was renamed to "W1 Inbound speed to lead (duplicate instant reply removed 2026-09-16)".
- **24d.** Spot-checked "Email 1 - Instant reply" in "Intake: Instant reply": From name "David Taylor, Atlas
  One Solutions", From email "David@AtlasOneSolutions.com", both correct, not lc. The lc. address Joel's
  replies landed at is GHL's own conversation-tracking mechanism (it rewrites Reply-To to an lc.-subdomain so
  replies route into Conversations), not a misconfigured From Email, so 24a's Forwarding Address fix is the
  correct and sufficient remedy. Did not re-run a full 30-workflow From Name/From Email audit this run since
  Runs AY/BA already did that pass (documented in the live log 2026-09-15); flagged as available on request.
- **24e.** Joel Gould's tags/tasks/opportunity/emails: not touched, as instructed.

### Part 21: blank lines in the internal "new intake" notice
- **21a.** Merge keys found in Settings > Custom Fields, folder "Form | Form 1":
  - Services requested: {{contact.which_core_services_would_you_like_included_in_your_quote}}
  - Other policies to quote: {{contact.which_other_policies_would_you_like_reviewed_or_quoted}}
  - Benefits quote: {{contact.review_or_quote_employee_benefits}}
  - On a PEO now: {{contact.on_a_peo_currently}}
  - Pay frequency: {{contact.pay_period_frequency}}
  Updated _BUILD-LOG/cadence-emails-2026-09-13/internal-new-intake.html: Services requested now uses the
  correct key; added the three new lines; softened step 2 of "What to do next" to "If files were uploaded
  (census, payroll report, WC policy) they are under Activity on the contact. If not, ask for them on the
  call." No dashes, no stray phone numbers in the file.
- **21b.** Re-pasted the body into "Intake: Instant reply"'s Internal Notification action via the source code
  dialog, saved, reloaded, confirmed the new merge keys are present and which_service is gone. Publish
  state unchanged.
- **21c.** The CALL NOW task with the wrong "Services requested:" key is not in "Intake: Instant reply"
  (that workflow has no Create Task action at all, confirmed by Fit to Screen on its full canvas). It is
  "#2 Task: CALL NOW" inside "W1 Inbound speed to lead" (found during Part 24's investigation). Its
  description pointed at a different, unpopulated custom field {{contact.services_requested}}, that's why
  it was blank on Joel Gould's task. Fixed to
  {{contact.which_core_services_would_you_like_included_in_your_quote}} and added a line "Phone:
  {{contact.phone}} times {{contact.legal_business_name}}". Saved, reload-confirmed.
- **21d.** INDEX.md and email-templates-map.md already have the correct row for internal-new-intake.html
  from Run BD; subject didn't change, so no edit needed.

### Part 22: State and industry on Form A
- **22a.** Added the built-in contact State element directly after Legal Business Name (it initially dropped
  above Legal Business Name; dragged back into the correct slot). Label "State (main office)", Required.
- **22b.** Added a dropdown mapped to the existing custom field Vertical (Prospecting folder, key
  contact.vertical) directly after State, before DBA/Trade Name. Label "What kind of business is it?", left
  optional, options auto-populated from the field's own current list (17 options, none added, matches read).
- **22c.** Before saving: opened Conditional Logic and reviewed every Show/Hide rule (about 10 rules covering
  PEO, benefits, WC, other insurance, core services). Every rule still resolved to its correct trigger and
  target field names after the two insertions, no blanks or broken targets, so GHL references fields by ID,
  not position, and no repair was needed. Saved the form. Reloaded the public form
  (https://api.leadconnectorhq.com/widget/form/Cxqawj85qg4ULUl64nMc) and confirmed: both new fields show in
  the right place; every conditional section still opens on its trigger (Workers Comp Yes shows
  carrier/expiration fields, Benefits Yes shows broker/carrier fields plus the census section, Other
  insurance Yes shows the policy checklist, core services PEO Payroll/ASO Payroll shows employee
  count/pay frequency fields); nothing else moved. Screenshots in _briefs/assets/run-BE/shots/
  (form-a-top.png, form-a-conditionals-revealed.png).

### Part 23: test
- Submitted Form A at 2026-09-16 19:49:51 MDT as: Run BE / Test Co, david+zzbe@atlasonesolutions.com,
  (702) 555-0198, Legal Business Name "Run BE Test Co", State Texas, industry Construction and trades, one
  core service (ASO Payroll, 5 full-time W-2 employees), Workers Comp No, Benefits Yes, one other policy
  (General Liability). Thank-you page shown about 19:50:01 MDT.
- New contact created: lQgqiCSWxydJGxnpBDu9. Confirmed:
  - Confirmation email sent correctly ("We've got it, Run BE. Here's what happens next", 07:50 PM, from
    David Taylor Atlas One Solutions).
  - CALL NOW task shows "Services requested: ASO Payroll" and "Phone: (702) 555-0198 times Run BE Test
    Co", the Part 21c fix verified working end to end on a real submission. Screenshot in repo shots.
- Test contact deleted (typed DELETE to confirm; 60-day restore window; cascade-deletes its task,
  opportunity, conversation, none of which needed separate cleanup).

## Assumptions
1. Treated "add a note in the workflow description" (Part 24c) as renaming the workflow, since GHL's
   workflow UI has no description field anywhere (Settings tab, Rename modal, list-actions menu all
   checked).
2. Used "Disable action" rather than delete for the duplicate Send Email node in W1, so the rest of that
   workflow's sequence (task, internal notification, longer nurture cadence) keeps running unaffected, the
   brief said "turn its Send Email action off," which Disable satisfies literally and reversibly.
3. Did not re-run a full From Name/From Email audit across all roughly 30 published workflows for Part 24d,
   since Runs AY and BA already completed that normalization pass (documented in the live log). Only
   spot-checked the node directly implicated in this run's issue.
4. Left "Currently offering benefits?" and other optional radios/fields blank during the Part 23 test since
   they weren't specified and aren't required for submission.
5. Chose Workers Comp = No for the test submission (not specified in the brief) to keep the test simple and
   avoid extra upload requirements.

## Skipped
- Nothing in Parts 21, 22, 23 was skipped.
- Part 24d's full workflow re-audit was intentionally narrowed to a spot-check (see Assumption 3).

## Questions for David
1. The W1 "#2 Task: CALL NOW" and its Internal Notification also duplicate, independently of the email
   fix made this run, this same workflow creates a second CALL NOW task and fires a second internal
   notification on every Form A/B submission (confirmed via its execution log for Joel Gould, all three
   actions fired 11:19:47-11:19:54 am). The brief only asked me to fix the duplicate Send Email, so I left
   those two other actions untouched. Do you want the CALL NOW task and Internal Notification actions in
   "W1 Inbound speed to lead" disabled too, so the whole legacy speed-to-lead sequence stops duplicating
   "Intake: Instant reply" entirely, or is there a reason W1's task/notification should stay active alongside
   the new workflow's?
2. W1 Inbound speed to lead is a much bigger workflow than just the email/task/notification, after the
   duplicate instant-reply sequence, it continues into "Replied already?" branching, more nurture emails
   (P-C-2, P-C-3), and cooling-off logic. I did not touch or review any of that downstream sequence this run
   since it was out of scope for Part 24's fix. Worth a dedicated review at some point to confirm it isn't
   overlapping with other nurture workflows (for example "Post-Presentation Email", "Tool-Lead Nurture").
3. The public form's thank-you page still has an em dash ("Thank you, your request has been
   received..." rendered with an em dash on the live page). Run BD flagged this as out of scope before;
   flagging again since it's still there and is a brand-rule violation (no dashes in copy).
4. Reply Address (Settings > Email Services > Reply & Forward Settings) is still empty, only asked to report
   it, not set it. Let me know if you want a value there.
