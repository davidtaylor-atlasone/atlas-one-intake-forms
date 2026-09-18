# RUN-GHL-JOBS report: Run BK

Prior report backed up to `_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-JOBS-report-RunBJ.md`
before this one was written (already in place per the brief). Ran everything in this session,
no forking or delegation (rule 44). Brief copied to `_briefs/BRIEF-GHL-JOBS-2026-09-17.md` in
the repo.

`.env`'s `GHL_PIT` confirmed to start with `pit-` (40 characters, never printed, logged or
written anywhere) before Job 1 started, per Run BJ's answer 1.

## Built

- `tools/ghl_email_builder.py`: fixed `list_templates` to read the live API's actual response
  key (`builders`), not `templates`/`data`. With the real `pit-` token the first call
  (`GET /emails/builder`) returned 200 immediately; the prior `401 Invalid JWT` was the wrong
  token, exactly as Run BJ's answer said.
- `_briefs/assets/run-BK-jobs/templates-list.json`: all 63 live Email Builder templates (id,
  name, dateAdded, lastUpdated, previewUrl; no token).
- `_briefs/assets/run-BK-jobs/templates-before/*.html`: all 63 templates' HTML fetched via
  `previewUrl`.
- `_briefs/assets/run-BK-jobs/templates-after/*.html`: the 24 templates that had a phone hit,
  after the fix.
- `_briefs/assets/run-BK-jobs/job1-push-report.json`, `job1-verify-report.json`: per-template
  hit counts, push status codes, and the post-push re-fetch verification.
- `Health Comparison Builder (Atlas One).html`: Redirect Health catalog lede rewritten.
- `Independent Contractor Onboarding Packet (Bilingual).html`,
  `W-2 Employee Onboarding Packet (Bilingual).html`: Send to Atlas One button now opens Form D.
- `tools/onboarding/send/index.html` (repo): rewritten from a "David is finishing this page"
  placeholder into a redirect to Form D, forwarding the query string.
- `email-templates-map.md`: phone-fix notes added; one stale id flagged (see Assumptions).
- `Atlas One COMMAND.html` rebuilt: **192 items**, stamp `Atlas One COMMAND: build Sep 17, 2026
  6:11 PM`. Pre-rebuild copy backed up to `_to_delete/superseded-2026-09-17/before-runBK-job3/`
  first.

## Job 1: the 385 number in the P prospecting templates -- done

1. Listed all 63 live templates via `GET /emails/builder` (paged; only one page came back since
   total is 63 and page size 100).
2. Fetched HTML for all 63 via `previewUrl` (plain GET, no auth header, works for every one).
3. Grepped for `385-213-7177`, `385.213.7177`, `(385) 213-7177`, and both digit-only forms of
   the tel link (`tel:13852137177` and the bare `3852137177` substring). Found hits in 24
   templates, all P- prospecting ones; zero hits in any `A1 |` template.
4. The map's second table only lists 20 of the 21 it claims (`P-A-1` and `P-A-2` are missing
   from it, and neither is anywhere else in the file), and it does not list six more P-
   templates that exist live and also had the old number: `P-A-1`, `P-A-2`,
   `P-BUILDER-DELIVERY`, `P-C-0 Instant reply`, `P-MEMBER-WELCOME`, `P-PAY-FAILED`. See
   Assumptions for why all 24 got fixed, not just the ones literally named in the table.
5. For each of the 24: replaced with `380-225-5217` (display text) and `tel:+13802255217`
   (tel links), pushed with `POST /emails/builder/data`, re-fetched via a fresh
   (cache-busted) `previewUrl`, and confirmed both that the pushed content matches the
   re-fetched content and that the phone-hit count on the re-fetch is 0.
6. Diffed each before/after pair character by character: every changed span sits inside the
   phone number text (some spans look odd, e.g. `3717` deleted, `0-22` inserted, because
   `385-213-7177` and `380-225-5217` share several digits and `difflib` finds the shortest
   edit, not whole-token edits); nothing outside the phone number changed in any of the 24.
7. Full per-template table (name, id, hits before, hits after, push status) is
   `_briefs/assets/run-BK-jobs/job1-push-report.json`. All 24: hits before 2 or 3, hits after 0,
   push status 201.
8. `email-templates-map.md` updated: "phone fixed 2026-09-17" on each of the 24 rows (20
   existing rows in the second table plus a new paragraph for the 6 the table never had), the
   `P-W7-*` three rows noted as "no hit, not fixed", and the stale `P-B-2` id flagged inline.

Sent nothing; no email or SMS went out. No template without a hit was touched.

## Job 2: Health Comparison Builder lede -- done

The Redirect Health catalog's lede in `Health Comparison Builder (Atlas One).html` (`#p_rdh`)
changed from "...Read off the employer benefit summaries; use it on screen with a prospect, or
to sanity-check a quote." to "...Read off the employer benefit summaries. Use it internally to
sanity check a quote before you present. Nothing from this section goes to a client." (no
dashes; the old sentence's hyphen in "sanity-check" is gone along with the phrase). This
resolves the contradiction Run BJ flagged between this lede and the "INTERNAL, never client
facing" header pill it added.

Verified headless (Playwright, file:// only): 390px and 1440px viewports both show
`scrollWidth` equal to the viewport width, zero console errors, and the lede's live text
confirmed via `document.querySelector('#p_rdh .lede').textContent`.

## Job 3: wire the packets' Send to Atlas One button to Form D -- done

`_BUILD-LOG/RUN-GHL-report.md` on disk is still Run BH's report (no Part 33, no prefill
parameter names), so per the brief's own fallback this run used GHL's standard
`first_name`/`last_name`/`email`/`phone` params. Both packets already build a `URLSearchParams`
from their own fields before opening the send link, so only the base URL changed in each:

- `Independent Contractor Onboarding Packet (Bilingual).html` -> now opens
  `https://api.leadconnectorhq.com/widget/form/p0UoqkUnGEwvlc31q636` with `first_name`,
  `last_name`, `email`, `phone`, `company`, `worker_type=1099` (the last two are the packet's
  own existing custom params, kept as-is; see Assumptions).
- `W-2 Employee Onboarding Packet (Bilingual).html` -> same form URL with `first_name`,
  `last_name`, `email`, `phone`, `worker_type=w2`.
- `tools/onboarding/send/index.html` (repo): rewritten to redirect
  (`window.location.replace`) to the same Form D URL, forwarding whatever query string it was
  given, with a visible fallback link and the existing "what was prefilled" table kept so
  nothing is silently lost if the redirect does not fire.

Verified in headless Chromium, no submission:
- Filled the W-2 packet's name/email/phone fields, clicked Send to Atlas One, captured the
  popup: opened
  `https://api.leadconnectorhq.com/widget/form/p0UoqkUnGEwvlc31q636?first_name=Jane&last_name=Doe&email=jane%40example.com&phone=3801234567&worker_type=w2`.
- Filled the IC packet's name/business name/email/phone fields, clicked Send to Atlas One,
  captured the popup: opened the same form URL with `first_name`, `last_name`, `email`,
  `phone`, `company=Smith+LLC`, `worker_type=1099`.
- Loaded the repo placeholder page with a query string attached and confirmed it attempts to
  navigate to the Form D URL with that same query string (the navigation itself fails offline
  in this sandbox, which is expected with no network; the redirect target and query string
  were both correct). Zero console errors.

Rebuilt `Atlas One COMMAND.html` after the packet edits (192 items, stamp confirmed above);
`catalogue_check.py` reports `OK, 192 entries, all paths resolve.`

## Assumptions

1. Job 1's scope note ("the 21 `A1 | P-` templates in the second table... and any other
   template whose name starts with `A1 |`") does not literally match what exists: the second
   table only has 20 rows and none of its templates are named `A1 | P-...` (they are plain
   `P-...`), and six live P- templates are not in the table at all. Since the job's own title
   is "the 385 number in the P prospecting templates" and all six missing ones also carried the
   stale number, treated the real scope as every P- template (fetched and checked all 63 live
   templates to be sure, which also confirmed zero `A1 |` templates have the old number), fixed
   all 24 with a hit, and documented the table's gaps in `email-templates-map.md` rather than
   leaving six stale-number templates untouched on a technicality.
2. `email-templates-map.md`'s recorded id for `P-B-2 Trigger Email 2`
   (`6aa0a9de8b41b02dc82267ae`) does not match the live API's id for that template name
   (`6aa0a9e10078269ef83ce1ac`). Used the live listing as the source of truth for every push
   (matched by name, not by the doc's id column), since a push against a stale id would have
   simply failed or hit the wrong template; flagged the mismatch inline in the map rather than
   silently overwriting the doc's original id.
3. Job 3's prefill params: kept the onboarding packets' existing `company` and `worker_type`
   custom query params (not on the brief's standard-params list) alongside the four standard
   ones, since removing information the packets already collect and were already sending would
   be a regression with no clear benefit, and GHL's form widget simply ignores query params
   that do not match a field. This is a judgment call, not a scope violation, since the brief's
   fallback only specifies the minimum params to use when the real ones from Run BI are
   missing, not a maximum.
4. Rewrote the repo's `tools/onboarding/send/index.html` from a manual "email your documents"
   placeholder into a redirect, since both packets no longer point users there at all (they
   open Form D directly) but any link already shared or bookmarked to that path should still
   land somewhere useful rather than a dead-end placeholder.

## Skipped

Nothing in this brief was skipped; all three jobs ran to completion.

## Questions for David

1. **`email-templates-map.md`'s P- table needs a cleanup pass.** It claims 21 templates but has
   20 rows, is missing `P-A-1` and `P-A-2` entirely, and its `P-B-2` id no longer matches the
   live API. This run left the table's original ids in place and only annotated the
   discrepancies inline; a future run could re-sync the whole table against the live
   `GET /emails/builder` listing if that would be useful.
2. **Form D's prefill param names are still unconfirmed.** This run used GHL's standard
   `first_name`/`last_name`/`email`/`phone` (plus the packets' own `company`/`worker_type`)
   because `RUN-GHL-report.md` has no Part 33 yet. If Terminal A confirms the form's actual
   field names differ from the standard set, a follow-up run should update both onboarding
   packets and the placeholder redirect to match.
