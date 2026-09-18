# BRIEF for the AUDIT terminal: Run A2 (corrections from the Cowork audit of Run A1)

Terminal name: AUDIT. Same rules as Run A1 (files and code only, no questions, log to
`TERMINAL-AUDIT-live.md`, report to `RUN-AUDIT-report.md` after backing up the A1 report to
`_to_delete/superseded-2026-09-18/prior-reports/RUN-AUDIT-report-RunA1.md`, copy in
`_briefs/assets/run-A2-audit/`, commit and push, hard stops unchanged, no dashes in copy, four colours).
Read first: `_BUILD-LOG/COWORK-AUDIT-run-A1-2026-09-18.md`. Cowork already edited the Workbench (payroll
rates, 2x test, pass band, fix text) and the sample JSON; do not undo those edits, build on them.

## Job 1: the manual rate rule (David's decision 2026-09-18, now in the atlas-pricing skill; read it first)
PEO per EE per check, PEO percent of gross, ASO and HCM rates are typed by David for every prospect. No default,
no stand in, blank or 0 on load, editable at all times including live during a presentation. If the rate is
blank the line shows "needs a rate" and is never guessed or dropped. PEO setup fees and other PEO line items
follow the same rule. Payroll through Atlas One Bookkeeping is the one fixed price: $30 monthly, $15 biweekly or
semi monthly, $7.50 weekly, per EE per check. Cowork already rebuilt Stage 2 of the Workbench this way (rate box
`s2rate`, `needs_rate` flag on `lines.payroll_admin`, Stage 5 prints "needs a rate"); verify it with a pasted
register (blank rate, then a typed rate, then the bookkeeping model) and do NOT add payroll rates to prices.json.
Then apply the same rule to the Quick Quote (`09 Quick Quote Tool/Atlas_One_Quick_Quote.html`: the `peo_flat`
$25, `peo_pct` 0.0095, `aso` $18 and `hcm_only` $12 defaults become blank with a "needs a rate" state that keeps
the line visible and the quote total honest) and to the Quote Cockpit if it carries its own copy of those lines.
Screenshot both before and after. Report exactly which fields changed.

## Job 2: the report's offer section
`build_audit_report.py`: "Your offer, good through <date>" lists what the membership includes, not the impact
lines. Change `audit.offer.lines` to `[{key, label, price_text}]` where key is a prices.json key (for example
`membership.professional`, `gl_import.semi_monthly_biweekly`, `payroll_models.peo`) and price_text is that
entry's price string; the bench's Stage 6 builds this list from checkboxes over the prices.json keys that
match the quoted Total Impact lines (payroll model chosen in Stage 2, WC placement, benefits placement,
bookkeeping if quoted, software resale if present) plus the tier. Update `AUDIT_SCHEMA.md` and the sample
JSON (Professional membership, PEO per EE per check, workers comp placement, health placement through the
carrier partners, software stack consolidation). Page one keeps the impact lines; page two shows tier card,
included services with prices, the 30 day paragraph, the guarantee, the button. Fix sources on page one in
plain words: map tool names to "from your card statements", "from your payroll register", "from your workers
comp declarations page", "from your benefits renewal", "from the health comparison", "from the retention
calculator"; never print a tool or script name on the client report. Rebuild the sample html and pdf into the
DEMO set (overwrite the 2026-09-18 files), rasterize, look, two pages, nothing clipped.

## Job 3: build_tim.py must not overwrite the sample
`build_tim.py` line that writes `SAMPLE_Tell_Me_More_LLC.json` from the embedded SAMPLE string: write only if
the file does not exist, and print a note when it skips. Run it and confirm the sample keeps its `audit` block
and the Total Impact page still shows $13,117.

## Job 4: bench polish
Replace `&mdash;` in the fix cards and anywhere else in the Workbench UI with a middle dot or colon. Grep the
file for `—` and `&mdash;` afterwards (fonts and base64 excluded) and report zero in UI strings.

## Job 5: verify, screenshots, COMMAND
Re-shoot every Workbench stage at 1200 and 390 with the sample loaded, the report pages, and the prep email,
into `_briefs/assets/run-A2-audit/shots/` (replace the stale A1 shots that showed "$0 a month"). Parity file
again (`runA2-parity.txt`). Rebuild COMMAND on the Mac (`catalogue_check.py` then `build_command.py` with the
path) so the stamp is local time, confirm the stamp. Update the atlas-audit skill if any path or rule changed,
re-zip it. Report: built, screenshots, assumptions, skipped, Questions for David at the end (carry forward
the seven from Run A1 that are still open).
