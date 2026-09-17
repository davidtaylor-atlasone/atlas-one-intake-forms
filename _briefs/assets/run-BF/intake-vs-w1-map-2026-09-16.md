# Intake: Instant reply vs W1 Inbound speed to lead, node map (Run BF Part 25, 2026-09-16)

Both workflows are Published and both trigger on "Form submitted" for the same two forms: Form A ("Atlas
One PEO Prospect Quote Request") and Form B ("Atlas One Accounting, Bookkeeping and Payroll Service
Request"). Every Form A or Form B submission enrolls a contact in both workflows at once. This table lists
every action in each, in order, with the decision for Part 25 and why.

## Intake: Instant reply (id 94b34c50-2ad7-4650-a42d-35a74365555b)

| Workflow | Action | Keep or Disable | Why |
|---|---|---|---|
| Intake: Instant reply | Trigger: Form B submitted (Bookkeeping) | Keep | Only owner of the two form triggers on this workflow. |
| Intake: Instant reply | Trigger: Form A submitted (PEO) | Keep | Same. |
| Intake: Instant reply | Email 1 - Instant reply | Keep | The one confirmation email a prospect should get. Not duplicated anywhere else. |
| Intake: Instant reply | Add Tag (intake-received) | Keep | Tags the contact; no other published workflow triggers on this tag (confirmed by search, see below), so it is not creating a second enrollment anywhere. |
| Intake: Instant reply | Internal Notification (to David) | Keep | This is now the ONLY internal new-intake notice David should get (Part 21/18 rebuilt this body with the full merge fields). W1's copy is being disabled below so there is exactly one. |

## W1 Inbound speed to lead (duplicate instant reply removed 2026-09-16) (id e50ddca0-1bc1-4a4b-a706-f2d02ba27259)

| Workflow | Action | Keep or Disable | Why |
|---|---|---|---|
| W1 | Trigger: Form A or Form B submitted | Keep | Only owner of the lead-lane stamp, last-touch, CALL NOW task and nurture cadence; nothing else builds these. |
| W1 | Lead Lane C Inbound (contact field update) | Keep | Lead lane stamp, not built anywhere else. |
| W1 | Add sequence active (tag) | Keep | Drives the "Suppressed?" and "Replied already?" gates further down; part of W1's own nurture logic. |
| W1 | Stamp Last Touch Date (contact field update) | Keep | Not built anywhere else. |
| W1 | Suppressed? (if/else: Tags includes "cooling 30d" or similar) | Keep | Gate logic, not a duplicate. |
| W1 branch "Suppressed" -> #1 Task: suppressed inbound, decide by hand | Keep | Only fires for suppressed contacts; not a duplicate of the CALL NOW task, which only fires in the "None" branch. |
| W1 branch "Suppressed" -> Email: P-C-0 Instant reply | Already Disabled (Run BE, 2026-09-16) | This was the original duplicate confirmation email (385-213-7177, no footer). Left disabled; still shows in the canvas as "(Disabled)". No change needed this run. |
| W1 branch "None" -> **#2 Task: CALL NOW** | Keep | The only task-creator on a Form A/B submission. "Intake: Instant reply" has no task action. |
| W1 branch "None" -> **Internal Notification** | **Disable this run** | Duplicate of "Intake: Instant reply"'s Internal Notification. David was getting two internal notices per lead (the bug this part fixes). "Intake: Instant reply"'s notice already carries the full merge fields (Part 18/21) and now runs first (its trigger fires the same instant); W1's copy is now redundant. Disabling the action (not deleting the workflow) keeps the audit trail and can be re-enabled if needed. |
| W1 branch "None" -> Wait 4 hours (business hours) | Keep | Part of the nurture cadence; not a duplicate creator. |
| W1 branch "None" -> Replied already? (if/else: Tags includes "reply received") | Keep | Gate logic. |
| W1 -> "Reply received" branch -> END | Keep | Stops the cadence once the prospect replies. |
| W1 -> "None" branch -> #3 Task: Call 2 plus voicemail, Wait 1 day, Email: P-C-2 Inbound Email 2, Wait 2 days, #4 Task: Call 3, Wait 3 days, Email: P-C-3 Inbound Email 3, Add cooling 30d, Remove sequence active, Wait 30 days, Remove cooling 30d, END | Keep | The nurture and cooling sequence Cowork asked to leave untouched. Not reviewed for correctness this run (out of scope), only confirmed it does not create a second task or send a second confirmation email. |

## Other published workflows checked for a Form A, Form B, tag `intake-received`, or tag `form-a-sent` trigger

Searched the full workflow list (30 rows) for every name containing "form", "PEO", "intake", "W1", "prospect", or "quote", and opened each one's trigger. None of the following trigger on Form A submitted, Form B submitted, tag `intake-received`, or tag `form-a-sent`:

| Workflow | Actual trigger | In scope? |
|---|---|---|
| Intake: Send bookkeeping form | Form A submitted, but gated on the "Quote or explore, no obligation" field being "Bookkeeping & accounting" or "Tax strategy & filings" (a sub-slice of Form A) | Fires on Form A, but only Adds Tag then ENDs (no email, no task) - not a duplicate confirmation or task creator, no change needed. |
| Send PEO form on tag | Contact Tag added includes "send-peo-form" | No (tag trigger, not Form A/B or intake-received/form-a-sent). Adds the "form-a-sent" tag itself; nothing triggers on receiving that tag (see below). |
| Send bookkeeping form on tag | Contact Tag added includes "send-bk-form" | No (tag trigger). |
| Intake: service sign up | Form submitted = "Atlas One Service Sign Up" (Form C1) | No. |
| Intake: document build | Form C2 submitted ("Atlas One Build This For Me") | No. |
| Atlas One - Tool Results Capture | Inbound Webhook, no filters | No. |
| Missing Info Follow-up | n/a | Draft, not Published - out of scope. |

No workflow anywhere triggers on tag `intake-received` (the tag "Intake: Instant reply" adds) or on tag
`form-a-sent` (the tag "Send PEO form on tag" adds after its own separate welcome sequence). No third
duplicate task-creator or confirmation-sender was found.

## Change made this run

W1's "Internal Notification" action: **Disabled**. Everything else in both workflows left as is.
