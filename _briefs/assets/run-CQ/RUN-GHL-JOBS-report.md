# Run CQ (GHL-JOBS), 2026-09-27, all three jobs complete

Job 0 (catalog fix at the source), Job 1 (digital business cards for David, held for Charity) and Job 2
(COMMAND / Sales Kit / charity rep kit rebuild) are all complete. Files and code only; never opened the
GoHighLevel browser UI or the portal repo. Run CP's report archived first to
`_to_delete/superseded-2026-09-27/RUN-CP-report.md`.

## Job 0: fix the software catalog at its source

Cowork's audit of Run CP (`COWORK-AUDIT-run-CP-2026-09-27.md`) found the 13 TD SYNNEX Cloud Marketplace
products back on Hold and several Pax8 rows contradicting their own TD SYNNEX Distribution notes.
Unpacking `software-catalog-src-2026-09-26.tgz` to fix this at the source turned up a bigger problem than
the audit described: that tgz's `catalog/data.py` was stale in a deeper way than "Run CP rebuilt without
Run CN's fix in it." It had **no TD SYNNEX Distribution tier at all**, and had never had the Run CN Job 7
Hold to Available fix in it either. Any future rebuild from this exact tgz, by name, would have wiped
both prior runs' work, not just the 13 rows Cowork caught. Fixing only the 13 flips as the short Job 0
brief describes would have shipped a catalog missing 33 vendor rows Cowork had just signed off on.

What was done, all in `catalog/data.py` and `catalog/build_catalog.py` inside the tgz, then repacked
under the same canonical filename (the stale original moved to
`_to_delete/superseded-2026-09-27/software-catalog-src-2026-09-26.tgz`):

1. Flipped the 13 named TD SYNNEX Cloud Marketplace rows from Hold to Available, quote on request: Google
   Workspace, Adobe Acrobat and Adobe Express for teams, Dropbox Business, Cisco Duo and Cisco security,
   Fortinet, Palo Alto Networks, Trend Micro, Symantec (Broadcom), CyFlare, CyberArk, DigiCert / Entrust,
   StorageCraft (Arcserve), Autodesk.
2. Re-added the TD SYNNEX Distribution tier (33 new rows, one line of what each vendor does, Available,
   quote on request, no prices) from the Run CP Job 1 brief text (`BRIEF-GHL-JOBS-runCP-done-2026-09-27.md`),
   since the source never had it: SonicWall, ESET, Ivanti, Arctic Wolf, GoSecure, OPSWAT, Cofense, Ping
   Identity, Infoblox, WinMagic, Utimaco, Altaro, Red Hat, SUSE, Progress Software, EnterpriseDB, Paessler
   PRTG, Devolutions, Checkmk, Parallels, NVIDIA, ServiceNow, TeamViewer, Corel, JetBrains, Faronics,
   PrinterLogic, Avaya, AudioCodes, Oracle Communications, NINJIO, CurrentWare, GoGuardian.
3. Added a second source note (TD SYNNEX Distribution 2026-09-26) to the 13 existing rows that overlap:
   Check Point (both rows), Cynet, Cato Networks, Veeam, Foxit, Five9, and reconciled the Pax8 Hold rows
   named in the brief so no row says "available through" a source while still showing Hold: Barracuda and
   ThreatLocker moved Available; N-able (Cove Data Protection) moved Available with a note that Cove itself
   still wants confirming; DocuSign split out of the old "Dropbox / Box / DocuSign" Hold row and moved
   Available, leaving "Dropbox / Box" on Hold; Carbonite split out of "Carbonite / Webroot (OpenText)" and
   moved Available, leaving Webroot on Hold; Fortinet removed from the old "Cloudflare / Fortinet / Cisco
   Meraki" Hold row (it already has its own Available row from step 1), leaving "Cloudflare / Cisco Meraki"
   on Hold.
4. Added a build guard to `build_catalog.py`: it asserts no row's note contains "available through" while
   its status is Hold, and pins the 13 named rows to Available by name, so a rebuild that would silently
   revert either regression now fails loudly instead of shipping.
5. Rebuilt: 193 rows, Signed 45, Available 120, Pending 3, **Hold 13** (was 28), Internal 12. Copied the
   regenerated md, xlsx and Sheet HTML to both live copies (`A1_Sales/Website/BRJ Software Marketplace
   Package 2026-09-26/` and `A1_Sales/Atlas 1 Software and Licenses/`). Rendered the Sheet PDF with
   headless Chromium (Playwright), zero console errors, copied to both locations. Checked the rendered
   HTML for distributor names and dashes: zero of either.
6. Updated the `catalogue.py` blurbs for the xlsx and Sheet rows with the corrected counts and this run's
   fix.
7. Checked `Email_to_Thomas_BRJ_website_update_followup_2026-09-27.txt`: it already says only "the Hold
   tab is small now" with no number, which is true at 13 (not under 12, so the brief's own rule says give
   no number). No edit needed.
8. Rebuilt `Atlas One for BRJ 2026-09-27.zip`: removed the Thomas email txt from inside it, replaced the
   three catalog files (md, xlsx, Sheet PDF) in place with the corrected versions. 46 files, confirmed no
   `Email_to_Thomas` file inside.

Final Hold list (13 rows) and why each stays: Webroot (OpenText) (Carbonite, the orderable half, split out
and Available), Mimecast, KnowBe4, Huntress, Bitwarden, Cisco Duo (the Pax8-specific row; Cisco Duo the
product is Available through the TD SYNNEX Cloud Marketplace row instead), Okta / JumpCloud, Intermedia /
Dialpad / Cytracom / Vonage, Adobe Acrobat and Creative Cloud (the Pax8-specific row; Adobe Acrobat and
Adobe Express for teams is Available through TD SYNNEX Cloud Marketplace instead), Dropbox / Box (DocuSign
split out and Available), Cloudflare / Cisco Meraki (Fortinet split out and Available), Vanta / Drata,
monday.com / Freshworks / HubSpot / Zoho One. None of these 13 carry a note claiming any source has them
as orderable; the build guard would fail if one did.

## Job 1: digital business cards

Built and tested three cards on branch `cards-draft` of `atlas-one-intake-forms` (committed, not pushed,
not merged to main -- publishing waits for David's yes). Mirrored every file to `A1_Sales/Business Cards/`
in the Master Kit. `david-cornerstone`, the superseded first draft named in an earlier BUILD-INDEX line,
was not built.

- `david`: Atlas One only, the everyday card.
- `david-wsa`: dual brand, Atlas One Full Mark plus a "with Cornerstone PEO" chip carrying the Cornerstone
  logo, and the approved line "Atlas One Solutions, Cornerstone PEO's number one preferred back office
  partner". Every QR and the booking link carry `utm_campaign=wsa`.
- `charity`: built and tested the same way, Atlas One only. **Held, not on the publish list** -- her
  atlasonesolutions.com mailbox does not exist yet. Her booking button reads "Booking coming soon" and is
  disabled, because `people.json`'s booking field for her is `null`.

Contact details on both David cards: David Taylor, Founder and President, david@atlasonesolutions.com,
380-225-5217 (380-CALL-A1S), booking link from `people.json`. The 385 cell and the Cornerstone email and
801 number never appear.

`people.json` gained a `cards` block (`_INTERNAL (do not share)/people.json`): one entry per card slug
with `person`, `title` (overrides the person's base title -- David's cards say "Founder and President"),
`brand_pair`, `campaign`, and `held`.

Per card, at `card/<slug>/` in the repo and mirrored to `A1_Sales/Business Cards/<slug>/`:
- `index.html`: logo(s), name, title, tap to call, tap to email, Book 15 minutes (reads the page's own
  `utm_source`/`utm_medium`/`utm_campaign` and appends them to the booking link), Save my contact (downloads
  `<slug>.vcf`), Share this card (Web Share API, falls back to copying the link), noindex. Atlas brand: four
  colors only, Horas and DM Sans embedded as base64 `@font-face`, no CDN, no photo, the Full Mark lockup as
  the hero.
- `<slug>.vcf`: vCard 3.0, N/FN/ORG/TITLE/TEL/EMAIL, the page URL and the booking URL, a NOTE line (plus the
  Cornerstone line on the WSA card), and the Atlas One mark as a small square base64 JPEG PHOTO (about 5 KB,
  comfortably under the 40 KB budget). Parse tested with `vobject` for all three cards.
- `qr-page.png`/`.svg` and `qr-vcard.png`/`.svg`: two QR codes per card, error correction H, quiet zone 4.
  The page QR carries `utm_source=business-card&utm_medium=qr&utm_campaign=<slug or wsa>` and has the Atlas
  One mark centered in it; the offline vCard QR carries the vCard with no photo (the photo does not fit in
  one QR code at error correction H, so the download button is the way to get the photo-carrying vCard). All
  six PNGs decode-verified against their source payload with `zbarimg`, logo overlay included.
- `lock-screen.png`: 1179x2556, the QR clear of the clock and the bottom buttons.
- `show/index.html`: full screen QR and name, requests a screen wake lock, meant to be added to the home
  screen.
- `print-card.html` / `card-3.5x2.pdf`: 3.5x2in card plus 0.125in bleed each side, crop marks at the trim
  line, front with the logo(s)/name/contact, back with the page QR.
- `print-full-page.html` / `card-full-page.pdf`: letter size for a booth table or front desk, both QR codes
  side by side, labelled "Open my card" and "Save without internet".

Also written to `A1_Sales/Business Cards/`: `Text-my-card.txt` (ready to paste texts for each card plus the
iPhone Text Replacement setup for an `a1card` shortcut), `HOW TO SHARE MY CARD.txt` (lock screen, show page,
text, NameDrop and Share Contact via David's own iPhone My Card, print), and `QR-plan-2026-09-26.md` (also
copied to `_BUILD-LOG/`) -- a tracking table for every future printed piece's QR destination and utm code,
plus the "My card QR" button (see Job 2) shipped now rather than planned.

Verification: Playwright confirmed all six pages (`index.html` and `show/index.html` for all three cards)
load with zero console errors and `scrollWidth` equals the 390px viewport. Device profile tests (WebKit
iPhone 15, Chromium Pixel 7) repeated the same checks plus the booking link's utm parameters and the Save
my contact download; Chromium passed every check on all three cards, WebKit's `<a download>` does not raise
a download event against a `file://` page (a WebKit and local file limitation, not a page defect -- see
Skipped). Screenshots for both device profiles and both page types: `_briefs/assets/run-CQ-cards/`.

## Job 2: rebuild COMMAND, the Sales Kit and the charity rep kit

Added a "My card QR" button to `build_command.py`'s header, next to the theme toggle: in COMMAND it is
wired to the existing Sending as picker (switches with the picker, using a new person-slug-to-card-slug map
built from `people.json`'s `cards` block) and opens that person's `card/<slug>/show/` page in a new tab; in
every `--person` rep kit build it is fixed to that person's own card. Added 4 rows to `catalogue.py` for the
cards: the `david` and `david-wsa` live links, a `charity` note flagged Held, and a folder row for
`A1_Sales/Business Cards/`.

`catalogue_check.py "$MK"`: one pre-existing finding unrelated to this run (`price-list-client-facing-2-pages`
prints prices not listed in `prices.json`), not touched by Jobs 0 to 2.

`build_command.py "$MK"`: **Atlas One COMMAND.html now 210 items** (was 206 before this run), stamp advanced
to the real build clock time (11:46 AM). `Atlas One Sales Kit.html` rebuilt, 59 items. Rendered headless in
Chromium: zero console errors, `#mycardqr` present and pointing at
`https://forms.atlasonesolutions.com/card/david/show/` by default.

`build_command.py "$MK" --person charity`: rebuilt Charity's whole rep kit (Sales Kit, 6 Division Sheets, 5
One Pagers, 8 Sales Pieces, 1 Price List, HTML and PDF). The build's own guard (zero
`david@atlasonesolutions.com` / David Taylor / Cornerstone leaks anywhere in her kit) passed clean -- this
is the "Run CL scanner" the brief asks to keep passing. Confirmed her Sales Kit's `#mycardqr` points at
`https://forms.atlasonesolutions.com/card/charity/show/`, her own held card.

## Assumptions

1. Re-created the 33-row TD SYNNEX Distribution tier from the Run CP Job 1 brief text rather than
   Run CP's own report, since the report's row counts didn't match its own row list and the source had
   none of it; the rebuilt totals (33 new, 13 second source notes, 46 total) match Cowork's audit exactly.
2. Kept the canonical filename `software-catalog-src-2026-09-26.tgz` for the fixed tarball (rather than
   dating it 09-27) since every brief in this project references that exact name; archived the stale
   original instead.
3. Split "Cisco Duo" (Pax8-only) and "Adobe Acrobat and Creative Cloud" (Pax8-only) were left on Hold as
   their own rows rather than merged into the now-Available TD SYNNEX Cloud Marketplace rows for the same
   vendors, since the brief's named list for step 3 didn't include them and they are legitimately a
   different Pax8-specific access question.
4. N-able (Cove Data Protection) marked Available with a note flagging that Cove specifically still wants
   confirming, since the TD SYNNEX Distribution list names "N-able" generally, not Cove by name.
5. Used the vCard-without-photo payload for the offline QR code and kept the photo only in the downloadable
   `.vcf`, since the photo-carrying vCard does not fit in a single QR code at error correction H.
6. Mapped a `people.json` person to a card by matching `cards[*].person`, preferring the entry whose own
   slug equals the person slug (so David's picker selection defaults to `david`, not `david-wsa`); a person
   with no card built yet gets no "My card QR" button rather than a broken link.
7. Gave the Cornerstone lockup its own rounded "with Cornerstone PEO" chip instead of placing the raw logo
   (which has a solid white background, not transparent) directly on the page background, after the first
   render showed it as a stray white box.

## Skipped

1. WebKit does not raise a `download` event for an `<a download>` link against a `file://` page, so the
   Save my contact download check is unverified specifically on the WebKit/iPhone profile (it is verified on
   Chromium/Pixel 7, and the same button and vcf were separately confirmed correct by hand). David's own
   phone check after publish (see below) is the real-world confirmation for iOS.
2. The GHL lane's external tracking script for the card pages (so scans count by `utm_campaign` inside GHL)
   is still just a note carried from Run CN Job 4; it is GHL browser UI work, out of scope for this
   files-and-code terminal.
3. Only the "My card QR" button and the 4 catalogue rows shipped this run for Job 1(j)'s "build now" item;
   the QR plan's other rows (one pagers, division sheets, the Sales Kit cover, benefits sheets) are a plan
   only, each is its own small job per `QR-plan-2026-09-26.md`.

## Questions for David

1. Cowork should re-audit the software catalog (193 rows, Hold 13) before the BRJ zip or the Thomas email
   goes out, per the standing rule after any GHL-JOBS catalog run.
2. Cove Data Protection specifically (inside the now-Available N-able row) still wants confirming with
   TD SYNNEX before it is quoted; flagged in the row's note.
3. Publish the cards when ready: `cd atlas-one-intake-forms && git checkout main && git merge cards-draft
   && git push origin main`. Nothing else changes -- COMMAND, the Sales Kit and Charity's rep kit already
   link to the live `forms.atlasonesolutions.com/card/...` addresses, they just will not resolve until this
   merge and push happen.
4. Do the same real phone checks from `HOW TO SHARE MY CARD.txt` once published: scan the `david` and
   `david-wsa` show pages with an iPhone camera, confirm Save my contact adds the right card with the logo
   as the photo, and confirm GitHub Pages serves `.vcf` as `text/vcard` (the live MIME type check the brief
   flagged as David's own to make).
5. Charity's card is ready the moment her mailbox exists: flip `held` to `false` in `people.json`'s `cards`
   block, no rebuild needed for the card itself, just add her to the publish list and to the WSA style QR
   plan.
