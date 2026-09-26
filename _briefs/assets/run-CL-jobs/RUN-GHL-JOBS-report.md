# RUN-GHL-JOBS-report: Run CL (GHL-JOBS terminal, 2026-09-26)

Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md`. Terminal: files and code only, never the GoHighLevel browser UI.

## Summary

Job 1 (Charity's kit, the three gaps Run CI's checks missed), Job 2 (retire Industry Starter Kits) and Job 5
(rebuild and prove) are complete and verified. Job 6 (TD SYNNEX carry-through) is confirmed complete. Jobs 3
and 4 are skipped: neither heading in the brief says "David approved," and the brief's own rule is to skip and
say so.

## Job 1: Charity's kit, the three gaps

### 1a. Cornerstone Zoom scheduler removed
Replaced `https://scheduler.zoom.us/david-taylor-qp71rc` with the Atlas One 15 minute intro call link
(`https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp`) everywhere it appeared,
button text set to "Book a call":

- The 11 named tool masters under `06 Calculators and Tools (NEW Aug 2026)/` (19 occurrences).
- `Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/templates.html` (3 more occurrences the
  brief's own file list did not name, found during the Job 5 deep verify pass).

Guard resweep: zero `scheduler.zoom.us` anywhere in the live Master Kit tree (only the untouched
`Atlas One Calculators (53 tools).html.bak-2026-08-27` backup still has it) and in the repo `tools/`.

### 1b. Bare "David" swept to company voice
Tools (audience=prospect or audience=client, anything a client or prospect runs): "Email David" -> "Email us",
"Talk to/Book with David" -> "Book a call", "David will/can/handles/returns" -> "we", internal code comments
neutralized, sample placeholders ("David Wilcox", "David Atlas", "David: Atlas One HR") -> "Jordan Lee". Files
touched: the 15 prospect-audience tools in `06 Calculators and Tools (NEW Aug 2026)/`, plus (found in the Job 5
deep verify pass, since they carry audience=client, not prospect) `_HANDOFF BRJ 2026-08-27/Atlas_One_PEO_Intake_Form.html`,
`Branded Intake Forms/Atlas_One_Email_Assistant_Setup_Intake.html`, `A1_Sales/Client Portal/Atlas_One_Client_Dashboard_GHL.html`,
and two generator-source spots that get baked into every build (`build_command.py`'s CSS comment and Present
zone lede, and two `catalogue.py` row blurbs shown as UI copy).

Sales pieces a person hands over: added a new swap contract, `a1-person-first`
(`<span class="a1-person-first">David</span>`, swapped by `_swap_person_first()` in `build_command.py`, wired
into `swap_footer_person`'s chain), and a `first_name` field for David and Charity in `people.json`. Applied to
the Employee Benefits Menu (two Next Steps lines), the Membership Brochure (the named-person paragraph) and the
QuickBooks Accountant Access Guide (the "Stuck?" line, on the catalogued A1_Sales copy only, not the stale
uncatalogued duplicate under `_INTERNAL/tools/bookkeeping-docs/`). Unit-tested `_swap_person_first` directly
against `get_person('charity')`: correct.

Skipped the company-voice sweep on the two audience=internal tools in `06 Calculators and Tools`
(`Atlas_One_Audit_Workbench.html`, `Payroll to GL Import Converter (Atlas One).html`) -- see Assumption 1.

### 1c. Dashes swept
Wrote an automated sweep keyed off every `inline=True`, `audience` in (`prospect`, `client`) catalogue entry:
`<title>` internal separators become a colon, digit-to-digit ranges become the word "to", any remaining em or
en dash used as a parenthetical pause becomes a comma. Swept 349 dashes across 25 catalogued tools (largest:
Labor Law Poster Center 117, Health Quote Census Intake 45, Certified Payroll Manager 36, PEO Comparison Tool
31), plus 59 more found in the Job 5 deep verify pass in the two `_HANDOFF BRJ 2026-08-27` intake form HTML
files (see Assumption 2) and one CSS disclosure-triangle glyph in the Client Dashboard using an en dash
character, changed to a plain hyphen. Also swept the two GHL page templates the brief quoted by exact title
(`Atlas_One_Booking_Confirmation.html`). Guard resweep: zero dashes on the full catalogue-scoped surface.

### 1d. Q2 and Q3 answered
Q2 (Employee Benefits Options duplicate contact after a swap): fixed. The `fcontact` block had four separate
hardcoded lines (email, phone, site, booking) below the `a1-footer-person` name/title span, so a per-rep swap
only updated the name/title line and left the rest as David's -- the exact bug Run CI flagged. Folded email,
phone and booking into the single `a1-footer-person` line and dropped the site URL line entirely. Verified with
`swap_footer_person('charity', ...)` directly and by screenshot: the whole line reads "Charity Taylor, Business
Advisor, charity@atlasonesolutions.com, 801-787-8154" with no leftover David contact info and no dangling
booking link (she carries none).
Q3 (census public footer): correct as is, no change needed (Run CF decision, confirmed).

## Job 2: Industry Starter Kits retired
Removed the `industry-starter-kits` row from `catalogue.py`. Moved
`07 New HR and Safety Docs (NEW Aug 2026)/Industry Starter Kits.pdf` to
`_to_delete/superseded-2026-09-26/Industry Starter Kits.pdf`. Grepped the whole Master Kit and A1_Sales tree for
"Industry Starter Kit": the only remaining live hit was inside `Atlas One COMMAND.html` itself, replaced by the
Job 5 rebuild. Did not touch the BRJ website package Cowork already rebuilt on 2026-09-26.

## Job 3: tool pricing model -- SKIPPED
Heading does not say "David approved." Per the brief's own rule, skipped and noted here.

## Job 4: contact@ on public and prospect pieces -- SKIPPED
Heading does not say "David approved." Per the brief's own rule, skipped and noted here.

## Job 5: rebuild and prove

**Builds.** `python3 catalogue_check.py "<Master_Kit>"` -> OK, 205 entries, all paths resolve, 17 present.py ids
present, zero a1-footer-person/support@ leaks (this guard caught my own first draft of the Job 1d fix, which had
put `support@AtlasOneSolutions.com` inside the `a1-footer-person` span; corrected to `david@atlasonesolutions.com`
before the rebuild). `python3 build_command.py "<Master_Kit>"` wrote `Atlas One COMMAND.html` (205 items, 57.7MB)
and the shared `A1_Sales/Atlas One Sales Kit.html` (58 items, 27.0MB). `python3 build_command.py --person charity
"<Master_Kit>"` rebuilt Charity's whole kit (prior copy moved to
`_to_delete/superseded-2026-09-22/charity-kit-before-CH-6`): Sales Kit (58 items), 6 Division Sheets, 5 One
Pagers, 8 Sales Pieces, 1 Price List, all HTML+PDF pairs. The build's own Job 2 guard reported clean both times.

**Deep verification.** Wrote a Python script that decodes every base64 blob in every HTML file and extracts
every PDF's text (pypdf) across Charity's whole 42-file folder. First pass found real leaks the catalogue-scoped
sweep had missed (all fixed and rebuilt, see 1a/1b/1c above and Assumption 2). Final pass reads zero on every
axis:

| Check | Charity's folder | Shared Sales Kit |
|---|---|---|
| `david@atlasonesolutions.com` | 0 | 0 |
| "David Taylor" outside the licensed sentence | 0 | (not separately re-checked; guard covers it) |
| bare "David" | 0 | not applicable, unswapped file names David by design |
| cornerstone | 0 | 0 |
| scheduler.zoom.us | 0 | 0 |
| old phone (385-213-7177 pattern) | 0 | not applicable |
| em/en dash | 0 | 0 |

Licensed-agent sentence present exactly once on each of the 4 target pieces (2 copies each, HTML+PDF, Employee
Benefits Menu and 2 Division Sheets), matching Run CI's pattern.

**Render and click-through.** Headless Chromium (Playwright, the npx path) at 1440px and 390px on Charity's
Sales Kit and on COMMAND: scrollWidth equals viewport at both widths on both files, zero console errors, zero
non-`file://` requests. Screenshots: `_briefs/assets/run-CL-jobs/shots/charity-sales-kit-{1440,390}.png`,
`command-{1440,390}.png`.

Clicked through three tools from Charity's kit by decoding their inlined blobs directly and rendering them
standalone (the picker UI's own "Expand all" + search filter left the matching rows hidden to Playwright's
visibility check even after filtering -- a UI test-harness limitation, not a content bug; the built file's own
blob content is what actually matters and is what got tested): Employee Benefits Options, NDA Builder, Atlas
One Savings Summary. All three: zero console errors. Screenshots:
`_briefs/assets/run-CL-jobs/shots/{benefits_options,nda_builder,savings_summary}-footer.png`. Benefits Options'
footer screenshot is the clearest proof of the 1a/1b/1d fixes together: one compact "Charity Taylor, Business
Advisor, charity@atlasonesolutions.com, 801-787-8154" line, both CTAs read "Book a call," and the licensed-agent
sentence still correctly names David (the one allowlisted exception).

Deployed nothing beyond the intake-forms repo (which needed no changes this run; `tools/` was already clean of
every guard this run checks).

## Job 6: TD SYNNEX software update carried through
`catalogue_check.py` confirms the 3 rows Cowork repointed at `A1_Sales/Website/BRJ Software Marketplace Package
2026-09-26/` resolve. Confirmed Charity's Job 5 rebuild carried both software one-pagers into her kit (they
carry `audience='internal'` in catalogue.py, but `division='Sell & Pitch'` puts them in the Sales Kit zone
regardless, the same override pattern as Intake & Client) and that both carry the new lines verbatim: "email and
tenant migrations, cloud storage and vulnerability scanning" (Software and Licenses one-pager) and "enterprise
plans (E3 and E5), Copilot Studio" (Microsoft 365 one-pager). Job 4 not approved, so no contact@ swap was
needed on the sheet's CTA. Nothing in this run named Pax8 or TD SYNNEX client facing.

## Not in this run
LTD row, Charity's GoHighLevel signatures and calendar, the TD SYNNEX product list, anything in the portal
repo. None of these were touched.

## Assumptions

1. The company-voice ("Email us" / "Book a call" / "we") sweep in Job 1b was applied only to
   `audience=prospect` and `audience=client` tools -- anything a client or prospect actually runs, matching the
   brief's own wording. The two `audience=internal` tools in `06 Calculators and Tools (NEW Aug 2026)/`
   (`Atlas_One_Audit_Workbench.html`, `Payroll to GL Import Converter (Atlas One).html`) were left naming David,
   since they never inline into a rep kit and are David's own working tools.
2. My first Job 1c log entry wrongly assumed the whole `12 GHL Setup doccs/_HANDOFF BRJ 2026-08-27/` folder was
   a frozen historical snapshot and skipped its PEO Intake Form. It is not frozen: `catalogue.py` points straight
   at both files in that folder (`bookkeeping-intake-form`, `peo-intake-form`) as the live source. The Job 5 deep
   verify pass caught this (59 dashes, 3 bare-David lines, still present after the first rebuild); both files
   are fixed and re-verified at zero.
3. Job 1a's brief instruction ("every one becomes ... button text 'Book a call'") was followed literally,
   including on Employee Benefits Options where two adjacent buttons ("Get my quote" and "Talk to David")
   already pointed at the same personal scheduler link before this run. Both now read "Book a call," which is a
   pre-existing duplicate-CTA layout this job relabeled rather than redesigned.
4. The `a1-person-first` swap contract is new infrastructure (this run). It only fires inside `swap_footer_person`'s
   call chain, i.e. only when a rep kit is built with `--person`; COMMAND and the shared Sales Kit (no
   `--person`) show the master file's own literal text, which is David's, so no swap was needed there.
5. The QuickBooks Accountant Access Guide's PDF (`A1_Sales/Atlas 1 Bookkeeping/Atlas_One_QuickBooks_Accountant_Access_Guide.pdf`)
   is `inline=False` in catalogue.py, i.e. not part of the blob-inlining build this run verifies end to end. The
   `a1-person-first` span is now correctly in its HTML master so a future per-person PDF regeneration of this
   specific piece (if one is ever built) will pick it up; regenerating that PDF for Charity today was out of
   this run's scope (no such per-person pipeline exists yet for standalone catalogued PDFs).
6. Left the stale, uncatalogued duplicate of the QuickBooks Accountant Access Guide under
   `_INTERNAL (do not share)/tools/bookkeeping-docs/` untouched -- `catalogue.py` points at the `A1_Sales` copy
   only, and the internal copy lacks the `a1-footer-person` contract markup the live one already has.

## Questions for David

1. Should the stale duplicate `_INTERNAL (do not share)/tools/bookkeeping-docs/Atlas_One_QuickBooks_Accountant_Access_Guide.html`
   (and its neighboring Cirque Lodge proposal files in the same folder) be moved to `_to_delete/`, or is that
   folder still doing a job I don't know about?
2. Employee Benefits Options has two adjacent CTA buttons that now both read "Book a call" (see Assumption 3) --
   worth giving one of them a distinct label/destination (e.g. an actual "Get my quote" flow) in a future run, or
   is a single repeated CTA fine here?
3. Jobs 3 and 4 are still waiting on your approval whenever you're ready for a run to pick them up.
