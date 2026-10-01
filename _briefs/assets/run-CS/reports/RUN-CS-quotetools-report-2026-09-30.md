# RUN CS quotetools report (2026-09-30)

MK = Master Kit, BK = A1_Sales/Atlas 1 Bookkeeping, BD = MK/_INTERNAL (do not share)/tools/bookkeeping-docs.

## Changed
1. Bookkeeping Marketing Sheet V8: BD/build.py (sheet function) then BD/Atlas_One_Bookkeeping_Marketing_Sheet_V8.html, BK/...V8.html and .pdf (7 pages), BD copy of the PDF. Small "Starting at $300, exact price after a 15 minute look at your books"; Medium and Large "Priced after a 15 minute look"; QuickBooks $38/$85/$140/$340; payroll minimum rows ($100 monthly, $150 other cycles, greater-of sentence, standalone only); Year-end W-2s one additional payroll run at your rate; payroll tax account rows ($250 withholding, $250 unemployment, $500 both, +$50 each additional local or state account, Nevada MBT example $300, expedited +$100); "at no additional charge" removed; bill pay $750 (A/R +$250), A/P or A/R standalone $250.
2. Client Agreement Packet MASTER: BD/build.py, BD/...MASTER.html, BK/...MASTER.pdf (9 pages), docx BK/Internal Master Bookkeeping/Atlas_One_MASTER_v1.0_4_Client_Agreement_Packet.docx. All card and ACH processor fee sentences (2.9% + $0.30, 0.8% ACH, return fee) replaced by "Payment by ACH is preferred. Atlas One does not charge a processing fee." The docx never had the card sentence, so I added the new sentence after the Fees paragraph. No late fee sentence.
3. Invoice MASTER (build.py also carried the late fee and fee cells, so I fixed it): BD/Atlas_One_Invoice_MASTER.html, BK/Atlas_One_Invoice_MASTER.pdf (still 1 page). $20 late fee sentence gone, fee cells say None, due within fifteen days of invoice date.
4. Quick Quote: MK/09 Quick Quote Tool/Atlas_One_Quick_Quote.html edited directly (there is no builder; the html is the source). Professional = 3 hands on hours a month and a quarterly review; background checks, drug testing, website, hosting, blogging now Quoted; wh_setup $250 per state account (default 2 = $500) plus new wh_local $50 line (expedited +$100 in text); bk_payroll computes max(minimum, rate x EE x periods) with a 4 option cycle select (monthly, semi, bi-weekly, weekly), setup $199; new bk_w2_yearend line; new bill_pay $750 line; 1099 line text reworded so it no longer sits next to "QuickBooks". PEO/ASO/HCM already had no defaults. Re-extracted MK/_INTERNAL.../tools/master-pricing-v8/quick_quote_services_2026-09-12.json (99 to 117 rows).
5. Quote Cockpit: MK/08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html and build_cockpit.py. The $25 and 0.95% defaults were already gone (rate empty); display text is now "Quoted for your company". Added bkMonthly() greater-of logic with per cycle minimums (also mixed pay schedules), bill pay, A/R add on, local tax account, W-2 year end lines, Small/Medium/Large as "starting at $300 / priced after a look", screening sub lines now $0 (Quoted). FIX FOUND: build_cockpit.py was stale and wiped SAFE_TRAIN and COI constants from the html (page broke). I added them to the builder, so it is now safe to rerun.
6. Internal master pricing: build_master_pricing_v8.py and Atlas_One_INTERNAL_Master_Pricing_V8.xlsx regenerated (CHECK PASS, V7 49/49, Cost and Margin 41/41, Quick Quote 117/117). QuickBooks retail 85/140/340 (vendor cost formula kept on the old 75/115/275 basis, no new cost or margin added), PEO flat retail cleared, notes updated.
7. Commission tracker, Screening calculator, Accountant Access Guide: not flagged, no changed price printed, untouched.

## Retired (copied or moved)
MK/_to_delete/superseded-2026-09-30/bookkeeping-sheet/ (old sheet PDFs x2, packet PDF, packet docx, invoice PDF), .../quickquote/ (old html and json), .../cockpit/ (old html and builder), .../master-pricing/ (old generator and xlsx).

## Tests run
Quick Quote in headless Chromium: 1 EE monthly $100, 4 monthly $120, 5 semi $150, 6 semi $180, 5 weekly $162.50, 5 bi-weekly $162.50, 1 bi-weekly $150, 3 monthly $100: all pass. Cockpit same cases pass. 1440 and 390: Quick Quote and Cockpit scrollWidth equals viewport, zero console errors, zero non-file requests. Sheet, packet and invoice are Letter print layouts (scrollWidth 436/489/693 at 390, unchanged design, they are PDFs). PDF text extracted with pypdf, old prices gone. Screenshots: _briefs/assets/run-CS/shots/quotetools/ (sheet, packet, invoice, quickquote, cockpit).

## price_scan
Before (my files): 59 QuickBooks hits repo wide, of which in my files: sheet html/pdf x3 ($275), build.py, Quick Quote 1099 line, xlsx, generator, json, plus build.py late fee and card surcharge. After: 0 hits across my 16 files.

## Assumptions
1. Quick Quote and Cockpit year-end W-2 run = max(minimum, rate x EE) per run (brief says "same floor logic"); a weekly client with 1 EE therefore shows $150 for the W-2 run. Confirm.
2. Pre-existing Letter print docs are not responsive at 390 wide.
3. build.py regenerated everything it builds, but I only rendered PDFs for sheet, packet MASTER, invoice MASTER. The Access To Hearing documents are in a client folder and their PDFs were not rendered or written (their html beside build.py changed to the no fee wording, so if re-sent they should be regenerated deliberately).
4. Services Overview html/pdf in A1 What we do Overview was rewritten by build.py with identical content (pdf not re-rendered).
5. Cockpit screening sub line prices set to 0 (Quoted), losing the internal per product retail list.

## Skipped
Nothing from the brief. Did not touch Gould, price list, membership sheets, division sheets, decks, generators, agreements, V4.5 subfolder.

## Questions for David
1. W-2 year end on a weekly or semi monthly client: is one run really the full $150 floor, or per employee only?
2. The Access To Hearing packet and invoice in its client folder still carry the old card fee wording. Regenerate them?
3. Quick Quote Bookkeeping Medium/Large ranges ($1,000 to $2,000 and $2,000 to $3,000) stay inside the tool as instructed; OK to keep?
