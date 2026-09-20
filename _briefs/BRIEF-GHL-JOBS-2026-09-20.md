# BRIEF-GHL-JOBS (current run: Run CA, 2026-09-20 08:45). Three corrections to Run BZ. Small run.

Terminal name: GHL-JOBS. Files and code only, never the GoHighLevel browser UI. No questions, log assumptions,
questions at the END. Never fork or background (rule 44). Commit and push. Assets `_briefs/assets/run-CA-jobs/`.
No dashes. Log to `TERMINAL-GHL-JOBS-live.md`; report to `RUN-GHL-JOBS-report.md` plus a copy in the assets
folder. Prior report already backed up. Delete nothing: superseded files move to
`OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-20/`.

Run BZ did the hard part correctly, the split and the scripts. It read an earlier version of its brief that
was revised while it was running, so three things need correcting. Nothing here is a rebuild.

## Correction 1: the entries are out of date order, so the index is claiming the wrong "last updated"
`_BUILD-LOG/index/ENTRIES.md` currently reads 09-17, 09-16, 09-15, 09-14, 09-20, 09-20, 09-18. The assembled
`BUILD-INDEX.md` therefore says "Last updated: 2026-09-17", which is wrong and is exactly the kind of quiet
drift this whole job existed to stop.
Fix it in the assembler, not by hand: `build_index.py` must sort entries by date, newest first, before it
writes anything, and where two entries share a date it keeps the order they appear in the file. Then make
`add_entry.py` insert in date order too rather than always prepending, so a back dated entry can never land in
the wrong place again. Rebuild and confirm the top of BUILD-INDEX.md now reads 2026-09-20.

## Correction 2: a missing day
There is one 09-18 entry and no 09-19 entry, though both days have run reports (portal runs P6 to P8, the
Pax8 and Microsoft partner work, GHL Runs BQ to BX). Read `_BUILD-LOG/` and the repo `_briefs/` history for
those two days and add what is missing, one paragraph per day, naming the log file, nothing invented. If a day
is genuinely already covered, say so instead of writing a second entry for it.

## Correction 3: the project copy is a pointer, and it must not be
David reads everything from his phone. The claude.ai project copy has to carry the FULL index, not a note
saying where the real one lives. Cowork uploads the file directly so nobody retypes it.
Retire `_BUILD-LOG/index/PROJECT-COPY-PASTE.md` to the `_to_delete` folder named above. In its place, have
`build_index.py` also write `_BUILD-LOG/index/BUILD-INDEX-for-project.md`, byte for byte identical to the
assembled `BUILD-INDEX.md`, every time it runs. Update `index/README.md` to match: the project copy is the
whole index, Cowork uploads it as a file after each entry is added, and nobody pastes anything.

## Verify
Run the assembler twice, confirm the second run changes nothing. Confirm the two generated files are byte for
byte identical (`cmp` them). Confirm the assembled index still contains the Master Kit path, "one carrier"
under 500 lives, `build_portal_single.py` and the four membership prices. Print the date order of every entry
heading as proof of Correction 1.

## Report
First line: the top entry date in the rebuilt index, and the full path of `BUILD-INDEX-for-project.md` with
its character count, which is what Cowork picks up. Then per correction: what changed, the proof, assumptions,
"Questions for David" at the end.
