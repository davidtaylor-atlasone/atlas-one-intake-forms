# RUN V report (terminal B, files only)

Built 2026-09-12 by Claude Code, unattended, no GHL UI, no questions asked. Brief copied to `repo:_briefs/RUN-V-terminal-B.md` with a progress log; scripts and renders in `repo:_briefs/assets/run-V/`. Nothing sent, nothing deployed, nothing deleted (retired files moved to `OneDrive:_to_delete/superseded-2026-09-12/`). Run S pricing files, agreements content and BUILD-INDEX.md were not touched.

Paths are relative to `2. A1 Official Docs/2. Atlas 1 Solutions Marketing/` unless marked `repo:` (atlas-one-intake-forms, main, pushed) or `OneDrive:`.

## Job 1: deck slide 25, confirmed tiers

- Deck: `A1_Sales/A1_Pitch Decks Inv/Founder General pitch deck partners/Partner Pitch Deck General/V9 Partner Pitch Deck/Atlas_One_General_Deck_LIGHT.pptx` (43 slides), edited in place; the copy from before this edit is at `OneDrive:_to_delete/superseded-2026-09-12/partner-deck-v9-light-before-slide25/`.
- Slide 25 had three columns, so three were kept: Essential $99 (sub line "Bundled with software, setup waived"), Professional $399 ("Per company / per month, setup $495, often waived"), Enterprise $999 ("Per company / per month, setup $995, waived on annual"). The three cards were tightened by 0.2 in (feature rows 0.25 in apart instead of 0.28) and one centred line sits under them: "Concierge, your fractional COO, $1,900 a month." Sub lines went from 9 to 8 pt so they stay on one line. Nothing else moved.
- The headline "Three Tiers + À La Carte Add-Ons." now reads "Four Tiers + À La Carte Add-Ons." (a "Three Tiers" title over a fourth tier note would contradict itself).
- The two "ATLAS ONE REVENUE" boxes ($299/mo and $899/mo recurring + software margin) and the add-on prices were left as they were; see question 1.
- Looked at: slide 25 rendered through the Run U python-pptx to HTML renderer (`repo:_briefs/assets/run-V/slide-25-after.png`), and the refreshed 43 slide contact sheet beside the deck (`Atlas_One_General_Deck_LIGHT_contact-sheet.png`). Nothing clipped. The renderer is an approximation; worth one look in PowerPoint.
- The 20 slide room cut was not touched; slide 25 stays out of it.

## Job 2: mobile layout pass on the tools

- Files (in `HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/`): `Retention Cost Calculator (Atlas One).html`, `Retention Cost Calculator (Espanol).html`, `Vendor Consolidation Savings (Espanol).html`, and `Vendor Consolidation Savings (Atlas One).html` (same 520 px table, so it got the same fix). Copies from before the pass: `OneDrive:_to_delete/superseded-2026-09-12/tools-before-mobile-pass/`.
- The cause on the retention calculators was two inline `grid-template-columns:repeat(3,1fr)` styles (the revolving door inputs and its three result cards) that beat the existing 900 px media query. On the vendor tools it was the 520 px minimum width table plus a three column result grid.
- Fix, additive, one `<style id="a1mobile-2026-09-12">` block per file, no calculation code touched: under 700 px every grid goes to one column, the summary bar rows stack the label above the bar, the vendor table becomes stacked rows (header hidden, each row a bordered block with the area name, the checkbox at the right, and "Monthly cost" / "Hrs / mo managing it" labels drawn by CSS, Spanish labels on the Spanish file); on screens under 700 px or any touch screen, inputs, selects and buttons are at least 44 px tall, the disclosure summaries get 12 px of padding (44 px), and each vendor checkbox sits inside a 44 by 44 px label.
- Measured in Chromium at 390 px: `document.documentElement.scrollWidth` is 390 on all four (before: 510, 526, 443, 391). Zero elements wider than the viewport. No JavaScript errors.
- Numbers: one sample calculation (20 retention inputs; 12 vendor rows with alternating checkboxes, costs and hours, $75 rate, 60 percent) was run before and after on each file and every output string compared: byte identical on all four (`repo:_briefs/assets/run-V/sample-before-retention-en.json` / `sample-after-retention-en.json`).
- Looked at: each file at 390 px (crops in `repo:_briefs/assets/run-V/*_390_crops.png`) and 1440 px (desktop unchanged).
- Repo: the two English files copied to `repo:tools/retention-cost/index.html` and `repo:tools/vendor-consolidation/index.html` (the repo copies were the same files minus the Run U print button), pushed; `https://forms.atlasonesolutions.com/tools/retention-cost/` and `/tools/vendor-consolidation/` return 200 and serve the new block.

## Job 3: five division sheets rebuilt

- Built from `HR_Docs/Atlas_One_Master_Kit/_INTERNAL (do not share)/tools/division_sheet_financial_template.html` with the builder `.../tools/division_sheets_build_2026-09-12.py` (content and layout in one script). Each is HTML plus a one page Letter PDF printed through Chromium, named exactly as before so every link and Hub card keeps working:
  - `A1_Sales/Atlas 1 Payroll PEO/Atlas_One_Division_Payroll_HR.html/.pdf` (Workforce & HR)
  - `A1_Sales/Atlas 1 Benefits/Atlas_One_Division_Benefits_Retirement.html/.pdf`
  - `A1_Sales/Atlas 1 Risk Docs/Atlas_One_Division_Risk_Insurance.html/.pdf`
  - `A1_Sales/Atlas 1 Risk Docs/Atlas 1 Tech Operations/Atlas_One_Division_Technology_Operations.html/.pdf`
  - `A1_Sales/Atlas 1 Consulting/Atlas_One_Division_Business_Consulting.html/.pdf`
- June PDFs moved to `OneDrive:_to_delete/superseded-2026-09-12/division-sheets-june-2026/` (suffixed `_June2026`).
- Same layout as Financial Services: top bar, eyebrow, Horas headline with a periwinkle phrase, rule, lede, four "Why it is different" tiles, six "What is included" cards, fine print, platform pills with the division highlighted, David's footer. The six cards per division follow the June service lists; every price is a retail line from `A1_Sales/Pricing/Atlas_One_Price_List.html` and a card line without a price list line carries no price. No vendor or PEO brand names (the price list's own vendor names were not carried over). No dashes. Four page fit sizes (tight for Workforce, roomy for Benefits, Risk and Consulting, medium for Technology) so each page fills to within 6 to 34 px of the footer; list type is 9.5 to 10.5 pt depending on the sheet.
- Looked at: each page rendered from the HTML, then the six PDFs rasterised into one contact sheet, side by side (`A1_Sales/Atlas_One_Division_Sheets_contact-sheet_2026-09-12.png`, copy in `repo:_briefs/assets/run-V/division-sheets-contact.png`). All six PDFs are one page, 8.5 by 11 in.
- Hub: the five "Division sheet" card descriptions now say rebuilt 2026-09-12 with the card list (Hub copy from before in `OneDrive:_to_delete/superseded-2026-09-12/master-hub-before-run-V/`); paths unchanged; the Hub opens with 154 cards and no errors.
- What changed vs June, one line per sheet, for David's claims review:
  - **Workforce & HR**: Delivery model narrative rewritten from "we become your co-employer" to PEO co-employment through Atlas One's PEO partners; four models instead of three (adds payroll through Atlas One Bookkeeping); retail prices added from the price list; "W-2 and 1099 issuance no charge" and "401(k) fee covered" claims dropped; dashes removed.
  - **Benefits & Retirement**: "Atlas One brokers and administers" and "vetted, A-rated carriers" replaced by "arranges and administers through its carrier and plan partners"; "Fortune-500-caliber" dropped; retail prices added (ICHRA $20, 401(k) PEP $65, Section 125 $5, benefits admin $7, open enrollment $500, COBRA $35, ACA $8, 5500 $950); no health plan of its own stated in the fine print; dashes removed.
  - **Risk & Insurance**: "One brokerage relationship" and "Atlas One shops the market through multiple A-rated carriers" replaced by placement through Atlas One's licensed agency and carrier partners; retail prices added (WC policy review $495, premium audit review 25% of recovered, MVR $12, safety manual $1,200 / $300); "Quoted" only on the lines the price list names; dashes removed.
  - **Technology & Operations**: Six cards now IT, software marketplace and payments (merged), workforce systems, CRM and website, documents, and a new AI services card; retail prices added (helpdesk $125, security audit $2,500, compliance package $500, HCM $12, ATS $95, LMS $4, form design $95, AI assistant tiers); dashes removed.
  - **Business Consulting**: New Membership card with the confirmed tiers ($99 / $399 / $999 / $1,900 with setup fees) and the Audit Guarantee, replacing the June "Risk & Compliance Advisory" card (its continuity and SOP lines moved to People, organisation and continuity); retail prices added (formation $750, strategy $250/hr, ROI $750, treasury $750, collateral $1,200, policy design $175); dashes removed.
## Job 4: PDF export of the partner decks

- Not done. LibreOffice is not on this machine (`soffice` not found, no LibreOffice.app). PowerPoint through AppleScript was tried once with a 120 second watchdog: PowerPoint launched and took the open command, then every AppleEvent timed out (-1712), the same symptom as Run U (most likely a first run or sign in dialog). The PowerPoint process the script started was closed and the deck reopens cleanly (43 slides). No PDFs written, so the deck Hub cards were left as they are. Script kept at `repo:_briefs/assets/run-V/pptx2pdf.applescript`.

## Job 5: Portal and this report

- Portal rebuilt with the path argument: **BUILD Sep 12, 2026 4:10 PM**, 38 tools, 10.35 MB. Opened headless: title and hero chip carry the stamp, no errors; the two patched calculators are inlined with the new mobile block (checked inside the base64 payloads).
- Repo commits on main, each pushed: brief, job 1, job 2 (with the tool files), job 3, job 4, report.

## Assumptions

1. Slide 25: the setup fees in the brief are part of "the confirmed tier set", so they went into the sub line under each price; the "ATLAS ONE REVENUE" boxes are derived numbers not listed in the brief, so they were left alone.
2. Slide 25: "Three Tiers" became "Four Tiers" in the headline; no other copy changed.
3. Tools: the 44 px rule is applied under 700 px and on any coarse pointer device; desktop rendering at 1440 px is unchanged. Vendor tables became stacked rows rather than a scroll box, since the brief allowed either and stacked rows keep the checkbox reachable.
4. Tools: the copy inside all four calculators still carries em dashes from August; the brief scoped this job to layout, so the copy was not touched (question 3).
5. Division sheets: the "six division service list" was taken from BUILD-INDEX (division names, four payroll models) plus the June sheets' own six card lists, since BUILD-INDEX has no per division service list beyond that.
6. Division sheets: Atlas One is described as placing coverage "through its licensed agency and carrier partners" and PEO co-employment "through Atlas One's PEO partners"; no sheet says Atlas One is a broker, a PEO, a carrier, a CPA firm or a law firm.
7. Division sheets: the Technology sheet merges the June "Payments & POS" card into "Software marketplace and payments" to make room for an "AI services" card (the AI Email Assistant and Task Agent lines on the price list). The Consulting sheet replaces the June "Risk & Compliance Advisory" card with the Membership card the brief asked for.
8. Division sheets: the Workers comp premium audit review line shows "Contingent" as its price with "25% of the premium recovered" in the text, because the long price string wrapped the card.
9. Division sheets: type size varies slightly per sheet (tight / medium / roomy classes) so each one fills its page; the layout is otherwise identical.
10. Job 4: one corrected retry of the AppleScript was made after the first attempt failed on a script bug of mine (the `open` verb did not return a reference); the second attempt is the one that timed out. No further attempts.

## Not done

- Deck PDFs (job 4), as above.
- Copy inside the four calculators still has em dashes and the "Fortune 500" style claims were not reviewed there; out of scope for a layout pass.

## Questions for David

1. Slide 25's "ATLAS ONE REVENUE" boxes still say $299/mo (Professional) and $899/mo (Enterprise) recurring plus software margin, derived from the old $499 and $1,299. Should they become $299 and $899 on the new prices (implies $100 of software in each), or another number?
2. The Concierge note on slide 25 is the one line from the brief; do you want the $1,500 setup mentioned there too?
3. The four calculators (and most of the August tools) still carry em dashes in their copy. Want a copy pass to the no dash rule across `06 Calculators and Tools`?
4. Division sheets: the Workforce sheet no longer says "W-2 and 1099 issuance at no charge" or "401(k) fee covered" (those are PEO partner terms, not Atlas One prices). Confirm, or tell me which PEO model terms you want stated.
5. Division sheets: the Benefits and Risk sheets say coverage is placed "through Atlas One's licensed agency and carrier partners". Is Atlas One itself a licensed agency in Utah? If so the wording can be stronger.
6. Division sheets: the Technology sheet now has an AI services card with the price list AI lines; keep, or swap back to a Payments & POS card?
7. PowerPoint on the Mac Studio still cannot be scripted (AppleEvent timeout). If you open PowerPoint once and clear whatever it is asking, the next run can export both PDFs and render slides exactly; otherwise Save As PDF by hand is one step per deck.
