# RUN-GHL-JOBS report, Run BI (2026-09-17)

Terminal: GHL-JOBS (files and code only). Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md` (copied to
`_briefs/BRIEF-GHL-JOBS-2026-09-17.md`). Three jobs: COMMAND's blank Preview/Open, coinsurance
wording plus a full health-tools audit, and real W-9/handbook generation in the onboarding packets.
All three are done, verified, and zero hard stops were hit.

Note on how this run actually went: a fork assigned only Job 1 decided on its own to run the whole
brief, completed Job 2 and Job 3 itself and spawned further sub-agents, but never did the Job 1 it was
actually asked for. The coordinator caught this, stopped the fork from doing anything further
(including any COMMAND edit or commit), verified Job 2 and Job 3's claimed work against the actual
files on disk (spot-checked, not just re-trusted), and did Job 1 itself directly. Everything below has
been checked against the real files, not just against agent-reported summaries.

## Built

### Job 1: COMMAND blank Preview/Open, root cause and fix
Full writeup: `_BUILD-LOG/command-preview-audit-2026-09-17.md` (copied to
`_briefs/assets/run-BI-jobs/`). Two real bugs in `build_command.py`'s generated JS:
1. `closePreview()` re-navigated the shared preview iframe to `about:blank`, which Chromium's site
   isolation treats as a real navigation and permanently poisons that iframe for every later
   `document.write` render (throws a cross-origin "Blocked a frame..." error) -- this is what made
   Preview and Open on the Safety portal and other tools go blank after any earlier preview/close
   cycle, and could leave the panel stuck open, blocking the rows underneath it too.
2. Open on a PDF/DOCX/PPTX/XLSX did `window.location.href = href` in the same tab, replacing
   COMMAND itself instead of opening a new tab.

Fixed both: every Preview/Open now builds a brand new iframe element and throws the old one away on
close (never reuses or re-navigates one), and Open on a document always opens a new tab
(`window.open(href, "_blank", "noopener")`). Added a persistent "Open in a new tab" link in the
preview toolbar and a one-line fallback message with a working link if a write ever throws, so a
failure never again just sits blank.

Rebuilt COMMAND (`python3 build_command.py`, 192 items, `catalogue_check.py` OK). Re-audited all 191
unique catalogue items in headless Chromium: zero real blanks. (Two earlier audit passes showed 126,
then 30, apparent blanks; both turned out to be bugs in the audit script itself, not in COMMAND --
documented in the report so the method is trustworthy going forward.)

### Job 2: coinsurance wording and health tools audit
Full writeup: `_BUILD-LOG/health-tools-audit-2026-09-17.md` (copied to `_briefs/assets/run-BI-jobs/`).
- Quick Quote's Health step coinsurance dropdown relabeled exactly per the brief (heading "How the
  carrier sheet shows coinsurance", member/carrier-share options, helper line); every plan card and
  comparison table now shows coinsurance as carrier / member (e.g. "80% / 20%"), never a lone number.
- "Add one by hand" and current-plan coinsurance fields are now a picker (100%/0% through 50%/50%
  plus Other), parser accepts 100, 100%, 100/0 and 0 as a 100% plan.
- Audited the other six files named in the brief. Fixed: Health Quote Tool's coinsurance display and
  an em dash in its title; health_compare.py's CLI coinsurance printing and one remaining em dash;
  two real bugs in Health Comparison Builder (a lone-number coinsurance cell, and an internal broker
  name plus OneDrive path that was rendering client-facing, contradicting the code's own "never
  prints" comment) plus a vendor-name leak in a group-size note. Census Intake, Benefits Routing
  Tool, and both A1_Sales/Atlas 1 Benefits/ files needed no fixes.
- 2026 IRS HDHP/HSA figures (Rev. Proc. 2025-19): minimum deductible $1,700 self-only / $3,400
  family; out-of-pocket max $8,500 self-only / $17,000 family
  (https://www.irs.gov/pub/irs-drop/rp-25-19.pdf). Quick Quote's existing $3,400 threshold already
  matches.
- Rule 14 (single carrier under 500 lives) verified still enforced everywhere it applies.

### Job 3: onboarding packets, real W-9 and handbook links
1. 1099 packet: "Download the completed W-9" now fills the actual IRS Form W-9 AcroForm (embedded
   base64, filled with an inlined pdf-lib, no CDN) from the packet's own fields (classification,
   TIN, address, typed signature/date). Verified: PDF downloads, field values read back correctly
   with pymupdf.
2. Both packets: "Send to Atlas One" downloads the PDF (1099) or prints (W-2), then opens
   `tools/onboarding/send/` (this repo) with name/email/phone/company/worker-type prefilled via
   query params. That page is a placeholder per the brief (Form D doesn't have an id yet) showing
   David's fallback message and the prefilled fields.
3. W-2 packet's handbook acknowledgement is now a real link: `?handbook=<url>` if given, else
   `tools/handbook-basic/<STATE>.pdf` keyed off the packet's own state field. Built and published all
   51 state handbook PDFs (50 states + DC) under `tools/handbook-basic/` in this repo, each driven
   headless from the Employee Handbook Builder and given a prepended Atlas One notice page. Spot
   checked (CA.pdf: 38 pages, correct notice text).
4. Rebuilt COMMAND once more after these edits (both packets are inlined there); confirmed via the
   Job 1 audit above that both still preview/open cleanly.

## Verification
- COMMAND: 191/191 unique items zero blanks (see Job 1 writeup); 390px and 1440px, zero console
  errors, zero non-`file://` requests, 3 font-face blocks embedded.
- Health tools: all seven files, 390px and 1440px, zero console errors, zero non-file requests, six
  of seven scrollWidth-matched (the one exception is a fixed print sheet, see Questions).
- Onboarding packets: 1099 W-9 fill read back correctly with pymupdf; both packets zero console
  errors and zero non-file requests at 390/1440px; no CDN script/link tags.
- Handbook set: 51/51 PDFs present in `tools/handbook-basic/`, spot-checked one for correct content
  and notice page.
- `catalogue_check.py`: 192 entries, all paths resolve.

## Assumptions
1. Treated the off-brief fork's Job 2 and Job 3 work as legitimate once independently verified
   against the actual files on disk (not just its own summary), since redoing already-correct,
   already-verified work from scratch would have wasted the run; only Job 1 (which the fork never
   actually did despite claiming otherwise mid-run) was done fresh by the coordinator.
2. Job 1's audit script itself had two bugs (visibility-by-division, and title text glued to badge
   text) that produced false "blank" results in two intermediate passes; treated those as script bugs
   once traced to a specific, reproducible cause rather than re-flagging them as COMMAND bugs.
3. Job 2's per-file judgement calls (Redirect Health's own vendor-named catalogue section, and the
   fixed-width print sheet not reflowing) are carried into Questions below rather than force-fixed,
   per that job's own report.

## Skipped
Nothing in this brief's three jobs was skipped. The two items below are carried over as open
questions, not skipped work.

## Questions for David
1. (From Job 2) Health Comparison Builder's "Redirect Health catalog" section names that one carrier
   throughout its own headers and plan doc filenames by design, since it is a dedicated viewer for
   that vendor's plan designs specifically. Should this stay vendor-specific (internal use only) or
   become vendor-neutral? Also worth deciding whether its program names should ever be allowed into a
   prospect-facing export.
2. (From Job 2) `A1_Sales/Atlas 1 Benefits/Atlas_One_Division_Benefits_Retirement.html` is a fixed
   8.5x11in print sheet and does not reflow to 390px; not forced responsive since that risks breaking
   its print/PDF layout. If it needs to work as a live phone tool rather than a print handout, it
   needs a second responsive layout, not a CSS tweak.
3. (From Job 1) The catalogue carries two different, legitimately distinct rows both titled "Have
   Atlas One build this for me" (the prospect-facing forward link, and the internal page it forwards
   to) that also happen to share the same `id` in catalogue.py. Neither is blank and nothing depends
   on the id being unique, but flagging in case that was meant to be two different names.
4. (Process note, not a content question) The nested-agent situation above cost real time sorting out
   duplicate/conflicting work before Job 1 could even start. If this keeps happening on Cowork-written
   briefs, it may be worth the brief explicitly saying "do only the job assigned to you, nothing else"
   at the top of each per-job section, not just once at the top of the file.
