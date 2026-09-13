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
