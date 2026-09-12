# RUN U (terminal B, files only, no GHL UI): backlog clearing while David answers the Run S questions

Written by Cowork 2026-09-12. Same rules as Run S: no questions, log assumptions, batch questions at the end of the
report, never delete (mv to `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-12/`), never send, never deploy,
brand rules (four colours, Horas + DM Sans embedded, no dashes in copy, status by form), verify by rendering and
looking. Do NOT touch pricing numbers, agreements content, BUILD-INDEX.md, or anything from Run S (David is reviewing
it). Master Kit: `find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null | grep -vi -e _to_delete -e archiv`.
Copy this file to `_briefs/RUN-U-terminal-B.md`, log there, commit after each job, report to
`<Master_Kit>/_BUILD-LOG/RUN-U-report.md`.

## Job 1: Financial Services division sheet (missing since August)
`Atlas_One_Division_Financial_Services.pdf` is missing or will not open. Find the other five division sheets
(search the Marketing folder and A1_Sales for `Atlas_One_Division_*`), read one fully (layout, sections, tone, length),
and rebuild the Financial Services sheet to match exactly: bookkeeping and accounting (AP/AR), tax strategy and filings,
fractional CFO, QuickBooks and general ledger, CPA and audited financials, payroll through Atlas One Bookkeeping.
Retail prices only, from `A1_Sales/Pricing/Atlas_One_Price_List.html` (Run S); no vendor names. If the other five are
PPTX, build PPTX with python-pptx and export PDF; if HTML, build HTML and print to PDF. Render to images and compare
side by side with one of the five. Save beside the other five, Hub card, retire any broken copy.

## Job 2: General / Partner deck v9 LIGHT fix pass
Find the deck (`2. Atlas 1 Solutions Marketing/` deck folder, name contains "Partner Investment Presentation" or
"v9 LIGHT", 43 slides). Known problems: title overflow on about ten slides, red and green status colours (brand has
none), and it is too long for the room. Do: (a) fix every title overflow (shorten or shrink, verify by rendering every
slide to PNG and looking); (b) replace red/green status with form: solid navy = done, tinted soft blue = in progress,
outlined = not started, plus a periwinkle left rule; (c) produce a 20-slide "room cut" as a SEPARATE file with
"_20-slide_cut" in the name, keeping the narrative arc (problem, six divisions, model, traction, economics, ask), and
NEVER include slides 26 and 27 (wholesale cost and margin) in the room cut; the full deck stays partner-only. Render
both decks to contact sheets, look at them, fix anything clipped. Hub cards for both. Do not change any number.

## Job 3: Mutual NDA template
Draft `A1_Sales/A1 Agreements/Atlas_One_Mutual_NDA_TEMPLATE_2026-09-12.docx` (python-docx, brand fonts, header
"DRAFT for attorney review. Not for signature."): mutual confidentiality, definition of confidential information,
exclusions, permitted use, term (2 years, survival 3 years for trade secrets), return or destruction, no licence,
no obligation to proceed, non-circumvention limited to introduced parties for 24 months, remedies, Utah law,
signature blocks, plus a "notes for counsel" page. Check the agreements index from Run S for the existing
"Mutual NDA & Non-Circumvention" PDFs and note where this draft differs. Hub card. Nothing sent.

## Job 4: tools improvement backlog, top items only
Read `<Master_Kit>/_BUILD-LOG/` for the 2026-08-28 backlog note (or the project mirror text inside BUILD-INDEX under
"IMPROVEMENT BACKLOG"). Do the first three items that are pure HTML edits across the calculators and generators:
labels on every line-item input box, a Print / Save as PDF button on every tool that lacks one, and per-tool help
text (one or two sentences under the title saying what the tool is for). Work file by file in
`06 Calculators and Tools (NEW Aug 2026)/`, keep a table of which files changed, render each changed tool at
390 px and 1440 px and look. Skip any item that needs new logic (state tax auto-fill, multi-page overflow). Rebuild
the Portal at the end (path argument) and confirm the stamp.

## Job 5: report
`RUN-U-report.md`: what changed, paths, screenshots looked at, assumptions, skipped items, questions at the end.
Commit and push the repo side; OneDrive side is in place.

---

## Progress log (terminal B)

- 2026-09-12: brief copied. Starting Job 1.
- Job 1 done: Financial Services division sheet rebuilt as HTML + PDF in A1_Sales/Atals 1 Financial Services/ (old June PDF, which did open here, moved to _to_delete/superseded-2026-09-12/division-sheet-financial-old/). Layout matched to the Consulting sheet side by side. Hub card.
- Job 2 done: Atlas_One_General_Deck_LIGHT.pptx fixed in place (original moved to _to_delete/superseded-2026-09-12/partner-deck-v9-light-before-fix/), 6 wrapped titles shrunk (slides 5, 12, 13, 15, 16, 30), 238 red/green colour uses replaced by form, 31 text runs turned white on navy. Room cut: Atlas_One_General_Deck_LIGHT_20-slide_cut.pptx (slides 1,2,3,4,5,7,8,11,15,19,22,24,28,31,32,33,34,40,41,43). PowerPoint AppleScript export hung, so rendering used a python-pptx to HTML renderer (scripts in _briefs/assets/run-U/) and Chromium; contact sheets saved beside the decks. Hub cards.
- Job 3 done: A1_Sales/A1 Agreements/Atlas_One_Mutual_NDA_TEMPLATE_2026-09-12.docx with a notes for counsel page that lists where it differs from the July 2026 Mutual NDA & Non-Circumvention master. Hub card under Agreements. Nothing sent.
- Job 4 done: 17 tool files changed (table in the report). Portal rebuilt.
- Job 5 done: report written. Run complete.
