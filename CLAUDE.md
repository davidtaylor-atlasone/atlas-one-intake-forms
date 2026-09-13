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

## Portal

The Portal (`<Master_Kit>/Atlas One PORTAL.html`) is generated: `python3 "<Master_Kit>/_INTERNAL (do not share)/build_portal_single.py" "<Master_Kit>"`
(the catalogue lives in `_INTERNAL (do not share)/build_portal.py`). Never hand edit the Portal. After a rebuild,
confirm the `<title>` stamp and the tool count, and back the previous Portal up to `_to_delete/` first.
