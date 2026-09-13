# BRIEF-GHL-JOBS (current run: Run AF, short, two fixes from the Run AE audit)

Rules as always: no questions, answer prompts yourself, live log to `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`, report
`_BUILD-LOG/RUN-GHL-JOBS-report.md` (quoted heredoc), commit and push, never delete (mv to
`OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-13/`).

## Job 1: the Portal was overwritten by the launcher. Restore it and make sure it cannot happen again.
`<Master_Kit>/Atlas One PORTAL.html` is now a 33 KB file titled "Atlas One — All Tools Portal" (stamp "REBUILT
September 13, 2026"). That is the output of `_INTERNAL (do not share)/build_portal.py` (the link launcher). The real
Portal is the single self-contained file from `build_portal_single.py` (17 MB, title "Atlas One Portal: build
<date time>", 43 or 44 tools inlined). The Run AE rebuilds used the wrong script.
1. Run `python3 "<Master_Kit>/_INTERNAL (do not share)/build_portal_single.py" "<Master_Kit>"`. Confirm the file is
   back over 15 MB, the <title> carries today's date and time, the tool count is 44, and open two tools inside it
   offline (fonts DM Sans, zero network requests, zero errors).
2. Make the mistake impossible: change `build_portal.py` so it never writes to `Atlas One PORTAL.html` (if it must
   write a launcher, write `Atlas One PORTAL (launcher, links only).html` instead, or write nothing when imported
   as a catalogue). Add to `repo:CLAUDE.md`: "The Portal is ONLY built by build_portal_single.py with the Master Kit
   path argument. build_portal.py is the catalogue; never run it to produce the Portal." Move the 33 KB launcher to
   `_to_delete/superseded-2026-09-13/portal-launcher-wrong-build/`.
3. Check the Master Hub and Tools Hub still open the Portal by the same file name.

## Job 2: what-we-do page, two vendor names
`repo:tools/what-we-do/index.html` (live at https://forms.atlasonesolutions.com/tools/what-we-do/, looked at, on
brand, both widths clean). Two lines name vendors on a public page: "Connecteam workforce hubs" becomes "Workforce
hub app (scheduling, tasks, chat)"; "Redirect Health" becomes "Alternative funding health plans (whole group)".
QuickBooks stays (it is the client's own software). Re-render, push, confirm 200, regenerate the PDF at
`A1_Sales/Atlas_One_Everything_We_Handle.pdf` (2 pages), Portal rebuilt with build_portal_single.py.

## Report: paths, Portal size and stamp, what was looked at, assumptions, Questions for David.
