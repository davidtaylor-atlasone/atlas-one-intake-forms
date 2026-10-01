# Run CS Job 4 report: readable on screen share, toggles you can see (2026-09-30, helper "screenshare")

## Built (full paths, all under `<MK>/_INTERNAL (do not share)/`)
- `screenshare_snippet.html`: the one shared snippet (CSS plus JS, marker comments `<!-- a1-screenshare:start v1 -->` / `<!-- a1-screenshare:end -->`). Screen only, print untouched.
- `apply_screenshare.py "<MK>" [--check]`: inserts or updates the snippet (CSS at the end of head, JS before the last body close), byte for byte idempotent (second run changes nothing), writes `screenshare_manifest.json`. `--check` exits 1 if an in scope file lacks the current snippet (lead: wire into catalogue_check.py). Also exposes `inject(html)` for generators.
- `verify_screenshare.py`: Playwright, Chromium AND WebKit (I installed Playwright WebKit, 77 MB), 1440 and 390, file://. CSV: `<MK>/_BUILD-LOG/screenshare-verify-2026-09-30.csv` (736 rows).
- Generators patched (not run): `tools/bookkeeping-docs/build.py` (page() now injects), `tools/division_sheets_build_2026-09-12.py` (inject before write); comment banners in `render_md_pages.py` (emails deliberately excluded), `08 ROI.../build_cockpit.py` (edits in place, snippet survives), `Total_Impact_Model/build_tim.py` (tim_template carries it), `tools/master-pricing-v8/build_master_pricing_v8.py`. Templates `tim_template.html`, `price_list_template.html`, `division_sheet_financial_template.html` carry the snippet themselves.

## What the snippet does
1. Text floors: body 17px, table text 16px, everything else with text 15px (p, li 16). Never lowers a larger size. Set by script as data attributes, applied with higher specificity than the page CSS.
2. "Presenting" button, fixed top right, 44px high, toggles `html.a1-presenting` (CSS zoom 130 percent, transform fallback), remembered in localStorage (try/catch), label "Presenting" / "Presenting: on", hidden in print. It steps the scale down (125, 120 ... 100) only if a page cannot take 130 without a sideways scroll at the window size, and says so in the label. It moves below a page's own top right control or fixed bar (detected by hit test).
3. Controls: native checkbox and radio redrawn (28px box, 2px border, check or dot, 44px footprint), range slider (2px track border, 30px knob), custom switches (hidden checkbox plus track, and role=switch) redrawn as 56 by 32 track with knob left plus dash (off) or knob right plus check (on) and an On/Off word beside it, tabs, chips, pills, segmented options, summaries and buttons get 44px min height and a 2px border (filled with a check mark when active), selects get 2px border and 44px height. Light surface: navy `#23304D` line, off white `#FAFAF8` knob. On any dark surface (dark theme pages, navy bars, navy cards, detected per control from the real background) off white line and navy knob. 3px `#788DE3` focus ring.
4. Narrow windows (700px or less): print page sheets that were fixed 8.5in wide now reflow (grids stack, flex rows wrap, fixed widths freed, tables get their own scroll wrapper) so `scrollWidth` equals the viewport.

## Files patched
183 files (see manifest `screenshare_manifest.json`), 54 skipped:
- 18 fragments with no head or body (blog web paste pieces, widget); 14 email template reading pages and COI notices (already sized by their renderer, verified by the rendered md step only); 12 business card print designs; 6 prospect or client named outputs (Access To Hearing, Cirque Lodge, SAMPLE audit reports, generated per deal from patched templates); Sales Kit (generated, lead owns); OSHA saved page (third party); Jason Petty kit (live deal, internal); the snippet file itself; others in excluded folders.
- Dr Gould folder, `_Rep Kits`, COMMAND, Sales Kit, build_command.py, catalogue.py, hubs.py, prices.json: not touched.
- Beyond the spec list I also included the 14 catalogue HTML tools that sit outside the named folders (Service Content Library, BRJ kit tools, Safety Training calendar, GHL setup pages, INTERNAL trackers).

## Marker check (grep -c, before I touched anything and after)
Counts of `a1-footer-person` and `a1-contact-person` on every in scope file that had either: 35 files, 0 changed.

| file | footer before | footer after | contact before | contact after |
|---|---|---|---|---|
| Atlas_One_Partner_Client_Program_PPG.html | 2 | 2 | 0 | 0 |
| Atlas_One_Services_Overview.html | 2 | 2 | 1 | 1 |
| Atlas_One_AI_Email_Assistant_OnePager.html | 2 | 2 | 0 | 0 |
| Atlas_One_AI_Task_Agent_OnePager.html | 2 | 2 | 0 | 0 |
| Atlas_One_Background_Screening_OnePager.html | 2 | 2 | 0 | 0 |
| Atlas_One_Division_Financial_Services.html | 1 | 1 | 0 | 0 |
| Atlas_One_Membership_Brochure.html | 2 | 2 | 0 | 0 |
| Atlas_One_Membership_Pricing.html | 2 | 2 | 0 | 0 |
| Atlas_One_Division_Benefits_Retirement.html | 1 | 1 | 0 | 0 |
| Atlas_One_Employee_Benefits_Menu.html | 2 | 2 | 0 | 0 |
| Atlas_One_Bookkeeping_Marketing_Sheet_V8.html | 1 | 1 | 1 | 1 |
| Atlas_One_QuickBooks_Accountant_Access_Guide.html | 2 | 2 | 0 | 0 |
| Atlas_One_Division_Business_Consulting.html | 1 | 1 | 0 | 0 |
| Atlas_One_Division_Payroll_HR.html | 1 | 1 | 0 | 0 |
| Atlas_One_Division_Technology_Operations.html | 1 | 1 | 0 | 0 |
| Atlas_One_Division_Risk_Insurance.html | 1 | 1 | 0 | 0 |
| Atlas_One_Microsoft_365_OnePager.html | 2 | 2 | 0 | 0 |
| Atlas_One_Software_and_Licenses_OnePager.html | 2 | 2 | 0 | 0 |
| Atlas_One_Client_Dashboard_GHL.html | 2 | 2 | 0 | 0 |
| Atlas_One_Client_Portal.html | 3 | 3 | 1 | 1 |
| Atlas_One_Industry_Overlay_01_Audiology.html | 2 | 2 | 0 | 0 |
| Atlas_One_Industry_Overlay_02_Dental.html | 2 | 2 | 0 | 0 |
| Atlas_One_Industry_Overlay_03_Construction.html | 2 | 2 | 0 | 0 |
| Atlas_One_Industry_Overlay_04_Technology.html | 2 | 2 | 0 | 0 |
| Atlas_One_Industry_Overlay_05_Hospitality.html | 2 | 2 | 0 | 0 |
| Atlas_One_Industry_Overlay_06_Professional_Services.html | 2 | 2 | 0 | 0 |
| Atlas_One_Price_List.html | 1 | 1 | 0 | 0 |
| Atlas_One_Proof_Sheet.html | 2 | 2 | 0 | 0 |
| Atlas_One_Total_Impact_Model.html | 2 | 2 | 0 | 0 |
| Atlas_One_Everything_We_Handle.html | 3 | 3 | 0 | 0 |
| Employee Benefits Options (Atlas One).html | 1 | 1 | 1 | 1 |
| Health Quote Census Intake (Atlas One).html | 1 | 1 | 1 | 1 |
| tim_template.html | 2 | 2 | 0 | 0 |
| Atlas_One_Bookkeeping_Marketing_Sheet_V8.html | 1 | 1 | 1 | 1 |
| price_list_template.html | 1 | 1 | 0 | 0 |

## Control families found and how each is covered
| family (examples) | covered by | instances checked | border 2px and 44px foot |
|---|---|---|---|
| native checkbox (Quick Quote services, census, cockpit rows, builders) | redrawn input, check mark, label min 44 | 1,240 | all pass |
| native radio (Business Infrastructure Audit 72 per file, intake forms) | redrawn input, dot | 1,276 | all pass |
| range slider (WSA credit page) | styled track and knob | 12 | pass (track border read from the rule, headless Chromium does not report slider pseudo styles) |
| custom switch (Cost of a Compliance Mistake role=switch, NDA, W-2 At-Will builders) | track plus knob drawn by snippet, On/Off word beside | 120 | all pass |
| segmented, tab, chip, pill, mopt, EN/ES toggle (NDA, Health Comparison, Cockpit, Pitch tabs, Quick Quote steps) | 2px border, 44px, filled plus check when active | 1,994 | all pass |
| buttons, summaries, selects | min 44px, 2px border where none, select redrawn so WebKit honours the height | 5,400 | all pass after the select fix |
Dark theme (Quick Quote, Prospect Web Pitch) rendered with prefers-color-scheme dark and looked at.

## Proof
Screenshots (before and after, 1440 and 390, Presenting at 1280x720 in both engines, dark): `/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs/assets/run-CS/shots/screenshare/` (16 families: toggle, switch and segmented, slider, two dark, two table heavy, two intake, two sales, tabs, chips, radios, bookkeeping sheet, self assessment). I looked at them and fixed what showed: switch tracks lost on dark rows (specificity, own background taken as surface), segmented option children double bordered, squeezed columns in the Services Overview at 390, the "Most popular" badge growing over the tier name in the membership sheet.
Final CSV: 736 rows (183 files, 2 engines, 1440 and 390, plus dark rows). Every row passes body 17, text 15, table 16, Presenting present and working (181 files reach 130 percent, 120 percent on Membership no longer, see below), no horizontal scroll at 390 or at 1280x720 Presenting, all control families pass. Remaining flagged rows (48) are all pre-existing and not caused by the snippet (the baseline run on the untouched files shows the same):
- network requests: Google Fonts link in 7 sales pieces (What We Do, AI Task Agent, Background Screening, Client Dashboard, Client Portal, Proof Sheet; Business Tools 17 generators loads one too), GHL form embed in Get Quote (its purpose), CDN script in Scan ID (zxing, also a WebKit console error).
- console error on the 3 templates (tim_template parse error on its placeholders, ERR_FILE_NOT_FOUND on the two other templates' placeholders): templates are not meant to open on their own.
Presenting stops short of 130 on 2 pages that are fixed print layouts: W-2 At-Will builder (120) and Invoice MASTER (125). Nothing clipped, no sideways scroll.

## Item 3, membership comparison sheet (`A1_Sales/Atals 1 Membership Pricing/Atlas_One_Membership_Pricing.html` and `.pdf`)
Screen: whole table fits at 1440 and at 390, and at 1280x720 with Presenting on I added a screen only reflow rule (the narrow layout mirrored for `html.a1-presenting`) and lifted the "Most popular" badge, both in that file. PDF: I printed the current HTML (print emulation, Letter, backgrounds) to a scratch PDF: 1 page, nothing clipped, same size and text as the existing PDF, so I did not replace the PDF. Screens: `membership-*` and `membership-pdf-*` in the shots folder.

## Item 4, Back Office Self Assessment
Question now reads "When were benefits last shopped with different carriers or brokers?" with a "Why shopping matters" note ("renewals creep up when nobody compares the market. One broker quoting one carrier is not shopping, it is the same answer asked twice."). No prices, no dashes, single file, offline. Edited: `<MK>/06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Back_Office_Self_Assessment.html` (carries the snippet) and, in the working tree only, `/Users/davidtaylor/Projects/atlas-one-intake-forms/tools/self-assessment/index.html` (not committed, no snippet: LEAD, please commit it). Rendered at 1440 and 390, no console errors (`selfassess-*` shots).

## price_scan
`price_scan.py -v` after: 0 retired price hits in total. Before for the files I own: 0.

## Assumptions
1. Prospect or client named outputs are skipped (templates patched); email pages skipped per spec.
2. Dark detection is per control from the real background, not from the theme setting, so navy bars on a light page also get the off white style.
3. Touch target for a native checkbox or radio is a 28px box with an 8px margin (44px footprint) plus a 44px label.
4. "Active" is read from class names (active, on, sel, selected, current, checked) or aria state; custom code that signals state any other way gets no check mark.
5. Text below 15px is raised even in decorative eyebrows, which can lengthen a layout slightly.
6. WebKit was missing, I installed it with Playwright.
7. The Tools page "Primary state" default of Utah in Cost of a Compliance Mistake is pre-existing and untouched.

## Skipped
Google Fonts links in 7 sales pieces (needs DM Sans embedded from `A1_Final Brand/3. Fonts/`, outside this job); fragments and email pages as above.

## Questions for David
1. Embed DM Sans in the 7 sales pieces that still call Google Fonts, so they work offline?
2. Quote Cockpit has an amber "Internal: margin and discount room" bar, off brand (colour only; internal tool). Make it navy outlined?
3. Cost of a Compliance Mistake defaults Primary State to Utah; should it default to a blank "Select your state"?
4. Commit the self assessment repo copy as is? (Lead action.)
5. Presenting button on a phone sits over the page header; fine, or hide it under 600px wide?
