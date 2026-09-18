# RUN-GHL-JOBS report: Run BO

Terminal: GHL-JOBS (files, code and the GHL API only, no browser). All three jobs in the brief
(Back Office Audit: fields, three audit emails as templates, the audit intake landing page) are
done. Zero hard stops, nothing sent.

## Job 1: audit contact fields

Read all contact custom fields first (`GET /locations/{id}/customFields`, 606 fields total).
Created two Contact fields in the existing folder `AmY51esJO2QF0v3wvODu`:

| Name | Key | Field id | Type |
|---|---|---|---|
| Audit Code | `contact.audit_code` | `nHP6JGw9eY0lyDNAs4Tc` | TEXT |
| Audit Offer Expires | `contact.audit_offer_expires` | `TGGXt9MICuxqMDk8LNpz` | DATE |

Searched the existing fields for WC policy expiration and benefits renewal (Form A, captured
2026-09-04) before creating anything: both already exist, created nothing for either.

| Name | Key | Field id | Type | Folder |
|---|---|---|---|---|
| Workers' Comp Policy Expiration Date | `contact.workers_comp_policy_expiration_date` | `eMCAKthzngNPmoED1zm4` | DATE | `rZZUbIfqUYHtMiO2ND5n` |
| Benefits Renewal Date | `contact.benefits_renewal_date` | `1HY5GB56JfGVW9pZNdCn` | DATE | `ra4rylFUwAUV611f1VrS` |

Saved the field creation responses (ids and metadata only, no token) to repo
`_briefs/assets/run-BO-jobs/audit-fields.json`.

## Job 2: the audit intake landing page

Built `audit/index.html` in `~/Projects/atlas-one-intake-forms`, same shell as `start/index.html`
(navy header bar, laptop mark, four brand colours, DM Sans, 380 footer). Title "Back Office Audit:
send your documents", the exact lede from the brief, and the four documents listed in plain words
(bank/card statements or QuickBooks Expenses by Vendor or Ramp export; last payroll register or
provider invoice; workers comp declarations page; benefits renewal or current carrier invoice).

`<div id="audit-form">` holds the fallback line ("The upload form is being switched on...") with a
mailto to David. A script constant at the top of the file, `const AUDIT_FORM_ID = ""`, is empty for
now; when the GHL terminal supplies a form id and it is filled in, the same script writes the GHL
widget iframe (`https://api.leadconnectorhq.com/widget/form/<id>`) plus `form_embed.js` into that
div, hides the fallback line, and passes `?audit_code=` from the page URL through to the form URL.

Verified headless Chromium (Playwright) at 390px and 1440px: `scrollWidth` equals the viewport at
both widths, zero console errors, and the only non `file://` requests are the Google Fonts CDN
calls that `start/index.html` itself already uses (see Assumptions). Screenshots at
`_briefs/assets/run-BO-jobs/audit-390.png` and `audit-1440.png`. Committed and pushed (`8aac48e`).
Live URL once GitHub Pages picks it up: `https://forms.atlasonesolutions.com/audit/`.

## Job 3: three audit emails pushed as templates

Confirmed the real merge key from Job 1 (`contact.audit_code`) before touching the file. In
`cadence-emails-2026-09-13/audit-prep.html`, replaced the literal `FORM_D_URL` with
`https://forms.atlasonesolutions.com/audit/?audit_code={{contact.audit_code}}`.

Wrote two new files in the same folder, same wrapper and signature block as `portal-doc-ready.html`:
`audit-offer-day20.html` (subject "Ten days left on your Audit offer, {{contact.first_name}}") and
`audit-offer-day28.html` (subject "Your Audit offer closes in two days"), both using
`{{contact.audit_offer_expires}}` and a "Book 15 minutes" button to the 15 minute intro booking
link (`https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp`, the
same link used elsewhere in this repo).

Pushed all three via `POST /emails/builder` then `POST /emails/builder/data`:

| Template name | Template id | Status |
|---|---|---|
| `A1 | Audit | prep` | `6aad411ab397941922a158c5` | create 201, fill 201 |
| `A1 | Audit | offer-day20` | `6aad411bb0cd6d0085e3ac07` | create 201, fill 201 |
| `A1 | Audit | offer-day28` | `6aad411d173deedb774b43e6` | create 201, fill 201 |

Fetched all three back via their `previewUrl` and diffed against source: the only differences on
every template are GHL's own Outlook/mso-fixes markup (an `<!-- outlook-fixes-applied -->` comment
and mso conditional font tags around button links), no content or link differences. Before and
after copies in `_briefs/assets/run-BO-jobs/before-after/`. Added a "Run BO" section to
`email-templates-map.md`. Sent nothing.

## Assumptions

1. Job 2's `start/index.html` shell loads DM Sans from the Google Fonts CDN, not the base64
   embedded font approach the project's brand rule describes for `tools/*` single file tools. Since
   the brief explicitly named `start/index.html` as the shell to reuse, matched it exactly rather
   than mixing conventions; `audit/index.html` sits alongside `start/` as a landing page, not inside
   `tools/`. Flagging in case David wants it moved to the base64 approach later.
2. The audit intake page's container width was narrowed from `start/index.html`'s 900px to 760px
   since this page has far less content (a header, a four item list and one form card); kept every
   other shell element (colours, mark, footer, font) identical.
3. Used the 15 minute intro call booking link already live in `start/index.html`
   (`atlas-one-15-minute-intro-call-hoswp`) for both offer emails' "Book 15 minutes" button, since
   the brief said "the 15 minute intro link" without a URL and this is the only 15 minute link found
   in the repo or the cadence folder.
4. `audit-offer-day20.html` and `audit-offer-day28.html` copy `portal-doc-ready.html`'s wrapper and
   signature byte for byte (header image, footer links, legal line), changing only the body and
   button per the brief's copy.

## Skipped

Nothing skipped. All three jobs done.

## Questions for David

1. Job 2: should `audit/index.html` be moved under `tools/` with the base64 embedded font
   treatment to match every other single file tool, or is it fine as a `start/`-style landing page
   with the Google Fonts CDN link (see Assumption 1)?
2. Job 2: the page still shows the fallback "email the documents to David" line since
   `AUDIT_FORM_ID` is empty. Once the GHL terminal builds the audit upload form and reports its id
   back, the next GHL-JOBS run needs to fill that constant, or say the word and this run can pick
   the id up directly from a Part number in the live log.
3. Job 3: confirm the "Book 15 minutes" link (Assumption 3) is still the right one to send, since
   it was not named explicitly in the brief.
