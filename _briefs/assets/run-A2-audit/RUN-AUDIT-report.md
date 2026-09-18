# Run A2 report: corrections from the Cowork audit of Run A1

Terminal: AUDIT. Brief: `_BUILD-LOG/BRIEF-AUDIT.md` (Run A2). Read first: `COWORK-AUDIT-run-A1-2026-09-18.md`.
Backed up the Run A1 report to `_to_delete/superseded-2026-09-18/prior-reports/RUN-AUDIT-report-RunA1.md`
before writing this one, as instructed.

## Job 1: the manual rate rule

Verified Stage 2 of the Audit Workbench (`06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Audit_Workbench.html`)
already applies David's rule correctly, in headless Chromium with a pasted register:
- Blank rate: `payroll_admin` prints "needs a rate" with the provider fee shown, never guessed.
- Typed rate ($25): quotes correctly (`PEO at $25 per employee per check x 5 x 52`).
- Bookkeeping model: always uses the fixed schedule ($7.50/EE/weekly in the test) regardless of
  what is in the rate box.

Applied the same rule where it did not yet exist:
- **Quick Quote** (`09 Quick Quote Tool/Atlas_One_Quick_Quote.html`): `peo_flat` ($25 default),
  `peo_pct` (0.0095), `aso_admin` ($18) and `hcm_only` ($12) now carry `rate: null, needsRate: true`.
  `rateOf()` returns `null` with no override; `price()` returns a `needsRate` line at $0 with a note;
  the price chip, the quote panel, the copy-summary and the saved log all show "Needs a rate"; the
  quote total and a new callout ("N items need an Atlas One rate") keep the total honest instead of
  silently charging $0. Verified: blank shows "Needs a rate" and is excluded from the total; a typed
  rate with 10 employees computes $542/mo, $6,500/yr correctly; zero console errors.
- **Quote Cockpit** (`08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html`): added a
  `NEEDS_RATE_MODELS` list (`peo_check`, `peo_pct`, `aso_check`, `hcm_month`; `bk_month` and
  `self_month` are untouched, one is the fixed price and the other is not named in the rule).
  `calc()` shows "needs a rate" instead of a silent $0 on the payroll tile and the itemized table;
  both PPTX deck builders (`buildDeck`, `buildDeck10`) show "Needs a rate" instead of a fabricated
  dollar figure and now confirm with David before building a deck with a blank required rate.
  Verified in headless Chromium: blank shows "needs a rate", placeholder text updates per model,
  zero console errors.

**Files changed** (all in the Master Kit on OneDrive, not this repo): `Atlas_One_Audit_Workbench.html`
(Stage 2 rate restore on load, see Job 5), `Atlas_One_Quick_Quote.html`, `Atlas_One_Quote_Cockpit.html`.

## Job 2: the report's offer section

Changed `audit.offer.lines` from a copy of the Total Impact dollar lines to `[{key, label, price_text}]`,
`key` a `prices.json` key. Added two new categories to `prices.json` (and the Workbench's embedded
copy of it) with no numeric rate, honoring Job 1's rule:
- `payroll_models`: `peo`, `peo_pct`, `aso`, `hcm` (all say "rate confirmed for your account, no
  default"), `bookkeeping` (the one fixed price, stated).
- `included_services`: `wc_placement`, `benefits_placement`, `bookkeeping_review`,
  `software_consolidation` (all "included with your membership," no fee).

Rewrote the Workbench's Stage 6 to build `offer.lines` from checkboxes over these `prices.json` keys,
defaulted from which Total Impact lines are quoted (payroll model from Stage 2, WC placement from
`wc_premium`, benefits placement from `health_premium`/`section_125`, bookkeeping from `bookkeeping`,
software resale from `software_stack`/`software_resold`) plus the membership tier, which is always
included and locked on. David can still uncheck or add items by hand. Verified in headless Chromium
loading the sample: exactly the five lines the brief named come back checked (Professional
membership, PEO per employee per check, workers comp placement, benefits placement, software stack
consolidation), zero console errors.

Fixed the tool-name leak in `build_audit_report.py`'s three fixes: a `SOURCE_WORDS` map now gives
every Total Impact line a plain-word source ("from your payroll register," "from your workers comp
declarations page," "from the health comparison," "from the retention calculator," "from your card
statements," "from your benefits renewal") in place of the internal tool name ("PEO deck," "stack
calc," etc). Also fixed the offer-lines fallback (used only when a prospect JSON has no `audit.offer.lines`
at all) to pull the tier's own `prices.json` entry rather than repeating the impact rows.

Updated `AUDIT_SCHEMA.md`'s `offer` shape and `SAMPLE_Tell_Me_More_LLC.json`'s `audit.offer.lines` to
the new shape (the five items above). Rebuilt the sample report html and pdf into the DEMO Proposal
Set (`12 DEMO Proposal Set/Atlas One — DEMO Proposal Set/`, overwriting the 2026-09-18 files in
place) and rasterized the full page: two pages, page one keeps the impact lines and the plain-word
fix sources, page two shows the offer table with prices, not dollars, nothing clipped, zero console
errors. Grepped the rendered HTML (outside the base64 font block): zero dashes, zero tool or script
names, zero vendor or PEO brand names.

## Job 3: build_tim.py no longer overwrites the sample

`build_tim.py` now checks whether `SAMPLE_Tell_Me_More_LLC.json` already exists before writing it,
and prints a skip note instead of overwriting from its embedded `SAMPLE` string. Ran it: printed
"skipped: .../SAMPLE_Tell_Me_More_LLC.json (already exists, carries the Audit Workbench's audit
block, never overwritten)"; the file's MD5 was identical before and after; the `audit` block
(including Job 2's `offer.lines`) survived; `total_impact_model.py` still reconciles the sample to
$13,117.

## Job 4: bench polish, no more em dashes

Grepped `Atlas_One_Audit_Workbench.html` for `&mdash;` and the literal em dash, excluding the base64
font blocks: found eight occurrences (the fix cards, the WC class-code table's empty-value
placeholder, and the amount/note lines for `software_stack`, `vendor_audit`, `payroll_admin`,
`subcontractor`, `section_125`, `hr_hours`, `turnover`). Replaced the "amount/yr — note" pattern with
a colon and the lone table placeholder with a middle dot. Re-grepped: zero remain in UI strings.
Verified in headless Chromium with the sample loaded: Stage 5 fix cards render correctly
("#1 · health_premium: $7,600/yr, confidence 0.8, about 30 days"), zero console errors.

## Job 5: verify, screenshots, COMMAND

Re-shot all six Workbench stages at 1200 px and 390 px with the sample loaded (via
`window.loadProspectFile` in headless Chromium, equivalent to the drag-and-drop path), plus the
sample report (both pages) and the audit-prep email, into `_briefs/assets/run-A2-audit/shots/`
(replacing the stale Run A1 set that showed "$0 a month"). Zero console errors and `scrollWidth`
equals the viewport at both widths, on every shot.

While shooting Stage 2, found a small gap and fixed it under this job (not asked for in the brief,
but the "editable at all times" rule implies re-opening a saved file should show the rate that was
typed): the Stage 2 rate input did not restore from a loaded prospect's `audit.payroll.atlas_one_rate`
/`atlas_one_model`, so reopening a saved file with a real rate on file showed a blank "needs a rate"
box even though the quote itself was already correct. Fixed in `renderStage2`; re-shot to confirm
($25 now shows in the box on load).

Wrote `_briefs/assets/run-A2-audit/runA2-parity.txt`: the Workbench (Stage 5), `total_impact_model.py`
and `build_audit_report.py` agree to the dollar on the sample ($13,117); Job 2's five offer lines
confirmed; Job 3's skip behavior confirmed with matching MD5s; Job 4's zero-`&mdash;` grep confirmed.

Rebuilt COMMAND on the Mac. `catalogue_check.py` passed first (199 entries, all paths resolve).
Backed up the prior `Atlas One COMMAND.html` and `Atlas One Sales Kit.html` outputs to
`_to_delete/superseded-2026-09-18/command-outputs/` before rebuilding. `build_command.py` wrote
`Atlas One COMMAND.html` (199 items) and `A1_Sales/Atlas One Sales Kit.html` (57 items), both
stamped "Sep 18, 2026  10:20 AM," matching the Mac's local clock at build time (the Run A1 stamp had
read UTC from a VM build). Confirmed zero internal tool names (Audit Workbench, `build_audit_report.py`)
in the prospect-facing Sales Kit.

Updated `~/.claude/skills/atlas-audit/SKILL.md`: the manual rate rule (with a pointer to the
atlas-pricing skill), the Payroll stage note (`needs_rate`, the bookkeeping fixed price), the Offer
stage note (the new `{key, label, price_text}` shape, checkboxes over `prices.json`, the tier always
included), the report command note (plain-word sources, no tool names), and marked the `build_tim.py`
sample-overwrite landmine fixed rather than open. Re-zipped to `atlas-audit.zip`. While rezipping,
found the existing zip had picked up a stale flat `SKILL.md` at its root from an earlier `zip -r`
run alongside the correctly nested `atlas-audit/SKILL.md`; deleted the old zip and rebuilt clean.

## Assumptions

1. `payroll_models` and `included_services` in `prices.json` are new categories this run added;
   they carry no numeric rate (PEO/ASO/HCM) or a stated fixed price (bookkeeping, all four
   included-service entries), consistent with Job 1's rule against adding payroll rates to
   `prices.json`. The specific wording of these four `included_services` labels and prices is my
   own; David may want different copy.
2. "Workers comp placement" and "health placement through the carrier partners" have no existing
   `prices.json` category (they are not fee lines, they are what membership includes). I added them
   under a new `included_services` key rather than inventing a price for either. If David sells
   these differently (a placement fee, a named carrier), this key should change.
3. The Stage 2 rate-restore-on-load fix (Job 5) only sets the input's displayed value; it does not
   retrigger the payroll calculation, since the loaded prospect's `lines.payroll_admin` is already
   correct from when it was saved. Re-uploading the register would recompute as normal.
4. Left the older, pre-audit-block copy of the sample at
   `08 ROI Quote Master Template/Total_Impact_Model/prospects/SAMPLE_Tell_Me_More_LLC.json`
   (dated 2026-09-08) untouched; it predates the audit feature and is not the file any of these
   four jobs, or the atlas-audit skill, point to.
5. Copied the Run A2 brief into this repo as `_briefs/BRIEF-AUDIT-runA2-2026-09-18.md` rather than
   overwriting `_briefs/BRIEF-AUDIT-2026-09-18.md`, since that filename already held the committed
   Run A1 brief.

## Skipped
Nothing in the brief was skipped.

## Questions for David

Carried forward from Run A1 (the design doc's open questions, `back-office-audit-run-design-2026-09-18.md`
section 6); the two Run A1 questions about the rate rule and the `build_tim.py` landmine are now
answered and fixed respectively, so they are dropped from this list.

1. Should the prep email go out automatically after every 30 minute booking, or only when you tag
   the contact?
2. Pulse: eight questions as drafted, or strike or add any before it goes live in the portal?
3. Keep the headcount tier rule (Essential under 10, Professional 10 to 49, Enterprise 50 to 149,
   Concierge 150 plus), or is Professional the default for everyone under 50?
4. Show the three year view on the client report, or first year only?
5. Form D uploads land on the GHL contact; fine, or should statements only ever be handled live on
   the call and in the browser tool, nothing stored?

New from this run:
6. The `included_services` wording (workers comp placement, benefits placement, bookkeeping
   review, software stack consolidation) in `prices.json` is my draft copy for what the offer table
   shows. Keep it, or do you have preferred wording for any of the four?
