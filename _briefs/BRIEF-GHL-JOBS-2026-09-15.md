# BRIEF for the GHL-JOBS terminal: Run AS (agreements and proposal masters, "one door" lines, launcher fixes)

Terminal name: GHL-JOBS. Files, code and headless Chromium only. Never the GoHighLevel browser. Read the whole
brief, build end to end, no questions, answer every permission prompt yourself, log assumptions, questions at the
END of the report. Live log `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`; report `_BUILD-LOG/RUN-GHL-JOBS-report.md`
(quoted heredoc). Back up the prior report to `_to_delete/superseded-2026-09-14/prior-reports/RUN-GHL-JOBS-report-RunAR.md`.
ONE terminal at a time on OneDrive: another process raced Run AR's audit last night. Do not fork parallel agents
that move files. /compact between jobs. Commit and push after each job.
Limits: no overwriting existing docx/pptx/xlsx (write NEW files, retire old ones with mv), no Azure, no GHL.

Master Kit: `~/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit/`
A1_Sales: `.../2. Atlas 1 Solutions Marketing/A1_Sales/`   Agreements folder: `A1_Sales/A1 Agreements/`
Spec for this run: `_BUILD-LOG/sign-and-bill-system-spec-2026-09-15.md` (read it first) and the project brief
copied at `_BUILD-LOG/agreements-and-proposal-system-brief-2026-09-11.md` if present (else the same text is
summarized in the spec).

## Job 0: launcher fixes from Run AR (small)
- `_INTERNAL (do not share)/build_command.py`: remove the "Atlas One Tools (share with prospects).html" output
  entirely (David retired it 2026-09-15: prospects use the public pages; paid builders stay behind the portal).
  Keep the catalogue `audience` field and the forbidden-term guard (run it against the COMMAND build's prospect
  and client entries so vendor names never leak into anything a client could see). Rebuild COMMAND; confirm
  the Tools file is not recreated (it already sits in `_to_delete/superseded-2026-09-14/launchers/`).
- Repo hygiene: mv `~/Projects/atlas-one-intake-forms/_briefs/assets/run-AI/cadence-emails/` (stale copies with
  the old phone) to `_briefs/assets/_stale/run-AI-cadence-emails/` and add a README there: "never paste from
  here; the source of truth is OneDrive _BUILD-LOG/cadence-emails-2026-09-13/". Grep the repo for any other
  html carrying 385-213-7177 and list them in the report.

## Job 1: the "one door" line in every client-facing email file
Write twelve one-sentence lines (no prices, no dashes, no vendor names), one per service family: benefits and
401(k); workers comp and premium reduction; general liability, E&O, cyber and bonding; bookkeeping and tax;
certified payroll; software, licenses and IT; AI Email Assistant and AI Task Agent; handbooks, safety manuals
and HR documents; vendor and software audit; COI tracking for subcontractors; payroll to QuickBooks journals;
"custom requests welcome, ask first". Voice: David's, plain, e.g. "One more thing: if a workers comp renewal or
a certificate request lands on your desk this month, send it to me first. It is what Atlas One is for."
Save the list as `cadence-emails-2026-09-13/ONE-DOOR-LINES.md`. Then add ONE line, rotating through the list in
send order, as its own paragraph just above "Thanks,<br>David" in every file in `cadence-emails-2026-09-13/`
(prospecting, books, booking, intake, confirmations, won emails; skip the three internal-* files and the two
reminders). Keep the existing footer line. Record which line went in which file in ONE-DOOR-LINES.md. Render
three at 390px, zero errors. No dashes anywhere in the new text.

## Job 2: the proposal shell and the agreement set (masters, Word + PDF, brand locked)
Build a generator in `_INTERNAL (do not share)/tools/agreements/` (python-docx + the existing pdf.js pattern
from `_INTERNAL (do not share)/tools/bookkeeping-docs/`; reuse its fonts and logo). Outputs to
`A1_Sales/A1 Agreements/2026-09-15 masters/`:
1. Master Client Services Agreement (search OneDrive first for any existing draft by that name or "MSA"; if none,
   write it: parties, services by schedule, fees and billing (monthly in advance, auto-pay or invoice net 10,
   late fee line left as a bracket for David), term and termination (30 days), confidentiality, data access,
   limitation of liability, independent contractor, vendor neutral statement, governing law Utah, signature).
2. Standalone Hold Harmless and "not legal advice" acknowledgement (one page, used for every document builder
   deliverable and the GL converter journals).
3. Schedules, one page each, with a price table pulled from a single `prices.json` (client prices only, from
   Quick Quote and the project's tier and AI prices): Bookkeeping (monthly plans, catch-up per month, advisory
   $150 per hour), Payroll to GL converter ($75 per month monthly to bi-weekly, $125 weekly, setup $250, extra
   entity or state $25 per month, included in Concierge), Certified Payroll ($125 per active job per month),
   WC Audit Recovery (contingency, percentage as a bracket [__%] for David), COI Tracking (price as bracket),
   AI Services (existing schedule, verify prices: Essentials $249, Professional $499, extra mailbox $75, setup
   $750, Task Agent $199 or $99 bundled, setup $500), Document Services (handbook, safety manual, NDA, IC and
   W-2 agreements at Quick Quote prices), Membership ($99 waived, $399 + $495, $999 + $995, $1,900 + $1,500).
4. Proposal shell: brand eyebrow, Horas title, periwinkle rule, DM Sans body, navy table headers, footer with
   380-225-5217 (380-CALL-A1S). Sections: overview, scope, what is not included, pricing table, how billing
   works, what we need from you, to accept, signature. Generate one sample proposal per schedule with a
   fictional client "Tell Me More LLC".
Every document: four colours, no dashes, "ATTORNEY REVIEW PENDING" watermark on agreements until David clears it.
Update `A1_Sales/A1 Agreements/Atlas_One_Agreements_How_They_Fit.md` with the new set. Add every new master to
`catalogue.py` (Agreements section) and rebuild COMMAND. Render every PDF's first page to PNG and look at it.

## Job 3: Quick Quote price line
In `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`, change `gl_import` from a single flat $75 to the frequency
model (monthly to bi-weekly $75, weekly $125, setup $250 one time, extra entity or state $25 per month), keeping
`editable:true`. Back up first to `_to_delete/superseded-2026-09-15/`. Render, zero errors, rebuild COMMAND.

## Report
Built (paths), Retired, Verification (PNG renders you looked at, sizes, greps), Assumptions, Skipped, Questions
for David at the end (include the bracketed values that need his number: late fee, WC contingency %, COI price).
