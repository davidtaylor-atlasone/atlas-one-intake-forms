# RUN-GHL-JOBS report: Run AX (2026-09-15)

Terminal: GHL-JOBS (files and code only). Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md`, copied to
`_briefs/BRIEF-GHL-JOBS-2026-09-15.md` in the atlas-one-intake-forms repo. Prior report backed up to
`_to_delete/superseded-2026-09-15/prior-reports/RUN-GHL-JOBS-report-RunAW.md`. All backups for files
touched this run are in `_to_delete/superseded-2026-09-15/pre-RunAX-backups/` (Master Kit side) and
`_to_delete/superseded-2026-09-15/pre-RunAX-backups/` in the repo (for `prices.json` and `generate.py`).

## Job 1: COMMAND navigation, theme, text size, "Your queue"

Files: `_INTERNAL (do not share)/build_command.py`, `catalogue.py`. Output: `Atlas One COMMAND.html`
(185 items).

**Built:**
1. Clicking a left-rail item now filters the main pane to that section only (all other `.section`
   elements are hidden via JS, not scrolled past). The rail badge count always matches the number of
   visible rows. Search still searches every row regardless of the active section and switches to a
   "Search results" heading with every matching section shown.
2. Light is now the default theme and does not follow the OS (`prefers-color-scheme` no longer drives
   it). A "Dark theme" / "Light theme" toggle button sits at the bottom of the rail; the choice is
   remembered in `localStorage` (`a1cmd_theme`) and re-applied on load.
3. Text sizes increased: `.rtitle` 14px to 17px, `.rblurb` 12.6px to 15px, `.navitem` 13.5px to 16px,
   `.sechead` 18px to 22px. Same four-colour palette in both themes, contrast unchanged from the
   pre-existing (already-reviewed) light/dark pairs, just triggered by an attribute instead of a media
   query.
4. Added a `queue` + `queue_order` flag to four catalogue entries: AI Email Assistant Approval Queue
   (LIVE), Tasks & Follow-ups (LIVE), Activity log (LIVE), and Client Dashboard (GHL) (my read of "the
   client portal admin link", see Assumptions). All four are now `pinned=True`. `build_command.py`
   renders them as a first, explicitly titled "Your queue" group at the top of Start here, before the
   normal Tools/Links kind groups; they also still render under their native division (Technology &
   Operations / Intake & Client) because the pinned-row mechanism already duplicated pinned rows into
   Start here without removing them from their native section.

**Verification (headless Chromium, Playwright, `_briefs/assets/run-AX/shots/`):**
- 1440x900 and 390x844, light and dark: `scrollWidth` equals `clientWidth` at both sizes, zero console
  errors and zero page errors in all four runs.
- Clicked every one of the 14 rail items at every viewport/theme combination: exactly one `.section`
  had `display !== none` each time, and its visible row count matched its rail badge exactly (checked
  all 14 divisions, e.g. Start here 22/22, Sell & Pitch 27/27, Agreements 25/25).
- Start here's first `<h3 class="subhead">` reads "Your queue" in every run.
- Typing "handbook" shows the "Search results" heading and multiple sections with matching rows.
- Screenshots: `command-1440-light-starthere.png`, `command-1440-dark-starthere.png`,
  `command-390-light-default.png`, plus `-search` and `-default` variants for both widths and themes.
  Looked at all of them; light and dark both read clearly at the new sizes.

## Job 2: GL converter price split

Files: `tools/agreements/prices.json`, `generate.py` (this repo), `09 Quick Quote Tool/
Atlas_One_Quick_Quote.html`, `_INTERNAL (do not share)/Atlas_One_INTERNAL_Master_Pricing_V8.xlsx`,
`A1_Sales/A1 Agreements/Atlas_One_Agreements_How_They_Fit.md` (Master Kit side).

**Built:**
- `prices.json`: `gl_import.standard` ($75/mo for monthly, semi-monthly or bi-weekly) split into
  `monthly` ($50/mo) and `semi_monthly_biweekly` ($75/mo). Weekly ($125/mo), setup ($250, waived
  Professional+, included Concierge) and the extra entity/state add-on ($25/mo) are unchanged.
- `generate.py`: `schedule_gl_import()` and the GL sample proposal in `sample_proposals()` updated to
  reference the two new keys as two separate pricing rows instead of one.
- Regenerated all 19 docx + PDF pairs (`python3 generate.py "<Master_Kit>"`) into `A1_Sales/A1
  Agreements/2026-09-15 masters/`.
- Quick Quote `gl_import` line: default rate changed from 75 to 50 (still fully editable, per the
  tool's own "every price is a starting point" design), note updated to name all three frequencies.
- Master Pricing V8, Financial Services sheet, row 14 ("Payroll to GL import"): retail column (C14)
  set to 50 (the monthly-payroll base rate), note (H14) rewritten from "proposed... pending David
  approval" to "approved 2026-09-15" with the full frequency breakdown.
- `Atlas_One_Agreements_How_They_Fit.md`: appended a dated "2026-09-15 (Run AX)" section documenting
  the price split and every file it touched, matching the doc's existing changelog pattern.
- Rebuilt COMMAND (185 items, `catalogue_check.py` OK, forbidden-term guard passed).

**Verification:**
- `catalogue_check.py "<Master_Kit>"` -> OK, 185 entries, all paths resolve, both before and after the
  COMMAND rebuild.
- `Atlas_One_Payroll_to_GL_Converter_Schedule.docx` and `Sample_Proposal_Payroll_to_GL_Converter.docx`
  tables read back with python-docx: `Monthly payroll -> $50 a month`, `Semi-monthly or bi-weekly
  payroll -> $75 a month`, both present as separate rows.
- BaseFont check on both PDFs: `strings ... | grep BaseFont` shows only `AAAAAA+Horas-Medium`,
  `BAAAAA+DMSans-Regular`, `CAAAAA+DMSans-Bold`. No LibreOffice font substitution.

## Job 3: discount line on proposals and Quick Quote

Files: `tools/agreements/prices.json`, `generate.py` (this repo), `09 Quick Quote Tool/
Atlas_One_Quick_Quote.html` (Master Kit side).

**Built:**
- `prices.json`: added an empty top-level `"discount": ""` key, per the brief.
- `generate.py`: new `parse_discount_arg()` (accepts `"10%"` or `"$200"`, raises on anything else),
  `discount_line_text()`, and `apply_discount_to_rows()`. The last sums every pricing-table row whose
  price is an exact `"$X a month"` string (skips ranges, one-time fees, and per-unit add-ons, which a
  flat percent/dollar discount cannot cleanly apply to), then appends three rows under the existing
  ones: `List total (monthly)`, `Introductory discount: <n>% (or $<n>) off the monthly fee for the
  first 12 months` with the dollar amount taken off, and `Discounted total (monthly)`. The discount
  amount is rounded first and the discounted total derived from that rounded figure, so the three
  numbers always add back to the list total (fixed a $1 rounding mismatch found in testing). The list
  price is never edited or removed. `build_proposal()` and `sample_proposals()` take an optional
  `discount` parameter; `main()` reads a new `--discount VALUE` flag (only affects the sample
  proposals it builds, not the Schedules, matching the brief's "a proposal build accepts --discount").
  Running `generate.py "<Master_Kit>"` with no `--discount` flag (the normal, everyday invocation)
  produces the same pricing tables as before this change, confirmed by re-running it against the real
  Master Kit and reading the GL sample proposal's table back with python-docx.
- Quick Quote: added a "Discount" control (Percent off / Dollars off, plus an amount field) to the top
  of the Quote panel's toolrow (stage 4 of 5, the "totals panel"). New `S.disc` state persisted the
  same way as everything else in the tool (`localStorage`). `totals()` now also returns `disc`,
  `moNet` (monthly after discount) and `yrNet`. `renderQuote()` always shows a "Monthly (list)" box
  (list price never hidden), adds a "Monthly (with discount)" box only when a discount is set, an
  "Introductory discount" line item naming the terms, and a discount-adjusted "Year one" / "Total,
  first 12 months" figure. "Copy summary" updated to match so the plain-text export does not silently
  drop the discount.

**Verification (headless Chromium):**
- `generate.py` against a scratch output directory with `--discount 10%`: GL sample proposal table
  shows `List total (monthly) $125 a month`, `Introductory discount: 10%... -$13 a month`,
  `Discounted total (monthly) $112 a month` ($125 - $13 = $112, confirmed the rounding fix holds).
  Repeated with `--discount $200` (dollar form): correct clamping and correct row text. BaseFont check
  on the discounted PDF still clean (Horas/DMSans only).
- Re-ran `generate.py "<Master_Kit>"` with no discount flag: the real GL sample proposal and schedule
  read back with only the original pricing rows, no discount rows, confirming the default, everyday
  build is unaffected.
- Quick Quote at 1440x900 and 390x844: enabled "Payroll to GL import" ($50/mo + $250 setup), set a 10%
  discount. Quote panel showed Monthly (list) $50, Monthly (with discount) $45, an "Introductory
  discount, 10% off the monthly fee for the first 12 months, -$5/mo" line, and Total first 12 months
  dropping from $850 to $790 ($5 x 12 = $60 off $850). Zero console errors at both sizes, `scrollWidth`
  equalled the viewport at both sizes. Screenshot: `_briefs/assets/run-AX/shots/
  quickquote-1440-discount.png`.

## Assumptions

1. **"The client portal admin link" (Job 1, bullet 4).** No file or link in the catalogue is titled or
   described as an admin control for the client portal; the only client-portal-adjacent entry is
   `client-dashboard-ghl` ("Client Dashboard (GHL)" / "The client portal dashboard."). I treated this
   as the intended link, since it is the one entry David would open from COMMAND (an internal tool) to
   see or manage what the client portal shows. Left its `audience` as `client` (unchanged) since that
   only affects the forbidden-term content scan, not visibility inside COMMAND. If this was meant to
   point at a different, not-yet-catalogued admin URL, it needs to be added to `catalogue.py` and this
   assumption corrected.
2. **"Your queue" ordering (Job 1, bullet 4).** Ordered the four rows exactly as the brief lists them:
   Approval Queue, Tasks & Follow-ups, Activity log, then Client Dashboard (GHL) last.
3. **Default landing section (Job 1, bullet 1).** The brief does not say what the very first thing a
   visitor sees should be before any rail click. I defaulted to showing "Start here" (the first rail
   item) rather than showing every section, since "click a section to filter" implies there is always
   an active single section, and Start here is the natural landing page.
4. **Master Pricing V8 GL row (Job 2).** The sheet has one row per service; splitting monthly and
   semi-monthly/bi-weekly into two spreadsheet rows would have meant restructuring row references
   elsewhere in the sheet, out of scope for this brief. Instead I set the retail column (C14) to the
   monthly-payroll base rate ($50, the lower of the two new tiers) and put the full frequency
   breakdown in the note column (H14), which is where the sheet already carried this kind of detail.
5. **Discount scope in generate.py (Job 3).** Read "a proposal build accepts --discount" as scoping the
   flag to `sample_proposals()` only, not the Schedules (`schedule_gl_import()` etc.), since a Schedule
   is the contract attachment, not the sales proposal, and the brief's example line ("Introductory
   discount: ...") reads as sales copy for a proposal, not contract language.
6. **Discount applies only to exact monthly-fee rows (Job 3).** `apply_discount_to_rows()` only sums
   rows priced as a bare `"$X a month"` string. Bookkeeping's tiers are ranges ("$300 to $1,000 a
   month") and several proposals are entirely one-time fees (Document Services) or contingency-based
   (WC Audit Recovery) — a flat percent/dollar discount cannot be cleanly applied to a range or a
   percentage-of-recovery fee, so those proposals will show no discount rows even when `--discount` is
   passed. This matches "applies to the monthly fee" in the brief and avoids inventing a number for
   pricing that isn't a fixed monthly figure.

## Skipped

- Nothing in the brief was skipped. All three jobs were built and verified end to end.

## Questions for David

1. Is `client-dashboard-ghl` ("Client Dashboard (GHL)") really what you meant by "the client portal
   admin link" in Job 1? If you have a different internal-only admin URL for the client portal, send it
   and I will swap the "Your queue" entry (and catalogue.py) to point at that instead.
2. Master Pricing V8's Financial Services sheet still has one row for "Payroll to GL import" priced at
   the $50 monthly-payroll rate, with the $75/$125 tiers only in the note column (see Assumption 4). If
   you want the sheet itself to carry two separate rows (one per frequency) so it can be summed or
   referenced independently, say so and I will restructure it and any formulas that reference row 14.
3. The proposal-generator discount (Job 3) is a build-time flag (`--discount 10%` when you run
   `generate.py`), not something exposed anywhere in COMMAND or a form. If you want a way to trigger a
   discounted proposal build without running Python by hand, tell me the workflow you have in mind
   (a small script prompt, a Quick Quote export button, etc.) and I will build it.
