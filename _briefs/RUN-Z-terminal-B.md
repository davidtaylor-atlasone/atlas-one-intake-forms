# RUN Z (terminal B, files only, no GHL UI): David's decisions on the Run W and Run Y questions

Given by David 2026-09-12, run unattended, no questions. Master Kit found with
`find ~ -type d -name "Atlas_One_Master_Kit" | grep -vi -e _to_delete -e archiv`.

Decisions to do:
1. Write "2025 to 2026" in full wherever Run W left "2025 to 26".
2. Retire the duplicate `06 Calculators and Tools (NEW Aug 2026)/Atlas One — Your Savings Summary.html` to
   `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-12/` and repoint any Hub, Tools Hub or build_portal.py entry
   that used it to `Atlas One Savings Summary (Atlas One).html`.
3. Portal title in `_INTERNAL/build_portal_single.py`: "Atlas One Portal — build ..." becomes "Atlas One Portal: build ...".
4. Leave "guaranteed rates" in the benefits presenter as is.
5. Give the kit copy of `Atlas_One_Time_Savings_Discovery.html` the same stacked mobile table Run Y gave the hosted copy,
   but keep the kit's meeting voice.
6. Give repo `tools/index.html` the same navy header bar the hosted tools use, push, confirm 200.
7. Mobile pass on the six tools that still scroll sideways at 390 px (Onboarding Tracker, Employee Benefits Options,
   Handbook Builder, NDA Builder, Safety Manual Builder, W-2 Agreement Builder): additive media query only, scrollWidth
   must equal 390 at 390 px, outputs and generated documents byte identical before and after on one sample each,
   back-ups to `_to_delete` first.
Then rebuild the Portal with the path argument, confirm the stamp, write `<Master_Kit>/_BUILD-LOG/RUN-Z-report.md`,
commit and push. Never send, never deploy beyond the normal Pages push, never delete.

---

## Progress log (terminal B)

- 2026-09-12: brief written to the repo. Starting item 1.
- Item 1 done: "2025 to 26" is now "2025 to 2026" in Business Value Diagnostic (EN, ES), Retention Cost Calculator (EN, ES) and repo tools/retention-cost/index.html (6 occurrences); the repo retention copy stays byte identical to the kit copy.
- Item 2 done: `Atlas One — Your Savings Summary.html` (byte identical to the "(Atlas One)" file) moved to OneDrive `_to_delete/superseded-2026-09-12/`. Nothing pointed at it: the Master Hub, the Tools Hub and build_portal.py already reference `Atlas One Savings Summary (Atlas One).html`; no repoint needed.
- Item 3 done: build_portal_single.py line 93 title is "Atlas One Portal: build {{STAMP}}".
- Item 4: nothing to do ("guaranteed rates" left as is).
- Item 5 done: kit Time Savings file got the hosted copy's mobile block as `<style id="a1mobile-2026-09-12">` (identical CSS); no copy changed (meeting voice kept); scrollWidth 390 at 390 px; Run Y sample (rate 40, 2 hrs, $120) byte identical before/after. Backup in `_to_delete/superseded-2026-09-12/tools-before-mobile-pass-run-Z/`.
- Item 6 done: repo tools/index.html has the hosted tools' navy `.hbar` (white logo, eyebrow "Free business tools"), bar moved outside `.wrap` so it spans the page; pushed (217948e); live `/tools/` returns 200 and is byte identical to the pushed file.
- Item 7 done: additive `<style id="a1mobile-2026-09-12">` block in each of the six (backups first, same folder as item 5). scrollWidth 390 at 390 px on all six (was 522, 413, 855, 470, 833, 439), zero elements wider than the viewport. Sample (Run W fill pattern, fixed clock) at 390 and 1440: field values, generated document innerHTML, body text and getState() byte identical before and after on all twelve captures. 1440 px renders pixel identical (NDA differs only at the pulsing live-preview dot). Scripts: `_briefs/assets/run-Z/{mobilepass.py,sample.mjs,compare.py,culprits.mjs,shots.mjs,crops.mjs}`.
