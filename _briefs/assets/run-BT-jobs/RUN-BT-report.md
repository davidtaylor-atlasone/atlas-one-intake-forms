# RUN-GHL-JOBS-report (Run BT, 2026-09-18, terminal GHL-JOBS)

Both offer emails (`audit-offer-day20.html`, `audit-offer-day28.html`) are clean of
`{{contact.audit_offer_expires}}`, live on GHL, and confirmed by fetching each template's
previewUrl back. The Audit report now writes the real expiry date to GHL after every render,
tested working (fake contact refused cleanly, `--no-ghl` skips, the sample auto-skips).

## The problem this run fixed

Run BQ found this GHL account's Date/Time Formatter cannot do date math, so the day 20 and
day 28 offer emails were printing `{{contact.audit_offer_expires}}`, a field the workflow was
setting to the day it ran, not a real expiry. A prospect on day 20 would read "your offer
expires" next to the date the offer started. This run took the date out of the emails and
made the one place that already computes it correctly, the Audit report, the source of truth,
and made it write that date back into GHL so a future workflow could read it without
re-deriving it wrong again.

## Job 1: took the date out of the two offer emails

`audit-offer-day20.html`: "The offer from your Back Office Audit report holds for ten more
days. The number, the three fixes and the price in that report stay good until then, along
with the guarantee..."

`audit-offer-day28.html`: "Two days left on the offer in your Audit report. After that the
numbers get rebuilt from current rates."

Both keep `{{contact.first_name}}`, the existing structure, CSS, button and signature
untouched. Grep confirms zero occurrences of `audit_offer_expires` in either file. Dash check
clean (no em dash, en dash, or hyphen used between spaces). Rendered headless at 390 and 700
wide and looked at both: no horizontal overflow, copy reads correctly. Screenshots in
`_briefs/assets/run-BT-jobs/shots/`.

## Job 2: re-pushed both templates in place

Used `tools/ghl_email_builder.py`'s `fill` call (`POST /emails/builder/data`) with the
existing templateIds, no new templates created:
- `A1 | Audit | offer-day20` (`6aad411bb0cd6d0085e3ac07`) — 201
- `A1 | Audit | offer-day28` (`6aad411d173deedb774b43e6`) — 201

Fetched both previewUrls back and saved to `_briefs/assets/run-BT-jobs/*.fetched.html`: grep
confirms zero occurrences of `audit_offer_expires` in the live templates and the new sentences
are present verbatim. Subjects for both come from `<title>`, neither used the merge tag, so
`email-templates-map.md` needed no edit.

## Job 3: the Audit report writes the real expiry to GHL

Added `update_contact_field` (`PUT /contacts/{contactId}`, body
`{"customFields":[{"id": field_id, "field_value": value}]}`) to
`tools/ghl_custom_fields.py` in the atlas-one-intake-forms repo, reusing that file's existing
`.env` / `GHL_PIT` token loader (never printed).

`build_audit_report.py` now computes `good_through` the exact same way the report body
already does (`audit.offer.good_through` or report date plus 30 days), so the value written to
GHL can never drift from the number the report prints. After the HTML and PDF render, it calls
`push_offer_expiry_to_ghl`, which:
- reads the contact id from `audit.ghl_contact_id` (added to `AUDIT_SCHEMA.md`)
- locates the sibling `atlas-one-intake-forms` repo's `tools/` directory (checks
  `~/Projects/atlas-one-intake-forms/tools` first, then a bounded walk of the home directory,
  skipping `_to_delete`, archive folders, `node_modules` and `.git`, so it works on either Mac
  from CLAUDE.md without a hardcoded username)
- writes the date to field `TGGXt9MICuxqMDk8LNpz` (Audit Offer Expires)
- on any problem at all (missing contact id, repo not found, missing token, a non 200/201
  status, any exception) prints one plain line and returns, never raising: "Could not set the
  offer expiry in GoHighLevel. Open the contact and type `<date>` into Audit Offer Expires."

`--no-ghl` skips the write outright. The write is also skipped automatically when the JSON
filename contains `SAMPLE` or the client is exactly `Tell Me More LLC`, so the sample can never
touch a real contact even if someone later adds a `ghl_contact_id` to it by habit.

Tested against a scratch copy of `prospects/big_red_jelly.json` in `/tmp` (never committed,
deleted after):
- fake contact id set: report rendered normally, PDF written, GHL call attempted and refused,
  correct fallback line printed with the real date (`2026-10-18`)
- same file with `--no-ghl`: report rendered, no GHL line printed at all
- the real `prospects/SAMPLE_Tell_Me_More_LLC.json`: report rendered, automatic sample skip
  fired, no GHL line printed

## Job 4: kept the sample honest

Re-rendered `SAMPLE_Tell_Me_More_LLC.json` in place
(`prospects/Atlas_One_Back_Office_Audit_Tell_Me_More_LLC__SAMPLE__fictional_2026-09-18.html`
and `.pdf`). Offer page reads "good through 2026-10-18" (report date plus 30, since the
sample's `audit.offer` block is empty), matching the same math the emails now rely on in
words. No GHL line printed, confirming the automatic sample skip. Screenshot in
`_briefs/assets/run-BT-jobs/shots/sample-report-page1.png`, looked at, renders clean.

Checked `catalogue.py`: the only row touching anything this run changed is `build-audit-report`,
and only by its path and title, both unchanged. Nothing catalogued changed, so COMMAND was not
rebuilt.

## Assumptions

1. Wrote the day 20 and day 28 sentences in David's voice from the brief's own bullet points,
   keeping "ten more days" and "two days left" as the only time references, both in words, no
   date.
2. `update_contact_field` uses the LeadConnector v2 contact PUT shape
   (`customFields: [{id, field_value}]`) since no prior example of writing a value (as opposed
   to creating a field) existed anywhere in this repo or the Master Kit; verified working
   against a fake contact id, which the API refused cleanly rather than erroring in a way that
   would suggest the shape itself was wrong.
3. `build_audit_report.py` needs code from a separate git repo (`atlas-one-intake-forms`) that
   is not a fixed path relative to the Master Kit. Rather than duplicate the token loader (the
   brief said reuse it), added a bounded run time search for that repo, checked against both
   Macs' home directories per CLAUDE.md. If the repo is ever moved somewhere neither guess nor
   the four level walk reaches, the report still finishes; it just prints the fallback line.
4. Sample skip checks both the filename (`SAMPLE`) and the client string (`Tell Me More LLC`)
   rather than only relying on the sample's JSON lacking `ghl_contact_id`, since a future edit
   to the sample file could add one by copy paste from a real prospect.
5. Did not touch `email-templates-map.md` since the row text (drawn from each file's `<title>`)
   already matched after the edit; neither title ever carried the merge tag.

## Questions for David

None. All four jobs completed clean; the only design call worth flagging is Assumption 3
above, which is documented rather than asked, since it does not block anything.
