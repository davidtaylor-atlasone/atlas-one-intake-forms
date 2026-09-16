# RUN GHL-JOBS report: Run BA (fix Run AZ's output path, rebuild the Total Impact page, retire the stray tree)

Terminal: GHL-JOBS (files and code only). Brief: BRIEF-GHL-JOBS.md, copied to repo at
_briefs/BRIEF-GHL-JOBS-2026-09-16-RunBA.md. Prior report (Run AZ) backed up to
_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunAZ.md before starting.

## Built

### Job 1: agreement set moved to the real masters folder
- Backed up the stale real masters folder (40 files, pre software schedule) to
  `_to_delete/superseded-2026-09-16/agreements-before-runBA/`.
- Hardened `generate.py` `main()` (repo `tools/agreements/generate.py` and the Master Kit mirror
  `_INTERNAL (do not share)/tools/agreements/generate.py`, kept byte identical) to require an explicit
  Master Kit path argument, check its basename is literally `Atlas_One_Master_Kit`, and refuse to create
  a brand new `A1_Sales` tree if the resolved output parent does not already exist. It no longer defaults
  to the current directory.
- Found the Master Kit mirror of the agreements tool was missing `fonts_faces.css` and `_render_pdf.mjs`
  entirely (only the repo copy had them) and copied both over so the mirror can run standalone again.
- Regenerated all 21 docx and PDF pairs into the real folder:
  `2. Atlas 1 Solutions Marketing/A1_Sales/A1 Agreements/2026-09-15 masters/`.
- Moved the whole wrong tree `_INTERNAL (do not share)/tools/A1_Sales/` (confirmed it held nothing but
  the 42 stray agreement files) to `_to_delete/superseded-2026-09-16/wrong-path-tree-from-runAZ/`.
- `catalogue.py` entries already pointed at the real masters folder, no edit needed. `catalogue_check.py`
  OK (194 entries). Rebuilt Atlas One COMMAND.html (194 items, 48,454,266 bytes).

### Job 2: Total Impact Model builder made self-contained
- Backed up the current `Atlas_One_Total_Impact_Model.html` to
  `_to_delete/superseded-2026-09-16/Atlas_One_Total_Impact_Model_before_runBA.html`.
- Copied `tools/agreements/fonts_faces.css` (repo) beside `build_tim.py` in
  `08 ROI Quote Master Template/Total_Impact_Model/` for the font block (see Assumptions).
- Extracted a clean `tim_template.html` from the existing output HTML, with five placeholders swapped
  in where `build_tim.py` used to inject content: `@@FONT_FACES@@`, `@@ROWS@@`,
  `@@LINES_JSON@@`/`@@DIVS_JSON@@`, `@@SAMPLE_JS@@`, `@@BUILD_DATE@@`.
- Rewrote `build_tim.py` to read `fonts_faces.css` and `tim_template.html` from beside itself (no more
  `/home/claude/pb` or `/home/claude/tim/tim.html`) and write straight to the real output path,
  `A1_Sales/Total Impact Model/Atlas_One_Total_Impact_Model.html`.
- Ran it: rebuilt 401 KB, 0 dashes. Rebuilt `catalogue_check.py` (194 entries OK) and Atlas One
  COMMAND.html again (194 items, 48,589,802 bytes) since this tool is inlined there.

## Verification
- All 21 regenerated PDFs: BaseFont check shows only Horas-Medium, DMSans-Regular and DMSans-Bold.
- Read back the Software and Licenses Schedule table (6 rows: Microsoft 365 Business Basic $7,
  Standard $14, Premium $22, Copilot $21, QuickBooks Online Simple Start $38 / Essentials $85 /
  Plus $140 / Advanced $340, other resold software quoted) and the Bookkeeping Schedule's QuickBooks
  row (same 4-plan pricing) directly from the regenerated docx files. Both correct.
- Confirmed nothing else lived under `_INTERNAL (do not share)/tools/A1_Sales/` before moving it.
- Total Impact Model page, headless Chromium (Playwright) at 1440 px and 390 px:
  - `scrollWidth` equals the viewport at both sizes.
  - Zero console errors, zero non-`file://` network requests, at both sizes.
  - Technology & Operations block now shows the "Software supplied through Atlas One" row (absent
    before).
  - Clicking "Load sample" gives the same hero numbers before and after: net first-year impact
    $13,117, three-year impact $41,578, in both the rebuilt page and the pre-Run-BA backup (the
    sample JSON carries no software fields, so the new row falls through to "not quoted" / zero and
    does not move the total). Screenshots: `_briefs/assets/run-BA/shots/tim-1440.png` and
    `tim-390.png`.
- Atlas One COMMAND.html re-verified after the second rebuild: `scrollWidth` = viewport at 1440,
  zero console errors.

## Assumptions
1. The brief named the font source as `tools/self-assessment/fonts_faces.css`; no such file exists.
   `tools/self-assessment/index.html` embeds its `@font-face` rules inline with no sidecar CSS file.
   Used `tools/agreements/fonts_faces.css` instead: it is the actual base64 Horas + DM Sans block
   already shipping in this repo (and the same source the Job 1 agreement PDFs were just rebuilt
   against), so it satisfies "the same base64 Horas + DM Sans block every other tool embeds" even
   though the path in the brief was wrong.
2. Root cause of Run AZ's wrong output path: `generate.py`'s path math (`mk/../..` then
   `A1_Sales/A1 Agreements/...`) was already correct for a Master Kit path argument; Run AZ must have
   invoked it with the `_INTERNAL/.../tools/agreements` folder itself as the argument instead of the
   Master Kit root, which resolves one level short. Fixed by validating the argument's basename and
   refusing to write into a tree whose parent does not already exist, rather than only re-deriving the
   same math a different way.
3. `build_tim.py`'s `out` path goes up four directory levels from
   `08 ROI Quote Master Template/Total_Impact_Model/` to `2. Atlas 1 Solutions Marketing`, mirroring the
   fix already in `generate.py`. Verified by inspecting the actual resolved path before running.
4. Left `total_impact_model.py` (the PEO deck's own copy of the LINES/software_resold logic, added in
   Run AZ Job 3) untouched; this run only touched the client-facing HTML builder, per the brief's scope.

## Skipped
- Nothing in this brief was skipped. No hard stops were hit (no email/SMS, no HIPAA toggle, no file
  deletions, no production deploy, no spend).

## Questions for David
1. Should `generate.py`'s new hard requirement for an explicit Master Kit path argument be applied the
   same way to any other build script in this repo that resolves output paths relative to a passed-in
   argument (for symmetry, and to head off the same class of mistake elsewhere)?
2. The old `build_tim.py` read its font data from `/home/claude/pb` and its CSS shell from
   `/home/claude/tim/tim.html`, both cloud-sandbox scratch paths that never existed on this Mac before
   today. Is there other tooling in the Master Kit built the same way (a cloud session's local scratch
   paths hardcoded into a script meant to be rerun later) that should get the same self-contained
   treatment proactively, rather than waiting for it to break?
3. `08 ROI Quote Master Template/Total_Impact_Model/prospects/big_red_jelly.json` does not have the new
   `software_resold` fields populated (only used in Run AZ's smoke test as a text dump, not through this
   page). Want that sample prospect brought up to date with a real Microsoft 365 / QuickBooks Online mix
   so it exercises the new row when demoed through this HTML page, or is the "Tell Me More LLC" sample
   used by this page's own "Load sample" button enough?

