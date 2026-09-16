# BRIEF for the GHL-JOBS terminal: Run BB (employment document builders: California protection built in, old pricing retired)

Terminal name: GHL-JOBS. Files and code only, headless Chromium for verification. Build end to end, no questions,
answer permission prompts yourself, log assumptions, questions at the END of the report. Back up the prior report to
`_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunBA.md`. Back up every file before editing.
Commit and push. Clients are in all 50 states. No dashes in copy.

Why: David lets clients generate W-2 at-will agreements, offer letters, 1099 agreements and NDAs from the builders.
Every output must protect Atlas One in every state, and California is the state that exposes a weak template.
Reference package (correct, current, built 2026-09-16): `2. A1 Official Docs/1. A1 Solutions prospect_Client/
2. Clients_A1/Vet AI PPG referral/2026-09-16 CA SVP Sales hire/` (offer letter, commission agreement, guide, hold
harmless with the Civil Code 1542 waiver). Use its language as the model.

## Job 1: find every builder
List every HTML builder for the W-2 at-will agreement, offer letter, 1099 contractor agreement and NDA (Master Kit
`06 Calculators and Tools`, any `Document Builders` folder, and any copy in A1_Sales or the portal repo). Report
paths and which are live in `catalogue.py`. Never edit a copy the catalogue does not point at; retire duplicates to
`_to_delete/superseded-2026-09-16/builders/`.

## Job 2: California logic in the W-2 at-will and offer letter builders
Add, keyed off a State picker that already exists (add one if it does not, all 50 states plus DC):
1. Classification toggle Exempt / Non-exempt. Exempt prints the exempt paragraph (FLSA and, for California, the
   Labor Code and Wage Orders), no overtime, salary must meet twice state minimum wage for full time in
   California; show a warning line under the field when the entered salary is below that floor (compute from a
   table of state minimum wages with the year, editable in one place at the top of the file). Non-exempt keeps
   the overtime and meal/rest break language.
2. Commission toggle. If commissions are paid, California requires a separate signed commission agreement (Labor
   Code 2751): the builder prints the reference paragraph in the offer letter AND generates the Sales Commission
   Agreement as a second document (sections: eligibility, OTE, rate and target, when earned, payment timing,
   draws and adjustments with the Atlas One defaults from the reference package, changes, separation, at-will,
   governing law, acknowledgement).
3. California PTO as earned wages (no forfeiture, payout at separation, accrual cap allowed) and paid sick leave
   kept separate and not paid out (40 hours or 5 days minimum). Final pay timing line. Labor Code 2802
   reimbursement paragraph. No non-compete clause ever for California (and print the "not enforceable" note).
4. Other states: keep the existing state handling; add the same PTO payout note for states that treat vacation as
   wages (list them in the state table with a source field), and the sick leave minimum where a state has one.
   If the state table does not exist, build it from the current builder's data and mark every row with the date.

## Job 3: protection on every output, every state
Every generated document (all four types, every state) must carry, in the footer and in an acknowledgement
block above the signatures: Atlas One Solutions is not a law firm and this is not legal advice; the client is
responsible for classification and compliance; have counsel review before use; prepared from information the
client supplied. Bundle the current Hold Harmless and Acknowledgement (the 2026-09-15 master in `A1_Sales/A1
Agreements/2026-09-15 masters/`, plus the California Civil Code 1542 waiver paragraph from the reference
package) as a final page of every generated PDF, and require a checkbox "I have read the Hold Harmless and
Acknowledgement" before the Generate button works. The protection travels with the document no matter who
generates it. Update the Hold Harmless master itself to carry the 1542 waiver as a California paragraph if it
does not already, regenerate its docx and PDF with generate.py, and note it.

## Job 4: retire the old pricing sheets and align prices
Move `A1_Sales/Atlas 1 Agreements build/Atlas_One_Employment_Documents_Pricing.pdf` and
`Atlas_One_Employment_Documents_Overview.pdf` (the Aug 25 $650 / $850 sheet) to
`_to_delete/superseded-2026-09-16/pricing/`. Grep the Master Kit and A1_Sales for "$650" and "$850" near
"offer letter" or "employment" and list any other copy. The live prices are the Quick Quote's: Agreement build
$450 per document, Agreement bundle $1,200, HR policy or document design $175; the $195/$295/$39 options doc
was never adopted. Make sure the builders' own price text (if any) says the same, and that `prices.json`
`documents` matches.

## Job 5: verify and rebuild
Headless Chromium at 1440 and 390: generate one California exempt offer letter with commissions (both documents
produced, floor warning off at $125,000 and on at $50,000), one California non-exempt, one Texas at-will, one
1099 for New York, one NDA. Check every output has the footer, the acknowledgement block and the hold harmless
page; no dashes; fonts embedded; zero console errors; no external requests. Screenshots in
`_briefs/assets/run-BB/shots/`. Retire the old builder versions, rebuild COMMAND, confirm the stamp.

## Report
Built, Verification (with the six test outputs listed), Assumptions, Skipped, Questions for David.
