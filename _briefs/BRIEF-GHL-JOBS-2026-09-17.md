# BRIEF for the GHL-JOBS terminal: Run BM (portal custom fields by API, Vertical options file, laptop mark on the front door, COMMAND blurb fix)

Terminal name: GHL-JOBS. Files, code and the GHL API only (no browser clicks in GHL). Build end to end, no
questions, answer permission prompts yourself, log assumptions, questions at the END of the report. Prior
report already backed up to `_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-JOBS-report-RunBL.md`.
Never fork, background or delegate to a sub agent (rule 44). Do only the jobs written here. Commit and push.
Repo assets in `_briefs/assets/run-BM-jobs/`. No dashes in copy. Log to `TERMINAL-GHL-JOBS-live.md`; report to
`RUN-GHL-JOBS-report.md` (quoted heredoc).

Token: `GHL_PIT` in `~/Projects/atlas-one-intake-forms/.env` (starts with `pit-`). Never print or log it, never
look in `~/.claude.json`. Location `AzTPxnK2vSUj19jYoDmR`, `Version: 2021-07-28`, browser User-Agent (the
Cloudflare fix from Run BK). Master Kit: find by name (`MK=$(find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null
| grep -vi -e _to_delete -e archiv | head -1)`). A1_Sales is `$MK/../../A1_Sales` (beside HR_Docs, Run BL confirmed).

## Job 1: two contact custom fields for the portal (Run P2 asked for them)
Custom Fields API (`GET /locations/{id}/customFields`, `POST /locations/{id}/customFields`). Read first: if a
field with name "Portal Switches" or "Portal Favorites" (or key `portal_switches` / `portal_favorites`) already
exists, do not create a second one. Otherwise create two Contact fields, type large text (multi line), names
"Portal Switches" and "Portal Favorites", in the folder the existing portal field `services` lives in (read
that field to find its folder; if none, the default folder). Save the response JSON (ids and keys, no token)
to `_briefs/assets/run-BM-jobs/portal-fields.json`. Then in `~/Projects/atlas-one-portal/.env` (David's
machine, same home) add or replace the two lines `GHL_FIELD_PORTAL_SWITCHES=<id>` and
`GHL_FIELD_PORTAL_FAVORITES=<id>` (Run P2's report names these env variables; open
`~/Projects/atlas-one-portal/server/fields.ts` to confirm the exact names and whether it expects the field id
or the key, and use what it expects). Do not commit `.env`. Also write the same two lines into
`_BUILD-LOG/portal-env-additions-2026-09-18.md` so the Azure app settings can be updated by David (the report
tells him: Azure portal, App Service atlas-one-portal, Settings, Environment variables, add the two names and
values, Apply; or note if `scripts/deploy-azure.sh` already pushes `.env` values, read it and say which).

## Job 2: the real Vertical options
`GET /locations/{id}/customFields`, find the contact field named "Vertical" (Prospecting folder). Write every
option, exactly spelled, one per line, to `_BUILD-LOG/ghl-vertical-options.md` with the field id and key at
the top. The PORTAL terminal keys its industry starter set on this file.

## Job 3: laptop mark on the front door and the forms index
The periwinkle laptop mark exists: `$MK/A1_Final Brand/1. Logos/Logo Mark/Full Color/Web/` (pick the SVG if there is
one, else the largest PNG). Copy it into the forms repo as `assets/atlas-one-mark.svg` (or `.png`) and use it in the
hero of `start/index.html` and `index.html` in place of the periwinkle "A1" square (keep the wordmark text
beside it). Verify both pages at 390 and 1440, zero console errors, screenshots to
`_briefs/assets/run-BM-jobs/shots/`. Commit and push.

## Job 4: two small COMMAND fixes, then rebuild
In `catalogue.py`: the "Prospect Pitch Deck" row's blurb is just "pptx."; make it "The 16 slide prospect deck
(pptx). Present it; do not email it. The 9 slide First Meeting cut is the PDF below." The row icon for pptx
rows renders a red chart emoji; use a plain periwinkle CSS glyph like the other kinds (four colours only).
Rebuild COMMAND and the Sales Kit (`python3 build_command.py "$MK"`), confirm the stamps show today,
`catalogue_check.py` OK, one screenshot each.

## Report
Field ids created or found, the Vertical options file path and count, which env names fields.ts expects and
what you wrote where, the mark file used, screenshots, assumptions, "Questions for David" at the end.
