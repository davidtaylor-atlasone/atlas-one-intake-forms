# RUN-AU-report.md (GHL-JOBS terminal, 2026-09-15)

Both jobs of the brief (`_BUILD-LOG/BRIEF-GHL-JOBS.md`, copied to `_briefs/BRIEF-GHL-JOBS-2026-09-15.md`
in the repo) are complete, verified, committed and pushed. Prior report backed up to
`_to_delete/superseded-2026-09-15/prior-reports/RUN-GHL-JOBS-report-RunAT.md`.

## Built

### Job 1: Software and Licenses Schedule, MSA and Hold Harmless amendments (Pax8 partner terms flow down)

- **`prices.json`, new `software` section.** Microsoft 365 Business Basic, Business Standard, Business
  Premium, and "any other resold software product," all priced "quoted, confirmed on the client's
  invoice." Quick Quote (`09 Quick Quote Tool/Atlas_One_Quick_Quote.html`) and Master Pricing V8 have no
  per product resold software client price anywhere; the only related line is the general "Software
  marketplace" item, itself priced `model:"quoted"`. See Questions for David.
- **New Schedule: Atlas_One_Software_and_Licenses_Schedule (docx + PDF, one page, ATTORNEY REVIEW PENDING
  banner).** `tools/agreements/generate.py`'s new `schedule_software_licenses()`: what is covered (named
  by product, never by distributor), vendor terms accepted by reference and no resale, commitment term
  matches the vendor's own term with auto renewal and no mid term cancellation on annual products (full
  remaining term owed if the Client leaves early), seat counts and true ups on the Client and billed as
  they happen, vendor price changes passed through with thirty days notice, automatic payment (ACH or
  card on file) required, Atlas One provisions and supports the tenant while the vendor provides the
  service, and the Client keeps its own data and tenant per the vendor's terms on termination. Pricing
  table from the new `software` section.
- **Master Client Services Agreement, new Section 11 ("Resold software and AI features").** Client
  indemnity for third party claims arising from the Client's misuse of resold software, the Client's use
  of AI output without the required human review, a virus or harmful code the Client introduces, or the
  Client's violation of a product vendor's own terms; a liability cap for resold software equal to the
  fees paid in the two months before the claim, replacing the general three month cap (Section 9) for
  that product only; a sentence that AI features in resold products can produce inaccurate output and the
  Client keeps a human in the loop. Governing law and General renumbered 11 to 12, 12 to 13. Section 2's
  late fee bracket is now filled in: "1.5% per month, or the highest rate the law allows, on amounts more
  than fifteen days past due" (matches Pax8's own late payment term; David's recommended default pending
  his answer, per the brief).
- **Standalone Hold Harmless and Acknowledgement, new Section 3 ("AI acknowledgement").** Extends AI
  coverage from an Atlas One AI assistant to "any AI product or feature Atlas One provides or resells,"
  naming a resold product's own AI feature (Microsoft 365 Copilot) as an example, with the same
  inaccurate output / human in the loop language as the MSA's new clause. See Assumptions for why this
  clause was written fresh rather than literally extended from existing text.
- **PDF pipeline fixed (again).** The PDF conversion step this run inherited was still `soffice --headless
  --convert-to pdf` (LibreOffice), even though `RUN-AT-report.md` and the live log both describe a
  Playwright/HTML rewrite as already done and verified; see Assumptions for the discrepancy. Reproduced
  the wrong font bug fresh (`BaseFont` came back `LinuxLibertineG`) and rebuilt the fix: every `build_*`
  function in `generate.py` now writes each piece of client copy once into a `Sink` object that carries
  both a python-docx `Document` (unchanged editable master) and a parallel HTML string using the same
  brand CSS and Horas/DM Sans fonts embedded base64 as `tools/self-assessment/index.html`.
  `render_all_pdfs()` batches every queued document through one headless Chromium session (Playwright, at
  the path CLAUDE.md documents) and prints each to PDF, waiting on `document.fonts.ready` before printing
  (a first pass without that wait let one heading on a page that had just spilled to page 2 render in a
  browser fallback font before the Horas file finished loading).
- **Regenerated all 20 docx and PDF pairs** (the 19 that existed plus the new Software and Licenses
  Schedule) into `A1_Sales/A1 Agreements/2026-09-15 masters/`. Backed up the pre run set (generate.py and
  the whole masters folder) to `_to_delete/superseded-2026-09-15/agreements-pre-runAU/`.
- **Page fit.** The new schedule first came out at 2 pages (signature block spilling). Tightened clause
  spacing (space before 8pt to 6pt) and page margins (1.6cm to 1.0cm top/bottom) and added
  `page-break-inside: avoid` on table rows; 19 of 20 documents are now one page, the 13 clause Master
  Client Services Agreement is a legitimate 2 pages (same as before this run).
- **Catalogue and COMMAND.** Added 2 entries to `catalogue.py` (docx + PDF) for the new schedule;
  `catalogue_check.py` passes clean at 186 entries (up from 184). Rebuilt `Atlas One COMMAND.html`
  (title stamp confirmed: "Atlas One COMMAND: build Sep 15, 2026 3:07 PM", 186 items).
- **Updated `Atlas_One_Agreements_How_They_Fit.md`** with a Run AU section (what changed and why) and a
  Send table row for resold software.

### Job 2: software cards notice (file only)

- Wrote `_BUILD-LOG/cadence-emails-2026-09-13/software-terms-line.md`: the one line notice ("Annual
  licences renew automatically and cannot be cancelled mid term; by ordering you accept the product
  vendor's terms") and a two sentence plain explanation, for the PORTAL terminal to paste onto software
  cards and the GHL terminal to paste as Form C1's software block first field label. No build beyond the
  file, per the brief.

## Verification

- **BaseFont proof.** `strings <pdf> | grep BaseFont` on all 20 regenerated PDFs shows only
  `Horas-Medium`, `DMSans-Regular`, `DMSans-Bold`; a scripted loop over the whole folder found zero hits
  for any other font name. Two file proofs:
  - `Atlas_One_Master_Client_Services_Agreement.pdf`: `/BaseFont /AAAAAA+Horas-Medium`,
    `/BaseFont /BAAAAA+DMSans-Regular`, `/BaseFont /CAAAAA+DMSans-Bold`
  - `Atlas_One_Software_and_Licenses_Schedule.pdf`: same three, same subset tags
- **No dashes.** Scripted check of `word/document.xml` inside all 20 regenerated `.docx` files for an
  em or en dash: zero found. `generate.py`'s own `check_no_dash()` also raises at build time if one
  reaches any paragraph (unchanged from prior runs); the new schedule and clauses were written clean.
- **Page counts.** Counted `/Type /Page` objects in all 20 PDFs: 19 are 1 page, the Master Client
  Services Agreement is 2 pages (unchanged from before this run, now with 13 clauses instead of 12).
- **Looked at renders.** `_briefs/assets/run-AU/shots/`: page 1 of the new Software and Licenses Schedule
  (watermark banner, all 7 clauses, pricing table, signature block, footer, all on one page); both pages
  of the Master Client Services Agreement (new Section 11 reads correctly, Governing law/General
  correctly renumbered 12/13, late fee bracket filled in); page 1 of the Hold Harmless (new Section 3 AI
  acknowledgement reads correctly). Confirmed the brand colours, Horas headings, DM Sans body, and that
  Horas's own lowercase glyphs render in a script style consistently across documents (not a
  fallback-font bug: cross checked "To accept" on both the new schedule and the MSA page 2, matching
  glyph shapes, `BaseFont` still `Horas-Medium` on both).
- **catalogue.py / COMMAND.** `catalogue_check.py` passes clean at 186 entries, all paths resolve.
  `build_command.py` rebuilt `Atlas One COMMAND.html` (186 items); title stamp confirmed. (No prospect
  facing Tools output to rebuild: David retired it in Run AS's Job 0, per that run's live log.)

## Assumptions

1. **The AI acknowledgement was written fresh, not literally extended.** The brief says to extend the AI
   acknowledgement "from 'Atlas One assistants' to 'any AI product or feature Atlas One provides or
   resells.'" Searched the whole Master Kit (excluding `_to_delete`) for "Atlas One assistants" and any
   AI acknowledgement clause and found no such text anywhere, including in the standalone Hold Harmless
   itself, which had no AI content at all before this run. Wrote the clause directly to the wider end
   state text the brief specifies, as a new Section 3, rather than trying to locate and edit
   nonexistent prior wording.
2. **Run AT's font fix did not survive on disk.** `RUN-AT-report.md` (now backed up) and the
   `TERMINAL-GHL-JOBS-live.md` entry from 2026-09-15 09:22 both describe rewriting `generate.py` into a
   block based generator with a companion `tools/agreements/_render_pdf.mjs` (Playwright), regenerating
   all 19 PDFs, and confirming clean `BaseFont` output. Neither that rewrite nor `_render_pdf.mjs` exist
   in `tools/agreements/` today; `generate.py` still had the original `soffice --headless --convert-to
   pdf` conversion step, and a fresh test of that step reproduced the original `LinuxLibertineG`
   substitution bug. The 20 PDFs already sitting in `A1_Sales/A1 Agreements/2026-09-15 masters/` at the
   start of this run did carry the correct `BaseFont` values, so Run AT's regenerated *output* did land
   on OneDrive even though its changed *generator script* apparently did not (or was reverted by some
   later, unlogged edit). Treated this as an open question rather than investigating further, since
   redoing the fix was faster and is now verified end to end; see Questions for David.
3. **Software pricing is "quoted" across the board.** Followed the brief's own fallback ("if Quick Quote
   has no line for a product, print 'quoted' and list it in the report") rather than inventing a
   Microsoft 365 per seat price. Listed three common Microsoft 365 Business tiers (Basic, Standard,
   Premium) as the likely products David resells via Pax8, plus a generic "any other resold software
   product" line, all quoted.
4. **Clause numbering, not clause splitting.** Inserted the new MSA clause as a single Section 11 covering
   indemnity, the liability cap, and the AI sentence together (the brief lists these as one job item),
   rather than three separate numbered clauses, to keep the document from growing past a clean 2 pages.
5. **Tightened spacing and margins apply to every document, not just the new schedule.** Reducing clause
   spacing and page margins to fit the new 7 clause schedule on one page also applies to the 19 existing
   documents on rebuild; all still render as one page (or 2 for the MSA) with more headroom than before,
   so no document lost content or layout integrity, confirmed by the page count check above.

## Skipped

- Nothing in the brief was skipped. No hard stop was triggered (no email/SMS, no HIPAA toggle, no file
  deletion, only moves to `_to_delete/`, no production deploy, no spending).

## Questions for David

1. **No Microsoft 365 (or other resold product) client price exists anywhere in Quick Quote or Master
   Pricing V8.** The Software and Licenses Schedule's pricing table is entirely "quoted" as a result.
   Once you have per seat client prices for the Microsoft 365 tiers (and any other Pax8 backed product
   you resell), they belong in `prices.json`'s new `software` section and the Quick Quote catalogue.
2. **Late fee, 1.5% per month after 15 days past due.** Filled in as your recommended default (matches
   Pax8's own late payment term) per the brief's instruction; confirm before this goes to a real client,
   same open item as Run AS/AT flagged for the general late fee clause.
3. **Where did Run AT's generator rewrite go?** (Assumption 2 above.) If you know of a separate edit that
   reverted `tools/agreements/generate.py` between Run AT and this run, worth understanding so the fix
   does not need doing a third time; otherwise this may be an OneDrive sync quirk worth watching on this
   machine.
4. **Attorney review banner.** Still on the Master Client Services Agreement, the standalone Hold
   Harmless, and now the new Software and Licenses Schedule too. Not touched this run since clearing it
   was not in scope; flagging since the amended documents (new clauses, correct fonts) could otherwise
   look ready to send.
5. **WC contingency percentage and COI monthly price** (carried over from Run AS/AT, still bracketed):
   unrelated to this run's Pax8 scope, still open.
