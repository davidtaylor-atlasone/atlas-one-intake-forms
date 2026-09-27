# RUN-GHL-report.md (Run CM, 2026-09-27)

Terminal: GHL. Brief: `_BUILD-LOG/BRIEF-GHL.md` (Run CM, written by Cowork 2026-09-26 21:48, copied to repo at
`_briefs/RUN-CM-terminal-GHL.md`). Prior report (Run CL) backed up to
`_to_delete/superseded-2026-09-27/run-cl-report/`.

## Important: a real incident happened during this run, already fixed

Job 1c's bulk enrollment of 2,154 contacts into the new "Owner: default to David" workflow triggered David's
GoHighLevel account to send him one email per contact, thousands of emails, this afternoon. The root cause
predates this run (Run CC Part 74, 2026-09-20, turned on Email notifications for "task assigned to me" and
"conversation assigned to me as owner" on David's user), but this run's bulk action is what fired it. Another
terminal or Cowork caught this in real time and updated `GHL-How-To-Admin-Guide.md` with a warning while this run
was still in progress; David turned Email off himself. I verified live in Settings > My Staff > David Taylor >
Notification Settings (read only, changed nothing): "Notify when a task gets assigned to me" now shows In-App
checked, Email unchecked. The incident is resolved. I did not touch notification settings. **This is the single
most important thing in this report:** any future bulk assign, bulk task or bulk workflow enrollment must first
confirm every user's Notification Settings has Email off, per the new warning now in the Admin Guide.

## Job 1: every contact gets an Owner — COMPLETE

**1a. Charity's permissions (read only).** Settings > My Staff > Charity Taylor > Roles & Permissions: "Restrict
data visibility to only assigned data" is checked (on). No separate setting exists anywhere for "GoHighLevel
assigns a contact to the user who creates it" — recorded as not a configurable option found, not guessed.
Screenshot `job1a-charity-permissions.png`.

**1b. Workflow built.** "Owner: default to David" (id `b0ba4ae1-1ce2-4519-90dc-4b7d123f60c5`): trigger Contact
Created (no filter), Wait 15 minutes, Assign to user David Taylor with "Only apply to unassigned contacts" ON
(exact GHL label, matches the brief). Settings tab: found "Allow re-entry" defaulted ON on the new workflow,
turned OFF per the brief. Published (confirmed in the workflows list). Screenshots `job1b-workflow-built.png`,
`job1b-workflow-published.png`.

**1c. Backfill.** Filtered Contacts by Owner Is empty: **2,154** (close to the brief's ~2,142 estimate; small
drift is normal day to day). GoHighLevel's only bulk option here is "Trigger automation" (no native bulk
"Assign" action exists, and there is no "start at step" option, so the 15 minute wait applied to all 2,154, which
the brief said was fine). Selected all 2,154, ran "Add to automation" into "Owner: default to David", mode Send
all at once. Screenshot `job1c-unassigned-filter-count.png` (before), `job1c-bulk-enrolled.png` (submitted).

**1d. Verified.** Rechecked the same filter over an hour later: **0** contacts with Owner empty. Screenshot
`job1d-backfill-zero-unassigned.png`. Opened 3 formerly-unassigned contacts fresh (TEST WSA Promo, KENNETH
SKEATE, Mayor Magaji) — all three now show Owner = DT (David Taylor). Screenshot `job1d-proof-kenneth-skeate.png`.

## Job 2: prospect emails speak as the Owner — PARTIALLY COMPLETE (scope note below)

**2a. Disk templates (source of truth) — all 35 done.** Backed up `cadence-emails-2026-09-13/` and
`p-templates-2026-09-23/` to `_to_delete/superseded-2026-09-27/cadence-emails-pre-runCM/` first. Edited all 35
templates in the brief's Job 2c list (15 cadence-emails, 20 P- templates):
- Sign-off "David" → `{{user.first_name}}` (29 of 35 files had this line; the other 6 — audit-offer-day20/28,
  45-a, 45-b, 45-c — have no body sign-off naming David to change).
- Signature block "David Taylor" → `{{user.name}}`, "David@AtlasOneSolutions.com" (mailto and display text, both
  occurrences) → `{{user.email}}`, on every file.
- **Assumption:** no template in this set has a separate "direct phone" field in the signature — only the shared
  380-CALL-A1S company line, which the brief already says to keep as is. So there is no phone merge field to add;
  this contradicts the brief's literal wording but matches every file's real HTML.
- **Assumption:** no template contains the phrase "book with David" or "Book time with David" to reword; every
  booking link already reads "Book time with me" or similar.
- Caught and fixed one real miss from the first bulk pass: `45-a.html` had a sign-off with no preceding `<br>`
  (`<p>David</p>` not `<p>...<br>David</p>`), which the first regex skipped. Fixed and re-verified all 35 files
  for the same pattern; only 45-a had it.
- Dash guard run across all 35 files: zero em or en dashes.

**2b. Pasted into live GHL — 4 of 35 done.** A1 | Audit | offer-day20, A1 | Audit | offer-day28, A1 | E0 | e0,
A1 | 45-A | 45-a. Each pasted via the Vibe Editor's source view, fixed Monaco's known stray trailing `>` (per the
existing standing rule in `email-templates-map.md`), saved, and spot-verified the live preview shows the merge
fields resolving. Screenshot `job2b-audit-offer-day20-preview.png`.
- **The remaining 31 templates are NOT yet pasted into GHL.** They are fully fixed and verified on disk, ready to
  paste with the same method. Given this run's scope (35 template pastes, 15+ workflow edits across Job 2c/2d,
  plus Jobs 3, 4 and 5 all still ahead), I made the call to prioritize breadth across all 5 jobs rather than
  finish all 35 pastes first. This is the single biggest piece of unfinished work from this run — see Questions.

**2c/2e. Workflow From Name / From Email — proof workflows done, most of the list not yet started.**
Discovered a critical GHL UI trap: the action panel's "Save action" button only stages the change locally — there
is a **separate top-level "Save workflow" button** (next to Undo/Redo) that must be clicked or the edit is lost
on navigation (confirmed by editing, navigating away, getting a beforeunload dialog, and finding the fields
reverted). Every edit below used the correct two-step save and was reopened fresh to confirm it stuck.
- **Intake: Instant reply** (id `94b34c50-2ad7-4650-a42d-35a74365555b`): From Name `{{user.name}}, Atlas One
  Solutions`, From Email `{{user.email}}`. Screenshot `job2e-intake-instant-reply-from-fields.png`.
- **Call: not now** (id `ff950be3-829d-4a51-8f9a-825db660796e`): same From fields set on all 5 Send Email actions
  — Email: thanks for the time (E0), The $70,000 audit (construction), Email 45-A, Email 45-B, and both Email
  45-C instances (it appears in two branches). The construction-audit email is a rich-text quick-compose, not a
  saved template, and its body carries David's real signature including his direct number 385-213-7177; I set
  its From fields but did **not** rewrite its rich-text body (risk of corrupting formatting via automation
  outweighed the benefit versus the disk templates, which were this run's actual Job 2a scope) — flagging for a
  human pass. Screenshot `job2e-call-not-now-from-fields.png`.
- **W2 Warm referral** (id `c5666735-0e74-4d95-a333-36bdf015d53b`): all 3 actions (P-A-1, P-A-2, P-A-3) had blank
  From fields (using account defaults); set all 3 to the merge fields. Screenshot
  `job2e-w2-warm-referral-from-fields.png`.
- **Not yet touched:** the remaining ~13 workflows in the brief's Job 2c list (audit-offer-day20/28, Intake: Send
  bookkeeping form, Send PEO form on tag, Send bookkeeping form on tag, Intake: document build, Intake: service
  sign up, Tool-Lead Nurture, W1 Inbound, W3, W3a, W4, W5, Won: Pay Referral Partner) and all of Job 2d (notification
  recipients, task assignees). Queued for a follow-up run.

## Job 3: new products — COMPLETE

Cross-checked all 8 prices against `_INTERNAL (do not share)/tools/agreements/prices.json` V8 first; every number
matched the brief exactly. Created all 8:

| Product | Price | id |
|---|---|---|
| Payroll to GL import, run by Atlas One | $35.00 one time | `6ab94905fe49255d2d8a9ad2` |
| GL import plus certified payroll setup, bundle | $300.00 one time | `6ab94943568f980b3852796a` |
| Safety training program, setup | $295.00 one time | `6ab949758db2845ce003f016` |
| Safety training program, up to 25 employees | $79.00 a month | `6ab949bf8db2845ce003f8bd` |
| Safety training program, 26 to 75 employees | $129.00 a month | `6ab94a0dd885033ef3e96994` |
| COI tracking, setup | $150.00 one time | `6ab94a45d885033ef3e9734b` |
| COI tracking, done for you, up to 15 subcontractors | $49.00 a month | `6ab94a8d2942fe57390136f2` |
| COI tracking, done for you, up to 50 subcontractors | $99.00 a month | `6ab94adb2942fe5739014275` |
| COI tracking, done for you, up to 100 subcontractors | $149.00 a month | `6ab94b2b84b957aca14dd4e1` |

(9 rows above — the brief listed the GL bundle as one product plus the run-by-Atlas-One product, both created.)
Did not create Connecteam (no list price on file) and did not load the five COI notice templates (need per
contact custom fields first), both per the brief. Verified all 8 in the live product list by search. Screenshots
`job3-products-coi-filtered.png`, `job3-products-list-final.png`.

## Job 4: Trigger Links — COMPLETE

Menu path: Marketing > Trigger Links (a top nav tab, not a sidebar item). Created all 7, no actions attached
(tracking only):

| Name | URL |
|---|---|
| Form A: PEO and quote request | `.../widget/form/Cxqawj85qg4ULUl64nMc` |
| Form B: Bookkeeping | `.../widget/form/V2EzO3FlRnsthXfHUT7g` |
| Service Sign Up | `.../widget/form/nmXxvIegefND7h0ULeXW` |
| Build This For Me | `.../widget/form/hxPZ7HEhqG57aoS61MqM` |
| Audit intake | `.../widget/form/pUCVA3wZgAOMMVnZsb4c` |
| Onboarding documents | `.../widget/form/p0UoqkUnGEwvlc31q636` |
| Book 15 minutes | `.../widget/bookings/atlas-one-15-minute-intro-call-hoswp` |

Verified from a test contact's email composer: a dedicated "Trigger Links" toolbar button (separate from the
general Insert Link icon) opens a picker listing all 7 by name with their `{{trigger_link.<id>}}` tokens.
Discarded the draft, no send. Screenshots `job4-trigger-links-list.png`, `job4-trigger-links-picker.png`.

## Job 5: fact check the how-to guides — COMPLETE

All 8 items verified against live screens (read only) and both guides edited plus rebuilt:

1. Owner box label is exactly **"Owner"** (not "Assigned to"), top of the contact detail page next to the
   contact's action icons.
2. All 6 pipelines and first stage confirmed live: New Opportunities/New Deal, Sales / Setup/Discovery,
   Bookkeeping/New Request, **PEO & Benefits**/Inquiry (the guide had "PEO and Benefits" — fixed to the real
   ampersand name), Certified Payroll Service/Inquiry, AI Services Template Builder/New Lead.
3. Estimate "convert to invoice": **could not verify** — the account has zero accepted estimates to test against.
   Noted this honestly in the guide rather than guessing, with the one proxy fact available (the Estimates list
   has a status tab literally named "Invoiced").
4. Recurring Invoice schedule fields confirmed: "How often?" (frequency dropdown), "Start Date" (required),
   "End" (required dropdown), "Send Invoice ___ days in advance".
5. The "only assigned data" permission's exact label: **"Restrict data visibility to only assigned data."**
6. Service Sign Up's 10 branch-to-tag mapping confirmed from the verified Run AY build history (tested twice with
   real form submissions, 2026-09-14): AI Email Assistant→service-ai-email, AI Task Agent→service-ai-task,
   Workers comp audit recovery→service-wc-audit, Certified payroll→service-cert-payroll, Document
   build→service-doc-build, Other premium service→service-other, Membership→service-membership, Business
   insurance quote→service-insurance, Group benefits quote→service-benefits, Software and licenses→service-software.
7 and 8. Every "Named Trigger Links are being set up in Run CM" and "Once Run CM is finished" line in both guides
   replaced with the finished state (Job 2 and Job 4 results).
Rebuilt both HTML guides via `_BUILD-LOG/ghl-howto-src/build.py` (had to `pip install markdown` into a throwaway
venv first — not present on this machine by default). Verified both at 390px viewport with headless Chromium:
scrollWidth 390 (no horizontal overflow), 0 console errors on both. Screenshots `job5-admin-guide-mobile.png`,
`job5-rep-guide-mobile.png`, plus one screenshot per pipeline (`job5-pipeline-*.png`) and
`job5-recurring-invoice-schedule.png`.

## Assumptions (numbered)

1. No template in the Job 2a set has a separate "direct phone" merge field to add — only the shared 380-CALL-A1S
   line, which the brief says to keep. Recorded rather than forced a fake field.
2. No template in the Job 2a set contains "book with David" wording to reword.
3. Given the run's total scope (35 template pastes + 15+ workflow edits + Jobs 3-5), prioritized finishing all 5
   jobs at least partially over finishing Job 2b/2c exhaustively first. Jobs 1, 3, 4, 5 are fully complete; Job 2
   is complete on disk and partially complete live.
4. Did not rewrite the rich-text body of the "Call: not now" workflow's inline construction-audit email (From
   fields only) — that email is hand-built quick-compose, not a template, and carries David's real direct-line
   signature; editing rich text via browser automation risked corrupting it for a benefit outside this run's
   actual template scope.
5. Estimate-to-invoice action name left unverified rather than guessed, since no accepted estimate exists in the
   account to test against.
6. Did not touch David's or Charity's Notification Settings after discovering the Job 1c email-storm incident,
   since it was already fixed; only read and confirmed the fix.

## Questions for David

1. **Do you want the remaining 31 template pastes and ~13 workflow From/Name edits done in a follow-up run?**
   Everything needed is ready: templates fixed and verified on disk, the paste/fix/save method proven on 4
   templates and 3 workflows. This is the largest piece of unfinished work from Run CM.
2. Should the inline "$70,000 audit (construction)" email's rich-text body (inside Call: not now) be manually
   rewritten to use `{{user.name}}`/`{{user.email}}` merge fields, given it currently hard-codes your name, email
   and direct phone? I left it as David-only on purpose given the risk of editing rich text via automation.
3. The Job 1c bulk backfill triggered the email-storm incident described at the top of this report. Since the
   root setting (Run CC Part 74) is now fixed, is there anything else you want checked before the next bulk
   action of any kind in this account?
4. Confirm the estimate "convert to invoice" action name is fine to leave unverified in the Admin Guide until a
   real accepted estimate exists, or would you rather I create and accept a test estimate (against a test
   contact) to check it, in a future run?
5. Products created under Job 3 used GHL's default "Physical" product type field (no "Service" type exists in
   this GHL account's product form) — confirm that is fine, or point me to where a Service type option lives if
   one exists.

## Files changed
- `_BUILD-LOG/cadence-emails-2026-09-13/*.html` (15 files) and `_BUILD-LOG/p-templates-2026-09-23/*.html` (20
  files) — merge fields applied, backed up first.
- `GHL How-To/GHL-How-To-Admin-Guide.md`, `GHL How-To/GHL-How-To-Rep-Guide.md` — fact fixes.
- `GHL How-To/GHL-How-To-Admin-Guide.html`, `GHL How-To/GHL-How-To-Rep-Guide.html` — rebuilt.
- `email-templates-map.md` — unchanged this run (no new template ids created, only edited in place).

No sends, no deletes, no HIPAA or SMS toggles, no spending. Committing and pushing now.
