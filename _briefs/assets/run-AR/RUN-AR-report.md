# Run AR report (GHL-JOBS terminal) — one launcher, OneDrive clean-up, calculator restyle

2026-09-14. Three jobs, all complete, committed and pushed. Prior report (Run AQ) backed up to
`_to_delete/superseded-2026-09-14/prior-reports/RUN-GHL-JOBS-report-RunAQ.md`.

## Built

**Job 1 — Atlas One COMMAND (one internal launcher) and Atlas One Tools (one shareable file)**

- `_INTERNAL (do not share)/catalogue.py`: 170 entries, the single source of truth for both outputs. Merged
  and deduped (by resolved absolute path, richer blurb kept) from build_portal.py's 44-tool SECTIONS, the
  retired Master Hub's 167-row ITEMS array, and the retired Tools Hub's 32-tool TOOLS array. Fields: id,
  title, blurb (dash-free), path (relative to the Marketing root), kind, division, audience, inline, badge,
  pinned. 12/12 of the named pinned items matched by exact path: Quick Quote, Quote Cockpit, Health Quote
  Tool, Time and Cost Savings Discovery, Vendor & Software Audit, Prospect Pitch Deck, Prospect Pitch Deck
  First Meeting cut, Membership Comparison (one page), Proof Sheet, Sales Conversation Playbook, Prospect
  Onboarding Tracker, Payroll → GL Import.
- `_INTERNAL (do not share)/catalogue_check.py`: fails the build if any catalogue path does not resolve. Passes
  clean (`catalogue_check: OK, 170 entries, all paths resolve.`).
- `_INTERNAL (do not share)/build_command.py`: the new builder (adapted from build_portal_single.py's
  base64-park/iframe-srcdoc mechanism, its size handling, and its build-stamp logic). Writes:
  - `Master_Kit/Atlas One COMMAND.html` — every internal/prospect/client entry, 170 items, 46.9MB.
  - `Master_Kit/Atlas One Tools (share with prospects).html` — prospect-only, 46 items, 21.3MB, no Internal
    section, no rate card, no relative links (everything inlined).
  - Both refuse to write to `Atlas One PORTAL.html` (same guard as build_portal.py).
  - The prospect build is grep-guarded: hard-fails on "cornerstone", "g&a", "verohcm" anywhere in any
    prospect-audience tool's raw source, and on "margin"/"commission"/"wholesale" everywhere except a small,
    hand-reviewed, commented allowlist (`FORBIDDEN_ALLOWLIST` in build_command.py — see Assumptions).
- New layout: left rail (Start here + the six divisions in official order + Sell & Pitch / Decks / Pricing &
  Quotes / Agreements / Email templates / Intake & Client / Industry overlays / Internal, each with an item
  count), collapsing to a "☰" top-bar toggle under 700px. Main area is rows (kind icon, title, one-line
  blurb, badge chip, Preview button for inlined html, Open button), grouped under Tools/Builders/Documents/
  Decks/etc. sub-headings inside each section. Search at top filters every row live. Fonts: Horas + DM Sans,
  embedded byte-for-byte from `tools/self-assessment/index.html`'s existing `@font-face` block (saved as
  `_INTERNAL (do not share)/fonts_embed.css` so build_command.py can reuse it without re-encoding). Status
  shown by form only (solid Open button, tinted badge chip, outlined Preview button, a star glyph for
  pinned) — four brand colours, checked in both light and dark (`prefers-color-scheme`).
- Fixed one real content leak found by the grep guard: the 53-calculator tool's helper text read "Atlas One
  brokers PEO across Cornerstone, G&A Partners, and Vero HCM" — rewritten to "Atlas One brokers PEO across
  several national carriers" (vendor-neutral, matches the brand rule that public tools never name vendors
  anyway).

**Job 2 — OneDrive duplicate/version/zip/junk/stale-content audit** (done by a parallel fork; folded in here)

- Report: `_BUILD-LOG/onedrive-audit-2026-09-14.md` (also at
  `atlas-one-intake-forms/_briefs/assets/run-AR/onedrive-audit-2026-09-14.md`).
- 2,482 files scanned in scope. 55 exact-duplicate sets (79 files; 45 moved, 34 left in place because they sit
  under a protected path). 25 zip files (14 confirmed as the protected `A1_Final Brand/` brand-kit deliverable,
  untouched; 5 redundant zips moved; 1 handled by the exact-duplicate pass; 5 left as list-only partial
  overlap). 71 junk files (`~$` locks, `.DS_Store`; 48 moved, 23 skipped under protected paths). 7 version
  families (list-only; 6 are the terminal's own dated build-journal checkpoints working as designed, 1 real
  question about three Master Blueprint docx versions). Zero live stale phone/price hits (every occurrence of
  the old number or the retired price tiers is in a build-journal or draft file, correctly left untouched).
  1,306 unreferenced-file candidates by heuristic, almost all bundled PDF/template-library folders meant to
  ship as a set — listed by group, nothing moved. 93 files moved total, all into
  `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-14/duplicates/` (with `zips/` and `junk/`
  subfolders), nothing deleted. A second, independent process was found to have raced on the same duplicate/
  junk logic concurrently (see Assumptions); one file (`04 Safety Library/.../_manifest.json`) had briefly
  had zero live copies as a result and was restored from `_to_delete` immediately, verified, no data lost.

**Job 3 — restyle the two calculator/generator hub files to the same layout**

- `06 Calculators and Tools (NEW Aug 2026)/Atlas One Calculators (53 tools).html`: replaced the top pill-filter
  + card-grid browse screen with a left rail of 7 categories (with counts, collapsing to a "Categories ☰" top
  bar under 700px) and rows (title, one-line blurb, industry tags, Open button) grouped under each category
  heading in the main area; the industry pill filter is kept as a secondary filter row under search. Horas +
  DM Sans embedded (this file had no font embedding before — used a system-ui stack). All 53 calculator forms
  and their `A1Nav.open/home/step` navigation are untouched; print button kept.
- `06 Calculators and Tools (NEW Aug 2026)/Atlas One Business Tools (17 generators).html` (28 tools, filename
  kept as-is per the brief): it already had a sidebar+form/preview shell, but the sidebar was a flat,
  un-grouped, un-searchable list of 28 buttons. Added 5 categories (Money & Billing 6, Field & Job Site 6, HR
  & Onboarding 9, Expenses & Assets 3, Operations & Identity 4 — invented groupings, see Assumptions), each
  collapsible with a count, a search box that filters by title/description and auto-expands matching
  categories, and a "Generators ☰" mobile toggle under 700px. Each row now shows the generator's one-line
  description under its title. All 28 generator forms/PDF exports are untouched.
- Both backed up to `_to_delete/superseded-2026-09-14/calculators-before/` before editing.
- Rebuilt `Atlas One COMMAND.html` and `Atlas One Tools (share with prospects).html` afterward so the inlined
  copies of both restyled files are current (final sizes: COMMAND 46.9MB / 170 items, Tools 21.3MB / 46 items).

## Retired

- `Master_Kit/Atlas One PORTAL.html` → `_to_delete/superseded-2026-09-14/launchers/`
- `Master_Kit/Atlas One — Tools Hub.html` → `_to_delete/superseded-2026-09-14/launchers/`
- `Atlas_One_MASTER_HUB.html` (Marketing root) → `_to_delete/superseded-2026-09-14/launchers/`
- `_INTERNAL (do not share)/build_portal_single.py`'s CLI now prints "superseded by build_command.py" and
  exits; the file is kept in place (build_command.py does not import from it, only from build_portal.py's
  SECTIONS/header_copy, which were only needed at catalogue-merge time, not at runtime).
- Repo `CLAUDE.md`'s Portal section rewritten to document `build_command.py`/`catalogue.py` as the new
  rebuild path.

## Verification

- Headless Chromium (Playwright), all four combinations (1440×900 and 390×844, light and dark
  `prefers-color-scheme`) for both `Atlas One COMMAND.html` and `Atlas One Tools (share with prospects).html`:
  0 console errors, 0 non-`file://` network requests, `scrollWidth === viewport width` at 390px. Screenshots
  in `_briefs/assets/run-AR/shots/` (command-*.png, tools-*.png).
- Confirmed 12/12 pinned items present (23 `.pinmark` DOM nodes because each pinned item legitimately renders
  twice — once under "Start here", once in its native division section, a deliberate favorites-style
  duplication, not a bug).
- Confirmed the prospect file has no "Internal (do not share)" section in the DOM and passed the forbidden-term
  build guard.
- Click-through on 8 representative rows across kinds: an inlined tool's Preview button opens its content in
  the in-page panel (verified `<body>` present inside the iframe); a relative-linked deck/doc/agreement's Open
  button carries an href that resolves to a real file on disk (verified with `fs.existsSync`); rows in
  Internal, Technology & Operations, Sell & Pitch and Financial Services sections all resolve correctly.
- Job 3: both restyled files render clean at 1440/390 (0 errors, 0 network, scrollWidth OK at 390). Category
  filter and row-click-to-open verified on both files (Labor Burden calculator opened via category+row click;
  PTO Request generator opened via category+row click) — screenshots `calc53-*.png`, `gen28-*.png` in the same
  shots folder.
- Job 2: verification is in `onedrive-audit-2026-09-14.md` itself (file-count tables, hash-based duplicate
  confirmation, zip content-list comparison).

## Assumptions

1. Division/audience for the merged catalogue is a heuristic, not a source-of-truth field the legacy launchers
   carried: Tools Hub-sourced entries default to `audience: prospect`; build_portal.py entries default to
   `prospect` unless already badged "Internal"; everything sourced only from the Master Hub defaults to
   `internal` (safer default given the file carries agreements, pricing and internal notes), except its
   `intake` category which is `client`. Division is likewise inferred from each source's own category, mapped
   onto the brief's named left-rail sections.
2. Six stale paths from the three old launchers had moved on disk since those catalogues were last built
   (`templates.html`, `Labor Law Poster Center.html`, `PEO Comparison Tool`, `Workforce Software Comparison`,
   two Branded Intake Forms) — remapped to their current real locations (all under the BRJ kit / Website
   Package / `_HANDOFF BRJ 2026-08-27` folders) rather than dropped.
3. Two catalogue entries were genuinely gone, not moved: "AI Email Assistant Client Setup Kit" and "Command
   Center" (the latter confirmed already renamed to "Command Center (superseded)" by an earlier run) — dropped
   from the catalogue rather than remapped.
4. Two catalogue entries were the old launchers pointing at *each other* (a Master Hub row linking to
   `Atlas One PORTAL.html`, another to `Atlas One — Tools Hub.html`) — removed, since keeping them would have
   put a dead link into the very file meant to replace them.
5. Reclassified "Payroll → GL Import" from prospect to internal audience: its "prepared by: Cornerstone PEO /
   G&A Partners" dropdown is explicitly internal-only branding logic, not something a prospect should see.
6. The forbidden-term grep guard is checked against each prospect-audience tool's raw HTML source before
   base64-parking (checking the final built document would be useless — base64 hides plaintext). "margin",
   "commission" and "wholesale" are common English words that also appear as legitimate prospect-facing form
   labels (a tool asking the prospect for their own gross margin, broker commission, or bonus/commission pay
   type) or third-party library internals (jsPDF's `__cell__.margins`) or government-body names (EEOC, a state
   tax commission). Every current hit for those three terms was read in full context by hand and confirmed
   safe; each is listed by exact file and term in `FORBIDDEN_ALLOWLIST` inside build_command.py with the
   reviewed reason in a comment. The vendor names ("cornerstone", "g&a", "verohcm") are never allowlisted —
   any appearance of those three still hard-fails the build everywhere.
7. The 5 categories invented for the 28-generator file (Money & Billing, Field & Job Site, HR & Onboarding,
   Expenses & Assets, Operations & Identity) are a new grouping — the file never had categories before, only a
   flat button list. Grouped by what each document is actually for; open to a different cut if David wants one.
8. A BRJ Resource Library catalog page (`Atlas One — Complete Kit for BRJ/5. Resource Library Catalog/...`)
   lists "Atlas One PORTAL (all-tools launcher)" with a website-route slug `/portal/` — left untouched: it
   describes a public-site route for a third-party developer handoff, unrelated to the Master Kit file that
   was just retired, and editing BRJ handoff copy was outside this run's narrow scope.
9. Two OneDrive audit jobs collided (this session's Job 2 and a concurrent duplicate-scan process); see the
   audit report's own Verification section for the one file that briefly had zero live copies and was
   restored — no data was lost, but it means two processes ran the identical safe-move logic on the same tree
   at the same time tonight, worth knowing if another parallel run is queued.

## Skipped

- Legacy `.doc`/`.ppt`/`.xls` (not `.docx`/`.pptx`/`.xlsx`) scanning for stale phone/price content — carried
  over as a known gap from Run AQ, not re-attempted this run (out of Job 2's scope as scoped this time).
- Editing the retired-price/old-phone hits found in `.docx`/`.pptx`/`.xlsx` files (from Run AQ's prior scan) —
  the harness's auto-mode classifier blocks in-place Office-file overwrites even with a backup; not
  re-attempted here since Job 2 this run was OneDrive duplicate/junk cleanup, not the Office-file text sweep.
- The BRJ Resource Library catalog page's stale Portal reference (see Assumption 8) — read-only handoff
  document, left as a note rather than edited.

## Questions for David

1. Does the 5-category grouping invented for the 28 business-document generators (Assumption 7) match how you
   think about them, or would you group them differently (e.g. by department instead of by document type)?
2. Three versions of a "Master Blueprint" docx were found in the OneDrive audit (version-family table) — which
   one is current? Not moved, listed only.
3. The audit's old-logo-filename check (brief section 2a) was skipped: no confident candidate for "the OLD
   globe A1 logo file name" was found without more context on what that filename actually is — can you confirm
   the exact old logo filename so a future pass can search for it specifically?
4. One zip (`Book Keeping Docs.zip`/`Archive.zip`) was found to contain a superseded V7 internal pricing doc no
   longer present live outside the zip — it was moved to `_to_delete/.../duplicates/zips/` along with the
   others; flag if you actually wanted that V7 doc kept accessible somewhere.
5. Given tonight's OneDrive Job 2 collision with a concurrent process (Assumption 9): are two GHL-JOBS terminal
   sessions being run intentionally in parallel on the same brief, or should only one run at a time going
   forward to avoid this kind of race?
