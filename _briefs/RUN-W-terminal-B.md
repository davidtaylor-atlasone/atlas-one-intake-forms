# RUN W (terminal B, files only, no GHL UI): no-dash copy pass across the tools

Written by Cowork 2026-09-12. Same rules as Runs S to V: no questions, log assumptions, batch questions at the end of
`<Master_Kit>/_BUILD-LOG/RUN-W-report.md`, never delete (mv to `_to_delete/superseded-2026-09-12/`), never send, never
deploy, verify by rendering and looking. Do not touch pricing numbers, agreements, division sheets, decks or
BUILD-INDEX.md. Copy this file to `_briefs/RUN-W-terminal-B.md`, commit after each job.

## Job 1: inventory
In `<Master_Kit>/06 Calculators and Tools (NEW Aug 2026)/` and the repo `tools/` folder, count em dashes (U+2014),
en dashes (U+2013) and spaced hyphens (" - ") that appear in VISIBLE copy (text nodes, placeholder, title, alt, aria
labels, and string literals that are rendered into the page) for every HTML file. Ignore CSS, JavaScript operators,
data attributes, base64 blobs, and hyphens inside compound words (W-2, co-employment, E-Verify, bi-weekly, 1099-NEC).
Write the table (file, count before) into the report before changing anything. Back up every file you will change
to `_to_delete/superseded-2026-09-12/tools-before-dash-pass/`.

## Job 2: the pass
Rewrite each dash in visible copy with a comma, period, colon, parentheses or a rephrase; never just delete it, never
change a number, a label's meaning, a merge field, a URL, a class name or any JavaScript logic. Where a dash separates
a label from a value in a rendered string (for example `"Total — " + x`), use a colon. Spanish files follow the same
rule. While in each file, flag (do not change) any claim that sounds like a guarantee or a superlative ("Fortune 500",
"guaranteed", "always", "A-rated") in a list for David; the only allowed guarantee wording is the Audit Guarantee.
After each file: open it in headless Chromium, confirm no JavaScript errors, run the tool's own sample calculation
before and after and compare the output strings (they must be byte identical apart from the dash edits), render at
390 px and 1440 px and look.

## Job 3: publish
Copy changed files that also live in the repo `tools/` into the repo, push, curl each live URL for 200. Rebuild the
Portal with the path argument, confirm the stamp. Report: the before and after counts per file, the claims list,
assumptions, anything skipped, questions.

## Progress log (terminal B)

- 2026-09-12 20:25: brief copied (Run W had not started: no repo copy of the brief, no log, no report). Starting Job 1 inventory.
- Job 1 done (inventory): scanner `_briefs/assets/run-W/inventory.py` classifies every em dash, en dash, entity (&mdash; &ndash; — –) and spaced hyphen by context (text node, visible attribute incl. data-en/data-es/placeholder/title/aria-label, JS string literal incl. template chunks; CSS, JS code, comments and non-visible attributes ignored). Before: 1,790 em + 253 en + 34 spaced hyphens visible across 43 kit files and 3 repo tools (table in the report; `inventory-before.json`). 46 files backed up to `_to_delete/superseded-2026-09-12/tools-before-dash-pass/` (repo copies under `repo-tools/`).
- Job 2 done (the pass): rule-based rewriter `dashpass.py` (+ `overrides.json`), every proposed rewrite reviewed in `dash-review-proposed.md` before applying. Rules: numeric/date ranges to "to"; label/value and short-lead dashes to a colon; mid-sentence dashes to a comma; paired dashes to commas, or parentheses when the aside has its own commas; wrapped option labels "— none —" to "(none)"; hint spans to parentheses; empty-value placeholders "—" / "$—" to "…" / "$…"; QuickBooks memo separators " - " to ": ". After: 0 / 0 / 0 visible. Two JS-logic exceptions logged: `shortGroup()` regex in the Handbook and Safety Manual builders now also accepts a colon so the toggle list still strips "Section N:" (one character); Cost of a Compliance Mistake total range separator span set to "to" by hand. Per file: headless Chromium load has zero JS errors on all 46 (before and after); one deterministic sample run per tool (every input filled, calculate buttons fired, Business Tools walked through all 28 generators) gives identical number sequences and identical words apart from the dash rewrites on every file (`sample-before/after-*.json`, `compare.py`); the only residual is the Handbook toggle list, where a literal "&mdash;" that used to render as raw text now reads "Protected Rights: Savings Clause". Rendered at 390 and 1440 (`contact-390.png`, `contact-1440.png`, `render-log.json`) and looked: no layout change; the six 390 px overflows (Onboarding Tracker 522, Benefits Options 413, Handbook 855, NDA 470, Safety Manual 833, W-2 Agreement 439) are identical on the before copies, so pre-existing. Claims list in `claims.txt` (for the report).
