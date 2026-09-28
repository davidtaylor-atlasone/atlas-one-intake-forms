# David's run sheet: AG3 GoHighLevel load (Run AG3, 2026-09-28)

Written by the AGENT terminal. It cannot write to GHL itself (the Claude Code permission
check blocks it), so you run these five lines yourself in the plain macOS Terminal app, in
this exact order. Each one is copy-paste-able as a single line. Scripts live in this repo:
`/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs/`.

**If a line stops partway through (network blip, you close the terminal, anything):
run the exact same line again.** Every script logs each contact it touches to a CSV as it
goes and skips anything already logged `ok`, so a rerun picks up where it left off -- it
will not create or note anything twice.

## 1. Dedupe the AG2 test notes (fixes the 10 contacts with two identical notes)

```
cd "/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs" && ~/atlas-one-venv/bin/python job_ag2_dedupe_notes.py --apply
```
Takes under 10 seconds (10 contacts, one API call each). Last line looks like:
`Done. Contacts with duplicate import notes: 10. Deleted: 10.`
List-only preview (no changes) if you want to see it first, drop `--apply`.

## 2. AG2 fix pass (fills in companyName on the 10 test contacts, attaches 5G Hearing's contact)

```
cd "/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs" && ~/atlas-one-venv/bin/python job_ag2_load.py all --fix
```
Takes under 15 seconds (10 contacts). Last line looks like:
`row <n> | A Krete Inc | ok-updated | <contact id> | updated; ...`

## 3. AG2 full load (the remaining ~993 Book of Business rows)

```
cd "/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs" && ~/atlas-one-venv/bin/python job_ag2_load.py all
```
Takes roughly 15-20 minutes (about 1,000 contacts at ~4.5 calls/second, each contact is a
search plus a note-check plus a create-or-update plus a note plus tags -- 4-5 calls each).
Last line looks like: `row <n> | <last company alphabetically-ish> | ok-created | <contact id> | created; added`.

## 4. Salesforce test20 (5 Client, 5 touched, 5 intent, 5 with dndEmail)

```
cd "/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs" && ~/atlas-one-venv/bin/python job_ag3_sf_load.py test20
```
Takes under a minute (20 rows). Last line looks like:
`<sfContactId> | <company> | ok-created | <contact id> | created; ...`.

## 5. Cowork checks the test20 results in GHL before you run the rest

Stop here and let Cowork verify the 20 test20 contacts read back correctly in GoHighLevel
(names, companyName, tags, the note on the account's main contact only, and that the 5
dndEmail contacts show DND on the Email channel only, nothing else) before you run the last
line. This is the same "spot check before the big run" step AG2's dryrun10 was for.

## 6. Salesforce full load (the remaining ~7,727 rows)

```
cd "/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs" && ~/atlas-one-venv/bin/python job_ag3_sf_load.py all
```
Takes roughly 1.5-2 hours (about 7,700 rows at ~4.5 calls/second, 3-5 calls per row). You can
close the terminal and come back -- rerunning the same line picks up from the log. Last line
looks like: `<sfContactId> | <company> | ok-created | <contact id> | created; ...`.

## If something looks wrong partway through

Stop that script (Ctrl+C is safe -- nothing in-flight gets half-written, the log only
records a row after its API calls finish) and hand the terminal back to Cowork or this
AGENT terminal with what you saw. Do not delete or hand-edit the CSV logs
(`ag2-load-log-2026-09-27.csv`, `sf-load-log-2026-09-27.csv`) -- they are what makes reruns
safe.
