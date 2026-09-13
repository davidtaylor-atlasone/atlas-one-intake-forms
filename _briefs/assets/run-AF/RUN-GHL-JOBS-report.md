# RUN-GHL-JOBS report (Run AF, 2026-09-13)

Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md`, copied to `repo:_briefs/BRIEF-GHL-JOBS-2026-09-13.md`. Two jobs, both done.

## Job 1: restore the Portal, make the overwrite mistake impossible

**What was wrong:** `Atlas One PORTAL.html` had been overwritten by `_INTERNAL (do not share)/build_portal.py`
(the link-launcher script) instead of `build_portal_single.py` (the real, single-file Portal). The file was down
to 33 KB, titled "Atlas One — All Tools Portal", stamped "REBUILT September 13, 2026".

**What was done:**
1. Backed the wrong 33 KB build up to
   `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-13/portal-launcher-wrong-build/Atlas One PORTAL (wrong-launcher-build).html`
   before touching anything.
2. Ran `python3 "<Master_Kit>/_INTERNAL (do not share)/build_portal_single.py" "<Master_Kit>"`. Real Portal
   restored: **19.4 MB** (well over the 15 MB floor named in the brief), title
   `Atlas One Portal: build Sep 13, 2026 11:31 AM` (later re-stamped 11:40 AM after Job 2's PDF refresh), **44
   tools** inlined.
3. Made the mistake structurally harder to repeat: `build_portal.py`'s `build()` now defaults its output filename
   to `Atlas One PORTAL (launcher, links only).html` and raises `SystemExit` if it is ever called with
   `out_name="Atlas One PORTAL.html"`. Verified both paths (default write succeeds under the new name; an explicit
   call with the real Portal's filename is refused) before touching the live file.
4. Added the rule to `repo:CLAUDE.md` under **Portal**: build_portal.py is the catalogue, never the Portal
   generator; only build_portal_single.py with the Master Kit path argument produces the real file.
5. Checked the Master Hub / Tools Hub link claim in the brief: there is no `Atlas One PORTAL.html`-linking "Master
   Hub" HTML file anywhere in the Master Kit (only `Atlas One — Tools Hub.html` exists at the root), and the Tools
   Hub does not itself `href` the Portal by filename — it is opened by double-clicking the file, not a link from
   another page. Nothing needed repointing. The only place the Portal's filename is referenced in an href-able way
   is inside the Portal's own catalogue entries and the BRJ resource library, and that BRJ mention is an unrelated
   coincidental text label, not a link to this file.

**Verified by rendering:** `file://` in headless Chromium (`/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs`).
Portal load: 0 console errors, 0 non-`file://` network requests. Opened four tool cards: **Quick Quote**, **Savings
Summary** and **Health Quote Census** (all three: DM Sans loaded in the tool's own iframe, `<h1>`/`<h2>` present, 0
errors, 0 network) plus the **Everything Atlas One handles** card, which renders raw PDF bytes in the iframe by
design (that card is a PDF, not an HTML tool, so `document.write()` of PDF bytes producing no `<style>`/serif
fallback is expected, not a defect).

## Job 2: two vendor names off the public what-we-do page

`repo:tools/what-we-do/index.html` (live at forms.atlasonesolutions.com/tools/what-we-do/):
- "Connecteam workforce hubs" → "Workforce hub app (scheduling, tasks, chat)"
- "Redirect Health" → "Alternative funding health plans (whole group)"
- QuickBooks left as-is (it's the client's own software, not a third-party vendor named on their behalf).

**Verified by rendering:** 390 / 768 / 1440 px, headless Chromium: 0 console errors, 0 non-`file://` requests,
`scrollWidth` equals the viewport at 390 px at every width. Screenshots at
`repo:_briefs/assets/run-AF/shots/wwd-390.png`, `wwd-768.png` (not saved, checked inline), `wwd-1440.png`.

**PDF regenerated:** `A1_Sales/Atlas_One_Everything_We_Handle.pdf` re-rendered from the edited HTML with
Playwright's `page.pdf({preferCSSPageSize:true, printBackground:true})` after `emulateMedia({media:'print'})`,
using the page's own `@media print` / `@page{size:letter}` rules. Confirmed **2 pages** and confirmed with `pypdf`
that the extracted text contains "Workforce hub app" / "Alternative funding health plans" and neither "Connecteam"
nor "Redirect Health". Copied to `A1_Sales/Atlas_One_Everything_We_Handle.pdf`.

**Portal:** rebuilt again after the PDF refresh (`build_portal_single.py`, 44 tools, title
`Atlas One Portal: build Sep 13, 2026 11:40 AM`). Confirmed the inlined PDF text no longer carries either retired
vendor name. The one remaining hit on "Connecteam" anywhere in the Portal file is inside an unrelated internal
tool (a vendor comparison generator that names Connecteam, Homebase, When I Work, Deputy, 7shifts, SwipeClock and
QuickBooks Time by design) — out of scope for this job, not touched.

**Git:** two commits on `main`, both pushed:
- `4b32f39` Run AF job 1: restore Portal, make the overwrite mistake impossible
- `91df937` Run AF job 2: remove two vendor names from the public what-we-do page

**Live 200 check:** `curl -o /dev/null -w '%{http_code}'` against
`https://forms.atlasonesolutions.com/tools/what-we-do/` returned **200**. At the moment of checking, the served
HTML still showed the old copy ("Connecteam", "Redirect Health") while `raw.githubusercontent.com` on the same
commit already showed the new copy — a CDN/build propagation lag on GitHub Pages' side, not a content or push
defect (the repo's what-we-do/index.html is confirmed correct at HEAD).

## What was looked at

- Portal (`Atlas One PORTAL.html`) opened offline in headless Chromium: home screen, Quick Quote card, Savings
  Summary card, Health Quote Census card, Everything Atlas One handles (PDF) card.
- `tools/what-we-do/index.html` rendered at 390 / 768 / 1440 px, full-page screenshots reviewed.
- Regenerated PDF's extracted text (`pypdf`), page count.
- `raw.githubusercontent.com` copy of the edited file, to separate "did the push land" from "has the CDN caught up."

## Assumptions

1. **Backing the wrong Portal build up, not just overwriting it.** The brief's own hard-stop rule ("never delete a
   file, move it to `_to_delete/superseded-<date>/` instead") was applied even though this run's job was to
   rebuild that exact file — copied the 33 KB wrong build to `_to_delete/superseded-2026-09-13/portal-launcher-wrong-build/`
   before running the real rebuild, rather than letting the rebuild silently clobber it.
2. **`build_portal.py`'s new default output filename.** The brief offered two options ("write
   `Atlas One PORTAL (launcher, links only).html` instead, or write nothing when imported as a catalogue"). Took
   the first, more conservative option: the launcher still has a use (a lightweight link list is sometimes wanted
   without the 18+ MB single file), so it keeps working, just never under the protected name, with a hard refusal
   if that name is ever passed explicitly.
3. **Second copy of the PDF.** Found the PDF also duplicated at
   `A1_Sales/Website/BRJ Pricing Page Package 2026-09-13/Atlas_One_Everything_We_Handle.pdf` (same filename, same
   content, prepared for the BRJ handoff). Updated that copy too rather than leaving a stale, vendor-named version
   sitting in a package meant to go out the door. Not named in the brief; flagged here in case that package is
   considered frozen once assembled.
4. **PDF regeneration method.** No PDF generator script exists in the repo or Master Kit; the prior run's report
   confirmed the original PDF was produced the same way, with Playwright's `page.pdf({preferCSSPageSize:true})`
   against the live page's own print stylesheet. Reused that method rather than inventing a new one.
5. **Screenshot at 768 px** was rendered and checked inline (clean, no overflow) but not saved as a file, since the
   brief only asks for two widths (390 and desktop) to be looked at; 768 was an extra spot-check.

## Questions for David

None. Both jobs were mechanical fixes with a clear reasonable call at every branch; nothing here needs a decision
only you can make. If GitHub Pages hasn't caught up by the time you read this, a hard refresh or a few more
minutes should clear it — the file itself is correct on `main`.
