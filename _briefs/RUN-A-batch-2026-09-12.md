# TERMINAL A BATCH (GHL browser UI only): Run P finish, Run Q copy edits, Run R service intake forms

## Progress log

- **2026-09-12, session start.** Chrome had just been restarted per the user's message. Navigated to
  `app.ridethehightide.com/workflows` to do the brief's low-stakes click test. The page never finished loading (stuck
  on GHL's own spinner past 20s, then the "click here to refresh" screen — not clicked), so per the dead UI rule did
  one real Cmd+R. After the reload the page went fully blank for 20+ seconds with zero interactive elements in the
  DOM. Console showed `FirebaseError: Missing or insufficient permissions` from GHL's app bundle, suggesting an
  auth/session issue rather than the leftover-modal cause from the prior report's Incident 2. **Stopped the whole
  batch per the rule** before any click landed and before Run Q or Run R were started. Full detail and next steps in
  `<Master_Kit>/_BUILD-LOG/RUN-P-report.md` (overwritten, "needs Chrome restart" at top).

Written by Cowork 2026-09-12 evening. David is away. Do all three runs in order, end to end, without asking questions.
Batch questions at the end of each report. Same rules as every GHL run: app.ridethehightide.com only, one tab, Chrome in
front, never click "click here to refresh", type email bodies through the </> source dialog (triple click inside the
textarea first), reload and re-read after every save, test contacts need a unique phone AND a plus-addressed email and
are deleted when done, no dashes anywhere in copy, never enable SMS, never enable the HIPAA feature. Copy this file to
`_briefs/RUN-A-batch-2026-09-12.md` in the atlas-one-intake-forms repo and log progress in it. Master Kit path:
`find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null | grep -vi -e _to_delete -e archiv`.

Dead UI rule: at the start of each run and after any blank canvas, open the Workflows list and click one workflow. If
the click does not land, do ONE Cmd+R, try once more, and if it still does not land STOP THE WHOLE BATCH, write the
report for the run you are in with the line "needs Chrome restart" at the top, and end. Do not try workarounds.

Reports: `<Master_Kit>/_BUILD-LOG/RUN-P-report.md` (overwrite), `RUN-Q-report.md`, `RUN-R-report.md`. Commit and push
after each run.

---

## RUN P: finish the follow-up cadence
Brief: `_briefs/RUN-P-cadence.md`. Current state (from RUN-P-report.md): Step 0 answered; tags quiet and recent-touch
exist; stage Quiet exists in Sales / Setup; "Post-Presentation Email" (304a9fa4-a256-4015-b767-031070f4186f) ends
Tag quiet -> Wait 4 days -> END with NO Gate 1; all ten email bodies final in `_briefs/assets/run-P/emails.md`.
Decisions already made: no opportunity stage move, tag only, no fork; no Quiet stage in PEO & Benefits; Part C is ONE
chained workflow; reuse "Last Touch Date".
1. Rebuild Gate 1 after "Wait 4 days": If/Else, six OR conditions, Tags includes reply received / booked /
   client-current / do-not-prospect / partner / dnc; yes branch ends the workflow. Publish, reload, re-read.
2. Copy action (node three-dot menu -> Copy action -> paste icon at the +), never cmd+v, for gates 2 to 6.
3. LT-1 to LT-5 from emails.md. After every send: Update contact field Last Touch Date = today, Add tag recent-touch,
   then the gate. Waits 4 / 4 / 14 / 14 / 3 days. End with Add tag not-now. Publish.
4. Part B in "Call: not now" (ff950be3-829d-4a51-8f9a-825db660796e): Last Touch Date = today + Add tag recent-touch
   after E0, 45-A, 45-B, 45-C; add client-current, quiet, dnc to the suppression gate if missing. Publish.
5. Part C: "Touch cooldown" (trigger tag recent-touch added, allow re-entry, Wait 10 days, Remove tag recent-touch).
   "Seasonal touches 2026-27": three tag-added triggers (hold-45, not-now, quiet), re-entry on, one linear chain at
   9:00 AM Mountain in date order: 2026-11-01 YE-1, 2026-11-15 YE-2, 2026-12-01 YE-3, 2026-12-15 YE-4, 2027-03-01 Q-1,
   2027-06-01 Q-1, 2027-09-01 Q-1. Every Wait: "If this date has already passed" = skip outbound till next wait.
   Before each send: suppression gate (client-current, do-not-prospect, partner, dnc, booked), then cooldown check
   (skip the send if tag recent-touch present). After each send: Last Touch Date = today + Add tag recent-touch.
   Publish. Bulk-add everyone currently in the Hold smart list once.
6. Part D: smart lists "Quiet / long tail" (tag quiet OR stage Quiet) and "Seasonal audience" (hold-45 OR not-now OR
   quiet, minus the five suppression tags).
7. Tests: one contact through Part A with every wait at 1 minute, prove the hand-off into "Call: not now"; one contact
   through Seasonal touches with the first date 2 minutes ahead, prove the send, prove the second pass is blocked by
   recent-touch. Put every wait and date back, reload and re-read each, delete both test contacts.
8. Commit, push, overwrite RUN-P-report.md (workflow ids, test times, skipped items, the December note: seasonal dates
   advance one year every December, questions).

## RUN Q: copy edits from David and the retention image
Source: `<Master_Kit>/_BUILD-LOG/cadence-email-ideas-2026-09-12.md`, items 1 to 6 and the E0 section. All edits are
through the </> source dialog on the existing branded wrapper; no dashes; keep every email short, one idea each.
1. 45-A ("Quick one", in "Call: not now"): second paragraph about workers comp class codes made explicit: owners often
   carry the wrong governing class, and nobody tracks employee hours by the work actually done, so nobody moves hours
   between class codes; tracked properly, with records, it saves thousands to tens of thousands a year. Add one
   home-by-five line near the close.
2. E0 (thanks for the call): add two links, not attachments, the Time and Cost Savings calculator and the Vendor
   Consolidation calculator at forms.atlasonesolutions.com/tools/ (find the exact paths in the repo `tools/` folder),
   plus one line offering the bilingual employee handbook builder as a member tool. Closing line is the home-by-five
   line. No safety manual.
3. New email "The $70,000 audit" for construction contacts only. Where: in "Call: not now", replace the 45-B send with
   an If/Else on the custom field Vertical = construction (the W0 vertical field; read its exact name and option value
   in the field list first): yes branch sends "The $70,000 audit", no branch sends the existing 45-B. Body: when a
   company does not collect certificates of insurance from its subs, the auditor charges premium on every uninsured
   sub's payroll; David just recovered over $70,000 for one client after a non-compliant audit; uninsured subs can sign
   a waiver so the client stops paying premium on them; two questions: "Have you ever had a non-compliant audit?" and
   "Do you like doing your insurance audits?"; booking link (15-minute intro). Same structure in "Post-Presentation
   Email" at the LT-2 slot (construction gets the audit email, everyone else keeps LT-2).
4. Q-1 (in Seasonal touches): add the time line: about a third of an owner's week goes to admin, 88 days a year, with
   a link to the Time and Cost Savings calculator. Add one home-by-five line to YE-1.
5. New email "A number most owners never add up" around the Vendor Consolidation calculator
   (forms.atlasonesolutions.com/tools/vendor-consolidation/): insert it as a new 45-B for everyone (the existing 45-B
   becomes 45-B-2 fourteen days later) ONLY if the "Call: not now" canvas edit stays simple; otherwise put it in the
   Seasonal touches chain as the 2027-06-01 send in place of that Q-1 and say so in the report.
6. LT-4 and Q-1: add a link to the Back Office Self-Assessment at
   `https://forms.atlasonesolutions.com/tools/self-assessment/` only if curl returns 200 (terminal B is building it in
   Run S). If 404, skip and note it.
7. 45-C: if `https://forms.atlasonesolutions.com/tools/assets/retention-sample-25ee.png` returns 200, insert it as an
   image above the button (plain img tag with width 560, alt "Sample retention cost result"). If 404, skip and note it.
8. Referral Partner dropdown (custom field, Prospecting or Sales folder): add options Ramp, Jotform, Deel, QuickBooks,
   Big Red Jelly. Verify with a page-text read after saving (options can silently fail to land).
9. Publish everything, reload and re-read each edited email, commit, push, write RUN-Q-report.md.

## RUN R: service intake forms and the "build this document for me" form
Check first what exists: Form A PEO (Cxqawj85qg4ULUl64nMc), Form B Bookkeeping (V2EzO3FlRnsthXfHUT7g), the AI Email
Assistant setup intake at forms.atlasonesolutions.com (in the repo), and the Onboarding Tracker fields
(`06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Tracker_Schema.md`). Reuse field names that already exist; create
new custom fields only when nothing fits. Forms are GHL native (Sites -> Forms), custom CSS design v3 like Forms A and
B, window at least 1512 px wide, save often (no autosave), audit every conditional rule after all structural edits.
1. Form C1 "Service sign-up" (one form, service picker first): Which service? (AI Email Assistant, AI Task Agent,
   Workers comp audit recovery, Certified payroll, Document build, Other premium service). Common block: company,
   contact, email, phone, headcount, states, best time to call. Conditional blocks shown only for the picked service:
   AI Email Assistant: mailboxes to connect (1 / up to 3 / more), email platform (Microsoft 365 / Google / other),
   who approves sends, plan (Essentials $249 / Professional $499), setup ($750 standard / $999 complex noted, not
   chosen by them). AI Task Agent: standalone $199 or bundled $99, where tasks live today (Outlook / GHL / paper /
   other). Workers comp audit recovery: carrier, policy renewal month, last audit result, do you collect COIs from subs
   (yes / some / no), number of subs, upload last audit letter (file), upload current WC policy (file). Certified
   payroll: agency (federal / Oregon / other), number of jobs, payroll system. Each block ends with a short "What we
   need from you and why" paragraph so David never goes back twice. Consent line, submit.
2. Form C2 "Have Atlas One build this for me": document picker (Employee handbook, Safety manual, Offer letter and
   at-will agreement, Independent contractor agreement, NDA, Other), what to add or change (long text), logo upload
   (file), HR contact name and email, states, headcount, deadline (date), anything else. Prefill from the query string
   parameter `doc` if GHL supports URL prefill on that field; note the result. After saving, take the form's public URL
   and put it into the constant `GHL_BUILD_FORM` at the top of `build/index.html` in the repo (terminal B created it in
   Run S; if the file does not exist yet, write the URL in the report and skip), push, and confirm
   `https://forms.atlasonesolutions.com/build/?doc=handbook` forwards to the form.
3. Two workflows: "Intake: service sign-up" (trigger form C1 submitted; add tag by service; create a task for David
   "Set up <service> for <company>" due next business day; send one confirmation email on the branded wrapper: what
   happens next and when, no dashes) and "Intake: document build" (trigger form C2; tag document-build; task for David
   "Build <document> for <company>, deadline <date>"; confirmation email; then a Wait 1 day and a second task
   "Deliver the built document" so nothing falls through). Publish both.
4. Seed each form with one test submission (unique phone, plus-addressed email), confirm the task and email fired,
   delete the test contacts. Commit, push, write RUN-R-report.md with the two form ids, the public URLs, workflow ids,
   any field that could not be created, and questions.
