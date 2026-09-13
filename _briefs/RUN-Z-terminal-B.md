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
