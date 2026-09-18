# RUN-BJ report (2026-09-18, status check only, no builds)

## Top item: Part 32 was already done, the Run BJ brief was written from a stale reading of RUN-BI-report.md

RUN-BI-report.md is internally contradictory: its opening paragraph says "Parts 32a and 32b ... were completed
... between the incident and the compaction," but the report also carries a leftover "Skipped" section from the
earlier stopped-early draft that lists Part 32a and Part 32b as "not started." Cowork's Run BJ brief (added
2026-09-17 18:45) reads that stale Skipped section and asks for Part 32 again.

The live log (`TERMINAL-GHL-live.md`, entries timestamped 2026-09-17, lines around "Part 32a, Gate 2 done"
through "Part 32b done (no change)") is authoritative here and shows the real state:

- Part 32a: all six gate edits done and verified by fresh-navigation reload: Gate 2, Gate 3, Gate 4 (both
  copies, general and construction), Gate 5 (both copies). Each got cooling 30d, cooling 60d, cooling 90d and
  hold 6m added as OR segments, same pattern as Gate 1. Publish toggle was untouched throughout (workflow was
  already in Draft from the earlier accidental unpublish, and never touched again after that).
- Part 32b: the Task Completed trigger's Add filters control was retried with a fresh navigation and still did
  not open a filter row (same stale-selector issue as Run BH). Per the brief's own contingency, the trigger was
  left unfiltered and this was reported as-is. No further attempt is warranted; this has now failed identically
  across two separate sessions (Run BH and Run BI).

Given that, this session did not redo any of Part 32's edits. Redoing gate edits that are already built and
verified would only risk duplicate OR segments or an accidental re-trigger of the same publish-toggle mistake
that caused the original incident.

## Built this session
Nothing. Read-only status check only.

## Verification
Did a Part 0 fresh navigation (root, Automation, Workflows list) and read the workflow list rows (not the
editor toggle, to stay strictly read-only per this brief's "Read only on the publish switches" line):

- "Post-Presentation Email": still reads **Draft**.
- "Intake: onboarding documents": still reads **Draft**.

Both match exactly what RUN-BI-report.md already flagged as outstanding. The Run BJ brief says "David is
publishing three workflows himself before this run: Post-Presentation Email, Intake: onboarding documents and
Reply task closed." That publishing has not happened yet as of this check. Did not open "Reply task closed" to
check its publish state since Part 32b's own outcome (leave the trigger unfiltered) does not depend on it, and
opening a workflow's editor was unnecessary for a pure status check.

Per the brief's own contingency ("if it reads Draft, stop ... and skip to Part 32b"): Part 32b is already done
(see above), so there was nothing further to do this session.

## Assumptions
1. Trusted the live log over RUN-BI-report.md's contradictory Skipped section, per this repo's own rule that
   the live log is the authoritative record of where a run actually stopped.
2. Did not attempt to re-verify Part 32a's gate contents node by node again in this session (screenshots already
   exist from the prior session's verification pass); re-opening each gate risked repeating the same panel-close
   misclick that caused the original publish-toggle incident, for no new information.
3. Did not touch any Draft/Publish switch, consistent with this brief's explicit "read only" instruction.

## Skipped
Nothing new was skipped; all of Part 32 was already complete before this session started.

## Questions for David
1. **Carried forward, still open:** please publish (or confirm you want to leave in Draft) these three
   workflows: "Post-Presentation Email" (accidentally unpublished by a misclick in a prior session, all gate
   edits are done underneath it), "Intake: onboarding documents" (fully built, blocked from publishing by the
   permission classifier), and "Reply task closed" if you want its tag-clearing behavior live.
2. "Reply task closed"'s Task Completed trigger still cannot take a filter through the UI (Add filters control
   has failed to open a filter row in two separate sessions, Run BH and Run BI, both with fresh navigation).
   Want a support ticket opened with GHL for this, or should it stay unfiltered indefinitely?
3. Please let Cowork know Part 32 is fully done so the brief file's stale "THIS RUN: Part 32" framing does not
   generate a third redundant ask.
