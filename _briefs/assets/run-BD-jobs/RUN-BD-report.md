# Run BD report, GHL-JOBS terminal (files and code only)

Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md`, copied to the repo at `_briefs/BRIEF-GHL-JOBS-2026-09-16-RunBD.md`.
Prior report (Run BC) backed up to `_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunBC.md`.

## Built

### Job 1: sales banner suppressed in print on all five client document builders

Files edited, all in `06 Calculators and Tools (NEW Aug 2026)/`, backed up first to
`_to_delete/superseded-2026-09-16/builders/before-runBD/`:
- Employee Handbook Builder (Bilingual 50-State).html
- Safety Manual Builder (Bilingual OSHA).html
- W-2 At-Will Employment Agreement Builder (Atlas One).html
- Independent Contractor Agreement Builder (Atlas One).html
- NDA Builder (Atlas One).html

Added `#atlas-cta-banner{display:none !important;}` inside each file's existing `@media print{...}` block
(matched to each file's own selector style, since the five files use three different print-hiding patterns:
plain selector lists, a `.cta-banner`/`.premium-banner` class approach, and a `visibility:hidden` isolation
pattern in the NDA builder). The `#atlas-cta-banner` div is the top banner reading "Want it done for you? ...
Email David, Book a call, or call 380-CALL-A1S" - it predates each file's print block and is addressed by id,
not class, so no existing rule matched it.

Grepped every HTML file under `06 Calculators and Tools (NEW Aug 2026)/` and `08 ROI Quote Master Template/` for
other unhidden banners, badges, or CTA strips per the brief. Found a SECOND, separate promo strip in three of the
five files (`class="cta-banner"` in the W-2 and NDA builders reading "Premium builder... Request a custom build",
`class="premium-banner"` in the Independent Contractor builder with the same message), plus a `premium-badge`
pill in the topbar of four files. All of these were already correctly hidden in print by pre-existing rules (the
topbar hide catches the badges; the W-2 and Independent Contractor builders already had explicit
`.cta-banner`/`.premium-banner` print rules; the NDA builder's visibility-based print isolation already hides
everything outside `#document`). Only the id-based `#atlas-cta-banner` banner was missing its rule, in all five
files. `atlas-cta-banner` does not appear anywhere outside these five files (checked every HTML file in both
folders).

### Job 2: retired the last two duplicate builders, and fixed a broken-link gap left by Run BB

Confirmed via grep that `catalogue.py` references only three files from `Atlas One — Complete Kit for BRJ/`
(templates.html, the Labor Law Poster Center, the PEO Comparison Tool) and nothing under
`10. Premium Builders (for paywall)/`. Moved the last two duplicates there (Employee Handbook Builder Bilingual
50-State, Safety Manual Builder Bilingual OSHA) to
`_to_delete/superseded-2026-09-16/builders/Complete Kit for BRJ premium builders/`, next to the three Run BB
already retired there.

While checking for other links into that folder (per the brief), found that the Complete Kit's own
`⭐ START HERE — BRJ Index.html` links to all five premium builders through a `PB="10. Premium Builders (for
paywall)/"` path prefix in its JS. Three of those five links (Independent Contractor, NDA, W-2) were already
broken, since Run BB moved those three files out of that folder on 2026-09-16 without updating this index - a
gap in that run that was not caught until now. Repointed all five entries to
`PB="../06 Calculators and Tools (NEW Aug 2026)/"` so every link on the page now resolves to the live copy.
Backed up the index file first, to the same `before-runBD` backup folder.

The Resource Library Catalog page's two mentions of these builder names ("Employee Handbook Builder (Bilingual,
50-state)", "Safety Manual Builder (Bilingual, OSHA)") are plain descriptive text with a suggested website-route
slug (`/tools/handbook-builder/`, `/tools/safety-manual-builder/`), no local file href - nothing to repoint
there.

`10. Premium Builders (for paywall)/` is now empty.

### Job 3: verify and rebuild

Wrote a Playwright script (headless Chromium, the project's pinned copy) that for each of the five builders:
opened the file from `file://`, filled the minimum identifying field (company/employee/contractor/counterparty
name - most fields already ship with an "Atlas One Solutions" default), ticked the `#hhGate` Hold Harmless
checkbox on the three agreement builders (the Handbook and Safety Manual builders have no such gate), took an
on-screen screenshot, checked `scrollWidth` at a 390px viewport, then `emulateMedia('print')` and `page.pdf()`.
Console errors and non-`file://` network requests were tracked for the whole session, not just page load.

`pdftotext` is not installed on this machine (noted by Run BC); used `pymupdf` for page-1 text extraction
instead, consistent with that run's assumption.

## Verification

All five, zero console errors, zero non-`file://` requests, `scrollWidth` equals a 390px viewport, banner
confirmed visible on screen (DOM check plus a direct look at the W-2 screenshot):

**Employee Handbook Builder** (35-page PDF), page 1 starts:
```
EN
Employee Handbook
Policies & Procedures
Test Company LLC
Effective …
```
No banned phrase, no dash character.

**Safety Manual Builder** (19-page PDF), page 1 starts:
```
EN
Safety Manual
Health & Safety Program
Test Company LLC
Effective …
```
No banned phrase, no dash character.

**W-2 At-Will Employment Agreement Builder** (4-page PDF), page 1 starts:
```
Atlas One Solutions
OFFER OF EMPLOYMENT & AT-WILL AGREEMENT
September 16, 2026
```
No banned phrase, no dash character. Rendered page 1 to a PNG and looked at it directly: clean letterhead and
offer letter body, no banner, no premium/custom-build strip anywhere on the page.

**Independent Contractor Agreement Builder** (6-page PDF), page 1 starts:
```
INDEPENDENT CONTRACTOR AGREEMENT
This Independent Contractor Agreement (the "Agreement") is entered into as of [Effective
Date] (the "Effective Date"), by and between Atlas One Solutions (the "Company"), and Jane
Doe (the "Contractor")...
```
No banned phrase, no dash character.

**NDA Builder** (5-page PDF), page 1 starts:
```
MUTUAL NON-DISCLOSURE AGREEMENT
```
No banned phrase, no dash character.

Banned phrases checked on every page-1 dump: "Want it done", "Email David", "Book a call", "380-CALL", "Request
a custom", "Get a custom-built". Zero hits on any of the five.

Screenshots (five on-screen PNGs) and the five print PDFs in `_briefs/assets/run-BD-jobs/shots/`. The five
page-1 text dumps at `_briefs/assets/run-BD-jobs/` (handbook-page1.txt, safety-manual-page1.txt,
w2-offer-letter-page1.txt, ic-agreement-page1.txt, nda-page1.txt).

`catalogue_check.py`: 192 entries, all resolve (unchanged count - this run's fixes were inline HTML/JS edits and
a Complete Kit index repoint, not catalogue path changes). Backed up prior `Atlas One COMMAND.html` to
`_to_delete/superseded-2026-09-16/command-before-runBD/`, rebuilt it (192 items, 48,648,048 bytes, stamp "Atlas
One COMMAND: build Sep 16, 2026 6:39 PM"), verified in headless Chromium at 1440px: zero console errors,
`scrollWidth` equals viewport.

## Assumptions

1. `pdftotext` is not installed on this machine; used `pymupdf` for PDF text extraction throughout, matching the
   assumption Run BC already logged.
2. "Fill the minimum fields" was read as the smallest edit needed to get a populated, non-placeholder-only
   document: one identifying name field per builder, leaving every other field at its shipped default (most of
   which already default to real values, e.g. "Atlas One Solutions" as the company name). This was enough for
   every generated PDF to carry real body content and clear the print check.
3. Left one now-stale sentence of prose in the Complete Kit's `START HERE` index ("Folder 10 — Premium
   Builders... no paywall needed right now") describing where the five builders live. It carries no link (the
   actual `href`s were fixed) and rewriting kit narrative copy felt outside a print-suppression and
   duplicate-retirement job; flagging in case David wants it reworded now that the folder is empty.
4. Treated the broken links from Run BB (three of the five `START HERE` index entries already pointing at files
   that no longer existed) as in scope for this job's "if anything else links to those two paths, repoint it"
   instruction, since fixing only the two named in this brief would have left three of the five links still
   broken on the same page for no benefit. Repointed all five together.
5. Verified `scrollWidth` at a 390px viewport only (the standard this repo has used since Run BB/BC), not
   separately at tablet width, consistent with precedent.

## Skipped

Nothing skipped. All three jobs in the brief were completed.

## Questions for David

1. The Complete Kit's `START HERE` index still had three broken tool links (Independent Contractor, NDA, W-2)
   left over from Run BB moving those files out of `10. Premium Builders (for paywall)/` without updating this
   index. Fixed as part of this run (see Job 2) - worth a quick look at that page to confirm the five links open
   correctly for whoever last opened it live.
2. Should the "Folder 10 — Premium Builders" descriptive paragraph in that same index be reworded or removed,
   now that all five builders live in `06 Calculators and Tools` and folder 10 is empty?
3. Is there a broader lesson here: when a run moves or renames a file, should every run's checklist include a
   repo-wide grep for the old filename/path before closing the job? This is the second time a file move left a
   stale link elsewhere in the kit (Run BB's move, caught in this run).
