# BRIEF-GHL-JOBS (current run: Run CG, 2026-09-22). Four Run CF carry overs, then Health Quote Census v3.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI. No questions
mid run. No sends, no deploy beyond pushing the intake forms repo, no spending. Deleting is a move into
`_to_delete/superseded-2026-09-22/`. No dashes in anything a client or prospect reads. Log to
`_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`, finish with `_BUILD-LOG/RUN-GHL-JOBS-report.md`. There is no time
limit; commit after each job. Screenshots to `_briefs/assets/run-CG-jobs/`.

Run CF was audited PASS by Cowork (COWORK-AUDIT-run-CF-2026-09-22.md). Its four questions are answered below
as jobs. Do not re ask them.

## Job A: remove the Cornerstone scheduler from an Atlas One public page

`tools/wc-premium-check/index.html` in the repo still carries https://scheduler.zoom.us/david-taylor-qp71rc,
which is David's CORNERSTONE Zoom scheduler, on an Atlas One page. Remove it. The only booking action on that
page is the group booking link (Book 15 minutes with David). Grep every page under `tools/` and `census/` for
`scheduler.zoom.us` afterwards: zero. Commit and push.

## Job B: the Certified Payroll Schedule and the nine sample proposals

`_INTERNAL (do not share)/tools/agreements/generate.py` `schedule_cert_payroll()` reads
`PRICES["cert_payroll"]["monthly"]`, a key that no longer exists. The prices are not unknown: David decided the
five certified payroll lines on 2026-09-21 (Run CD Job 4) and they are the five sub keys now in `prices.json`
(setup, report, state_monthly, federal_weekly, done_for_you). Rewrite the schedule to print those five lines
from `prices.json` with the labels Quick Quote uses for them, then regenerate
`Atlas_One_Certified_Payroll_Schedule` and all nine `Sample_Proposal_*.pdf` into
`A1_Sales/A1 Agreements/2026-09-15 masters/`. Check each output for the new footer, zero `Lehi`, zero
385-213-7177, zero dashes. Do not invent a price: if any of the five keys is empty, print "Priced after review"
for that line and list it in the report.

## Job C: Charity's folder gets every sales piece (catalogue stays as it is)

Answer to Run CF question 1: do NOT change catalogue.py audience or inline flags. COMMAND is how David presents;
a rep's folder of finished files is the rep kit. Add Charity's own copies, through `swap_footer_person()` exactly
as Run CF did the division sheets, of: Proof Sheet, Membership Pricing, Membership Brochure, Employee Benefits
Menu, Bookkeeping Marketing Sheet V8, QuickBooks Accountant Access Guide, Services Overview, and Everything We
Handle (public footer version, `public=True`, no email). HTML and PDF, into
`A1_Sales/_Rep Kits/Charity Taylor/Sales Pieces/`. Each: `david@atlasonesolutions`=0, `Charity Taylor`=1,
385=0, dashes=0. Make `build_command.py --person <slug>` produce this whole folder set in one command so the
next rep is one command, and say the command in the report.

## Job D: the price list audience

`A1_Sales/Pricing/Atlas_One_Price_List.html` is titled client facing and retail only but catalogued internal.
Run the six term forbidden check and a grep for cost, margin and vendor names against it. If clean, set both
catalogue entries to `audience='client'`, put the standard footer on it, regenerate its PDF, rebuild COMMAND.
If anything internal is on it, leave it internal and list what you found.

Also: grep the prospect and client audience tools in the Master Kit for `david@atlasonesolutions.com` (Run CF
found 96 inside Tools zone content, for example a contact tip in the 17 generators file). A tool's contact line
is support@atlasonesolutions.com (Run CD rule). Change those literals to support@ and list each file.

# Then: Health Quote Census v3 (was queued as Run CF, then CG)

Rewritten by Cowork (chat A1 GHL Jobs) 2026-09-22 after auditing the tool on disk. Supersedes the earlier queued
census note. Do these jobs after Jobs A to D above. Files and code only, no
GoHighLevel browser, no sends, no deploy beyond pushing the repo copy. No dashes. Model: Sonnet 5.

## What the audit found

1. Master `06 Calculators and Tools (NEW Aug 2026)/Health Quote Census Intake (Atlas One).html` (Sep 14 14:26)
   and repo `census/index.html` (Sep 14 14:32) differ by exactly one line: the repo footer reads
   "380-CALL-A1S (380-225-5217)", the master reads "380-225-5217". Take the repo line, then edit the master and
   copy it to the repo so they end identical. Run CF put the public footer (footer_html public=True) on the repo page; keep it.
2. Current table columns: First name, Last / ID, Relationship, DOB or Age, Gender, Home street, City, State,
   Home ZIP, Coverage tier. The download and import are CSV only (`parseCSV`, `rowsToCSV`); there is no xlsx.
   The older eight column template (with Tobacco and Dependents) still imports. Keep that working.
3. IMPORTANT CORRECTION to the earlier note: the "Do you want more than one plan option" question is one, two or
   three plans. It is NOT a list of coverage lines and cannot drive the salary rule. The coverage lines are the
   `name="coverage"` checkboxes: Medical, Dental, Vision, Life, Disability, Accident/Ancillary. They lump STD
   with LTD and have no Hospital indemnity or Critical illness at all.

## Job 1: split the coverage checkboxes

Replace the six with: Medical, Dental, Vision, Life, Short term disability, Long term disability, Accident,
Hospital indemnity, Critical illness. Map the old values on import or reload: Disability ticks both STD and
LTD, Accident/Ancillary ticks Accident. Update every place the values are read (summary rows, the emailed or
downloaded summary, any lines.push).

## Job 2: the column list, in this order

1. Emp Seq # (required, family grouping number: an employee and all their dependents share it, next employee
   is 2). Assigned automatically and shown read only in the tool; a typed column in the template.
2. EE # (optional, the employer's own number, free text).
3. Last Name (rename "Last / ID", drop the ID wording everywhere).
4. First Name. 5. Relationship (Employee, Spouse, Child). 6. Date of birth (keep accepting age as today).
7. Gender.
8. Full address as four fields (street, city, state, ZIP) for every employee, replacing the rule that only ZIP
   was collected under ten employees. Dependent rows get "Same as employee", ticked by default, copying the
   employee's address; unticked opens the four fields.
9. Hire date (estimate if unknown).
10. Employee status: Full time (FT) or Part time (PT). Employee rows only.
11. Position / occupation, free text. Employee rows only.
12. Pay type: Hourly or Salary. Employee rows only.
13. Annual salary or hourly rate, one column labelled and validated by pay type. Optional, EXCEPT required on
    every employee row when any of Accident, Hospital indemnity, Short term disability or Long term disability
    is ticked in Job 1, with one plain sentence: "These plans pay a benefit based on earnings, so we need a pay
    figure to quote them."
Keep Coverage tier where it sits today (after ZIP) so existing files still map; state its position in the report.
Dependent rows grey out 10 to 13 and cannot hold a value.

Keep every v2 decision: relationship column, no tobacco, SSN optional, masked, never posted, dependent and
spouse expansion, the plan options question, nothing leaves the browser, the GHL 15 minute booking link.

## Job 3: the template and the import check

Same columns, same order, same wording as the tool. Keep the CSV. Add an xlsx built in the browser (SheetJS
embedded inline, no CDN, the tools must work offline) with real data validation on Relationship, Employee status
and Pay type, a first Instructions tab explaining Emp Seq # and which columns are optional, and one sample
family (employee, spouse, child, Emp Seq 1) marked SAMPLE, DELETE. On upload or paste, if the columns do not
match the current template or the older eight column one, name the missing column instead of failing silently.

## Job 4: rebuild and verify

Rebuild COMMAND (rule 12). Headless Chromium at 1440 and 390: add two families and check Emp Seq numbering,
Same as employee copying, the salary column required with each of the four income lines and optional with none,
dependent rows refusing status, position and pay type, download both templates and re upload each, import an
old eight column file. Screenshots to `_briefs/assets/run-CF-jobs/`. Commit and push the repo copy.

Settled, do not re raise: David sells long term disability and every ancillary line. No caveat wording on LTD.

Note: the old Job 0 (David's name on the public pages) moved into Run CF on 2026-09-22.
