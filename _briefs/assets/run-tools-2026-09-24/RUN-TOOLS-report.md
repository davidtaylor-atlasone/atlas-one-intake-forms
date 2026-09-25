# RUN-TOOLS report (2026-09-24)

Terminal: TOOLS. Brief: `_BUILD-LOG/BRIEF-TOOLS.md` (copied to `_briefs/BRIEF-TOOLS-2026-09-24.md` in
atlas-one-intake-forms). One job, no stages.

## Job 1: fix the #FDECEC red tint in the invoice tie-out table

File touched: `06 Calculators and Tools (NEW Aug 2026)/Payroll to GL Import Converter (Atlas One).html`

What changed:
- Added a `.tie-fail td:first-child{border-left:6px solid var(--navy)}` rule next to the existing `.fixpill`
  style (same file, CSS block near the `.chk.fail` / `.fixpill` rules).
- In `renderInvoiceTie`, the failing tie-out row now gets `class="tie-fail"` instead of
  `style="background:#FDECEC"`, and its label cell gets a `<span class="fixpill">Fix</span>` (the same pill
  markup stage 6's checks use) ahead of the invoice line label. No background tint anywhere.
- Bumped the version stamp from v3.0 to v3.1 in both places it prints: the header `.stamp` div and the
  `VERSION` variable that feeds the READ ME File ID line in the exported package.

Grep result: `grep -n FDECEC` on the file now returns zero matches. A follow-up grep for any hex color outside
navy/periwinkle/off white/soft blue/white/black/transparent found some pre-existing tints already in the file
before this job (`#EEF2FC`, `#C3CEEA`, `#A8B6EE`, `#F4F6FA`, `#f4f6fd`, `#f7f8fb`, `#fbfcfe`, `#5B6478`,
`#c9d4e0`) — these are lighter washes/shades of navy and periwinkle used for banners, disclaimers and hint
boxes, present in v3.0 and outside the scope of this job (the brief named FDECEC as "the one place in the file
that still breaks that rule"). Logged under Assumptions and flagged to David below in case a broader
brand-color sweep is wanted later.

Verification (headless Chromium, Playwright): loaded the live file, injected the exact stage 5 tie-out table
markup the tool produces for a failing line (reproducing `renderInvoiceTie`'s output rather than driving the
full upload/paste workflow, since forcing a real invoice mismatch through the UI needed a register file and
invoice text neither of which the brief supplied), screenshotted at 1280px (desktop) and 390px (mobile):
- `_briefs/assets/run-tools-2026-09-24/shots/stage5-tieout-desktop.png`
- `_briefs/assets/run-tools-2026-09-24/shots/stage5-tieout-mobile.png`
Both show no red anywhere; the failing row reads clearly via the navy left rule and periwinkle "FIX" pill,
matching stage 6's family. Computed styles confirmed the left border is `rgb(35, 48, 77)` (#23304D navy) at
6px, and the failing row's background is transparent (no tint). Zero console errors on either load.

Rebuilt `Atlas One COMMAND.html` with `build_command.py`. Title stamp changed from "build Sep 23, 2026 4:24 PM"
to "build Sep 24, 2026 7:11 PM"; item count unchanged at 206 (expected, this was an in-place edit to an
existing tool, not an add/remove).

Logged: one line appended to `_BUILD-LOG/TOOL-gl-converter-log.md` and one to
`_BUILD-LOG/TERMINAL-TOOLS-live.md`.

## Assumptions

1. Verified the fix by reproducing the exact HTML the tool's own `renderInvoiceTie` function generates for a
   failing row (synthetic gross/tax figures), rather than driving the full stage 1 to 5 workflow with a real
   payroll register and invoice paste, since the brief did not supply sample data and the fix is a pure
   CSS/markup change with no logic touched. This verifies the same markup real usage would produce.
2. Read the pre-existing lighter tints (`#EEF2FC`, `#C3CEEA`, etc.) as out of scope: the brief called FDECEC
   "the one place in the file that still breaks that rule," so these were treated as already-accepted design
   choices from v3.0, not new violations introduced by this job. Not changed.
3. Left rule color set to navy per the brief's explicit instruction ("a thick left rule in navy"), with the
   FIX pill kept in its existing periwinkle-on-navy styling reused verbatim from stage 6, rather than trying to
   match stage 6's full solid-navy-bar treatment, since a table row inside a bordered grid reads better with a
   rule-plus-label than a solid fill that would collide with adjacent rows' borders.

## Questions for David

1. The grep in Job 1 turned up several pre-existing tint colors elsewhere in the same file (`#EEF2FC`,
   `#C3CEEA`, `#A8B6EE`, `#F4F6FA`, `#f4f6fd`, `#f7f8fb`, `#fbfcfe`, `#5B6478`, `#c9d4e0`), used for banners,
   disclaimers and hint boxes. They predate this job and were not part of the brief. Want a follow-up job to
   sweep those to the four brand colors too, or are they intentional tints/shades that are fine to keep?
