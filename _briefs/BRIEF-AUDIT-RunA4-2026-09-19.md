# BRIEF for the AUDIT terminal: Run A4 (prove the Audit on real export shapes, then a second full audit from blank)

Written by Cowork 2026-09-19 (chat "A1 AUDIT workbench"). Runs A1, A2 and A3 (2026-09-18) built the Back Office
Audit Workbench, `build_audit_report.py`, `AUDIT_SCHEMA.md`, the vendor tool hand off, the prep email and the
atlas-audit skill, all audited PASS (`_BUILD-LOG/COWORK-AUDIT-run-A1-2026-09-18.md`). Nothing from those runs is
rebuilt here. This run closes what those runs left open: the xlsx path of the payroll reader was never tested, the
vendor tool cannot read the two exports the prep email tells prospects to bring (QuickBooks and Ramp both export
xlsx), the pulse export does not hand its code to the bench, and the whole path has only ever been proven on the
hand tuned Tell Me More sample. Seven jobs, one run, no stopping.

Terminal name: AUDIT. Files and code only: the Master Kit on OneDrive and the repo `~/Projects/atlas-one-intake-forms`
(assets in `_briefs/assets/run-A4-audit/`, public vendor tool at `tools/vendor-audit/index.html`). Never the
GoHighLevel browser. Never the portal repo `~/Projects/atlas-one-portal` (the PORTAL terminal owns it and its runs are audited separately;
read nothing there, write nothing there). Build end to end, no questions, answer every permission prompt yourself,
make the reasonable call and log it under Assumptions, questions at the END of the report. Never fork, background
or delegate to a sub agent. Do only the jobs written here.

Log to `<Master_Kit>/_BUILD-LOG/TERMINAL-AUDIT-live.md` (one dated line after every step). Before writing the
report, copy the Run A3 report to `_to_delete/superseded-2026-09-19/prior-reports/RUN-AUDIT-report-RunA3.md`. Report
to `<Master_Kit>/_BUILD-LOG/RUN-AUDIT-report.md` (quoted heredoc or file tool) AND a copy in
`_briefs/assets/run-A4-audit/`. Copy this brief to `_briefs/BRIEF-AUDIT-RunA4-2026-09-19.md`. Commit and push after
each job, adding only your own paths (the repo has unrelated modified files under `_briefs/assets/run-N/`, leave
them alone, never `git add -A`); `git pull --rebase` before each commit because the GHL terminal commits to the same
repo. Hard stops: sending an email, enabling SMS, enabling GHL's HIPAA feature, deleting a file (move to
`OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-19/` instead), deploying to production, spending money.

Find the Master Kit by name: `find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null | grep -vi -e _to_delete
-e archiv`. Call it `$MK`. A1_Sales is `$MK/../../A1_Sales`. Read before building: `$MK/_BUILD-LOG/
COWORK-AUDIT-run-A1-2026-09-18.md` (all three run audits and David's rate rule), `$MK/_BUILD-LOG/
audit-decisions-2026-09-18.md`, `$MK/_BUILD-LOG/pulse-questions-2026-09-18.md` (export shape), `$MK/08 ROI Quote
Master Template/Total_Impact_Model/AUDIT_SCHEMA.md`, `total_impact_model.py`, `build_audit_report.py`,
`SAMPLE_Tell_Me_More_LLC.json`, the Audit Workbench and the Vendor & Software Audit (master and Spanish twin), and
the atlas-audit, atlas-pricing, atlas-brand, atlas-voice and atlas-ship skills in `~/.claude/skills/`.

Brand and build rules (non negotiable): four colours (#23304D, #788DE3, #FAFAF8, #DBE4ED), Horas headlines, DM
Sans body, DM Mono for numbers, fonts embedded as base64 from the existing tools (no CDN, no Google Fonts), status by
form not colour, no dashes anywhere in copy (a phone number keeps its hyphens), works offline on iPhone, iPad and
desktop (scrollWidth equals viewport at 390 px), verified by rendering in headless Chromium and looking at the
screenshots. Client facing files: no vendor or PEO brand names, no margins, no internal prices. Rates rule stands:
PEO, ASO and HCM rates are typed every time, blank on load, "needs a rate" until typed; bookkeeping payroll is the
only fixed price. All fixture data in this run is invented: no real company, person, account or amount anywhere.

## Job 1: the payroll reader proven on xlsx and on four real world register layouts
Fixtures first, in `_briefs/assets/run-A4-audit/fixtures/payroll/`, each as .xlsx AND .csv, 12 to 30 invented
employees, three departments, one pay period, with the shape of (a) a modern online payroll journal (one row per
employee, columns for gross, each employer tax, each deduction, net, department), (b) a legacy big provider
register (header block above the columns, subtotal rows per department, a grand total row, a fee line at the
bottom), (c) a PEO invoice (per employee lines plus an admin fee per check line and an employer taxes block),
(d) an accounting suite payroll summary (sections stacked vertically: Wages, Employer Taxes, Deductions, with
employee names as columns). Add (e) the same PEO invoice as pasted text.
Then drop each into Stage 2 in headless Chromium and check every output the Total Impact needs: headcount, pay
frequency, annualized gross, employer tax burden, provider fee per check and per year, payroll by department.
Fix the reader where it misreads (the classifier is the GL Converter's; fix in the bench's copy and note whether
the GL Converter master `06 Calculators.../Payroll to GL Import Converter (Atlas One).html` has the same fault, fix
it there too if so, since the master is the source). Subtotal and total rows must never count as employees. A fee
line found means `payroll_admin` is quoted from the typed rate; none found means "not quoted", never a guess.
Also: the bench's xlsx reader depends on `DecompressionStream`. Where the browser lacks it, the bench must say in
plain words "This browser cannot open .xlsx here. Save the register as CSV and drop that in." instead of failing
silently; prove the message by stubbing `DecompressionStream` to undefined in a test run. Write
`_briefs/assets/run-A4-audit/runA4-payroll-fixtures.txt`: for each fixture, expected vs read for every field.

## Job 2: the vendor tool reads what the prep email tells prospects to bring
The prep email says: three months of bank or card statements, or the QuickBooks "Expenses by Vendor Summary"
export, or the Ramp vendor export. Today the tool accepts `.csv,.txt,.tsv,.qbo,.ofx` only, and both QuickBooks and
Ramp export xlsx. Fixtures in `_briefs/assets/run-A4-audit/fixtures/vendors/`, all invented: (a) a bank checking
CSV, three monthly files (Date, Description, Amount, Balance), (b) a card CSV, three monthly files, with the middle
month duplicated across two files to prove de duplication, (c) the QuickBooks vendor summary as xlsx (title rows,
a Vendor column, a Total column, a TOTAL row, no dates), (d) a Ramp transactions export as xlsx and csv (merchant,
amount, date, cardholder, category, memo).
Build: (1) xlsx reading in the Vendor & Software Audit, reusing the bench's own zip and sheet reader (copy the
function, do not write a second parser); accept `.xlsx` in the file input and on drop; (2) the summary shape: when
a file has vendor and total columns and no dates, treat it as a period summary, ask for the period length in months
(default 3) in one small field that appears only then, and count months from that; (3) the Ramp shape, merchant
column as the description. Apply to the master, the Spanish twin and the public copy in the repo (same three files
Run A1 touched). Nothing else on the tool changes. Then the round trip: drop (a) plus (b), Send to Audit, load the
JSON into the Workbench, confirm `audit.vendors` and the two lines (`software_stack`, `vendor_audit` memo) arrive
and the month count is 3, not 4. Screenshots before and after at 1200 and 390. Write `runA4-vendor-fixtures.txt`.

## Job 3: the pulse export hands its code and round to the bench
When a portal export (`{"pulse": {...}}`, shape in `pulse-questions-2026-09-18.md`) is pasted in Stage 4: set
`audit.code` from `pulse.code` when `audit.code` is blank (never overwrite a typed one; if they differ, show
"Pulse code HDG2609 does not match this audit's code TMM-2026-09" and keep both); store `pulse.round` as
`audit.pulse.round`; show `pulse.client` beside the bench's own client name and flag a mismatch in plain words;
honour `"status": "waiting"` by printing the count and "Waiting for five responses", no score, no averages. Add
`round` to `AUDIT_SCHEMA.md` and the sample (round "Audit"). The report already prints "Staff pulse in progress"
under five responses; confirm that path with the waiting export.

## Job 4: a second full audit from blank, scripted, on an invented dental practice
Prove the whole path on something other than the hand tuned sample. Fixture prospect: Harbor Dental Group
(invented), 12 employees, Utah, biweekly, two class codes on the dec page (a dental office code and a clerical
code), a health renewal with two tiers and employer share, no Section 125, pulse export = the worked example in
`pulse-questions-2026-09-18.md` (code HDG2609, 7 responses, score 3.7). In headless Chromium, from a blank bench:
load the vendors JSON from Job 2, drop the Job 1 fixture (a), type the dec page and the benefits, type a PEO rate
of 25, paste the pulse export, read Stage 5, set Stage 6 (rule gives Professional recommended, Enterprise also),
Save the prospect JSON. Then run `total_impact_model.py` and `build_audit_report.py` on that file. Bench, script and
report must agree to the dollar on first year and three year; the 2x test must print; the report must show two
tier cards, the Staff Pulse Score line and zero dashes, vendor names or internal wording. Everything from this job
lives in `_briefs/assets/run-A4-audit/harbor/` (JSON, html, pdf, shots at 1200 and 390 for every stage and both
report pages). Nothing goes into the DEMO Proposal Set or the Master Kit: the Tell Me More sample stays the one
sample David sees. Write `runA4-parity.txt` covering both the sample and Harbor.

## Job 5: retire the stale duplicate sample
`$MK/08 ROI Quote Master Template/Total_Impact_Model/prospects/SAMPLE_Tell_Me_More_LLC.json` is a pre audit copy
from Sep 8 (Run A3 Assumption 5). Grep the Master Kit and the repo to prove nothing reads it, then move it to
`OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-19/`. If anything does read it, leave it and say so.

## Job 6: the call sheet, inside the Workbench, one page, printable
David runs the Audit live in 30 minutes and needs the sequence in front of him without opening a second file. Add a
"Call sheet" button in the Workbench header that opens a full screen overlay (and prints as one page): the six
stages with a minute budget for a 30 minute call (open 0 to 3, vendors 3 to 10, payroll 10 to 16, WC and benefits
16 to 24, pulse and the three fixes 24 to 27, offer and book the 45 minute follow up 27 to 30), for each stage
what to ask the prospect for, what to drop in or type, and the one sentence that moves to the next stage; the
close: read the Total Impact number, the three fixes, "the written offer is good for 30 days", book the 45 minute
follow up (https://api.leadconnectorhq.com/widget/groups/book-david). Plain words, no dashes, no jargon, internal
(prices may show). No new file: this stays inside the one tool.

## Job 7: verify, COMMAND, skill, report
Re-shoot all six stages with the sample loaded, plus the call sheet overlay, at 1200 and 390: zero console errors,
scrollWidth equals viewport. Rebuild the sample report html and pdf in the DEMO set and confirm nothing changed in
its numbers ($13,117 first year, $41,578 three year). Rebuild COMMAND on the Mac (catalogue_check.py first, back
up the prior outputs to `_to_delete/superseded-2026-09-19/command-outputs/`, stamp local, confirm the Sales Kit
carries no internal tool names). Update and re-zip the atlas-audit skill (xlsx and summary exports accepted, pulse
code handshake, call sheet, Harbor fixture as the test prospect). Report: built, paths, what was looked at,
assumptions, skipped, Questions for David at the end.

## Standing answers so nothing is re-asked
The five questions in `back-office-audit-run-design-2026-09-18.md` section 6 are still open and this run keeps the
defaults recorded there. Tier rule under 8 / 8 to 30 / 31 to 50 / 51 up. Included services wording is "the work,
never the premium". The 90 day re-pulse clock starts on the `client-current` tag (GHL Part 6). Pulse codes are
created by the portal, never by the bench or GHL.
