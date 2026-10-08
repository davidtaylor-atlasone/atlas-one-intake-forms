# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CY, 2026-10-07): bookkeeping payroll quoted, governing law by state

Installed by A1 GHL Jobs 4 after the Run CX audit (PASS, claude/ghl-jobs-run-CX-audit-2026-10-07.md). Archive Run CX's
report first. Files and code only, never the GHL UI. No questions mid run, no sends, no spending, no deploys, no git push
to main of atlas-one-intake-forms. No dashes in anything a client, prospect or BRJ reads. Log real clock times. Finish
with RUN-GHL-JOBS-report.md. RETIRE RULE: overwrite in place, list replaced files under "Retire".

## Job 1: bookkeeping payroll becomes "Quoted for your company" (David approved 2026-10-07)
Payroll through Atlas One Bookkeeping is no longer a printed price. It reads "Quoted for your company (headcount, pay
cycle, PTO tracking and more)", exactly like PEO, ASO and HCM. Every other price stays as listed.
- prices.json: V12. Replace the bookkeeping payroll block with a quoted entry; changelog line "V12 2026-10-07
  bookkeeping payroll quoted, David." Keep the old numbers only in the INTERNAL Master Pricing sheet as a guide.
- Retire from every client, rep and BRJ piece, tool, generator and sheet: $30 / $15 / $7.50 per employee, the $100
  and $150 monthly minimums, $199 payroll setup, $130 quarterly filing, $20 new hire onboarding, $20 / $10 / $5 1099
  contractor rates, and the Run CW W-2 line ("one extra payroll run at your rate"). Includes Quick Quote, Quote
  Cockpit, Price List, bookkeeping marketing sheet, membership brochure and pricing, Service Content Library, Audit
  Workbench, agreement masters (Bookkeeping Schedule), BRJ pricing page, Sales Kit, gen_pricing_skill.py.
- Do NOT touch: payroll tax account setup ($250 per state account etc.), Payroll to GL import, certified payroll,
  any vendor sheet. Watch for false hits: $20, $130 and $199 appear in other services; only change payroll lines.
- Add the retired figures (in payroll context) to the price_scan guard.
- Dr Gould files: do not touch (operator lane).

## Job 2: governing law follows the client's state (clients are national)
The Independent Contractor Agreement Builder and the W-2 At-Will Employment Agreement Builder print "governed by the
laws of the State of Utah". Replace with a required state picker (all 50 states plus DC) that fills the Governing Law
clause and venue with the state where the worker performs the work; default to the client state field if the builder
has one, otherwise blank and required. Apply the same check to every other agreement builder and the agreement
masters (generate.py): any hard coded Utah governing law or venue becomes [State] or the picker. Atlas One's OWN
agreements with its clients (MCSA, Membership Agreement, NDA where Atlas One is a party) keep Utah, since Atlas One
is the Utah party. List every file you changed and every one you left on Utah and why.

## Job 3: rebuild and prove
Rebuild COMMAND, Sales Kit, `--person charity` (overwrite in place, as Run CX did), BRJ package with today's date.
Guards green, Chromium and WebKit at 1440 and 390, zero console errors, fill each agreement builder once with a
non Utah state and screenshot the governing law clause. Grep proof of zero retired payroll figures in payroll context
across A1_Sales, the Master Kit outputs and her zip. Report and Retire list.
