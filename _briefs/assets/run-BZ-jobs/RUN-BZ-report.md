# RUN BZ (GHL-JOBS) report, 2026-09-20

The generated index is `_BUILD-LOG/BUILD-INDEX.md`. From now on, add one line to it with:

```
python3 "_BUILD-LOG/index/add_entry.py" "<YYYY-MM-DD>" "<one paragraph, no dashes>" "<Master_Kit path>"
```

Never edit `BUILD-INDEX.md` by hand again; it is generated and any hand edit is lost on the
next rebuild.

## Job 1: split what exists

Wrote a one time `split_index.py` (kept in the session scratchpad, not in the Master Kit,
since it never needs to run again) and used it to split the stale 515 line
`_BUILD-LOG/BUILD-INDEX.md` mirror into:

- `_BUILD-LOG/index/ENTRIES.md` — the dated narrative log. The old file only ever had two
  "Last updated" paragraphs (the current one, and one giant "(prev)" rollup holding every
  earlier update nested inside it), so the split produced two blocks, `## 2026-09-20` and
  `## 2026-09-18`, each the full verbatim body of its paragraph. Nothing inside the nested
  "(prev ...)" history within those two paragraphs was touched or reformatted.
- `_BUILD-LOG/index/REFERENCE.md` — the title, the "Read this first" line, the 2026-09-19
  drift reconciliation note, the platform rule and the strategy/prospecting/mandate/terminals
  notes, then every section from WHERE THINGS LIVE through Rules that keep biting us, in the
  original order and wording. One line was added, an `<!-- ENTRIES -->` marker where the
  assembler splices the narrative log back in; nothing else changed.

Verification: a script did a word level diff between the original file and the two new
files combined. Only five tokens were absent from the combined output: `Last`, `updated:`,
`07:30`, `(prev)`, `00:20`, the five words of the two paragraph prefixes I replaced with
`## <date>` headers. Every other word, including four spot checks (the Master Kit path, the
single carrier rule under 500 lives, `build_portal_single.py`, all four membership prices),
was present. Line counts: original 515, `ENTRIES.md` 34 (mostly the two long paragraphs and
a short instruction header), `REFERENCE.md` 514 (513 original reference lines plus the one
new marker line).

## Job 2: the assembler and the append helper

Wrote `_BUILD-LOG/index/build_index.py` (reads `ENTRIES.md` and `REFERENCE.md`, renders the
newest dated block as the `Last updated:` line and every other block as a `(prev) Last
updated:` line, splices that into `REFERENCE.md` at the `<!-- ENTRIES -->` marker, writes
`BUILD-INDEX.md`) and `_BUILD-LOG/index/add_entry.py` (prepends a new `## <date>` block to
`ENTRIES.md`, refuses an exact duplicate date plus identical text, then calls the
assembler).

Verification: ran the assembler twice back to back after the split; both runs produced a
byte identical `BUILD-INDEX.md` (same md5). Confirmed the same four spot checks were still
present in the regenerated file.

## Job 3: catch the index up to today

**Item 1, the 2026-09-14 to 2026-09-18 gap check.** 2026-09-18 was already covered (it is
one of the two blocks from the split), so it was skipped. Added one entry each for
2026-09-14, 2026-09-15, 2026-09-16 and 2026-09-17, drawn from the primary run reports rather
than the existing narrative, since that narrative is PORTAL and AUDIT centric and undercovers
the EMAIL terminal's four workstreams those days. Logs used: the `RUN-EMAIL-report-*`,
`BRIEF-EMAIL-*-done-*`, and `COWORK-AUDIT-runs-BC-and-BB-2026-09-16.md` files, plus
`skills-system-2026-09-17.md`, `cockpit-vs-quick-quote-2026-09-17.md`,
`command-preview-audit-2026-09-17.md`, `health-tools-audit-2026-09-17.md` and
`w1-nurture-review-2026-09-17.md` for the 09-17 non-EMAIL workstreams. Spot checked two
facts against the source reports and both matched exactly: 1,340 documents fixed in the
09-14 phone sweep, and `SEND_ENABLED` reading false both before and after the 09-16 deploy.
One real defect was caught in this pass: the first draft of the 2026-09-15 entry lost a
dollar figure (a swallowed `$` sign, the same class of bug the project's own heredoc rule
exists to prevent) saying the Bookkeeping Marketing Sheet's Small plan "now starts at  per
month." Traced it to `RUN-EMAIL-report-bookkeeping-marketing-sheet-2026-09-15.md` and
corrected it to **$299 per month**. Scanned the rest of the file for the same double space
pattern and found no other gaps.

**Item 2, the 2026-09-20 audit complete entry.** Added, text taken from the brief (it
already names the source log, `claude/ghl-audit-chunk-complete-2026-09-20.md`) and cross
checked against this session's own git log, which shows the matching commits: Run BX (the
live AND/OR fix on the client services email) and Run BY (the Something else prep email gap
and the after the call gate).

`ENTRIES.md` now has seven blocks: 2026-09-20 (audit complete), 2026-09-20 (the original
portal rollup from the split, correctly kept as its own block since it is a separate real
update the same day), 2026-09-18, 2026-09-17, 2026-09-16, 2026-09-15, 2026-09-14. Rebuilt
after every add; final rebuild is byte identical on a second run. `BUILD-INDEX.md` is now
526 lines.

## Job 4: make the old copy unmistakable

Wrote `_BUILD-LOG/index/README.md` in plain words: `BUILD-INDEX.md` is generated and never
hand edited, `ENTRIES.md` is the only thing that changes every run and only through
`add_entry.py`, `REFERENCE.md` is edited directly like always when something stable actually
changes, and the claude.ai project's copy is now a pointer.

Wired `build_index.py` to also regenerate `_BUILD-LOG/index/PROJECT-COPY-PASTE.md` on every
run: the exact short text David can paste over the claude.ai project's `claude/BUILD-INDEX.md`,
stating the live index is the generated file in the Master Kit, giving its path, the one
`add_entry.py` command, and the last ten entries (currently all seven, since there are not
yet ten). Verified it regenerates byte identically on a second run alongside `BUILD-INDEX.md`.

## Assumptions

1. The two original "Last updated" paragraphs in the stale file each became one `ENTRIES.md`
   block dated by their own timestamp (2026-09-20 and 2026-09-18), keeping their full nested
   "(prev ...)" sub-history as the block's body text rather than trying to decompose that
   nested chain into further per-date blocks. Decomposing it risked garbling or dropping text
   from a single very long, hand-written paragraph; keeping it as one verbatim block satisfies
   "losing nothing" with certainty. A future run can split that body into finer dated blocks
   by hand if David wants that granularity.
2. The Note (2026-09-19 drift reconciliation), the platform rule, and the
   strategy/prospecting/mandate/terminals notes were filed under `REFERENCE.md`, not
   `ENTRIES.md`, since they are standing context that does not change every run (unlike the
   "Last updated" chain), which is what the brief's own contrast between the two files implies.
3. Multiple entries can share a date (2026-09-20 now has two separate blocks). This matches
   reality, several distinct updates landed the same day, and the brief does not say a date
   can only appear once.
4. The `<!-- ENTRIES -->` marker line added to `REFERENCE.md` is a one line, invisible in
   rendered Markdown addition needed for the assembler to know where to splice the narrative
   log back in. It carries no content of its own so it does not count against "losing nothing."
5. For the gap check, a fork agent was dispatched to research and draft the four missing
   day paragraphs. It was told to report the paragraphs back rather than write files, but it
   went ahead and called `add_entry.py` itself. Its output was verified rather than discarded
   (two facts spot checked, the whole file scanned for the swallowed dollar sign pattern that
   check turned up), since the content held up and redoing it from scratch would have cost the
   same verification work twice for no benefit. Noted so future runs know this happened, not
   as a defect to fix.
6. Only `_briefs/BRIEF-GHL-JOBS-2026-09-20.md` was added to the git repo this run; every
   other file this brief describes lives in the Master Kit on OneDrive, which is not the git
   repo, so there was nothing else to commit there. Committed and pushed as Run BZ.

## Questions for David

1. Do you want the two large rolled up "Last updated" bodies (2026-09-20 and 2026-09-18)
   broken apart into their individual nested dates as a follow up job, or is keeping them as
   two single blocks fine going forward? New entries from today onward will already be clean
   one date one block; this only affects the two inherited blocks from the old format.
2. `PROJECT-COPY-PASTE.md` is ready to paste into the claude.ai project's
   `claude/BUILD-INDEX.md`; want that done this run, or do you want to review the generated
   `BUILD-INDEX.md` first?
