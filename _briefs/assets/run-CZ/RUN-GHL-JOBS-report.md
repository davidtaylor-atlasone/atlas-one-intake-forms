# RUN-GHL-JOBS-report, Run CZ, 2026-10-09

Run CY's report is archived at `_BUILD-LOG/RUN-GHL-JOBS-report-runCY-done-2026-10-07.md`. Brief copy: repo `_briefs/BRIEF-GHL-JOBS-2026-10-09.md`. Evidence: repo `_briefs/assets/run-CZ/`.

## Built

**Job 1: client folders removed from build manifests.**
- `_INTERNAL (do not share)/tools/bookkeeping-docs/build.py`: the `PROSPECT` and `ATH` constants (path under `1. A1 Solutions prospect_Client`) are gone. The Access To Hearing Client Agreement Packet and October invoice are now built only when `--client <folder>` is passed, and they write into the folder given. Off by default. The Access To Hearing proposal still renders beside build.py (Master Kit), as before.
- Rebuilt `manifest.json`: 9 entries down to 7, zero client folder paths.
- Every other build script checked for an output path under the client folder: `build_command.py`, `tools/agreements/generate.py`, `tools/division_sheets_build_2026-09-12.py`, `tools/render_html_pdfs.py`, `tools/build_mutual_nda_2026-09-12.py`, `tools/build_referral_partner_agreement_2026-09-12.py`, `_BUILD-LOG/brj-website-update-src/build_brj_update.py`, `_BUILD-LOG/appdirect/*.py`, the PEO generator, `export_for_cornerstone_crm.py`, `master-pricing-v8/build_master_pricing_v8.py`. None writes under the client folder, so nothing else needed removing. Only `build.py` had one. The SCL builder and a BRJ package builder script were not found as separate scripts in the Master Kit (the BRJ website update builder is the closest and is clean); see Questions.
- Repo (`atlas-one-intake-forms`): no live script writes to the client folder. Hits are only old run artifacts under `_briefs/assets/run-AG1c` and `run-AG1d`, left alone.

**Job 2: guard.** `_INTERNAL (do not share)/catalogue_check.py` has a new check, "no build manifest or output list writes under the client folder". It fails on a catalogue path, any `*manifest*.json`, or any build script (build*.py, *_build*.py, generate.py, render_*.py) containing `1. A1 Solutions prospect_Client` outside a comment. It was proven both ways: before the rebuild it FAILED on the stale `manifest.json` (lines 9 and 19), after the rebuild it prints `ok`.

catalogue_check result after the rebuild: 1 of 27 failed.
- FAIL `catalogue paths resolve`: `missing path: business-cards-folder: A1_Sales/Business Cards/`. Not from this run. The folder does not exist under A1_Sales. Not touched.
- The GHL How-To booking link fail (15 minute intro calendar in `GHL How-To/GHL-How-To-Admin-Guide.html` and `.md`) was FAILING at the start of this run and is PASSING now: the GHL lane edited that file at 17:46 during this run. I did not edit it.
- Note (existing): the installed atlas-pricing skill still prints 10 figures not in prices.json, pending David's yes on `SKILL-atlas-pricing-proposed.md`.

**Job 3: prove.** Snapshot of every file under `1. A1 Solutions prospect_Client` (1,217 files: mtime, size, path) before and after running the bookkeeping build (`python3 build.py`, then `node pdf.js`). Sorted and diffed: IDENTICAL, zero files added, removed or changed. Files in the repo: `_briefs/assets/run-CZ/client-tree-before-and-after-identical.txt`. The Access To Hearing files that sit in the client folder keep their earlier mtimes (Oct 9 17:21, written by the old build before this fix).

Every file the build changed (all Master Kit or A1_Sales, listed with mtimes in `_briefs/assets/run-CZ/changed.txt`):
- A1_Sales: `A1 What we do Overview/Atlas_One_Services_Overview.html` and `.pdf`; `Atlas 1 Bookkeeping/Atlas_One_Bookkeeping_Marketing_Sheet_V8.html` and `.pdf`; `Atlas_One_Client_Agreement_Packet_MASTER.pdf`; `Atlas_One_Invoice_MASTER.pdf`. (17:43:57 to 17:44:10)
- Master Kit `_INTERNAL (do not share)/tools/bookkeeping-docs/`: the 7 HTML pages, `manifest.json`, and the 3 PDFs (QuickBooks Accountant Access Guide, Access To Hearing proposal, Cirque Lodge proposal). (17:43:57 to 17:44:12)
- Not rebuilt: the Access To Hearing agreement packet and invoice (opt in only now). COMMAND was not rebuilt because no catalogue entry or tool changed.

## Looked at
No renders to look at: no layout changed. The build's own font check printed `fonts [true, true]` for all 7 PDFs.

## Assumptions
1. The opt in flag takes the target folder as its argument (`python3 build.py --client "<folder>"`), so the client folder name is never written in the script.
2. With the flag off, the stale Access To Hearing agreement and invoice PDFs already in the client folder are left exactly as they are.
3. The guard scans only manifests and build scripts under the Master Kit and A1_Sales (skipping `_to_delete`, `_BUILD-LOG`), plus catalogue paths. Comment lines are exempt.
4. `pdf.js` needed Playwright 1.63 from the `e41f203b7505f1fb` npx cache; the other cached version had no matching browser.

## Skipped
- The two build script names in the brief that I could not find as separate files: the SCL builder and a BRJ package builder.
- `render_html_pdfs.py` takes its job list from a CSV passed at run time, so the guard cannot see its paths; it has no client folder path of its own.

## Retire
Nothing replaced. Edited in place: `build.py`, `manifest.json` (regenerated), `catalogue_check.py`, the 9 regenerated HTML/PDF outputs above. Run CY's report was copied, not moved.

## Questions for David
1. Where are the SCL builder and the BRJ package builder? I found no script by those names. Point me at the paths and I will check them.
2. `A1_Sales/Business Cards/` is missing and catalogue row `business-cards-folder` points to it. Move the folder back, or drop the row?
3. Should the Access To Hearing agreement and invoice be regenerated into the client folder with `--client`? They were last written 17:21 today by the old build and are unchanged.
