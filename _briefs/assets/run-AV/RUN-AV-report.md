# RUN-GHL-JOBS report: Run AV (push cadence emails into GHL as templates via API)

Stopped after Job 0 and the write-path probe in Job 1, per the brief's own stop condition. No
templates with real content were created; Job 2 (proof) was not attempted since there was nothing
real to verify.

## Built

Nothing shippable. Four empty "New Template" shells exist in GHL (Marketing > Emails > Templates)
from probing the write API; see Skipped/cleanup below. `_briefs/BRIEF-GHL-JOBS-2026-09-15.md` (copy
of the brief) is the only file added to this repo this run.

## What was checked (Job 0, passed)

`GET https://services.leadconnectorhq.com/emails/builder?locationId=AzTPxnK2vSUj19jYoDmR` with
`Version: 2021-07-28` returned HTTP 200 with the existing 27 templates (`builders` array, `total`
array), so the `emails/builder.readonly` scope is present and working.

## Source file check (Job 1, prep, passed)

`_BUILD-LOG/cadence-emails-2026-09-13/` has 44 `.html` files. Excluding the 6 placeholders the brief
names (`45-b.html`, `45-c.html`, `construction-audit.html`, `email-4.html`, `ye-2.html`, `ye-4.html`
-- `email-3.html` does not exist, confirmed by a prior run) and the 3 `internal-*.html` files leaves
**35 full-body files** to push. All 35 were checked and all 35 pass:

- Contain `380-225-5217`: 35/35
- Contain the wrong `385-213...` number: 0/35
- Contain `{{contact.company_name}}` in the body: 0/35 (the merge tag appears only in Won Email 7's
  *subject*, per INDEX.md -- that is a legitimate personalization use in the subject line, not a
  body leak, and subjects are set from INDEX.md text, not read from the file bodies)
- Contain an em dash, en dash, or a spaced hyphen used as a dash: 0/35

The 35-file list is the same set Job 1 would have pushed had the write API worked.

## Why Job 1 stopped: the Email Builder API cannot write template content

The brief's only documented write call is `POST /emails/builder`, then a `GET` to confirm. I could
not find the payload shape anywhere in the Master Kit (the one prior report that used this API,
`ghl-prospecting-workflows-REPORT-2026-09-08.md`, names a two-step `POST /emails/builder` then
`POST /emails/builder/data` but records no request bodies), so I derived it from the API's own `422`
validation messages and then tested it end to end. Findings, in the order tried:

1. `POST /emails/builder` with `{}` -> `422 "locationId is required"`.
2. `POST /emails/builder` with `{locationId}` -> `422`, `"type must be html,folder,import,builder,blank,ai_template,vibe-editor"`.
3. `POST /emails/builder` with `{locationId, type:"html"}` -> **201**, `{id: "6aa9c57694dd617868466523"}`.
   Re-fetching the list shows this created a template, but named `"New Template"` with an **empty**
   `index.html` at its `previewUrl`.
4. Repeated step 3 adding `name`, `html`, `content`, `body`, `editorContent`, and `subject` fields to
   the create call, in two separate attempts -> both still **201**, and both still came back as
   `"New Template"` with an empty body when re-fetched. The create endpoint silently ignores every
   content field tried; it only ever creates a blank shell.
5. Tried to update one of the shells afterward with real content, four different route shapes, all
   with the shell's real id:
   - `PUT /emails/builder/{id}` -> `404 "Cannot PUT /emails/builder/{id}"`
   - `PUT /emails/builder/{locationId}/{id}` -> `404 "Cannot PUT /emails/builder/{locationId}/{id}"`
   - `PATCH /emails/builder/{locationId}/{id}` -> `404 "Cannot PATCH /emails/builder/{locationId}/{id}"`
   - `POST /emails/builder/{locationId}/{id}` -> `404 "Cannot POST /emails/builder/{locationId}/{id}"`
   These are bare-router 404s (no such route mapped), not scope/permission errors -- there is no
   update endpoint at any of these paths.
6. `GET /emails/builder/{locationId}/{id}` (single-template detail; the one place a companion write
   endpoint might plausibly live) -> `401 "The token is not authorized for this scope."` This matches
   the 2026-09-08 report's finding exactly: this Private Integration cannot read a template's detail,
   only the list.
7. `type:"import"` (one of the six values the API accepts) turns out to mean "import from a
   marketing-email provider account," not "import raw HTML": `POST /emails/builder` with
   `{locationId, type:"import"}` -> `422`, `"importProvider is required and must be a valid
   EmailTemplateProvider(mailchimp,active_campaign)"` plus `"importURL is required..."`. There is no
   generic HTML-import path here either.
8. As a sanity check, tried HighLevel's current, documented v3 template API instead:
   `POST https://services.leadconnectorhq.com/emails/locations/{locationId}/templates` with
   `Version: v3`, `editorType: "html"`, `editorContent: "<html>...</html>"` -> `401 "The token is
   not authorized for this scope."` This needs `emails/templates.write`, a different scope than the
   two the brief's Job 0 names, and the Private Integration does not have it.

**Conclusion:** with the scopes this Private Integration token has (`emails/builder.readonly`,
`emails/builder.write`), the only thing the write scope actually unlocks is creating an empty,
unnamed template shell. There is no reachable endpoint, documented or guessed, that sets a
template's name, subject, or HTML body. The premise of the brief (create 35 templates through the
Email Builder API, body = file verbatim) cannot be done from this terminal with this token.

This matches the brief's own stop instruction ("if the API rejects raw HTML templates, say exactly
what it returned and stop after the first failure; do not paste in a browser") in spirit even though
no single call returned an outright rejection: every content-carrying field is silently dropped
rather than erroring, which is a worse failure mode to walk into blind by continuing to push all 35
files one at a time.

## Verification

None -- Job 2 (fetch two templates back and diff, render one in headless Chromium) was not attempted
since no template with real content exists to fetch or render.

## Assumptions

1. Treated the brief's stop condition as covering this finding (silent field-dropping, not a hard
   error) rather than only a literal API rejection, since continuing to call a create endpoint that
   ignores content 35 more times would not have produced anything useful.
2. Did not attempt to log into the GHL browser UI to inspect the network calls the Marketing >
   Emails > Templates page itself makes when a human creates an HTML template, since terminal
   assignment (GHL-JOBS is files/code/API only) forbids that; only the GHL terminal (terminal A) is
   allowed in that UI. That inspection would very likely reveal the real save endpoint quickly and
   is the fastest unblock, but it is out of scope for this terminal.
3. Did not attempt the four other allowed `type` values (`folder`, `blank`, `ai_template`,
   `vibe-editor`) beyond `html` and `import`, since `folder` is for organizing templates (not
   content), and `ai_template`/`vibe-editor` looked like they would trigger GHL's AI generation
   flow rather than accept literal HTML, which risks unpredictable side effects (an AI-writing call)
   for a token scoped only for API automation. Flagged rather than tried.
4. Left the 4 empty "New Template" shells in place rather than trying harder to delete them, since
   this session's own tool sandbox blocks DELETE calls to a shared resource as an irreversible
   action requiring explicit user permission, and repeated deletion attempts would not have changed
   that. Their ids are listed below for manual cleanup (Marketing > Emails > Templates, delete any
   template still literally named "New Template" with today's date).

## Skipped

- All 35 full-body cadence email files (listed in the source check above): not pushed, since there
  is no working write path. File list is otherwise ready to go the moment a real endpoint is found.
- The 6 placeholder files (`45-b`, `45-c`, `construction-audit`, `email-4`, `ye-2`, `ye-4`) and 3
  `internal-*` files: correctly excluded per the brief, not attempted.
- `email-templates-map.md` / `email-templates-map.json`: not written, since no templates with real
  ids-to-content mapping exist yet.
- Job 2 (proof: fetch, diff, render, screenshot): not attempted, nothing to verify.

### Cleanup needed in GHL (4 empty junk templates, all named "New Template", all created today
2026-09-15 while probing)
- `6aa9c57694dd617868466523`
- `6aa9c5b9e686ab50486928b1`
- `6aa9c5ef3029d837f98f9666`
- `6aa9c6179ed784b5df8c1a95`

## Questions for David

1. **Can the GHL terminal (terminal A) open Marketing > Emails > Templates, create one HTML
   template by hand, and read the network tab for the save request?** That is very likely the
   fastest way to find the real save endpoint (name, subject, HTML body) that this terminal
   could not discover from outside the browser. Once that shape is known, this terminal can push
   all 35 files through it in one job.
2. **Should the Private Integration's scopes be widened to `emails/templates.write` (the newer v3
   API)?** That endpoint is HighLevel's current documented template-create API and, unlike the
   `/emails/builder` path this brief named, it visibly accepts `editorContent` in the same call
   that creates the template. If that scope is added (Settings > Integrations > Private
   Integrations > Atlas One apps > Edit > Scopes > search "templates" > tick write > Update), this
   terminal can very likely finish the whole brief through that endpoint instead, no browser needed.
3. **OK to delete the 4 empty "New Template" shells listed above** (or should David delete them
   directly in Marketing > Emails > Templates)? This terminal's own sandbox blocks it from issuing
   the DELETE call itself.
4. Given the underlying problem (Quick Compose in the workflow editor rewriting pasted HTML), is
   there a workaround already available in GHL that does not depend on the Email Builder API at
   all, for example a "paste as HTML" toggle inside Quick Compose, or building the 35 templates by
   hand in the Templates UI (terminal A) rather than through the API? That would unblock delivery
   even before the API question above is answered.
