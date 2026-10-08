# RUN-GHL-JOBS-report, Run CY, 2026-10-07

Run CX's report is archived at `_BUILD-LOG/RUN-GHL-JOBS-report-runCX-done-2026-10-07.md`. Brief copy: repo `_briefs/BRIEF-GHL-JOBS-2026-10-07.md`. Evidence: repo `_briefs/assets/run-CY/` (grep-proof.txt, render-results.json, render-check.mjs, blank-state-shots.mjs, shots/).

## Built
| Job | Status |
|---|---|
| 1 Bookkeeping payroll becomes "Quoted for your company" | DONE. prices.json V12, every source, generator and output listed below. Guard added to price_scan.py. Grep proof: zero retired figures in payroll context outside the two exceptions named under Skipped. |
| 2 Governing law follows the client's state | DONE for the three builders that print a governing law for the client's own parties (Independent Contractor, W-2 At-Will, NDA Builder). Atlas One's own agreements stay on Utah, list below. |
| 3 Rebuild and prove | DONE. COMMAND stamp "Oct 7, 2026 6:05 PM" (was 1:37 PM), 216 items. Sales Kit 62 items. `--person charity` rebuilt in place, zip 77 entries, `--check-zip` clean. BRJ package dated 2026-10-07. Chromium and WebKit at 1440 and 390: 8 of 8 page loads and 16 of 16 builder fills clean. catalogue_check: 25 of 26 green, the one fail is not from this run (Question 3). |

## Job 1: what changed
Source of truth
- `_INTERNAL (do not share)/tools/agreements/prices.json`: V12, changelog line "V12 2026-10-07 bookkeeping payroll quoted, David." `payroll_models.bookkeeping` now reads "Quoted for your company (headcount, pay cycle, PTO tracking and more)". Removed `bookkeeping_setup`, `bookkeeping_quarterly_filing`, `bookkeeping_new_hire`, `payroll_bookkeeping_minimum`, `payroll_year_end`. The `other_catalogue` rows for quarterly payroll filing, 1099 contractor payroll and new hire onboarding carry the same quoted text. Payroll tax account setup, GL import, certified payroll and contractor payroll administration ($5) are untouched.
- `gen_pricing_skill.py` rewritten for the quoted block, retired figures added to its RETIRED list, `SKILL-atlas-pricing-proposed.md` regenerated.
- `price_scan.py`: new rule "Bookkeeping payroll figures (retired, now Quoted for your company)". Proven to fire on each retired figure and not on workers comp class code rates, "$1 to $15" time tracking, "$15 per employee one time" time setup, GL import or ICHRA lines.

Tools edited
- `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`: payroll through bookkeeping, standalone W-2, 1099 contractor payroll, new hire onboarding and quarterly filings are `quoted` lines (a rep can still type a number). The payroll setup row and the Year end W-2 row are removed. Dead pricing code and the minimum table are removed.
- `08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html`: bookkeeping payroll joins the models that need a typed rate (blank shows "Quoted for your company"), minimums removed, new hire and quarterly filing lines carry no price, Year end W-2 line removed.
- `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Audit_Workbench.html`: embedded PRICES refreshed from V12, hint text and client price text for bookkeeping payroll now use the typed rate.
- `14 Service Content Library/`: rebuilt from `service-content-library-src-2026-09-30.tgz` (edited and repacked in place): json, csv, html, KB md and catalogue ts overwritten. The KB standing answer no longer prints the 15 minute intro calendar address (it failed the intro calendar guard).

Sales material (sources and outputs)
- Price List: `tools/master-pricing-v8/price_list_template.html`, `A1_Sales/Pricing/Atlas_One_Price_List.html` and `.pdf` (3 pages, same count).
- Division sheets: `tools/division_sheets_build_2026-09-12.py`, `tools/division_sheet_financial_template.html`; `Atlas_One_Division_Payroll_HR.html/.pdf` and `Atlas_One_Division_Financial_Services.html/.pdf` (1 page each, same count).
- Bookkeeping: `tools/bookkeeping-docs/build.py` (payroll tables are now one quoted row each), then `build.py` and `pdf.js` run. Rewrote the Marketing Sheet V8 (html and pdf, in A1_Sales and the tools copy), Services Overview, packets and invoices (see Assumption 9, a client folder deviation).
- `A1_Sales/A1_Pitch Decks Inv/Atlas One Presentation Services Deck.pdf` and `(rep safe).pdf`: no editable source. Pages 10 to 15 (the old v4.0 bookkeeping pages carrying the rates) replaced with the 7 page rebuilt Marketing Sheet. Now 21 and 18 pages. `rep_assets.py` comment updated (Cornerstone pages are now 19 to 21).
- `tools/master-pricing-v8/README.md`: note that the INTERNAL Master Pricing V8 sheet, its builder and the quick quote services json keep the old numbers as a guide.
- BRJ pricing page: no payroll figures were ever in it. Package copied to `A1_Sales/Website/Atlas One for BRJ 2026-10-07/` and `.zip` (70 files; every file with a source counterpart checked byte for byte against its current source, none stale).

## Job 2: governing law
Changed (all in `06 Calculators and Tools (NEW Aug 2026)/`)
- `Independent Contractor Agreement Builder (Atlas One).html`: "State where the work is performed (required)" picker, blank by default, all 50 states plus DC. Fills the Governing Law clause and the courts or arbitration venue. Blank prints "[State]", shows a visible warning with icon and text, and disables Print until a state is picked. Sample data now loads Texas and an Austin address.
- `W-2 At-Will Employment Agreement Builder (Atlas One).html`: same picker ("State where the employee works"), fills the Governing Law clause and the commission agreement clause. This builder has no venue clause.
- `NDA Builder (Atlas One).html`: governing law was optional with Utah preselected. The picker is now blank and required when the clause is on; it fills Governing Law and the courts location.

Left on Utah, and why (Atlas One is the Utah party)
- `_INTERNAL (do not share)/tools/agreements/generate.py` and its outputs: Master Client Services Agreement, Hold Harmless and Acknowledgement, Gould Membership Packet, the schedules.
- The Hold Harmless and Acknowledgement page the three builders append: Atlas One's own document with the user.
- `tools/bookkeeping-docs/build.py` Client Agreement Packet (Atlas One and its bookkeeping client, Utah County venue).
- `tools/build_mutual_nda_2026-09-12.py` Mutual NDA template, `tools/build_referral_partner_agreement_2026-09-12.py` Referral Partner Agreement, Book of Business Non Circumvention, the Founder Mutual NDA (docx and pdf): Atlas One is a party.
- Vendor Partner Directory note "Governing law: Utah": a vendor contract note, not a template.
- Employee Handbook Builder (50 state) and the 17 generators: no governing law clause. Their "Utah" strings are state data for the Utah option.

Not changed: Dr Gould agreement files (operator lane).

## Looked at
- `shots/`: COMMAND and Sales Kit at 1440 and 390, Price List page 1, Workforce and Financial division sheets, Services Deck page 11, Bookkeeping sheet page 3, each builder with the state blank (warning visible), and each builder filled with a non Utah state in Chromium and WebKit at 1440 and 390: Independent Contractor with Texas and with District of Columbia, W-2 with Ohio, NDA with Florida. Clause text reads, for example, "governed by ... the laws of the State of Texas" and "courts located in the State of Texas"; DC reads "the District of Columbia".
- `render-results.json`: scrollWidth equals viewport in all 24 loads (8 page loads and 16 builder fills), zero console errors, zero requests other than file, data or blob. Blank state checks: required, aria-invalid set, "[State]" in the document, Print disabled; after picking a state Print enables once the Hold Harmless box is ticked.
- Looked at the rebuilt deck page, price list and division sheet renders by eye: no overflow, page counts unchanged.

## Retire (the auditing chat deletes these; nothing was deleted or parked)
- `A1_Sales/Website/Atlas One for BRJ 2026-10-06/` (folder) and `Atlas One for BRJ 2026-10-06.zip`: replaced by the 2026-10-07 folder and zip.
- `A1_Sales/Atlas 1 Bookkeeping/Book Keeping zip V 7.0/Book Keeping V 7.0.zip`: stale V7 archive (Marketing Sheet V7 pdf and docx, INTERNAL Master Pricing V7 pdf and docx). Not edited. It is the only place outside the INTERNAL guide and Dr Gould's files that still holds the old payroll numbers. Recommend deleting it or moving it out of A1_Sales.
- Overwritten in place (old content replaced, same filenames): Price List html and pdf; Payroll HR and Financial Services division sheets html and pdf; Bookkeeping Marketing Sheet V8 html and pdf (A1_Sales and the tools copy); Services Overview html and pdf; `Atlas One Presentation Services Deck.pdf` and `(rep safe).pdf`; Service Content Library five outputs and the source tgz; Quick Quote, Quote Cockpit, Audit Workbench, three agreement builders; COMMAND and Sales Kit; every file in `_Rep Kits/Charity Taylor/` dated 2026-10-07 (45 RETIRE lines printed by the build, covering Price List, Division Sheets, One Pagers, Sales Pieces, Service Decks, Client Presentations, Decks) and `Charity Taylor.zip`.

## Assumptions
1. Quarterly payroll filing's monthly equivalent ($43.33) is part of the retired $130 filing, so it is quoted too (prices.json `other_catalogue`).
2. "Quoted for your company (headcount, pay cycle, PTO tracking and more)" is the exact PEO wording from prices.json and is used on every payroll line. 1099 contractor payroll, new hire onboarding and quarterly filing read just "Quoted" where a narrow price column would wrap.
3. Contractor payroll administration ($5 per contractor per month) was not in the retire list, so it stays.
4. Quick Quote: lines turned to the `quoted` model. The standalone "Payroll setup" row and the Year end W-2 row are removed rather than quoted, since setup and W-2s are folded into the one quoted payroll line.
5. The INTERNAL Master Pricing V8 xlsx, its builder and the quick quote services json keep the old numbers per the brief; `price_scan.py` skips those three basenames only.
6. The `Book of Business` CRM notes (historic partner records, not Atlas One prices) are excluded from the grep proof.
7. Division sheets were patched in the generated html (the Financial sheet has hand edits beyond its template) and the builder and template were edited to match.
8. The Services Deck had no source, so the bookkeeping pages are a swap, not a redraw. The deck loses the old v4.0 footer on those pages and its outline bookmarks (69 full, 54 rep safe).
9. `bookkeeping-docs/build.py` has a standing manifest that also writes two Access To Hearing PDFs (Client Agreement Packet and the October invoice) into the prospect and client folder (`1. A1 Solutions prospect_Client/3. Quotes_A1/Access To Hearing LLC (Guiden Group)/`). I ran the build before noticing that, so those two PDFs were re-rendered. Their text did not change (the payroll tables are not in them), but it is a write into a client folder that I should have caught first. Logged in the live log.
10. Governing law default: none of the three builders has a client state field (the company address is one free text line), so the picker is blank and required.
11. The Hold Harmless and Acknowledgement page appended to every builder document names Utah law. It is Atlas One's own agreement with the user, so it stays on Utah.
12. `apply_screenshare.py` was run (twice) after the SCL rebuild; its check is green on 184 files.
13. `Atlas One Tools (share with prospects).html` is not produced by the current builder (only COMMAND and the Sales Kit are), so there was nothing to rebuild.
14. Repo commits are local on the branch `ghl-jobs-run-cw`, not pushed to main, per the brief.

## Skipped
- Dr Gould files: not touched (operator lane). Two Dr Gould hits remain in the proof (Payroll Quote html and pdf, "a new hire adds $20 a paycheck"). The catalogue guard reports them as waived.
- `Book Keeping V 7.0.zip`: not edited, on the Retire list.

## Questions for David
1. The Hold Harmless and Acknowledgement page that every builder appends says "governed by the laws of the State of Utah" (California 1542 text still appears for California). I kept Utah because Atlas One is the party. If you want that page to follow the worker's state too, say so.
2. Audiology Partnership Plus and the WSA Scottsdale offer print "$150 / $175 / $200 per pay period" for the payroll tiers. That is a separate channel price, not the bookkeeping payroll rates, so I left it. Should it also become Quoted? And Dr Gould's Payroll Quote prints "$20 a paycheck" (operator lane): tell the A1 AGENT lane if that has to change.
3. `catalogue_check.py` has 1 fail that is not from this run: `GHL How-To/GHL-How-To-Admin-Guide.md` and `.html` (changed 13:45 today by the GHL lane) carry the 15 minute intro calendar address. I did not edit them. Should the GHL lane swap them to the people.json link?
4. I re-rendered two Access To Hearing PDFs in a client folder by accident (Assumption 9). Do you want that client folder removed from the bookkeeping build's manifest so a rebuild never writes there?
5. The Services Deck PDFs now have the rebuilt 7 page bookkeeping sheet in the middle and lost their bookmarks. Acceptable, or do you want the deck rebuilt from a real source?
6. Quick Quote and the Cockpit now show payroll through bookkeeping as a type in line, with no sample figure (same as PEO). Do you want a typical range shown to reps as a hint?
