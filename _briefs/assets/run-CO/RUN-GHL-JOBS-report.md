# RUN-GHL-JOBS-report (GHL-JOBS Run CO, 2026-09-27)

Terminal: GHL-JOBS. Files and code only, never the GoHighLevel browser UI. Brief:
`_BUILD-LOG/BRIEF-GHL-JOBS.md`, copied to the intake forms repo at
`_briefs/BRIEF-GHL-JOBS-2026-09-27.md`. Live log: `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`.

An earlier attempt at this run stalled with no real work done (an orchestration issue caught
and corrected before anything on disk was touched or claimed done). This is the run that
actually happened, everything below is verified against files on disk.

## What was built

### Job 3: contact@ sweep, COMPLETE and verified clean

Ran `check_role_and_support_emails()` directly (the guard function Run CN added to
`catalogue_check.py`) to get past `main()`'s early exit on the one pre-existing Price List
finding, and got the real punch list: 39 hits.

Before touching anything, read the actual text around every hit to confirm it really was a
company contact line and not an operational instruction that should stay, per the brief's own
rule. All 36 support@ hits (34 of the `06 Calculators and Tools (NEW Aug 2026)/` lead magnet
tools plus the two `A1_Sales/AI Services and Assistants/` onepagers) turned out to be the
company footer line or a mailto CTA (`Atlas One Solutions · support@AtlasOneSolutions.com ·
380-225-5217`), never a "for help email support@" instruction. Batch swapped
`support@AtlasOneSolutions.com` to `contact@AtlasOneSolutions.com` (case preserved) directly in
each source file (these ARE the source pieces, not build outputs, so a direct edit is correct
per the brief).

Files changed (36):
- `06 Calculators and Tools (NEW Aug 2026)/Atlas One Business Tools (17 generators).html`
- `06 Calculators and Tools (NEW Aug 2026)/Atlas One Calculators (53 tools).html`
- `06 Calculators and Tools (NEW Aug 2026)/Auditoria_de_Proveedores_y_Software_Espanol.html`
- `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Back_Office_Self_Assessment.html`
- `06 Calculators and Tools (NEW Aug 2026)/Business Infrastructure Audit (Espanol).html`
- `06 Calculators and Tools (NEW Aug 2026)/Business Value Diagnostic (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Business Value Diagnostic (Espanol).html`
- `06 Calculators and Tools (NEW Aug 2026)/Compliance Risk Scorecard (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Cost of a Compliance Mistake (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Business Infrastructure Audit (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Retention Cost Calculator (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Vendor_Software_Audit.html`
- `06 Calculators and Tools (NEW Aug 2026)/Certified Payroll Converter (WH-347) (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Employee Benefits Options (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/COI to Workers Comp Premium Estimator (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Everything_We_Handle.html`
- `06 Calculators and Tools (NEW Aug 2026)/Health Comparison Builder (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Health Quote Census Intake (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Atlas One Savings Summary (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Independent Contractor Onboarding Packet (Bilingual).html`
- `06 Calculators and Tools (NEW Aug 2026)/Independent Contractor Agreement Builder (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Disciplinary Write-Up Notice Generator (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Employee Handbook Builder (Bilingual 50-State).html`
- `06 Calculators and Tools (NEW Aug 2026)/Employee Benefits Package & Enrollment Guide (Bilingual) (Atlas One).html`
- `Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/templates.html`
- `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Build_This_For_Me.html`
- `06 Calculators and Tools (NEW Aug 2026)/NDA Builder (Atlas One).html`
- `Atlas One — Complete Kit for BRJ/3. Comparison & Lead-Magnet Tools/PEO Comparison Tool (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Retention Cost Calculator (Espanol).html`
- `06 Calculators and Tools (NEW Aug 2026)/Safety Manual Builder (Bilingual OSHA).html`
- `06 Calculators and Tools (NEW Aug 2026)/Separation Letter Generator (Atlas One).html` (also
  fixed a `placeholder="support@AtlasOneSolutions.com"` example hint on an input field)
- `06 Calculators and Tools (NEW Aug 2026)/W-2 At-Will Employment Agreement Builder (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/W-2 Employee Onboarding Packet (Bilingual).html`
- `05 Build Specs (for BRJ)/Atlas One Website Package/Workforce Software Comparison (Atlas One).html`
- `A1_Sales/AI Services and Assistants/Atlas_One_AI_Email_Assistant_OnePager.html`
- `A1_Sales/AI Services and Assistants/Atlas_One_AI_Task_Agent_OnePager.html`

The remaining 3 hits are real exceptions, now on a documented allow list in
`_INTERNAL (do not share)/catalogue_check.py` instead of silently ignored:
- `Atlas_One_Email_Assistant_Setup_Intake.html`: "Addresses like info@, sales@ or claims@ are
  usually shared" is explanatory prose about mailbox types in general, and a separate
  `placeholder="info@yourcompany.com"` is a UI hint showing the client the format to type
  their OWN company's address, never Atlas One's info@ or sales@. Added
  `_ROLE_EMAIL_ALLOW_LIST = {"ai-email-assistant-setup-intake": {"info@", "sales@"}}`.
- `Atlas_One_Bookkeeping_Intake_Form.html`: "add bookkeeping@atlasonesolutions.com as an
  accountant user in QuickBooks Online" is the same operational invite instruction already
  allow-listed for the QuickBooks Accountant Access Guide. Changed
  `_BOOKKEEPING_EMAIL_EXCEPTION_TITLE` (single string) to
  `_BOOKKEEPING_EMAIL_EXCEPTION_TITLES` (tuple of both titles).

Also fixed the em dash the brief called out: "Contract bundle — all three" in the Quick Quote
catalogue item, changed to "Contract bundle: all three" in both
`09 Quick Quote Tool/Atlas_One_Quick_Quote.html` (the live tool) and its source
`_INTERNAL (do not share)/tools/master-pricing-v8/quick_quote_services_2026-09-12.json`. The
Service Content Library's copies of this item already used a colon from a prior run.

**Verified**: `python3 catalogue_check.py "<Master Kit>"` now ends clean except the one
pre-existing, already-documented finding (`Atlas_One_Price_List.html` carries genuine retail
numbers outside `prices.json`'s narrow price-cell scope, not a defect, not new this run).
Confirmed directly with `check_role_and_support_emails()`: 0 hits.

### Job 4: rebuild and prove, NOT run this session

Job 3's edits are source-file text swaps only (no build step touches these standalone
06-Calculators tools; they are not COMMAND-generated). COMMAND, the Sales Kit and
`--person charity` were not rebuilt this run since Job 1 and Job 2 (which the full Job 4
verification depends on) were not attempted. Rebuilding and re-proving now would only restate
Run CN's already-verified state; recommend running Job 4 for real once Job 1 and Job 2 land.

## What was NOT attempted this run, and why

**Job 1 (digital business cards)**: not started. This is a genuinely large net-new build: two
phone pages, two vCards with embedded photos, four QR codes (PNG+SVG, decode-verified) per
card, two lock screen images, two full screen "show" pages, print PDFs with bleed and crop
marks, Playwright screenshots on two device profiles, a QR placement plan document, and a
COMMAND catalogue row, times three cards (david, david-wsa, charity held). That is a multi-hour
design-and-build job in its own right, not something to rush through in the time remaining in
this run without risking exactly the "looks like a stock template" failure the brief warns
against. No `cards-draft` branch was created since no card work happened.

**Job 2 (safety quiz split and Spanish)**: not attempted this run. Adding `q_es`/`a_es` to all
24×5 quiz items in `safety-calendar.json` in plain, crew level Spanish, then regenerating 24
month pages into three separate print pages each (talk / no-answer employee quiz / supervisor
answer key) plus bilingual sign-in sheet headings and updating two Connecteam import kits, is
real bilingual content authoring across many files, not a mechanical fix. It did not fit in
this run alongside Job 3's verification work.

Both are carried forward to the next GHL-JOBS run rather than rushed or faked.

## Assumptions

1. The `support@` → `contact@` swap only touched occurrences confirmed by reading the
   surrounding text as the company footer/mailto line; none were left as a blind find-and-
   replace across the whole file (checked each of the 34 06-Calculators tools plus the 2
   onepagers individually before writing).
2. The `Separation Letter Generator`'s `placeholder="support@AtlasOneSolutions.com"` on an
   input field was treated as the same company-line pattern and swapped too, even though
   strictly it is example text for a UI hint, since leaving Atlas One's own retired address as
   the shown example would be inconsistent with every other surface.
3. `info@`/`sales@` in the Email Assistant Setup Intake and `bookkeeping@` in the Bookkeeping
   Intake Form are allow-listed rather than rewritten, because rewriting them would break
   either the intake form's own explanation of mailbox sharing or the literal QuickBooks
   accountant-invite address the client needs to type exactly as given.
4. Job 4 (rebuild and prove) was skipped rather than run against an unfinished Job 1/Job 2,
   since a "prove" pass this early would only restate Run CN's already-verified state and add
   nothing new to check.

## Skipped (carried forward)

- Job 1: digital business cards, entirely.
- Job 2: safety quiz Spanish split, entirely.
- Job 4: rebuild and prove, pending Job 1 and Job 2.

## Questions for David

1. None generated by the work actually completed this run (the contact@ sweep and the em dash
   fix were both mechanical, brief-specified fixes with no open judgment calls left).
2. Carried forward from Run CN, still open: the workers comp audit recovery percentage (25% on
   the Price List, blank in `prices.json`); whether managed Azure Virtual Desktop via Nerdio
   becomes a real Atlas One service or stays internal tooling; whether the
   `Toolbox Talks (from the Safety Library zip)` folder (confirmed the only copy of those 28
   PDFs anywhere in the Master Kit) should be renamed as Run CN's audit suggested given it is
   not actually a duplicate; and the TD SYNNEX vendors still waiting on portal access.
3. Job 1 publish step, for when digital business cards are eventually built: merge and push the
   `cards-draft` branch of `atlas-one-intake-forms` to `main`. Not applicable yet, no cards
   branch exists this run.
