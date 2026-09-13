# RUN AA report (terminal B, files only)

Built 2026-09-12 by Claude Code, unattended, no GHL UI, no questions asked. Job: three decided items (Portal note punctuation, NDA Builder logo-control selector, two tools added to the catalogues), then the Portal rebuild. Scripts, captures and renders in `repo:_briefs/assets/run-AA/`. Nothing sent, nothing deployed, nothing deleted (every file changed in the kit was copied, byte identical, to `OneDrive:_to_delete/superseded-2026-09-12/run-AA-before/` first).

Paths are relative to `HR_Docs/Atlas_One_Master_Kit/` unless marked `repo:` (atlas-one-intake-forms, main, pushed), `OneDrive:` (the OneDrive-AtlasOneSolutions root) or `_INTERNAL/` (`_INTERNAL (do not share)/`). `CAL/` is `06 Calculators and Tools (NEW Aug 2026)/`.

## What was done

1. **Portal note, em dash to period.** `_INTERNAL/build_portal_single.py` line 277 now reads `it. Nothing loads from a folder, a server or the internet.` (was `it — nothing loads ...`). One line changed in the builder (diff against the backup shows only line 277). The rebuilt Portal's landing note reads "This file is self-contained. All 40 tools live inside it. Nothing loads from a folder, a server or the internet. Copy it anywhere, email it to yourself, put it on a phone or iPad, open it on a plane. It behaves the same everywhere." No em dash is left in that paragraph.

2. **NDA Builder, one-token fix.** `CAL/NDA Builder (Atlas One).html` line 779: `FORM_SEL = ".panel.form"` (was `".panel-form"`). Diff against the backup shows only that line. Cause: the form pane's class is `panel form` (two classes), so `.panel-form` matched nothing and the logo module fell back to its `position:fixed; top:12px; right:12px` box, which sat on top of the CTA banner.
   - Before (backup file, `repo:_briefs/assets/run-AA/shots/_nda-before-log.json`): control `position:fixed`, not inside the form; `elementFromPoint` at the centre of "Book a call" returned the logo control at 390 px and the logo label at 1440 px, i.e. the button was covered.
   - After (`_nda-after-log.json`): control `position:static`, inside `.panel.form`, slotted directly after the "Save your work" block (at 390 px: top 590, 358 wide; at 1440 px: top 329, 613 wide, inside the 670 px form pane); `elementFromPoint` at the centre of "Book a call" returns the button itself at both widths. scrollWidth 390 at 390 px and 1440 at 1440 px, no JavaScript errors.
   - Looked at: `repo:_briefs/assets/run-AA/shots/NDA_Builder_after_390_top.png` and `NDA_Builder_after_1440_top.png` (viewport), `NDA_Builder_after_390.png` and `NDA_Builder_after_1440.png` (full page), plus the `_before_` set. In both "after" shots the "Add your company logo / Upload" control is the second block in the left pane and "Email David" / "Book a call" are clear in the banner.

3. **Two tools added to the catalogues.**
   - `_INTERNAL/build_portal.py`: `CAL/Atlas_One_Time_Savings_Discovery.html` added to **Calculators & Diagnostics** as "Time and Cost Savings Discovery" (after the Back Office Self-Assessment, no badge, blurb mentions the live copy at forms.atlasonesolutions.com/tools/time-savings/); `CAL/Atlas_One_Onboarding_Tracker.html` added to **Quoting & Proposals** as "Prospect Onboarding Tracker" with the **Internal** badge (last card in that section, after the COI → WC estimator). The file still parses (`ast.parse`).
   - `Atlas One — Tools Hub.html`: "Time and Cost Savings Discovery" added to **Diagnostics & Savings**, tag `new`, after the Back Office Self-Assessment; the Hub's count is computed (`TOOLS.length`) and now reads "29 tools" (was 28). The card renders in that category and its href (`06%20Calculators...%2FAtlas_One_Time_Savings_Discovery.html`, decoded) resolves to the file. The Onboarding Tracker was **not** added to the Hub. Looked at: `repo:_briefs/assets/run-AA/shots/Tools_Hub_1440.png`, log `_hub-log.json`.

4. **Portal rebuilt** with `python3 build_portal_single.py "<Master_Kit>"` from `_INTERNAL/`. Output: 40 tools (was 38), 8.27 MB inlined, 11.09 MB file (11,632,915 bytes). Stamp: `<title>Atlas One Portal: build Sep 12, 2026  9:54 PM</title>` and the build chip `BUILD Sep 12, 2026  9:54 PM` (previous build was 9:29 PM, 38 tools). Checked headless from `file://` with the network blocked (`repo:_briefs/assets/run-AA/portal-check.mjs`, log `shots/_portal-log.json`):
   - Home grid shows 40 cards. Search placeholder "Search 40 tools…".
   - Clicking **Prospect Onboarding Tracker** (card `t6`, INTERNAL chip, Quoting & Proposals) turns the frame on, the pill strip highlights it, and the document inside the iframe has title "Atlas One: Prospect Onboarding Tracker", 45,927 body characters and 217 inputs/selects/textareas. Looked at: `shots/Portal_onboarding_tracker_1440.png`.
   - Clicking **Time and Cost Savings Discovery** (card `t13`, Calculators & Diagnostics) does the same: inner title "Atlas One: Time & Cost Savings Discovery", h1 "What are they doing by hand today?", 44 inputs, hero numbers 251 hours / $8,785 / $8,785 with the defaults. Looked at: `shots/Portal_time_savings_1440.png`.
   - No page errors. The previous Portal (9:29 PM build) is at `OneDrive:_to_delete/superseded-2026-09-12/run-AA-before/Atlas One PORTAL.html`.

## Files changed in the kit

| File | Change |
|---|---|
| `_INTERNAL/build_portal_single.py` | line 277, em dash to period |
| `_INTERNAL/build_portal.py` | two catalogue entries (lines 43–44, 59–60) |
| `CAL/NDA Builder (Atlas One).html` | line 779, `FORM_SEL` |
| `Atlas One — Tools Hub.html` | one `TOOLS` entry (line 272) |
| `Atlas One PORTAL.html` | rebuilt, 9:54 PM stamp, 40 tools |
| `_BUILD-LOG/RUN-AA-report.md` | this report |

Backups of the five changed files (before state) in `OneDrive:_to_delete/superseded-2026-09-12/run-AA-before/`, each checked with `cmp` at copy time.

## Repo

`repo:_briefs/assets/run-AA/`: `nda-check.mjs`, `portal-check.mjs`, `hub-check.mjs`, `shots/` (NDA before/after at 390 and 1440, Portal home and both new tools, Tools Hub, the four JSON logs), and a copy of this report. One commit on main, `b25c946`, pushed.

## Assumptions

1. The `find` command returns two kits; `grep -vi _to_delete` does not exclude `Desktop/Atlas One Builds/_TO DELETE (stale kit)/` because that folder name has a space, not an underscore. The OneDrive kit (`HR_Docs/Atlas_One_Master_Kit`) was used; the Desktop one was not touched.
2. Section for the Onboarding Tracker in the Portal: the decision said "Portal only (internal)" without naming a section. It went into **Quoting & Proposals** (it records what the prospect signed up for, pricing and deal terms, calls and the setup-team handoff), with the same `Internal` badge the Quick Quote and Command Center carry. Moving it to another section is a one-line change in `build_portal.py`.
3. Blurbs were written from the tools' own hero copy. Portal blurbs read for David ("Fill in with the prospect", "what they signed up for"); the Hub blurb reads for the prospect ("the tasks you still do by hand"), matching the voice of the other Hub cards.
4. Backups went to the Run Z folder pattern (`OneDrive:_to_delete/superseded-2026-09-12/`) in a `run-AA-before/` subfolder so they do not mix with Run Z's files.

## Observation, not changed

- The kit copy of `Atlas_One_Time_Savings_Discovery.html` still carries a `<link>` to Google Fonts (DM Sans), so with no network the body falls back to a serif face inside the Portal (visible in `Portal_time_savings_1440.png`, which was rendered offline). Twelve other kit tools have the same link; the hosted copy (`repo:tools/time-savings/index.html`) embeds the fonts. Outside the three decided items, so left as is. If the Portal is meant to look right on a plane, embedding DM Sans in the kit copy the way Run Y did for the hosted one is the fix.
