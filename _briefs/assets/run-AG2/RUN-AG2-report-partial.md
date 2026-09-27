# RUN AG2 (Run AG2, 2026-09-27): load master-book-v4 into GoHighLevel -- BLOCKED before any write

Terminal: AGENT. Brief: `_briefs/BRIEF-AGENT-2026-09-27-AG2.md` (title line says APPROVED BY DAVID).

## Status: stopped before any GHL write. Nothing was created, updated, tagged, or noted in GHL.

## What was done (all read-only)

1. Backed up AG1d's `RUN-AGENT-report.md` to `_to_delete/superseded-2026-09-27/run-ag1d-report/`.
2. Read `master-book-v4-2026-09-26.xlsx`: Book tab has 2,375 companies. 1,007 are `Load ready = yes`
   (842 `create`, 161 `update`, plus 4 `skip` that are load-ready but flagged skip for other reasons).
   1,337 are `skip - needs contact`. 35 rows carry Status `Broker or Partner` or `Vendor` (8 of those
   are numbered category folders, not real companies -- 27 are real partner/vendor entities that Job 2
   has to enrich before they can load).
3. Confirmed the Private Integration token (`GHL_PIT` in repo `.env`) and location
   `AzTPxnK2vSUj19jYoDmR` work, read-only:
   - `GET /contacts/search/duplicate` by email found Cirque Lodge's exact recorded GHL Contact ID
     (`0Z9vDJw3SCmz5ODah6X5`) and Ibex Plumbing's by phone (`HrTLbCJRfFEGDnKYdqrS`) -- the Book's
     "GHL match method" column is accurate on both spot checks.
   - The three custom fields the brief names all exist with the exact names given: Employee Count
     (`jhys6ULyKSEL8pxXTdYt`), Current Payroll Provider (`2Wg0Mpj4wO8GaJjZaqdo`), Vertical
     (`gZn8B7wJU1zXDuKYrNoi`, a picklist of 20 options).
   - Found David Taylor's GHL user id (`vTV2wRivyR9f9XWNook3`) for the "assign every created contact
     to David" rule, via `/users/`.
4. Found a live example of the exact defect the brief's rule 7 warns about: 5B USA LLC's Book row has
   its Main contact as Oliver Ramage at `oliver.ramage@peoplepayglobal.com` -- PPG's own domain, not
   a client contact. Built a `PARTNER_DOMAINS` exclusion set (peoplepayglobal.com plus every domain
   found on a Broker/Partner/Vendor row in the Book or in `Atlas_One_Vendor_Partner_Directory.xlsx`)
   and a contact picker that falls back to another linked contact (Contacts tab) or company phone only,
   with a "Referral partner contact: name, email" line added to that company's note, exactly as rule 7
   asks.
5. Wrote `job_ag2_load.py` (copy in this repo at `_briefs/job_ag2_load.py`): for each load-ready row it
   searches GHL by email then phone (rule 2), creates or fills-blanks-only on an existing contact
   (rule 3), adds tags without ever replacing the existing tag list (rule 4), never touches DND
   (rule 5), assigns new contacts to David (rule 6), applies the rule 7 domain fallback, and writes one
   capped (60,000 char) note per company built from the Book row's own fields plus every linked row in
   the Notes tab, newest first (rule 8). It throttles to roughly 4.5 calls/second with exponential
   backoff on 429, and logs every attempt to a resumable CSV
   (`_INTERNAL (do not share)/Book of Business/ag2-load-log-2026-09-27.csv`) so a rerun skips rows
   already logged `ok` (rule 9). It has a `dryrun10` mode that picks AAMCOR, Cirque Lodge, Ibex
   Plumbing and 5G Hearing plus six more create-action rows, exactly as rule 10 asks.

## Where it stopped

Running `job_ag2_load.py dryrun10` -- the mandated first real step -- was denied by the harness's own
auto-mode permission classifier, reason "External System Writes". That is a tool-permission gate
separate from the brief's own "APPROVED BY DAVID" title line, and this terminal cannot approve past it
itself; doing so would be working around a denial rather than getting a real yes. No GHL data was
touched. Nothing else in the run failed -- this is the one thing that needs David directly.

## What David needs to do

Either:
- Approve the specific Bash permission this needs so the terminal can run
  `python3 job_ag2_load.py dryrun10` itself and continue exactly per the brief (dry run 10, read back
  and verify, then the remaining ~997 rows, then Job 2), or
- Run `python3 job_ag2_load.py dryrun10` from `_briefs/job_ag2_load.py` himself in a terminal, then hand
  the run back to this terminal to read back and verify the 10 contacts and continue.

## Assumptions logged so far (for the final report once the load runs)

1. No column in the Book tab maps cleanly to the "Current Payroll Provider" or "Vertical" custom
   fields -- the script leaves both blank rather than guess. Flagged here; David can say if a mapping
   exists (e.g. Services text) before the real run, otherwise these two fields stay unset for every
   record this run touches.
2. Employee Count is the only one of the three named custom fields with a direct source column
   (`Employees`), so it is the only one set automatically.
3. The `PARTNER_DOMAINS` exclusion set for rule 7 is a static list built once from the Book tab plus
   the Vendor Directory spreadsheet, not pulled live from GHL -- if a referral partner's domain is
   missing from that list, its contact would load with the wrong "Main contact" until corrected by
   hand.

## Questions for David

1. Do you want to grant the Bash permission for this script, or would you rather run it yourself and
   hand control back?
2. Is there a source for "Current Payroll Provider" or "Vertical" I'm missing (a Services-text mapping,
   a CSR convention), or should both stay blank for this run?
