# RUN T report (terminal B, files only)

Built 2026-09-12 by Claude Code. No GHL UI, no questions asked, no pricing numbers, agreements or BUILD-INDEX.md touched.

## 1. "104 services" corrected to 99

- `Atlas_One_MASTER_HUB.html`: Quick Quote card text now "99 services, all six divisions."
- `_INTERNAL (do not share)/build_portal.py`: Quick Quote blurb now "99 services across all six divisions".
- `Atlas One — Tools Hub.html`: checked, it never stated a count; no change.
- `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`: checked the visible text, it never states a count (the only "104" is a CSS padding value); no change.
- Portal rebuilt with the path argument: `Atlas One PORTAL.html`, **BUILD Sep 12, 2026 1:19 PM**, 38 tools, 10.32 MB, and the "99 services" blurb is inside it.

## 2. Public tools index

`repo:tools/index.html` already listed both tools (from Run S) with one line descriptions. Each card now also carries the tool's name above the question headline: Back Office Self-Assessment, Retention Cost Calculator, Vendor Consolidation Savings, Workers Comp Premium Check. Rendered at 1200 px and checked. Pushed (commit "Run T: name each tool on the public tools index"); https://forms.atlasonesolutions.com/tools/ returns 200 and serves the new markup (Pages build status: built).

## 3. Price list and pricing page re-rendered

- `A1_Sales/Pricing/Atlas_One_Price_List.html` at 390 px and 1440 px: no horizontal overflow at either width, no wrapped price (price cells are nowrap; the checker's "wrapped" hits were tall rows from wrapped descriptions, confirmed by eye). One real defect found and fixed: on screen at 1440 px the absolutely positioned footer overlapped the last row of page 1 ("Group health, dental, vision ..."). The footer is now static on screen (the page grows) and absolute only in print, so the PDF layout is unchanged. Template in `_INTERNAL (do not share)/tools/master-pricing-v8/price_list_template.html` updated to match.
- `A1_Sales/Pricing/Atlas_One_Price_List.pdf` re-rendered (2 Letter pages, print check: page 1 content ends at 944 px of 1056, page 2 at 900); page 1 thumbnail looked at, clean.
- `A1_Sales/Website/Atlas_One_Website_Pricing_Page_DRAFT.html` at 390 px and 1440 px: no overflow, no wrapped prices or stat figures; nothing to fix.

## 4. Commits

Repo `atlas-one-intake-forms`, main: "Run T: name each tool on the public tools index" (tools/index.html) and "Run T: report" (this file mirrored to `_briefs/assets/run-T/`). OneDrive changes (Hub, build_portal.py, Portal, price list HTML and PDF, template) are not in git; they are in place on OneDrive.
