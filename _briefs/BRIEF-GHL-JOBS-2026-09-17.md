# BRIEF for the GHL-JOBS terminal: Run BH (the P prospecting templates phone fix, with the token pointer this time)

Terminal name: GHL-JOBS. Files, code and the GHL API only (no browser clicks in GHL). Build end to end, no
questions, answer permission prompts yourself, log assumptions, questions at the END of the report. Back up the
prior report to `_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-JOBS-report-RunBG.md` (already copied;
overwrite is fine). Commit and push. Repo assets in `_briefs/assets/run-BH-jobs/`. No dashes in copy.

Answers to Run BG's questions (Cowork, 2026-09-17 08:35):
1. The token exists and Run AW used it. It is NOT in a .env or the keychain. It is in `~/.claude.json` under
   `projects` > `/Users/davidtaylor` > `mcpServers` > `gohighlevel` > `headers.Authorization` (a Bearer header
   for https://services.leadconnectorhq.com/mcp/). Run AV's report documented this in its "How the API access
   worked, for next time" section (`_briefs/assets/run-AV/RUN-AV-report.md`); the pointer is also in
   `_INTERNAL (do not share)/GHL-click-guide-FormB-FormC-2026-08-29.md`. Read the token from that file at run
   time with a small Python snippet; never copy it into the repo, a log, a report or a brief.
2. Run AW's report is at `_briefs/assets/run-AW/RUN-GHL-JOBS-report.md` in this repo (it was never in
   `_to_delete`; Cowork's pointer was wrong). It has the exact two call sequence: `POST /emails/builder`
   (create, `title`), `POST /emails/builder/data` (fill, `editorType:"html"`, `html`), `GET /emails/builder`
   (list), `DELETE /emails/builder/{locationId}/{id}`. Location AzTPxnK2vSUj19jYoDmR, `Version: 2021-07-28`.
   Save a reusable helper as `tools/ghl_email_builder.py` in the repo (reads the token from ~/.claude.json,
   functions list, get_html_by_preview, create, fill, delete) so no run rederives this again.

## Job 1: the 385 number in the P prospecting templates
1. List every template (`GET /emails/builder`, page through). Save the list as
   `_briefs/assets/run-BH-jobs/templates-list.json` (ids, names, dates; no token).
2. For each of the 21 `A1 | P-` templates in `_BUILD-LOG/email-templates-map.md` (second table) and any other
   template whose name starts with `A1 |`: fetch its HTML. Run AW read templates back through their
   `previewUrl`; if the list response carries no preview URL, try `GET /emails/builder/{id}` or the
   `/emails/builder/data` read form; if none returns the HTML, say exactly which calls returned what and stop
   Job 1 cleanly (the GHL browser terminal then edits P-C-2 and P-C-3 by hand). Save each fetched HTML to
   `_briefs/assets/run-BH-jobs/templates-before/<name>.html`.
3. Grep them for `385-213-7177`, `385.213.7177`, `(385) 213-7177`, `+13852137177`, `3852137177`. Table of hits
   by template.
4. For each hit: replace with `380-225-5217` (tel links `tel:+13802255217`), nothing else changes, push with
   `POST /emails/builder/data` for that templateId, re-fetch, diff: only the phone differs. Save the after copy
   to `templates-after/`. Never touch a template with no hit. Send nothing.
5. Report: template name, id, hits before, hits after, updated yes or no. Update
   `_BUILD-LOG/email-templates-map.md` with a one line note "phone fixed 2026-09-17" on each updated row.

## Job 2: nothing else. Do not rebuild COMMAND (no Master Kit tool changed).

## Report
Built, Verification (the hits table, one before and after diff quoted), Assumptions, Skipped, Questions.
