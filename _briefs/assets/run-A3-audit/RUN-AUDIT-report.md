# Run A3 report: David's decisions of 2026-09-18 evening

Terminal: AUDIT. Brief: `_BUILD-LOG/BRIEF-AUDIT.md` (Run A3, five jobs). Read first:
`COWORK-AUDIT-run-A1-2026-09-18.md`. Backed up the Run A2 report to
`_to_delete/superseded-2026-09-18/prior-reports/RUN-AUDIT-report-RunA2.md` before writing this one.

## Job 1: tier rule and two tier offer

`MEMBERSHIP_TIER_BY_HEADCOUNT` in the Audit Workbench now follows David's rule: under 8 employees
Essential, 8 to 30 Professional, 31 to 50 Enterprise, 51 and up Concierge. Added `nextTier()` and
`audit.offer.also_tier`, the next tier up (`null` for Concierge, nothing sits above it). Stage 6 gained a
second, independent, editable "Also worth a look" tier selector beside the recommended one, both defaulting
from headcount, each with its own monthly/setup KPI tiles. `AUDIT_SCHEMA.md` documents the rule and the new
field; the sample (25 employees) carries `also_tier: "enterprise"`, matching the brief's own worked example
(Professional recommended, Enterprise also).

`build_audit_report.py` page two now renders two tier cards side by side: the recommended one solid navy,
`also_tier` outlined navy, labelled "Recommended" and "Also worth a look" (status by form, never colour
alone), each with monthly and setup pulled fresh from `prices.json` (a new `tier_monthly_setup()` helper),
with the included services table (`offer.lines`) underneath both. The 2x guarantee test in Stage 5 already
read the recommended tier's fee row and needed no change; confirmed it still does, never `also_tier`.

## Job 2: three year line

`build_audit_report.py` now computes `three_year_net` from `total_impact_model.py`'s own `three_year()`
(same rows and fee the headline number uses, same 3% growth and fee escalation) and prints "Over three
years: $41,578" under the hero net figure on report page one. The Audit Workbench's header pin gained the
same line (`#tiThree`), computed from `timThreeYear()`, the bench's 1:1 port of the model. Verified the
sample prints $41,578 in both the model's own three-year view, the report and the bench, to the dollar
(model: $41,578.33, rounds to $41,578 everywhere it is displayed).

## Job 3: pulse to ten questions and the Staff Pulse Score

Found `_BUILD-LOG/pulse-questions-2026-09-18.md` already written by the PORTAL terminal (Run P5); used it
as the exact spec instead of re-deriving from `BRIEF-PORTAL-queued-pulse.md`, since it is the source of
truth both terminals must match. Stage 4's grid is now the ten questions: q1 to q4 and q8 a 1 to 5 scale,
q5 to q7 a choice (stored as the mean option index, 0 based), q9 pick up to three (a capped multi select),
q10 optional free text. The Staff Pulse Score is the mean of q1, q2, q3, q4 and q8, one decimal, written to
`audit.pulse.score`; the two lowest of that same five are `audit.pulse.weakest`, by key. Both are only
meaningful once `audit.pulse.responses` is 5 or more. The paste box now accepts the portal's export shape,
`{"pulse": {round, sent, responses, score, weakest, averages, picks, free_text}}`, or a bare pulse object.

`build_audit_report.py`'s "What we found" prints "Staff Pulse Score 3.7 of 5, weakest: benefits
understanding, documents" (plain word labels from a `PULSE_LABELS` map, never a q number) only when
responses are 5 or more and a score is present, otherwise "Staff pulse in progress" as before. The sample's
`audit.pulse` was rewritten to the portal's own worked example (7 responses, score 3.7, weakest q3 and q4,
picks, free text) so the report demonstrates the five-or-more state, verified by rendering.

## Job 4: included services wording

`prices.json` `included_services` rewritten to David's wording: wc_placement "Workers comp shopped and
placed, Shopped and placed for you, premium quoted separately"; benefits_placement "Health and benefits
shopped and placed, Shopped and placed for you, premiums quoted separately"; bookkeeping_review
"Bookkeeping review, Plan and price confirmed after we see your books"; software_consolidation "Software
stack consolidated, Moved onto one bill with one call for support." Refreshed the Workbench's embedded
`PRICES` copy and the sample's `offer.lines` for the three included services rows already checked on the
sample (wc placement, benefits placement, software consolidation).

## Job 5: verify, COMMAND, skill

**Parity** (`_BUILD-LOG/runA3-parity.txt`): bench, script and report agree to the dollar on the sample,
first year ($13,117) and three-year ($41,578); the tier rule (25 employees, Professional recommended,
Enterprise also); the 2x test (recommended tier only, $18,400 documented vs $10,566, pass); and the Staff
Pulse Score (3.7 of 5, weakest benefits understanding and documents).

**Rendered and looked at**, headless Chromium, sample loaded: Stage 4 and Stage 6 at 1200px and 390px
(zero console errors, `scrollWidth` equals the viewport at both widths); both report pages at 1200px and
390px (zero console errors, zero horizontal scroll, PDF still renders 2 pages, zero dashes, zero vendor or
PEO brand names). Screenshots in `_briefs/assets/run-A3-audit/shots/` in this repo (`stage4-1200.png`,
`stage4-390.png`, `stage6-1200.png`, `stage6-390.png`, `report-p1-1200.png`, `report-p1-390.png`,
`report-p2-1200.png`, `report-p2-390.png`).

**Sample rebuilt in place** in `12 DEMO Proposal Set/Atlas One — DEMO Proposal Set/`
(`Atlas_One_Back_Office_Audit_Tell_Me_More_LLC__SAMPLE__fictional_2026-09-18.html` and `.pdf`), both
verified by rendering above.

**COMMAND rebuilt on the Mac**: `catalogue_check.py` passed first (199 entries, all paths resolve, no
catalogue change was needed this run since every Job 1 to 4 edit was in place on existing files). Backed up
the prior `Atlas One COMMAND.html` and `Atlas One Sales Kit.html` to
`_to_delete/superseded-2026-09-18/command-outputs/` first. `build_command.py` wrote `Atlas One COMMAND.html`
(199 items) and `Atlas One Sales Kit.html` (57 items, in `A1_Sales/`), both stamped 2:07 PM local (confirmed
against `date`); grepped the Sales Kit for the Audit Workbench and `build_audit_report.py` (both internal
only): zero occurrences.

**atlas-audit skill updated and re-zipped**: the tier rule, the two tier offer and `also_tier`, the ten
questions and the Staff Pulse Score formula and plain word labels, the included services wording, and the
90 day re-pulse noted as queued GHL Part 6 (a workflow, 90 days after the client's start date, that opens a
new pulse round labelled "90 day" the same way the audit round was sent). Re-zipped to
`_BUILD-LOG/skills-for-claude-app/atlas-audit.zip` (one nested `SKILL.md`, clean).

## Assumptions

1. Used `_BUILD-LOG/pulse-questions-2026-09-18.md` (written by the PORTAL terminal, Run P5) as the source
   of truth for the ten questions, the score formula and the export shape, rather than re-deriving them
   from `BRIEF-PORTAL-queued-pulse.md`, since the brief said to match the PORTAL run's file when it exists
   and it already did, with more precise detail (option lists, the export JSON shape, the plain word
   labels) than the queued brief carried.
2. Read "the two weakest" in the brief's Job 3 as the two weakest **of the same five** that make up the
   Staff Pulse Score (q1, q2, q3, q4, q8), per the PORTAL terminal's own design doc language ("the two
   weakest of those five named"), not the two weakest of all ten questions. The brief's own example text
   ("weakest: benefits understanding, hours chasing admin") mixes a scored question (q3) with a non scored
   one (q5) and reads as illustrative copy carried over from an earlier draft, not a literal expected value;
   the rendered sample instead shows "benefits understanding, documents" (q3 and q4), the actual two lowest
   of the scored five for the sample's own numbers.
3. Read Job 1's "the included services table under both" as the existing single `offer.lines` table shown
   once, underneath both tier cards (the included services do not differ by tier, only the membership price
   does), rather than duplicating the table under each card.
4. `also_tier`'s monthly and setup are computed fresh from `prices.json` at render time in both the bench
   and the report, never stored as numbers in the JSON, so they can never drift from a `prices.json` change
   the way a cached number could.
5. Left `prospects/SAMPLE_Tell_Me_More_LLC.json` (a stale, pre audit block copy from `build_tim.py`'s early
   testing, last touched Sep 8) alone; it is not the file any tool in this run reads or writes
   (`build_tim.py`'s sample path is `Total_Impact_Model/SAMPLE_Tell_Me_More_LLC.json`, one level up), so
   updating it would be untracked scope creep.

## Skipped

Nothing in the five jobs was skipped. The 90 day re-pulse GHL workflow itself (Part 6) is explicitly a GHL
terminal item per the brief and the atlas-audit skill; this run only notes it as queued, per instruction.

## Questions for David

1. Job 4's included services wording drops any placement fee framing entirely ("premium quoted separately"
   / "premiums quoted separately"). Confirm that is intentional for both WC and benefits, since the prior
   copy explicitly said "no placement fee" and the new copy is silent on whether a placement fee exists.
2. `also_tier` is always exactly one tier up from the recommendation. If a prospect is a strong fit for a
   tier two steps up (say Essential recommended but Enterprise realistic), Stage 6's "Also worth a look"
   selector is already free text editable so this is possible today, but confirm the report should never
   auto suggest more than one tier up on its own.
3. Confirmed carried forward from Run A1/A2, still open: the xlsx path of the payroll reader has not been
   tested end to end (only CSV), and the six questions in `back-office-audit-run-design-2026-09-18.md`
   section 6 beyond included_services wording (now answered by Job 4) remain unanswered.
4. The 90 day re-pulse workflow (GHL Part 6) needs David's decision on exactly which trigger date starts
   the 90 day clock: the audit report date, the signed agreement date, or the client's Atlas One start date;
   the skill currently just says "90 days after the client's start date" as a placeholder assumption.
