# RUN-GHL-JOBS-report.md (Run BP, GHL-JOBS terminal, 2026-09-18)

waiting on GHL Run BP

## Detail

The brief for this run (`_BUILD-LOG/BRIEF-GHL-JOBS.md`) is explicit: run this job only after the GHL
(browser) terminal completes its own Run BP and writes `_BUILD-LOG/audit-form-id.md` with a non empty
`AUDIT_FORM_ID=` value. That file was checked at the start of this run and does not exist yet.

Per the brief's own stop condition ("If it is missing or `AUDIT_FORM_ID=` is empty, stop and write
'waiting on GHL Run BP' as the report"), this run did neither Job 1 (fill the `AUDIT_FORM_ID` constant in
`audit/index.html` and verify) nor Job 2 (add the audit intake catalogue row and rebuild COMMAND).

No files were changed in the Master Kit or the repo other than this report and the terminal live log.
The brief was copied to `_briefs/BRIEF-GHL-JOBS-2026-09-18.md` in the repo as usual.

## Assumptions

1. Treated "GHL Run BP" in the brief as referring to the GHL browser terminal's own run (which builds the
   audit upload form in GoHighLevel and is expected to write `audit-form-id.md`), not this GHL-JOBS
   terminal. No such file exists on disk, so no id was available to check for emptiness either way.

## Skipped

Both jobs in the brief (Job 1: fill `AUDIT_FORM_ID` and verify; Job 2: add the audit intake catalogue row
and rebuild COMMAND) are skipped, per the brief's own stop condition.

## Questions for David

1. Has the GHL terminal's Run BP (building the audit upload form in GoHighLevel) actually run yet? If it
   has and simply has not written `_BUILD-LOG/audit-form-id.md`, say the word and this terminal can pick
   the form id up directly from a Part number in `TERMINAL-GHL-live.md` instead of waiting on the file.
2. If Run BP has not started, no action is needed here until it has: rerun `/run-ghl-jobs` once
   `audit-form-id.md` exists with a real id.
