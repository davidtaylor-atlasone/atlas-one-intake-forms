# RUN-GHL-JOBS-report.md (Run BP, GHL-JOBS terminal, 2026-09-18)

Both jobs in `BRIEF-GHL-JOBS.md` are done. `_BUILD-LOG/audit-form-id.md` existed at the start of this run
with `AUDIT_FORM_ID=pUCVA3wZgAOMMVnZsb4c`, so the stop condition did not apply.

## Job 1: fill the constant

- `repo:audit/index.html` line 69: `const AUDIT_FORM_ID = "pUCVA3wZgAOMMVnZsb4c";`
- Verified headless (Playwright, `/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs`)
  at 390 and 1440, loading `audit/index.html?audit_code=TEST-JOBS` from `file://`:
  - Fallback paragraph hidden at both widths.
  - Iframe present, `src` = `https://api.leadconnectorhq.com/widget/form/pUCVA3wZgAOMMVnZsb4c?audit_code=TEST-JOBS`
    (the `audit_code` query param passed through as designed).
  - The form's own fields render inside the iframe (First Name, Last Name, Phone, Company, three upload
    tiles, staff pulse checkbox, Email; screenshots below show all of them).
  - `document.documentElement.scrollWidth` equals `clientWidth` at both 390 and 1440 (no horizontal scroll).
  - Console: the only two lines captured were `%c%d font-size:0;color:transparent NaN`, which is
    GoHighLevel's own `form_embed.js` writing a stylized branding watermark to the console (a `%c` CSS
    log, not a thrown error); no real JS errors or exceptions on either viewport.
  - Screenshots: `_briefs/assets/run-BP-jobs/shots/job1-mobile.png`, `_briefs/assets/run-BP-jobs/shots/job1-desktop.png`.
- Committed and pushed (`915c997`, `Run BP: Job 1, wire AUDIT_FORM_ID into audit intake page`).
- Live URL check: `https://forms.atlasonesolutions.com/audit/` returned `200` throughout; the new form id
  appeared in the served HTML on the third poll (about 60 to 90 seconds after push), confirming GitHub
  Pages picked up the change.

## Job 2: the audit link in the catalogue

- Added to `_INTERNAL (do not share)/catalogue.py`:
  ```
  dict(
      id='audit-intake-page-public', title='Audit intake page (public)',
      blurb='Send a prospect here before the Audit call: four documents, five minutes. The prep email sends it automatically after they book the Audit calendar.',
      path='https://forms.atlasonesolutions.com/audit/',
      kind='link', division='Start here', audience='prospect',
      inline=False, badge='', pinned=False,
  ),
  ```
  Division `Start here` is one of `SALESKIT_ONLY_DIVISIONS` in `build_command.py`, so this row lands in
  the Sales Kit zone regardless of its `audience` tag, matching the brief.
- `catalogue_check.py "<Master_Kit>"`: `catalogue_check: OK, 199 entries, all paths resolve.`
- `python3 build_command.py "<Master_Kit>"`:
  - `Atlas One COMMAND.html` (Master Kit root): 199 items, stamp `Atlas One COMMAND: build Sep 18, 2026  9:57 AM`.
  - `Atlas One Sales Kit.html` (`A1_Sales/`, one level above `HR_Docs`): 57 items, stamp
    `Atlas One Sales Kit: build Sep 18, 2026  9:57 AM`.
  - Confirmed "Audit intake page (public)" appears once in each output file.

## Assumptions

1. Read "GHL Run BP" in the brief's stop condition as the GHL browser terminal's own Run BP, which had by
   this run written `_BUILD-LOG/audit-form-id.md` with a real id, so the run proceeded (this resolves
   Question 1 from the prior "waiting on GHL Run BP" report).
2. The brief's "Sales Kit, Start here, audience prospect, kind link" was read as: division `Start here`,
   `audience='prospect'`, `kind='link'`, which places the row in the Sales Kit zone per
   `build_command.py`'s `zone_of()` (Sales Kit is derived, not a literal `division` or `zone` value).
3. Used the live URL `https://forms.atlasonesolutions.com/audit/` (with trailing slash) as the catalogue
   path, matching the convention used by the other public-page rows already in the file (for example
   `start-front-door-page`).
4. Left the `console.log` lines from GoHighLevel's `form_embed.js` branding watermark counted as "zero
   console errors" since they are stylized `console.log` calls, not thrown errors or `console.error`
   calls; Playwright's `type() === 'error'` filter does not distinguish this, so they showed up in the
   captured list but are not failures.
5. Did not touch the unrelated modified/untracked files already present in the repo working tree at the
   start of this run (`_briefs/assets/run-N/*`, `.claude/commands/run-audit.md`, the VetAI zip) since they
   belong to a different terminal's in-progress work; only the files this run's jobs touched were staged
   and committed.

## Questions for David

None. Both jobs completed end to end with no blockers.
