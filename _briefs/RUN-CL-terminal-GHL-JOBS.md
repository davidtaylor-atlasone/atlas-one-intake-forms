# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CL, 2026-09-26). Charity's kit made handable, dashes out of the tools, Industry Starter Kits retired, the tool pricing model, contact@ on public pieces.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI. No questions
mid run. No sends, no deploy beyond pushing the intake forms repo, no spending. Deleting is a move into
`Master_Kit/_to_delete/superseded-2026-09-26/`. No dashes in anything a client or prospect reads. Log to
`_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`, finish with `_BUILD-LOG/RUN-GHL-JOBS-report.md`. No time limit; commit
after each job. Screenshots to `_briefs/assets/run-CL-jobs/`. Name this run "GHL-JOBS Run CL" everywhere (the
GHL terminal already used CJ and CK).

Cowork audited Run CI on disk (COWORK-AUDIT-run-CI-2026-09-26.md). Everything Run CI claimed checks out: in
Charity's folder (43 files, 50 decoded blobs, every PDF's text) there are zero david@, zero "David Taylor"
outside the licensed agent sentence, zero "cornerstone", zero 385 number, and the licensed agent sentence sits
on exactly the six insurance files. Three things the Run CI checks did not look for keep her kit from being
handed over. They are Job 1.

## Job 1: Charity's kit, the three gaps Run CI's checks missed

### 1a. David's Cornerstone Zoom scheduler is still inside 11 tools
`scheduler.zoom.us/david-taylor-qp71rc` appears 44 times in 12 blobs of BOTH the shared Sales Kit and
Charity's Sales Kit. The "cornerstone" guard misses it because the URL never says Cornerstone, and the "David
Taylor" guard misses it because of the hyphen. Run CG removed it from the public page only. Master files that
carry it (grep them all again, this list is what Cowork found):
Atlas One Calculators (53 tools), Certified Payroll Converter (WH-347), Employee Handbook Builder (Bilingual
50-State), COI to Workers Comp Premium Estimator, Atlas One Savings Summary, W-2 At-Will Employment Agreement
Builder, NDA Builder, Independent Contractor Agreement Builder, Safety Manual Builder (Bilingual OSHA),
Employee Benefits Options, Employee Benefits Package & Enrollment Guide (Bilingual), all in
`06 Calculators and Tools (NEW Aug 2026)/`. Also check the intake forms repo copies under `tools/`.
Fix: every one becomes the Atlas One 15 minute intro call
`https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp`, button text "Book a
call". Guard: `scheduler.zoom.us` anywhere in COMMAND, the shared Sales Kit, a rep kit or a repo tools page
fails the build. Cornerstone material outside Atlas One builds keeps its own scheduler and is not touched.

### 1b. Bare "David" in the tools and sales pieces
Run CI swept "David Taylor". It did not look for "David" alone, which the reader still sees. Charity's kit
carries it in visible copy of 22 blobs and 5 sales pieces. Examples: "Email David", "Talk to David", "Book a
call with David", "Every question goes to David.", "Tell David which lines interest you", "David stays on as
the person who answers", "David or his team keeps a live file", "Call or text David at 380-CALL-A1S", "Tell
David which document you need and he builds it" (the Build request page and its Sales Kit row blurb in
catalogue.py), "Pricing depends on scope: contact David", "David will review it", "Saved. David will have
these scores".
Rule, same as Run CI's company line rule:
- Tools (anything a client or prospect runs): company voice. "Email David" becomes "Email us" (mailto
  contact@ if Job 4 is approved, otherwise support@), "Talk to David" and "Book a call with David" become
  "Book a call", sentences become "we" or "Atlas One" ("We will review it", "Every question comes to us").
- Sales pieces a person hands over (Benefits Menu, Everything We Handle, Membership Brochure, QuickBooks
  Accountant Access Guide, and any other piece you find): the name is the person's first name through a new
  swap contract, `a1-person-first`, filled from a new `first_name` field in people.json (David, Charity). In
  COMMAND and the shared Sales Kit it stays David; in Charity's kit it reads Charity. "He" and "his" next to
  it become neutral ("Tell Charity which lines interest you and who pays. You will hear back with what it
  costs").
- Internal notes in code comments that name David ("SETUP (David)", "David's preview/edit mode", "David finds
  an auto dark build hard to read"): delete the comment or make it neutral. A rep kit ships the code.
- Sample and placeholder names in forms ("David Wilcox", "David Atlas", "David: Atlas One HR"): neutral
  placeholders ("Jordan Lee", "Your name", "HR Manager").
- Employee Benefits Options: its admin hints ("David fills in", "David: type guaranteed monthly rates") become
  "Rep fills in" and "Type guaranteed monthly rates".
Guard: in a non default person's kit, `\bDavid\b` anywhere in raw text, decoded blobs or PDF text fails the
build, with exactly one allowlisted sentence, the licensed agent line.

### 1c. Dashes inside the tools
416 em and en dashes sit in the decoded blobs of the Sales Kit across 29 tools, including visible titles
("You're Booked — Atlas One", "Atlas One Solutions — Quote & Onboarding Intake", "Free HR & Business
Templates — 40 Ready-to-Use Forms") and the Labor Law Poster Center (117). David's answer to Run CI question 1:
sweep them all, visible copy and comments alike. Replace with a colon, a comma, a period or parentheses as the
sentence needs; never a hyphen used as a dash. Number ranges become "to". Do the master files, then the repo
public copies of the same tools. Guard: any em or en dash in COMMAND's prospect zones, the shared Sales Kit,
a rep kit (decoded) or its PDFs fails the build.

### 1d. Run CI questions 2 and 3, answered
- Q2, Employee Benefits Options duplicate contact after a swap: yes, fix it. Give the footer card one compact
  person line (name, title, email, phone) and drop the hardcoded email, phone and site lines below it so the
  card reads once.
- Q3, the census public footer using the public no email person line: correct, keep it (Run CF decision).

## Job 2: retire the Industry Starter Kits
David retired it. Remove the `industry-starter-kits` row from catalogue.py, move
`07 New HR and Safety Docs (NEW Aug 2026)/Industry Starter Kits.pdf` into
`_to_delete/superseded-2026-09-26/`, grep every catalogue, hub and repo page for "Industry Starter Kit" and
remove the link, rebuild COMMAND. (Cowork already retired the BRJ Complete Kit folder 7 copy and rebuilt the
BRJ website package on 2026-09-26: A1_Sales/Website/BRJ Website Update 2026-09-26/ and Atlas One for BRJ
2026-09-26.zip. Do not touch that package.)

## Job 3: the tool pricing model (WAITING FOR DAVID)
One rule for every tool, printed the same way on every price list: included in a membership tier, one time,
or monthly standalone. Source of truth `_INTERNAL (do not share)/tools/agreements/prices.json`; Quick Quote,
the client price list, the Bookkeeping Marketing Sheet V8 add ons and the rep kit price list regenerate from
it and must agree to the dollar. Prices already set stay exactly as they are (handbook $950 custom, $299
basic, $250 update; safety manual $1,200, $299 basic, $300 update; GL converter $50 monthly payroll, $75 semi
monthly or bi weekly, $125 weekly, $25 per extra entity or state, $250 setup waived Professional and up;
certified payroll $300 setup, $60 per report, $125 a month state monthly job, $250 a month federal weekly
job, $400 a month done for you).
Add these five lines:
- GL converter, Atlas One runs it and sends the files: $35 per payroll run.
- GL converter plus certified payroll bought together: one setup fee, $300, not both.
- Safety training program: $750 program build one time, then $149 a month up to 25 employees plus $4 a month
  per employee over 25 (roster, completion date and time per person, supervisor sign off, downloadable
  record). Included in Concierge.
- COI tracking for subcontractors: $49 a month up to 25 subs, $99 a month over 25, $250 setup (the COI phase 2
  proposal; replaces the "[__] price pending" placeholder).
- Inclusion lines: the 28 business generators, the write up generator and the separation letter generator
  are included from Professional up and are not sold alone; GL converter and certified payroll tools are
  included in Concierge; Enterprise includes one handbook or safety manual a year; Concierge includes both.
Also list the GL converter and certified payroll as add ons on the Bookkeeping Marketing Sheet V8.
Never print a price on a lead magnet calculator. The portal catalogue notes belong to the PORTAL lane: write
`_BUILD-LOG/BRIEF-PORTAL-queued-tool-pricing.md` with the same table for the portal chat to fold in, and do not
touch the portal repo.
If this job's heading does not say "David approved", skip it and say so in the report.

## Job 4: contact@ on public and prospect pieces (WAITING FOR DAVID)
Public and prospect facing company line: contact@atlasonesolutions.com (website pieces, one pagers, division
sheets, calculators, public tools, the company line in people.json footers for prospect material). Client
facing pieces keep support@ (portal, invoices, client documents, onboarding packets, agreements, client
confirmations). A person line keeps that person's own email. Add a guard: AR@, AP@, Info@, Sales@ and
Bookkeeping@ never appear on public or prospect material (Bookkeeping@ only on the QuickBooks Accountant Access
Guide). The template library PDFs that still print david@ in their footer move to contact@ when you regenerate
them; if regenerating the 155 or 208 PDFs is more than a script run, list them and leave it for a later run.
If this job's heading does not say "David approved", skip it and say so in the report.

## Job 5: rebuild and prove
Rebuild COMMAND, the shared Sales Kit and `--person charity`. Report per file, decoding every blob and reading
every PDF's text: david@, "David Taylor" outside the licensed agent sentence, bare "David", cornerstone,
scheduler.zoom.us, 385-213-7177, em and en dashes. All zero for Charity's folder, and zero for dashes and
scheduler.zoom.us in the shared Sales Kit. Headless at 1440 and 390 on her Sales Kit and COMMAND, zero console
errors. Click through three tools in her Sales Kit (a builder, a calculator, Employee Benefits Options) and
screenshot the footers. Deploy nothing beyond pushing the intake forms repo tools changes.

## Job 6: carry the TD SYNNEX software update through (Cowork did the source edits 2026-09-26)
Cowork already updated the masters: A1_Sales/Atlas 1 Software and Licenses/ (Software and Licenses one pager and Microsoft 365 one pager HTML and PDF, the Software Marketplace Sheet HTML and PDF, the website copy) and the catalog, now in A1_Sales/Website/BRJ Software Marketplace Package 2026-09-26/ (the 09-18 folder was renamed; catalogue.py's three paths already point at the new name). Source: _BUILD-LOG/software-catalog-src-2026-09-26.tgz. Your part: the COMMAND rebuild in Job 5 picks up the renamed paths (confirm the three catalogue rows open), and Charity's rep kit copies of the two software one pagers must carry the new lines ("email and tenant migrations, cloud storage and vulnerability scanning" and "enterprise plans (E3 and E5), Copilot Studio"). If Job 4 is approved, the sheet's CTA email and the one pagers' company line move to contact@ like every other public piece; rerun build_catalog.py from the tgz for the sheet rather than editing its HTML. Never name Pax8 or TD SYNNEX on anything client facing.

## Not in this run
LTD row (waiting on the carrier and rate). Charity's GoHighLevel signatures and calendar (GHL lane). The TD
SYNNEX product list (arrives from A1 PARTNER TD SYNNEX later). Anything in the portal repo.
