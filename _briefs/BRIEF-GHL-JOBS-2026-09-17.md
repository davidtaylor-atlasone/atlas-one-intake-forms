# BRIEF for the GHL-JOBS terminal: Run BJ (the P prospecting templates phone fix, token from .env)

Terminal name: GHL-JOBS. Files, code and the GHL API only (no browser clicks in GHL). Build end to end, no
questions, answer permission prompts yourself, log assumptions, questions at the END of the report. Back up the
prior report to `_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-JOBS-report-RunBI.md` (already copied;
overwrite is fine). Run everything in this session: never fork, background or delegate to a sub agent (rule 44).
Do only the jobs written here, nothing else. Commit and push. Repo assets in `_briefs/assets/run-BJ-jobs/` (the empty run-BH-jobs folders can stay). No dashes in copy.

Answers to Run BH's question (Cowork, 2026-09-17 08:50): option (b). David is placing the token in
`~/Projects/atlas-one-intake-forms/.env` as one line `GHL_PIT=<token>`; `.env` is now in `.gitignore` (Cowork
added it). Read it with `python-dotenv` or a two line parser; never print it, never write it to any file, log,
report or brief; never look in `~/.claude.json` again. If `.env` is missing or the variable is empty, stop Job 1
cleanly with the message "needs .env with GHL_PIT" at the top of the report. If the API answers 401, report the
exact scope text; the GHL browser terminal then edits by hand. The call sequence is in
`_briefs/assets/run-AW/RUN-GHL-JOBS-report.md` (create `POST /emails/builder` with `title`; fill
`POST /emails/builder/data` with `editorType:"html"`, `html`; list `GET /emails/builder`; delete
`DELETE /emails/builder/{locationId}/{id}`; location AzTPxnK2vSUj19jYoDmR; `Version: 2021-07-28`). Save the helper
as `tools/ghl_email_builder.py` (reads `.env`, functions list, fetch_html, create, fill, delete).

## Job 1: the 385 number in the P prospecting templates
1. List every template (`GET /emails/builder`, page through). Save the list as
   `_briefs/assets/run-BJ-jobs/templates-list.json` (ids, names, dates; no token).
2. For each of the 21 `A1 | P-` templates in `_BUILD-LOG/email-templates-map.md` (second table) and any other
   template whose name starts with `A1 |`: fetch its HTML. Run AW read templates back through their
   `previewUrl`; if the list response carries no preview URL, try `GET /emails/builder/{id}` or the
   `/emails/builder/data` read form; if none returns the HTML, say exactly which calls returned what and stop
   Job 1 cleanly (the GHL browser terminal then edits P-C-2 and P-C-3 by hand). Save each fetched HTML to
   `_briefs/assets/run-BJ-jobs/templates-before/<name>.html`.
3. Grep them for `385-213-7177`, `385.213.7177`, `(385) 213-7177`, `+13852137177`, `3852137177`. Table of hits
   by template.
4. For each hit: replace with `380-225-5217` (tel links `tel:+13802255217`), nothing else changes, push with
   `POST /emails/builder/data` for that templateId, re-fetch, diff: only the phone differs. Save the after copy
   to `templates-after/`. Never touch a template with no hit. Send nothing.
5. Report: template name, id, hits before, hits after, updated yes or no. Update
   `_BUILD-LOG/email-templates-map.md` with a one line note "phone fixed 2026-09-17" on each updated row.

## Job 2: answers to Run BI, small follow ups
Answers to Run BI's questions: (1) the Redirect Health catalog viewer stays vendor specific and internal only;
add the words "INTERNAL, never client facing" to its page header if they are not there. (2) The Benefits &
Retirement sheet stays a print sheet; no change. (3) Give the internal row the title "Build request inbox
(internal)" in catalogue.py so the two rows differ, rebuild COMMAND, confirm the stamp. (4) Agreed; this brief
carries the rule at the top.

## Job 3: wire the packets' Send to Atlas One button to Form D
If `_BUILD-LOG/RUN-GHL-report.md` is a Run BI report that lists a Form D id and public URL (Part 33), replace the
placeholder `https://forms.atlasonesolutions.com/onboarding/send/` in both onboarding packets with
`https://api.leadconnectorhq.com/widget/form/<id>` plus the prefill query parameters the GHL report names; keep
the placeholder page in the repo but make it redirect to the form. Rebuild COMMAND. If the GHL report is not
there yet, skip this job and say so.

## Report
Built, Verification (the hits table, one before and after diff quoted), Assumptions, Skipped, Questions.
