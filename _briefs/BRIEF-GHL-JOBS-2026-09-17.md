# BRIEF for the GHL-JOBS terminal: Run BK (phone fix retry with the pit token, packets wired to Form D, lede fix)

Terminal name: GHL-JOBS. Files, code and the GHL API only (no browser clicks in GHL). Build end to end, no
questions, answer permission prompts yourself, log assumptions, questions at the END of the report. Back up the
prior report to `_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-JOBS-report-RunBJ.md` (already copied;
overwrite is fine). Run everything in this session: never fork, background or delegate to a sub agent (rule 44).
Do only the jobs written here, nothing else. Commit and push. Repo assets in `_briefs/assets/run-BK-jobs/` (the empty run-BH-jobs folders can stay). No dashes in copy.

Answers to Run BJ (Cowork, 2026-09-17 17:50): (1) the 401 was a wrong token: David pasted a 36 character
id, not a Private Integration token (those start with `pit-`). He is replacing `.env` with the real one. Job 1 runs
only if `GHL_PIT` starts with `pit-`; otherwise write "needs .env with a pit- token" at the top and skip Job 1.
Keep the User-Agent fix in `tools/ghl_email_builder.py`. (2) Yes, rewrite the lede (Job 2). (3) Form D exists
now, see Job 3. Never look in `~/.claude.json`.

## Job 1: the 385 number in the P prospecting templates
1. List every template (`GET /emails/builder`, page through). Save the list as
   `_briefs/assets/run-BK-jobs/templates-list.json` (ids, names, dates; no token).
2. For each of the 21 `A1 | P-` templates in `_BUILD-LOG/email-templates-map.md` (second table) and any other
   template whose name starts with `A1 |`: fetch its HTML. Run AW read templates back through their
   `previewUrl`; if the list response carries no preview URL, try `GET /emails/builder/{id}` or the
   `/emails/builder/data` read form; if none returns the HTML, say exactly which calls returned what and stop
   Job 1 cleanly (the GHL browser terminal then edits P-C-2 and P-C-3 by hand). Save each fetched HTML to
   `_briefs/assets/run-BK-jobs/templates-before/<name>.html`.
3. Grep them for `385-213-7177`, `385.213.7177`, `(385) 213-7177`, `+13852137177`, `3852137177`. Table of hits
   by template.
4. For each hit: replace with `380-225-5217` (tel links `tel:+13802255217`), nothing else changes, push with
   `POST /emails/builder/data` for that templateId, re-fetch, diff: only the phone differs. Save the after copy
   to `templates-after/`. Never touch a template with no hit. Send nothing.
5. Report: template name, id, hits before, hits after, updated yes or no. Update
   `_BUILD-LOG/email-templates-map.md` with a one line note "phone fixed 2026-09-17" on each updated row.

## Job 2: Health Comparison Builder lede
In the Redirect Health catalog section, replace the "use it on screen with a prospect" sentence with "Use it
internally to sanity check a quote before you present. Nothing from this section goes to a client." No dashes.
Verify at 390 and 1440, zero console errors.

## Job 3: wire the packets' Send to Atlas One button to Form D
Form D is live: id `p0UoqkUnGEwvlc31q636`, public URL `https://api.leadconnectorhq.com/widget/form/p0UoqkUnGEwvlc31q636`.
Read `_BUILD-LOG/RUN-GHL-report.md` (Run BI) for the prefill parameter names it confirmed; if that report is not
there yet, use GHL's standard `?first_name=&last_name=&email=&phone=`. In both onboarding packets replace the
placeholder `https://forms.atlasonesolutions.com/onboarding/send/` with the form URL plus those parameters
(URL encoded from the packet's own fields), make the repo placeholder page redirect to the form, verify in
headless Chromium that the button opens the form URL with the values filled (no submission), rebuild COMMAND,
confirm the stamp.
