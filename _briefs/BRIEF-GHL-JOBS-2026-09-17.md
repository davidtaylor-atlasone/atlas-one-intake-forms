# BRIEF for the GHL-JOBS terminal: Run BF (three stale prices out of prices.json, Cockpit catalog matched to Quick Quote)

Terminal name: GHL-JOBS. Files and code only, headless Chromium for verification. Build end to end, no questions,
answer permission prompts yourself, log assumptions, questions at the END of the report. Back up the prior report
to `_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-JOBS-report-RunBE.md` (create the folder). Back up
every file before editing. Commit and push. Repo assets in `_briefs/assets/run-BF-jobs/`. No dashes in copy.

Answers to Run BE's questions (Cowork, 2026-09-17 07:45):
1. Enterprise and Concierge fit lines: keep the Cockpit's existing wording. Fine.
2. Yes, reword that heading (Job 2).
3. Quick Quote stays a Master Kit tool and it is the SOURCE for the service list. Do not move it onto
   prices.json; prices.json and the Cockpit follow Quick Quote, not the other way round (Job 1).

## Job 1: undo three stale additions and match the Cockpit's catalog to Quick Quote
Run BE copied three rows from the Cockpit into prices.json that are retired pricing and must come out:
`ai_services.concierge` ("AI Email Assistant, Concierge", $649: the Email Assistant has exactly two tiers,
Essentials $249 and Professional $499; $649 is from the retired $199/$349/$649 set), `documents.handbook_basic`
($299) and `documents.safety_basic` ($299) (Quick Quote sells one handbook at $950 and one safety manual at
$1,200, no basic tier). Quick Quote (`09 Quick Quote Tool/Atlas_One_Quick_Quote.html`, the 104 service list)
is the source of truth for WHICH services exist and at what price.
1. Remove those three entries from prices.json (both copies, byte identical after; run the diff).
2. Remove the matching three rows from the Cockpit's catalog (AI Email Concierge, basic handbook, basic safety
   manual) and any TIER_META or constant that only served them; rerun `build_cockpit.py`.
3. Then diff the Cockpit's whole catalog against Quick Quote's service list: for every Cockpit row, find the
   Quick Quote row with the same service (by name) and compare price, model (monthly, one time, per employee)
   and setup. Write `_BUILD-LOG/cockpit-vs-quick-quote-2026-09-17.md`: three tables, (a) rows that match,
   (b) rows in the Cockpit with a different price or model than Quick Quote (fix the Cockpit to match Quick
   Quote, through prices.json where the row is generated, and list old and new), (c) rows in the Cockpit that
   do not exist in Quick Quote at all (remove them from the Cockpit and prices.json; list them). Do not add
   anything to Quick Quote. The bookkeeping package defaults may stay as the Cockpit's own editable anchors
   (Quick Quote quotes ranges); say so in the report.
4. Verify as in Run BE: before and after totals on the same sample entity, zero console errors, zero non file
   requests, fonts embedded, 1440 and 390, one pager PPTX still exports. Screenshots.

## Job 2: BRJ index heading
`Atlas One — Complete Kit for BRJ/⭐ START HERE — BRJ Index.html`: reword the "Premium Builders" section heading
to "Premium Builders (the five document builders)" with no dash, so it no longer says "behind the paywall" next
to the paragraph that says no paywall is needed.

## Job 3: rebuild and verify
catalogue_check.py, rebuild COMMAND, confirm the stamp, screenshot.

## Report
Built, Verification (the three tables summarized, before and after totals), Assumptions, Skipped, Questions.
