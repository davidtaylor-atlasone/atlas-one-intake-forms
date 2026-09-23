# CLAUDE.md (atlas-one-intake-forms)

Static hosting for Atlas One's branded intake forms and public tools (GitHub Pages at forms.atlasonesolutions.com).
Source of truth for most files is the Master Kit on OneDrive; find it with
`find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null | grep -vi -e _to_delete -e archiv -e "TO DELETE"`
(use the OneDrive copy). `_BUILD-LOG/` below means `<Master_Kit>/_BUILD-LOG/`.

## How every run in this repo works (terminal rules, added Run AC 2026-09-13)

1. **Read the brief from disk.** Briefs live at `_BUILD-LOG/RUN-<X>-terminal-<A|B>.md`. Copy the brief to
   `_briefs/RUN-<X>-terminal-<A|B>.md` in this repo before starting. Terminal A is the only session allowed in the
   GHL browser UI; terminal B is code and files only.
2. **Live log after every step.** Append one dated line to `_BUILD-LOG/TERMINAL-<A|B>-live.md` after every step of
   every job ("done: ...", "next: ..."). Create the file if it is missing. Newest line at the bottom. This is how a
   chat reads the terminal without David pasting anything; if a report is missing, the live log shows where the
   run stopped.
3. **Report at the end.** Write `_BUILD-LOG/RUN-<X>-report.md` when the run finishes: what was built, paths, what was
   looked at (renders), an **Assumptions** section (every judgment call, numbered) and a **Questions for David**
   section at the very end. Copy the report to `_briefs/assets/run-<X>/`.
4. **Never ask questions mid-run.** Make the reasonable call, log it under Assumptions, put the question at the end
   of the report. Answer every permission prompt yourself.
5. **Hard stops (the only things that halt a run):** sending an email or SMS, enabling SMS, enabling GHL's HIPAA
   feature, deleting a file (move it to `OneDrive-AtlasOneSolutions/_to_delete/superseded-<date>/` instead),
   deploying to production, spending money. Never do any of these.
6. **Commit and push after every job.** One commit per job on `main`, message starts with `Run <X>:`.
7. **Verify by rendering and looking.** Headless Chromium (Playwright at
   `/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs`), screenshots into
   `_briefs/assets/run-<X>/shots/`. Every tool must work offline on iPhone, iPad and desktop: `scrollWidth` equals the
   viewport at 390 px, no console errors, no network requests other than `file://`.
8. **Always write reports and logs with a quoted heredoc (`<<'EOF'`) or a file write tool, never an unquoted
   heredoc.** An unquoted heredoc lets the shell expand `$` inside the text, so dollar amounts like `$99` or `$0`
   get silently swallowed or replaced with command output (this happened to RUN-AC-report.md).

## Brand rules (every HTML tool)

- Four colours only: `#23304D` (navy), `#788DE3` (periwinkle), `#FAFAF8` (paper), `#DBE4ED` (mist).
- Horas for headlines, DM Sans for body. Fonts embedded as base64 (`data:font/ttf`, the way
  `tools/self-assessment/index.html` does it; font files in `<Master_Kit>/A1_Final Brand/3. Fonts/`). No CDN, no
  Google Fonts link, no external script.
- No dashes in copy (no em dash, no en dash, no hyphenated phrase where a comma or colon will do; hyphens inside
  compound words such as "co-employment" are fine).
- Status by form, not colour (icons, shapes, labels; colour alone never carries meaning).
- Every tool is a single self-contained HTML file that works from `file://` with no network.

## Atlas One COMMAND (Run AR, 2026-09-14: replaces the Portal, the Tools Hub and the Master Hub)

David used to open three separate launchers and could not tell them apart: `Atlas One PORTAL.html` (44 tools
inlined, internal, carried the rate card), `Atlas One — Tools Hub.html` (32 links, meant for prospects but broke
if the file traveled without its folder) and `Atlas_One_MASTER_HUB.html` (167 rows of sales docs, decks, pricing
and tool links, internal). All three are retired to `_to_delete/superseded-2026-09-14/launchers/`. There are now
two outputs from one builder, in the layout of the client portal app (left navigation with counts, rows not
cards, search at top):

- `<Master_Kit>/Atlas One COMMAND.html`: every internal, prospect and client tool, doc, deck, sheet and PDF.
- `<Master_Kit>/Atlas One Tools (share with prospects).html`: prospect-only, everything inlined, no Internal
  section, no rate card, no margins, no vendor names (grep-guarded at build time).

Rebuild command: `python3 "<Master_Kit>/_INTERNAL (do not share)/build_command.py" "<Master_Kit>"`

The single source of truth for both outputs is `_INTERNAL (do not share)/catalogue.py` (a static Python list,
merged once from the three legacy launchers' catalogues; there is no more upstream to regenerate from, so add or
change a tool by editing catalogue.py directly). Run `catalogue_check.py "<Master_Kit>"` after any edit to
catalogue.py; it fails if a path does not resolve. Never hand edit either generated HTML output. After a
rebuild, confirm the `<title>` stamp and the item count, and back the previous outputs up to `_to_delete/` first.

`build_portal.py` and `build_portal_single.py` are kept in place for their catalogue/inlining logic but no
longer produce anything to open directly; running `build_portal_single.py` now just prints that it is superseded
by `build_command.py` and exits. Never write to `Atlas One PORTAL.html`, `Atlas One — Tools Hub.html` or
`Atlas_One_MASTER_HUB.html` again — those names are retired.

## TOOLS terminal rules (added 2026-09-22, chat "A1 TOOLS fix-it and GL v3")

The TOOLS terminal is David's standing fix-it agent for every tool in the Master Kit, Atlas One COMMAND.html
(the Master Hub / command center presenter) and any calculator, generator or builder under
`<Master_Kit>/06 Calculators and Tools (NEW Aug 2026)/` and similar folders. Not only the GL converter. Every
run follows the same terminal rules as every other terminal in this file (read the brief from disk, live log,
end report, no mid-run questions, hard stops), plus these TOOLS-specific rules:

1. Edit only the Master Kit and `A1_Sales` (sibling of `HR_Docs` under `2. Atlas 1 Solutions Marketing`). Never
   write into a client folder (anything under `2. A1 Official Docs/1. A1 Solutions prospect_Client/`). Reading a
   client folder is fine, and sometimes required, for verification against a real file, when a brief explicitly
   says so; writing, editing or copying into one is not, ever.
2. Never delete a file. Move it to `_to_delete/superseded-<date>/` in the same OneDrive tree instead.
3. Rebuild `<Master_Kit>/Atlas One COMMAND.html` after any tool edit
   (`python3 "<Master_Kit>/_INTERNAL (do not share)/build_command.py" "<Master_Kit>"`) and confirm the stamp and
   item count actually changed before calling a job done.
4. Append one line per fix to `<Master_Kit>/_BUILD-LOG/TOOL-<toolname>-log.md` (create the file if it does not
   exist yet), in addition to the standing `TERMINAL-TOOLS-live.md` and `RUN-TOOLS-report.md` files every run
   already writes.
5. Brief lives at `<Master_Kit>/_BUILD-LOG/BRIEF-TOOLS.md`, live log at
   `<Master_Kit>/_BUILD-LOG/TERMINAL-TOOLS-live.md`, end report at `<Master_Kit>/_BUILD-LOG/RUN-TOOLS-report.md`,
   exactly like every other terminal in this file.
