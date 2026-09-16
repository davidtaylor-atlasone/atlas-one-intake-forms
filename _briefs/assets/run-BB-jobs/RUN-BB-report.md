# Run BB report, GHL-JOBS terminal (files and code only)

Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md`, "employment document builders: California protection built in, old
pricing retired." Copied to the portal repo at `_briefs/BRIEF-GHL-JOBS-2026-09-16-RunBB.md`.

## Built

### Job 1, found every builder
There are exactly three live employment-document builders, all under `06 Calculators and Tools (NEW Aug
2026)/` and all referenced by `catalogue.py`:

- `W-2 At-Will Employment Agreement Builder (Atlas One).html` (catalogue id `w-2-at-will-agreement`). This one
  tool covers both the "W-2 at-will agreement" and the "offer letter" named separately in the brief; the
  brief's own catalogue blurb already describes it as building "a custom at-will offer letter and employment
  agreement." There is no separate offer-letter-only tool anywhere in the Master Kit, A1_Sales, or this repo.
- `Independent Contractor Agreement Builder (Atlas One).html` (catalogue id `contractor-agreement`), the 1099
  agreement.
- `NDA Builder (Atlas One).html` (catalogue id `nda-builder`).

Exact duplicate copies of all three existed under the "Atlas One, Complete Kit for BRJ" folder's
`10. Premium Builders (for paywall)/` subfolder, not referenced anywhere in `catalogue.py`. Moved all three to
`_to_delete/superseded-2026-09-16/builders/Complete Kit for BRJ premium builders/`. The `_gold_backup_2026-08-24`
snapshot copies were left untouched, that is a full backup tree, not a live duplicate. Backed up the three live
files themselves to `_to_delete/superseded-2026-09-16/builders/before-runBB/` before making any edits.

### Job 2, California logic (W-2 at-will / offer letter builder)
Added, keyed off the existing "Governing law (state)" picker (already covers all 50 states plus DC):

- `STATE_MIN_WAGE` table (50 states + DC, one editable block near the top of the script, dated 2026-01-01) used
  to compute the California exempt salary floor live: twice the California minimum wage for full time work,
  currently about **$70,304 a year**. A warning line appears under the FLSA field and is printed into the
  document itself when the entered salary is below the floor for a California exempt hire. Verified: warning
  off at $125,000, warning on at $50,000.
- Non-exempt in California now prints the daily/weekly overtime language (1.5x over 8/day or 40/week, 2x over
  12/day) plus the meal and rest break paragraph, in addition to the generic overtime line used elsewhere.
- A **Commissions Paid** toggle (OTE, rate, target, payment timing, draws/adjustments fields, defaulted from the
  Atlas One language in the Vet AI CA SVP Sales reference package). When on, the offer letter prints a
  commission reference paragraph (citing Labor Code 2751 when the state is California) and the tool always
  generates a real second document, the **Sales Commission Agreement**, appended on its own printed page in the
  same output (ten numbered sections: eligibility, OTE, rate and target, how/when earned, payment timing,
  draws/adjustments, plan changes, effect of separation, at-will, entire agreement/governing law).
- A new **State Specific Terms** section, built automatically:
  - California: PTO treated as wages (no forfeiture, payout at separation, reasonable accrual cap allowed),
    paid sick leave (Healthy Workplaces Healthy Families Act minimum, kept separate, not paid out at
    separation), final pay timing (immediate/72 hour rules), Labor Code 2802 expense reimbursement, and a hard
    non-compete block (Business and Professions Code 16600 not-enforceable note, which prints regardless of the
    non-compete toggle).
  - Other states: a `VACATION_AS_WAGES_STATES` list (California, Colorado, Illinois, Louisiana, Massachusetts,
    Montana, Nebraska, Nevada, North Dakota, Rhode Island) prints a payout-at-separation note, and a
    `SICK_LEAVE_STATES` table (19 states plus DC with a mandatory paid sick leave law) prints that state's
    accrual minimum. Both tables are internal summaries built into the tool, dated, and flagged in code comments
    to be confirmed against current state law before relying on them for a specific hire (see Assumptions).
- Added a **Non-compete** optional clause toggle for non-California states (never available for California,
  per the hard block above).

### Job 3, protection on every output, every state
Applied to all three live builders (W-2/offer letter, 1099, NDA):

- Every generated document now bundles a **Hold Harmless & Acknowledgement** page as its final printed page
  (same ten-section language as the Atlas One master: not a law firm, independent review, client
  responsibilities, disclaimer of warranties, hold harmless, indemnification, limitation of liability,
  governing law), with the **California Civil Code 1542 release and waiver** paragraph appended automatically
  whenever the document's governing state is California.
- An **Acknowledgement** block sits directly above the signature block on the main document (not just in the
  footer), referencing the bundled Hold Harmless page and stating that Atlas One is not a law firm, this is not
  legal advice, the client is responsible for classification and compliance, the client has had the
  opportunity to have counsel review the document, and the document was prepared from information the client
  supplied.
- The footer disclaimer on every document now carries that same language.
- A required checkbox, "I have read the Hold Harmless and Acknowledgement," gates every Print / Save as PDF
  button in all three tools: the button is disabled by default (HTML `disabled` attribute) and only enables
  once the checkbox is checked, with a JS guard on the click handler itself as defense in depth.
- Updated the actual **Hold Harmless master** (`_INTERNAL (do not share)/tools/agreements/generate.py`, both
  the repo copy and the Master Kit mirror, confirmed byte-identical after the edit): it did not carry the
  California 1542 waiver before this run. Added clause 5, "California, release and waiver of unknown claims
  (Civil Code 1542)," and updated the signature governing-law line to reference it. Backed up the masters
  folder to `_to_delete/superseded-2026-09-16/agreements-before-runBB/` first, then ran `generate.py` to
  regenerate all 21 docx/PDF pairs into `A1_Sales/A1 Agreements/2026-09-15 masters/`. Confirmed the 1542
  language is present in the regenerated `Atlas_One_Hold_Harmless_and_Acknowledgement.docx`, and the PDF
  BaseFont check still shows only `Horas-Medium` / `DMSans-Regular` / `DMSans-Bold`.

### Job 4, old pricing retired
Moved `Atlas_One_Employment_Documents_Pricing.pdf` and `Atlas_One_Employment_Documents_Overview.pdf` (the Aug
25 $650/$850 sheet) from `A1_Sales/Atlas 1 Agreements build/` to `_to_delete/superseded-2026-09-16/pricing/`.
Grepped the Master Kit and A1_Sales for stray "$650"/"$850" near "offer letter"/"employment": zero hits in any
text-searchable file. `prices.json`'s `documents` block (repo and `_INTERNAL` mirror, byte-identical) already
carried the correct live prices (`agreement_each` $450, `agreement_bundle` $1,200, `hr_docs` $175); no edit was
needed there, and none of the three builders print a price anywhere in their own UI or output, so there was no
builder price text to fix either.

Removing the two PDFs broke `catalogue_check.py` (two entries pointed at the now-retired files: id's
`employment-documents-pricing` and `employment-documents-overview`). Removed both entries from `catalogue.py`.
`catalogue_check.py` now reports 192 entries, all paths resolve.

### Job 5, verify and rebuild
Rebuilt Atlas One COMMAND: backed up the pre-run copy to
`_to_delete/superseded-2026-09-16/command-before-runBB/`, ran `build_command.py`, confirmed 192 items,
48,647,636 bytes, stamp `Atlas One COMMAND: build Sep 16, 2026 1:53 PM`. Verified in headless Chromium at
1440px: scrollWidth equals viewport, zero console errors.

## Verification (headless Chromium, Playwright, all six required test outputs)

Screenshots in `_briefs/assets/run-BB-jobs/shots/`.

1. **California exempt offer letter with commissions, $125,000 salary.** Floor warning off (confirmed no
   "Warning: this salary is below" / "Warning: the salary entered" text anywhere in the render). Both
   documents produced in a single output: the offer letter (with the Labor Code 2751 reference paragraph) and
   the Sales Commission Agreement, followed by the bundled Hold Harmless page with the 1542 waiver present.
   `w2_ca_exempt_125k_1440.png`, `w2_ca_exempt_125k_390.png`.
2. **Same, $50,000 salary.** Floor warning present in the rendered document.
   `w2_ca_exempt_50k_warning_1440.png`.
3. **California non-exempt.** Meal period and rest period language present; Healthy Workplaces Healthy
   Families sick leave and "treated as wages" PTO language present. `w2_ca_nonexempt_1440.png`.
4. **Texas at-will.** Hold Harmless page bundled, no California-only language present anywhere in the
   document. `w2_tx_atwill_1440.png`.
5. **New York 1099 (Independent Contractor Agreement).** Hold Harmless page bundled, footer protection
   paragraph present, print buttons correctly disabled until the acknowledgement checkbox is checked (both
   toolbar print buttons in this tool are gated together). `ic_ny_1440.png`, `ic_ny_390.png`.
6. **NDA.** Hold Harmless page bundled, print button gate behaves the same way. `nda_1440.png`, `nda_390.png`.

Across all six: zero console errors, zero non-`file://` network requests, `scrollWidth` equals the viewport at
390px, and a scan of every rendered document's full text found zero em dash or en dash characters. JS syntax
of every `<script>` block in all three builders checked with `node --check`.

## Assumptions

1. The brief's "offer letter" and "W-2 at-will agreement" builders are the same single tool (the catalogue's
   own blurb already describes it that way); Job 2's logic was built into that one file rather than split
   across two.
2. `STATE_MIN_WAGE`, `VACATION_AS_WAGES_STATES`, and `SICK_LEAVE_STATES` are internal summaries built from
   general knowledge of each law, dated 2026-01-01 in the code, not pulled from a live legal database. State
   minimum wages in particular change every January and, in a few states, more often (Denver, Seattle, and
   other city ordinances are not reflected at all, only state floors). The code comments flag every table to be
   confirmed with each state's labor department before being relied on for a specific hire; I did not attempt
   to verify all 51 rows against current statute text, only California's rate and the mechanics of the floor
   calculation, since that is the one the brief's test case depends on.
3. The Sales Commission Agreement is now generated whenever "Commissions Paid" is on, in any state, not only
   California (California is the only state where the brief requires it and where the reference paragraph
   cites Labor Code 2751, but generating the real document for every state is safer than generating it only
   for California and leaving other states with just a bonus/commission sentence).
4. The Hold Harmless page bundled into every generated document mirrors the Atlas One master's own language
   (now including the 1542 clause) rather than literally embedding the regenerated PDF file, since these
   builders are single self-contained offline HTML files with no server-side PDF merge step; printing the tool
   produces one PDF containing the main document, the commission agreement when applicable, and the Hold
   Harmless page, which satisfies "the protection travels with the document no matter who generates it."
5. For the Independent Contractor Agreement Builder, both existing Print buttons (one in the form toolbar, one
   in the preview header) are gated together off the same checkbox, since gating only one would leave an
   ungated path to print.
6. For the NDA Builder, the Hold Harmless page's governing-state selection follows the NDA's own optional
   "Governing Law" toggle (the tool does not require a state to be chosen); when that toggle is off, the
   bundled Hold Harmless defaults to Utah with no 1542 language, matching how the rest of that document handles
   an unselected state.
7. Non-compete clauses were added as a new optional toggle for non-California states; the tool previously had
   no non-compete clause at all (only non-solicitation), so this is new functionality, not a fix.

## Skipped
Nothing in the five jobs was skipped. The California minimum-wage-driven exempt floor is the only piece of the
new state data that was hand-verified beyond general knowledge, per Assumption 2.

## Questions for David

1. The California minimum wage used for the exempt salary floor ($16.90/hr for 2026, giving a floor of about
   $70,304/yr) is my best recollection, not a fresh pull from the California Department of Industrial
   Relations. Please confirm the current rate so the floor in the tool is exact, since it changes every
   January 1.
2. Should the `STATE_MIN_WAGE`, `VACATION_AS_WAGES_STATES`, and `SICK_LEAVE_STATES` tables be reviewed by
   counsel once, then treated as a maintained internal reference (updated once a year), or would you rather
   this tool only handle California specially and leave every other state on the existing generic language,
   dropping the other-state vacation/sick-leave notes entirely until they are verified?
3. The Sales Commission Agreement is now generated for every state when "Commissions Paid" is checked, not
   only California. Confirm that is what you want, since some states may not need or want a formal written
   commission agreement (though it never hurts to have one in writing).
4. Confirm the two retired pricing PDFs (`Atlas_One_Employment_Documents_Pricing.pdf`,
   `Atlas_One_Employment_Documents_Overview.pdf`) are fully superseded and nothing else still links to them
   from outside the Master Kit (email templates, GHL forms, etc, which this terminal cannot check since it is
   files and code only, not the GHL browser).
