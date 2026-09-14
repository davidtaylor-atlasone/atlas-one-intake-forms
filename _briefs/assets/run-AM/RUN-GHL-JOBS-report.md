# RUN-GHL-JOBS Report (Run AM, 2026-09-14)

Two Portal fixes David found on 2026-09-14. Both jobs done end to end, no hard stops hit.

## Job 1: "Everything Atlas One handles" card showed PDF gibberish

**Cause:** `build_portal.py` line 31 pointed the catalogue entry at
`A1_Sales/Atlas_One_Everything_We_Handle.pdf`; the single-file Portal inlines PDFs as raw text, so the card
rendered as gibberish instead of the page.

**Fix:**
- Copied the live page (`repo:tools/what-we-do/index.html`) into the Master Kit unchanged as
  `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Everything_We_Handle.html`.
- Updated `_INTERNAL (do not share)/build_portal.py` line 31 to point the catalogue entry at that HTML file
  instead of the PDF, and trimmed the blurb's "printed" wording since it's no longer a print of the PDF.
- The PDF itself was left untouched in `A1_Sales/` for attaching to emails, per the brief.
- Backed up the pre-run Portal to `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-14/Atlas One PORTAL
  (before RUN-AM).html` before rebuilding.
- Rebuilt the Portal with `build_portal_single.py "<Master_Kit>"`. Stamp: `Atlas One Portal: build Sep 14, 2026
  8:49 AM`, 44 tools.

**Checked for other places pointing at the PDF as an inline page** ("Tools Hub" and "Master Hub" cards, per the
brief): searched `Atlas One — Tools Hub.html` and the whole Master Kit for `Everything_We_Handle` references.
The only reference besides the Sales PDF itself was the one catalogue line in `build_portal.py`, now fixed.
There is no separate "Master Hub" file; the Portal itself is the master hub and is the one place that needed
fixing.

**Verified:** rendered `Atlas_One_Everything_We_Handle.html` in headless Chromium.
- Title: "Everything Atlas One handles"
- Hero renders, six division cards render (Workforce & HR, Benefits & Retirement, Financial Services, Risk &
  Insurance, Technology & Operations, Business Consulting)
- Zero console errors, zero non-file:// network requests
- At 390px: `document.documentElement.scrollWidth` = `window.innerWidth` = 390
- Screenshots: `_briefs/assets/run-AM/shots/what-we-do-1440.png`, `_briefs/assets/run-AM/shots/what-we-do-390.png`

## Job 2: "Have Atlas One build this for me" white box read vague

**Fix**, on `repo:build/index.html` (and synced identical to the Master Kit copy at
`06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Build_This_For_Me.html`):

- Replaced the static "Document" pill with a real `<select>` dropdown (`#docselect`) styled to match the brand
  (navy pill border, DM Sans, periwinkle focus ring), listing the eleven builders plus Other:
  Employee Handbook, Safety Manual, W-2 At-Will Agreement, Contractor Agreement, NDA, Disciplinary Write-Up,
  Separation Letter, W-2 Onboarding Packet, 1099 Onboarding Packet, Enrollment Guide, Other. It pre-selects from
  the existing `?doc=` query param (unknown or missing slugs fall back to "Other") and the visitor can change it.
- Added four optional text fields in a two-column grid (stacks to one column under 480px): Company name, Number
  of employees, States you operate in, When you need it.
- Replaced the vague copy with the exact plain-voice paragraph from the brief: "Pick the document, answer the
  four questions, and click Email David. Your email opens already written with those answers so nothing is left
  to explain. David builds it around your business, reviews it with you, and sends it back ready to sign,
  usually within five business days. If it is easier to talk it through, book the 30 minute call instead and
  bring the same four answers."
- "Email David" mailto now builds subject `Build this for me: <document>` and a body listing the four answers
  (blank lines if a field is left empty) plus an open `Anything else I should know:` line, regenerated live on
  every keystroke/selection change so the link is always current when clicked.
- "Book a 30 minute call" (group booking link) and "Or call 385-213-7177." left unchanged.
- `GHL_BUILD_FORM` redirect logic (currently empty, holding-page mode) left untouched.

**Verified in headless Chromium:**
- Rendered at 1440px and 390px. Screenshots: `_briefs/assets/run-AM/shots/build-1440.png`,
  `_briefs/assets/run-AM/shots/build-390.png`
- 390px: `scrollWidth` = `innerWidth` = 390, zero console errors, zero non-file:// requests
- `?doc=nda` pre-selected "NDA" in the dropdown
- Filled Company name "Acme Construction LLC", Number of employees "18", States "Utah, Idaho", When you need it
  "Within two weeks", then read the generated mailto href. Decoded:

```
mailto:David@AtlasOneSolutions.com?subject=Build this for me: NDA&body=Company name: Acme Construction LLC
Number of employees: 18
States you operate in: Utah, Idaho
When you need it: Within two weeks

Anything else I should know:
```

- Pushed to `main`, waited for the GitHub Pages deploy, then confirmed `forms.atlasonesolutions.com/build/`
  returns `200` and serves the new copy (`docselect` present, new paragraph text present, matches the pushed
  file).
- Backed up the pre-job-2 Portal to `_to_delete/superseded-2026-09-14/Atlas One PORTAL (before RUN-AM job2).html`
  and rebuilt the Portal again since a tool file changed. Stamp: `Atlas One Portal: build Sep 14, 2026 8:53 AM`,
  44 tools.

## Paths touched

- Repo: `build/index.html` (modified)
- Master Kit: `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Everything_We_Handle.html` (new file)
- Master Kit: `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Build_This_For_Me.html` (modified, kept
  identical to repo copy)
- Master Kit: `_INTERNAL (do not share)/build_portal.py` (catalogue entry updated)
- Master Kit: `Atlas One PORTAL.html` (rebuilt twice, once per job)
- Master Kit: `_to_delete/superseded-2026-09-14/` (two pre-run Portal backups)
- Repo: `_briefs/BRIEF-GHL-JOBS-2026-09-14.md` (brief copy), `_briefs/assets/run-AM/shots/*.png` (four
  screenshots)

## What was looked at

- `tools/what-we-do/index.html` source, confirmed self-contained (fonts and logo as base64 data URIs, only
  outbound `href`s to booking link, other tool pages, tel:, and mailto:, no `<script src>` or `<link
  rel="stylesheet">` to anything external)
- `build_portal.py` catalogue block and the `CAL`/`SALES` path variables it uses
- All four rendered screenshots (what-we-do at 1440 and 390, build page at 1440 and 390)
- The generated mailto href with sample data filled in
- The live `forms.atlasonesolutions.com/build/` response after the Pages deploy

## Assumptions

1. The eleven builder slugs in the `NAMES` map: kept the five that already existed (`handbook`,
   `safety-manual`, `offer-letter`, `ic-agreement`, `nda`) and invented six new ones for the builders that had
   no prior `?doc=` convention anywhere in the repo or Master Kit (`writeup`, `separation`, `w2-onboarding`,
   `1099-onboarding`, `enrollment-guide`, `other`). Searched the repo and every builder page that links to this
   tool for an existing slug convention for those six and found none, so this is a clean invention, not a
   guess at something that already existed elsewhere.
2. Renamed two display labels to match the brief's dropdown wording exactly (brief said "W-2 At-Will
   Agreement" and "Contractor Agreement"; the old copy said "W-2 At-Will Employment Agreement" and
   "Independent Contractor Agreement"). Kept the old, more precise `nda` label change from
   "Non-Disclosure Agreement" to "NDA" for the same reason, since the brief's own list used the short forms.
3. When `?doc=` is missing or doesn't match a known slug, the dropdown now defaults to "Other" (previously
   the static pill showed a blank "Which document?" placeholder, which a `<select>` can't cleanly replicate
   without either a pre-selected value or a disabled empty option). "Other" reads correctly either way and
   is one of the eleven options the brief asked for, so no dead end.
4. Job 1's blurb text ("The public what-we-do page, printed...") kept everything except the word "printed,"
   since the card no longer represents a printout of a PDF; left the rest of the wording (including the "Live
   at forms.atlasonesolutions.com/what-we-do/" line) as-is since the brief only asked to fix the broken
   render, not rewrite the blurb.
5. Left the H1 and lede paragraph on the build page untouched. The brief's complaint and rewrite instructions
   were specifically about "the white box," i.e. the card; the lede above it already reads clearly and wasn't
   called out.

## Skipped

Nothing in the brief was skipped. No hard stops were hit (no email sent, no SMS, no HIPAA toggle, no file
deleted, no production deploy outside the normal git push to the GitHub Pages branch, no money spent).

## Questions for David

None. Both jobs were fully specified and no judgment call needed escalating beyond the Assumptions above.
