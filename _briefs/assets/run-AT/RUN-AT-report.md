# RUN-AT-report.md (GHL-JOBS terminal, 2026-09-15)

Both jobs of the brief (`_BUILD-LOG/BRIEF-GHL-JOBS.md`, copied to `_briefs/RUN-AT-GHL-JOBS-2026-09-15.md`
in the repo) are complete, verified, committed and pushed.

## Built

### Job 1: agreement PDF fonts fixed

- **Diagnosed the actual bug.** Run AS's PDFs embedded FrankRuhlHofshi and LinuxLibertine instead of
  DM Sans/Horas even though the TTFs were already installed in `~/Library/Fonts/` (that install was
  Run AS's own fix attempt). Reproduced the wrong-font PDF with a fresh `soffice --headless --convert-to
  pdf` after confirming `fc-match "DM Sans"` and `fc-match "Horas"` resolve correctly at the fontconfig
  level. The real problem: macOS itself never registered the fonts. `system_profiler SPFontsDataType`
  never listed DM Sans or Horas, and a direct CoreText registration attempt (`CTFontManagerRegisterFontsForURL`
  via ctypes) failed with `OSStatus -50`. This looks like a fontd/headless-session limitation specific to
  this machine (LibreOffice on macOS uses CoreText, not fontconfig, for its actual font list), not a docx
  or LibreOffice bug per se.
- **Switched the PDF step per the brief's documented fallback.** `tools/agreements/generate.py` now builds
  every document as a list of content blocks (`Doc` class) and renders that same list twice: once to a
  `.docx` master via python-docx (unchanged tool, still the editable file) and once to HTML, printed with
  headless Chromium via Playwright (`tools/agreements/_render_pdf.mjs`). The HTML uses the same
  `fonts_faces.css` Horas/DM Sans base64 `@font-face` block `tools/self-assessment/index.html` embeds, so
  the PDF renderer never depends on the macOS font registry at all.
- **Regenerated all 19 docx+PDF pairs** into `A1_Sales/A1 Agreements/2026-09-15 masters/`. Backed up the
  19 wrong-font PDFs to `_to_delete/superseded-2026-09-15/agreements-wrong-fonts/` (docx files were never
  wrong, only the PDF conversion step; docx masters are untouched content-wise, just regenerated from the
  same block list for consistency).
- **Tightened the print CSS once** after the first pass left 4 documents with a stray orphaned footer line
  on a near-blank page 2 (smaller margins and line-heights, no content changes). 18 of 19 documents are now
  a single page; the Master Client Services Agreement (12 clauses) is a legitimate 2 pages, same as before.

### Job 2: web pitch page at `tools/pitch/`

- `tools/pitch/extract_slides.py` (python-pptx) pulls every slide's title/body/notes from
  `Atlas_One_Prospect_Pitch_Deck.pptx` into `tools/pitch/slides.json` (16 slides). `tools/pitch/build.py`
  renders `index.html` from that JSON, pulling every sentence by slide/line index (never hand-typed) and
  running a mechanical dash-fixer (digit-dash-digit becomes "to", every other em/en dash becomes a comma)
  to satisfy the no-dashes brand rule the 2026-09-15 deck copy predates.
- **Eight tabs** map all 16 slides: Overview (1), The problem (2, 3), Six divisions (4, 5, plus the three
  deep-dive slides 11-13 folded into an accordion under each of the six division cards so the tab does not
  become a scrolling wall), How it works (6), A sample number (7, 8), Proof (9), Membership (10, tiers
  overridden per the brief), Next step (14, 15). Slide 16 (the presenter's own "hide this before
  presenting" cheat sheet) is deliberately excluded, see Assumptions.
- **Personalization.** `?for=Company` changes the header to "Prepared for Company". `?ee=N&industry=X`
  reruns the Total Impact Model's own `compute()` formula (same LINES model, same gross/net math as
  `Atlas_One_Total_Impact_Model.html`), fed the same 25-employee `SAMPLE` line items that file already
  ships (which are themselves the deck's slide 8 numbers) and scaled by `N/25`. No new formula was
  invented. Without parameters the tab shows the deck's 25-employee sample verbatim.
- **Membership tab** shows only Essential ($99/mo) and Professional ($399/mo) with their setup-fee lines
  from `prices.json`; Enterprise and Concierge read "Built around your business. Starts with a 30 minute
  Back Office Audit." (the one place this script writes text that is not sourced from slides.json, since
  it is a website decision overriding the deck, not deck copy).
- **Brand.** Horas + DM Sans embedded (byte-for-byte `fonts_faces.css` extracted from
  `tools/self-assessment/index.html`), the real transparent Full Mark SVG (`A1_Final Brand/1. Logos/Full
  Mark/Full Color/...svg`, 7.2 KB, only navy and periwinkle fills, no external font dependency), four
  colours only, "Serving businesses in all 50 states" in the footer, `tel:+13802255217`, a booking button
  (`api.leadconnectorhq.com/widget/groups/book-david`) on every tab, a Download PDF button to the copied
  `Atlas_One_Prospect_Pitch_Deck_First_Meeting.pdf`, a print stylesheet (one page per tab).
- **Dark mode**, not explicitly built into any prior GHL tool but required by this brief's verification
  line ("light and dark"): added a `prefers-color-scheme: dark` palette using only the same four brand
  colours (card surfaces become low-alpha tints of paper/periwinkle rather than a fifth colour). The logo's
  navy fill is swapped to paper in dark mode via a CSS custom property inside the inlined SVG, otherwise it
  disappeared against the dark navy page background.

## Verification

- **Font proof (Job 1).** `strings <pdf> | grep BaseFont` on every one of the 19 regenerated PDFs shows
  only `Horas-Medium`, `DMSans-Regular`, `DMSans-Bold`; zero `FrankRuhl`/`LinuxLibertine` hits across all
  19 (grep loop over the whole folder). Two file proofs:
  - `Atlas_One_Master_Client_Services_Agreement.pdf`: `AAAAAA+Horas-Medium`, `BAAAAA+DMSans-Regular`,
    `CAAAAA+DMSans-Bold`
  - `Sample_Proposal_Membership.pdf`: same three, same subset tags
  Looked at all 19 first-page renders (`sips`) plus the Master Client Services Agreement's and Bookkeeping
  Schedule's second pages: headings in Horas, body in DM Sans, brand colours, signature tables intact, no
  dashes. Screenshots in `_briefs/assets/run-AT/shots/`.
- **Pitch page (Job 2).** Headless Chromium at 1440 and 390, light and dark (`colorScheme: "dark"`): zero
  console errors, zero non-`file://` network requests, `scrollWidth === clientWidth` at both viewports.
  Every one of the 8 tabs opened and screenshotted (button click, not hash-only navigation, since a
  same-document hash change on a `file://` URL does not re-run inline scripts in Chromium, confirmed by
  reproducing the stale-tab bug once and fixing the test, not the page). One personalized render
  (`?for=Tell Me More LLC&ee=60&industry=construction`): header changed, sample-number tab recomputed to
  $44,160 found / 53 hrs/mo / $5,283 fee / $38,877 net. Mobile `<select>` dropdown tested (switches tabs
  correctly at 390px, hidden at desktop width). Division accordion tested open/close, and confirmed dark
  mode legibility. Print stylesheet rendered to a 9-page PDF (8 tabs plus a trailing blank page) and looked
  at page 1. Screenshots in `_briefs/assets/run-AT/shots/` (pitch_*.png, 15 files).
- **Live URL.** `https://forms.atlasonesolutions.com/tools/pitch/` returned 200 after the push (checked
  with a short poll, propagation was under two minutes).
- **catalogue.py / COMMAND.** `catalogue_check.py` passes clean at 185 entries. COMMAND rebuilt twice
  (once after Job 1, confirming the stamp and 184-item count were unaffected by the PDF regeneration since
  paths didn't change; once after Job 2, 185 items, the new pitch page entry resolves).

## Assumptions

1. **Slide 16 excluded from the client-facing page.** It is explicitly labeled in its own body text
   "Reference: how to run this deck" and its speaker notes say "hide it before presenting." Treated as
   presenter-only material, not deck content a prospect should see, so it has no tab and none of its text
   reaches `index.html`.
2. **Dash-fixing rule.** A digit-dash-digit range ("10-20", "15-30%") becomes "10 to 20" / "15 to 30%"; any
   other em/en dash (used throughout the deck as a pause or an explanation) becomes a comma. Applied
   mechanically and uniformly, not sentence-by-sentence by hand, so it is possible one or two resulting
   sentences read slightly less punchy than a human rewrite would. Every rendered tab was read after the
   fix and nothing looked broken, but flagging the mechanism in case a specific line should be manually
   tightened later.
3. **Deep-dive to division mapping (Six divisions tab).** The deck's three "deep dive" slides (11-13) cover
   six divisions across three slides with four bullets each. Split each slide's four bullets between the
   two or three divisions it actually covers (e.g. slide 12's four bullets split 2/2 between Benefits &
   Retirement and Financial Services; slide 13's four bullets split 1/1/2 between Risk & Insurance,
   Technology & Operations, and Business Consulting) rather than showing the same four bullets under every
   division on that slide. This is the more accurate mapping but is an interpretation, not something the
   deck states explicitly.
4. **`?industry=` is cosmetic, not a second scaling factor.** It changes the sample-number tab's headline
   and intro sentence ("a 60-person construction company") but does not change the dollar math, which
   scales on employee count only, reusing the Total Impact Model's own line items. Inventing an
   industry-specific multiplier would have been a new formula, which the brief said not to do.
5. **catalogue.py entry set `inline=False`.** Every other similar prospect-facing tool in the catalogue is
   `inline=True` (base64-parked into COMMAND's own HTML, opened in an iframe via `document.write`). The
   pitch page has a real relative link (the Download PDF button) that would not resolve once base64-parked
   into a different file's iframe with no matching base path, so this entry opens as a normal link to the
   copied file on disk instead, keeping the download working when browsed from COMMAND. The real, public
   page at `forms.atlasonesolutions.com/tools/pitch/` is unaffected either way.
6. **Master Kit copy of the pitch page.** Copied `tools/pitch/index.html` and the PDF into
   `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Prospect_Web_Pitch.html` (and the PDF alongside it)
   so `catalogue.py`'s path resolution (relative to the Master Kit's parent folder) could find it, matching
   the existing pattern for every other repo-sourced tool in the catalogue (e.g. the Back Office
   Self-Assessment). The repo file stays the source of truth; re-run `build.py` and re-copy if the deck or
   page changes.
7. **Membership tab setup-fee wording** for Essential/Professional comes verbatim from `prices.json`
   (`tools/agreements/prices.json`, the same file Job 1's agreements generator uses), not retyped.

## Skipped

- Nothing in either job was skipped. Both hard stops that blocked prior runs (Azure production deploy,
  overwriting existing OneDrive docx/pptx/xlsx files) were not relevant to this brief; no email/SMS, no
  file deletion (only moves to `_to_delete/`), no production deploy, no spending.

## Questions for David

1. **Attorney review banner.** The Master Client Services Agreement and the standalone Hold Harmless still
   carry the "ATTORNEY REVIEW PENDING" banner from Run AS. Not touched this run since fixing that wasn't in
   scope; flagging since these are now the correct-font versions that could otherwise look ready to send.
2. **Deep-dive division split (Assumption 3).** If you'd rather every division on a shared deep-dive slide
   show all four of that slide's bullets (matching the deck's own slide grouping) instead of the split I
   made, that's a one-line change in `tools/pitch/build.py`'s `DIVISIONS` list.
3. **Industry-specific sample-number math.** Right now `?industry=` only changes copy, not the dollar
   figures. If you want industry to actually shift the estimate (e.g. construction skews workers' comp
   higher), that needs a real per-industry multiplier defined somewhere, which the brief didn't specify and
   I didn't want to invent.
4. **Pitch page COMMAND entry not inlined (Assumption 5).** Every other similar tool base64-parks into
   COMMAND; this one opens as a real link so the Download PDF button keeps working. If you'd rather have it
   inlined for consistency (accepting a broken Download PDF button only inside COMMAND, not on the live
   site), say so and I'll flip `inline=True`.
