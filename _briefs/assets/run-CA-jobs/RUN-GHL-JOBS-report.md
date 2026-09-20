# RUN-GHL-JOBS report: Run CA, 2026-09-20

Top entry date in the rebuilt index: **2026-09-20**.
Full path of the project copy: `/Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit/_BUILD-LOG/index/BUILD-INDEX-for-project.md`, **111,216 characters**, confirmed byte for byte identical to `_BUILD-LOG/BUILD-INDEX.md` with `cmp`.

Small run, three corrections to Run BZ (it read an earlier version of its brief that was revised mid run). Nothing here is a rebuild of BUILD-INDEX.md's content, only the assembler and the entries.

## Correction 1: date order

`ENTRIES.md` had the entries in the order 09-17, 09-16, 09-15, 09-14, 09-20, 09-20, 09-18 (the order Run BZ happened to write them), so the assembled `BUILD-INDEX.md` read "Last updated: 2026-09-17" even though 09-20 entries existed further down the file.

What changed:
- `index/build_index.py`: `parse_entries()` now sorts the parsed entries by date, newest first, with a stable sort so two entries sharing a date keep the order they appear in the file. This runs every time the assembler runs, so the "Last updated" line can never again read a stale date no matter what order `ENTRIES.md` happens to be in.
- `index/add_entry.py`: no longer always prepends. It now scans for the first existing entry whose date is older than the one being added and inserts before it, so a back dated entry lands in its correct place in `ENTRIES.md` rather than jumping to the top. Same date entries still append after the existing ones with that date, so they read in the order they were added.
- `ENTRIES.md` itself was rewritten in sorted order (09-20, 09-20, 09-19, 09-18, 09-17, 09-16, 09-15, 09-14) so the file matches what the header says it is ("newest first") going forward, not just what the assembler produces.

Proof, date order of every entry heading, printed after the fix:
```
## 2026-09-20
## 2026-09-20
## 2026-09-19
## 2026-09-18
## 2026-09-17
## 2026-09-16
## 2026-09-15
## 2026-09-14
```
`BUILD-INDEX.md` line 6 now reads: `Last updated: 2026-09-20 (BACK OFFICE AUDIT GHL SIDE COMPLETE AND PROVEN LIVE...)`.

## Correction 2: the missing day

Read `_BUILD-LOG/` file timestamps and the repo's commit history (`~/Projects/atlas-one-intake-forms`) for 09-18 and 09-19.

- **09-18 is already covered.** The existing `## 2026-09-18` entry (software store published, portal Runs P5 and P6, the day's recap chain) already carries that day's work. No second entry written for it, per the brief's instruction to say so instead of duplicating.
- **09-19 had no entry at all**, though the day has real run reports: `COWORK-AUDIT-run-A4-2026-09-19.md`, `build-queue-decisions-2026-09-19.md`, `COWORK-AUDIT-run-P7-2026-09-19.md`, `COWORK-AUDIT-run-P8-2026-09-19.md`, and repo commits `0888a36` through `5919aec` (Runs BV, BW, BX, BY on the GHL terminal, Run A4 on the AUDIT terminal). Added one paragraph, via `add_entry.py`, naming those files and commits: AUDIT Run A4 closing the Workbench's seven remaining jobs and its Cowork audit; PORTAL Runs P7 and P8 audited PASS and deployed; and the GHL terminal's AND/OR bug in Booking: client services email found, fixed and proven live, plus the Something else prep email gap and Booking after the call gate closes. Nothing in the paragraph was invented; every claim traces to one of those four files or a named commit range.

## Correction 3: the project copy must carry the whole index

`PROJECT-COPY-PASTE.md` told David to paste a short pointer over the claude.ai project's `BUILD-INDEX.md`. David reads from his phone, so a pointer he cannot follow is worse than the problem the split was meant to fix.

What changed:
- `index/build_index.py` now writes `index/BUILD-INDEX-for-project.md`, the exact same assembled text as `_BUILD-LOG/BUILD-INDEX.md`, every time it runs (same variable, same write, no separate pointer text or "last ten entries" summary).
- `PROJECT-COPY-PASTE.md` retired to `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-20/PROJECT-COPY-PASTE.md` (moved, not deleted).
- `index/README.md` updated: the project copy section now describes `BUILD-INDEX-for-project.md` as the whole index, uploaded as a file by Cowork after each entry, nobody pastes anything.

Proof: `cmp _BUILD-LOG/BUILD-INDEX.md _BUILD-LOG/index/BUILD-INDEX-for-project.md` returns no difference (both 111,216 characters, 529 lines).

## Verify

- Ran `python3 build_index.py "<Master_Kit>"` twice in a row: second run's `BUILD-INDEX.md` is byte for byte identical to the first (`cmp` clean).
- `BUILD-INDEX.md` and `BUILD-INDEX-for-project.md` are byte for byte identical (`cmp` clean).
- Assembled index still contains the Master Kit path (35 hits), the single carrier rule under 500 lives (`**enforces the single-carrier rule under 500 lives**`), `build_portal_single.py` (2 hits, unchanged since it lives in `REFERENCE.md` which this run did not touch), and the four membership prices (`$99 / $399 / $999 / $1,900`).
- Entry heading order printed above, newest first, ties in file order preserved.

## Assumptions

1. "The two generated files" in the brief's Verify section means `BUILD-INDEX.md` and `BUILD-INDEX-for-project.md`; there is no third generated file.
2. For Correction 2, "GHL Runs BQ to BX" in the brief's framing is the day span's overall run range, not a claim that every run in that range falls on 09-19; git history shows BQ through BU landed 09-18 (already inside the existing 09-18 entry's "prev" trail) and BV through BY landed 09-19, so the new 09-19 paragraph covers BV to BY plus Run A4 and Portal P7/P8, the things that genuinely had no dated entry yet.
3. Rewrote `ENTRIES.md`'s existing entries into sorted order in this run (not just relying on the assembler to sort at read time), since the brief's own wording is "the entries are out of date order" about the file, and leaving the raw file scrambled while only the assembled output looks right would let the same drift happen again the next time someone reads `ENTRIES.md` directly.
4. Moved `PROJECT-COPY-PASTE.md` to `_to_delete/superseded-2026-09-20/` rather than deleting it outright, per the standing rule against deleting files.
5. Did not touch `REFERENCE.md`; none of the three corrections call for a change to it, and the brief's Verify section treats its content (Master Kit path, carrier rule, `build_portal_single.py`, membership prices) as things that must still be present, not things to edit.

## Questions for David

1. None. All three corrections were mechanical fixes to files this terminal already owned; no judgment call needed David's input.
