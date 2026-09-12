# RUN U report (terminal B, files only)

Built 2026-09-12 by Claude Code, unattended, no GHL UI, no questions asked. Brief copied to `repo:_briefs/RUN-U-terminal-B.md` with a progress log. Nothing sent, nothing deployed, nothing deleted (retired files moved to `OneDrive:_to_delete/superseded-2026-09-12/`). Pricing numbers, agreement content, BUILD-INDEX.md and the Run S deliverables were not touched.

Paths are relative to `2. A1 Official Docs/2. Atlas 1 Solutions Marketing/` unless marked `repo:` (atlas-one-intake-forms, pushed to main) or `OneDrive:`.

## Job 1: Financial Services division sheet

- Built `A1_Sales/Atals 1 Financial Services/Atlas_One_Division_Financial_Services.html` and `.pdf` (one Letter page). The other five sheets are PDFs only (June 2026, no source), so the rebuild is HTML printed to PDF through Chromium; the HTML template is kept at `HR_Docs/Atlas_One_Master_Kit/_INTERNAL (do not share)/tools/division_sheet_financial_template.html`.
- Layout matched to the Business Consulting sheet, rendered side by side: top bar with logo and "One Call Solves Everything", eyebrow, Horas headline with a periwinkle phrase, rule, lede, four "Why it is different" tiles, six "What is included" cards, platform pills with Financial Services highlighted, David's footer.
- Six cards as briefed: bookkeeping and accounting (AP/AR), tax strategy and filings, fractional CFO, QuickBooks and general ledger, CPA and audited financials, payroll through Atlas One Bookkeeping. Every price is retail from `A1_Sales/Pricing/Atlas_One_Price_List.html`; no vendor names.
- The June PDF opened fine on this machine (55 KB, one page, text layer intact). It was replaced anyway and moved to `OneDrive:_to_delete/superseded-2026-09-12/division-sheet-financial-old/Atlas_One_Division_Financial_Services_June2026.pdf` so only one version exists. Hub card "Division sheet: Financial Services" now points at the rebuilt PDF.
- Screenshots looked at: the page fit check (content ends 4 px above the footer), the PDF thumbnail, and the side by side with Consulting.

## Job 2: Partner deck v9 LIGHT fix pass and 20 slide room cut

- Deck: `A1_Sales/A1_Pitch Decks Inv/Founder General pitch deck partners/Partner Pitch Deck General/V9 Partner Pitch Deck/Atlas_One_General_Deck_LIGHT.pptx` (43 slides). Fixed in place; the untouched original is at `OneDrive:_to_delete/superseded-2026-09-12/partner-deck-v9-light-before-fix/Atlas_One_General_Deck_LIGHT_before-2026-09-12-fix.pptx`.
- (a) Title overflow: six Horas titles wrapped past their box onto the subtitle (slides 5, 12, 13, 15, 16, 30). Font shrunk by the smallest step that fits (36 to 31 or 33 pt); no wording changed. The other "about ten" the brief expected were single line numbers whose boxes are tight but do not wrap; PowerPoint does not clip them, so they were left alone.
- (b) Red and green replaced by form: 238 colour uses changed. Green fills (059669, 10B981) on header bars became solid navy with white text (31 runs turned white); green thin rules became periwinkle; green borders became navy. Red fills (991B1B, EF4444) on header bars became tinted soft blue; red thin rules became periwinkle; red borders and the light red tint became soft blue and off white. Red and green text became navy. The tick and cross glyphs stay, so before/after and done/not done still read by form.
- (c) Room cut: `Atlas_One_General_Deck_LIGHT_20-slide_cut.pptx` beside it, slides 1, 2, 3, 4, 5, 7, 8, 11, 15, 19, 22, 24, 28, 31, 32, 33, 34, 40, 41, 43 of the fixed deck (cover, big idea, founder, problem x3, solution, six divisions, competitive advantage and landscape, revenue model, LTV, how it works, traction x2, projections, valuation, founding partner structure, the ask, invitation). Slides 26 and 27 are out as instructed, and slide 23 (Master Reseller: wholesale $22 to retail $30 and margin) is out for the same reason.
- No number was changed anywhere.
- Rendering: PowerPoint's AppleScript export hung (AppleEvent timeout, most likely a first run dialog), so every slide was rendered with a python-pptx to HTML renderer and screenshotted in Chromium (scripts in `repo:_briefs/assets/run-U/`). Contact sheets of both decks were looked at and saved beside the decks (`..._contact-sheet.png`). Nothing is clipped in either. Caveat: the renderer is an approximation of PowerPoint; David should flip through both decks once in PowerPoint.
- Hub: the "General Deck LIGHT" card (which called the 43 slide deck "the cut for the room") now says PARTNER ONLY and points to the 20 slide cut for the room; a new card for the room cut.

## Job 3: Mutual NDA template

- `A1_Sales/A1 Agreements/Atlas_One_Mutual_NDA_TEMPLATE_2026-09-12.docx` (python-docx, DM Sans body, Horas headings, header on every page "DRAFT for attorney review. Not for signature."). Sections: purpose; confidential information and exclusions; obligations (care, permitted use, required disclosure, notice of breach); return or destruction with an archival copy carve out; no licence, no obligation to proceed, no relationship; non circumvention limited to Introduced Parties for 24 months; two year term, three year survival, trade secrets for as long as they qualify; remedies (injunction, fees, consequential damages exclusion); Utah law and Utah County venue; signature blocks; notes for counsel.
- The notes page lists how it differs from the July 2026 Mutual NDA & Non-Circumvention master (open ended term with 30 day notice and five year survival vs two years and three; 36 month all relationship non circumvention with liquidated damages vs 24 months on introduced parties only; the July employee non solicitation is not carried). Hub card under Agreements. Build script at `_INTERNAL (do not share)/tools/build_mutual_nda_2026-09-12.py`. Nothing sent.

## Job 4: tools backlog, top three items

The 2026-08-28 backlog note is not in `_BUILD-LOG/` (it lives in the project mirror); the BUILD-INDEX summary was used. Findings before editing: the generators hub already had labelled column headers over every money line item and the timesheet (an additive 2026-08-28 script), and both hubs and every standalone tool already had one or two sentences of help text under the title. What was actually missing was accessible labels on the line item inputs (placeholder only), labels on six paired inputs in the S-Corp calculator, and a Print / Save as PDF button on the two hubs and fifteen standalone tools.

Files changed (all in `06 Calculators and Tools (NEW Aug 2026)/`):

| File | What changed |
|---|---|
| `Atlas One Business Tools (17 generators).html` | aria-labels on every line item and timesheet input; Print / Save as PDF button beside Download PDF; print stylesheet (preview only). Help text already present (toolDesc). |
| `Atlas One Calculators (53 tools).html` | aria-labels on the six paired S-Corp inputs that had only placeholders; Print / Save as PDF button in every calculator header with a print stylesheet (active calculator only). Help text already present on all 53. |
| `Business Infrastructure Audit (Atlas One).html` | Print / Save as PDF button (in the header bar) plus print stylesheet; help text already present. |
| `Business Infrastructure Audit (Espanol).html` | Print / Save as PDF button (in the header bar) plus print stylesheet; help text already present. |
| `Business Value Diagnostic (Atlas One).html` | Print / Save as PDF button (in the header bar) plus print stylesheet; help text already present. |
| `Business Value Diagnostic (Espanol).html` | Print / Save as PDF button (in the header bar) plus print stylesheet; help text already present. |
| `Vendor Consolidation Savings (Atlas One).html` | Print / Save as PDF button (in the header bar) plus print stylesheet; help text already present. |
| `Vendor Consolidation Savings (Espanol).html` | Print / Save as PDF button (in the header bar) plus print stylesheet; help text already present. |
| `Retention Cost Calculator (Atlas One).html` | Print / Save as PDF button (in the header bar) plus print stylesheet; help text already present. |
| `Retention Cost Calculator (Espanol).html` | Print / Save as PDF button (in the header bar) plus print stylesheet; help text already present. |
| `Retention Scorecard (Atlas One).html` | Print / Save as PDF button (under the title) plus print stylesheet; help text already present. |
| `Retention Scorecard (Espanol).html` | Print / Save as PDF button (under the title) plus print stylesheet; help text already present. |
| `COI to Workers Comp Premium Estimator (Atlas One).html` | Print / Save as PDF button (under the title) plus print stylesheet; help text already present. |
| `Compliance Risk Scorecard (Atlas One).html` | Print / Save as PDF button (under the title) plus print stylesheet; help text already present. |
| `Cost of a Compliance Mistake (Atlas One).html` | Print / Save as PDF button (under the title) plus print stylesheet; help text already present. |
| `Health Comparison Builder (Atlas One).html` | Print / Save as PDF button (under the title) plus print stylesheet; help text already present. |
| `Atlas_One_Back_Office_Self_Assessment.html` | Print / Save as PDF button (in the header bar) plus print stylesheet; help text already present. |

- One defect caught and fixed during the pass: the generators hub's first `</style>` sits inside a jsPDF string, so the print stylesheet first landed there and broke the page's JavaScript ("Invalid or unexpected token"); it was moved to the page's real stylesheet and the page loads with no errors.
- Every changed file was rendered at 390 px and 1440 px (34 screenshots) and checked for the button, for JavaScript errors, and for horizontal overflow; the calculators hub was also checked with a calculator open and in print media (only the active calculator prints); the generators hub was checked in print media (preview only).
- Pre-existing, not touched: the Retention Cost Calculator (both languages) and the Vendor Consolidation Savings (Spanish) already scroll sideways at 390 px because of fixed width grids and a 520 px table; that is a layout change, not one of the three items.
- Skipped, as instructed: `Atlas_One_Scan_ID.html` (camera tool, nothing to print), `Atlas_One_Build_This_For_Me.html`, the command center. State tax auto fill already exists in the generators hub; multi page overflow needs new logic.
- Portal rebuilt with the path argument: **BUILD Sep 12, 2026 1:48 PM**, 38 tools, 10.34 MB; opened headless, stamp confirmed.

## Job 5: this report

- Master Hub: 156 cards, every file card resolves on disk; Tools Hub 28 tools, all resolve.
- Repo commits on main: brief, job 1, job 2 (with the deck scripts), job 3, job 4 (with the changed files table), report. Each pushed.

## Assumptions

1. The Financial Services sheet exists and opens here; "will not open" was probably a OneDrive placeholder on David's machine. Rebuilt anyway.
2. The other five division sheets carry em dashes and "Enrolled Agent" claims from June; the rebuilt sheet follows the current no dash rule and does not claim Enrolled Agent or CPA status (Hoffman is not a CPA per the directory note), saying "coordinated with a licensed CPA" instead.
3. Slide 23 was excluded from the room cut alongside 26 and 27 because it prints wholesale cost and margin.
4. Red/green mapping: green (good, done) to solid navy, red (bad, before) to tinted soft blue, thin rules to periwinkle, text to navy. Checkmarks and crosses stay.
5. The room cut keeps slide 25 out (it shows $99 / $499 / $1,299 tiers, which are not the confirmed set); numbers in the full deck were not changed, per the brief.
6. Print buttons on standalone tools are injected by a small script at the end of each file (additive, guarded), not by editing each layout by hand; on phones the header bar wraps so the button drops to a second line.
7. The Scan ID tool has no print button on purpose.

## Not done

- No PDF export of either deck (PowerPoint automation hung). The PPTX files and contact sheet PNGs are in place; David can Save As PDF in PowerPoint in one step.
- Slide 25 pricing in the full deck left as is (numbers untouched by instruction).

## Questions for David

1. Deck slide 25 shows Essential $99 / Professional $499 / Enterprise $1,299, not the confirmed $99 / $399 / $999 / $1,900. Update the slide, or drop it from the full deck too?
2. The full deck's cover has two decorative circles overlapping "Presented by" on the right in the render; is that how it looks in PowerPoint, or a renderer artefact? Worth a look when you open it.
3. The 20 slide cut still names Sherweb, PartnerStack and Cornerstone PEO on the equity slide (40). Keep, or strip vendor names for the room?
4. Mutual NDA: replace the July master or keep both (this one for early conversations)? Counsel's call, flagged in the notes page.
5. Financial Services sheet: should the other five division sheets be rebuilt the same way (no dashes, retail prices, current claims)? They are June PDFs with no editable source.
6. Retention Cost Calculator and Vendor Consolidation (Spanish) scroll sideways on a phone; want a mobile layout pass on those two?
7. PowerPoint on the Mac Studio needs a first run or sign in before it can be scripted; if you open it once, future runs can export PDFs and render slides exactly.
