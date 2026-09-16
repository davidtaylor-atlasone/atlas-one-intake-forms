# BRIEF for the GHL-JOBS terminal: Run BA (fix Run AZ's output path, rebuild the Total Impact page, retire the stray tree)

Run AZ is done and audited. Its Job 2 wrote the 21 agreement documents to the WRONG place: it created a new tree
`_INTERNAL (do not share)/tools/A1_Sales/A1 Agreements/2026-09-15 masters/` inside the Master Kit. The real,
client-facing masters folder is `2. Atlas 1 Solutions Marketing/A1_Sales/A1 Agreements/2026-09-15 masters/`
(sibling of HR_Docs, NOT inside the Master Kit). Cowork could not move files itself (sandbox), so this run does it.

Terminal name: GHL-JOBS. Files and code only. Back up the prior report to
`_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunAZ.md`. Commit and push. No dashes.
Answers to Run AZ's questions: Ledger and Solopreneur stay dropped. QuickBooks Time stays quoted. Pax8 costs
come later from David (leave the Cockpit cost field at 0). The Cockpit reading Quick Quote's catalogue is a
later job, not this one. The software one-pager tgz belongs to another chat; leave it.

## Job 1: put the agreement set where it belongs
1. Back up the current real masters folder (every file) to `_to_delete/superseded-2026-09-16/agreements-before-runBA/`.
2. Fix `generate.py` (repo `tools/agreements/generate.py` AND the Master Kit mirror) so its default output is the
   real masters folder above, resolved from the Master Kit path argument by going up to `2. Atlas 1 Solutions
   Marketing` and into `A1_Sales/A1 Agreements/2026-09-15 masters`. Never write under `_INTERNAL` again.
3. Regenerate all 21 docx and PDF pairs into the real folder (overwriting the same-named files; that is the
   point). BaseFont check on every PDF: Horas and DM Sans only. Read back the Software and Licenses Schedule and
   the Bookkeeping Schedule tables and confirm the six software prices and the QuickBooks line print.
4. Move the whole wrong tree `_INTERNAL (do not share)/tools/A1_Sales/` to
   `_to_delete/superseded-2026-09-16/wrong-path-tree-from-runAZ/`. Confirm nothing else lives under it first.
5. `catalogue.py`: confirm every agreement entry points at the real masters folder (it should already); run
   `catalogue_check.py`; rebuild COMMAND; confirm the stamp.

## Job 2: rebuild the Total Impact Model page so the software line is live
`A1_Sales/Total Impact Model/build_tim.py` depends on `/home/claude/pb` and `/home/claude/tim/tim.html`, which
were a cloud sandbox's scratch files and do not exist on this Mac. Make the builder self-contained:
- the font block comes from `tools/self-assessment/fonts_faces.css` in the repo (same base64 Horas + DM Sans every
  other tool embeds);
- the page template is the existing output `Atlas_One_Total_Impact_Model.html`: read it, locate the embedded
  LINES JSON (and any other block build_tim.py injects), and save a clean template `tim_template.html` beside
  build_tim.py with placeholders where those blocks go. Then build_tim.py reads the template and fonts from
  beside itself. Back up the current HTML first to `_to_delete/superseded-2026-09-16/`.
- Rebuild. Verify in headless Chromium at 1440 and 390: the Technology & Operations block shows the new
  "Software supplied through Atlas One" row, the sample number for the 25 employee company is unchanged from
  before (read the hero number before and after and print both), zero console errors, no external requests.
- Rebuild COMMAND again if the HTML is inlined there.

## Report
Built, paths, Verification, Assumptions, Skipped, Questions for David.
