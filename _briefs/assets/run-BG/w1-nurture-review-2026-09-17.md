# W1 nurture review (Run BG, Part 27, 2026-09-17)

Read only. No edits made to any workflow, tag, task or contact in this run.

## 1. W1 "Inbound speed to lead" full sequence after the Suppressed? gate

Workflow: `W1 Inbound speed to lead (duplicate instant reply removed 2026-09-16)`
(id `e50ddca0-1bc1-4a4b-a706-f2d02ba27259`), Draft toggle on, Publish on.

Trigger: Form A or Form B submitted (Form is any of "Atlas One PEO / Prospect Quote Request",
"Atlas One Accounting, Bookkeeping and Payroll Service Request").

Top of chain (before the Suppressed gate): Lead Lane C Inbound -> Add sequence active ->
Stamp Last Touch Date -> Suppressed?

### Suppressed? gate (If/else, "Build your own" recipe)

Branch "Suppressed" fires if Tags includes ANY of (OR logic across the list; each entry shown
requires "all of the selected tags", but the entries are OR'd together): `cooling 30d`,
`cooling 60d`, `cooling 90d`, `hold 6m`, `dnc` (at least 5 tag conditions confirmed in the
panel; the condition count badge read "11" so there may be more entries below the ones read on
screen; not fully scrolled and enumerated this run).

Branch "None" (default): none of the suppression tags present.

### Suppressed branch (in order)

| Order | Node | Type | Detail |
|---|---|---|---|
| 1 | #1 Task: suppressed inbound, decide by hand | Task | manual decision task |
| 2 | Email: P-C-0 Instant reply | Email, **Disabled** | node is disabled, does not send |
| 3 | END | | |

### None branch (in order, with waits)

| Order | Node | Type | Detail |
|---|---|---|---|
| 1 | #2 Task: CALL NOW | Task | the only task creator on the main path |
| 2 | Internal Notification | In-app push notification (NOT email) | Title "CALL NOW inbound lead", body "CALL NOW: {{Contact.Company Name}} {{Contact.Phone}}", to David Taylor. **Confirmed still ENABLED** (no "(Disabled)" tag on the node, unlike P-C-0). See Section 3, this contradicts Run BF Part 25's instruction to disable it. |
| 3 | Wait 4 hours (business hours) | Wait | |
| 4 | Replied already? | If/else | If Tags includes "reply received" |
| 4a | -> Reply received branch | | END (stop the cadence if the prospect already replied) |
| 4b | -> None branch (continues below) | | |
| 5 | #3 Task: Call 2 plus voicemail | Task | |
| 6 | Wait 1 day | Wait | |
| 7 | Email: P-C-2 Inbound Email 2 | Email, template `P-C-2 Inbound Email 2` (id `6aa0a9e60078269ef83ce1e3`, in email-templates-map.md, P- prospecting section) | Subject and From left blank (uses template default). **Footer phone is stale: 385-213-7177**, not the current 380-225-5217. |
| 8 | Wait 2 days | Wait | |
| 9 | #4 Task: Call 3 | Task | |
| 10 | Wait 3 days | Wait | |
| 11 | Email: P-C-3 Inbound Email 3 | Email, template `P-C-3 Inbound Email 3` (id `6aa0a9e82ac25123fb0d99aa`, in map, same section) | Subject and From left blank. **Footer phone is also stale: 385-213-7177**, and the footer includes the full compliance line "Atlas One Solutions LLC, Las Vegas, NV". |
| 12 | Add cooling 30d | Tag add | |
| 13 | Remove sequence active | Tag remove | |
| 14 | Wait 30 days | Wait | |
| 15 | Remove cooling 30d | Tag remove | |
| 16 | END | | |

## 2. Overlaps with other nurtures

| Workflow | Trigger | Suppression gate | Can it run at the same time as W1? |
|---|---|---|---|
| Post-Presentation Email | Pipeline stage changed to "Sales/Setup - Quote Gathering" OR "PEO - Census & documents collected" | **None found.** Linear sequence only: Wait 2 hours -> Email 1 -> Wait 3 days -> Email 2 -> Wait 4 days, no If/else node anywhere in the tree. | **Yes.** Any Form A/B submitter whose opportunity also gets moved into either of those two pipeline stages within the same window (for example a fast quote-gathering call) gets Post-Presentation emails with zero check against W1's cooling/dnc/hold tags or against W1's own in-flight state. Nothing here reads the "sequence active" tag W1 sets. |
| Tool-Lead Nurture | Contact Created, Lead Source is "Website Tool/Calculator" | "Already engaged?": If Tags includes "intake-received" -> END; else -> Email 5A -> Wait -> Email 5B -> Add Tag "nurtured" -> END | **Timing dependent.** This only checks the single tag `intake-received`, not W1's cooling/dnc/hold tags. W1 does not appear to set `intake-received` itself in the mapped chain (that tag is set elsewhere, per Run BF/BD context, on the Instant reply workflow). If a contact fills the tool calculator (creating the contact) and later submits Form A, whichever tag lands first decides: if `intake-received` lands before Tool-Lead Nurture's own Wait finishes, it gates correctly; if W1 (via the separate Instant reply workflow) is slower than that Wait, both nurtures fire concurrently, since Tool-Lead Nurture never checks W1's tags and W1 never checks `intake-received`/tool-lead source. |
| Call: not now | Tag added includes "not-now" | "Suppressed?": If Tags includes ANY of `client-current`, `do-not-prospect`, `partner`, `dnc` (confirmed 4; branch is "Build your own" so there may be more not read) | **Yes if double-tagged.** This gate does not check `cooling 30d/60d/90d` or `hold 6m`, the tags W1 uses. A contact who is both inbound-cooling (from W1) and manually tagged `not-now` (for example after a "call, not interested right now" outcome logged by David) would get both W1's remaining P-C-2/P-C-3 emails and the full Call: not now chain (E0, LT-1 through LT-5, 45-A) at the same time. Nothing in either workflow's gate references the other's tag set. |

## 3. Stale or Quick Compose emails found in W1

| Send | Node | Issue |
|---|---|---|
| Email: P-C-2 Inbound Email 2 | W1, None branch | Footer phone **385-213-7177** (stale, pre Run BE fix; should read 380-225-5217). Uses the template from email-templates-map.md (not Quick Compose), so the fix belongs in the template itself, not the workflow node. |
| Email: P-C-3 Inbound Email 3 | W1, None branch | Same stale footer phone **385-213-7177**, plus the compliance footer line "Atlas One Solutions LLC, Las Vegas, NV". Also template-based, not Quick Compose. |
| Email: P-C-0 Instant reply | W1, Suppressed branch | Disabled, not sent; not checked for phone freshness this run since it cannot fire. |
| Internal Notification | W1, None branch | Not an email (push notification type), so no footer/phone to check, but see the enabled/disabled finding below. |

No Quick Compose (non-template) email nodes were found in W1's mapped chain; both live email
sends (P-C-2, P-C-3) reference templates already listed in email-templates-map.md.

## 4. Recommendation

**Keep W1 as the inbound speed-to-lead workflow.** It is the only place that creates the CALL
NOW task chain (#1 through #4) and drives the 4-hour-then-daily call cadence that "Intake:
Instant reply" does not attempt. Folding it into the P-prospecting workflows (Post-Presentation
Email, Tool-Lead Nurture, Call: not now) would mean rebuilding that task cadence inside a
workflow designed for a different trigger shape (pipeline stage / tag-added / tool-lead source,
not form-submitted), which is a bigger and riskier change than fixing the three problems found
here.

Exact node changes a future run should make:

1. **W1 > Internal Notification action: disable it.** Run BF Part 25 instructed this and the
   report claims it was done, but the node in the builder today shows **no "(Disabled)"
   marker**, unlike the P-C-0 email node right above it which does show one. The disable did
   not save, or was reverted. This is a live discrepancy between the BF report and the current
   workflow state; flagging rather than fixing since this run is read only.
2. **P-C-2 Inbound Email 2 template and P-C-3 Inbound Email 3 template: replace 385-213-7177
   with 380-225-5217** in the footer (Email Builder API push, same pattern as the Run BE phone
   fix on the cadence templates).
3. **Post-Presentation Email: add a Suppressed? gate** mirroring W1's (at minimum checking
   `cooling 30d/60d/90d`, `hold 6m`, `dnc`) before Email 1, since it currently has no gate at
   all and can fire on top of any other active nurture for the same contact.
4. **Tool-Lead Nurture "Already engaged?" gate: add W1's cooling/dnc/hold tags** to the
   existing `intake-received` check, so a contact who is mid-W1-cadence does not also get
   Email 5A/5B from the tool-lead path.
5. **Call: not now "Suppressed?" gate: add `cooling 30d/60d/90d` and `hold 6m`** to the
   existing `client-current` / `do-not-prospect` / `partner` / `dnc` list, so a contact tagged
   both `not-now` and mid-W1-cooling does not receive both cadences.

## Assumptions

1. The Suppressed? gate condition count badge read "11" for W1 but only 5 tag entries were
   read on screen (cooling 30d, cooling 60d, cooling 90d, hold 6m, dnc); the remainder were not
   scrolled into view this run. Treated as "at least these 5" above rather than a complete list.
2. "Fired for him" style verification for Part 28 (below) used the workflow's Execution Logs
   panel, which the UI states covers the last 60 days; treated a "No logs found" result on that
   panel as proof the workflow has never executed for anyone in that window, Joel Gould
   included.
3. Where the tree showed a node id in an edge but no corresponding button rendered (this
   happened once, in Tool-Lead Nurture, for the "Add Tag - nurtured" END segment before a
   Fit to Screen + screenshot resolved it), a screenshot was used to confirm the actual node
   instead of relying on the accessibility tree alone.

## Skipped

- Did not scroll to the bottom of the W1 Suppressed? gate's full condition list past the 5th
  entry (dnc); the badge suggests more conditions exist.
- Did not open every node inside "Call: not now" past the Suppressed? gate (E0, LT-1 through
  LT-5, 45-A and their waits); the brief only asked for this workflow's trigger and gate, not
  its full map like W1.

## Questions for David

1. Should the Internal Notification node in W1 actually be disabled right now (per Run BF), or
   was that instruction superseded by something after Run BF that kept it live on purpose? The
   builder shows it enabled today.
2. Do you want the phone-footer fix (385 to 380-225-5217) pushed to the P-C-2 and P-C-3
   templates in this same pass as the other P- prospecting workflow templates (W7, cold outreach
   etc), since those may share the same stale footer and were out of scope for this read-only
   run?
3. Given the overlap findings, do you want the cross-workflow suppression gates (item 3 to 5 in
   the Recommendation) built now, or should W1 stay the only guarded nurture for now while the
   others get audited on a future run?
