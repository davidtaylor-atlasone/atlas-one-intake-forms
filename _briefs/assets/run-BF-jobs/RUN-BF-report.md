# Run BF report (GHL-JOBS terminal), 2026-09-17

Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md` ("Run BF (three stale prices out of prices.json, Cockpit catalog matched to
Quick Quote)"). Copied to the repo at `_briefs/BRIEF-GHL-JOBS-2026-09-17.md`. All three jobs done end to end, no
hard stops.

## Built

### Job 1: undo three stale prices.json additions, match the Cockpit's catalog to Quick Quote

**1. Removed the three retired entries** from both copies of `prices.json` (`_INTERNAL (do not share)/tools/agreements/prices.json`
and the repo's `tools/agreements/prices.json`, kept byte identical, diffed after every edit):
- `ai_services.concierge` (AI Email Assistant, Concierge, $649) — the Email Assistant has exactly two tiers
  now, Essentials $249 and Professional $499.
- `documents.handbook_basic` ($299 one time) — Quick Quote sells one handbook, custom, $950.
- `documents.safety_basic` ($299 one time) — Quick Quote sells one safety manual, $1,200.

**2. Removed the matching rows from the Cockpit's catalog** (`08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html`):
the `hbBasic` and `safeBasic` catalog rows, and the "AI Email — Concierge" option from the `AIEMAIL` dropdown
array. Updated `build_cockpit.py` so `build_aiemail()` no longer reads `prices.json`'s `ai_services.concierge`
and `main()` no longer generates `HANDBOOK_BASIC_SETUP` / `SAFETY_BASIC_SETUP` (those constants and the print
statement that referenced them were removed). Reran `build_cockpit.py`; it wrote cleanly with no missing-key
errors.

**3. Diffed the Cockpit's whole catalog (31 rows in `cat()`) against Quick Quote's 104-row SERVICES list**, by
matching each row's service name/concept. Full three-table writeup at
`_BUILD-LOG/cockpit-vs-quick-quote-2026-09-17.md` (copied to `_briefs/assets/run-BF-jobs/`). Summary:
- **Matches (table a):** every generated figure (membership tiers, certified payroll, handbook, safety manual,
  AI Email, QBO, M365) already lines up, since prices.json is now the shared source for both tools. A handful
  of Cockpit rows (bookkeeping anchors, time & attendance vendor list, background/drug screening itemized
  types, P&C insurance lines, Jotform tiers, withholding setup defaults) are the Cockpit's own itemized
  vendor-comparison tools where Quick Quote only carries a flat figure or a generic "quoted" catch-all —
  nothing to reconcile there, same treatment the bookkeeping anchors already got in Run BE.
- **Fixed (table b), three real mismatches:**
  - `k401` (401(k) administration): setup was $350, Quick Quote's `k401` row is $450 → fixed to $450 (hand
    literal in `cat()`; prices.json has no retirement section to generate it from).
  - `qbgl` (QuickBooks integration / GL export-import): was $0/fully quoted, Quick Quote's matching `gl_import`
    row ("Payroll to GL import") defaults to $50/mo with $250 setup → fixed by wiring `build_cockpit.py` to
    `prices.json`'s `gl_import.monthly` / `gl_import.setup` (new `GL_IMPORT_PRICE` / `GL_IMPORT_SETUP` constants).
  - `strat` (Business strategy consulting): was $0/fully quoted, Quick Quote's `strategy` row defaults to
    $250/hour → fixed to $250 (hand literal; billed per hour typed in, same as Quick Quote).
- **No Quick Quote counterpart (table c):** none. Every Cockpit row maps to either a named Quick Quote row or
  one of its generic quoted catch-alls (software marketplace, general liability and related insurance,
  withholding setup), so nothing was removed under this heading.

**4. Verification:** Playwright (headless Chromium) against the same seven-item sample entity (certified
payroll, 401(k), GL import, business strategy, AI Email Assistant, custom handbook, custom safety manual), run
on the pre-edit backup and the rebuilt Cockpit:
- Before: $374/mo, $3,250 setup. After: $674/mo, $3,600 setup. The $300/mo and $350 setup differences match the
  three fixes exactly ($50 GL import + $250 strategy monthly; $100 401(k) + $250 GL import setup).
- AI Email dropdown confirmed down to three options (Essentials, Professional, Extra mailbox); Concierge gone.
- Zero console errors, zero non-file network requests, scrollWidth equals viewport at 1440px and 390px, on
  both the before and after versions.
- Fonts: 4 `@font-face` blocks still embedded as base64.
- One-pager PPTX export: clicked the button, download completed, zero console errors.
- Screenshots and the test PPTX at `_briefs/assets/run-BF-jobs/` (shots subfolder for the images).

### Job 2: BRJ index heading

`Atlas One — Complete Kit for BRJ/⭐ START HERE — BRJ Index.html`: reworded the Premium Builders section
heading from `"Premium Builders — build behind the paywall"` (an em dash, and text that directly contradicted
the paragraph right above it saying no paywall is needed right now) to `"Premium Builders (the five document
builders)"`, no dash. Verified with headless Chromium: the `<h2>` renders the new text, zero console errors,
zero non-file requests, scrollWidth equals viewport at 1440px and 390px. Screenshots at
`_briefs/assets/run-BF-jobs/shots/brj_index_1440.png` and `_390.png`.

### Job 3: verify and rebuild

- `catalogue_check.py`: 192 entries, all paths resolve (unchanged; this run touched no catalogue paths).
- Backed up the pre-run `Atlas One COMMAND.html` to `_to_delete/superseded-2026-09-17/command-before-runBF/`,
  rebuilt it (192 items, 48,648,912 bytes), stamp confirmed: `Atlas One COMMAND: build Sep 17, 2026  7:49 AM`.
  Headless Chromium at 1440px: zero console errors, scrollWidth equals viewport. Screenshot at
  `_briefs/assets/run-BF-jobs/shots/command_1440.png`.

## Files touched

- `_INTERNAL (do not share)/tools/agreements/prices.json` and the repo's `tools/agreements/prices.json` (byte
  identical, three entries removed)
- `08 ROI Quote Master Template/build_cockpit.py` (concierge dropped from `build_aiemail()`, basic-tier
  constants dropped, GL import constants added)
- `08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html` (rebuilt by `build_cockpit.py`; two catalog rows
  removed by hand, two catalog rows' literals fixed by hand — k401, strat — one row rewired to generated
  constants — qbgl)
- `Atlas One — Complete Kit for BRJ/⭐ START HERE — BRJ Index.html` (one heading string)
- `Atlas One COMMAND.html` (rebuilt)

Backups before every edit: `_to_delete/superseded-2026-09-17/before-runBF/` (prices.json, the Cockpit,
build_cockpit.py, the BRJ index) and `_to_delete/superseded-2026-09-17/command-before-runBF/` (COMMAND). Prior
report backed up to `_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-JOBS-report-RunBE.md`.

## What was looked at

- Full read of Quick Quote's SERVICES array (104 rows) and the Cockpit's `cat()` function (31 rows) plus the
  sub-option lists it references (TALINES, SCREEN, INSLINES, JOTF, BKPKG, QBO, M365, AIEMAIL, MEMTIER).
- `build_cockpit.py` end to end, including the marker-fenced blocks it generates in the Cockpit.
- Playwright screenshots at 1440px and 390px for the Cockpit (before and after), the BRJ index, and the
  rebuilt COMMAND.
- The downloaded one-pager PPTX (confirmed it downloads and the export path runs with no console errors; did
  not open and inspect every slide by hand).

## Assumptions

1. Treated Quick Quote's "quoted" catch-all rows (`sw_marketplace`, `gl`/`eo`/`cyber`/`keyman`/`bonds`,
   `wh_setup`) as valid counterparts for the Cockpit's itemized vendor-comparison sub-lists (Jotform tiers,
   P&C insurance lines, withholding setup defaults), rather than treating each itemized sub-line as a
   standalone service needing its own Quick Quote match. Reasoning: Quick Quote intentionally doesn't itemize
   at that level; the Cockpit's itemization is its own internal quoting detail, same treatment the bookkeeping
   package anchors already got in Run BE.
2. For `ta` (Time & Attendance) and `screen` (Background & drug screening), only the one sub-option that does
   overlap Quick Quote by name (Connecteam Operations Hub, $5/EE/mo) was checked and matches; the other vendor
   options (SwipeClock, TLM, Prism HCM, the 17 itemized screening check types) have no Quick Quote figure to
   compare against at all, so they were left alone rather than deleted.
3. For the three genuine mismatches found (k401, qbgl, strat), fixed the Cockpit's default number to Quick
   Quote's number even though two of the three (k401, strat) are hand literals rather than prices.json-generated
   — reasoning: the brief's instruction was "fix the Cockpit to match Quick Quote, through prices.json where the
   row is generated," which implies a hand fix is fine where it isn't generated. Did not expand prices.json's
   schema to add a retirement/consulting section for these, to avoid enlarging its scope beyond what this run's
   brief asked for.
4. `qbgl` was judged to be the same service as Quick Quote's `gl_import` ("Payroll to GL import") based on both
   living under Financial Services and both describing payroll-to-QuickBooks/Sage journal conversion. Wired it
   to `gl_import`'s monthly figure ($50) as the default rate rather than adding pay-frequency sub-options
   (Quick Quote itself uses a single editable rate with a note about the frequency variants, not a dropdown),
   to match Quick Quote's own presentation.
5. Left `apar` (A/P + A/R management) alone rather than guessing a default — see Questions below.

## Skipped

- Nothing in this brief was skipped.

## Questions for David

1. **`apar` (A/P + A/R management) in the Cockpit bundles two separate Quick Quote services** (`ap`, $250/mo,
   and `ar`, $250/mo) into one row, currently defaulting to $0/fully quoted. Should it default to $250/mo (as
   if only one of the two is typically sold together), $500/mo (both), or stay fully quoted as it is now? Left
   untouched pending your call.
2. Same three questions Run BE left open at the end of its report are still open (bookkeeping package point
   defaults vs. Quick Quote's quoted ranges being intentionally different structures; whether the AI Task Agent
   standalone figure should ever surface in the Cockpit's own catalog rather than only the bundled figure; and
   whether Quick Quote itself should eventually move onto the same `build_*.py` pattern as the Cockpit). Not
   part of this brief's scope, just flagging they're still outstanding.
3. The Cockpit's `ins` row groups General Liability, Professional Liability, E&O, Property, Cyber, Bonds and
   several other lines into one card (all quoted, itemized with `INSLINES`), while Quick Quote prices `gl`,
   `eo`, `cyber`, `keyman` and `bonds` as five separate quoted rows. Both are "quoted" so there's no number in
   conflict, but if you'd like the Cockpit split to mirror Quick Quote's five-row split exactly, that's a
   larger restructure than this brief covers — say the word and it's a quick follow-up job.
