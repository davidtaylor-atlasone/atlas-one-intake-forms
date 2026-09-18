# RUN A1 report: the Back Office Audit Workbench

AUDIT terminal. Files and code only; never opened the GoHighLevel browser or the portal repo.
All six jobs from `_BUILD-LOG/BRIEF-AUDIT.md` done end to end, no questions asked mid-run.

## Built

**Job 1, the audit JSON schema**
- `08 ROI Quote Master Template/Total_Impact_Model/AUDIT_SCHEMA.md`: the optional `audit` block.
- Proof it changes nothing: `_BUILD-LOG/runA1-tim-before.txt` and `runA1-tim-after.txt`, diffed
  byte identical.

**Job 2, Vendor & Software Audit hand off**
- `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Vendor_Software_Audit.html` (master),
  `Auditoria_de_Proveedores_y_Software_Espanol.html` (Spanish twin), and
  `repo:tools/vendor-audit/index.html` (public copy, button says "Save my results"): multiple
  file drop, multiple pasted statements (separated by a line of three or more dashes), cross file
  transaction dedupe (same normalized merchant, date and amount kept once), and a
  "Send to Audit" button that downloads `<Company>_audit_vendors.json` with `audit.vendors` plus
  `lines.software_stack` and `lines.vendor_audit` (memo). Nothing else on the tool changed.
- Verified: pasted two overlapping fake statements, one shared transaction was correctly dropped
  and reported; downloaded payload inspected field by field. Screenshots at 1200 and 390, before
  and after, English and Spanish, zero console errors, no horizontal scroll.

**Job 3, the Audit Workbench**
- `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Audit_Workbench.html`. Internal, one file,
  carries pricing. Left rail, six stages, Total Impact pinned in the header from Stage 1 on. Load,
  drag and drop, and paste all load the whole prospect JSON or a `_audit_vendors.json` hand off;
  Save writes the whole file back.
  - Stage 1 Vendors: drop the hand off JSON, or paste a statement directly through the same
    catalog and parser as the vendor tool (copied, not duplicated as a second UI).
  - Stage 2 Payroll: reads an xlsx or csv register, or a pasted invoice, through the Payroll to GL
    Import Converter's own column classifier, copied verbatim (source lines noted in a comment;
    the Converter itself is untouched). Produces headcount, frequency, annualized gross, employer
    taxes, provider fee, payroll by department; `lines.payroll_admin` is never written without a
    real provider fee line.
  - Stage 3 WC and benefits: typed entry, live math, the COI to WC estimator's own formula for
    subcontractor exposure, Section 125 math exactly as specified.
  - Stage 4 Pulse: the eight questions built in, manual grid plus a paste box for the future
    portal aggregate, memo lines gated on an entered rate or replacement cost.
  - Stage 5 Total Impact: `total_impact_model.py`'s `build`/`fee_row`/`three_year` ported to JS
    line for line. **Parity proven to the dollar**: `_BUILD-LOG/runA1-parity.txt`, sample $13,117
    and Big Red Jelly $1,667, both gross and net.
  - Stage 6 Offer: tier by headcount, prices read from `prices.json` by key, print button for a
    client safe view (internal boxes hidden via an `internal-only` class).
- Verified: full six stage click through with real inputs, desktop and mobile, zero console
  errors, zero horizontal scroll at 390px (found and fixed a CSS grid/flexbox mobile blowout along
  the way: an `align-items:flex-start` on the stacked mobile layout and a class name collision
  with the vendor tool's own responsive table rule). Screenshots for every stage with the sample
  loaded, both viewports, in `_briefs/assets/run-A1-audit/shots/workbench-stage*-*.png`.

**Job 4, `build_audit_report.py`**
- `08 ROI Quote Master Template/Total_Impact_Model/build_audit_report.py`, beside `build_tim.py`.
  Imports `total_impact_model.py` directly for the math (cannot drift from the model or the Total
  Impact page). Renders a two page Letter report: hero with the Total Impact number and division
  waterfall, the three fixes and what we found on page one, the offer on page two. PDF via the
  same Playwright install referenced in this repo's CLAUDE.md.
- Verified: ran against the sample ($13,117, $399/mo Professional once the audit block carried an
  offer) and against Big Red Jelly (different shape: a negative payroll_admin line, a memo line, a
  fee already netted to zero, no `audit` block at all) without error. Rasterized both pages,
  looked at them, fixed one real bug (an em dash left a stray comma with bad spacing in fix
  labels) and one page count bug (three pages instead of two) before they shipped.
  Screenshots: `_briefs/assets/run-A1-audit/shots/report-sample-page1.png` / `page2.png`.

**Job 5, sample, prep email, COMMAND, skill**
- `SAMPLE_Tell_Me_More_LLC.json` gained a full fictional `audit` block (25 employees, biweekly,
  consistent with the existing $4,200 / $7,600 / $1,900 / $3,100 / $1,600 lines). Model still
  reconciles to $13,117; the Total Impact page still loads its own sample and shows $13,117. The
  sample report was built into
  `12 DEMO Proposal Set/Atlas One — DEMO Proposal Set/Atlas_One_Back_Office_Audit_Tell_Me_More_LLC__SAMPLE__fictional_2026-09-18.html`
  and `.pdf`.
- `_BUILD-LOG/cadence-emails-2026-09-13/audit-prep.html`: same wrapper, signature and button style
  as `booking-c1.html`. Subject "What to have ready for your Back Office Audit," button
  "Upload them ahead of time" pointing at the literal token `FORM_D_URL` for the GHL terminal to
  replace. INDEX.md row added. Rendered, screenshotted, zero dashes.
- COMMAND: `catalogue.py` gained the Audit Workbench (Sell & Pitch, pinned, internal) and
  `build_audit_report.py` (internal). `catalogue_check.py` passed at 198 entries. Rebuilt both
  outputs; confirmed by grep that neither internal item appears in the prospect facing output.
- `~/.claude/skills/atlas-audit/SKILL.md` written (170 character description), zipped to
  `_BUILD-LOG/skills-for-claude-app/atlas-audit.zip`, logged in `skills-system-2026-09-17.md`.

**Job 6, verify and retire**
- All screenshots above saved to `repo:_briefs/assets/run-A1-audit/shots/`.
- Parity file: `_BUILD-LOG/runA1-parity.txt` (bench vs script, gross and net, both prospects,
  PASS).
- Nothing was retired this run. One older format was found and left alone as instructed: the
  Vendor & Software Audit tool's own Save/Load button writes `{v:1, state:{...}}`, a different
  shape from the new `_audit_vendors.json` hand off. Both are correct and coexist by design: Save
  is the tool's own working file, Send to Audit is the new one way hand off to the bench.
- Public repo: committed only `tools/vendor-audit/index.html`, the brief copy, and screenshots.
  Nothing else from the Master Kit was pushed.

## Assumptions (numbered, made without stopping to ask)

1. `prices.json` has no PEO per EE per check, PEO percent of gross, ASO or HCM specific rate. The
   Workbench's payroll model picker uses the membership tier's monthly fee as a stand in for
   those three (noted in the line's own `note` text so it is never silently wrong), and the real
   `gl_import` fee for "Bookkeeping payroll." This is a pricing gap upstream of this run, not
   something the Workbench should paper over with an invented number.
2. The effort day table in the brief does not cover `health_premium`, `hr_hours` or
   `software_resold`. Defaulted to 30 days, editable per fix.
3. Confidence defaults not given a line by line rule in the brief: 1.0 for `software_stack`,
   `vendor_audit` and `payroll_admin` (numbers a document or a computed hand off produced), 0.5 for
   `subcontractor` and `turnover` (estimates), 0.8 for everything else (David's typed entry: WC
   re-rate, benefits, health). Editable per line.
4. Pay frequency for Stage 2 is a picker David sets or confirms, not auto-detected from check
   dates: most registers do not carry a reliable per row check date column, and the brief already
   allows headcount and department to come from the data while leaving room for a human check.
5. Multi statement paste (Job 2) uses a line of three or more dashes as the separator between
   pasted statements, documented in the tool. Multi file drop needed no such convention.
6. Found a landmine in the existing `build_tim.py`: it always overwrites
   `SAMPLE_Tell_Me_More_LLC.json` from its own embedded copy, which has no `audit` block. Running
   it after adding the audit block wiped it once during this run; re-applied it and documented the
   trap in the atlas-audit skill so it does not surprise a future session.
7. Built the Workbench on the Vendor & Software Audit tool's shell (fonts, colours, header bar):
   it is itself one of the "2026-09 tools" the brief points to, and reusing a shell already proven
   at 390px avoided re-solving brand compliance from scratch.
8. Stage 4's `hr_hours` memo hour count is vendor stage hours a month x 12, plus the pulse's
   "hours a week chasing admin" average (question 5) x headcount x 52, matching the brief's
   wording as literally as the two inputs allow.
9. Noticed the COMMAND rebuild's prospect facing output is now named `Atlas One Sales Kit.html`,
   not `Atlas One Tools (share with prospects).html` as the project's own CLAUDE.md still says.
   That naming drifted in an earlier run, before this one; not changed here, just noted since it
   is easy to go looking for the wrong filename.

## Skipped
- The portal's anonymous pulse route and admin aggregate: queued for the PORTAL terminal per the
  design doc; the bench takes pulse answers typed in or pasted until it ships.
- Form D "Audit intake," the two custom fields, the prep email inside the booking workflow, and
  the offer follow up workflow: queued for the GHL terminal; this terminal never opens that
  browser.
- Did not test the Workbench's xlsx reader against a live binary .xlsx file in this run (it is a
  verbatim copy of the GL Converter's own reader, already shipped and working); tested the same
  code path with pasted CSV text instead.

## Questions for David
Starting with the five the design doc left open (`back-office-audit-run-design-2026-09-18.md`,
section 6), none of which this run needed to answer to build the Audit end to end:
1. Should the prep email go out automatically after every 30 minute booking, or only when you tag
   the contact?
2. Pulse: eight questions as drafted, or strike or add any before it goes live in the portal?
3. Keep the headcount tier rule (Essential under 10, Professional 10 to 49, Enterprise 50 to 149,
   Concierge 150 plus), or is Professional the default for everyone under 50?
4. Show the three year view on the client report, or first year only?
5. Form D uploads land on the GHL contact; fine, or should statements only ever be handled live on
   the call and in the browser tool, nothing stored?

And two that came up in the build itself:
6. Want real PEO per EE per check / PEO percent of gross / ASO / HCM prices added to
   `prices.json`, so the Workbench's payroll model picker stops standing in with the membership
   fee (Assumption 1 above)?
7. Fine with `build_tim.py` staying as is (Assumption 6), or should its embedded `SAMPLE` string
   be updated to carry the `audit` block too, so a future run of it stops needing a manual re-add?
