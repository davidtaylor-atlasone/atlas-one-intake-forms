# BRIEF for the GHL-JOBS terminal: Run BD (sales banner printing on client documents, last two duplicate builders)

Terminal name: GHL-JOBS. Files and code only, headless Chromium for verification. Build end to end, no questions,
answer permission prompts yourself, log assumptions, questions at the END of the report. Back up the prior report
to `_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunBC.md` (Cowork already copied it there;
overwrite is fine). Back up every file before editing. Commit and push. Repo assets in
`_briefs/assets/run-BD-jobs/`. No dashes in copy. Clients are in all 50 states.

Answers to Run BC's questions (Cowork, 2026-09-16 17:25):
1. Keep the quiz buttons at "1 to 20" and "15 to 50". Consistent with the tier copy is right.
2. The 5 page preview PDF is fine; nobody depends on the page count. No re-render.
3. Leave the Quote Cockpit's internal dashes alone.
4. Suppress the banner in print. That is this run's Job 1, and it is bigger than the W-2 builder.

## Job 1: the sales banner prints on every client document
Cowork checked: the `<div id="atlas-cta-banner">` ("Want it done for you? ... Email David, Book a call, 380-CALL-A1S")
sits above `.topbar` in five live tools and none of them hide it in `@media print`, so a client who generates an
employee handbook, a safety manual, an offer letter, a contractor agreement or an NDA prints an Atlas One sales
banner on page 1 of the document they hand to their employee. The `.cta-banner` class rule at line 272 of the W-2
builder does not match it (it is an id, not that class). Files, all in `06 Calculators and Tools (NEW Aug 2026)/`:
- Employee Handbook Builder (Bilingual 50-State).html
- Safety Manual Builder (Bilingual OSHA).html
- W-2 At-Will Employment Agreement Builder (Atlas One).html
- Independent Contractor Agreement Builder (Atlas One).html
- NDA Builder (Atlas One).html
Fix: inside each file's existing `@media print{...}` block add `#atlas-cta-banner{display:none !important;}`.
Then grep every HTML file under `06 Calculators and Tools (NEW Aug 2026)/` and `08 ROI Quote Master Template/`
for any other element rendered above the document that has no print rule (top bars, premium badges, "Have Atlas
One build this for me" buttons, the request-a-custom-build strip, chat or booking widgets) and hide those in
print too. The printed document must contain only the document, the acknowledgement block, the signatures, the
footer disclaimer and the bundled Hold Harmless page.

## Job 2: retire the last two duplicate builders
Run BB retired the three duplicate builders under `Atlas One — Complete Kit for BRJ/10. Premium Builders (for
paywall)/`. Two more live there: `Employee Handbook Builder (Bilingual 50-State).html` and `Safety Manual Builder
(Bilingual OSHA).html`. `catalogue.py` references three other files in the Complete Kit folder (templates.html, the
Labor Law Poster Center, the PEO Comparison Tool) but nothing under `10. Premium Builders`. Confirm that with grep,
then move the two to `_to_delete/superseded-2026-09-16/builders/Complete Kit for BRJ premium builders/` next to the
other three. If anything else in the kit links to those two paths (grep the Complete Kit's own index or hub
pages), repoint the link to the live copy in `06 Calculators and Tools`.

## Job 3: verify and rebuild
For each of the five builders: open in headless Chromium, fill the minimum fields, tick the Hold Harmless gate,
print to PDF (Playwright `page.pdf` with `emulateMedia('print')`), run pdftotext on page 1 and confirm it does NOT
contain "Want it done", "Email David", "Book a call", "380-CALL" or "Request a custom" and DOES start with the
document heading. Also confirm the on screen view still shows the banner (only print hides it). Zero console
errors, no external requests, no dashes added. Screenshots and the five page-1 text dumps in
`_briefs/assets/run-BD-jobs/`. catalogue_check.py, rebuild COMMAND (the builders are inlined), confirm the stamp.

## Report
Built, Verification (five page-1 dumps quoted), Assumptions, Skipped, Questions for David.
