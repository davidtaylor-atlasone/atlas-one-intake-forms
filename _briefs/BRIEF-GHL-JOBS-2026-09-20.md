# BRIEF-GHL-JOBS (current run: Run BZ, 2026-09-20). Make BUILD-INDEX a file that can be appended to, instead of a 40KB map that has to be retyped whole to add one line.

Terminal name: GHL-JOBS. Files and code only, never the GoHighLevel browser UI. Build end to end, no questions,
log assumptions, questions at the END. Never fork or background (rule 44). Commit and push after each job.
Assets `_briefs/assets/run-BZ-jobs/`. No dashes in any copy. Log to `TERMINAL-GHL-JOBS-live.md`; report to
`Master_Kit/_BUILD-LOG/RUN-GHL-JOBS-report.md` plus a copy in the assets folder. Prior report already backed
up. Delete nothing: superseded files move to `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-20/`.

## The problem
`claude/BUILD-INDEX.md` lives only in the claude.ai project. There is no way to patch it, so adding one line
means an assistant retyping the whole 40KB map from memory, which risks silently losing part of the one
document that stops us rebuilding things that already exist. It has drifted for exactly this reason: the
OneDrive mirror `_BUILD-LOG/BUILD-INDEX.md` has been stale since 2026-09-14.

## The shape to build
One append only entries file, plus the stable reference sections, plus a tiny script that assembles the whole
index. Nobody ever edits the assembled file by hand again.

## Job 1: split what exists
Read `_BUILD-LOG/BUILD-INDEX.md` (the stale mirror) and split it, losing nothing, into:
- `_BUILD-LOG/index/ENTRIES.md`: the dated "Last updated" narrative entries, newest first, one entry per
  block, each starting `## <YYYY-MM-DD>` followed by its text. These are the things that change every run.
- `_BUILD-LOG/index/REFERENCE.md`: everything that is not a dated entry, in its existing order and wording:
  where the files live, the sales tools table, the six divisions, the four payroll models, launchers, document
  builders, payroll and accounting tools, benefits strategy, health carrier facts, pricing sources of truth,
  brand and project setup, free tools, domains, back office, the OPEN table, NOT BUILT YET, and the rules that
  keep biting us.
Change no wording. This is a split, not a rewrite. Report the line count of the original and of the two parts
so it is obvious nothing was dropped.

## Job 2: the assembler and the append helper
`_BUILD-LOG/index/build_index.py`: reads ENTRIES.md and REFERENCE.md and writes
`_BUILD-LOG/BUILD-INDEX.md` as header, then the newest entry as the "Last updated" line, then the remaining
entries, then the reference sections. It must be rerunnable and produce identical output when nothing changed.
`_BUILD-LOG/index/add_entry.py "<YYYY-MM-DD>" "<one paragraph>"`: prepends a new entry block to ENTRIES.md,
refuses a duplicate date plus identical text, then runs the assembler. That is the whole future workflow: one
command, one line, no retyping.
Verify: run the assembler twice, confirm the second run changes nothing (diff is empty), and confirm the
assembled file still contains a handful of spot checked strings from deep inside the reference sections
(the Master Kit path, "one carrier" under 500 lives, `build_portal_single.py`, the four membership prices).

## Job 3: catch the index up to today
Add these entries with `add_entry.py`, newest last so they land in the right order, each as one paragraph, no
dashes. Take the detail from the named logs, do not invent any:
1. 2026-09-14 to 2026-09-18 gap check: read `_BUILD-LOG/` and the repo `_briefs/` history and add one entry
   per day that has a run report but no entry in ENTRIES.md, summarising what shipped that day in one
   paragraph, naming the log file. If a day is already covered, skip it and say so.
2. 2026-09-20: BACK OFFICE AUDIT GHL SIDE COMPLETE AND PROVEN LIVE (Runs BQ to BY): booking question routes
   clients away from the prep email, client services email fires on the tag alone (AND to OR fix), Something
   else bookings get nothing audit specific, Form E uploads land tags and tasks, after the call follow up
   published and gated on audit-offer-sent, offer expiry now comes from the Audit report by API since GHL has
   no date math. Log: `claude/ghl-audit-chunk-complete-2026-09-20.md`.

## Job 4: make the old copy unmistakable
Write `_BUILD-LOG/index/README.md` in plain words: BUILD-INDEX.md is generated, never edit it by hand, add an
entry with `add_entry.py`, and the claude.ai project copy is now a pointer. Also write
`_BUILD-LOG/index/PROJECT-COPY-PASTE.md` containing the exact short text David can paste over the project's
`claude/BUILD-INDEX.md` so that copy says: the live index is the generated file in the Master Kit, here is its
path, and here are the last ten entries. Regenerate that file whenever the assembler runs.

## Report
First line: the path of the generated index and the one command to add an entry from now on. Then per job:
what was done, the line counts proving nothing was lost, the spot checks, assumptions, "Questions for David"
at the end.
