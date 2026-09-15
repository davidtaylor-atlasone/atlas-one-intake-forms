# Run AS report (GHL-JOBS terminal): agreements and proposal masters, one door lines, launcher fixes

2026-09-15. Four jobs, all complete, committed and pushed to the repo (main). Prior report (Run AR)
backed up to `_to_delete/superseded-2026-09-15/prior-reports/RUN-GHL-JOBS-report-RunAR.md`. Brief read
from `_BUILD-LOG/BRIEF-GHL-JOBS.md`, copied to `_briefs/BRIEF-GHL-JOBS-2026-09-15.md` in the repo. Also
read the sign and bill spec (`_BUILD-LOG/sign-and-bill-system-spec-2026-09-15.md`) and the 2026-09-11
agreements and proposal brief for context.

## Built

### Job 0: launcher fixes from Run AR

- `_INTERNAL (do not share)/build_command.py`: removed the "Atlas One Tools (share with prospects).html"
  output entirely, per David (2026-09-15: prospects use the public forms.atlasonesolutions.com pages,
  paid builders stay behind the internal COMMAND launcher). Kept the catalogue `audience` field and the
  forbidden-term guard; it now runs against COMMAND's own prospect and client audience rows (a new
  `check_audiences` parameter), since COMMAND legitimately carries internal-audience rows that name
  vendors and margins and must not be scanned. The build also hard-refuses the retired filename outright.
  Old prospect file backed up to `_to_delete/superseded-2026-09-15/launchers/`. Rebuilt COMMAND (171
  items at that point, guard clean); confirmed the prospect Tools file is not recreated.
- Repo hygiene: moved `_briefs/assets/run-AI/cadence-emails/` (stale renders carrying the old phone
  number) to `_briefs/assets/_stale/run-AI-cadence-emails/` with a README pointing at the real source of
  truth on OneDrive. Swept the repo for 385-213-7177: only `tools/phone_sweep.py` (the sweep utility
  itself, expected to carry the old number as its search target) and historical build-journal, brief and
  report text remain; both out of scope, left untouched per Run AQ precedent.

### Job 1: the "one door" line in every client-facing cadence email

- `_BUILD-LOG/cadence-emails-2026-09-13/ONE-DOOR-LINES.md`: twelve one-sentence lines, one per service
  family (benefits and 401(k); workers comp; general liability, E&O, cyber and bonding; bookkeeping and
  tax; certified payroll; software, licenses and IT; AI Email Assistant and AI Task Agent; handbooks,
  safety manuals and HR documents; vendor and software audit; COI tracking; payroll to QuickBooks
  journals; custom requests welcome). No prices, no dashes, no vendor names, David's voice.
- Inserted one line, rotating through the list in send order, as its own paragraph just above the
  signature in all 39 client-facing files (prospecting, books, booking, intake, confirmations, won
  emails). Skipped the three internal-* staff notification files and the two booking reminders per the
  brief. `email-3.html` is named in INDEX.md as a placeholder send but does not exist in the directory
  (a gap from a prior run); nothing to edit there. The six placeholder sends (body read live from GHL)
  get the line as a ready-to-paste paragraph with an HTML comment telling the GHL terminal where to place
  it, since the file does not carry the live body to anchor against directly. Existing footer line
  unchanged. Files backed up first to `_to_delete/superseded-2026-09-15/cadence-emails-before-onedoor/`.

### Job 2: the proposal shell and the agreement set (masters, Word + PDF, brand locked)

- Confirmed by search: the Master Client Services Agreement and the standalone Hold Harmless that How
  They Fit describes were not on OneDrive anywhere (same finding as the 2026-09-11 audit). Built both
  from scratch.
- New generator: `_INTERNAL (do not share)/tools/agreements/generate.py` (python-docx), reading client
  prices only from a new `_INTERNAL (do not share)/tools/agreements/prices.json` (pulled from the Quick
  Quote catalogue and Master Pricing V8; no vendor cost or margin in the file). Fonts (DM Sans, Horas)
  and the general approach copied from `tools/bookkeeping-docs/`. PDF produced by LibreOffice headless
  conversion of the docx (`soffice --headless --convert-to pdf`) rather than bookkeeping-docs' HTML plus
  Playwright pipeline, since these are true editable Word masters, not HTML-only proposals; this keeps
  the same "generate it, never hand edit the output" discipline with a different last step. The
  generator raises on any em dash or en dash reaching client copy, the same check build.py uses.
- 19 documents built (docx and PDF) into `A1_Sales/A1 Agreements/2026-09-15 masters/`:
  - Master Client Services Agreement
  - Hold Harmless and Acknowledgement (standalone)
  - Schedule, Bookkeeping
  - Schedule, Payroll to GL Converter
  - Schedule, Certified Payroll
  - Schedule, WC Audit Recovery
  - Schedule, COI Tracking
  - Schedule, AI Services (regenerated; prices verified to match the existing schedule exactly)
  - Schedule, Document Services
  - Schedule, Membership
  - Proposal Shell (blank master)
  - Eight sample proposals, one per Schedule, for a fictional client, Tell Me More LLC
- Every agreement and Schedule carries an "ATTORNEY REVIEW PENDING" banner. Four colours only, no
  dashes anywhere in the generated copy (enforced by the generator, not just checked after the fact).
  Did not touch or overwrite the existing `Atlas_One_AI_Services_Schedule.docx` in the parent Agreements
  folder; confirmed its mtime is unchanged after this run.
- Updated `A1_Sales/A1 Agreements/Atlas_One_Agreements_How_They_Fit.md` with the new set and a quick
  reference table for which Schedule to send with which sale.
- Added all 19 documents to `catalogue.py` (Agreements section, NEW badge). `catalogue_check.py` passes
  clean: 184 entries, all paths resolve. Rebuilt Atlas One COMMAND (184 items, forbidden-term guard
  clean).

### Job 3: Quick Quote price line

- `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`: `gl_import` now carries `setup:250` (kept
  `editable:true`) plus a documentation note describing the frequency model ($75/mo monthly, semi-monthly
  or bi-weekly; $125/mo weekly, via the same editable rate field every other price in the tool already
  uses; this matches the existing convention where a `note` field documents pricing detail without being
  rendered in the UI, the same as several other services in the file). Added a new `per_unit_mo` line
  `gl_import_extra` at $25/mo per extra entity or state. Backed up the pre-change file to
  `_to_delete/superseded-2026-09-15/quick-quote-before/`. Rebuilt COMMAND (171 items at that point, guard
  clean).
- Also updated `Atlas_One_INTERNAL_Master_Pricing_V8.xlsx` (Financial Services sheet, row 14, Notes
  column) with a "proposed 2026-09-15" note describing the same frequency model, per the spec. Backed up
  first; left the retail price and setup fee columns as-is pending David's approval (spec's own Open
  item). This xlsx edit succeeded this run (a prior run, Run AQ, hit a harness guardrail blocking
  in-place office file overwrites even with a backup; that guardrail did not trigger this time).

## Verification

- Job 0: COMMAND rebuilt clean (171 to 184 items across the run), renders with 0 console errors and 0
  non-file network requests at 1440px and 390px, light and dark; the prospect Tools file confirmed absent
  after rebuild.
- Job 1: rendered `email-1.html`, `won-email-6.html` and `45-b.html` (a placeholder) headless at 390px:
  scrollWidth equals viewport, 0 console errors; the only non-file network request in any of these is the
  existing GHL-hosted header image, unchanged from before this job (email templates are not held to the
  same fully-offline standard as the HTML tools, since they are meant to be pasted into GHL, which hosts
  the logo image itself).
- Job 2: rendered every one of the 19 PDFs' first page to PNG and looked at all of them. Used two
  independent renderers after finding LibreOffice's own headless PNG export was dropping thin glyphs
  (lowercase i, some e's) at normal body text size on this machine: confirmed via `pypdf` text extraction
  that the actual PDF content was correct, and via `sips` (macOS's native Quartz PDF renderer) that every
  glyph displays correctly at normal size. The bug was isolated to LibreOffice's own low-resolution PNG
  rasterizer, not the deliverable PDFs; installed the DM Sans and Horas TTFs system-wide plus Homebrew
  fontconfig so the LibreOffice conversion path has the real brand fonts available (previously it was
  silently substituting a fallback), and switched all further QA screenshots to `sips`.
- Job 3: rendered Quick Quote at 1440px and 390px: 0 console errors, scrollWidth equals viewport at both,
  0 network requests. Toggled the GL import row on screen to confirm the $75/mo rate, $250 setup field,
  and the new extra-entity add-on all display and calculate correctly.

## Assumptions

1. Job 0: removing "Atlas One Tools (share with prospects).html" entirely (not just retiring it) matches
   David's own words in the brief ("prospects use the public pages"), so the builder no longer writes
   that file at all rather than writing an empty or redirect stub.
2. Job 0: the forbidden-term guard on COMMAND now scopes its grep to prospect- and client-audience rows
   only (`check_audiences`), since COMMAND (unlike the old prospect-only Tools file) legitimately carries
   internal rows that name vendors, margins and commissions on purpose. The old "no Internal-division item
   leaked into the prospect build" check was removed since it no longer applies to a single, all-audience
   launcher.
3. Job 1: rotated the twelve one-door lines in "send order" grouped as prospecting, books, booking,
   intake, confirmations, won emails, in roughly the order each group's own send sequence runs (per
   INDEX.md), since the brief said "in send order" without spelling out the exact 39-file sequence.
4. Job 1: for the six placeholder sends (body kept live in GHL, not stored in this repo's copy), the
   one-door line is delivered as a ready-to-paste paragraph inside an HTML comment rather than physically
   inserted above a signature that is not present in the file, since the actual live body and its
   signature are not captured here. The GHL terminal places it when it next touches that send.
5. Job 2: catalogued Bookkeeping, GL Converter, WC Audit Recovery and COI Tracking as four separate one
   page Schedules (matching this run's own Job 2 brief, which lists them as four items), rather than the
   sign-and-bill spec's "Software Tools Schedule" grouping that combines GL Converter and COI Tracking
   into one Schedule. The direct job brief for this run is more specific than the broader spec and took
   precedence; flagged here so the spec and How They Fit can be reconciled later if David wants the
   grouped version instead.
6. Job 2: "ATTORNEY REVIEW PENDING" is a solid periwinkle banner across the top of the document rather
   than a diagonal Word watermark. A true diagonal watermark needs a VML shape injected into the header
   XML, which is fragile across Word and LibreOffice versions and effectively invisible when a page is
   converted to PDF at low contrast; a solid banner is unmissable, reliable everywhere, and stays inside
   the four-colour rule (no need for a translucent red diagonal, which would add a fifth colour).
7. Job 2: PDF generation uses LibreOffice headless conversion of the docx, not an HTML-plus-Playwright
   pipeline like bookkeeping-docs. These are true editable Word masters (the brief calls for "Word + PDF"
   outputs), so the docx is the authored source and the PDF is a faithful rendering of it, rather than a
   second, separately-authored HTML document standing in for the Word file.
8. Job 2: the bookkeeping catch-up rate is documented as "billed at your plan's monthly rate for each
   month of catch up needed, prorated for a partial month" rather than a separate fixed number, since no
   distinct catch-up price exists anywhere in Quick Quote, Master Pricing V8, or the bookkeeping marketing
   sheet (only "each engagement is scoped and priced" language for advisory work). This is the common,
   reasonable default for catch-up bookkeeping billing and does not invent a number that is not backed by
   an existing source.
9. Job 3: the gl_import frequency detail (which rate applies to which payroll frequency) lives in an
   unused-by-the-UI `note` field on the service entry, matching the existing convention several other
   Quick Quote services already use for documentation that is not rendered on screen (for example `aca`
   and `open_enroll`). The actual $75 versus $125 choice is made the same way every other adjustable
   price in the tool is made: David types over the rate field for a weekly-payroll client.

## Skipped

- The PEO Schedule and the book-of-business / non-circumvention protection (both explicitly waiting on
  the Cornerstone and G&A CSAs, per How They Fit; not part of this run's Job 2 scope).
- GHL browser work (Documents & Contracts templates, products, recurring-invoice templates, the QuickBooks
  integration, the sign-and-bill workflow): explicitly step 2 of the spec's build order and explicitly the
  GHL browser terminal's job, not this one.
- The portal "Add this" wiring: explicitly step 3 of the spec's build order, a different terminal's job.

## Questions for David

1. **WC audit recovery contingency percentage.** The Schedule ships with `[__]%` as a placeholder. What
   percentage of recovered premium is Atlas One's fee?
2. **COI tracking monthly price.** No price for this service exists anywhere in Quick Quote or Master
   Pricing V8; the Schedule ships with a `[__]` placeholder. What should the monthly price be?
3. **Late fee.** Carried over from the 2026-09-11 audit and the spec's own Open list: keep the invoice
   template's $20-after-the-5th late fee and turn it on in GHL, or drop it? The Master Client Services
   Agreement's fees clause also ships with a `[__]` placeholder for this same number, so it needs to be
   the same answer in both places.
4. **GL converter pricing approval.** The frequency model built into Quick Quote and noted in Master
   Pricing V8 this run ($75/mo monthly, semi-monthly or bi-weekly; $125/mo weekly; $250 setup, waived on
   Professional and above, included in Concierge; $25/mo per extra entity or state) is the spec's own
   proposed pricing decision. Approve as-is, or change any of these numbers?
5. **Attorney review.** Every new agreement and Schedule carries the "ATTORNEY REVIEW PENDING" banner and
   is not yet cleared to send for a real client signature. When counsel has reviewed the Master Client
   Services Agreement and the Hold Harmless, the banner and the corresponding line in generate.py should
   come out and every document rebuilt.
6. **Schedule grouping.** This run built WC Audit Recovery, COI Tracking, and GL Converter as three
   separate Schedules (per this run's own brief); the sign-and-bill spec describes GL Converter and COI
   Tracking sharing one "Software Tools Schedule" instead. Keep them separate, or should a future pass
   merge GL Converter and COI Tracking into one Schedule to match the spec, with How They Fit updated to
   match?
