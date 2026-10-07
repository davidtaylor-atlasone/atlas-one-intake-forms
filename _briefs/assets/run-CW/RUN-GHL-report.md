# RUN-GHL-JOBS report: Run CW, 2026-10-06 (19:30 to 20:40 MT)

Terminal: GHL-JOBS (code and files only, never the GHL UI). Brief: `BRIEF-GHL-JOBS.md` (copied to `_briefs/BRIEF-GHL-JOBS-2026-10-06.md` in the intake forms repo). Run CU report archived first as `RUN-GHL-JOBS-report-runCU-done-2026-10-06.md`.

## Status in one look

| Job | Result |
|---|---|
| 1. Annual plans OFF | DONE. Zero annual plan phrases across the Master Kit and A1_Sales (text, DOCX, PPTX, XLSX, PDF). Guard added so they cannot come back. One exception: Dr Gould's six live deal PDFs, see Questions 2. |
| 2. Builder no longer makes _to_delete | PARTLY DONE. New guard written and wired around the COMMAND and Sales Kit build. The change to `build_command.py` that stops the rep kit build from moving the old kit into `_to_delete` was DENIED by the permission classifier (twice). Not done. See Questions 1. |
| 3. Small follow ups | DONE (Quick Quote W-2 line, Utah and Draper to [City] and [state], Comp and commission plan design on the allow list). |
| 4. Rebuild and prove | PARTLY DONE. COMMAND and Sales Kit rebuilt, 25 of 25 guards green, renders clean. Charity's kit and zip NOT rebuilt (blocked by Job 2). Her zip still has the old annual wording, do not send it. |

## Job 1: annual plans are OFF (David, 2026-10-06)

Sources edited first, then every output regenerated or patched in place.

- `tools/agreements/prices.json`: now V11. Enterprise setup reads "$995, often waived". `annual_plans` status is OFF. Changelog line added: "V11 2026-10-06 annual plans removed, David."
- Membership brochure and Membership Pricing page (HTML, then PDF reprinted with `render_html_pdfs.py`, page counts same: 4 and 1), Price List (HTML, template, PDF reprinted, 3 pages), division sheets (`division_sheets_build`, Consulting sheet), Professional Membership Inclusions and Membership Scope templates (HTML and PDF), Quick Quote (html and json), Quote Cockpit (html and `build_cockpit.py`), Audit Workbench (and its embedded copy of prices.json), Prospect Web Pitch, Service Content Library (FAQ "Is annual billing required?" became "Is the setup fee always charged?": "No. The $995 setup fee is often waived, and your Atlas One proposal states exactly what is due."), BRJ Pricing Page SPEC (html plus preview PDF at 1120 px so it stays 5 pages at 840 by 792).
- Membership Schedule and all 22 agreement masters: `generate.py` heading "Setup fee and annual option" became "Setup fee", the "or on an annual plan" wording is gone. Rebuilt with `generate.py` (docx and pdf).
- Pitch decks: First Meeting, Prospect, Partner General LIGHT (the "waived on an annual start" and "waived on annual" lines). First Meeting deck PDF re-exported (9 pages), copy in `06 Calculators and Tools` refreshed.
- Micah (ExcelHealth) package: Executive Summary Insert docx and PDF re-exported (4 pages); Non Insurance Services Menu PDF has no source file, so that one line was patched inside the PDF (redact and rewrite, same size and colour, looked at, clean).
- AI Email demo decks (Tell Me More LLC): the "Pay annually, Setup waived + 15% off, saves $1,648" row removed and replaced with "Billing, Monthly" so the table has no empty row.
- INTERNAL: `Selling_the_Membership_INTERNAL` PDF (lever 2 "Annual plan: two months free" is now "Never offer free months, prepay deals or a discount on the monthly"; no HTML source exists so the PDF was patched, looked at), Master Pricing V8 xlsx note and builder, Jason Petty kit, AI Assistant Intake Requirements (annual question removed), `gen_pricing_skill.py` text, `hubs.py` and `catalogue.py` blurbs.
- Price guard: `price_scan.py` has a new rule "Annual plan offers" (two months free, waived on annual, pay annually, annual billing, annual option, annual prepay, monthly or annual, 15% off annual). `catalogue_check.py` runs it, so a hit fails the build.
- BRJ package rebuilt with today's date: `A1_Sales/Website/Atlas One for BRJ 2026-10-06/` and `.zip` (47 files: the 41 from 2026-10-04 plus a new "4 Pricing Page" folder with the corrected SPEC, brochure, pricing and preview PDFs and the instructions).

Left as is on purpose: Microsoft 365 "per user, annual term" (a vendor licence term, not an Atlas One plan offer), "annual Back Office Audit" and "Annual security audit" (service names), AppDirect internal vendor contract terms, Competitive Intel deck and the Rippling email (a competitor's offer, excluded from the guard).

## Job 2: stop the builder making _to_delete folders

- `retire_guard.py` (new, `_INTERNAL`): `snapshot()` and `assert_none_created()` fail a build that creates any folder named `_to_delete` or `superseded-*` under the Marketing root. It also runs around any command: `python3 retire_guard.py "<Master_Kit>" -- python3 build_command.py "<Master_Kit>"`. The COMMAND and Sales Kit build ran under it this run: passed, 4 pre existing folders ignored.
- NOT done: editing `build_command.py` `build_rep_everything()` so `--person` overwrites in place and prints RETIRE and STALE lines instead of moving the old kit into `_to_delete/superseded-<date>/`. The edit was denied (reason given: irreversible local destruction). I did not retry it another way, and I did not run `--person charity` with the old code because that would create the folder this brief forbids. The original file is unchanged, see Questions 1.
- Also untouched for the same reason: `tools/agreements_inventory_2026-09-12.py` still has an opt in `--move` that parks duplicates in `_to_delete`. It only runs if someone types `--move`.

## Job 3: small follow ups

1. Quick Quote year end W-2 line now reads "Year-end W-2s (one extra payroll run at your rate, monthly minimum applies)" (html and the json source).
2. David's masters: Prospecting Playbook (time zone block now "in the time zone of each list; one batch per time zone", "owners in [state]", "[City] location"), Overlay 01 and 02 (Draper to [City]), Overlay 03 ("the cold months in your state"), Overlay 04 ("[state] software teams"), PrismHR census template Provo row to [City], [State], [ZIP]. `rep_scrub.py` kept working (its strict Utah block rewrite is now tolerant); `test_rep_scrub.py` ALL PASS.
3. "Comp and commission plan design" is on the rep pay guard allow list (`ALLOWED_SERVICE_NAMES` in `rep_scrub.py`, used by the pay scan and the final forbidden term scan, plus a test line).

## Job 4: rebuild and prove

- `catalogue_check.py`: OK, 216 entries, all 25 checks passed. Two failures found and fixed first: the Audit Workbench embedded PRICES copy (refreshed from prices.json) and a dead catalogue row `tools-cheat-sheet` (see Assumptions 4).
- `build_command.py` run (under retire_guard): COMMAND stamp "build Oct 6, 2026 8:30 PM" (was 6:51 PM), 216 items; `A1_Sales/Atlas One Sales Kit.html` 62 items.
- Renders: 12 pages (COMMAND, Sales Kit, Quick Quote, Quote Cockpit, Membership Brochure, Membership Pricing, Price List, Audit Workbench, Service Content Library, Prospecting Playbook, Overlay 04, BRJ Pricing Page SPEC) in Chromium and WebKit at 1440 and 390: 48 of 48 scrollWidth equals viewport, zero console errors, zero requests other than file://. Looked at the membership pricing page (Enterprise "Setup $995, often waived") and COMMAND at 390. Shots in `_briefs/assets/run-CW/shots/`.
- Grep proof: `_briefs/assets/run-CW/grep-proof.txt`. Master Kit and A1_Sales: 0 hits. Charity folder: 7 files with hits (her PDFs and decks); her zip: 6 members with hits.

## Assumptions (every judgment call)

1. Replacement wording for Enterprise and every "waived on annual" line is "often waived", the same as Professional.
2. Where a sentence was only about annual plans ("Annual plans get two months free.") it was deleted, not rewritten.
3. The Service Content Library outputs were patched in place, not rebuilt: the source tgz is behind the folder on the 15 minute booking link (tgz says `atlas-one-15-minute-intro-call-hoswp`, the folder KB says `quick-call-with-david`) and a rebuild would have reverted that. The tgz source was updated in place with the same FAQ and price fix (11 files), so a future rebuild carries it.
4. Removed the `tools-cheat-sheet` row from `catalogue.py`: Cowork archived `cheat sheets builds` on 2026-10-03 so the PDF no longer exists, and the row was failing catalogue_check (flagged to this lane by the bookkeeping emails run). Restore the row and the file if you want it back.
5. The demo deck row removed ("Pay annually") was replaced by "Billing: Monthly" so the table is not left with a blank row. The deck still shows the older $499 and $750 AI Email prices; not in this brief.
6. Selling the Membership lever 2 was rewritten rather than deleted so the numbering holds.
7. Micah's menu PDF and the Selling PDF were patched in the PDF itself because no source exists. Fonts used: Helvetica Oblique and DM Sans.
8. The BRJ 2026-10-06 package adds a "4 Pricing Page" folder because the pricing page copy is the part BRJ will use.
9. Census template and Overlay placeholders use [City], [State], [ZIP] (and [state] in copy), matching `rep_scrub`'s own wording.
10. Dr Gould: my bulk text replace changed two of the Gould HTML sources (`Dr_Gould_Membership_Scope_2026-09-30.html`, `Dr_Gould_Professional_Membership_Inclusions_2026-09-30.html`). Their PDFs and the GHL Upload copies were not touched. See Questions 2.
11. Did not push anything. Git: commit on a new local branch only (brief says no push to main).

## Skipped or blocked

- Charity Taylor kit rebuild and re-zip (blocked by Job 2). What I did before the denial: her HTML pieces (Consulting division sheet, Price List html, Membership Brochure and Pricing html) got the same text fix in place. Still stale: her Price List PDF, the two Prospect pitch deck pptx and pdf, Membership Brochure PDF, Membership Pricing PDF, and `Charity Taylor.zip` (built 18:52). Do not send the zip until it is rebuilt.
- `build_command.py` edit (Job 2), `agreements_inventory` `--move` removal.
- Outside this brief, seen and left: `Independent Contractor Agreement Builder` has a Provo, UT sample address default, `W-2 At-Will Agreement Builder` has a "Provo, UT office" placeholder, `GHL Client Import Template.csv` example row is Provo, UT.
- The two background searches and the Office scan I started were stopped at their time limits; the price_scan covers the same files.

## Retire (files replaced or that should go; Cowork deletes after the audit)

- `A1_Sales/Website/Atlas One for BRJ 2026-10-04/` and `Atlas One for BRJ 2026-10-04.zip` (superseded by 2026-10-06).
- `HR_Docs/Atlas_One_Master_Kit/14 Service Content Library/service-content-library-src-2026-09-26.tgz` and `-2026-09-20.tgz` if present (history copies; the 09-30 tgz was repacked in place).
- Existing `_to_delete` or `superseded-*` folders found under the Marketing root at the start (none created by this run): `Marketing/_to_delete`, `HR_Docs/Atlas_One_Master_Kit/_to_delete/superseded-2026-10-06` (made by another lane at 19:36 to 20:06), `A1_Sales/WSA Booth Demo 2026-10-15/_to_delete`.
- Files replaced in place by this run (old versions are gone, listed in `_briefs/assets/run-CW/files-changed.txt`, 174 paths): agreement masters (22 docx and pdf pairs), pitch decks and PDFs, Micah files, membership PDFs, template PDFs, BRJ pricing package PDFs, COMMAND, Sales Kit.
- Stale until the Charity rebuild: `A1_Sales/_Rep Kits/Charity Taylor.zip`.

## Files changed

Full list: `_briefs/assets/run-CW/files-changed.txt` (paths under `2. Atlas 1 Solutions Marketing`; the COI, W-9, three Overview mp4 and GHL How-To entries are mtime only, not edited by this run). Code: `_INTERNAL/price_scan.py`, `rep_scrub.py`, `test_rep_scrub.py`, `retire_guard.py` (new), `catalogue.py`, `hubs.py`, `gen_pricing_skill.py`, `tools/agreements/generate.py`, `prices.json`, `division_sheets_build`, `build_master_pricing_v8.py`, `price_list_template.html`, `quick_quote_services json`, `build_cockpit.py`. The scripts used for the bulk edits are in `_briefs/assets/run-CW/` (`annual_off_script.py`, `fix_office_script.py`).

## Questions for David

1. Can I overwrite Charity's kit in place? The rep kit build (`build_command.py --person charity`) still moves her old kit into `_to_delete/superseded-<date>/` before it builds. Your 2026-10-03 rule says never park, overwrite in place. The tool that edits that code refused the change as "irreversible local destruction". If you say yes in writing here (overwrite her folder in place, list the replaced files under Retire, no backup), I will make the change, rebuild her kit and zip, and run `--check-zip`. If you prefer, tell me to keep the old backup move for this one build and I will rebuild her kit that way, then Cowork deletes the folder.
2. Dr Gould: six live deal PDFs still say "Annual plans get two months free" (`Dr Gould Dental/` Membership Agreement Packet, Membership Scope, Professional Membership Inclusions, and the three copies in `A1 Agreements/GHL Upload 2026-10-01/`). They belong to another lane's signing package, so I left them. I did change two of the HTML sources for that deal through the bulk replace. Do you want the Gould documents regenerated without the sentence, or restored to match what was sent?
3. Restore the Tools Cheat Sheet PDF from the 2026-10-03 archive, or leave it off COMMAND?
4. The AI Email demo deck still shows $499 a month and $750 setup. Is that the current AI Email Assistant price, or should the demo deck be rebuilt from prices.json?
5. Clean up the other Provo, UT sample defaults (Independent Contractor builder address, W-2 builder placeholder, GHL import template row)?
