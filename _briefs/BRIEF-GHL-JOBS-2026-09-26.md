# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CM, 2026-09-26). One price source feeding every price list, the safety training program content, the COI done for you kit, two cleanup moves.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI and never the
portal repo. No questions mid run. No sends, no deploy beyond pushing the intake forms repo, no spending.
Deleting is a move into `Master_Kit/_to_delete/superseded-2026-09-26/`. No dashes in anything a client or
prospect reads. Log to `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`, finish with `_BUILD-LOG/RUN-GHL-JOBS-report.md`.
No time limit; commit after each job. Screenshots to `_briefs/assets/run-CM-jobs/`. Name this run "GHL-JOBS Run
CM" everywhere. Run CL was audited PASS (claude/ghl-jobs-run-CL-audit-2026-09-26.md); keep every Run CL guard on.

## Job 1: one price source, every price list in lockstep (David approved 2026-09-26)

The source of truth is `_INTERNAL (do not share)/tools/agreements/prices.json` (V8). Its existing prices stay
exactly as they are: GL converter $50 a month monthly payroll, $75 semi monthly or bi weekly, $125 weekly, $25 a
month per extra entity or state, $250 setup waived Professional and up; certified payroll $300 setup, $60 per
report, $125 a month per active state monthly job, $250 a month per active federal weekly job, $400 a month done
for you; handbook custom $950, basic $299, update $250; safety manual custom $1,200, basic $299, update $300;
updates included Professional and up. Handbook and safety manual carry NO setup fee.

Add these approved lines to prices.json (client family only, no cost or margin):
- Safety training program, done for you: $295 one time to build it for the client's industry and load it
  (waived Enterprise and up), then $79 a month up to 25 employees, $129 a month for 26 to 75, larger quoted.
  Includes a new talk and quiz each month, a new hire not yet trained alert and a quarterly report to the
  owner. Included in Concierge. When the client uses Connecteam for employee self service, Connecteam's own
  license is added at Connecteam's list price.
- Safety training, do it yourself: the 12 month calendar and the talk library in the portal, included
  Professional and up.
- COI tracking, self service (the existing COI Tracker): included Professional and up.
- COI tracking, done for you: $49 a month up to 15 subs, $99 up to 50, $149 up to 100, larger quoted; $150 setup,
  waived Professional and up; included in Concierge up to 25 subs. Replaces the "[__] price pending" line.
- Inclusion lines: the 28 business generators, the write up generator and the separation letter generator are
  included from Professional up and are not sold alone; GL converter and certified payroll tools are included in
  Concierge; Enterprise includes one handbook or safety manual a year; Concierge includes both.

Then make every place a price is printed read from prices.json, or match it to the dollar, and list each one in
the report with before and after: Quick Quote (09 Quick Quote Tool), the Quote Cockpit, the client price list
(and the rep kit copy), the Bookkeeping Marketing Sheet V8 (add the GL converter and certified payroll as add
ons), the Membership Pricing sheet and Brochure (inclusion lines only if they already list inclusions), the
Employee Benefits Menu (no tool prices; check only), the Everything We Handle page and PDF (no prices; check
only), the service content library (14 Service Content Library: regenerate with build.py, it refuses retired
prices), COMMAND and the shared Sales Kit (rebuild). Grep the whole Master Kit and A1_Sales for every retired or
conflicting figure (the first work plan table's "$75/mo monthly payroll", "NOT SET", "$750", "$149 a month up to
25", "$250 setup" next to COI, and the atlas-pricing retired list) and fix or report each hit. Add a guard to
catalogue_check.py: any price string in a prospect or client piece that is not in prices.json fails the build
(allow a documented exception list for vendor retail prices such as Microsoft and QuickBooks).
Two lines are NOT approved yet and must not be printed anywhere: the GL converter run by Atlas One at $35 per
payroll run, and the GL converter plus certified payroll bundle setup of $300. Leave them out.
Portal catalogue notes and GoHighLevel products belong to other lanes: write
`_BUILD-LOG/BRIEF-PORTAL-queued-tool-pricing.md` and `_BUILD-LOG/BRIEF-GHL-queued-products.md`, each with the
full table above and the path to prices.json. The portal file also points at the software catalog (A1_Sales/Website/BRJ Software Marketplace Package 2026-09-26/Atlas_One_Software_Marketplace_Catalog_v2.xlsx, Website NOW and Marketplace (Available) tabs) so the portal's Add services software list matches the website. Touch neither the portal repo nor GoHighLevel.

## Job 2: safety training program content (the only new build)

The portal already tracks employees, per topic checkmarks and supervisor sign off (portal features/safety). What
is missing is the content. Build it once as files the portal and Connecteam can both load:
- A 12 month safety calendar (one page, printable, both languages): each month 1 to 3 topics, drawn from OSHA's
  and state OSHA plans' published monthly safety topic calendars and the most cited OSHA standards; cite the
  source for the calendar on the page. Two tracks: general industry and construction.
- For each month: a toolbox talk (one page, plain words, English and Spanish), a checklist where one fits, a
  five question quiz with an answer key, and a sign in sheet. Reuse the existing Safety Library, the 28
  excavation toolbox talks and the Safety Manual Builder programs wherever a topic already exists; do not
  duplicate content.
- A machine readable index `safety-calendar.json` (month, track, topics, file names, quiz questions and answers)
  so the portal can show month folders and score a quiz later.
- A Connecteam import kit: each month as a course with its quiz in the shape Connecteam's course builder accepts
  (text, PDF attachment, quiz questions). If an import format is not documented, produce copy ready text per
  course and say so.
Location: `Master_Kit/04 Safety Library/Safety Training Program/` (create). Company line only, no person, no
dashes, no vendor names. Add one COMMAND row (Workforce and HR, audience client).

## Job 3: COI done for you kit (files only)

For the done for you COI service: a one page service schedule for the agreements folder (what Atlas One does,
what the client decides; Atlas One never holds, releases or advises on payment, the contractor alone decides
whether to release payment), and the notice texts as finished HTML email files in the cadence email style:
certificate request, 30 day expiry reminder, 7 day reminder, expired and payment on hold until a current
certificate or waiver is received, and certificate received thank you. Sender is Atlas One Solutions on behalf of
the contractor, contact@ as reply. The GHL lane loads them as templates later; note that in the queued GHL file.

## Job 4: Employee Benefits Options buttons (Run CL question 2)
The two adjacent buttons both read "Book a call". Make the first "Get my quote", pointing to
https://forms.atlasonesolutions.com/census/, and keep the second "Book a call". Master file, then rebuild.

## Job 5: two cleanup moves
- `Atlas One — Complete Kit for BRJ/0 updated kit 9.24.26/` and its 28 MB zip: an uncatalogued copy that still
  carries David's Cornerstone scheduler link and the retired Industry Starter Kits. Move the folder to
  `_to_delete/superseded-2026-09-26/brj-kit-copy-2026-09-24/`. Check catalogue.py first; stop and report if
  anything points into it.
- `_INTERNAL (do not share)/tools/bookkeeping-docs/`: the stale duplicate QuickBooks Accountant Access Guide.
  Move only that file to `_to_delete/superseded-2026-09-26/`. Leave the Cirque Lodge files where they are and
  list them in the report (client files, David decides).

## Job 6: rebuild and prove
Rebuild COMMAND, the shared Sales Kit and `--person charity`. Rerun the Run CL scanner over Charity's folder (all
zero on david@, David Taylor outside the licensed sentence, bare David, cornerstone, scheduler.zoom.us, 385 number,
dashes) and the new price guard. Headless at 1440 and 390 on the price list, Quick Quote and the safety calendar,
zero console errors, screenshots.

## Waiting on David, do not do
Job 4 of Run CL (contact@ on public pieces) is still waiting. The $35 GL per run price and the $300 bundle setup.
