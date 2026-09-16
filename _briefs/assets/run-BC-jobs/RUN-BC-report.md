# Run BC report, GHL-JOBS terminal (files and code only)

Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md`, "membership headcount labels everywhere, commission agreement clean up."
Copied to the portal repo at `_briefs/BRIEF-GHL-JOBS-2026-09-16.md`. Prior report (Run BB) backed up to
`_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunBB.md`.

## Built

### Job 1: membership headcount labels

New labels applied everywhere the old headcount clause appeared. Files edited (all backed up first to
`_to_delete/superseded-2026-09-16/before-runBC/`):

1. `A1_Sales/Atals 1 Membership Pricing/Atlas_One_Membership_Pricing.html` (the four tier comparison sheet,
   Essential and Professional `for` divs) and its `.pdf`, re-rendered with `render_html_pdfs.py`. Still fits one
   Letter landscape page (1 page before, 1 page after).
2. `A1_Sales/Atals 1 Membership Pricing/Atlas_One_Membership_Brochure.html` (page 4 tier picker table) and its
   `.pdf`, re-rendered, page count unchanged (4 pages before and after).
3. `A1_Sales/Website/BRJ Pricing Page Package 2026-09-13/Atlas_One_Pricing_Page_SPEC.html` (the "fit" divs for
   Essential and Professional, plus the three question tier picker's employee count buttons for consistency
   with the new copy), re-rendered to `Atlas_One_Pricing_Page_SPEC_preview.pdf`, and the two PDF copies in that
   folder (`Atlas_One_Membership_Pricing.pdf`, `Atlas_One_Membership_Brochure.pdf`) replaced with the fresh
   renders from item 1 and 2.
4. `08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html` (the `TIERSET` array used to build the export
   deck).

Old to new label text, everywhere it appeared:

| File | Tier | Old | New |
|---|---|---|---|
| Membership Pricing sheet | Essential | "Under 20 employees, one state. You do most of it yourself." | "1 to 20 employees, one state, you do most of it yourself." |
| Membership Pricing sheet | Professional | "About 20 to 50 employees. The owner is still the back office." | "15 to 50 employees, the owner is still the back office." |
| Brochure, Pricing Page SPEC, Quote Cockpit | Essential | "Under 20 employees, one state, under five hours a month. No benefits renewal to manage yet." | "1 to 20 employees, one state, under five hours a month. No benefits renewal to manage yet." |
| Brochure, Pricing Page SPEC, Quote Cockpit | Professional | "Twenty to fifty employees, or five to fifteen hours a month. The owner is still the back office." | "15 to 50 employees, or five to fifteen hours a month. The owner is still the back office." |
| Pricing Page SPEC, tier picker buttons | (question 01) | "Under 20" / "20 to 50" | "1 to 20" / "15 to 50" |

Not changed, checked and confirmed clean:
- Repo Quick Quote (no such file exists there; the standalone Quick Quote tool lives in the Master Kit at
  `09 Quick Quote Tool/`) and the Master Kit's own Quick Quote tool, grepped for "employees" near
  Essential/Professional, zero hits.
- Portal "Add services" card: grepped `Atlas One COMMAND.html` and `Atlas_One_Cornerstone_Strategy_INTERNAL.html`
  for the old headcount patterns, zero hits (the live client portal app itself is owned by the separate PORTAL
  terminal, out of scope for this run; nothing in the Master Kit's own COMMAND/Cornerstone files carried a
  headcount clause to fix).
- `_INTERNAL (do not share)/tools/agreements/generate.py` Membership Schedule: grepped, does not carry a
  headcount clause, nothing to regenerate.

Wrote `Note_to_Thomas_headcount_labels_2026-09-16.txt` in the BRJ package folder, two lines, no dashes, plain
words, telling him the Essential and Professional fit lines changed and what they now read, and that the tier
picker's first two employee count buttons changed to match.

Ran `catalogue_check.py`: 192 entries, all paths resolve. Backed up the prior `Atlas One COMMAND.html` to
`_to_delete/superseded-2026-09-16/before-runBC/`, rebuilt it: 192 items, 48,647,596 bytes, stamp "Atlas One
COMMAND: build Sep 16, 2026 2:10 PM". `Atlas One Tools (share with prospects).html` is intentionally retired
per the build script's own comment (superseded by separate pages), nothing to rebuild there.

### Job 2: commission agreement clean up

In `06 Calculators and Tools (NEW Aug 2026)/W-2 At-Will Employment Agreement Builder (Atlas One).html` (backed
up first), removed the two editorial sentences from the printed Sales Commission Agreement:
- Section 4 ("How and When a Commission is Earned"): removed "Default earning terms prepared by Atlas One for
  the Company's review; the Company's counsel should confirm or adjust before signing."
- Section 6 ("Draws, Advances, and Adjustments"): removed "Default terms prepared by Atlas One; the Company's
  counsel should confirm before signing."

Added the same guidance as an on screen only hint, in the same style as the existing FLSA and state hints,
directly under the Draws/advances/adjustments field (the last field in the Commissions Paid section): "The
earning terms in Section 4 and the draws and adjustments terms in Section 6 of the Sales Commission Agreement
are Atlas One defaults, prepared for the Company's review. Have the Company's counsel confirm or adjust them
before signing. This note is for you only and does not print on the document." It never prints because it sits
outside the print-only document containers the same way the FLSA and state hints already do.

Confirmed the page-break-before rule (`.doc-page-break{page-break-before:always;}`, CSS line 218) sits on the
Sales Commission Agreement's own opening `<div>` (line 785), the same pattern used for the Hold Harmless page
(opening `<div>` at line 763), so the commission agreement starts on its own printed page independent of the
Hold Harmless page.

## Verification

Ran the brief's $125,000 California test end to end with headless Chromium: California governing state, exempt,
$125,000 salary, commissions on ($185,000 OTE, 8% rate), Hold Harmless gate checked, printed to PDF.

- 7 pages total, zero console errors.
- Page 1 to 3: the offer letter (California exempt floor check passes silently at $125,000, no warning shown,
  as expected since $125,000 is above the roughly $70,304 floor).
- Page 4: opens directly with "SALES COMMISSION AGREEMENT" as its first line, its own page, not sharing the
  offer letter's last page.
- Page 6: opens directly with "HOLD HARMLESS & ACKNOWLEDGEMENT" as its first line.
- Zero occurrences of "Default earning terms prepared" or "Default terms prepared" anywhere in the printed
  output (confirmed with `pymupdf` text extraction across all 7 pages).
- Zero em or en dash characters anywhere in the printed output.

Test PDF saved to `_briefs/assets/run-BC-jobs/W2_CA_125k_commission_test.pdf`.

Headless Chromium at 1440px and 390px on every edited HTML file (screenshots in
`_briefs/assets/run-BC-jobs/shots/`):

| File | scrollWidth = viewport | console errors | non file:// requests | dash characters |
|---|---|---|---|---|
| Atlas_One_Membership_Pricing.html | yes | 0 | 0 | 0 |
| Atlas_One_Membership_Brochure.html | yes | 0 | 0 | 0 |
| Atlas_One_Pricing_Page_SPEC.html | yes | 0 | 0 | 0 |
| Atlas_One_Quote_Cockpit.html | yes | 0 | 0 | 15 (pre-existing, see Assumptions) |
| W-2 At-Will Employment Agreement Builder (Atlas One).html | yes | 0 | 0 | 0 |

`pdftotext` grep on the five regenerated PDFs (`Atlas_One_Membership_Pricing.pdf`,
`Atlas_One_Membership_Brochure.pdf` in both their home folder and the BRJ website package folder, and
`Atlas_One_Pricing_Page_SPEC_preview.pdf`): new labels present in all five, zero leftover "Under 20", "20 to
50", "About 20 to 50" or "Twenty to fifty" text, zero em or en dash characters. (`pdftotext` is not installed on
this machine; substituted `pymupdf` for text and page count extraction throughout, same result, see
Assumptions.)

## Assumptions

1. `pdftotext` is not installed on this machine. Used `pymupdf` (already installed and used elsewhere in the
   Master Kit's own tooling, e.g. `render_html_pdfs.py`) for page count and text extraction everywhere the
   brief calls for `pdftotext`. Same information, different tool.
2. `Atlas_One_Pricing_Page_SPEC_preview.pdf` moved from 3 pages to 5 pages on re-render. Tested the unedited
   backup HTML (byte for byte the same as before my two word edits) at every desktop width from 768px to
   1600px and could not reproduce a 3 page render at any width; the closest ranges (1366 to 1600px) all land on
   5 pages. The original 3 page PDF was evidently produced with different render settings than
   `render_html_pdfs.py`'s width/height path, which are not recorded anywhere I could find. This file is a
   scrollable webpage preview (no `@page` rule, unlike the pricing sheet), and the brief only states a hard
   one page requirement for the Membership Pricing sheet, not for this preview, so I rendered it at 1120px
   (the page's own `max-width:1080px` plus its side padding) and moved on rather than guessing further at
   settings I cannot recover.
3. Also updated the Pricing Page SPEC's tier picker employee count buttons ("Under 20" / "20 to 50" to "1 to
   20" / "15 to 50") even though the brief's four grep patterns technically caught them as a side effect rather
   than naming them directly, because leaving the quiz answers out of step with the tier fit text one paragraph
   above them would read as a mismatch on the same page. The button values (`data-v="0"`, `data-v="1"`, etc.)
   that drive the picker's scoring logic were not touched, only the visible label text.
4. Left the Quote Cockpit's 15 pre-existing em and en dash characters alone (product and hub names like
   "Connecteam, Operations Hub," per-unit labels like "per EE/mo," dollar ranges like "$300 to 1,000/mo," and
   one internal only "margin and discount" label). None of them are in text I touched for this run, they
   predate Run BC, and this tool carries an internal quoting sheet that isn't itself a client facing brand
   document in the same sense as the pricing sheet or brochure. Flagging it rather than rewriting unrelated
   copy I was not asked to touch.
5. Noted, did not touch: the W-2 builder prints a "Want it done for you, email David, book a call" banner on
   page 1 of every generated document (no print media rule hides it). This predates Run BC and is not part of
   either job in this brief.

## Skipped

Nothing in the brief was skipped. Both jobs, all files listed, and all verification steps were completed.

## Questions for David

1. The Pricing Page SPEC's quiz picker buttons now read "1 to 20" and "15 to 50" to match the new tier fit
   copy (see Assumption 3). If you would rather the quiz keep its own independent buckets regardless of the
   tier copy, say so and I will revert just the button labels.
2. `Atlas_One_Pricing_Page_SPEC_preview.pdf` is now 5 pages instead of 3 (see Assumption 2). I could not find
   the original render settings anywhere in the Master Kit to reproduce the exact 3 page version. If a specific
   page count or viewport width matters for how BRJ or anyone else uses this preview file, tell me the target
   and I will re-render to it.
3. The Quote Cockpit's internal quoting text still uses several dashes (Assumption 4). It is marked
   "INTERNAL, NEVER SHOWN TO CLIENT" in places, so I left it, but if you want the whole tool held to the same
   no dash rule as client facing collateral, I can clean it up as a follow up job.
4. The "Want it done for you" banner prints on page 1 of every W-2 builder document (Assumption 5). Want that
   suppressed from print output in a future job, or is it intentional that a printed copy carries the CTA?
