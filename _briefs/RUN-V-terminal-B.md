# RUN V (terminal B, files only, no GHL UI): follow-ons from Run U

Written by Cowork 2026-09-12. Same rules as Runs S and U: no questions, log assumptions, batch questions at the end
of `<Master_Kit>/_BUILD-LOG/RUN-V-report.md`, never delete (mv to `_to_delete/superseded-2026-09-12/`), never send,
never deploy, brand rules, verify by rendering and looking. Do not touch Run S pricing files, agreements content or
BUILD-INDEX.md. Copy this file to `_briefs/RUN-V-terminal-B.md`, commit after each job.

## Job 1: deck slide 25, confirmed tiers
In `A1_Sales/A1_Pitch Decks Inv/Founder General pitch deck partners/Partner Pitch Deck General/V9 Partner Pitch Deck/
Atlas_One_General_Deck_LIGHT.pptx` (the fixed 43-slide deck), slide 25 shows $99 / $499 / $1,299. The confirmed, final
tier set is a recorded decision, so this is the one number change allowed: Essential $99 (setup waived), Professional
$399 (setup $495, often waived), Enterprise $999 (setup $995, waived on annual), Concierge $1,900 (setup $1,500).
If the slide has three columns, keep three (Essential, Professional, Enterprise) and add a one-line note under them:
"Concierge, your fractional COO, $1,900 a month." Keep the layout, shrink text if needed, render the slide and look.
Do not add slide 25 to the room cut.

## Job 2: mobile layout pass on three tools
`06 Calculators and Tools (NEW Aug 2026)/`: Retention Cost Calculator (Atlas One), Retention Cost Calculator (Espanol),
Vendor Consolidation Savings (Espanol) scroll sideways at 390 px (fixed width grids, a 520 px table). Make them stack
on narrow screens (grid to one column under 700 px, tables to stacked rows or a scroll container with the page body
never wider than the screen), touch targets at least 44 px. Same fix on the English Vendor Consolidation if it has
the same table. Render each at 390 px and 1440 px, confirm document.documentElement.scrollWidth equals the viewport
width at 390 px, and that the numbers produced are unchanged (run one sample calculation before and after and compare).
Then copy the fixed files into the repo `tools/` equivalents if those tools are also published there
(retention-cost, vendor-consolidation), push, confirm 200.

## Job 3: rebuild the other five division sheets to match Financial Services
The June 2026 PDFs (Workforce & HR, Benefits & Retirement, Risk & Insurance, Technology & Operations, Business
Consulting) carry em dashes and out of date claims and have no editable source. Rebuild each from the template
`_INTERNAL (do not share)/tools/division_sheet_financial_template.html` used in Run U: same layout, six "What is
included" cards per division from the six-division service list in `_BUILD-LOG/BUILD-INDEX.md` and the project
instructions, retail prices only from `A1_Sales/Pricing/Atlas_One_Price_List.html` (leave the price line off a card
when the price list has no line for it), no vendor or PEO brand names, no dashes, no claims about licences Atlas One
does not hold (say "through Atlas One's carrier partners", never "our health plan"). Membership tiers on the Business
Consulting sheet, if mentioned, are the confirmed set. HTML + PDF per division, one Letter page each, named exactly
like the existing PDFs so every link keeps working; move the June PDFs to
`_to_delete/superseded-2026-09-12/division-sheets-june-2026/`. Render all six as a contact sheet and look at it
side by side. Keep a one-line "what changed vs June" per sheet in the report so David can review the claims.

## Job 4: PDF export of both partner decks
Try in this order: (1) LibreOffice headless if present (`soffice --headless --convert-to pdf`), (2) PowerPoint via
AppleScript with a 120 second timeout, once. If both fail, skip and say so; do not loop. Save PDFs beside the PPTX
files. Do not add Hub cards for the PDFs if the PPTX cards already exist; update those cards' descriptions to say a
PDF sits beside the deck.

## Job 5: report
Rebuild the Portal if any tool changed (path argument, confirm the stamp). `RUN-V-report.md`: what changed, paths,
what was looked at, assumptions, skipped items, questions at the end. Commit and push the repo side.

---

## Progress log (terminal B)

- 2026-09-12: brief copied. Starting Job 1.
- Job 1 done: slide 25 of Atlas_One_General_Deck_LIGHT.pptx now Essential $99 (setup waived) / Professional $399 (setup $495, often waived) / Enterprise $999 (setup $995, waived on annual), three columns kept, cards tightened by 0.2 in, one line note "Concierge, your fractional COO, $1,900 a month." under the cards, headline "Three Tiers" changed to "Four Tiers". Before copy in _to_delete/superseded-2026-09-12/partner-deck-v9-light-before-slide25/. Rendered slide 25 and the full contact sheet (refreshed beside the deck) and looked. Room cut untouched (slide 25 stays out). Script: _briefs/assets/run-V/slide25.py.
- Job 2 done: additive mobile CSS block (id a1mobile-2026-09-12) in Retention Cost Calculator (EN, ES) and Vendor Consolidation Savings (EN, ES): grids to one column under 700 px, the 520 px vendor table becomes stacked rows (thead hidden, per field labels via ::before), 44 px inputs/select/buttons on touch screens, checkboxes wrapped in a 44 px label. Before copies in _to_delete/superseded-2026-09-12/tools-before-mobile-pass/. Measured at 390 px: scrollWidth 390 on all four (was 510, 526, 443, 391); one sample calculation (20 inputs / 12 vendor rows) gives byte identical outputs before and after; screenshots at 390 and 1440 looked at. English copies pushed to repo tools/retention-cost and tools/vendor-consolidation. Scripts: _briefs/assets/run-V/{overflow,sample,shots}.mjs, mobilepass.py.
- Job 3 done: five division sheets rebuilt from the Financial Services template as HTML + PDF (one Letter page each, Chromium print), same file names in the same folders (Atlas 1 Payroll PEO, Atlas 1 Benefits, Atlas 1 Risk Docs, Atlas 1 Risk Docs/Atlas 1 Tech Operations, Atlas 1 Consulting). June PDFs moved to _to_delete/superseded-2026-09-12/division-sheets-june-2026/. Six cards per sheet from the June service lists, prices only from the price list, no vendor or PEO brand names, no dashes, licence claims reworded (through Atlas One's carrier / agency / PEO partners). Contact sheet of all six looked at, saved as A1_Sales/Atlas_One_Division_Sheets_contact-sheet_2026-09-12.png. Five Hub card descriptions updated (Hub backed up to _to_delete/superseded-2026-09-12/master-hub-before-run-V/). Builder saved as _INTERNAL (do not share)/tools/division_sheets_build_2026-09-12.py and _briefs/assets/run-V/division_sheets.py.
