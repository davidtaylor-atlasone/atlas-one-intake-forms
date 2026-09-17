# BRIEF for the GHL-JOBS terminal: Run BE (one price source: the Quote Cockpit reads prices.json; kit index clean-up)

Terminal name: GHL-JOBS. Files and code only, headless Chromium for verification. Build end to end, no questions,
answer permission prompts yourself, log assumptions, questions at the END of the report. Back up the prior report
to `_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunBD.md` (already copied; overwrite is
fine). Back up every file before editing. Commit and push. Repo assets in `_briefs/assets/run-BE-jobs/`. No dashes
in copy. Clients are in all 50 states.

Answers to Run BD's questions (Cowork, 2026-09-16 22:00):
1. Noted; the five links are yours to keep working (Job 2 below re-tests them).
2. Yes, reword that paragraph (Job 2).
3. Yes. New standing rule for every GHL-JOBS run: before a job that moves or renames a file closes, grep the whole
   Master Kit, A1_Sales and the repo for the old path and filename and repoint every hit. Cowork is adding it to
   BUILD-INDEX as rule 40; you apply it from this run on.

## Job 1: the Quote Cockpit stops carrying its own price list
Today three tools carry prices: Quick Quote (`09 Quick Quote Tool/Atlas_One_Quick_Quote.html`), the Quote Cockpit
(`08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html`, its own service list and TIERSET), and
`_INTERNAL (do not share)/tools/agreements/prices.json` (the source the agreements, the Total Impact Model and
the repo Quick Quote read). Run AZ noted the Cockpit and Quick Quote "now need keeping in step". End that.
1. Read how `build_tim.py` (Total Impact Model) and the repo Quick Quote embed prices.json at build time. Do the
   same for the Cockpit: create `08 ROI Quote Master Template/build_cockpit.py` that reads prices.json (repo copy
   and _INTERNAL mirror are byte identical; read the _INTERNAL one, resolve the path relative to the script) and
   writes the Cockpit's service list, membership TIERSET (names, monthly, setup, headcount fit lines) and any
   other price constants into the HTML between two marker comments, keeping the file fully offline and self
   contained. The Cockpit must not fetch anything at run time.
2. If prices.json lacks a service the Cockpit lists today, add it to prices.json (both copies stay byte
   identical; run the same diff check Run BB used) with the Cockpit's current price, and list every such
   addition in the report. If the Cockpit has a price that differs from prices.json, prices.json wins; list
   every difference with old and new.
3. Verify: run the builder, open the Cockpit in headless Chromium at 1440 and 390, load the built in sample
   (or Save/Open a sample JSON), confirm the summary totals before and after the rebuild and explain any
   difference by the price differences in step 2. Zero console errors, zero non file requests, fonts still
   embedded, no dashes added. Export the one pager PPTX once and confirm it still downloads.
4. The membership headcount lines must read "1 to 20 employees, one state, under five hours a month of back
   office work. You do most of it yourself." and "15 to 50 employees, or five to fifteen hours a month. The owner
   is still the back office." (Run BC); make prices.json carry those strings so every tool prints the same words.
5. Retire nothing else this run; note in the report whether Quick Quote in `09 Quick Quote Tool/` also carries
   its own list (if it does, say so and estimate the same treatment for the next run; do not do it now).

## Job 2: kit index clean-up
In `Atlas One — Complete Kit for BRJ/⭐ START HERE — BRJ Index.html` reword the "Folder 10 — Premium Builders"
paragraph to say the five builders live in `06 Calculators and Tools` and open from the links below, no dashes in
the new sentence. Re-test all five links resolve. Then apply the new rule: grep the Master Kit, A1_Sales and the
repo for "10. Premium Builders" and for each of the five builder filenames and repoint or report every hit.

## Job 3: rebuild and verify
catalogue_check.py, rebuild COMMAND (the Cockpit is inlined), confirm the stamp, screenshots in
`_briefs/assets/run-BE-jobs/shots/`.

## Report
Built, Verification (before and after totals, the price differences table), Assumptions, Skipped, Questions.
