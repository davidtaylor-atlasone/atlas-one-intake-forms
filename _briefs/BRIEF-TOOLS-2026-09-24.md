# BRIEF-TOOLS: fix the one remaining brand violation on the GL converter (written 2026-09-24 by Cowork, chat "A1 TOOLS gl-converter")

Second run of the standing TOOLS terminal. One small job, no stages, no stopping for questions. Batch
anything unexpected into the Questions for David section at the end of RUN-TOOLS-report.md.

Find the Master Kit: `find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null | grep -vi -e _to_delete -e archiv
-e "TO DELETE"` (use the OneDrive one, under `2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/`).
Call it `<Master_Kit>`.

## Job 1: fix the #FDECEC red tint in the invoice tie-out table

File: `<Master_Kit>/06 Calculators and Tools (NEW Aug 2026)/Payroll to GL Import Converter (Atlas One).html`
(currently v3.0, shipped 2026-09-22).

In stage 5 (Invoice tie-out), a line that fails to tie is shaded with `background:#FDECEC`, a pale red. Atlas
One's brand rule is four colors only (navy #23304D, periwinkle #788DE3, off white #FAFAF8, soft blue #DBE4ED),
no red, no fifth color, status differentiated by FORM (solid fill, pill, left rule), never by introducing a
color. This is the one place in the file that still breaks that rule; every other failing-state treatment in
the tool (stage 6's checks) already does it correctly with a solid navy bar, off white text, a bold FIX pill,
and a thick left rule.

Change the failing row's treatment in stage 5 to the same family: no red background, a thick left rule in navy
and a small bold label (reuse the FIX pill styling, sized to fit inside a table row) instead of the tint. Match
stage 6's pattern as closely as the table layout allows; use your judgment on the exact sizing so it still reads
clearly at a table row's height, both desktop and 390px.

Grep the whole file afterward for `FDECEC` and for any other hex color outside the four brand colors and
white/black/transparent, to confirm nothing else slipped in. Zero matches expected.

Bump the version stamp to v3.1, real build date, everywhere it prints (the header and the READ ME File ID).
Rebuild `<Master_Kit>/Atlas One COMMAND.html` with
`python3 "<Master_Kit>/_INTERNAL (do not share)/build_command.py" "<Master_Kit>"` and confirm the stamp changed.

Verify in headless Chromium: load the tool, get to stage 5 with at least one failing tie-out line (any register
that doesn't balance to the pasted invoice text works, or edit a value to force a mismatch), screenshot it at
desktop and 390px widths, confirm no red is visible anywhere and the failing row is still unmistakable. Zero
console errors.

Append one line to `<Master_Kit>/_BUILD-LOG/TOOL-gl-converter-log.md`: date, "v3.1: fixed the FDECEC red tint
on the invoice tie-out table to a form-only treatment (brand compliance)."

That's the whole job. No new gl-converter write-up needed, the log line and the report are enough; Cowork will
fold this into the project record.

## Verification and reporting
Append one dated line to `<Master_Kit>/_BUILD-LOG/TERMINAL-TOOLS-live.md` when done. Write
`<Master_Kit>/_BUILD-LOG/RUN-TOOLS-report.md`: what changed, the path touched, the grep result confirming no
red remains, the screenshots taken, an Assumptions section, and a Questions for David section at the very end
(likely empty, this job is small).

## Hard stops
Sending an email, enabling SMS, enabling GHL's HIPAA feature, deleting a file (move to
`_to_delete/superseded-<date>/` instead), deploying to production, spending money. None of these should come
up in this job.
