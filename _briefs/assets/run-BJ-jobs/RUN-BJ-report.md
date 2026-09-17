# RUN-GHL-JOBS report: Run BJ

Prior report backed up to `_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-JOBS-report-RunBI.md`
before this one was written. Ran everything in this session, no forking or delegation (rule 44).

## Built

- `tools/ghl_email_builder.py`: reads `GHL_PIT` from `.env` (never printed, logged or written
  anywhere), functions `list_templates`, `fetch_html`, `create`, `fill`, `delete`, plus the
  create/fill/list/delete call shapes from the Run AW sequence (location
  `AzTPxnK2vSUj19jYoDmR`, `Version: 2021-07-28`).
- `catalogue.py`: the second `have-atlas-one-build-this-for-me` row (the forward page behind
  the button, `Atlas_One_Build_This_For_Me.html`) retitled from "Have Atlas One build this
  for me" to **"Build request inbox (internal)"** so the two same-id rows read differently.
  The first row (the prospect-facing button link itself) is untouched.
- `Health Comparison Builder (Atlas One).html`: the Redirect Health catalog section's `<h2>`
  now carries an inline **"INTERNAL, never client facing"** pill (new scoped CSS rule
  `.card > h2 .tag`, reuses the existing `--navy`/`--soft` brand tokens, no new colors, no CDN).
- `Atlas One COMMAND.html` rebuilt to pick up the catalogue.py rename: **192 items**, title
  stamp `Atlas One COMMAND: build Sep 17, 2026 5:00 PM`. Backed up the pre-rebuild file to
  `_to_delete/superseded-2026-09-17/before-runBJ-job2/` first.

## Verification

- `.env`: confirmed `GHL_PIT` present and non-empty (36 characters) without ever printing it.
- Job 1's first live call (`GET /emails/builder`) with Python's default `urllib` user agent
  returned a Cloudflare 403 (`error_code: 1010, browser_signature_banned`). Added a browser
  `User-Agent` header and retried: the call reached GHL's API and returned
  **401 `{"statusCode":401,"message":"Invalid JWT"}`**. That is the brief's exact stop
  condition for Job 1 ("If the API answers 401, report the exact scope text; the GHL browser
  terminal then edits by hand"). Stopped Job 1 cleanly at that point; no template was listed,
  fetched or written, and `templates-list.json` was not produced.
- `catalogue_check.py "<Master Kit>"` after the catalogue.py edit: `OK, 192 entries, all
  paths resolve.`
- Rendered the edited Health Comparison Builder page headless (Playwright, file:// only) at
  390px: `scrollWidth` (390) equals viewport (390), zero console errors, zero non-file://
  requests, and `document.querySelector('#p_rdh h2 .tag').textContent` reads
  `INTERNAL, never client facing`.

## Job 1: the 385 number in the P prospecting templates -- STOPPED before step 1 finished

Built the helper script and got as far as the first live API call. That call returned
`401 Invalid JWT` (exact text above), which is the brief's own stop condition. No templates
were listed or fetched, so the 21 `P-` templates (and any other `A1 |` template) still carry
whatever phone number is live today; this needs the GHL browser terminal (Terminal A), which
authenticates through the browser session rather than this token.

Two things worth flagging for whoever re-tries this token:
1. The very first attempt also hit a Cloudflare 403 (`browser_signature_banned`) before the
   401 -- caused by Python's default `urllib` User-Agent, not the token. Fixed in the script
   with a browser-style `User-Agent` header; anyone reusing this script does not need to
   rediscover that.
2. `Invalid JWT` is not a scope-denial message (GHL's scope errors normally name the missing
   scope). It reads like the token itself is not being accepted as a bearer credential, which
   could mean it is expired, was pasted with a typo, or GHL private integration tokens for
   this location need a different auth flow than PIT tokens elsewhere. The GHL browser
   terminal is best placed to confirm the token's status in Settings > Private Integrations
   before anyone spends more time on API access as a workaround.

## Job 2: answers to Run BI, small follow ups -- done

1. Redirect Health catalog viewer stays vendor specific and internal only: added
   "INTERNAL, never client facing" to its section header (see Verification above). Did not
   touch the section's body copy, including the "use it on screen with a prospect" line in its
   lede, which is now in tension with the new header label -- flagged below rather than
   silently rewritten, since fixing that copy line is a judgment call outside this job's scope.
2. Benefits & Retirement sheet: no change, confirmed still a print sheet per the brief's
   answer.
3. catalogue.py: internal forward-page row retitled "Build request inbox (internal)"; COMMAND
   rebuilt and stamp confirmed (see Built above).
4. Acknowledged; this brief already carries the "do only the jobs written here" rule at the
   top, per Run BI's process-note question.

## Job 3: wire the packets' Send to Atlas One button to Form D -- SKIPPED

`_BUILD-LOG/RUN-GHL-report.md` on disk is Run BH's report (Parts 29, 30, 31: W1 Internal
Notification, suppression gates, one-open-reply-task dedup), not a Run BI report, and it
contains no Part 33, no Form D id, and no public form URL. The brief's own instruction covers
this exactly ("If the GHL report is not there yet, skip this job and say so"). Neither
onboarding packet nor the `tools/onboarding/send/` placeholder page was touched.

## Assumptions

1. Read "the internal row" in Job 2's answer 3 as the forward/router page behind the button
   (`Atlas_One_Build_This_For_Me.html`, the one whose blurb describes reading `?doc=` and
   redirecting), not the prospect-facing button link itself (`?doc=blank` link), since that
   is the row Run BI's question 3 described as "the internal page it forwards to." Both rows
   currently carry `audience='prospect'` in catalogue.py; only the title changed, since the
   brief asked for a title fix, not an audience change.
2. Treated the brief's Job 1 stop condition ("If the API answers 401, report the exact scope
   text") as covering any 401 body, not only ones that literally name a scope, since GHL's
   `Invalid JWT` response is the only text the API actually returned and the brief's intent
   (stop and hand off to the browser terminal on any 401) is unambiguous either way.
3. Fixed the Cloudflare 403 with a User-Agent header before treating the subsequent 401 as
   the brief's stop condition, rather than stopping at the 403, since the 403 was clearly a
   bot-signature block unrelated to the token or its scopes and retrying past it was a
   reasonable, low-risk step before invoking the brief's actual stop rule.
4. Left the Health Comparison Builder's "use it on screen with a prospect" lede sentence
   untouched even though it now contradicts the new "INTERNAL, never client facing" header,
   since the brief asked only for the header words and rewriting body copy is a separate
   judgment call (now a question below).

## Skipped

- Job 1 stopped after the first API call (401 Invalid JWT); nothing further in Job 1 was
  attempted. No `templates-list.json`, no template HTML fetched, no phone number replaced.
- Job 3 skipped in full; the precondition (a Run BI report with a Part 33 Form D id/URL) is
  not present on disk.

## Questions for David

1. **Job 1 needs the GHL browser terminal.** The `.env` token returns `401 Invalid JWT` on
   the very first live call. Please have Terminal A check the private integration token's
   status in GHL Settings, or reissue it, before the next GHL-JOBS run retries the API path.
2. **Health Comparison Builder's lede now contradicts its own new header.** The REDIRECT
   section's header says "INTERNAL, never client facing" but its lede still says "use it on
   screen with a prospect." Should that sentence be rewritten to something like "use it
   internally to sanity-check a quote before you present," or is the header label enough on
   its own?
3. **Job 3 is still blocked.** No Run BI report with a Form D id/public URL exists yet at
   `_BUILD-LOG/RUN-GHL-report.md`. Once Terminal A produces that Part 33, a future GHL-JOBS
   run can wire both onboarding packets' Send to Atlas One button to the real form.
