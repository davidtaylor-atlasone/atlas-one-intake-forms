# RUN-GHL-JOBS report: Run BM

Terminal: GHL-JOBS (files, code and the GHL API only, no browser). All four jobs in the brief done. Zero hard
stops. Report copied to repo `_briefs/assets/run-BM-jobs/RUN-BM-report.md`.

## Job 1: two contact custom fields for the portal

Read all contact custom fields first (`GET /locations/{id}/customFields`): no existing "Portal Switches" or
"Portal Favorites" field, no `portal_switches` or `portal_favorites` key, so nothing to skip.

Found the existing `services` field's folder (`parentId AmY51esJO2QF0v3wvODu`) and created two new Contact
fields there, type `LARGE_TEXT`:

- **Portal Switches**: id `zUZ55MT5SCj5nFCj0yYK`, key `contact.portal_switches` (201)
- **Portal Favorites**: id `Va0mTobvO3OloAmuFv6T`, key `contact.portal_favorites` (201)

Response JSON (ids and keys, no token) saved to repo `_briefs/assets/run-BM-jobs/portal-fields.json`.

Opened `~/Projects/atlas-one-portal/server/fields.ts`: its `KNOWN_IDS` map reads `GHL_FIELD_PORTAL_SWITCHES`
and `GHL_FIELD_PORTAL_FAVORITES` as field **ids** (not keys) -- `fieldValue()` looks a contact's custom field up
by `x.id === id`. Appended both env lines to `~/Projects/atlas-one-portal/.env` (not committed, matches the
repo's existing `.env` convention: it already held only secrets like the GHL token and session secret, no prior
`GHL_FIELD_*` lines to replace).

Checked `scripts/deploy-azure.sh`: it only zips `dist`, `dist-server` and `package.json` and pushes that zip
with `az webapp deploy`. It never reads or pushes `.env`, so the two new variables will not reach Azure on the
next deploy by themselves. Wrote `_BUILD-LOG/portal-env-additions-2026-09-18.md` telling David to add them by
hand in the Azure Portal (App Service `atlas-one-portal`, resource group `atlas-one-ai-email-assistant-v2`,
Settings > Environment variables, Apply) -- a one-time step, they persist across future deploys.

## Job 2: the real Vertical options

Same customFields read found the Vertical field (Prospecting folder): id `gZn8B7wJU1zXDuKYrNoi`, key
`contact.vertical`. Wrote every option, exactly as GHL returns it, to `_BUILD-LOG/ghl-vertical-options.md`
(id and key at the top, 20 options below). The live set today is actually two overlapping generations of
options (an older 7 option set and a newer 13 option set with different spellings for similar meanings, e.g.
"Professional Services" vs "Professional services (law, accounting, agencies)") -- the brief said write every
option exactly spelled, so all 20 went in verbatim, no merging or pruning.

## Job 3: laptop mark on the front door and the forms index

Found the periwinkle logo mark at `A1_Final Brand/1. Logos/Logo Mark/Full Color/Web/`, took the SVG
(`atlas-one-solutions-logo-mark-full-color-rgb.svg`, fill `#788de3`, transparent background). Copied it into
the forms repo as `assets/atlas-one-mark.svg`. In both `index.html` and `start/index.html`, replaced the
periwinkle "A1" square (`<div class="mark">A1</div>` on a `background:var(--peri)` box) with an `<img>` of the
real mark at the same box size, wordmark text kept beside it as before.

Verified with headless Chromium (the project's Playwright install) at 390 and 1440 for both pages: `scrollWidth`
equals the viewport width at both sizes, zero console errors, zero `pageerror` events. The only non `file://`
requests on either page are the pre-existing Google Fonts calls both pages already made before this job (an
online-only exception Run BL already logged for `start/index.html`; `index.html` had the same Google Fonts link
already in place too, not something this job added). Screenshots:
`_briefs/assets/run-BM-jobs/shots/index-390.png`, `index-1440.png`, `start-390.png`, `start-1440.png`.

## Job 4: two small COMMAND fixes, then rebuild

`catalogue.py`: the "Prospect Pitch Deck" row's (`id prospect-pitch-deck`) blurb changed from `"pptx."` to
`"The 16 slide prospect deck (pptx). Present it; do not email it. The 9 slide First Meeting cut is the PDF
below."`, matching the brief's text verbatim.

`build_command.py`: `row_html()`'s `kind_icon` map had `"deck": "&#128200;"` (a colorful chart-trending emoji,
red line included) for every pptx row. Changed to `"deck": "&#9638;"` (a plain geometric glyph, square with
orthogonal crosshatch fill), which -- like the other kind icons -- inherits `.ricon`'s periwinkle text color
instead of carrying its own built-in emoji colors. Four colours only, confirmed by eye in the screenshot below.

Ran `catalogue_check.py "$MK"`: OK, 196 entries, all paths resolve. Backed up both prior build outputs (`Atlas
One COMMAND.html`, `A1_Sales/Atlas One Sales Kit.html`) to
`_to_delete/superseded-2026-09-18/before-runBM-job4/` before rebuilding. Rebuilt with
`python3 build_command.py "$MK"`: `Atlas One COMMAND.html` 196 items, stamp "Sep 17, 2026 10:03 PM"; `Atlas One
Sales Kit.html` 56 items, same stamp.

Rendered `Atlas One COMMAND.html` headless at 1440, unlocked the Internal zone (`sessionStorage
a1cmd_unlocked_internal=1`, the client side passphrase curtain, not a security bypass), searched for "Prospect
Pitch Deck" and screenshotted the row: new blurb text confirmed verbatim, icon renders as the plain periwinkle
glyph, zero console errors. Screenshots: `_briefs/assets/run-BM-jobs/shots/command-prospect-pitch-deck-row.png`,
`command-full.png`.

## Files touched

- GHL: two new Contact custom fields created (Job 1), no fields deleted or modified.
- `~/Projects/atlas-one-portal/.env`: two lines appended (not committed).
- `_BUILD-LOG/portal-env-additions-2026-09-18.md`: new, Azure instructions for David.
- `_BUILD-LOG/ghl-vertical-options.md`: new.
- Forms repo (`~/Projects/atlas-one-intake-forms`, committed and pushed):
  - `assets/atlas-one-mark.svg` (new)
  - `index.html`, `start/index.html` (mark swapped in)
  - `tools/ghl_custom_fields.py` (new helper, list/create custom fields)
  - `_briefs/BRIEF-GHL-JOBS-2026-09-17.md`, `_briefs/assets/run-BM-jobs/*` (brief copy, field creation JSON,
    screenshots)
- Master Kit `_INTERNAL (do not share)/catalogue.py`: one blurb string changed.
- Master Kit `_INTERNAL (do not share)/build_command.py`: one icon mapping changed.
- Master Kit `Atlas One COMMAND.html`, `A1_Sales/Atlas One Sales Kit.html`: rebuilt (generated output, not hand
  edited).
- Prior COMMAND and Sales Kit outputs backed up to
  `_to_delete/superseded-2026-09-18/before-runBM-job4/`.
- Prior `RUN-GHL-JOBS-report.md` (Run BL's) backed up to
  `_to_delete/superseded-2026-09-18/prior-reports/RUN-GHL-JOBS-report-RunBL.md`.

## Assumptions

1. Job 1's folder for the two new fields: the brief said use the folder the existing `services` field lives in.
   Read that field's `parentId` (`AmY51esJO2QF0v3wvODu`) directly from the API response and used it, rather than
   guessing a folder name.
2. Job 1's env format: the brief said open `fields.ts` and use what it expects (id or key). It expects field
   ids, confirmed by reading `KNOWN_IDS` and `fieldValue()`'s `x.id === id` lookup. Used the ids, not the keys.
3. Job 1's deploy note: since `deploy-azure.sh` never touches `.env`, wrote the Azure Portal manual steps as the
   brief's fallback instructed, rather than assuming a script would carry the new variables.
4. Job 2: the Vertical field currently holds two generations of options that overlap in meaning but differ in
   exact wording. The brief said write every option exactly spelled with no instruction to dedupe or reconcile,
   so all 20 went into the file untouched. Flagged below as a question, since the duplication looks like it
   might be worth cleaning up in GHL itself at some point.
5. Job 3: no laptop specific glyph exists at the path in the brief or elsewhere checked; that path holds the
   company's one periwinkle logo mark (an abstract shape, not literally a laptop), which is what "the periwinkle
   laptop mark" in the brief most plausibly refers to (a colloquial name for the mark, not a literal laptop
   icon). Used it as instructed.
6. Job 3: kept the pre-existing Google Fonts `<link>` on both pages as is; the brief's "works from file:// with
   no network" rule is stated for CLAUDE.md's general HTML tools, and both these front-door pages were already
   online-only pages before this job (index.html already had the same Google Fonts link; Run BL logged the same
   exception for `start/index.html`). Not treated as a new violation to fix, since neither page's font loading
   was part of this job's scope.
7. Job 4's icon replacement: picked `&#9638;` (a plain geometric block glyph) as a monochrome stand in for the
   pptx/deck icon, since the brief asked for "a plain periwinkle CSS glyph like the other kinds" without naming
   a specific character. Confirmed by screenshot that it renders in periwinkle, not multi-color.

## Questions for David

1. The Vertical field in GHL currently has two overlapping generations of options (7 older + 13 newer, e.g.
   "Professional Services" vs "Professional services (law, accounting, agencies)"). Want the old 7 removed from
   the live field in GHL, or left as is for now? `ghl-vertical-options.md` lists all 20 as they exist today; no
   changes were made to the field itself in this run.
2. Once you've added the two `GHL_FIELD_PORTAL_SWITCHES` / `GHL_FIELD_PORTAL_FAVORITES` values in Azure App
   Service settings (see `portal-env-additions-2026-09-18.md`), does the portal app need a restart to pick them
   up, or does it read env vars fresh on next request? Wanted to flag it rather than assume.
