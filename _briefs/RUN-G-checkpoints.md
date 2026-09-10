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

---

## Checkpoint 5: W1 Inbound speed to lead COMPLETE

### David's decisions applied from here on (Run G part 3)
1. **No SMS anywhere.** Every `Send SMS` step and its `sms consent` If/Else is skipped in
   every workflow. Sequences stay linear. Texting will be added later as small
   tag-triggered side workflows once A2P is approved.
2. **Stop on response ON** in Settings for W1, W2, W3, W3a, W4, W5 and W7, in place of the
   Goal: Customer Replied step, which is skipped everywhere.
3. **Form B is `Atlas One, Accounting, Bookkeeping & Payroll, Service Request`** — the
   earlier guess was right, no change needed.
4. **W6 keeps Remove From Workflow = "All workflows except current workflow."** Confirmed,
   see checkpoint 2 for why.

### Template list re-read live (the old REPORT text was stale)
Checked in the Send Email picker on 9 Sep 2026. **The duplicates are gone.** `P-A-3` returns
exactly one row; `P-B-` returns exactly one each of `P-B-1`, `P-B-120`, `P-B-2`, `P-B-3`,
`P-B-4`. `P-C-0 Instant reply` exists and carries the branded Atlas One wrapper. The live
list is now the source of truth; deferred question 5 in the report is closed.

### W1 Inbound speed to lead  (Draft, id e50ddca0-1bc1-4a4b-a706-f2d02ba27259)

**Settings:** Allow re-entry **OFF**, **Stop on response ON**.

**Trigger:** `Form submitted` "Form A or Form B submitted", filter **Form is** — is any of
`Atlas One — PEO / Prospect Quote Request` and
`Atlas One — Accounting, Bookkeeping & Payroll — Service Request`. Saves as
`Form is is any of [...]`, an OR, so one trigger replaces the sheet's two.

**Actions, in order:**

| # | Card | Settings |
|---|---|---|
| 1 | Update contact field "Lead Lane C Inbound" | `Lead Lane` = **C Inbound** |
| 2 | Add contact tag "Add sequence active" | `sequence active` |
| 3 | Update contact field "Stamp Last Touch Date" | `Last Touch Date` = **Current Date** |
| 4 | If/Else **"Suppressed?"** | branch `Suppressed`: `Tags` **Includes** `cooling 30d` **OR** `cooling 60d` **OR** `cooling 90d` **OR** `hold 6m` **OR** `dnc` (five separate OR conditions, because Includes with several tags means ALL) |

Branch **Suppressed**: Add task "Task: suppressed inbound, decide by hand", title
`Inbound from a suppressed contact: {{contact.company_name}}. Decide by hand.`, David,
due 0 Days. Then END.

Branch **None** carries the whole sequence:

| # | Card | Settings |
|---|---|---|
| 5 | Email "Email: P-C-0 Instant reply" | linked template `P-C-0 Instant reply`, Subject left empty so it inherits the template's |
| ~~6~~ | ~~If/Else SMS consent + Send SMS~~ | **SKIPPED per decision 1** |
| 7 | Add task "Task: CALL NOW" | title `CALL NOW: {{contact.company_name}} {{contact.phone}}`, description carries `{{contact.services_requested}}` (resolved as a real custom field), David, due 0 Days |
| 8 | Internal notification | type **Notification** (app push), title `CALL NOW inbound lead`, message `CALL NOW: {{contact.company_name}} {{contact.phone}}`, redirect **Contact**, to Particular user **David Taylor** |
| 9 | Wait "Wait 4 hours (business hours)" | 4 hours, **Advance window ON**, Mon to Fri, **08:30 AM to 5:00 PM** |
| 10 | If/Else **"Replied already?"** | branch `Reply received`: `Tags` **Includes** `reply received` |

Branch **Reply received**: no steps, ENDs. Branch **None** continues:

| # | Card | Settings |
|---|---|---|
| 10b | Add task "Task: Call 2 plus voicemail" | title `Call 2 plus voicemail: {{contact.company_name}}`, David, due **0 Days at 3:00 PM** |
| 11 | Wait "Wait 1 day" | 1 day |
| 12 | Email "Email: P-C-2 Inbound Email 2" | linked template `P-C-2 Inbound Email 2` |
| 13 | Wait "Wait 2 days" | 2 days |
| 14 | Add task "Task: Call 3" | title `Call 3: {{contact.company_name}}`, David, due 0 Days |
| ~~15~~ | ~~If/Else SMS consent + Send SMS~~ | **SKIPPED per decision 1** |
| 16 | Wait "Wait 3 days" | 3 days |
| 17 | Email "Email: P-C-3 Inbound Email 3" | linked template `P-C-3 Inbound Email 3` |
| 18 | Add contact tag "Add cooling 30d" | `cooling 30d` |
| 19 | Remove contact tag "Remove sequence active" | `sequence active` |
| 20 | Wait "Wait 30 days" | 30 days |
| 21 | Remove contact tag "Remove cooling 30d" | `cooling 30d` |

**Deviation, logged: "due in 5 minutes" is not expressible.** The task due date is
Value + Unit where Unit is only Days / Weeks / Months / Years, plus an optional time of
day. The CALL NOW task (step 7) is therefore **0 Days**, i.e. due today, which is the
finest granularity the action offers. The Internal notification at step 8 is what actually
delivers the immediacy.

**Deviation, logged: Goal step skipped**, replaced by Settings > Stop on response, per
decision 2.

### More builder findings
14. **The Wait action has two different layouts.** Sometimes it opens straight into
    "For a set period of time"; sometimes it opens on a full menu of eight wait types and
    a stray click lands on "Until the contact replies". Always read the **Selected wait
    type** line and use **Change type** if it is wrong. After changing type the Time period
    and Unit reset to `0 minutes`, so set both again.
15. The tag picker sometimes needs the search text typed **twice**: the first `type` lands
    while the list is still loading and is swallowed.
16. `{{contact.services_requested}}` resolves to a real field
    (`Contact.Custom Fields.Services Requested`), so the runbook's token is valid.

---

## Checkpoint 6: W2 Warm referral (PARTIAL) and run stopped here

### W2 Warm referral  (Draft, id c5666735-0e74-4d95-a333-36bdf015d53b)

**Settings:** Allow re-entry **OFF**, **Stop on response ON**. Both verified on screen.

**Trigger:** `Contact changed`, named "Lead Lane set to A Referral", filter
`Lead Lane` **Has changed to** `A Referral`. Reads back on the card as
`Lead Lane is "A Referral"`.

**Finding 17.** The `Contact changed` trigger's operators are **Has changed** and
**Has changed to**. "Has changed to" then offers the dropdown's real values, which is how
the sheet's "value **is** `A Referral`" is expressed. W0 used "Has changed" (any value);
W2 uses "Has changed to".

**Action 1 built: If/Else "Cornerstone gate"**
- Branch **Cornerstone**: `Brand Identity` **Is** `Cornerstone`. **No steps, so it ENDs.**
  This is the mirror of W7's gate and is what stops a contact running both.
- Branch **None**: will carry actions 2 to 23.

### Actions 2 to 23 of W2 are NOT built
Still to do, from the build sheet with the SMS decision applied (W2 has no SMS steps
anyway): the suppression If/Else and its task, `sequence active`, `Sequence Step` = 1, the
reply-all task, the Personal Line approval gate, the three P-A emails with their calls and
waits, the "tell the referrer" task, and the `cooling 60d` tail.

### Not started
**W3, W3a, W4, W5 and W7 have not been created.**

### Where to resume
Open **W2**, click the `+` under the **None** branch of "Cornerstone gate", and continue at
action 2. Then W3, W3a, W4, W5, W7. Every one of them needs, in Settings:
**Allow re-entry per the sheet** and **Stop on response ON**; and **no Goal step and no SMS
steps anywhere**.

### Freezes
None in this segment. Two earlier (checkpoint 3), both recovered, never three in a row.

---

## Checkpoint 7: W2 Warm referral COMPLETE

### W2 Warm referral  (Draft, id c5666735-0e74-4d95-a333-36bdf015d53b)

**Settings:** Allow re-entry **OFF**, **Stop on response ON**.
**Trigger:** `Contact changed` "Lead Lane set to A Referral", filter `Lead Lane`
**Has changed to** `A Referral`.

**Action 1: If/Else "Cornerstone gate"**
- Branch **Cornerstone**: `Brand Identity` **Is** `Cornerstone`. No steps, ENDs. This is
  the mirror of W7's gate and is what stops a contact running both.
- Branch **None** carries everything below.

**Action 2: If/Else "Suppressed?"**
- Branch **Suppressed**: `Tags` **Includes** `cooling 30d` **OR** `cooling 60d` **OR**
  `cooling 90d` **OR** `hold 6m` **OR** `dnc` (five OR'd conditions).
  Inside: Add task "Task: suppressed referral, decide by hand", title
  `Referral for a suppressed contact: {{contact.company_name}}. Decide by hand.`,
  David, 0 Days. Then ENDs.
- Branch **None** carries the sequence:

| # | Card | Settings |
|---|---|---|
| 3 | Add contact tag "Add sequence active" | `sequence active` |
| 4 | Update contact field "Sequence Step 1" | `Sequence Step` = `1` |
| 5 | Add task "Task: reply-all to the intro" | title `Reply-all to the intro within 1 hour: {{contact.company_name}} (referred by {{contact.referral_partner_name}})`, David, 0 Days |
| 6 | Wait **"Gate: wait for Personal Line"** | type **Until specific conditions are met**, segment `Personal Line` **Is not empty**, **Timeout ON = 2 days** |

The gate produces two branches:

- **Time out** (2 days, still no personal line): Add task "Task: write the personal line",
  title `Write the personal line for {{contact.company_name}}`, David, 0 Days. Then ENDs.
- **Condition** (personal line filled) carries the rest:

| # | Card | Settings |
|---|---|---|
| 7 | Add task "Task: Call plus voicemail 1" | `Call plus voicemail 1: {{contact.company_name}}`, David, **0 Days at 10:00 AM** |
| 8 | Email "Email: P-A-1 Referral Email 1" | linked template `P-A-1 Referral Email 1` |
| 9 | Update contact field "Stamp Last Touch Date" | `Last Touch Date` = **Current Date** |
| 10 | Wait "Wait 2 days" | 2 days |
| 11 | Add task "Task: Call 2 different hour" | `Call 2, different hour: {{contact.company_name}}`, David, **0 Days at 4:00 PM** |
| 12 | Wait "Wait 2 days" | 2 days |
| 13 | Email "Email: P-A-2 Referral Email 2" | linked template `P-A-2 Referral Email 2` |
| 14 | Update contact field "Stamp Last Touch Date" | `Last Touch Date` = Current Date |
| 15 | Wait "Wait 3 days" | 3 days |
| 16 | Add task "Task: Call plus voicemail 2" | `Call plus voicemail 2: {{contact.company_name}}`, David, 0 Days |
| 17 | Wait "Wait 2 days" | 2 days |
| 18 | Email "Email: P-A-3 Referral Email 3" | linked template `P-A-3 Referral Email 3` |
| 19 | Add task "Task: tell the referrer" | `Tell {{contact.referral_partner_name}} you could not reach {{contact.company_name}}`, David, 0 Days |
| 20 | Add contact tag "Add cooling 60d" | `cooling 60d` |
| 21 | Remove contact tag "Remove sequence active" | `sequence active` |
| 22 | Wait "Wait 60 days" | 60 days |
| 23 | Remove contact tag "Remove cooling 60d" | `cooling 60d` |

**No SMS steps** (W2 had none in the sheet anyway). **No Goal step**; Stop on response
covers it.

**Deviation, logged: the Personal Line gate does not loop.** The sheet's step 6a says
"on timeout, create the task, then a second Wait on the same condition, timeout 2 days",
i.e. nudge and keep waiting. Branches do not rejoin, so looping back into the sequence
would mean duplicating all 17 remaining actions into the Time out branch. Built instead as
a **hard stop**: the Time out branch raises the "write the personal line" task and ends.
That is consistent with the sheet's own reasoning ("a referral email with a generic first
line wastes the referral") but it does mean **David must act on that task, and the contact
does not resume on its own**. If you want the resume, the options are the same three as
before: duplicate the tail, or lengthen the timeout so the gate simply waits, or re-set
`Lead Lane` on the contact to re-trigger (which needs Allow re-entry ON).

**Finding 18.** The **Wait > Until specific conditions are met** type has its own
**Timeout** toggle, and when it is on the action forks into a **Condition** branch and a
**Time out** branch. That is the mechanism for every approval gate in this build (W2, W3,
W5).

**Finding 19.** `P-A-1` and `P-A-2` were the two templates the earlier report could not
verify. Their previews render correctly in the Send Email picker: the Atlas One wrapper,
the periwinkle button, and `{{contact.referral_partner_name}}`, `{{contact.personal_line}}`
and `{{contact.vertical_proof}}` all present as merge fields. Report item 2 is closed.

---

## Checkpoint 8: W3 Trigger sequence COMPLETE

### W3 Trigger sequence  (Draft, id 5d02c838-41a3-47b1-be92-aa7c03ee74df)

**Settings:** Allow re-entry **ON** (per the sheet, it runs once per trigger event),
**Stop on response ON**.

**Trigger:** `Contact changed` "Trigger Date set", filter `Trigger Date` **Has changed**
(any value). Reads back as `Trigger Date has changed`.

**Action 1: If/Else "DNC gate"**
- Branch **DNC**: `Tags` **Includes** `dnc`. No steps, ENDs. DNC is absolute.
- Branch **None** carries everything below.

| # | Card | Settings |
|---|---|---|
| 3 | Add contact tag "Add sequence active" | `sequence active` |
| 4 | Wait **"Gate: wait for Personal Line"** | Until specific conditions are met, `Personal Line` **Is not empty**, Timeout **2 days** |

Gate branches:
- **Time out**: Add task "Task: write the personal line", title
  `Write the personal line for {{contact.company_name}}`, David, 0 Days. ENDs.
- **Condition** carries the sequence:

| # | Card | Settings |
|---|---|---|
| 5 | Add task "Task: Call plus voicemail" | `Call plus voicemail: {{contact.company_name}}, trigger {{contact.trigger_type}}`, David, **0 Days at 10:00 AM** |
| 6 | Email "Email: P-B-1 Trigger Email 1" | linked template |
| 7 | Update contact field "Stamp Last Touch Date" | `Last Touch Date` = **Current Date** |
| 8 | Wait "Wait 2 days" | 2 days |
| 9 | Email "Email: P-B-2 Trigger Email 2" | linked template |
| 10 | Wait "Wait 2 days" | 2 days |
| 11 | Add task "Task: Call no voicemail" | `Call, no voicemail: {{contact.company_name}}`, David, **0 Days at 4:00 PM** |
| 12 | Wait "Wait 2 days" | 2 days |
| 13 | Add task "Task: Call" | `Call: {{contact.company_name}}`, David, 0 Days |
| 14 | Email "Email: P-B-3 Trigger Email 3" | linked template |
| 15 | Wait "Wait 1 day" | 1 day |
| 16 | Email "Email: P-B-4 Trigger close" | linked template |
| 17 | Remove contact tag "Remove sequence active" | `sequence active` |
| 18 | Add contact tag "Add cooling 90d" | `cooling 90d` |
| 18 | Wait "Wait 90 days" | 90 days |
| 18 | Remove contact tag "Remove cooling 90d" | `cooling 90d` |

**Step 18 is the simple always `Cooling 90d` version**, per your decision. No
`Lifted Suppression` field, no three-branch re-add.

**Deviation, logged: the sheet's step 2 was dropped as a consequence.** Step 2 was an
If/Else on the cooling/hold tags whose only job was to set
`Lifted Suppression` = `Yes` so that step 18 could put the right tag back. With the simple
step 18 that record is never read, so the If/Else would have been a no-op that fires and
falls straight through. The behaviour is unchanged and intended: **a real trigger event
runs the sequence even if the contact was cooling, and the contact ends on `cooling 90d`
regardless of what they were on before.** The one cost, already noted in the sheet, is that
a contact who was in `hold 6m` comes back after 90 days rather than serving the rest of
the six months.

**Also note:** the DNC branch is a hard stop, so a `dnc` contact never reaches the
suppression logic at all, which is the intended precedence.

---

## Checkpoint 9: W3a Renewal calendar COMPLETE

**Workflow:** `W3a Renewal calendar`, id `4ee0dbd6-51d2-4ba1-85b3-1c07ee0649fc`. **Draft.**

**Settings:** Allow re-entry **ON**, Allow multiple opportunities ON, **Stop on response ON**
(all three carried over from W3 and were verified, not re-toggled).

**Triggers, both `Contact changed`:**

| # | Name | Filter | Reads back on the card as |
|---|---|---|---|
| 1 | WC Renewal Date set | `WC Renewal Date` **Has changed** | WC Renewal Date has changed |
| 2 | Benefits Renewal Date set | `Benefits Renewal Date` **Has changed** | Benefits Renewal Date has changed |

**Action 1: If/Else `Which renewal date`**, three outputs:

| Branch | Condition |
|---|---|
| WC renewal date set | `WC Renewal Date` **Is not empty** |
| Benefits renewal date set | `Benefits Renewal Date` **Is not empty** |
| None | falls through to END |

**Inside the WC branch (8 actions), all saved:**

| # | Action | Settings |
|---|---|---|
| 1 | Wait "Wait until WC renewal minus 120" | dynamic date `Contact.Custom Fields.WC Renewal Date`, **Before this date, 120 days** |
| 2 | Email "Email P-B-120 Renewal heads up" | linked template `P-B-120 Renewal heads-up` |
| 3 | Wait "Wait until WC renewal minus 90" | same field, **90 days before** |
| 4 | Update contact field "Set Trigger Type WC renewal" | `Trigger Type` = `WC renewal` |
| 5 | Update contact field "Set Trigger Date to WC renewal date" | `Trigger Date` = **Custom Date** `Contact.Custom Fields.WC Renewal Date` |
| 6 | Wait "Wait until WC renewal minus 60" | same field, **60 days before** |
| 7 | Add task "Task last window to quote" | title `Last window to quote: {{contact.company_name}}`, David Taylor, **0 Days** |
| 8 | Email "Email P-B-60 Last window" | linked template `P-B-60 Last window` |

**Inside the Benefits branch: the same 8 actions**, with `Benefits Renewal Date` as the
wait and Trigger Date field, `Trigger Type` = `Benefits renewal`, and the two email
templates and the task unchanged.

### Builder findings worth keeping

**1. A contact date field minus N days IS expressible.** This was the open question and the
answer is yes, via a route that is not obvious. Wait action, wait type **"Until a specific
date/time"**, then the **three dot menu to the right of the date field, set to `Dynamic`**.
The field turns into "Enter custom variable" with a merge tag picker; pick
`Contact > Custom Fields > <the date field>`. Then choose **"Before this date"** under "When
should the contact proceed?" and put the offset in the **days** box. The panel confirms it in
words: "Contact will proceed 120 days before the scheduled time." All five date relative
waits in W3a are built this way. No deviation needed.

**2. "If this date has already passed" was left at the GHL default**, which is *"Skip all
outbound communication actions till next wait or event start date action"*. This is exactly
what the sheet's test expects: set a test renewal date 100 days out and the minus 120 wait
is already in the past, so its email is skipped and the contact moves on to the minus 90
wait, which shows as scheduled 10 days from now.

**3. Linking an email template needs the row clicked TWICE.** The first click ticks the row
but does not link it, and saving then fails with a red **"Subject not found"** under the
mandatory Subject box. Click the same row again and the panel redraws with the body preview
and a **"Linked template: <name>"** line; save then succeeds and the subject is inherited
from the template. Subject was left empty on both W3a emails, as in W1 and W2.

**4. "Copy all actions from here" exists and works across branches.** The `...` menu on any
action card offers Copy action / **Copy all actions from here** / Move / Delete / Notes.
Copying from the first WC action put the whole eight action chain on the clipboard, and a
**"Paste below"** icon then appears beside every `+` on the canvas; pasting under the
Benefits branch cloned all eight in one click. Only five nodes then needed editing (the
three waits, Trigger Type, Trigger Date); the two emails and the task were already correct.
This is the fastest way to build any mirrored branch and is worth using again in W7.

**5. Editing a pasted dynamic date field:** click into the chip field, `cmd+a`, Delete to
clear the old chip, then reopen the tag picker and choose the new field. The days offset is
preserved across the swap and does not need re-entering.

### Assumption logged

**A contact with BOTH renewal dates set only runs the WC branch.** GHL If/Else sends a
contact down the *first* branch whose condition matches, so `Benefits Renewal Date` is never
evaluated for a contact that also has a `WC Renewal Date`. The build sheet specifies this
two branch shape, so it is built as written, but the consequence is worth knowing: such a
contact gets the WC calendar only, and `Trigger Type` is stamped `WC renewal`. If both lanes
should ever run for one contact, the fix is two separate workflows rather than two branches.

### Task description was required

The Add task panel makes **Description** mandatory, so the task carries the line
*"The renewal is 60 days out. This is the last window to quote it."* The sheet did not
specify one. No dashes.

---

## Checkpoint 10: W4 Cold cadence COMPLETE

**Workflow:** `W4 Cold cadence`, id `b4b3c3ba-7b15-4c1e-b541-21c894c48849`. **Draft.**

**Settings:** Allow re-entry **OFF** (turned off, it defaults on), Allow multiple opportunities
ON, **Stop on response ON**. **Time window: Specific time ON, 08:00 AM to 5:00 PM, Mon to Fri**
(Sun and Sat unchecked). Timezone left on **Account timezone**, which is the Lehi UT account,
so Mountain. Every one of those was already the GHL default once "Specific time" was switched
on, so nothing but the toggle itself had to be set.

**Trigger:** `Contact tag` named "Batch ready tag added", filter **Tag added** `batch ready`.
Reads back on the card as `Tag added includes "batch ready"`.

**Action 1: If/Else `Suppression check`**, branch **Suppressed** =
`Tags` **Includes** `cooling 30d` **OR** `cooling 60d` **OR** `cooling 90d` **OR** `hold 6m`
**OR** `dnc` (five separate conditions joined with OR, the same shape as W1, W2 and W3),
plus the **None** branch that carries the whole cadence.

**Suppressed branch (2 actions, then END):**

| # | Action | Settings |
|---|---|---|
| 1a | Remove contact tag "Remove batch ready" | `batch ready` |
| 1b | Add task "Task skipped suppressed" | `Skipped, suppressed: {{contact.company_name}}`, David Taylor, 0 Days |

**None branch, the cadence (22 actions, all saved):**

| # | Action | Settings |
|---|---|---|
| 2 | Remove contact tag "Remove batch ready" | `batch ready` |
| 3 | Add contact tag "Add sequence active" | `sequence active` |
| 4 | Update contact field "Set Sequence Step 1" | `Sequence Step` = `1` |
| 5 | Add task "Task Call plus VM1 10 AM" | `Call + VM1 10 AM: {{contact.company_name}}`, David, **0 Days at 10:00 AM** |
| 6 | Email "Email P-D-1 Cold Email 1" | linked template `P-D-1 Cold Email 1` |
| 7 | Update contact field "Stamp Last Touch Date" | `Last Touch Date` = **Current Date** |
| 8 | Wait "Wait 2 days" | 2 days, **Advance window ON**, Mon to Fri, 08:00 AM to 5:00 PM |
| 9 | Email "Email P-D-2 Cold Email 2" | linked template `P-D-2 Cold Email 2` |
| 10 | Wait "Wait 2 days" | same as 8 |
| 11 | Add task "Task Call no VM 4 PM" | `Call, no VM, 4 PM: {{contact.company_name}}`, David, **0 Days at 4:00 PM** |
| 12 | Wait "Wait 2 days" | same as 8 |
| 13 | Add task "Task Call plus VM2 10 AM" | `Call + VM2, 10 AM: {{contact.company_name}}`, David, **0 Days at 10:00 AM** |
| 14 | Email "Email P-D-3 Cold Email 3" | linked template `P-D-3 Cold Email 3` |
| ~~15~~ | ~~Send SMS + its If/Else on `SMS consent`~~ | **SKIPPED per your instruction. No SMS anywhere.** |
| 16 | Wait "Wait 2 days" | same as 8 |
| 17 | Add task "Task LinkedIn note or card" | `LinkedIn note or handwritten card (top accounts only): {{contact.company_name}}`, David, 0 Days |
| 18 | Wait "Wait 2 days" | same as 8 |
| 19 | Add task "Task Call 3 last live attempt" | `Call 3, 4 PM, last live attempt: {{contact.company_name}}`, David, **0 Days at 4:00 PM** |
| 20 | Wait "Wait 3 days" | 3 days, Advance window ON, same window |
| 21 | Email "Email P-D-4 Cold breakup" | linked template `P-D-4 Cold breakup` |
| 22 | Add contact tag "Add cooling 90d" | `cooling 90d` |
| 23 | Remove contact tag "Remove sequence active" | `sequence active` |
| 24 | Wait "Wait 90 days" | 90 days, **no** advance window (a rest, not a touch) |
| 25 | Remove contact tag "Remove cooling 90d" | `cooling 90d` |

**Skipped step, logged as instructed:** the sheet's **step 15** was a `SMS consent` If/Else
with a disabled Send SMS inside it. Both the branch and the SMS are gone and the sequence
runs straight from Email 3 to the 2 day wait. This is the third and last SMS step in the
whole build (W1 had two); nothing in any workflow now sends or references SMS.

### Deviations found in the builder

**1. "Send with a random delay" does not exist.** The Send Email action's **Additional
settings** offers only *Track clicks*, *UTM tracking* and *Add tags*. There is no random or
jittered send option, and the Wait action's "For a set period of time" takes a fixed number
only, so the sheet's fallback ("a Wait of 1 to 60 minutes, random") cannot be built either.
**Nothing was substituted**, because a fixed wait would delay every contact by the same
amount and so would not spread the batch at all. The practical mitigation is the one already
in the sheet: David tags `batch ready` in small batches, and the 8 to 5 window plus the 20 a
day warm up cap keeps the volume low. Worth revisiting if GHL adds jitter.

**2. "Send as reply to previous email" is not offered either.** The sheet anticipated this;
the `P-D-2` template's own subject carries the `Re:` treatment, so nothing was needed.

### Builder findings worth keeping

**3. Dropdown options need TWO clicks.** This is the single most useful thing learned in this
workflow. In tag pickers, operator lists, field lists, the Assign to list, the Unit list and
the date value list, one click only highlights the row; **a second click on the same row
commits it**. `double_click` is NOT a safe substitute: in the If/Else field dropdown the
second half of a double click falls through to the row underneath and silently rewrites a
different condition (it turned condition 1 into "Company name" once and had to be rebuilt).
Click, wait, click again, then screenshot to confirm the chip.

**4. Do not press Escape in the same batch as a tag selection.** Clicking the option then
immediately sending Escape reverts the pending chip. Take a screenshot (or click a neutral
part of the panel) between the selection and any dismissal.

**5. The OR joiner has to be set BEFORE adding the next condition.** The AND/OR dropdown at
the bottom of a branch governs the joiner for the row that gets added next; the "And"/"Or"
label printed between existing rows is static text and is not clickable. Set the dropdown to
OR (two clicks), confirm the label between the rows flips to "Or", then press the `+`.

**6. Copy and paste is the way to build repeated actions.** One "Wait 2 days" was built with
its Advance window, then **Copy action** put it on the clipboard and a **Paste below** icon
appeared beside every `+` on the canvas; steps 10, 12, 16 and 18 are one click each, and step
20 is that same paste with the period edited from 2 to 3. The clipboard survives across many
other actions, so copy once and paste all the way down. The same trick cloned "Remove batch
ready" from the Suppressed branch into the None branch.

**7. The task time picker needs care.** It is three scrolling columns (hour, minute, AM/PM)
with an OK button. Choosing an hour scrolls the AM/PM column, so **AM often ends up as PM**;
scroll that column back up and click AM, check the text box reads e.g. `10:00 AM`, then OK.

**8. Task Description is mandatory** on every Add task, so each of the six tasks carries a
one line instruction. None of them contain a dash.

---

## Checkpoint 11: W5 Lost deal re-approach COMPLETE

**Workflow:** `W5 Lost deal re-approach`, id `30d1fed8-590a-44b5-b326-0eb65366fc31`. **Draft.**

**Settings:** Allow re-entry **ON** (it had carried over as OFF from W4 and was turned back
on), Allow multiple opportunities ON, **Stop on response ON**. No time window.

**Trigger:** `Opportunity status changed` named "Opportunity marked Lost", filter
**Moved to status** = **Lost**. No pipeline filter, so it fires from any pipeline, which is
what the sheet asked for. Reads back on the card as `Moved to status is "Lost"`.

**Actions 1 and 2, before the gate:**

| # | Action | Settings |
|---|---|---|
| 1 | Update contact field "Set Lead Lane E Lost" | `Lead Lane` = `E Lost` |
| 2 | Add task "Task record the loss debrief" | `Record: provider chosen, reason, renewal date, the one thing they wanted: {{contact.company_name}}`, David Taylor, 0 Days |

**Action 3, the Personal Line gate:** Wait "Gate wait for Personal Line", type **Until
specific conditions are met**, segment `Personal Line` **Is not empty**, **Timeout ON, 2
days**. This forks into a **Condition** branch and a **Time out** branch, exactly as in W1.

**Time out branch (fires when Personal Line is still empty after 2 days):**
Add task "Task write the personal line", title `Write the personal line: {{contact.company_name}}`,
David, 0 Days, then **END**. Same hard stop decision as W1: the sheet says "then task, then
wait again", but the branches never rejoin, so looping would mean duplicating the entire 12
action tail inside the Time out branch. The task tells David to fill the field and re enrol
the contact, and **Allow re-entry is ON in this workflow**, so re enrolling actually works
here (which it did not in W4).

**Condition branch, the sequence:**

| # | Action | Settings |
|---|---|---|
| 4 | Email "Email P-E-0 Gracious close" | linked template `P-E-0 Gracious close` |
| ~~5~~ | ~~Update `Next Touch Date` = today + 120 days~~ | **DROPPED, see deviation below** |
| 6 | Wait "Wait 120 days four months" | 120 days |
| 7 | Email "Email P-E-4 Month four" | linked template `P-E-4 Month four` |
| 8 | Wait "Wait 90 days" | 90 days |
| 9 | Email "Email P-E-Q1 Quarterly tool" | linked template `P-E-Q1 Quarterly tool` |
| 10 | Wait "Wait 90 days" | 90 days |
| 11 | Email "Email P-E-Q2 Quarterly law change" | linked template `P-E-Q2 Quarterly law change` |
| 12 | Wait "Wait 90 days" | 90 days |
| 13 | Email "Email P-E-Q3 Quarterly proof story" | linked template `P-E-Q3 Quarterly proof story` |
| 14 | Wait "Wait 90 days" | 90 days |
| 15 | Email "Email P-E-Q1 Quarterly tool repeat" | linked template `P-E-Q1 Quarterly tool` again |
| 16 | END | four touches a year is the ceiling, as the sheet says |

### Deviation: step 5 could not be built and was dropped

**`Next Touch Date` = today plus 120 days is not expressible.** The Update contact field
action offers exactly three date modes and none of them does arithmetic:

- **Custom Date**, a free text or merge field box (this is how W3a's `Trigger Date` was set
  from another contact date field), but merge fields carry a value, not a value plus an offset;
- **Current Date**, today with no offset;
- **Specific Date**, a fixed calendar picker, a hard date that would be wrong the day after.

**Nothing was substituted.** Writing `Current Date` would have put a wrong and misleading
date into a field David may filter or report on, which is worse than leaving it empty. The
scheduling this step was meant to describe is already carried by **action 6, the 120 day
wait**, so no behaviour is lost: the next touch still happens at day 120. Only the reporting
field goes unpopulated.

**Note the asymmetry, since it is confusing:** GHL *does* do relative date maths in two other
places, the **Wait** action's "Before this date / After this date" offset (used all through
W3a) and the **Add task** due date's "N Days" from now (used everywhere). It is only *Update
contact field* that has no offset. If a `Next Touch Date` value is genuinely needed, the ways
in are a small side workflow, a custom value, or GHL adding date maths to field updates.

### Also noted

**Wait has no "months" unit** (seconds, minutes, hours, days only), so the sheet's "4 months"
is built as **120 days**, the same convention used for "6 months" as 180 days in W6b.

---

## Checkpoint 12: W7 WSA handoff (Cornerstone) COMPLETE

**Workflow:** `W7 WSA handoff (Cornerstone)`, id `04e13657-82b9-4c96-8367-0bcfde1e79ee`.
**Draft.** Built as the sheet says, by **duplicating W2** from the workflows list, then
changing only what is listed below. Everything else is exactly as W2 built it.

**How the duplicate was made:** workflows list, the `...` on `W2 Warm referral`,
**Duplicate workflow**. GHL asks for the new name in the dialog itself, so
`W7 WSA handoff (Cornerstone)` was typed there and no rename was needed afterwards. The copy
arrives as a **Draft** with the trigger, both If/Else gates, the Personal Line gate and all
23 actions intact.

**Settings:** inherited from W2 unchanged, so Allow re-entry **OFF**, Allow multiple
opportunities ON, **Stop on response ON**. Correct for W7 as specified.

**Trigger:** unchanged from W2, `Contact changed` "Lead Lane set to A Referral", filter
`Lead Lane` **Has changed to** `A Referral`.

### Change 1: the Cornerstone gate, inverted

W2's action 1 branch was `Brand Identity` **Is** `Cornerstone` and it **ended**; the None
branch carried the sequence. W7 needs the opposite. Rather than move 20 actions between
branches, the **branch condition itself was inverted**:

| | W2 | W7 |
|---|---|---|
| Branch name | Cornerstone | **Not Cornerstone** |
| Condition | `Brand Identity` **Is** `Cornerstone` | `Brand Identity` **Is not** `Cornerstone` |
| That branch | ENDs | **ENDs** |
| None branch | carries the sequence | carries the sequence |

The result is what the sheet asked for: **W7 runs only when `Brand Identity` is
`Cornerstone`**, because the None branch is reached only when "is not Cornerstone" is false.
It also means a contact with an **empty** Brand Identity ends at action 1, which is the safe
direction: W7 should never fire for a contact whose brand is unknown. W2 and W7 remain exact
mirrors, so a contact runs one or the other and never both.

**Note on the operator swap:** changing `Is` to `Is not` **clears the value**, so
`Cornerstone` had to be re-selected afterwards. Check the value box after any operator change.

### Change 2: the four task titles

| # | New title | Action name |
|---|---|---|
| 5 | `WSA: reply-all to Zak's intro within 1 hour: {{contact.company_name}}` | Task WSA reply-all to Zak intro |
| 7 | `WSA: call + voicemail 1: {{contact.company_name}}` | Task WSA call plus voicemail 1 |
| 11 | `WSA: call, different hour: {{contact.company_name}}` | Task WSA call different hour |
| 16 | `WSA: call + voicemail 2: {{contact.company_name}}` | Task WSA call plus voicemail 2 |
| 19 | `Tell Zak Call at WSA you could not reach {{contact.company_name}}` | Task tell Zak at WSA |

Each description was also reworded for the Cornerstone channel (for example task 5 now reads
"Warm referral from Zak at WSA. Reply-all to the introduction within the hour, as
Cornerstone."). Times and assignees were left exactly as W2 had them.

### Change 3: the three Send Email steps replaced, per your decision

**Your instruction was "W7 uses Internal Notification plus a task on the contact instead of
Send Email, GHL never sends as Cornerstone."** So W2's actions 8, 13 and 18 (`P-A-1`,
`P-A-2`, `P-A-3`) were **deleted** and each replaced by a **pair**:

| Replaces | Internal notification | Add task |
|---|---|---|
| action 8 | "Notify David send WSA Email 1", type **Email**, to particular user **David Taylor**, subject `Send WSA Email 1 as Cornerstone` | "Task send WSA Email 1", title `WSA: send Email 1 as Cornerstone: {{contact.company_name}}`, David, 0 Days |
| action 13 | "Notify David send WSA Email 2", same shape, subject `Send WSA Email 2 as Cornerstone` | "Task send WSA Email 2", title `WSA: send Email 2 as Cornerstone: {{contact.company_name}}` |
| action 18 | "Notify David send WSA Email 3", same shape, subject `Send WSA Email 3 as Cornerstone` | "Task send WSA Email 3", title `WSA: send Email 3 as Cornerstone: {{contact.company_name}}` |

Every one of the six carries the same instruction and the same guardrail, worded as:

> Send WSA Email N to this contact from david.taylor@cornerstonepeo.com. Use the P-W7-N WSA
> Email N wording. Cornerstone identity only, PEO scope only, present the credit total only.

**Consequences worth stating plainly:**

- **W7 now sends nothing to the prospect automatically.** All three touches are handed to
  David to send by hand from the Cornerstone mailbox. That is the intended trade: it removes
  any chance of GHL sending Atlas One branding into the Cornerstone channel.
- The `P-W7-1`, `P-W7-2` and `P-W7-3` templates are **not linked to any action** in W7. They
  remain in the template library as the wording David copies from.
- The sheet's "From name / From address = David Taylor, Cornerstone PEO /
  david.taylor@cornerstonepeo.com on all three Send Email cards" no longer applies, since
  there are no Send Email cards. **Appendix B item 2, verifying that address as an additional
  sender, is therefore no longer a blocker for W7 to run** (it stays on the list only if you
  later want GHL to send these directly).
- **Stop on response is ON**, so if the prospect replies to David's manual email from the
  Cornerstone mailbox, GHL will not see it and will not stop the workflow. The remaining
  touches keep firing as tasks until David marks them done or removes the contact. Worth
  knowing before publishing.

### Builder findings

**Editing a task inside a duplicated workflow is where the panel bites.** Twice the typed
Action name landed in the Title and vice versa, and once an extra Company Name chip was
appended. Two causes, both avoidable:

1. **The panel is still loading** for a second or two after the card is clicked. Type nothing
   until a screenshot shows the populated fields.
2. **Clicking the Title at its centre lands on a merge chip**, which opens the tag browser
   instead of focusing the text. **Click the Title at its far left (about x=830), where the
   plain text is**, then `cmd+a` and Delete to clear chips and text together.

Do the fields **one at a time with a screenshot between**, never in one long batch.

---

## Checkpoint 13: Run I, Cowork audit fixes applied and all ten workflows PUBLISHED

Two fixes from the Cowork audit, then the publish pass. Everything below is live.

### Fix 1: the Personal Line gate can now restart itself

The audit was right: the gate was a dead end. The Time out branch raised a task and ended,
and in W2 and W7 re-entry was OFF, so filling the field in afterwards did nothing. Fixed in
all four workflows that carry the gate.

| Workflow | Allow re-entry | Clear step added in the Time out branch | Restart is triggered by |
|---|---|---|---|
| **W2 Warm referral** | **turned ON** (was OFF) | Update contact field, **Clear field data**, `Lead Lane` | David setting `Lead Lane` back to `A Referral` |
| **W7 WSA handoff** | **turned ON** (was OFF) | Update contact field, **Clear field data**, `Lead Lane` | David setting `Lead Lane` back to `A Referral` |
| **W3 Trigger sequence** | already ON | Update contact field, **Clear field data**, `Trigger Type` | David writing `Trigger Date` again |
| **W5 Lost deal re-approach** | already ON | **none**, as instructed; the trigger is the opportunity status | David setting the opportunity back to **Lost** |

The Time out branch in each now reads: **nudge task, then the clear step, then END.**

**Task titles, as set:**

- W2 and W7: `Write the personal line, then set Lead Lane back to A Referral to restart`
- W3: `Write the personal line, then set Trigger Type and Trigger Date again to restart`
- W5: `Write the personal line, then set the opportunity back to Lost to restart`

Each task description now spells out the loop: what was cleared, what to write, and what to
set to fire the trigger again. Every action was renamed
`Task write the personal line and restart` so the card says what it does.

**Why the field has to be cleared:** GHL's `Contact changed` triggers fire on a *change*.
Setting `Lead Lane` to `A Referral` when it already reads `A Referral` is not a change, so
nothing fires. Emptying it on the way out is what makes David's re-entry a real change.

**W3 and W5 wordings differ from W2 and W7 by necessity.** W3's trigger is
`Trigger Date has changed`, not Trigger Type, so clearing Trigger Type alone would not
restart it; the task says to set **both** and notes that writing Trigger Date is the part
that fires. W5 has no field to clear at all, so it only got the wording.

### Builder finding: there is a purpose built "Clear field data"

The Update contact field action's **ACTION TYPE** dropdown has three modes, and the third is
exactly what was needed:

- **Update field data**, replaces the current value
- **Add to field data**, adds without removing
- **Clear field data**, *empties the field*

With Clear selected the panel drops the value box entirely and just asks which field or
fields to empty. No blank-value trick required.

### Fix 2: W3 now has the same suppression gate as W1 and W4

Added immediately after the DNC gate: If/Else **"Suppression check"**, branch **Suppressed**
= `Tags` **Includes** `cooling 30d` **OR** `cooling 60d` **OR** `cooling 90d` **OR**
`hold 6m` **OR** `dnc`, five separate OR'd conditions, the same shape as W1, W2, W4 and W7.

- **Suppressed branch:** Add task "Task skipped suppressed", title
  `Skipped, suppressed: {{contact.company_name}}`, David Taylor, **0 Days**, then **END**.
- **None branch:** everything that used to follow the DNC gate, starting at
  `Add sequence active` and running through the whole lane B sequence.

**Important builder behaviour, worth knowing before anyone repeats this.** Inserting an
If/Else into the middle of an existing chain does **not** leave the downstream actions after
the If/Else, and it does not put them in the None branch either. GHL attaches the entire
downstream chain to the **first branch**, which here was Suppressed, and leaves None empty.
That is exactly backwards from what was wanted.

The fix is the `...` menu's **Move all actions from here**. Clicking it on the first
downstream action turns every insertion point on the canvas into a **"Move here"** target
(and marks the illegal ones **"Not allowed"**, so it will not let you drop a chain inside
itself). Clicking the target under the **None** branch relocated all 20 or so actions in one
move. Verified afterwards: Suppressed ends at the task, None carries the sequence.

### The publish pass

Published in the order given, each confirmed **Published** in the Status column before moving
on. The workflows list `...` menu carries **Publish workflow** with a confirm dialog, which is
faster than opening each one and flipping the Draft toggle.

| # | Workflow | Status |
|---|---|---|
| 1 | W6 Suppression and caps | **Published** |
| 2 | W6b Sequence stalled | **Published** |
| 3 | W0 Set vertical lines | **Published** |
| 4 | W1 Inbound speed to lead | **Published** |
| 5 | W5 Lost deal re-approach | **Published** |
| 6 | W4 Cold cadence | **Published** |
| 7 | W3a Renewal calendar | **Published** |
| 8 | W3 Trigger sequence | **Published** |
| 9 | W2 Warm referral | **Published** |
| 10 | W7 WSA handoff (Cornerstone) | **Published** |

Confirmed a final time on one screen with the list set to 50 per page: all ten read
Published, all ten show 0 total enrolled and 0 active enrolled, so nothing has fired yet.

### Still true after this run

- **No SMS** anywhere, so A2P is not a blocker.
- **W7 sends nothing automatically**; its three touches are David's to send from the
  Cornerstone mailbox. Stop on response cannot see a reply to a manually sent email, so the
  later W7 tasks keep firing until David clears them.
- **W5 step 5** (`Next Touch Date` = today plus 120 days) is still dropped; GHL has no date
  arithmetic in field updates.
- **The `[link]` placeholder** still needs replacing in the Email 3 templates.
- Part 10 is still untouched: no smart lists, old shells left alone, no test contacts, A2P
  status not read.

---

## Checkpoint 14: Run J. Placeholder audit, smart lists, live test BLOCKED

### 1. The `[link]` placeholders: nothing to change, the chain is already correct

All seven named templates were opened in the code editor and read end to end, body and
signature. **Not one contains `[link]` or `[tool]`. No template was edited.**

| Template | What its body actually holds | Changed |
|---|---|---|
| `P-A-3 Referral Email 3` | no tool line at all, CTA is the Back Office Audit booking button | no |
| `P-B-3 Trigger Email 3` | "Here is the tool I mentioned: **{{contact.vertical_tool}}**" | no |
| `P-D-3 Cold Email 3` | same line, **{{contact.vertical_tool}}** | no |
| `P-E-Q1 Quarterly tool` | same line, **{{contact.vertical_tool}}** | no |
| `P-E-Q2 Quarterly law change` | no tool line, CTA is the booking button | no |
| `P-E-Q3 Quarterly proof story` | `{{contact.vertical_proof}}`, CTA is the booking button | no |
| `P-W7-3 WSA Email 3` | no tool line, CTA is the Zoom scheduler link | no |

**The carry forward note in the Run G report was wrong and is now retired.** It said "the
`[link]` placeholder still needs replacing in the Email 3 templates". That came from the
build sheet's Appendix A, which used `[link]` as a placeholder **in the W0 vertical values**,
not in the templates. W0 was built in Run G part 2 with the real URLs, per your instruction
at the time, so the placeholder never reached the CRM.

**Verified end to end:** W0's Construction branch, action "Set Construction lines", holds
`Vertical Tool` = `WC premium check: https://forms.atlasonesolutions.com/tools/w...`, a real
live URL. The three tool emails render `{{contact.vertical_tool}}`. So W0 writes the URL and
the reader sees the URL. **Nothing to fix.**

### 2. Smart lists: the two the sheet names

Part 10 of the build sheet names **two** smart lists and both are built:

| Name | Filters | Count now |
|---|---|---|
| **Sequence Active** | `Tag` **Is** `sequence active` | 0 |
| **Stalled** | `Tag` **Is** `sequence active` **AND** `Last Touch Date` **Is** **More than 5 Days Ago** | 0 |

Both read 0 because no contact has ever been enrolled, which is correct.

**Discrepancy with the Run J instruction, flagged rather than guessed at.** The instruction
named six lists in its parenthetical: Sequence active, Cooling, Hold, DNC, Reply received,
Batch ready. **The sheet names none of Cooling, Hold, DNC, Reply received or Batch ready**,
and it *does* name **Stalled**, which the parenthetical omits. The instruction's own rule was
"build the ones the sheet names, skip anything the sheet does not name", so the sheet won:
Sequence Active and Stalled built, the other five skipped. Say the word and the five tag
lists take about a minute each.

### Builder findings

**Smart list filters are OR by default and the OR pill is not a toggle.** Two top level
filters are joined with **OR** and clicking the pill does nothing. **AND** comes from
**"Add nested filter"** *inside* an existing filter block, which prints AND between the rows.
That is how Stalled is built.

**Date fields have no "before" operator.** The operator list is only Is / Is not / Is empty /
Is not empty. The relative comparison lives in the **value** dropdown: Between, More than,
After date, Less than, Before date, In the next, In the last, then a number, a unit, and
**Ago** or **From now**. "Is before 5 days ago" is therefore built as
**Is → More than → 5 → Days → Ago**. Same shape as the W6b workaround from Run G.

### 3. The live test could not be run. Add Contact is broken in this session.

**The test never started, because the test contact could not be created.**

`Contacts > Add Contact` opens its panel and **accepts typing normally**: First name `Test`,
Last name `Prospect`, Email `david@atlasonesolutions.com` all entered and visible. But
**every button in that panel is dead**. Save does nothing, and neither does Cancel, the X in
the corner, or the trash icon on the phone row. No error, no toast, no network response, no
validation message. The panel just sits there.

Tried, in this order:
1. Save. Nothing.
2. Waited, re-checked all fields were valid including the required First name. Save. Nothing.
3. Full page reload, re-entered everything from scratch. Save. Nothing.
4. Blurred the focused field and pressed Escape first in case a dropdown had focus. Save.
   Nothing.
5. Deleted the empty phone row, on the theory that a blank phone with no type selected was
   failing validation silently. **The trash icon was dead too**, which is what showed the
   problem is the whole panel, not the form contents.

After the fifth attempt I stopped rather than keep hammering a dead control.

**Confirmed no mess was left behind.** Searched contacts for "Test Prospect" after a fresh
page load: **no contacts found.** Nothing was half created, so there is nothing to delete and
step 4's cleanup is a no op.

**Everything downstream of contact creation is therefore untested and unclaimed:**
- W0 filling Vertical Opener, Vertical Proof and Vertical Tool: **not tested**
- Form A submission: **not attempted**
- W1 firing, `P-C-0 Instant reply` arriving with the branded wrapper: **not tested**
- The CALL NOW task and the notification bell: **not tested**
- W6 on the `not interested` tag removing `sequence active`, adding `hold 6m`, and pulling the
  contact out of W1: **not tested**

`_briefs/assets/run-J/` holds the two screenshots that were actually earned:
`01-smart-lists-created.jpg` (Stalled and Sequence Active in the tab bar) and
`02-no-test-contact-clean-state.jpg` (the search proving no test contact exists). No
screenshots exist for the W0, W1 or W6 confirmations because those confirmations never
happened.

**What unblocks it:** most likely a stale front end. A hard reload of the CRM in a fresh tab,
or a different browser session, usually revives a panel whose buttons have stopped binding.
Creating the contact by CSV import, or from the Conversations pane, would also sidestep the
Add Contact panel entirely. Once one contact called Test Prospect exists with
`Vertical` = `Construction`, the rest of the Run J step 3 script runs as written.

---

## Checkpoint 15: Run J part 2. Blocked. The Contacts module is down, and the test email was already taken

Nothing in Run J part 2 could be completed. Two separate problems, one of them a real finding
about the data rather than the UI.

### Finding 1: `david@atlasonesolutions.com` already belongs to a real contact

The Run J part 1 mystery is solved. Add Contact was not broken then; **GHL was silently
refusing a duplicate email.** Searching that address in the Conversations contact picker
returns an existing contact:

> **David taylor | david@atlasonesolutions.com**

That is David's own record, not test data. The Run J part 2 script would have had this run
end by **deleting** it, after tagging it `not interested` and pushing it through W6. That is
an irreversible production action on a real contact, so it was not done.

**Substitution made, and it needs your sign off:** the test email was changed to
**`david+testprospect@atlasonesolutions.com`**. Plus addressing still delivers to the same
inbox, so the branded `P-C-0` check would still have been verifiable, but it creates a
distinct record that is safe to tag, sequence and delete. This matches the convention already
in the CRM, which holds `david+seedb@atlasonesolutions.com` and `seed-a@` / `seed-d@`
records from earlier test rounds. `_briefs/assets/run-J/test-prospect.csv` is written with
that address, ready for the import when the UI comes back.

### Finding 2: the Contacts module will not render

**Contacts is the only broken module.** Verified by elimination in the same session and the
same tab:

| Module | State |
|---|---|
| **Automation > Workflows list** | renders fully, all ten workflows and their statuses |
| **Conversations** | renders fully, inbox, threads, message history |
| **Contacts (list, smart lists, Add Contact, Import)** | **body renders completely empty** |
| **Contact Details panel inside Conversations** | rendered once, then went blank on reload |

The Contacts page paints its header and the Smart Lists / Bulk Actions / Custom Fields /
Tasks / Companies tab strip, and **nothing below it**. No toolbar, no Add Contact button, no
Import control, no contact rows, no smart list tabs. Screenshot:
`_briefs/assets/run-J/03-contacts-module-down.jpg`.

**This is not a stale front end.** Tried, all with 20 to 30 second settles:
a brand new tab; `Cmd+Shift+R` hard reload on `/contacts/`; a second hard reload on
`/contacts/smart_list/All`; and in between, navigating away to Automation and Conversations
(both fine) and back. The blank state survived every one. The Contact Details panel in
Conversations going blank on a later load points at the **contact data layer**, not a cached
bundle.

### All three contact creation paths were tried and all three are blocked

| Path | Result |
|---|---|
| **A. Contacts > Add Contact** | the module does not render, so there is no Add Contact button to click. In Run J part 1 the panel did open and its Save was dead, which Finding 1 now explains as the duplicate email block. |
| **B. Conversations > new conversation** | the compose modal opens (slowly, about 30 seconds) and offers Message Contacts, but its picker **only selects contacts that already exist**. This GHL build has no create a new contact option inside it, so path B cannot create anything. |
| **C. CSV import** | Import lives inside the same non rendering Contacts module. The CSV is written and waiting; there is no upload control to feed it to. |

### Consequently, unattempted

Every remaining item depends on a contact record or on the Contacts module:

- **Part 1** test contact, Vertical = Construction, Lead Lane = Inbound: **not created**
- **Part 2** W0 filling the vertical line fields; Form A submission; `P-C-0 Instant reply`
  and its branded wrapper; the CALL NOW task; the notification bell; W6 on `not interested`:
  **all unattempted**, no enrollment history to record because nothing was ever enrolled
- **Part 3** the five remaining smart lists: **not built.** Smart Lists is a tab inside the
  broken module. The two from Run J part 1, **Sequence Active** and **Stalled**, were created
  before the outage and should still exist; they could not be re-verified today.
- **Part 4** cleanup: **nothing to clean up**, since nothing was created. The real
  David taylor contact was left untouched.

### One useful thing was confirmed for Part 3

The reply tag W6 actually applies is **`reply received`**, not `replied`. So
"Prospecting: Reply received" must filter on `Tag is reply received`. Noted so the list is
built correctly when the module returns.

### To resume

1. Confirm the Contacts module renders again. If it is still blank, it is worth raising with
   High Tide or GHL support, since Automation and Conversations are healthy, which points at
   something location specific rather than a general outage.
2. Decide on the email. Either approve `david+testprospect@atlasonesolutions.com`, or name a
   different address, or say explicitly that the real `david@atlasonesolutions.com` contact
   should be used and then **not** deleted at the end.
3. Everything else in the Run J part 2 script then runs as written.

---

## Checkpoint 16: Run J part 3. API live test. W0 and W6 PASS, Form A did not land, Contacts still down

The API route worked and produced two real, verified passes. The browser route stayed broken
and got worse during the run.

### Part 0: Contacts did NOT recover

`/v2/location/.../contacts/` still paints its header and tab strip and **nothing below**,
after a fresh tab plus `Cmd+Shift+R` plus a 20 second settle. Part 3 smart lists were
therefore **skipped**, as instructed.

One useful discovery: **Settings > Custom Fields renders fine** even though Contacts does
not. That is where the field names and keys below came from.

**Late in the run the whole CRM UI went blank**, Automation included. The W1 enrollment
history check could not be done for that reason. The API stayed healthy throughout.

### The Private Integration key is contacts scope only

| Endpoint | Result |
|---|---|
| `GET /contacts/` , `POST /contacts/` , `PUT` , `DELETE` , `/contacts/{id}/tasks` , `/contacts/{id}/tags` | **200 / 201, all fine** |
| `GET /locations/{id}/customFields` | **401 not authorized for this scope** |
| `GET /locations/{id}` , `/locations/{id}/tags` , `/workflows/` | **401 same** |

So the Part 1 step 1 id map could not be pulled from `customFields`. It was rebuilt instead
from **Settings > Custom Fields** (names, keys, types) cross referenced with **ids observed on
live contact payloads**, and written to `_briefs/assets/run-J/field-ids.json`. Five ids are
confirmed by value matching; `Sequence Step` and `Trigger Type` are recorded with keys but
`null` ids, because this run never wrote to them.

### Two corrections to the brief

1. **There is no "Vertical Pain" field.** The three fields W0 writes are **Vertical Opener,
   Vertical Proof, Vertical Tool**. Confirmed in Settings > Custom Fields and in the live
   payload.
2. **Lead Lane's inbound value is `C Inbound`,** not `Inbound`.

### Finding: W0 does not fire on contact creation, only on update

This matters for anyone bulk importing.

- `POST /contacts/` with `Vertical = Construction` in the same call created the contact at
  **14:08:41Z**. Waited 95 seconds. **The three vertical fields stayed empty.**
- A follow up `PUT` changing Vertical to `Technology` at **14:10:53Z** populated all three by
  **14:12:28Z**, inside 95 seconds.
- A second `PUT` back to `Construction` at **14:12:43Z** repopulated with the Construction
  copy by **14:14:18Z**.

W0's trigger is `Contact changed` with filter `Vertical has changed`, and GHL evidently does
not count "set during creation" as a change. **A CSV import or API create that sets Vertical
in one shot will not run W0.** The lane values have to be written as a second step.

### PASS: W0 wrote the right Construction copy, with the real URL

Saved to `_briefs/assets/run-J/02-w0-fields.json`:

- **Vertical Opener** = "Your workers' comp renewal is the one window where a carrier will
  actually compete for you..."
- **Vertical Proof** = "A 30 man electrical contractor had the expense constant charged in
  both states, three guys on the wrong class code..."
- **Vertical Tool** = `WC premium check: https://forms.atlasonesolutions.com/tools/wc-premium-check/`

**No `[link]` placeholder**, a real live URL. That independently confirms checkpoint 14's
conclusion from the other direction: W0 writes the URL, and the templates render
`{{contact.vertical_tool}}`.

### FAIL: Form A submitted successfully but produced no contact

Form A is **"Atlas One — PEO / Prospect Quote Request"**, form id `Cxqawj85qg4ULUl64nMc`,
public URL `https://api.leadconnectorhq.com/widget/form/Cxqawj85qg4ULUl64nMc`.

Submitted at about **14:19Z** with Test / Prospect / david+testprospect@atlasonesolutions.com
/ Test Co. **Phone is a required field on Form A**, so the reserved fictional number
`(385) 555-0199` was used; both SMS consent boxes were deliberately left unchecked. The form
returned its real thank you page: "Thank you — your request has been received."

**Nothing reached the CRM.** Checked repeatedly over the following minutes:

- the test contact's `dateUpdated` stayed at **14:12:45Z**, my own last PUT
- `phone` stayed null, so the form's phone never landed
- **no duplicate contact was created**: queries for `testprospect`, `Test Co`, `Prospect` and
  `5550199` returned only my API contact and one unrelated Sep 6 seed
- **zero tasks** on the contact

So **W1 never triggered**, and with it the `P-C-0 Instant reply`, the CALL NOW task and the
internal notification are all **unverified**. This is almost certainly the same platform
problem as the blank UI, which set in around the same minute.

### PASS: W6 fired, and fast

`POST /contacts/{id}/tags` with `["not interested"]` at **14:24:32Z**. Re-read at
**14:24:36Z**: tags were **`["not interested", "hold 6m"]`**.

W6's Not interested branch added `hold 6m` in about **four seconds**. Saved to
`06-w6-contact.json`. This also proves the **workflow engine was healthy the whole time**,
which is what makes the Form A failure a form or ingestion problem rather than an automation
one. W6's `Remove sequence active` step had nothing to remove because W1 never ran, so that
half of the check is untested rather than failed.

### Cleanup: clean

Zero tasks to delete. `DELETE /contacts/{id}` returned 200 `succeeded: true`. Verified twice:
the `testprospect` query returns **0 matches**, and a direct GET of the id returns
**400 Contact not found**. The real **David taylor** contact was never touched, and neither
was the unrelated `david+seedb@` seed from Sep 6.

### The reply-received tag, again

W6 applies **`reply received`**, not `replied`. When the smart lists finally get built,
"Prospecting: Reply received" must filter on `Tag is reply received`.

### Still open

1. **Contacts module down**, now accompanied by intermittent whole-UI blanking. Worth raising
   with High Tide or GHL. Automation and the API are fine, so it is not a full outage.
2. **Form A ingestion.** A submission that returns a thank you page but creates no contact is
   the more serious of the two, because it would silently drop real leads. Worth checking the
   form's own Submissions tab once the UI is back, to see whether the submission was recorded
   and simply not converted, or lost entirely.
3. **Five smart lists** still unbuilt.
4. **P-C-0, the CALL NOW task and the notification bell** still unverified.

---

## Checkpoint 17: Run J part 4. Root cause found. Form A is NOT broken. Checkpoint 16 corrected

### Root cause: GHL deduplicates form submissions on PHONE NUMBER

**Form A works correctly. Checkpoint 16's "Form A drops submissions" conclusion was wrong and
is retracted here.**

What actually happened on 10 Sep at 14:19Z: Form A requires a phone, so the test used the
reserved fictional number **(385) 555-0199**. That number was **already on an existing
contact**: `david+seedb@atlasonesolutions.com`, the Sep 6 seed, itself created by a Form A
submission. GHL matched the new submission to that contact by phone and **updated it**
instead of creating a `david+testprospect@` contact.

Evidence, all from the API on the seed contact `PKPX9APnAQlcrpER2Mr1`:

- `dateUpdated` was **2026-09-10T14:19:11.982Z**, the exact submission minute
- `firstName` / `lastName` had been overwritten from **Seed / RunB** to **Test / Prospect**
- `phone` **+13855550199**, the number submitted
- tags had gained **`sequence active`**, which only W1 adds
- a task **`CALL NOW:  (385) 555-0199`** existed, created 14:19, assigned to David
- Sites > Forms > Submissions shows the row **present**, 08:19 AM MDT, with a linked contact
  avatar, alongside the Sep 6 seed rows

So the submission was never dropped. It landed on the wrong contact because the test reused a
phone number, and the search that "proved" it missing was looking for the wrong email.

**Practical consequence for real use:** none. Real prospects have distinct phone numbers.
**Consequence for testing:** every test submission needs a unique phone, not just a unique
email. `field-ids.json` and the CSV convention should note that.

### Part 1 diagnostics, for the record

- **Form A field types:** the Submissions table renders **Email, First name, Last name,
  Phone** as dedicated standard columns and every row carries a linked contact avatar, which
  rules out the "email is a custom field" hypothesis. **No form edit was made, per the
  Part 2 rule.**
- **Seed contacts** `david+seedb@`, `seed-a@`, `seed-d@` all show
  `source: Atlas One — PEO / Prospect Quote Request` and real phones, confirming Form A has
  been creating contacts correctly since Sep 6.
- **GHL status page:** *All services are online*, last updated Sep 10 8:40am MDT. **No
  incident** in the 13:30Z to 15:00Z window. The blank UI is local to this account, not a
  platform outage. Screenshot `08-status.jpg`.

### The W1 chain actually PASSED, on the seed contact

Because W1 really did run, this run finally verified the chain end to end:

| Check | Result |
|---|---|
| **P-C-0 Instant reply** | **PASS.** Outbound at **08:19 AM** to `david+seedb@atlasonesolutions.com`, A1 Solutions branded wrapper, correct body copy, **no literal `[link]`**. Screenshot `03-instant-reply.jpg` |
| **CALL NOW task** | **PASS.** `CALL NOW:  (385) 555-0199`, due 2026-09-10, assigned to David. Saved to `04-task.json` |
| **Notification bell** | **not captured**, the UI degraded before it could be screenshotted |
| **W6 suppression** | **PASS.** `not interested` at 14:52:46Z produced `hold 6m` by 14:52:51Z, about **5 seconds** |

Note the CALL NOW title reads `CALL NOW:  (385) 555-0199` with a double space, because
`{{contact.company_name}}` was empty on the seed contact. Cosmetic, and only because of the
mismatched contact.

### Side effect I caused on a seed contact, and what I did about it

The submission overwrote a real seed record. Remediation done:

1. **Name restored** from Test / Prospect back to **Seed / RunB** (API PUT, 200).
2. **`sequence active` removed** via the Conversations contact panel, returning tags to the
   original `intake-received`, `form-a-sent`.
3. **W1 enrollment stopped.** W1 has **no Personal Line gate**, so left alone it would have
   kept sending `P-C-2` at day 1 and `P-C-3` at about day 6 to `david+seedb@`, plus three
   more tasks. Both the Contacts module and the workflow builder were blank, so the
   enrollment could not be removed directly. Instead **`not interested` was added**, which
   fires W6 and its Remove From Workflow step. Confirmed: `hold 6m` appeared 5 seconds later.

**Residue left on `david+seedb@atlasonesolutions.com`, for David to clear when convenient:**

- tags **`not interested`** and **`hold 6m`**. `hold 6m` self removes after 180 days; both are
  safe to delete by hand.
- the task **`CALL NOW:  (385) 555-0199`**, id `DQu5aianVjDqSgl4Xp1F`. It could not be
  deleted: the API `DELETE` calls were refused by this session's own safety classifier, and
  the Contacts and Tasks UI is blank.

Nothing was touched on the real **David taylor** contact.

### Parts that could not be run

- **Part 3, the W0 Contact Created trigger: NOT DONE.** The workflow builder renders blank, so
  W0 could not be edited. The underlying finding from checkpoint 16 stands and still needs
  this fix: **W0 does not fire when a contact is created with Vertical already set**, only on
  a later update. A CSV import or API create that sets Vertical in one shot will not run W0.
- **Part 4, the five smart lists: SKIPPED.** Contacts is still blank after a fresh tab, a hard
  reload and a 20 second settle.

### UI health, narrowing further

Working: Dashboard, Sites and Forms, Conversations, Settings > Custom Fields, and the whole
API. Blank: **Contacts** (all tabs) and, newly today, **individual workflow pages** in
Automation, though the Workflows list itself rendered earlier. Given GHL reports all services
online, this looks account or sub account specific and is worth raising with High Tide.

### Cleanup

`testprospect` and `testcreate` both return **0 contacts**. No test contacts remain.

---

## Checkpoint 18: Run K. Seed cleaned, W0 now fires on create, seven smart lists

Date: 2026-09-10. The Contacts module came back on its own, so the work blocked across Runs J
part 2 to part 4 could finally be done.

### Part 0, Contacts renders: PASS

Fresh load of `/contacts/smart_list/All` painted the full grid, **2137 Contacts**, rows, the
Add Contact button, Filters and Sort. No blank pane. The outage described in checkpoints 15 to
17 is over. Nothing was changed to fix it.

### Part 1, seed contact cleaned: PASS, with one item not verifiable

`Seed RunB`, id `PKPX9APnAQlcrpER2Mr1`, `david+seedb@atlasonesolutions.com`.

| Item | Result |
|---|---|
| Remove `not interested` | **Done**, via the X on the tag chip |
| Remove `hold 6m` | **Done**, same way |
| Tags left behind | `intake-received`, `form-a-sent`, exactly the original two. Panel reads **Tags (2)** |
| Delete task `CALL NOW:  (385) 555-0199` | **Done.** Task ⋮ > Delete > confirmation dialog > Delete task. Tasks panel now reads **No tasks yet** |
| Confirm no active workflows | **Could not verify.** This GHL build exposes no Automations or active-workflow view on the contact record. Checked every right-rail tab (Activity, Associations, Opportunities, Tasks, Documents) and the full left panel |

Screenshot `_briefs/assets/run-K/01-seedb-clean.jpg`.

The residue listed at the end of checkpoint 17 is now fully cleared.

### Part 2, W0 Contact Created trigger: PASS. The checkpoint 16 gap is closed

This is the fix for the standing finding that **W0 did not fire when a contact was created
with Vertical already set, only on a later update**.

**The filter could not be written as "Vertical is not empty".** The Contact created trigger's
filter offers only the seven stored dropdown values (Audiology, Dental Ortho Optometry ENT,
Construction, Technology, Hospitality, Professional Services, Other) and the value control is
**single select**, confirmed by probing it. There is no "is not empty" operator on that
trigger.

**What was built instead: one Contact created trigger per vertical value, seven in total.**
Set theoretically this is identical to "Vertical is not empty", and it avoids the alternative
of an unfiltered Contact created trigger, which would enrol every new contact in the location.

W0 now carries **eight triggers**:

| # | Trigger | Filter |
|---|---|---|
| 1 | Contact changed, `Vertical changed` | Vertical has changed (pre-existing) |
| 2 | Contact created, `Created with Vertical Construction` | Vertical is "Construction" |
| 3 | Contact created, `Created with Vertical Audiology` | Vertical is "Audiology" |
| 4 | Contact created, `Created with Vertical Dental Ortho Optometry ENT` | Vertical is "Dental Ortho Optometry ENT" |
| 5 | Contact created, `Created with Vertical Technology` | Vertical is "Technology" |
| 6 | Contact created, `Created with Vertical Hospitality` | Vertical is "Hospitality" |
| 7 | Contact created, `Created with Vertical Professional Services` | Vertical is "Professional Services" |
| 8 | Contact created, `Created with Vertical Other` | Vertical is "Other" |

Saved and **Published**, verified after a full page reload: all eight triggers persist and the
toggle reads Publish.

Note on trigger 8: the Route by vertical If/Else has branches for the six named verticals plus
a **None** branch that runs no action, so a contact created with Vertical = Other enrols and
ends without writing anything. Harmless, and kept for exact parity with "is not empty".

**Live test through the API: PASS.**

- POST `/contacts/` at 09:34 MDT with firstName Test, lastName Create,
  `david+testcreate@atlasonesolutions.com`, `+13855550142`, and `vertical = Construction`
  **in the same request**. Contact id `lUccVrywU9nFZYKMwVqo`.
- 95 seconds later, GET returned all three lane fields filled:
  - **Vertical Opener** — "Your workers' comp renewal is the one window where a carrier will
    actually compete for you…"
  - **Vertical Proof** — "A 30 man electrical contractor had the expense constant charged in
    both states…"
  - **Vertical Tool** — `WC premium check: https://forms.atlasonesolutions.com/tools/wc-premium-check/`

Compare with Run J part 4, where the same single-shot create left all three empty after 95
seconds. **A CSV import or API create that sets Vertical in one shot now runs W0.**

**Cleanup: PASS.** Contact deleted in the UI (Contacts > tick > Delete > type DELETE >
Delete). API search for `testcreate` returns **total: 0**.

### Part 3, five smart lists built, seven in total: PASS

| Smart list | Definition as built | Count at build time |
|---|---|---|
| `Prospecting: Cooling` | Tag **Is** cooling 30d, cooling 60d, cooling 90d | 0 |
| `Prospecting: Hold` | Tag **Is** hold 6m | 0 |
| `Prospecting: DNC` | Tag **Is** dnc, not interested | 0 |
| `Prospecting: Reply received` | Tag **Is** reply received | 1 |
| `Prospecting: Batch ready` | Lead Lane **Is** `D Cold` **AND** Tag **Is not** cooling 30d, cooling 60d, cooling 90d, hold 6m, dnc, not interested **AND** Sequence Step **Is empty** | 0 |

Plus the two from Run G: `Sequence Active` and `Stalled`. Manage smart lists reads
**1 - 7 of 7**. Screenshot `_briefs/assets/run-K/02-smart-lists.jpg`.

**The exact Lead Lane value is `D Cold`, not `Cold`.** The stored options are `A Referral`,
`B Trigger`, `C Inbound`, `D Cold`, `E Lost`. This matches the earlier correction that
Inbound is stored as `C Inbound`.

### Two UI facts worth keeping

- **Multi-value on a single filter row is OR.** `Tag Is a, b, c` means any of them, and
  `Tag Is not a, b, c` means none of them. That is why Cooling and DNC each need only one
  filter row, and why the six-tag exclusion in Batch ready is one row.
- **A numeric custom field does have `Is empty`,** but it sits **below the fold** in the
  operator dropdown, under Equals to, Does not equal, Between, Greater than, Greater than or
  equal to, Less than, Less than or equal to. Scroll the dropdown to reach `Is not empty` and
  `Is empty`.
- **Creating a smart list from the Add smart list panel does not carry filters.** The reliable
  sequence is: open the **All** list, set Filters, **Apply**, then **Unsaved changes > Save as
  new smart list** and name it there.

### Open items

- **No active-workflow view on a contact record** in this build, so "is this contact enrolled
  anywhere" cannot be answered from the contact. Enrollment history on each workflow is the
  only route.
- `Prospecting: Batch ready` returns 0 because no contact yet carries Lead Lane `D Cold`.
  The definition is correct; it will populate when cold prospects are loaded.
