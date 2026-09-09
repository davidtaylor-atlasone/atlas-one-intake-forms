# Run G checkpoints (prospecting workflows W0 to W7)

Run started 2026-09-08. Working at app.ridethehightide.com, location AzTPxnK2vSUj19jYoDmR.

## Standing decisions for this run (David's instructions override the brief)
- **Nothing is Published.** Every workflow is saved as **Draft**. The brief and runbook say Publish
  after each test; David reserves publishing as the one production step after Cowork audits.
- **Committing to git at each checkpoint.** The brief says "commit nothing to git"; David asked for
  a commit per checkpoint. Checkpoint notes live here; the audit report also goes to
  prospecting-workflows-W1-W7-REPORT.md.
- Every Send SMS action is built and left **disabled**.
- No `open`/`open -R`/osascript. One Chrome tab only.

## Checkpoint 1: fields and tags

### Navigation finding
Direct URL loads of /settings/* spin forever ("If you are having issues loading the app").
In-app navigation (Dashboard, then click Settings, then the left menu) loads fine. All settings
work in this run was done by clicking, not by typing URLs.

### Custom fields
Already existed in the Prospecting folder (created Sep 08 by an earlier pass), verified not rebuilt:

| Field | Type | Options read back |
|---|---|---|
| Lead Lane | Dropdown (single) | A Referral, B Trigger, C Inbound, D Cold, E Lost |
| Brand Identity | Dropdown (single) | Atlas One, Cornerstone |
| Vertical | Dropdown (single) | Audiology, Dental Ortho Optometry ENT, Construction, Technology, Hospitality, Professional Services, Other |
| Trigger Type | Dropdown (single) | WC renewal, Benefits renewal, New location, Hiring, Ownership change, Vendor complaint, Other |

Created this checkpoint (all Contact object, Prospecting folder). Field count went 747 to 758.

| Field | Type | Key |
|---|---|---|
| Personal Line | Multi line | {{contact.personal_line}} |
| Vertical Opener | Multi line | {{contact.vertical_opener}} |
| Vertical Proof | Multi line | {{contact.vertical_proof}} |
| Vertical Tool | Single line | {{contact.vertical_tool}} |
| Referral Partner Name | Single line | {{contact.referral_partner_name}} |
| Trigger Date | Date picker | {{contact.trigger_date}} |
| Last Touch Date | Date picker | {{contact.last_touch_date}} |
| Next Touch Date | Date picker | {{contact.next_touch_date}} |
| Benefits Renewal Date | Date picker | {{contact.benefits_renewal_date}} |
| Sequence Step | Number | {{contact.sequence_step}} |
| Lifted Suppression | Checkbox (option "Yes") | {{contact.lifted_suppression}} |

Vertical Proof was first created as Single line by mistake; GHL will not let you change a field's
type after creation, so it was deleted and rebuilt as Multi line. Key survived unchanged.

### Tags (11 created, count 11 to 22)
sms consent, cell verified, cooling 30d, cooling 60d, cooling 90d, hold 6m, dnc,
sequence active, batch ready, reply received, not interested.

**GHL lowercases every tag name on save.** The runbook's capitalisation (`SMS consent`,
`Sequence Active`, `DNC`) cannot be preserved. Workflow steps will reference the lowercase forms.
No contact has been tagged `sms consent` and none will be.

### Deviations and assumptions logged at checkpoint 1
1. **WC Renewal Date does not exist under that name.** The runbook says it "already exists from
   Form A; reuse". What exists is **`Workers' Comp Policy Expiration Date`** (Date picker, folder
   Form | Form 1, key {{contact.workers_comp_policy_expiration_date}}). Assumed that is the same
   thing and will be used for W3a's WC branch. Not duplicated.
2. **Benefits Renewal Date did not exist as a date.** Form A has `Benefits Renewal Month`
   (Single line, a month name). A month string cannot drive W3a's minus 120/90/60 date offsets,
   so a real `Benefits Renewal Date` date picker was created. Form A still writes the month field;
   the two are not connected yet. See deferred question 1.
3. **Referral Partner is an Opportunity dropdown**, not a contact text field, so it cannot hold an
   arbitrary referrer name and will not merge reliably into a contact triggered email. Created
   `Referral Partner Name` (contact, single line) for the email merge and left the Opportunity
   dropdown alone for pipeline reporting. Templates use {{contact.referral_partner_name}}.
4. **The brief says 24 templates; the runbook table enumerates 23.** Built 23.

### Templates prepared offline (not yet loaded into GHL)
23 bodies generated from the live "Booking: confirm and remind" Email C1 HTML as the wrapper base,
so header logo, periwinkle table button, text signature, ONE CALL SOLVES EVERYTHING line and Lehi
footer match Run E exactly. Checked programmatically: zero em or en dashes in any subject or body;
the three W7 bodies contain no "Atlas One", no "atlasonesolutions", no "Hearvana", and no credit
mechanics. W7 uses a Cornerstone text wordmark in the header because no Cornerstone logo asset
exists in the source files (deferred question 2).

---

## Checkpoint 2: tool hosting verified, W6 and W6b built

### Tools are live
`git push origin main` put commit b8d8aaa on the remote. All three calculators returned
**200 on the first poll**, so the `[link]` placeholders in Appendix A can be replaced with
real URLs in W0:

- https://forms.atlasonesolutions.com/tools/retention-cost/
- https://forms.atlasonesolutions.com/tools/vendor-consolidation/
- https://forms.atlasonesolutions.com/tools/wc-premium-check/

### Builder findings that apply to every workflow in this run
1. **The builder is a cross-origin iframe** (`client-app-automation-workflows.leadconnectorhq.com`).
   JavaScript, the accessibility tree and the `find` tool cannot reach inside it. Everything
   is coordinate clicks on screenshots.
2. **Dropdown options need two clicks** (first hovers, second selects), or `type` then
   `Down` then `Return`. A single click silently does nothing. Where both failed, opening the
   dropdown and pressing `Return` on the highlighted first item worked.
3. **Set the action NAME before selecting a tag.** Renaming the action after picking a tag
   clears the tag chip.
4. **Wait units are seconds / minutes / hours / days only.** There is no "months". 6 months
   is built as **180 days**. Wait defaults to `0 minutes`, so both the number and the unit
   have to be set every time.
5. **Task due date is required** and is Value + Unit (Days/Weeks/Months/Years) + optional
   time. "Due today" is `0 Days`. Task **Description is also required**; the runbook only
   gives titles, so a one line description was written for each task.
6. **If/Else branches do not rejoin.** Each branch runs to its own END. Anything the runbook
   lists as a step "after" an If/Else has to be built *inside* the branch it belongs to.
7. **Tag conditions:** operators are Includes / Does not include / Is not empty / Is empty.
   Selecting several tags under **Includes means ALL of them (AND)**. The runbook's
   "is one of" therefore needs one segment per tag joined with **OR**, not one Includes with
   five tags. This affects W1 step 4, W2 step 2, W3 step 2 and W4 step 1.
8. **Date field conditions:** operators are only Is / Is not / Is not empty / Is empty, but
   the value side offers Today, Tomorrow, Yesterday, On, After, Before, After date,
   Before date, and Before/After take a number plus Days/Weeks/Months/Years. There is no
   single "within the last N days" operator.

### W6 Suppression and caps  (Draft, id 32015c79-5132-43ae-9aa2-09f2321a8426)
Allow re-entry ON (it is ON by default; not changed).

Triggers, three:
1. `Customer Replied`, no filters (no filter = any channel).
2. `Contact tag` named "Tag added: not interested", filter Tag added includes `not interested`.
3. `Contact tag` named "Tag added: dnc", filter Tag added includes `dnc`.

Actions:
| # | Card | Settings |
|---|---|---|
| 1 | Remove contact tag "Remove sequence active" | tag `sequence active` |
| 2 | Remove from workflow "Remove from all other workflows" | **All workflows except current workflow** |
| 3 | If/Else "Route by reason" | 3 branches |

Branch **DNC** (`Tags` includes `dnc`): Update contact field "Clear Next Touch Date",
action type **Clear field data**, field `Next Touch Date`. Then END.

Branch **Not interested** (`Tags` includes `not interested`): Add contact tag `hold 6m`
then Wait **180 days (6 months)** then Remove contact tag `hold 6m`. Then END.

Branch **None** (the reply case): Add contact tag `reply received`; Add task
"Task: read and respond" (title `Reply from {{contact.first_name}} {{contact.last_name}}: read and respond`,
assigned David Taylor, due 0 Days); Internal notification, type **Notification** (app push),
title `Reply received`, message `Reply from {{contact.company_name}}`, redirect page
**Conversation**, to Particular user **David Taylor**. Then END.

**Deviation, logged:** the build sheet says Remove From Workflow > **All workflows**.
Chosen instead: **All workflows except current workflow**. "All workflows" includes W6
itself, which ends W6's own execution at step 2, so the branch that adds `hold 6m`, the
reply task and the notification would never run. Excluding the current workflow keeps the
brake identical for every other sequence and preserves the notification. Reverse it only
if you decide the notification does not matter.

**Deviation, logged:** the build sheet puts Internal Notification as top level action 4,
after the If/Else. Because branches do not rejoin (finding 6), and because its body is
`Reply from {{contact.company_name}}`, it was built **inside the None (reply) branch**,
next to the reply task. A DNC or Not interested tag therefore does not ping David, which
matches the intent of the copy.

**Deviation, logged:** notification channel is **Notification (app push)**, not SMS.
The build sheet says "SMS or app push" and no SMS may be enabled before A2P is Approved.

### W6b Sequence stalled  (Draft, id 3e30bb6d-29fd-4a00-99fd-9a25c1ec6ddc)
Allow re-entry ON (default).

Trigger: `Contact tag` named "Tag added: sequence active", filter Tag added includes
`sequence active`.

Actions:
| # | Card | Settings |
|---|---|---|
| 1 | Wait "Wait 5 days" | set period of time, 5 days |
| 2 | If/Else "Touched recently?" | see below |

Branch **Touched in last 5 days**: `Last Touch Date` **Is not** **Before** **5 Days**.
No steps, ends. Branch **None** (that is, the contact WAS last touched more than 5 days
ago, so the sequence has stalled): Add task "Task: sequence stalled", title
`Sequence stalled: {{contact.company_name}}`, assigned David Taylor, due 0 Days.

**Deviation, logged:** the build sheet writes the condition as `Last Touch Date` **is
within the last** 5 days with the task in the else. GHL has no "is within the last"
operator (finding 8). The equivalent built is `Is not` + `Before 5 Days`, which is true
when the contact HAS been touched inside the window, so the true branch ends and the
**None** branch carries the stalled task. Same logic, expressed with the operators that
exist.

### Still open at this checkpoint
- A2P status not yet read (Settings > Phone Numbers > Trust Center).
- No SMS action exists yet; the first ones appear in W1 and W4 and will be built disabled.

---

## Checkpoint 3: W0 Set vertical lines

### W0 Set vertical lines  (Draft, id de389546-ad9f-42a2-9784-bc231014c8a0)
Allow re-entry ON (default).

**Trigger:** `Contact changed`, named "Vertical changed", filter **Vertical has changed**.
(The trigger type is called *Contact changed*, not "Contact Field Updated"; its operators
are only **Has changed** and **Has changed to**. "Has changed" is the any-value form the
build sheet asked for.)

**Action 1: If/Else "Route by vertical"**, seven branches, each `Vertical` **Is** <value>:
Audiology, Dental Ortho Optometry ENT, Construction, Technology, Hospitality,
Professional Services, and the built-in **None** branch for Other and blank.

**Inside each branch: one `Update contact field` action** (action type **Update field data**)
carrying all three values at once, rather than three separate actions. GHL's update action
takes a list of fields, so one card per branch is the same result with a third of the steps.

| Branch | Action name | Fields set |
|---|---|---|
| Audiology | Set Audiology lines | Vertical Opener, Vertical Proof, Vertical Tool |
| Dental Ortho Optometry ENT | Set Dental Ortho Optometry ENT lines | same three |
| Construction | Set Construction lines | same three |
| Technology | Set Technology lines | same three |
| Hospitality | Set Hospitality lines | same three |
| Professional Services | Set Professional Services lines | same three |
| None | Set generic lines (Other and blank) | same three |

All 21 values are the Appendix A text verbatim, **with the `[link]` placeholder replaced by
the live URL**:

| Branch | Vertical Tool value |
|---|---|
| Audiology | `Retention Cost calculator: https://forms.atlasonesolutions.com/tools/retention-cost/` |
| Dental Ortho Optometry ENT | `Retention Cost calculator: https://forms.atlasonesolutions.com/tools/retention-cost/` |
| Construction | `WC premium check: https://forms.atlasonesolutions.com/tools/wc-premium-check/` |
| Technology | `Vendor Consolidation calculator: https://forms.atlasonesolutions.com/tools/vendor-consolidation/` |
| Hospitality | `Retention Cost calculator: https://forms.atlasonesolutions.com/tools/retention-cost/` |
| Professional Services | `Vendor Consolidation calculator: https://forms.atlasonesolutions.com/tools/vendor-consolidation/` |
| None (generic) | `Vendor Consolidation calculator: https://forms.atlasonesolutions.com/tools/vendor-consolidation/` |

**All seven action cards were reopened and read back** after saving; each shows Vertical
Opener, Vertical Proof and Vertical Tool populated. Deferred question 5 in the report
(placeholder links) is now closed for W0. **The Email 3 templates still merge
`{{contact.vertical_tool}}`, so they pick the real URL up automatically; no template edit
is needed.**

### More builder findings
9. **Typing `/` opens GHL's merge-tag picker** inside any value field. Every tool URL ends
   in `/`, so the picker was left open over the Save button each time. Clicking another
   field (or Escape then another field) closes it; only then does Save register.
10. **"Error while saving the workflow"** appeared once on the last branch. It was
    transient: reopening the action showed all three fields stored and the header read
    Saved. Worth re-reading any action that throws it rather than redoing the work.
11. The canvas **zoom must be near 100%** for the `+` buttons to respond. At 154% and 190%
    clicks on `+` did nothing.
12. Clicking the panel's **X can open the Workflow AI sidebar** instead of closing; the
    left sidebar toggle (top left, next to Workflows list) closes that.

### Freezes
Two in a row while trying to open Create workflow > Start from Scratch after the W6b
checkpoint. Recovered per the runbook: Dashboard, then Automation in the left menu; when
that was not enough, a full reload of the location dashboard URL followed by clicking
Automation. Third attempt succeeded, so the counter reset. No checkpoint was lost.

---

## Checkpoint 4: W1 Inbound speed to lead (PARTIAL) and run stopped here

### W1 Inbound speed to lead  (Draft, id e50ddca0-1bc1-4a4b-a706-f2d02ba27259)

**Settings:** Allow re-entry **OFF** (turned off, verified). **Stop on response ON** (see
the Goal decision below). Allow multiple opportunities left at its default ON.

**Trigger (one, not two):** `Form submitted`, named "Form A or Form B submitted", filter
**Form is** — is any of:
- `Atlas One — PEO / Prospect Quote Request`  (Form A)
- `Atlas One — Accounting, Bookkeeping & Payroll — Service Request`  (taken as Form B)

**Deviation, logged:** the build sheet says Form A and Form B need **two separate
triggers** because "filters inside a single trigger are ANDed". That is true of separate
filter *rows*, but the **Form is** filter is itself a multi-select and the saved trigger
reads `Form is is any of [...]` — an OR. One trigger is therefore exactly equivalent to
the two the sheet asks for, with half the surface to maintain. The third form on the
location, `Form 0`, was deliberately not included.

**Assumption to confirm:** the build sheet never names Form B. The location has exactly
three forms; `Atlas One — Accounting, Bookkeeping & Payroll — Service Request` is the only
plausible second intake form, so it was used. **If Form B is meant to be something else,
this filter is the one thing to change.**

**Deviation, logged (the Goal step):** the sheet wants a Goal step "Event: Customer
Replied, on match skip to end" at the top of every sequence workflow. GHL's **Goal event**
action exists, but its goal types are: Received an Email Event, Clicked a trigger link,
Added a contact Tag, Removed a contact Tag, Appointment status, Payment Received, Form
Submitted, Document Status, Invoice paid, Review request clicked, **User Replied**, Task
status. There is **no Customer Replied goal** — "User Replied" is the staff user, not the
contact, so using it would have been wrong. Used instead: **Settings > Stop on response
= ON**, whose own description is "Ends workflow for a contact if the contact responds to a
message that is sent from this workflow". That is the Goal step's intent, enforced at the
workflow level rather than as a canvas node. W6 remains the global backstop (Customer
Replied removes the contact from all other workflows). **Apply the same setting to W2, W3,
W4, W5 and W7 in place of their Goal steps.**

**Actions built and saved (3 of 21):**

| # | Card | Settings |
|---|---|---|
| 1 | Update contact field "Lead Lane C Inbound" | field `Lead Lane` = **C Inbound** |
| 2 | Add contact tag "Add sequence active" | tag `sequence active` |
| 3 | Update contact field "Stamp Last Touch Date" | field `Last Touch Date` = **Current Date** |

**Finding 13.** A date field in Update contact field does not take `{{right_now.date}}`.
Its value picker offers **Custom Date / Current Date / Specific Date**; **Current Date** is
the native equivalent and is what was used. Use it everywhere the sheet writes
`{{right_now.date}}`.

### Actions 4 to 21 of W1 are NOT built
Still to do, per the build sheet: the suppression If/Else and its task, the P-C-0 Instant
reply send, the two SMS gates, the CALL NOW task and notification, the business hours wait,
the reply check, and the rest of the cadence through `cooling 30d`.

**Design problem to settle before building step 6 and step 15 (the SMS gates).**
Branches in this builder **do not rejoin** (finding 6). The sheet's "If SMS consent then
Send SMS" followed by more steps cannot be expressed inline: whatever follows the If/Else
has to be duplicated into every branch. Three options, none free:
1. Put the Send SMS inline and **disabled**, with no consent branch, and rely on the
   `sms consent` tag being what qualifies a contact for SMS at enable time. Simplest, but
   the gate is a procedure rather than a control.
2. Build the branch and **duplicate the tail** of the sequence into both branches (15 steps
   after step 6, 6 steps after step 15). Faithful, but doubles the maintenance surface.
3. Move both SMS sends to the **end** of their segment so the tail to duplicate is empty.
   Changes the cadence order slightly.
**This needs David's call.** Nothing was built for steps 6 and 15 rather than guess.

### Not started
**W2, W3, W3a, W4, W5, W7 have not been created.** The run stopped here; see the report
for exactly where to resume.
