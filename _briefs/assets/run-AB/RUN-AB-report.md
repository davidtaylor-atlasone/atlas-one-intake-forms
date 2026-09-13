# RUN AB report (terminal B, files only)

Built 2026-09-13 by Claude Code, unattended, no GHL UI, no questions asked. Job: find every HTML tool in `06 Calculators and Tools (NEW Aug 2026)/` and at the Master Kit root that still loads a font from fonts.googleapis.com or fonts.gstatic.com, remove the Google link, embed DM Sans (and Horas where needed) the way the hosted self-assessment does, prove the font offline, rebuild the Portal. Scripts, logs and renders in `repo:_briefs/assets/run-AB/`. Nothing sent, nothing deployed, nothing deleted (every changed file was copied first, byte identical, to `OneDrive:_to_delete/superseded-2026-09-13/fonts-before/`; the previous Portal to `.../superseded-2026-09-13/portal-before/`).

Paths are relative to `HR_Docs/Atlas_One_Master_Kit/` unless marked `repo:` (atlas-one-intake-forms, main, pushed), `OneDrive:` (the OneDrive-AtlasOneSolutions root) or `_INTERNAL/`. `CAL/` is `06 Calculators and Tools (NEW Aug 2026)/`.

## What was found

**Twelve files, all in `CAL/`; none at the kit root.** The brief said thirteen; the search (`grep -rl` for `fonts.googleapis` or `fonts.gstatic`, recursive under `CAL/` and over the root `*.html`) finds twelve, the same twelve Run AA counted ("12 other kit tools have the same link" was miscounted in that summary: it was 11 others plus Time Savings). The root has only the Tools Hub and the Portal, neither of which links Google. Every one of the twelve asked for DM Sans; nine of them (`preconnect` pairs plus the `css2` stylesheet) and three had the stylesheet link alone. Three of the stylesheet links were the two line `media="print" onload=...` non-blocking form.

## What was done to each file

`repo:_briefs/assets/run-AB/embedfonts.py` (log: `_patch-log.jsonl`). For each file: copy to the backup folder and check it reads back identical; drop every `<link>` whose href is on fonts.googleapis.com or fonts.gstatic.com (preconnects included); put one `<style id="a1fonts-2026-09-13">` block where the css2 stylesheet link was, containing one `@font-face` per face in exactly the self-assessment's form: `font-family:'DM Sans';src:url(data:font/ttf;base64,…) format('truetype');font-weight:N;font-display:swap`. DM Sans 400 and 700 always; 500 when the file's CSS has `font-weight:500` (eight files); Horas (`font-weight:400 700`) only in the one file that uses Horas without embedding it (the command center). A Python check strips the block back out and gets the original minus the removed links, byte for byte: nothing else in any file changed.

Font bytes come from `A1_Final Brand/3. Fonts/DM_Sans/static/DMSans-Regular.ttf`, `DMSans-Medium.ttf`, `DMSans-Bold.ttf` and `Horas-Medium.ttf`. The Regular, Bold and Horas files are byte identical to what `repo:tools/self-assessment/index.html` embeds (checked by decoding its base64 and comparing), so the Medium face is the same family, same source, same encoding.

## Results (1440 px, network blocked, `repo:_briefs/assets/run-AB/fontcheck.mjs`, log `shots/_fontcheck-log.json`)

Each file was rendered three ways: **A** the backup with the network blocked (what the kit did offline), **B** the backup with the Google css2 request answered locally by the same three brand TTFs (a stand in for online), **C** the patched file with the network blocked. The rendered face comes from Chrome's `CSS.getPlatformFontsForNode` on up to 40 text bearing elements per page, not from the CSS string. "Layout B = C" compares the rounded bounding rect of every element in the page between B and C.

| # | File | Links removed | Faces embedded | Body text before (offline) | Body text after (offline) | DM Sans asked / rendered | Serif | JS errors | Layout B = C | Size |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `Atlas One Business Tools (17 generators).html` | 3 | DM Sans 400, DM Sans 700 | .SF NS (system) | DM Sans | 9 / 9 | 0 | 0 | yes | 857 KB → 1004 KB |
| 2 | `Atlas One Savings Summary (Atlas One).html` | 3 | DM Sans 400, DM Sans 500, DM Sans 700 | .SF NS (system) | DM Sans | 12 / 12 | 0 | 0 | yes | 33 KB → 253 KB |
| 3 | `Atlas_One_Collections_Letter.html` | 3 | DM Sans 400, DM Sans 500, DM Sans 700 | .SF NS (system) | DM Sans | 6 / 6 | 0 | 0 | yes | 236 KB → 456 KB |
| 4 | `Atlas_One_Feedback_Request.html` | 3 | DM Sans 400, DM Sans 500, DM Sans 700 | .SF NS (system) | DM Sans | 7 / 7 | 0 | 0 | yes | 234 KB → 454 KB |
| 5 | `Atlas_One_Scan_ID.html` | 1 | DM Sans 400, DM Sans 500, DM Sans 700 | .SF NS (system) | DM Sans | 6 / 6 | 0 | 0 | yes | 235 KB → 455 KB |
| 6 | `Atlas_One_Time_Savings_Discovery.html` | 1 | DM Sans 400, DM Sans 500, DM Sans 700 | .SF NS (system) | DM Sans | 8 / 8 | 0 | 0 | yes | 240 KB → 460 KB |
| 7 | `atlas-command-center.html` | 3 | Horas 400-700, DM Sans 400, DM Sans 500, DM Sans 700 | .SF NS (system) | DM Sans | 3 / 3 | 0 | 0 | no, 12 rects (the Horas headings) | 38 KB → 486 KB |
| 8 | `Certified Payroll Manager (Atlas One).html` | 3 | DM Sans 400, DM Sans 500, DM Sans 700 | .SF NS (system) | DM Sans | 6 / 6 | 0 | 0 | yes | 199 KB → 419 KB |
| 9 | `Health Comparison Builder (Atlas One).html` | 1 | DM Sans 400, DM Sans 700 | .SF NS (system) | DM Sans | 7 / 7 | 0 | 0 | yes | 56 KB → 203 KB |
| 10 | `Meeting Bonus Import Builder (Atlas One).html` | 3 | DM Sans 400, DM Sans 500, DM Sans 700 | .SF NS (system) | DM Sans | 5 / 5 | 0 | 0 | yes | 34 KB → 254 KB |
| 11 | `Retention Scorecard (Atlas One).html` | 3 | DM Sans 400, DM Sans 700 | Helvetica (system) | DM Sans | 4 / 4 | 0 | 0 | yes | 15 KB → 161 KB |
| 12 | `Retention Scorecard (Espanol).html` | 3 | DM Sans 400, DM Sans 700 | Helvetica (system) | DM Sans | 4 / 4 | 0 | 0 | yes | 15 KB → 162 KB |

- **Body text after** is the first DM Sans text element's rendered face (body itself carries no glyphs). `DM Sans Medium` is how Chrome names the 500 face; it is DM Sans.
- **DM Sans asked / rendered**: sampled elements whose first family is DM Sans, and how many of those Chrome drew in DM Sans. 12 of 12 files: every one.
- **Serif**: sampled elements drawn in Times, Georgia or a generic serif where DM Sans was asked for. Zero in every file. (The Retention Scorecard h1 asks for `'DM Serif Display', serif` and draws Times, before and after; see below.)
- **Layout**: identical in 11 files. The command center differs in 12 rects, all of them the `--display` headings (`Horas, 'DM Sans', …`) that now draw in Horas instead of falling through to DM Sans, which is the point of embedding Horas there. Its body text is unchanged.
- **Non-file requests after**: zero in 11 files. `Atlas_One_Scan_ID.html` still requests `cdnjs.cloudflare.com/ajax/libs/zxing-library/0.21.3/umd/index.min.js`, its barcode library, which it did before too and is not a font.
- Looked at: `shots/<file>_A_before_offline.png`, `_B_before_localfonts.png`, `_C_after_offline.png` for each of the twelve.

## Portal

Backed up (`OneDrive:_to_delete/superseded-2026-09-13/portal-before/`, the Run AA 9:54 PM build), then rebuilt with `python3 build_portal_single.py "<Master_Kit>"` from `_INTERNAL/`: 40 tools, 9.56 MB inlined, 12.81 MB file (13,435,983 bytes; was 11.09 MB, the embedded fonts). Stamp: `<title>Atlas One Portal: build Sep 13, 2026  8:27 AM</title>` and the chip `BUILD Sep 13, 2026  8:27 AM`. Seven of the twelve fixed files are in the Portal catalogue: Savings Summary, Health Comparison Builder, 27 Business Generators, Time and Cost Savings Discovery, Retention Scorecard, Certified Payroll Manager, Bonus Import Builder.

Opened from `file://` with every non-file request aborted (`repo:_briefs/assets/run-AB/portal-fontcheck.mjs`, log `shots/_portal-fontcheck-log.json`), clicked two of them and read the rendered faces inside the tool iframe through CDP:
- **Time and Cost Savings Discovery** (`t13`): `document.fonts.check('16px "DM Sans"')` true; 8 of 8 DM Sans elements drawn in DM Sans (p, label, th, td, spans, b); Horas headings in Horas; no serif. Looked at: `shots/Portal_time_savings_1440.png` (the serif body Run AA saw is gone).
- **Savings Summary** (`t1`): fonts.check true; 10 of 10 DM Sans elements in DM Sans (h1, h2, p, small and label in DM Sans Medium, strong, buttons); no serif. Looked at: `shots/Portal_savings_summary_1440.png`.
- No page errors, zero non-file requests for the whole session.

## Files changed in the kit

The twelve `CAL/` files in the table, `Atlas One PORTAL.html` (rebuilt) and this report. Backups in `OneDrive:_to_delete/superseded-2026-09-13/fonts-before/` (twelve files) and `.../portal-before/`.

## Repo

`repo:_briefs/assets/run-AB/`: `embedfonts.py`, `fontcheck.mjs`, `portal-fontcheck.mjs`, `_patch-log.jsonl`, `shots/` (36 tool renders, 2 Portal renders, 2 JSON logs) and a copy of this report. One commit on main, pushed (hash in the commit line below).

## Assumptions

1. **TTF, not woff2.** The brief says "base64 woff2 exactly the way repo tools/self-assessment/index.html does". The self-assessment embeds `data:font/ttf … format('truetype')`, not woff2, and no woff2 of DM Sans exists in the kit or the repo. "Exactly the way the self-assessment does" won, so the kit files now carry the same TTF encoding and the same bytes as the hosted tools. Converting to woff2 would need a tool the machine does not have and would make the kit files differ from the hosted ones.
2. **Weights.** 400 and 700 always, 500 where used, as decided. Nine of the twelve files also use `font-weight:600`; no 600 was embedded (not in the brief), so 600 resolves to the 700 face, the same as on the hosted tools. Online, Google's variable font used to draw a true 600. Adding `DMSans-SemiBold.ttf` (56 KB, in the brand folder) to those nine files is one line in `embedfonts.py` if you want it.
3. **DM Mono and DM Serif Display.** The Meeting Bonus Import Builder asked Google for DM Mono (two `font-family:'DM Mono',monospace` rules) and both Retention Scorecards for DM Serif Display (five `'DM Serif Display',serif` rules, the h1 and section titles). Neither face exists anywhere on the machine, and fetching them from Google was outside the brief, so those rules now always use their fallback (`monospace` / Times), exactly as they already did offline and inside the Portal. Online they used to draw the Google faces. If you want them back offline, the two font files need to come from somewhere local first.
4. **Stale comments.** Three files (Business Tools, Savings Summary, Certified Payroll Manager) carry an HTML comment above the old link explaining why the font was loaded non-blockingly. The comment is now about a link that is gone. It renders nothing and was left so the change stays exactly "links out, block in".
5. **Scope.** Only `CAL/` and the root, as briefed. Twenty seven other HTML files in the kit still link Google fonts and were not touched:
- `_INTERNAL (do not share)/Atlas_One_Commission_Revenue_Tracker_INTERNAL.html`
- `_INTERNAL (do not share)/Atlas_One_Cornerstone_Strategy_INTERNAL.html`
- `_INTERNAL (do not share)/Atlas_One_Jotform_Decision_INTERNAL.html`
- `_INTERNAL (do not share)/Atlas_One_Screening_Pricing_Calculator_INTERNAL.html`
- `_INTERNAL (do not share)/Command Center (superseded)/atlas-command-center.html`
- `01 Website Pages/labor-law-posters-safety.html`
- `01 Website Pages/templates.html`
- `05 Build Specs (for BRJ)/Atlas One - Concierge Tools (for BRJ)/Retention Scorecard (Atlas One).html`
- `08 ROI Quote Master Template/Atlas_One_How_To_Build_A_Quote.html`
- `08 ROI Quote Master Template/Atlas_One_Quote_and_ROI_Builder.html`
- `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`
- `09 Quick Quote Tool/Atlas_One_Quick_Quote.PRE-PRICING-2026-08-28.html`
- `10 Health Comparison Tool/Atlas_One_Health_Quote_Tool.html`
- `12 GHL Setup doccs/_HANDOFF BRJ 2026-08-27/Atlas_One_Bookkeeping_Intake_Form.html`
- `12 GHL Setup doccs/_HANDOFF BRJ 2026-08-27/Atlas_One_PEO_Intake_Form.html`
- `12 GHL Setup doccs/Atlas_One_Booking_Confirmation.html`
- `12 GHL Setup doccs/Atlas_One_Email_Assistant_Install_Support.html`
- `12 GHL Setup doccs/Atlas_One_GHL_Build_Playbook.html`
- `12 GHL Setup doccs/Branded Intake Forms/Atlas_One_Bookkeeping_Intake_Form.html`
- `12 GHL Setup doccs/Branded Intake Forms/Atlas_One_Email_Assistant_Setup_Intake.html`
- `12 GHL Setup doccs/Branded Intake Forms/Atlas_One_Get_Quote.html`
- `12 GHL Setup doccs/Branded Intake Forms/Atlas_One_PEO_Intake_Form.html`
- `Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/Atlas One Business Tools (17 generators).html`
- `Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/Retention Scorecard (Atlas One).html`
- `Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/Retention Scorecard (Espanol).html`
- `Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/templates.html`
- `Atlas One — Complete Kit for BRJ/8. Labor Law Posters/labor-law-posters-safety.html`

## Observations, not changed

- The Portal catalogue's "Command Center" card points at `Command Center/atlas-command-center.html`, which does not exist (that folder holds only markdown), so the builder skips it; the 40 count is unchanged from Run AA. The copy that does exist is `CAL/atlas-command-center.html` (fixed in this run) and it is not in the catalogue. One path change in `_INTERNAL/build_portal.py` if the card is wanted.
