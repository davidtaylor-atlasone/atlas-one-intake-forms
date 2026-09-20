# RUN-AUDIT-report.md (Run A4, 2026-09-19)

Seven jobs from `BRIEF-AUDIT.md`, all built and verified by rendering. Job 5 (retire the stale
sample) was done first since it was quick; everything else follows the brief's own order.

## Job 1: payroll reader proven on xlsx and four real world register layouts
Five invented fixtures (a modern payroll journal, a legacy register with subtotals/grand total/a
footer fee, a PEO invoice with a combined Employer Taxes column and an Invoice Total row, an
accounting suite summary with sections stacked vertically, and the PEO invoice pasted as tab
separated text), csv and xlsx pairs where applicable, in
`_briefs/assets/run-A4-audit/fixtures/payroll/`.

Found and fixed three real gaps in the Audit Workbench's copy of the payroll classifier:
1. The totals-row filter only matched a row whose label started with "total", "grand total" or
   "subtotal"; an "Invoice Total" row was counted as a 21st employee. Widened to catch "total" as
   a standalone word anywhere in the label.
2. `guessCat` had no rule for a single combined "Employer Taxes" column (only recognized
   401k/benefit words after "employer"); it fell through to "unknown" and was silently dropped
   from the employer tax sum. Added a rule.
3. A fee that is one footer line for the whole run, not a per-employee column, was invisible to
   the fee scan. Added a fallback that reads a labeled admin/processing/service/PEO/delivery fee
   line below the header.

Fixes 1 and 2 are shared classifier code copied from "Payroll to GL Import Converter (Atlas
One).html"; the master had the identical fault in both spots (confirmed by reading its code) and
was fixed there too, then smoke tested (zero console errors). Also added a vertical-sections
fallback for the accounting-suite shape (bench only; the master still cannot build a journal from
that shape, a known carried-forward gap, not silently fixed) and a tab-delimited path for the
paste box. Proved the existing DecompressionStream fallback message ("This browser cannot unpack
.xlsx. Save as CSV and upload that.") by stubbing it undefined.

All nine reads now correct, zero console errors, screenshots at 1200 and 390 (scrollWidth matches
viewport). Details and expected-vs-read numbers: `runA4-payroll-fixtures.txt`.

## Job 2: the vendor tool reads what the prep email tells prospects to bring
Added xlsx reading to the Vendor & Software Audit (`AtlasXlsx`, copied verbatim from the
Workbench's own copy of the GL Converter's zip/sheet reader, not a second parser), accepted on the
file input and on drop (added a drop handler; none existed before). Added a period-summary
detector: a Vendor + Total header with no date column (the QuickBooks "Expenses by Vendor
Summary" export) now prompts for the period length in months (default 3, field hidden until that
shape is found) and divides each vendor's total across synthetic monthly transactions that flow
through the existing engine unchanged. The Ramp shape needed no new field mapping ("Merchant" was
already recognized); xlsx reading was the only real gap.

Applied identically to the master, the Spanish twin (two new UI strings translated, code
untouched) and the repo public copy (kept the "Send to Audit" / "Save my results" label
difference). Fixtures: three invented bank months, four invented card files (July duplicated to
prove cross file de duplication still removes exactly 3 duplicate rows, not 4), a QuickBooks
summary xlsx, and a Ramp export as both xlsx and csv, in
`_briefs/assets/run-A4-audit/fixtures/vendors/`.

Full round trip proven: dropped the bank and card fixtures, built the "Send to Audit" payload, fed
it straight into the Audit Workbench's `ingestVendorsPayload`, confirmed `audit.vendors.count` (7),
`software_stack` and `vendor_audit` lines both arrived, and every vendor's count stayed 3, not 4.
All three files tested in headless Chromium at 1200 and 390, zero console errors, scrollWidth
matches viewport. Details: `runA4-vendor-fixtures.txt`.

## Job 3: the pulse export hands its code and round to the bench
Stage 4 now does the full handshake: an Audit code field (`audit.code`, blank until typed) is set
from a pasted export's `pulse.code` only when it is still blank, never overwritten once typed; a
mismatch shows both codes in plain words ("Pulse code HDG2609 does not match this audit's code
TMM-2026-09") instead of picking one. `pulse.client` is shown beside the bench's own client name
with the same mismatch wording. `pulse.round` is copied straight into `audit.pulse.round` and
shown in the Stage 4 KPI row. A `"status": "waiting"` export clears score/weakest/averages/picks
so the count and "Waiting for five responses" print, never a half built score.

Added `round` to `AUDIT_SCHEMA.md`'s pulse shape and to `SAMPLE_Tell_Me_More_LLC.json`'s
`audit.pulse` (round: "Audit"). Verified in headless Chromium: blank code gets set from the
export, a typed code that disagrees shows the mismatch line, a waiting export shows "3 (waiting
for five responses)" and "not enough data", zero console errors. Confirmed `build_audit_report.py`
already prints "Staff pulse in progress" for a waiting export (tested with a throwaway copy of the
sample, deleted afterward, not committed anywhere) and still prints "Staff Pulse Score 3.7 of 5,
weakest: benefits understanding, documents" for the real sample, unchanged.
`total_impact_model.py` still reconciles the sample to $13,117 / $41,578 after the schema
addition.

## Job 4: a second full audit from blank, on Harbor Dental Group (invented, fictional)
Built Harbor Dental Group from a blank Workbench, scripted end to end in headless Chromium:
Stage 1 client name plus the exact vendor round trip payload from Job 2 (7 sources, de
duplicated); Stage 2 the Job 1 fixture (a) payroll xlsx (20 employees per the register; that
fixture carries no fee line, so `payroll_admin` stays honestly "not quoted"), PEO model, $25 per
employee per check rate, biweekly; Stage 3 two typed WC class codes (8021 dental office, 8810
clerical) and two benefit tiers, 65% employer share, no Section 125; Stage 4 the exact worked
pulse export from `pulse-questions-2026-09-18.md` (code HDG2609, 7 of 12 responses, score 3.7);
Stage 6 left on the rule (headcount 20, Professional recommended, Enterprise also worth a look).

Confirmed to the dollar across three independent reads: `total_impact_model.py` (gross $3,971,
net year one -$1,312, three-year net -$3,019), the Workbench's own `timReport` (same three
numbers, read after loading the saved JSON fresh, independent of the session that built it), and
`build_audit_report.py`'s rendered report (2 pages, `audit.code` correctly picked up as HDG2609
from the pulse paste, Staff Pulse Score line, two tier cards, zero dashes, zero vendor or PEO
names). The 2x test prints (and correctly does not pass, given this fixture's thin data: no
incumbent payroll fee and no health premium comparison typed for it). All six stages shot at 1200
and 390, zero console errors. Saved to the repo only (`_briefs/assets/run-A4-audit/harbor/`),
nothing in the Master Kit or the DEMO set. Details: `runA4-parity.txt` (covers both the sample and
Harbor).

## Job 5: retired the stale duplicate sample
`prospects/SAMPLE_Tell_Me_More_LLC.json` (a pre-audit copy from September 8) was confirmed unread
by anything: `build_tim.py`'s `sample_path` points at the Total_Impact_Model root file of the same
name, a different file, not the one in `prospects/`. Moved to
`OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-19/`.

## Job 6: the call sheet
Added a "Call sheet" button to the Workbench header, opening a full screen overlay (Escape or
Close to leave, its own Print button) with the six stages against a 30 minute call clock, each
with what to ask for, what to drop in or type, and the one sentence that moves to the next stage,
plus a close box (read the Total Impact number, walk the three fixes, "the written offer is good
for 30 days," book the 45 minute follow up). No new file; it lives inside the Workbench. Print CSS
hides everything else and fits the whole sheet on one Letter page (confirmed by rendering to PDF
and counting pages: 1). Zero console errors and zero dashes at 1200 and 390.

## Job 7: verify, COMMAND, skill, report
Re-shot all six stages with the sample loaded, plus the call sheet, at 1200 and 390: 14 checks,
all zero console errors, scrollWidth equals viewport on every one. Rebuilt the sample report html
and pdf (both the DEMO Proposal Set and `prospects/` copies); numbers unchanged ($13,117 first
year, $41,578 three year, 2 pages). Rebuilt COMMAND on the Mac: `catalogue_check.py` passed (199
entries) before the build; backed up the prior COMMAND and Sales Kit outputs to
`_to_delete/superseded-2026-09-19/command-outputs/` first; `build_command.py` wrote
"Atlas One COMMAND.html" (199 items) and "A1_Sales/Atlas One Sales Kit.html" (57 items), stamped
"Sep 19, 2026  6:54 PM" (confirmed against `date`, local Mac time); grepped the Sales Kit for the
internal tool names this run touched (Audit Workbench, build_audit_report, GL Import Converter,
Quick Quote, Cockpit), zero found. Updated `~/.claude/skills/atlas-audit/SKILL.md` (xlsx and
summary exports, the pulse code/round handshake, the call sheet, Harbor as the second test
prospect) and re-zipped it; one nested SKILL.md, clean.

## Built, paths
- Payroll classifier fixes: `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Audit_Workbench.html`
  and `06 Calculators and Tools (NEW Aug 2026)/Payroll to GL Import Converter (Atlas One).html`.
- Vendor tool xlsx/summary shape: `Atlas_One_Vendor_Software_Audit.html`,
  `Auditoria_de_Proveedores_y_Software_Espanol.html`, and the repo's `tools/vendor-audit/index.html`.
- Pulse handshake and call sheet: `Atlas_One_Audit_Workbench.html`.
- Schema: `08 ROI Quote Master Template/Total_Impact_Model/AUDIT_SCHEMA.md`,
  `SAMPLE_Tell_Me_More_LLC.json`.
- Retired: `prospects/SAMPLE_Tell_Me_More_LLC.json` moved to `_to_delete/superseded-2026-09-19/`.
- Rebuilt: `Atlas One COMMAND.html`, `A1_Sales/Atlas One Sales Kit.html`.
- Skill: `~/.claude/skills/atlas-audit/SKILL.md`, re-zipped to
  `_BUILD-LOG/skills-for-claude-app/atlas-audit.zip`.
- Repo: `_briefs/BRIEF-AUDIT-RunA4-2026-09-19.md`, all fixtures, test scripts, screenshots,
  `runA4-payroll-fixtures.txt`, `runA4-vendor-fixtures.txt`, `runA4-parity.txt`, and
  `_briefs/assets/run-A4-audit/harbor/` (Harbor's JSON, html, pdf and screenshots), all under
  `_briefs/assets/run-A4-audit/`.

## What was looked at
Every fixture read in headless Chromium and checked field by field against hand-computed expected
values (not just "it didn't crash"). Every screenshot checked for scrollWidth equal to viewport
and zero console errors, at 1200 and 390, for: Stage 2 with a payroll fixture, the vendor tool
before and after an xlsx load, Stage 4 with the pulse handshake, all six Workbench stages with the
sample loaded, the call sheet overlay, and all six Harbor stages. The Harbor report's PDF page
count was checked with a Python PDF reader, not assumed. The sample report's numbers were grepped
directly out of the rebuilt HTML, not read from a prior report's claim.

## Assumptions
1. Job 1's fixture (b) footer fee is read as one whole-run figure (`periodFee` set directly from
   the footer line's number), the same semantic the column-based fee scan already uses per pay
   period; annualized the same way. This is a flat per-run fee, not literally "per check," and is
   labeled "provider fee per check" in the KPI row the same as the column-based path; logged here
   since the wording is a small stretch for this one shape.
2. Job 1's vertical-sections fallback (the accounting-suite shape) reads headcount, gross and
   employer taxes only; it does not attempt a department or fee split, because the fixture that
   exercises it carries neither. If a real vertical export shows up with a department or fee
   section, that needs a second pass, noted as a Question below.
3. Job 4 used the Job 1 fixture (a) (20 employees) for Harbor's payroll even though the brief
   describes Harbor as "12 employees," since the brief explicitly says to drop that fixture and the
   reader's job is to read headcount from the register, never a typed guess. Both 12 and 20 land in
   the same 8-to-30 Professional bracket, so the tier outcome the brief names (Professional
   recommended, Enterprise also) is unaffected.
4. Job 2's round trip used the vendor tool's `buildAuditVendorsPayload()` function directly (the
   same function the "Send to Audit" button calls) rather than driving an actual file download and
   re-upload through the browser's download manager, since headless Chromium's download handling
   adds no verification value over calling the same function the button calls.
5. The call sheet's booking link (`https://api.leadconnectorhq.com/widget/groups/book-david`) was
   copied verbatim from the brief; not verified live (this terminal never opens the GHL browser).

## Skipped
Nothing in the seven jobs was skipped. Not attempted, and out of scope for this run: fixing the GL
Converter master's own journal-building output for the vertical-sections payroll shape (Job 1's
Assumption 2 above); a genuine 12-employee Harbor payroll fixture (Assumption 3); verifying the
call sheet's booking link resolves (Assumption 5, GHL terminal's domain).

## Questions for David
1. If a real prospect's payroll export turns out to be a vertical/transposed shape with a
   department or fee section, is reading headcount/gross/tax only (no department, no fee) good
   enough for that call, or does the vertical-sections fallback need a second pass to handle those
   too before it comes up for real?
2. The five open questions from `back-office-audit-run-design-2026-09-18.md` section 6 are still
   open; this run kept the recorded defaults and did not re-ask them.
3. Carried forward from Run A3: same three open items noted there (naming drift on the prospect
   facing COMMAND output already noted in a prior run's log, not re-litigated here).
