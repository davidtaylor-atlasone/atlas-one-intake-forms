# RUN-GHL report: Run BF, 2026-09-16

Two parts this run: Part 25 (one owner per action on a Form A/B submission, fixing the double internal
notice bug) and Part 26 (thank you page copy, no dashes).

## Part 25: one owner per action

### Built

1. Read "Intake: Instant reply" and "W1 Inbound speed to lead (duplicate instant reply removed 2026-09-16)"
   end to end (Fit to Screen, then node by node) and wrote
   `_BUILD-LOG/intake-vs-w1-map-2026-09-16.md`: one table per workflow, one row per action, columns Workflow,
   Action, Keep or Disable, Why, plus a table of every other published workflow checked for a Form A, Form B,
   tag `intake-received`, or tag `form-a-sent` trigger.
2. Searched the full workflow list (30 published/draft rows) for every name containing "form", "PEO",
   "intake", "W1", "prospect", "quote", "speed", or "sequence" and opened each one's trigger. Confirmed only
   two workflows trigger on Form A or Form B submitted: "Intake: Instant reply" and W1. No workflow anywhere
   triggers on tag `intake-received` (the tag Intake: Instant reply adds) or tag `form-a-sent` (the tag Send
   PEO form on tag adds after its own separate welcome sequence). No third duplicate task-creator or
   confirmation-sender exists.
3. Made the one change the brief called for: in W1, disabled the "Internal Notification" action (the node
   between "#2 Task: CALL NOW" and "Wait 4 hours"). Saved, then verified by leaving the workflow entirely
   (Automation > Workflows, not a direct URL — direct workflow deep links 404 in this ghl-browser profile)
   and reopening it fresh: the node now reads "Internal Notification (Disabled)". "#2 Task: CALL NOW" is
   unchanged and still active — it is the only task-creator on a Form A/B submission.
4. Left everything else in both workflows untouched: W1's lead lane stamp (Lead Lane C Inbound), last touch
   stamp, "Suppressed?" gate, "Replied already?" gate, and the full P-C-2/P-C-3 nurture and cooling sequence
   were not modified, per Cowork's instruction to leave the nurture logic alone this run. "Intake: Instant
   reply"'s Email 1, Add Tag (intake-received), and its own Internal Notification (now the sole new-intake
   notice) were not touched.

### Verification

- The map file: `_BUILD-LOG/intake-vs-w1-map-2026-09-16.md`.
- Node-list read-back after a fresh reload (not a cached tab) confirms the disable persisted:
  "Internal Notification (Disabled)" and "#2 Task: CALL NOW" (active) both present in W1, in that order,
  right after the "None" branch of the Suppressed? gate.
- **Not verified end to end with a live submission.** See Skipped below.

### Skipped

- **Part 25c (the live test submission) was not completed.** Filling the Form A test data (Run BF Test Co,
  david+zzbf@atlasonesolutions.com, (702) 555-0197, Colorado) worked, but the Claude Code auto-mode
  permission classifier denied the "Get My Quote" submit click as a "Real-World Transaction", even though
  this is the same authorized test-submission pattern used and approved in Runs BD and BE (a `david+zz...@`
  test address that gets deleted afterward). I did not try to route around the block (for example by
  submitting via Enter instead of the button) since that is the same action under a different name. The
  form was left filled but unsubmitted.
- Because of that, Part 25's fix is verified by reading the workflow structure and confirming the disabled
  state persisted after a save and reload, but NOT by watching an actual Form A submission produce exactly
  one confirmation email, one internal notice, one CALL NOW task, and one opportunity. Run BE's test contact
  (used for the last live verification of this trigger) was already deleted before this run started, so
  there was no existing execution log to fall back on either.

## Part 26: thank you page copy, no dashes

### Built

- **Form A** (`Cxqawj85qg4ULUl64nMc`, Atlas One — PEO / Prospect Quote Request): On Submit message
  rewritten from "Thank you — your request has been received. An Atlas One Solutions specialist will
  review your information and reach out shortly with next steps." to the brief's exact text:
  "Thank you. Your request has been received. David will review it and reach out within one business day."
  Saved; confirmed by leaving the form (Back to the forms list, which showed the row's Updated timestamp
  jump to the save time) and reopening it fresh.
- **Form B** (`V2EzO3FlRnsthXfHUT7g`, Atlas One — Accounting, Bookkeeping & Payroll — Service Request): On
  Submit message rewritten the same way to: "Thank you. Your bookkeeping details are in. David will reach
  out within one business day." Saved.
- **C1** (`nmXxvIegefND7h0ULeXW`, Atlas One — Service Sign Up) and **C2** (`hxPZ7HEhqG57aoS61MqM`, Atlas
  One — Build This For Me): both already read "Thank you. Your request has been received and David will be
  in touch within one business day." with no dash of any kind (confirmed by scanning the actual text nodes
  for hyphen, en dash, and em dash code points — none found). This was fixed in an earlier run (Run AN's
  answer (1), "yes, remove the em dash on the shared thank-you page"). No edit was needed or made.

### Verification

Read all four back from the form builder's own "On Submit" preview panel (a live rendering of the saved
message, not just the editor field) rather than the live public form, since the builder's preview is the
faster and equally authoritative source for a message that only shows after a real submission. Window was
1600px wide throughout (above the 1512px minimum).

- Form A preview: "Thank you. Your request has been received. David will review it and reach out within
  one business day."
- Form B preview: "Thank you. Your bookkeeping details are in. David will reach out within one business
  day."
- C1 preview: "Thank you. Your request has been received and David will be in touch within one business
  day."
- C2 preview: "Thank you. Your request has been received and David will be in touch within one business
  day."

None of the four contain a hyphen, en dash, or em dash.

## Assumptions

1. Read Part 25's "confirm ... on a fresh submission" as requiring the actual submit click, which the
   permission classifier blocked; I did not substitute a different action to force it through, and left it
   as a Skipped item rather than guess at a workaround.
2. For Part 26's "read the thank-you text from the form's own preview if the builder offers one, otherwise
   report the saved text": the form builder's On Submit tab renders a live "Preview" box next to the
   editor, which is the builder's own preview. I used that rather than reloading the public form and
   submitting nothing, since submitting nothing on the public form doesn't reveal the thank-you text at all
   (it only shows after a real submission) — the builder's preview was the only way to read it back without
   another live submission.
3. C1 and C2 needed no edit since they already carry the exact dash-free copy from an earlier run; I did not
   rewrite them to a different wording just to "confirm" a change, since the brief says "keep their current
   meaning, remove the dash" and there was no dash to remove.
4. Direct deep-link navigation to `/automation/workflow/<id>` and `/automation/workflows` 404s in this
   ghl-browser Playwright profile even mid-session; all verification reloads went through the app shell
   (home page > Automation nav > workflow row click) instead, consistent with the "no direct deep URLs"
   rule already in the brief.

## Questions for David

1. Part 25c (the fresh test submission) is unverified end to end. Can you either (a) grant the Bash/browser
   permission for GHL public form test-submissions so a future run can complete this pattern of test, or
   (b) submit the Form A test yourself (Run BF Test Co, david+zzbf@atlasonesolutions.com, (702) 555-0197,
   Colorado) and let a future run read the result from the execution logs / your inbox, or (c) confirm you're
   fine trusting the structural verification (the disabled node persisted after reload) without a live run?
2. Run BE's open questions (from its report) are still open: whether to also disable W1's duplicate CALL NOW
   task and Internal Notification actions beyond what Part 25 asked for (Part 25 only asked to disable the
   Internal Notification, which is now done; W1's own task creator, "#2 Task: CALL NOW", was explicitly kept
   per this run's brief since "Intake: Instant reply" has no task action) — flagging again in case that
   answer changes.
3. W1's downstream nurture sequence (P-C-2, P-C-3, cooling, the "suppressed inbound" branch) still has not
   been reviewed for correctness this run or last — only confirmed it does not create a second task or
   confirmation email. Worth a dedicated review pass if it hasn't run recently.
4. The Reply Address setting on Email Services (flagged in Run BE) — Cowork's answer this run confirmed
   leaving it empty on purpose; no further action needed, just confirming that's still current.
