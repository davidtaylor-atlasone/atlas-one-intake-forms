# BRIEF for the AUDIT terminal: Run A3 (David's decisions of 2026-09-18 evening)

Terminal name: AUDIT. Same rules as Runs A1 and A2 (files and code only, no questions, log to
`TERMINAL-AUDIT-live.md`, back up the A2 report to `_to_delete/superseded-2026-09-18/prior-reports/
RUN-AUDIT-report-RunA2.md`, report to `RUN-AUDIT-report.md`, copy in `_briefs/assets/run-A3-audit/`, commit and
push, hard stops unchanged, no dashes, four colours, verify by rendering). Read
`_BUILD-LOG/COWORK-AUDIT-run-A1-2026-09-18.md` first. Small run, five jobs.

## Job 1: tier rule and two tier offer
Workbench `MEMBERSHIP_TIER_BY_HEADCOUNT`: under 8 employees Essential, 8 to 30 Professional, 31 to 50 Enterprise,
51 and up Concierge (David's rule). Add `offer.also_tier` = the next tier up (Concierge has none). Stage 6 shows
both, "Recommended" and "Also worth a look", both editable. `audit.offer` gains `also_tier`; update
`AUDIT_SCHEMA.md` and the sample (25 employees: Professional recommended, Enterprise also). `build_audit_report.py`
page two: two tier cards side by side (recommended solid navy, the other outlined navy, status by form), each with
monthly and setup from prices.json, the included services table under both. The 2x test uses the recommended tier.

## Job 2: three year line
Report page one, under the first year number: one line "Over three years: $<three_year_net>" from the model's
`three_year` (same 3% growth and fee escalation). Sample prints $41,578 or whatever the model says; assert they match.
Workbench header pin gets the same small line under the first year figure.

## Job 3: pulse to ten questions and the Staff Pulse Score
Stage 4 grid becomes the ten questions in `_BUILD-LOG/pulse-questions-2026-09-18.md` (if the PORTAL run has not
written it yet, take them from `BRIEF-PORTAL-queued-pulse.md`, same text). Paste box accepts the new export shape
(`round, score, weakest, picks`). Compute the Staff Pulse Score (mean of q1, q2, q3, q4, q8) and the two weakest;
write `audit.pulse.score` and `.weakest`. Report "What we found" prints "Staff Pulse Score 3.7 of 5; weakest: benefits
understanding, hours chasing admin" only with five or more responses, otherwise "Staff pulse in progress". Question
labels in plain words on the report, never q numbers.

## Job 4: included services wording (David's answer, the work not the premium)
prices.json `included_services` price strings become: wc_placement "Shopped and placed for you, premium quoted
separately"; benefits_placement "Shopped and placed for you, premiums quoted separately"; bookkeeping_review "Plan
and price confirmed after we see your books"; software_consolidation "Moved onto one bill with one call for support".
Labels: "Workers comp shopped and placed", "Health and benefits shopped and placed", "Bookkeeping review", "Software
stack consolidated". Refresh the Workbench's embedded PRICES copy and the sample offer lines.

## Job 5: verify, COMMAND, skill
Parity again (bench, script, report, first year and three year). Re-shoot Stage 4, Stage 6 and both report pages at
1200 and 390 into `_briefs/assets/run-A3-audit/shots/`. Rebuild the sample report html and pdf in the DEMO set.
Rebuild COMMAND on the Mac (stamp local). Update and re-zip the atlas-audit skill (tier rule, two tier offer, ten
questions, score, 90 day re-pulse noted as GHL Part 6). Report: built, assumptions, skipped, questions at the end.
