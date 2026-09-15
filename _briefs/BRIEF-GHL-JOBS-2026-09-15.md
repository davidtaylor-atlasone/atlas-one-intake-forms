# BRIEF for the GHL-JOBS terminal: Run AX (COMMAND navigation and theme, GL converter prices, discount line)
Run AW (35 templates) is done and audited. Back up the prior report to `_to_delete/superseded-2026-09-15/prior-reports/RUN-GHL-JOBS-report-RunAW.md`.

Terminal name: GHL-JOBS. Files and code only. Build end to end, no questions, permission prompts answered by
you, assumptions logged, questions at the END of the report. Live log `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`;
report `_BUILD-LOG/RUN-GHL-JOBS-report.md`. Back up the prior report to
`_to_delete/superseded-<date>/prior-reports/`. Back up every file before editing it. Commit and push.

## Job 1: COMMAND navigation (David, 2026-09-15, with screenshots)
Source: `_INTERNAL (do not share)/build_command.py` and `catalogue.py`. Output `Master_Kit/Atlas One COMMAND.html`.
1. Clicking a left-rail section must show ONLY that section's rows on the right. Today it scrolls to the
   section heading and the other sections are still below it, so David scrolls out of Technology &
   Operations into Business Consulting without noticing. Filter, do not scroll-jump. "Start here" shows
   only the pinned rows. Search still searches everything and shows a "Search results" view.
2. Default to the LIGHT theme (off-white #FAFAF8 page, soft blue #DBE4ED rails and cards, dark blue text).
   Keep the theme toggle; remember the choice in localStorage. David finds the dark build hard to read:
   "everything is dark navy on a black background".
3. Text one step bigger everywhere: row titles 17px, blurbs 15px, rail items 16px, section headings 22px.
   Re-check contrast in both themes against the four brand colours; status by form, never a fifth colour.
4. Move the three AI Email Assistant links (Approval Queue, Tasks & Follow-ups, Activity log) and the client
   portal admin link into "Start here" as the first group, titled "Your queue", and pin them. Keep them in
   Technology & Operations too.
Verify in headless Chromium at 1440 and 390, both themes: click every rail item and confirm the right pane
holds only that section (count rows against the rail badge), zero console errors, scrollWidth = viewport.
Screenshots in `_briefs/assets/run-AX/shots/`. Look at them.

## Job 2: GL converter prices (David approved 2026-09-15)
New client prices: monthly payroll $50 a month; semi-monthly or bi-weekly $75 a month; weekly $125 a month;
setup $250 one time, waived on Professional and above, included in Concierge; each additional entity or
state journal on the same payroll $25 a month. Update, in this order, backing up each first:
`tools/agreements/prices.json` (gl_import: split "standard" into monthly $50 and semi_monthly_biweekly $75),
regenerate the GL Converter Schedule and its sample proposal (docx + PDF, Horas/DM Sans only, check BaseFont),
Quick Quote `gl_import` rate and documentation note (09 Quick Quote Tool), Master Pricing V8 xlsx Financial
Services GL row (retail column now approved, note "approved 2026-09-15"), `Atlas_One_Agreements_How_They_Fit.md`.
Rebuild COMMAND.

## Job 3: discount line on every proposal and on Quick Quote
Add an optional discount to the proposal generator: `discount` in prices.json is empty by default; a proposal
build accepts `--discount 10%` or `--discount $200` and prints a line "Introductory discount: 10% off the
monthly fee for the first 12 months" (or the dollar form) under the totals, with the discounted total next to
the list total. Quick Quote gets a single "Discount" control at the top of the totals panel (percent or dollar,
applies to monthly recurring, shown as its own line on the printed quote). Never hide the list price.

## Report
Built, Verification (screenshots, BaseFont check, Quick Quote render), Assumptions, Skipped, Questions for David.
