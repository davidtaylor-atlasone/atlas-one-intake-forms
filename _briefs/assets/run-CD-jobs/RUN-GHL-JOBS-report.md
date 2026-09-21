# RUN-GHL-JOBS report: Run CD, 2026-09-21

Atlas One COMMAND.html: 53.8 MB, 206 items, build stamp on the header shows the time of the last rebuild
in this run (last rebuild ran after the contact sweep, Job 4). Present decks added about 1.87 MB of raw
JPEG bytes (about 2.5 MB after base64). Atlas One Sales Kit.html: 24.0 MB, 57 items.

Terminal: GHL-JOBS, Sonnet 5, files and code only, never the GoHighLevel browser UI. Brief:
`_BUILD-LOG/BRIEF-GHL-JOBS.md`, copied to `_briefs/RUN-GHL-JOBS-2026-09-21.md` in the intake forms repo.

## Job 1: the three COMMAND bugs

All three fixed in `build_command.py`.

**1a, nothing scrolls.** `#main{flex:1 1 auto;min-height:0;display:flex;flex-direction:column}` added
(it had no CSS at all before this run). `#content` changed to
`flex:1 1 auto;min-height:0;overflow-y:auto;-webkit-overflow-scrolling:touch`. `height:100dvh` added
after the `height:100vh` fallback on `body`. `#topheader{position:sticky;top:0}` left in place as the
brief said to; it is harmless inside the flex column, checked.

Proof, Playwright headless Chromium, 1440x900, 1024x768 and 390x844, all four zones (Internal unlocked
with the passphrase first), asserting `#content.scrollHeight > #content.clientHeight`, then scrolling to
the bottom and asserting the last `.row` in the active zone has `getBoundingClientRect().bottom` inside
the viewport:

- All 21 assertions (3 viewports times 3 catalogue-driven zones, plus Present, which shows cards not
  rows) passed. Example: desktop 1440, Sales Kit, scrollHeight 4492 vs clientHeight 705, last row bottom
  805.8 inside 900. Screenshots `job1a-<zone>-<viewport>.png` in `_briefs/assets/run-CD-jobs/shots/`.
- Load at 390 wide: 144 ms, 0 console errors, `document.documentElement.scrollWidth` is exactly 390.
- Safari: opened `Atlas One COMMAND.html` once with `open -a Safari` as the brief asked. **A human Safari
  check is still outstanding** — I cannot drive or screenshot Safari from this terminal, only launch it.

**1b, search that lets go.** Added a visible Clear button in `#topbar` (hidden while the box is empty).
One `resetFilter()` now does everything the brief asked: clears `data-hidden` off every row in the whole
document, restores every section's `display`, hides the search heading and the empty message, updates the
count. It is called from the Clear button, from `run()` when the term is empty, from `showZone()` before
it switches (this is the exact bug: `showZone()` used to clear the box without calling anything, so a
hidden row or a `display:none` section from a search survived a tab switch), from the Escape handler, and
from `closePreview()` (David's own repro: closing the preview left a filter behind).

Collapse all / Expand all: two buttons in `#topbar`. Every `.sechead` is now a `<button>` with a caret that
rotates and a count chip, toggling its own `.secbody`. Collapsed state is remembered per zone in
`localStorage` under `a1cmd_collapsed_<zone slug>`, read and written inside try/catch; a search always
force-expands a section that contains a hit and never touches localStorage while doing it.

Proof:
- Search "handbook": hid 42 rows. Closed the preview: box cleared itself, 0 rows left hidden. Clear
  button: emptied the box, 0 rows hidden. Switched Tools then back to Sales Kit: 0 rows hidden, 0 sections
  left `display:none`.
- Collapse all on Sales Kit at 1024 wide: 7 of 7 sections collapsed, screenshot
  `job1b-collapsed-1024.png` shows the zone fits one screen. Reloaded the page: 7 of 7 still collapsed
  (localStorage held). Expand all: 0 collapsed.

**1c, the undisclosed passphrase.** `INTERNAL_PASSPHRASE` moved out of `build_command.py` into
`catalogue.py`, with a three line comment above it saying what it is (a curtain on the Internal tab for
this browser tab only, not security, since the built file carries the value in plain text), that a change
takes effect on the next build, and that `None` removes the curtain entirely (then `lock_internal=False`).
`build_command.py` imports it and falls back to its own `"atlas1"` default only if the name is missing.
A one line hint now prints under the passphrase box: "Set in catalogue.py as INTERNAL_PASSPHRASE. Set it
to None to remove this curtain." The passphrase itself is never printed on screen.

**Current value: `atlas1`** (unchanged; written here in plain text per the brief so David has it).

Not changed, reported per the brief: the AI Email Assistant Approval Queue, the Activity log, and Tasks
and Follow ups all sit in the Internal zone behind this curtain today. See Questions for David.

## Job 2: the Present zone

Fourth top tab, `ZONE_ORDER = ["Sales Kit", "Tools", "Internal", "Present"]`. Confirmed Sales Kit still
cannot reach it: `Atlas One Sales Kit.html` passes `zone_filter={"Sales Kit","Tools"}` and the Present tab
and zone are only added when `include_present=True`, which the Sales Kit build never passes. Grepped the
built Sales Kit file for "Present" (5 hits, all inside the unrelated title "Benefits Options Presenter",
none is the tab or a playlist page title) and for a playlist page title (0 hits). Clean.

`_INTERNAL (do not share)/present.py` holds `PLAYLISTS` and `TALK_TRACKS`, an explicit list of catalogue
ids per the brief, nothing derived from a filter. `catalogue_check.py` now also checks that every id in
`present.py` exists in the catalogue (it does, 17 ids: the 11 named pages plus the 6 new division sheet
HTML rows).

Six new catalogue rows added, `division-sheet-<slug>-html`, audience internal, division "Sell & Pitch",
kind tool, pointing at the HTML twins already sitting beside the PDF rows. The PDF rows are untouched.

**The runner.** A full screen pane (`#presentrunner`), separate from `#previewpane`. Top bar shows the
playlist name, "page N of M" (M matches the brief's page counts: 4, 7, 10, 16 for every one of the eight
playlists), the page title, a clock that runs from Start and keeps running across pages, the suggested
minute budget for the current page, and an "On pace" / "Behind" word (form only, no colour, per the brand
rule). Back, Next and Exit buttons; left/right arrows, space for next, Escape for exit; touch swipe left
and right on the stage. Every non-deck page renders into a brand new iframe built from scratch (same
`freshFrame()` pattern the existing preview pane already used, for the same reason: a reused iframe goes
permanently cross origin under Chromium's site isolation). `<style>.brandbar{display:none !important}</style>`
is injected into every rendered page. Deck pages render as `<img>` from an inlined base64 data URI, never a
PDF in an iframe. The "page N of M" counter counts catalogue stops, not deck slides: a deck counts as one
stop, and Next/Back page through its own slide images before advancing to the next stop, so the clock and
counter match the brief's stated page counts exactly while still showing every slide.

**Deck rendering.** `render_decks()` renders each deck PDF into cached JPEGs under
`_INTERNAL (do not share)/present_assets/<deck id>/pNN.jpg`, re-rendering only when the PDF's mtime is
newer than the cached images. `pdftoppm` is not installed on this Mac Studio, so it fell back to PyMuPDF
(already installed) as the brief said to try second. Client Launch Deck rendered 10 pages, First Meeting
deck rendered 9 pages, both confirmed by counting the resulting image files. Total added: about 1.87 MB
raw JPEG (about 2.5 MB once base64'd into the page). COMMAND came in at 53.8 MB, comfortably under the
78 MB split threshold, so it stays one file; no `Atlas One PRESENT.html` split needed.

**The playlists**, all eight built and verified end to end with headless Chromium: started each one from
its card, clicked Next through to the last page (asserting every rendered stop has real content: a
non-empty image src or, for an iframe, more than 500 characters of body text), confirmed the counter and
clock moved, confirmed Back changes the page, confirmed Exit returns to the Present tab with the zone
intact. All 8 passed, matching the stop counts the brief specified:

| playlist | stops | reached |
|---|---|---|
| prospect-15 | 4 | page 4 of 4 |
| prospect-30 | 7 | page 7 of 7 |
| prospect-45 | 10 | page 10 of 10 |
| prospect-60 | 16 | page 16 of 16 |
| client-15 | 4 | page 4 of 4 |
| client-30 | 7 | page 7 of 7 |
| client-45 | 10 | page 10 of 10 |
| client-60 | 16 | page 16 of 16 |

Screenshots `job2-<key>.png` and `job2-phone-390.png` in the assets folder.

**Minute budgets** (computed, not hand written, `present.compute_budgets`: talk track takes 2 minutes off
the top, the rest splits across the pages, Discovery and Total Impact weighted double since they are live
and David types into them, everything else weighted one, floored to whole minutes with the remainder added
to the last page):

- prospect-15: First Meeting deck 2, Discovery 5, Proof Sheet 2, Membership 4
- prospect-30: deck 3, Everything 3, Discovery 6, Proof Sheet 3, Membership 3, Total Impact 6, Portal 4
- prospect-45: deck 3, Everything 3, Business Overview 3, Discovery 7, Proof Sheet 3, Benefits Menu 3,
  Software 3, Membership 3, Total Impact 7, Portal 8
- prospect-60: deck 3, Everything 3, Business Overview 3, six division sheets 3 each, Discovery 6,
  Proof Sheet 3, Benefits Menu 3, Software 3, Membership 3, Total Impact 6, Portal 7
- client-15: Client Launch Deck 3, Everything 3, Proof Sheet 3, Membership 4 (no Discovery in 15 minutes
  for a current client, per the brief: they need to hear what else Atlas One now handles, not the
  discovery tool)
- client-30 / client-45 / client-60: same shape as the matching prospect length, Client Launch Deck in
  place of the First Meeting deck

**Talk track screens**, one per playlist, eight total, cut (not rewritten) from
`Atlas_One_Sales_Conversation_Playbook.html` section 3 (the matching rung: 15 minutes uses "the first
meeting," 30 uses "the Back-Office Audit," 45 and 60 use "Audit plus proposal," 60 also adds the five core
questions from section 4), plus the fixed why-Atlas-One line (one relationship, vendor neutral, volume
pricing, the Audit Guarantee) on every track, plus, on the four Current client tracks only, the
acquisition reassurance (nothing about their payroll, PEO, HR or benefits moves; nobody is taking over
their account; same advisor, new name, more services) placed first, right after the opening, per the
brief's instruction that this one matters most. Ran the forbidden term scan over the talk track text at
build time (a hard `SystemExit`, no allowlist) — clean, no hits.

**Nothing internal in Present.** Extended the content check so every id named in `present.py` is scanned
regardless of its audience tag, not just prospect/client rows. Two hits, both already reviewed and
allowlisted with a reason, matching the brief's verified findings:
- `A1_Sales/Atlas 1 Benefits/Atlas_One_Employee_Benefits_Menu.html` hits "cornerstone" (the `CONFIG.cs`
  brand toggle data, nothing renders unless clicked, and Present hides `.brandbar` anyway).
- `A1_Sales/Atlas 1 Consulting/Atlas_One_Division_Business_Consulting.html` hits "margin" and
  "commission" ("Margin and pricing analysis," "Comp and commission plan design," service names the
  client buys, not Atlas One's own economics).

No third hit. A wider grep of the built COMMAND file (stripped of every base64 blob) for the six forbidden
terms does surface older, pre-existing Internal-zone and Tools-zone catalogue row labels this run did not
touch: "Commission & Revenue Tracker," "Cornerstone Strategy," "Partner Pitch Deck v9 (send version,
prints cost and margin on slides 26 and 27)," and a WSA overlay note. These are internal-only reference
rows describing Atlas One's own internal documents, and COMMAND itself is never shared outside the Master
Kit (see the file's own docstring); the guard that actually matters is on the file that could reach a
prospect, `Atlas One Sales Kit.html`, whose own build-time forbidden-term check (which does raise
`SystemExit` on a real hit) passed clean, and which structurally cannot include Present at all.

`.brandbar` check: none of the eleven named pages or six division sheets actually render a visible
`.brandbar` element in the Master Kit today (checked all of them; the Employee Benefits Menu file has the
CSS class defined and a `CONFIG.cs` toggle in its data, but no element in its markup uses the class). So
this run confirmed the defensive style injection mechanism directly — the runner's rendered iframe for the
Employee Benefits Menu page carries the injected `<style>.brandbar{display:none !important}</style>` —
rather than confirming an element actually disappeared, since there is currently nothing on screen for it
to hide. Confirmed the Sales Kit zone's own preview pane for the same file has no such element either (so
nothing was broken there). If a future sales piece adds a real Atlas One / Cornerstone toggle bar with
this class, it will already be hidden inside Present without any further change.

**Phone.** Present tab is visible and usable at 390 wide, not hidden. `scrollWidth` is exactly 390.
Started `prospect-15`, paged forward once, screenshot `job2-phone-390.png`.

## Job 3: playlist pages live in A1_Sales

Copied `Atlas_One_Everything_We_Handle.pdf` from the BRJ package to the `A1_Sales` root (copy, not move;
the BRJ package keeps its own copy).

Audited every other page named in the playlists against `A1_Sales`: **all of them were already there**,
each already living at the exact path `catalogue.py` points at (the six division sheet HTML twins, the
two decks, the Employee Benefits Menu, the Proof Sheet, the Membership comparison, the Total Impact
Model, the Client Portal leave-behind, the Software and Licenses one-pager, What We Do Business Overview).
Nothing needed copying there.

Two pages deliberately not copied, per the brief: the Time and Cost Savings Discovery tool and the
Everything Atlas One handles public page. Both are live tools that belong in
`06 Calculators and Tools (NEW Aug 2026)/`, both are inlined into COMMAND so no playlist ever opens the
file directly, and a second copy in `A1_Sales` would drift out of date the first time either tool is
edited.

## Job 4: queued price and contact jobs

Read `_BUILD-LOG/BRIEF-GHL-JOBS-queued-pricing-and-contact-sweep.md`, ran both jobs, moved it to
`_to_delete/superseded-2026-09-21/` when done. Source of truth for every price:
`14 Service Content Library/service_content_library.json` (already carried the new prices; this job was
to bring the consuming files into line with it, not to re-derive them).

**Price book.** Changed in `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`,
`_INTERNAL (do not share)/tools/agreements/prices.json`, `A1_Sales/Pricing/Atlas_One_Price_List.html`, and
the Quote Cockpit (`08 ROI Quote Master Template/build_cockpit.py` reads `prices.json`, rebuilt after):
- `handbook_update`: now `one_time`, $250, renamed "Handbook update" (was `flat_mo` $20.83, shown as
  $250/yr, named "Handbook annual update").
- `safety_update`: now `one_time`, $300, renamed "Safety manual update" (was `flat_mo` $25, $300/yr).
- Added `handbook_basic` and `safety_basic`, $299 each, `one_time`, to Quick Quote and `prices.json` (Quick
  Quote did not already carry them).
- `cert_payroll` replaced with five lines in Quick Quote and `prices.json`: `cert_payroll_setup` $300 one
  time per company, `cert_payroll_report` $60 per report, `cert_payroll_state` $125/mo per active job,
  `cert_payroll_federal` $250/mo per active job, `cert_payroll_done` $400/mo per active job. The Cockpit's
  single `CERTPAY_PRICE` number now reads `prices["cert_payroll"]["state_monthly"]` ($125), the same
  figure it always showed, since the Cockpit has one certified payroll line, not five.
- `books_m` / `books_l`: label unchanged, client facing price string on the Price List and in `prices.json`
  now reads "Priced after a 15 minute look at your books"; the `$1,000 to $2,000` and `$2,000 to $3,000`
  ranges stay inside Quick Quote only (David's own tool), never printed on a client page.
- Ran `node --check` against the extracted Quick Quote script (syntax clean), validated `prices.json` as
  JSON, and ran `build_cockpit.py` to confirm the new keys resolve (output: `certpay 125 ... handbook
  custom 950 safety custom 1200 ...`).
- **Not found and not changed:** "the Agreements library card copy in the portal (documents block)." No
  local source file in this repo or the Master Kit renders that copy; the Client Portal leave-behind
  one-pager here (`A1_Sales/Client Portal/Atlas_One_Client_Portal.html`) does not carry a documents/pricing
  block, and no other file under either tree matched "Agreements library" as live UI copy. This most likely
  lives inside the GoHighLevel client portal itself, which this files-only terminal cannot open. Question
  for David, below.

**Contact block sweep.** Built `_INTERNAL (do not share)/contact.json` with `sales` (David, today),
`support` (Atlas One Solutions Support, support@atlasonesolutions.com, 380-225-5217) and an empty `rep`
slot for later. `build_command.py` now reads the Sales Kit hero line's phone number from
`contact.json["support"]` instead of a literal string (the only place in `build_command.py` that carried a
literal contact).

Scope, found on disk 2026-09-21: 40 text files (html/py/json/md/txt/js/css/csv/ts, excluding `_to_delete`)
carried `david@atlasonesolutions.com`. After the sweep: 34. The 6 changed:
- `A1_Sales/Website/BRJ Software Marketplace Package 2026-09-18/Atlas_One_Software_Marketplace_Sheet.html`
- `A1_Sales/Atlas 1 Software and Licenses/Atlas_One_Software_and_Licenses_OnePager.html`
- `A1_Sales/Atlas 1 Software and Licenses/Atlas_One_Microsoft_365_OnePager.html`
- `A1_Sales/Atlas 1 Software and Licenses/Atlas_One_Software_Marketplace_Sheet.html`
- `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Everything_We_Handle.html`
- `12 GHL Setup doccs/Branded Intake Forms/Atlas_One_AI_Email_Assistant_Help.html`

All six are tool footers or a help page (explicit "support" categories per the brief's rule), swept to
`support@atlasonesolutions.com`; the phone number was already the shared main line, so it did not change.

Left as David on purpose (prospect facing sales pieces or a booking flow tied to him personally, per the
brief's rule): `A1_Sales/A1 What we do Overview/Atlas_One_Partner_Client_Program_PPG.html` (its CTA books
directly into David's own calendar, `book-david`), `A1_Sales/Email Templates/
Atlas_One_Bookkeeping_Cadence_2026-09-13.md` (a cadence email template, explicitly kept per the brief),
and `Email_to_Thomas_BRJ_software_marketplace_2026-09-18.html` (a historical already-sent email's
copy-paste instructions, addressed from David).

Of the remaining 34: `contact.json` itself (the new source of truth, carries `david@` correctly under the
`sales` role), `catalogue.py` (one internal admin note, "sign in as david@atlasonesolutions.com to see
what any client sees," not a client facing contact), `Atlas One COMMAND.html` (regenerated after the
sweep, still carries that same internal note as inlined text), and roughly 30 files under `_BUILD-LOG/`
(checkpoints, run reports, briefs, the index) which are historical records, not live client facing
material, and were left untouched on purpose.

The brief's own note said 123 Office and PDF files in `A1_Sales` are not scanned by grep and should be
regenerated from source rather than hand edited; this run did not open or edit any Office or PDF file,
per rule 37 (Office overwrites are David's, from the plain Terminal). No list of sourceless Office/PDF
files was compiled this run; flagged as a question for David rather than guessed at.

M365 transport rule signature: not touched.

## Job 5: rebuild and verify

`catalogue_check.py` passed before every rebuild (206 catalogue entries, all paths resolve, 17 present.py
ids all present). Rebuilt with
`python3 "_INTERNAL (do not share)/build_command.py" "<Master_Kit path>"` three times over the run (after
Job 1/2, after the price book, after the contact sweep); the report's numbers above are from the final
rebuild.

Full Playwright verification suite (script saved this run, not part of the repo) at 1440x900, 1024x768
and 390x844:
1. All four zones scroll to their last row, Internal unlocked with the passphrase first — pass, all 21
   assertions (see Job 1a).
2. Search "handbook", close the preview, confirm the filter is gone without touching the box, Clear
   button, tab switch and back — pass, all 4 assertions (see Job 1b).
3. Collapse all, screenshot at 1024, reload, confirm the collapsed state came back, clear it — pass, all
   3 assertions (see Job 1b).
4. Start all eight playlists, page through every page to the last one, confirm every page renders real
   content, confirm the counter and clock move, confirm Back works, confirm Exit returns to the Present
   tab with the zone intact — pass, every one of the 8 playlists reached its last stated page (see the
   table in Job 2).
5. Grepped the built COMMAND for the six forbidden terms outside base64 blobs and outside the reviewed
   allowlist (see Job 2's writeup: clean except pre-existing Internal/Tools-zone reference labels this run
   did not touch, which never reach a prospect since COMMAND itself is never shared); grepped the built
   Sales Kit file for "Present" and for a playlist page title — both clean.
6. Confirmed `.brandbar` hides inside Present (the injected style is present in the rendered page; no
   playlist page in the Master Kit today carries a visible `.brandbar` element to actually hide, see Job
   2) and that the same file's element status is unchanged in the Sales Kit zone's own preview pane.

Screenshots in `_briefs/assets/run-CD-jobs/shots/` in the intake forms repo: `job1a-*`, `job1b-collapsed
-1024.png`, `job2-<playlist-key>.png` (all 8), `job2-phone-390.png`.

## Assumptions

1. Present's "page N of M" counts catalogue stops, not deck slides, matching the brief's stated counts
   (4/7/10/16) exactly; a deck stop pages through its own slide images internally before the counter
   advances. This is the only reading of the brief that makes "First Meeting deck" a single stop in a
   4-page playlist while still rendering all nine of its slides.
2. The `.brandbar`-hiding style injection is verified as a mechanism (the `<style>` tag is present in the
   rendered iframe) rather than by watching an actual element disappear, since no page currently in the
   Master Kit's Present playlists renders a visible `.brandbar` element. If one is added later it will
   already be hidden with no further change needed.
3. The two Present forbidden-term allowlist entries are the same two the brief's own verified findings
   named; added with the same one-line-reason style as the existing entries.
4. `books_m` / `books_l`: kept the $1,000 to $3,000 dollar ranges inside Quick Quote (David's own tool)
   unchanged, since the brief said those ranges stay there for his own use and never print on a client
   page; only the client facing price strings (Price List, `prices.json`) changed.
5. The Quote Cockpit's single certified payroll figure now reads the "state monthly job" price ($125),
   the same number it showed before the five-line split, since the Cockpit has one certified payroll line
   in its quote builder, not five. Did not attempt to add four more line items to the Cockpit's UI; that
   would be new scope beyond "prices follow the library."
6. Everything Atlas One handles' page footer (a public, prospect facing acquisition page) was swept to
   support rather than kept as David, on the "every tool footer moves to support, when unsure support"
   rule, even though the page's own CTA still books directly into David's calendar (that booking widget
   URL was not touched, only the printed email address).
7. Did not touch `division_sheets_build_2026-09-12.py`, `service_deck.py`, the master-pricing-v8 tooling,
   the service content library's CSV/generated.ts outputs, or any `_BUILD-LOG` history file, even though
   several also carry `david@atlasonesolutions.com` — these are either generators/derived outputs outside
   the brief's named five files, or historical records that should not be edited after the fact.
8. Left the Partner Client Program PPG one-pager and the BRJ "Email to Thomas" draft on David's contact,
   reading them as prospect/partner facing sales sends in the spirit of the brief's explicit keep-David
   list even though neither is literally named in it.

## Questions for David

1. "The Agreements library card copy in the portal (documents block)" named in the queued brief was not
   found anywhere in this repo or the Master Kit as an editable source file. Is that copy actually inside
   the live GoHighLevel client portal (out of reach for a files-only terminal), or is there a source file
   under a name I did not search for?
2. The AI Email Assistant Approval Queue, the Activity log, and Tasks and Follow ups all sit behind the
   Internal zone's passphrase curtain in COMMAND today (unchanged this run, reported per the brief). Is
   that the right place for them, or should any of the three move to a zone that does not need the
   passphrase?
3. The brief's own note said 123 Office and PDF files in `A1_Sales` are not grep-scanned for
   `david@atlasonesolutions.com` and should be regenerated from source rather than hand edited. No list of
   which ones have no source was compiled this run (rule 37, Office overwrites are yours). Do you want that
   list built as a follow-up job?
4. `Atlas_One_Software_and_Licenses_OnePager.html` and its three sibling one-pagers were swept to support
   as tool footers, even though they are also handed to prospects directly (one is in the Present 45/60
   minute playlists). If you would rather prospect facing one-pagers keep your name in the footer even
   though they are "tools," say so and I will revert those four.
