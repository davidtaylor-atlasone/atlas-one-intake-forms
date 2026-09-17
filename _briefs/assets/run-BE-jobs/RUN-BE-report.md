# Run BE report, GHL-JOBS terminal (files and code only)

Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md`, copied to the repo at `_briefs/BRIEF-GHL-JOBS-2026-09-16-RunBE.md`.
Prior report (Run BD) already backed up by Cowork to `_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunBD.md`.

## Built

### Job 1: the Cockpit reads prices.json, single price source
- `08 ROI Quote Master Template/build_cockpit.py` (new). Reads the _INTERNAL copy of prices.json and writes
  two marker fenced blocks into `Atlas_One_Quote_Cockpit.html`:
  - `ATLAS_ONE_PRICES_BEGIN/END`: the QBO, Microsoft 365 and AI Email price arrays, the membership MEMTIER
    array, and named constants (CERTPAY_PRICE, AIEMAIL_ESSENTIAL_PRICE, AIEMAIL_SETUP, AITASK_PRICE,
    HANDBOOK_BASIC_SETUP, HANDBOOK_CUSTOM_SETUP, SAFETY_BASIC_SETUP, SAFETY_CUSTOM_SETUP, and the four
    Microsoft 365 per user prices).
  - `ATLAS_ONE_TIERSET_BEGIN/END`: the four membership tiers, each with its fit line now sourced from
    `prices.json membership.*.fit`.
  As a one time setup edit (never needed again, the builder owns these blocks from here on), the Cockpit's
  own service catalog rows for certified payroll, the basic and custom handbook, the basic and custom safety
  manual, the AI Email Assistant, the AI Task Agent and the four Microsoft 365 rows now reference these
  generated constants instead of hand typed numbers.
- `_INTERNAL (do not share)/tools/agreements/prices.json` and the repo mirror `tools/agreements/prices.json`
  (kept byte identical, diffed after every edit):
  - Added a `fit` field to all four `membership` entries (Job 1.4). Essential and Professional carry the
    exact wording from Run BC; Enterprise and Concierge carry the Cockpit's own existing wording, since the
    brief only specified new text for the first two.
  - Added `ai_services.concierge` ("AI Email Assistant, Concierge", $649 a month), `documents.handbook_basic`
    ($299 one time) and `documents.safety_basic` ($299 one time): three services the Cockpit already listed
    that prices.json did not have.
- Backups: `Atlas_One_Quote_Cockpit.html`, both prices.json copies and the BRJ index, all copied to
  `_to_delete/superseded-2026-09-16/before-runBE/` before any edit.

### Job 2: kit index clean up
- `Atlas One — Complete Kit for BRJ/⭐ START HERE — BRJ Index.html`: reworded the Folder 10 paragraph. It now
  says the five builders live in `06 Calculators and Tools` and open from the links below, with no dashes in
  the new sentence.
- Applied the new standing rule from this run on: grepped the Master Kit, A1_Sales and the repo for
  "10. Premium Builders" and for each of the five builder filenames.

### Job 3: rebuild and verify
- `catalogue_check.py`: 192 entries, all resolve (unchanged by this run).
- Rebuilt `Atlas One COMMAND.html`: 192 items, 48,649,198 bytes, stamp "Atlas One COMMAND: build Sep 16, 2026
  10:06 PM", backed up the pre run copy to `_to_delete/superseded-2026-09-16/command-before-runBE/` first.

## Verification

### Job 1: before and after totals
Ran the same sample entity (Professional membership, certified payroll, AI Email Assistant Essentials, a
custom Employee Handbook, a custom Safety Manual, all turned on) through the pre edit backup and the rebuilt
Cockpit in headless Chromium (Playwright), reading the page's own totals off the DOM.

| Line | Before | After | Change |
|---|---|---|---|
| Certified Payroll | $75/mo | $125/mo | prices.json wins, +$50/mo |
| AI Email Assistant (Essentials) | $199/mo | $249/mo | prices.json wins, +$50/mo |
| Employee Handbook, custom | $750 setup | $950 setup | prices.json wins, +$200 |
| Safety Manual, custom | $750 setup | $1,200 setup | prices.json wins, +$450 |
| Atlas One Membership, Professional | $399/mo, $495 setup | $399/mo, $495 setup | no change, already matched |
| Total monthly, all in | $673 | $773 | +$100/mo, matches the two monthly corrections |
| One time setup (separate) | $2,745 | $3,395 | +$650, matches the two setup corrections |

Every other Cockpit price checked against prices.json (QuickBooks Online, all four Microsoft 365 tiers, the
four membership dollar amounts) already matched, no change made there.

Reviewed and left alone, different structure rather than a same field conflict:
- Bookkeeping package price (Cockpit gives point default prices of $600, $1,500, $2,500 for the Small,
  Medium and Large tiers; prices.json gives quoted ranges for the same tiers, for example "$300 to $1,000 a
  month"). Nothing in prices.json to swap the Cockpit's editable default anchor for.
- AI Task Agent: the Cockpit only ever shows the bundled with Email Assistant figure ($99/mo, setup waived),
  which already matches `ai_services.task_agent_bundled`. `ai_services.task_agent_standalone` ($199/mo) has
  no Cockpit row and none was added, since the brief's rule only requires adding a service the Cockpit has
  and prices.json lacks, not the reverse.

Console errors: 0. Non file network requests: 0. `scrollWidth` equals the viewport at 1440 and 390 px, on
both the before and after file. The four base64 `@font-face` blocks are still present. Exported the one
pager PPTX end to end (click through Playwright): it downloads, zero console errors, saved as
`_briefs/assets/run-BE-jobs/Atlas_One_Proposal_test.pptx`.

One cosmetic side effect worth flagging: `json.dumps` writes the pre existing em dash inside "AI Email —
Essentials" as a `\uXXXX` escape rather than the literal character. The browser renders it identically (same
em dash on screen, confirmed in the screenshots), it is a source encoding change only, not a copy change.
These dashes predate this run (Run BC already flagged 15 pre existing em/en dash characters in the Cockpit as
out of scope) and no new ones were added.

Screenshots: `_briefs/assets/run-BE-jobs/shots/cockpit_before_1440.png`, `cockpit_after_1440.png`,
`cockpit_before_390.png`, `cockpit_after_390.png`.

### Job 2: links and grep
All five builder links on the BRJ index resolve (confirmed on disk and by reading the rendered `<a href>`
values in headless Chromium). Zero console errors, zero non file requests, `scrollWidth` equals viewport at
1440 and 390 px. Screenshots: `_briefs/assets/run-BE-jobs/shots/brj_index_1440.png`, `brj_index_390.png`.

The standing rule grep (Master Kit, A1_Sales, the repo) for "10. Premium Builders" and each of the five
builder filenames returned hits only in: the BRJ index itself (already fixed, both live and the frozen
`_gold_backup_2026-08-24` snapshot), historical run reports and live logs (`RUN-*-report.md`,
`TERMINAL-*-live.md`, past `_briefs/BRIEF-*` copies), which are records of what already happened and are
never repointed, and `catalogue.py`, `build_command.py` and `build_portal.py`, all three of which already
point at `06 Calculators and Tools (NEW Aug 2026)`, never at the retired `10. Premium Builders` path. Nothing
needed repointing.

### Job 3
`catalogue_check.py`: 192 entries, all resolve. COMMAND rebuilt and confirmed in headless Chromium: zero
console errors, `scrollWidth` equals viewport at 1440 px. Screenshot:
`_briefs/assets/run-BE-jobs/shots/command_1440.png`.

## Assumptions
1. The brief's premise that build_tim.py and the repo Quick Quote already "embed prices.json at build time"
   into HTML between markers did not match what is on disk: build_tim.py never touches prices.json (it is a
   static Python line list), `total_impact_model.py` reads prices.json at run time in Python rather than
   baking it into HTML, and there is no Quick Quote tool anywhere in the repo (`atlas-one-intake-forms`),
   only in the Master Kit's `09 Quick Quote Tool/`, which carries its own hand typed prices with no build
   script at all. Took the working example that does exist, `total_impact_model.py`'s
   `os.path.normpath` relative resolution of PRICES_PATH, as the pattern to follow for `build_cockpit.py`'s
   own path resolution, and designed the marker block mechanism fresh since nothing to copy for that part
   existed yet.
2. Kept the membership tiers' setup fee wording ("setup waived", "setup $495, often waived", and so on) and
   the "what is included" marketing copy as authored constants inside build_cockpit.py (TIER_META), the same
   way build_tim.py keeps its own LINES list as authored Python data rather than parsed from a JSON price
   string. The build does cross check the numeric monthly and setup figures in TIER_META against prices.json
   and would need updating if they ever disagree; only the prose phrasing itself is not machine generated.
   Reasoning: prices.json's own price strings are written as sentences ("$495 a month, $495 setup, often
   waived") which read fine as prose but do not have a clean, stable substring to lift into a shorter UI
   label without fragile parsing.
3. The MEMTIER dropdown labels (used in the "mem" catalog row's option list) now show the fuller setup
   wording for Professional and Enterprise ("setup $495, often waived" instead of the previous shorter
   "setup $495") since they are generated from the same TIER_META note as the export deck's TIERSET. More
   informative, not incorrect, flagging since it is a small visible text change beyond the brief's four
   numeric corrections.
4. Treated "the repo Quick Quote" mentioned in Job 1.5 as referring to the Master Kit's
   `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`, the only Quick Quote tool that exists; confirmed it has
   no build script and still carries hand typed prices, and estimated the future build_cockpit.py style
   treatment at 1 to 2 hours (its prices sit inline in one larger settings object rather than behind the
   Cockpit's own catalog() indirection, so the marker block would need to wrap more of the file).
5. AI Email Assistant Concierge ($649/mo): added to prices.json with no setup fee, matching how the Cockpit
   itself lists it (no separate setup figure for that tier).

## Skipped
- Documents that the brief's Job 2 did not ask about: the BRJ index's own section heading still reads
  "Premium Builders — build behind the paywall" (an em dash, and text that now contradicts the paragraph
  just above it saying "no paywall needed right now"). Left it alone since the brief named only the Folder 10
  paragraph; flagging it here since it sits one line away from what was just fixed.
- Bookkeeping package default prices and the AI Task Agent standalone tier, reviewed above under Verification,
  not changed since neither is a same field numeric conflict.
- `09 Quick Quote Tool/Atlas_One_Quick_Quote.html` itself: not touched this run, per Job 1.5's instruction to
  only note it and estimate, not do it now.

## Questions for David
1. Job 1.4 gave exact wording for the Essential and Professional membership fit lines and I used the
   Cockpit's own existing wording for Enterprise and Concierge (unchanged by this run). Confirm that is right,
   or send the wording you want for those two if there is a preferred version.
2. The BRJ index's Premium Builders section still says "build behind the paywall" in its own heading, right
   next to a paragraph that now says no paywall is needed right now. Want that heading reworded in the next
   run, and should the dash come out of it at the same time?
3. Job 1.5 asked for an estimate rather than the work itself: is `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`
   moving onto prices.json next, and if so should its own build script also feed the repo's mirrored
   prices.json the same way, or does Quick Quote stay a Master Kit only tool?
