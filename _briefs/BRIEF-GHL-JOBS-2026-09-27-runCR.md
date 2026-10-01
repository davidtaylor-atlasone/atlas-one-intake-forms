# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CR, 2026-09-27). Job 1: safety quiz split and Spanish. Job 2: two card wording fixes. Job 3: rebuild.

Installed by A1 GHL Jobs 3 after its audit of Run CQ (COWORK-AUDIT-run-CQ-2026-09-27.md, PASS). Job 1 was carried unstarted through Runs CN and CO and must be finished in this run. Archive Run CQ's report first.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI and never the
portal repo. No questions mid run. No sends, no spending, no new vendors. Deleting is a move into
`Master_Kit/_to_delete/superseded-<date>/`. No dashes in anything a client or prospect reads. Log a line when each job
STARTS and ends with the real clock time (`date`), never an estimated time. There is NO time limit: this run has
one job, so do all of it; do not stop early to "carry it forward". Finish with `_BUILD-LOG/RUN-GHL-JOBS-report.md`
(archive the previous report first). Keep every Run CL to CO guard on.

## Job 1: Safety Training Program quiz split and Spanish
Folder `04 Safety Library/Safety Training Program/`.
- Add `q_es` and `a_es` to every quiz item in safety-calendar.json (24 months x 5). Plain, crew level Spanish, the same
  register as the existing Espanol talk text on the General Industry pages.
- Regenerate the 24 month pages so each prints three separate pages: (1) the talk (as today), (2) an employee quiz
  with NO answers, English question then Spanish under it, with name, date and score lines, (3) a supervisor answer key
  page. The sign in sheet headings get Spanish under the English (Nombre, Firma, Fecha, Calificacion).
- The 12 month calendar page gets Spanish under each month's topic.
- Update the two Connecteam import kits to carry the Spanish questions.
- Leave `Construction/Toolbox Talks (reused from Safety Library)/` where it is. Cowork found the source: the 28 talks
  exist only as `Atlas One — Complete Kit for BRJ/7. Safety Library (programs & checklists)/Excavation Toolbox Talks
  (28 EN and ES).zip`, so this folder is the only unzipped copy and the month pages may keep linking to it. Rename the
  folder to `Toolbox Talks (from the Safety Library zip)` and fix every link and the json (Cowork decided; not a question for David).
- Print one month to PDF and prove the quiz and the answer key land on separate pages; headless 1440 and 390, zero
  console errors, screenshots.

## Job 2: two business card wording fixes (branch cards-draft only, do not push or merge)
- The helper line under the buttons says "Tap Save my contact" while the button reads "Save <Name>'s contact". Make them match.
- Remove the "Show my screen" button from the prospect facing `card/<slug>/index.html` (it is David's own tool); keep the
  show page itself and its home screen shortcut. Re-run the card tests and screenshots; commit on `cards-draft`.

## Job 3: rebuild COMMAND, the shared Sales Kit and --person charity, rerun every guard, report.
