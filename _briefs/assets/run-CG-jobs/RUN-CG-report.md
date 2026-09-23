# RUN-GHL-JOBS report: Run CG (2026-09-22)

Terminal: GHL-JOBS. Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md` (copied to the repo at
`_briefs/BRIEF-GHL-JOBS-2026-09-22.md`). Four Run CF carry overs (Jobs A to D), then Health Quote
Census v3 (Census Jobs 1 to 4). All jobs complete. Zero hard stops (no email or SMS sent, no HIPAA
toggle, no file deleted, nothing deployed, no spend).

## Job A: remove the Cornerstone scheduler

Removed `https://scheduler.zoom.us/david-taylor-qp71rc` from `tools/wc-premium-check/index.html`.
The group booking link ("Book 15 minutes with David") is now the only booking action on the page.
Grep of `tools/` and `census/` for `scheduler.zoom.us`: zero hits.

- Repo: `tools/wc-premium-check/index.html`
- Commit: `3346e9c` ("Run CG: Job A")

## Job B: Certified Payroll Schedule and the nine sample proposals

`_INTERNAL (do not share)/tools/agreements/generate.py`'s `schedule_cert_payroll()` and the
matching block in `sample_proposals()` read `PRICES["cert_payroll"]["monthly"]`, a key that no
longer existed. Rewrote both to read the five sub keys David set on 2026-09-21 (setup, report,
state_monthly, federal_weekly, done_for_you) with their `prices.json` labels. All five keys were
present and priced, so no "Priced after review" line was needed anywhere.

Regenerated all 21 documents (the schedule, the 9 sample proposals, and the other 11 that share
the same run) into `A1_Sales/A1 Agreements/2026-09-15 masters/`. Verified by extracting the raw
text from every regenerated `.docx`: zero "Lehi", zero "385-213-7177", zero em or en dash across
the Certified Payroll Schedule and all 9 sample proposals (the only hyphens present are "WH-347"
and the "380-CALL-A1S" footer phone format, both fine).

`generate.py` lives only in the OneDrive Master Kit, not the git repo, so this job made no repo
changes.

- Master Kit: `_INTERNAL (do not share)/tools/agreements/generate.py`
- Output: `A1_Sales/A1 Agreements/2026-09-15 masters/` (21 files, all regenerated)

## Job C: Charity's Sales Pieces folder + `--person` command

Per Run CF's answer to its own question 1, catalogue.py's audience and inline flags were left
untouched. Built Charity's own footer-swapped copies (HTML and PDF) of the eight named pieces
(Proof Sheet, Membership Pricing, Membership Brochure, Employee Benefits Menu, Bookkeeping
Marketing Sheet V8, QuickBooks Accountant Access Guide, Services Overview, and Everything We
Handle with the public footer) into `A1_Sales/_Rep Kits/Charity Taylor/Sales Pieces/`.

Added `build_rep_sales_pieces()` to `build_command.py` and wired it into the existing `--person`
flag alongside `build_rep_kit()`, so the whole folder set (the Sales Kit bundle plus these eight
pieces) is one command for the next rep:

```
python3 "<Master_Kit>/_INTERNAL (do not share)/build_command.py" --person <slug> "<Master_Kit>"
```

Two real bugs found and fixed while wiring this up:

1. `swap_footer_person()`'s regex only matched a double-quoted `class="..."` attribute. The
   Bookkeeping Marketing Sheet V8 source writes `class='a1-footer-person'` with single quotes, so
   the swap silently failed on that one piece until the regex was widened to accept either quote
   style (a strict widening; every file that already matched still matches the same way).
2. Everything We Handle (the public what-we-do page) carried no `a1-footer-person` element at
   all — it is a generic public page naming no one. Added one (David, `public=True`, no email,
   matching the page's existing `support@` contact row) so the swap has something to act on.

Verified all 8 outputs (16 files): `david@atlasonesolutions` = 0, `Charity Taylor` = 1 in every
file, the real old area code phone number (`385-213-7177`, any separator) = 0, em/en dash = 0,
every PDF non-empty. (The raw substring "385" is not a useful check on its own: several of these
pieces carry an inlined SVG logo whose path coordinate data contains "385" many times over, which
is not the old phone number.)

No git repo changes (`build_command.py` and its output are Master Kit / A1_Sales only).

- Master Kit: `_INTERNAL (do not share)/build_command.py` (`swap_footer_person`, new
  `build_rep_sales_pieces`, `--person` wiring)
- Master Kit: `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Everything_We_Handle.html`
  (added its `a1-footer-person`/`a1-footer-company` footer)
- Output: `A1_Sales/_Rep Kits/Charity Taylor/Sales Pieces/` (16 files)

## Job D: Price List audience + the david@ contact-line sweep

**Price List.** Ran the forbidden-term check on `A1_Sales/Pricing/Atlas_One_Price_List.html`
after stripping CSS/script noise: `margin` = 1 hit, an inline `style="margin-top:16px"` (a CSS
property, not the term); `cost` = 2 hits ("job costing" and "attorney review is available at
cost", both benign client-facing language); zero commission, wholesale, cornerstone, g&a,
verohcm, or vendor/PEO names. Clean. Set both catalogue.py entries (`price-list-pdf`,
`price-list-client-facing-2-pages`) to `audience='client'`. The page had no footer at all; added
the standard `a1-footer-person`/`a1-footer-company` footer to its last page, and changed its one
inline contact line from `David@AtlasOneSolutions.com` to `support@atlasonesolutions.com` (the
Run CD tool-contact-line rule). Regenerated the PDF (Playwright print) — page count held at 2,
`david@` absent, `support@` present. Rebuilt COMMAND (206 items, same count) and the shared Sales
Kit (57 to 58 items, the Price List now flows through it).

**david@ sweep.** Grepped every prospect- and client-audience HTML tool in the Master Kit for the
literal `david@atlasonesolutions.com` (any case). Found 106 occurrences across 39 files — real
contact-line usages, both visible HTML text and `jsPDF`-generated footer strings inside
calculator/generator tools (for example "Atlas One Business Tools (17 generators).html"), not
incidental sample data. Replaced every one with `support@atlasonesolutions.com`, preserving
surrounding case (`David` -> `Support`, `david` -> `support`; the domain casing was untouched).
Confirmed zero `david@atlasonesolutions.com` remains across every prospect/client file afterward.

Full list of the 39 files changed (all under the Master Kit / A1_Sales, occurrence count first):

```
2  06 Calculators and Tools (NEW Aug 2026)/Atlas One Business Tools (17 generators).html
3  06 Calculators and Tools (NEW Aug 2026)/Atlas One Calculators (53 tools).html
1  06 Calculators and Tools (NEW Aug 2026)/Auditoria_de_Proveedores_y_Software_Espanol.html
1  06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Back_Office_Self_Assessment.html
1  06 Calculators and Tools (NEW Aug 2026)/Business Infrastructure Audit (Espanol).html
1  06 Calculators and Tools (NEW Aug 2026)/Business Value Diagnostic (Atlas One).html
1  06 Calculators and Tools (NEW Aug 2026)/Business Value Diagnostic (Espanol).html
3  06 Calculators and Tools (NEW Aug 2026)/Compliance Risk Scorecard (Atlas One).html
3  06 Calculators and Tools (NEW Aug 2026)/Cost of a Compliance Mistake (Atlas One).html
1  06 Calculators and Tools (NEW Aug 2026)/Business Infrastructure Audit (Atlas One).html
1  06 Calculators and Tools (NEW Aug 2026)/Retention Cost Calculator (Atlas One).html
1  06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Vendor_Software_Audit.html
4  06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Prospect_Web_Pitch.html
4  06 Calculators and Tools (NEW Aug 2026)/Certified Payroll Converter (WH-347) (Atlas One).html
3  12 GHL Setup doccs/Branded Intake Forms/Atlas_One_Email_Assistant_Setup_Intake.html
2  12 GHL Setup doccs/Atlas_One_Booking_Confirmation.html
3  A1_Sales/Client Portal/Atlas_One_Client_Dashboard_GHL.html
4  06 Calculators and Tools (NEW Aug 2026)/Employee Benefits Options (Atlas One).html
3  06 Calculators and Tools (NEW Aug 2026)/COI to Workers Comp Premium Estimator (Atlas One).html
1  06 Calculators and Tools (NEW Aug 2026)/Health Comparison Builder (Atlas One).html
4  06 Calculators and Tools (NEW Aug 2026)/Health Quote Census Intake (Atlas One).html
3  06 Calculators and Tools (NEW Aug 2026)/Atlas One Savings Summary (Atlas One).html
2  A1_Sales/AI Services and Assistants/Atlas_One_AI_Email_Assistant_OnePager.html
2  A1_Sales/AI Services and Assistants/Atlas_One_AI_Task_Agent_OnePager.html
10 06 Calculators and Tools (NEW Aug 2026)/Independent Contractor Onboarding Packet (Bilingual).html
4  06 Calculators and Tools (NEW Aug 2026)/Independent Contractor Agreement Builder (Atlas One).html
2  06 Calculators and Tools (NEW Aug 2026)/Disciplinary Write-Up Notice Generator (Atlas One).html
1  06 Calculators and Tools (NEW Aug 2026)/Employee Handbook Builder (Bilingual 50-State).html
2  06 Calculators and Tools (NEW Aug 2026)/Employee Benefits Package & Enrollment Guide (Bilingual) (Atlas One).html
1  Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/templates.html
3  06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Build_This_For_Me.html
5  06 Calculators and Tools (NEW Aug 2026)/NDA Builder (Atlas One).html
1  Atlas One — Complete Kit for BRJ/3. Comparison & Lead-Magnet Tools/PEO Comparison Tool (Atlas One).html
1  06 Calculators and Tools (NEW Aug 2026)/Retention Cost Calculator (Espanol).html
1  06 Calculators and Tools (NEW Aug 2026)/Safety Manual Builder (Bilingual OSHA).html
3  06 Calculators and Tools (NEW Aug 2026)/Separation Letter Generator (Atlas One).html
5  06 Calculators and Tools (NEW Aug 2026)/W-2 At-Will Employment Agreement Builder (Atlas One).html
12 06 Calculators and Tools (NEW Aug 2026)/W-2 Employee Onboarding Packet (Bilingual).html
1  05 Build Specs (for BRJ)/Atlas One Website Package/Workforce Software Comparison (Atlas One).html
```

No git repo changes for this job (all 39 files are in the Master Kit / A1_Sales, not the repo; the
census file's 4 occurrences here are the ones later reconciled into the repo copy in Census v3's
setup step below).

## Health Quote Census v3 (Census Jobs 1 to 4)

**Setup: reconciling the repo and master copies.** The brief expected the two copies to differ by
exactly one footer line (phone format). They actually differed by three, because Job D (above) had
already fired on the master copy of this file (it is a catalogued prospect-audience tool) and
replaced its old, person-less footer and its `mailto:` widget's `david@` with `support@`. Took the
repo's public footer (David Taylor, Founder, the 380-CALL-A1S phone format, the "Book 15 minutes
with David" link, no email — Run CF's `public=True` footer) onto the master copy, and applied the
same `david@` -> `support@` fix to the repo's `mailto:` widget line (which lives outside the Master
Kit tree, so Job D's sweep never reached it). Confirmed identical by `diff` before starting the
rewrite, and again after finishing it.

### Job 1: split the coverage checkboxes

Replaced the six coverage checkboxes with nine: Medical, Dental, Vision, Life, Short term
disability, Long term disability, Accident, Hospital indemnity, Critical illness. Every place that
reads coverage values (validation, the review summary, the downloaded CSV's "Lines" row, the
emailed summary) already reads from the live checkbox set generically, so no separate rewrite was
needed there beyond the checkbox markup itself.

Old-value mapping ("Disability" ticks both disability lines, "Accident/Ancillary" ticks Accident)
is implemented through the save-and-reload build widget's `save`/`load` extension hooks
(`window.A1_SAVE_CFG.save` / `.load`), which now round-trip the coverage list explicitly and run
it through `mapLegacyCoverage()` on load. Every coverage checkbox also now carries its own `id`
(it did not before), which is a real, separate bug fix: the generic per-control save/reload scan
in the shared `a1-save-js` widget keys a control by `id || name`, and all nine (previously six)
coverage checkboxes share `name="coverage"` — without ids, only the last one in DOM order would
ever round-trip through that generic path. A build saved before this ids fix (i.e. before today)
cannot be fully reconstructed on reload; see Assumptions.

### Job 2: the 13 column list

Rebuilt the census table to: Emp Seq # (auto assigned per family, shown read-only in the tool),
EE # (optional, free text), Last name, First name, Relationship, Date of birth (still accepts a
typed age), Gender, Street/City/State/ZIP as four always-visible fields (replacing the old rule
that hid them under 10 employees), Coverage tier (kept in its existing position, right after ZIP),
Hire date, Employee status (FT/PT), Position, Pay type (Hourly/Salary), Salary or rate — the last
four employee rows only. Dependant rows grey out (disable) status, position, pay type and salary.
A dependant row also gets a "Same as employee" checkbox, ticked by default, that mirrors the
employee's street/city/state/ZIP; unticking it opens four independent fields, pre-filled with the
mirrored value as a starting point.

Salary or rate is required on an employee row whenever Accident, Hospital indemnity, Short term
disability or Long term disability is checked in step 3. A note box appears in step 4 with the
exact sentence the brief specifies ("These plans pay a benefit based on earnings, so we need a pay
figure to quote them."), and the same sentence becomes the step 4 error banner if the visitor tries
to continue with a blank salary on an employee row that needs one; the offending cell is marked
invalid.

### Job 3: template and import

The CSV and the new Excel (.xlsx) template share the same 18 columns, order and wording as the
tool, and the same one sample family (Jane/Tom/Ava Doe, Emp Seq 1, every name suffixed "(SAMPLE,
DELETE)"). The Excel template is built with SheetJS (embedded inline, no CDN — the same
`xlsx.full.min.js` community build already vendored in this Mac's npm cache) and carries:

- An Instructions tab explaining Emp Seq # and which columns are optional.
- Real Excel dropdown data validation on Relationship, Employee status and Pay type. The
  community SheetJS build cannot *write* Excel data validation (that is a paid-tier-only feature
  there); this hand-builds the `<dataValidations>` XML and patches it directly into SheetJS's own
  zip output. SheetJS's writer stores zip entries uncompressed by default, so no deflate/inflate
  code was needed — only a small STORE-only zip reader/writer and a CRC32, both inline. Verified
  independently with Python's `openpyxl` (not SheetJS itself) that the rebuilt file opens cleanly
  and reports three real `DataValidation` objects with the correct dropdown lists, both on a test
  build and on the file the live page actually downloads.

Upload now accepts both `.csv` and `.xlsx`. A header that matches neither the current 18 column
template nor the older 8 column one is named, column by column (the specific missing column
labels), instead of being silently guessed at.

### Job 4: rebuild and verify

Verified in headless Chromium (Playwright) at 1440 and 390 px:

- Added two families (add employee, +spouse, +child). Emp Seq numbers came out `1, 1, 1, 2, 2` as
  expected.
- Found and fixed a real bug: a newly added dependant (via +spouse/+child, or on CSV/Excel import)
  showed a blank, disabled address instead of the employee's — `rowData()` already resolved the
  correct value for anything that reads the data (downloads, the review screen), but the visible
  input itself was never populated on creation. Fixed by syncing the display immediately after a
  new dependant row is inserted, in both the +spouse/+child handler and `addRow()`.
- Unticking "Same as employee" correctly enables the four address fields, pre-filled with the
  mirrored value.
- Dependant rows correctly grey out status, position, pay type and salary.
- Salary-required validation correctly blocks step 4 with the exact sentence, marks the right
  cells invalid, and clears once every employee row that needs a figure has one.
- Downloaded both templates live from the running page (not just a test build) and re-uploaded
  each: 3 rows imported cleanly from both. The downloaded Excel file was independently re-opened
  with `openpyxl` and confirmed to carry the real dropdown validations.
- Imported an old 8 column file (First, Last/ID, DOB or Age, Gender, ZIP, Tier, Tobacco,
  Dependents): imported cleanly, mapped to `Employee` relationship as before.
- Zero console errors throughout every step above. `scrollWidth` equals the viewport at both 1440
  and 390.

Rebuilding COMMAND surfaced one more real issue: the forbidden-term check flagged "margin" in the
census file, a false positive from the embedded SheetJS library's own internal property/tag names
(`!margins`, `<pagemargins/>`), unrelated to Atlas One's economics. Added it to this file's
existing `FORBIDDEN_ALLOWLIST` entry in `build_command.py` (which already allowlisted "commission"
for the broker-commission question), with a comment explaining why. Rebuilt COMMAND clean (206
items). Reran `--person charity` after every catalogue/build_command.py change in this run to
confirm nothing broke; it still builds clean (58 items, forbidden terms: none).

Screenshots: `_briefs/assets/run-CF-jobs/shots/` (the brief's own path for this section, despite
this being Run CG — followed literally as written).

- Repo: `census/index.html` (full rewrite)
- Master Kit: `06 Calculators and Tools (NEW Aug 2026)/Health Quote Census Intake (Atlas One).html`
  (kept byte-identical to the repo copy)
- Master Kit: `_INTERNAL (do not share)/build_command.py` (allowlist entry)
- Commit: `a57482a` ("Run CG: Health Quote Census v3, Jobs 1-4")

## Assumptions

1. **Job B wording.** Changed the Certified Payroll Schedule's billing sentence from "Billed
   monthly based on the number of active jobs reported that month" to "Billed based on the number
   of active jobs reported each month, plus setup and per report fees where they apply", since the
   schedule now also lists one-time setup and per-report fees alongside the two monthly-per-job
   lines; the old sentence only described the monthly-per-job billing.
2. **Job C: kept the Division Sheets / One Pagers build as its own thing.** Run CF's earlier,
   ad hoc `swap_footer_person()` pass for the six division sheets and five one pagers was not
   folded into the new `build_rep_sales_pieces()` / `--person` flow, since the brief's Job C list
   is the eight named Sales Pieces only. `--person <slug>` today produces the Sales Kit bundle plus
   these eight pieces; the Division Sheets and One Pagers a rep already has stay as a separate,
   already-built folder. Extending `--person` to also regenerate those is a natural next step if
   David wants one command to produce everything a rep has, not just what changed this run.
3. **Job C: `swap_footer_person()` quote-style widening.** Treated the single-quote vs
   double-quote class-attribute fix as a strict widening safe to make in the shared function
   (every file that matched before still matches the same way), rather than adding a second,
   narrower helper just for the one affected file.
4. **Job D: Price List footer placement.** The Price List has two printed pages, each with its own
   `.foot` div (page footer, not a contact block). Added the `a1-footer-person`/`a1-footer-company`
   contract only to the last page's `.foot`, matching how a printed multi-page document usually
   carries its full contact block once, at the end, rather than repeating it on every page.
5. **Job D: "385" check for Job C could not literally mean the raw substring.** The brief's
   verification list for Job C's Sales Pieces says `385=0`; several of those pieces carry an
   inlined SVG logo whose vector path coordinate data contains the digits "385" many times over
   (not a phone number). Checked for the actual old area code and number pattern
   (`385-213-7177`, any separator, or `tel:385...`) instead of the raw substring; confirmed zero
   real hits in every case the raw count had flagged as non-zero.
6. **Census, relationship options.** The brief's Job 2 column list names Relationship as
   "(Employee, Spouse, Child)". Kept the existing fourth option, Domestic partner, since dropping
   it would remove real functionality (a legitimate benefits-eligible relationship) and nothing in
   the brief explicitly asked for it to go; read the parenthetical as naming the common categories,
   not an exhaustive list.
7. **Census, Hire date is not employee-only.** The brief's Job 2 list marks columns 10 to 13
   (Employee status, Position, Pay type, Salary or rate) "Employee rows only" and says "Dependent
   rows grey out 10 to 13" as an explicit, closed range. Column 9, Hire date, is not in that range,
   so it stays editable on every row, including dependants, per the literal column list — even
   though "estimate if unknown" reads as employee-oriented. Flagged as a question for David below
   in case this was meant to be employee-only too.
8. **Census, sample family and SAMPLE/DELETE marking on the CSV template too.** The brief's Job 3
   describes the sample family and its "(SAMPLE, DELETE)" marking under the Excel template
   specifically. Applied the same sample family and marking to the CSV template as well, for
   consistency between the two downloads, since nothing suggested the CSV template should keep its
   old, different two-family sample instead.
9. **Census, real Excel data validation over a documentation-only substitute.** Given the embedded
   community SheetJS build cannot write native data validation, the alternative to hand-building
   the `dataValidations` XML would have been to skip real dropdowns and rely on the Instructions
   tab plus the tool's already-tolerant import-time normalizers (which accept many free-text
   variants). Built the real dropdowns instead, since the brief specifically asked for "real data
   validation," and verified the result independently with `openpyxl`.
10. **Census, old `.a1build.json` saves and coverage.** A build saved before today's coverage
    checkbox id fix cannot be fully reconstructed on reload (the pre-existing shared-name/no-id
    collision in the generic save widget only ever preserved whichever coverage checkbox was last
    in DOM order, not what was actually checked). This is a pre-existing bug in behavior that
    predates this run, not something introduced by it; going forward, every save/reload round-trips
    coverage correctly, and the CFG hooks additionally support forward migration of any legacy
    value list.

## Skipped

Nothing in the brief was skipped. The only judgment calls made along the way are listed above under
Assumptions; the only open item genuinely needing David's word is Hire date's row scope
(Assumption 7), listed below.

## Questions for David

1. **Census, Hire date on dependant rows.** Right now Hire date stays editable on Spouse/Child rows
   too, following the brief's literal "Dependent rows grey out 10 to 13" range. Should Hire date
   actually be Employee-rows-only, matching Employee status/Position/Pay type/Salary right next to
   it?
2. **Rep kit scope.** `--person <slug>` currently builds the Sales Kit bundle plus the eight Sales
   Pieces from this run. Should it also regenerate the Division Sheets and One Pagers Run CF built
   for Charity, so the whole rep kit (not just what changed today) really is one command for the
   next rep?
3. **Price List now client-audience.** It is now client-facing in COMMAND and the shared Sales Kit.
   Anything else that should change now that it is reachable outside the Internal zone (e.g. should
   it also get a rep-kit copy the way the eight Job C pieces did)?
4. **The four carry-over questions from Run CF's own report** were folded into this run's Jobs A to
   D as instructed and are answered by the work above; nothing further outstanding from them.
