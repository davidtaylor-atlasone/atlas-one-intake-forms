## Progress log

- **2026-09-12 (later session), stopped before any edits ("needs Chrome restart").** User confirmed GHL was
  already logged in and responsive. Direct nav to `/workflows` still hit the same "click here to refresh" then
  blank-page Firebase-permissions failure as the prior attempt. Navigating to the app root instead worked and
  landed on a fully interactive Dashboard; clicking into Automation loaded the Workflows list shell and table with
  real data. But the workflows table (cross-origin iframe) did not respond to any click — tried the "Call: not
  now" row at three offsets, the "Needs review" tab, and "Create workflow", all with zero effect. Did the one
  allowed Cmd+R on that page and retried; still dead. Per the dead UI rule, stopped the whole batch before Part 1,
  Part 2, or Run R. Re-verified outside the browser that the Part 2 item 4 URL still 404s and `GHL_BUILD_FORM` is
  still unset. Full detail, including a narrower diagnosis than the account-wide Firebase failures seen before,
  in `<Master_Kit>/_BUILD-LOG/RUN-X-report.md` ("needs Chrome restart" at top).
- **2026-09-12, stopped before any edits ("needs Chrome restart").** Copied this brief in, then ran the standing
  dead-UI click test on the Workflows list before starting Part 1: the app stuck on GHL's own loading spinner past
  20s, then the "click here to refresh" screen (never clicked). Did the one allowed Cmd+R; the page went fully
  blank afterward with console showing `FirebaseError: Missing or insufficient permissions` from GHL's app bundle —
  same signature as the account-wide auth/session failure from the RUN-P "session start" incident, not the
  narrower Sites-only failure from the most recent RUN-R-report.md. Per the dead UI rule, stopped the whole batch
  before Part 1, Part 2, or Run R. Confirmed outside the browser that the Part 2 item 4 URL
  (`https://forms.atlasonesolutions.com/tools/time-savings/`) still 404s, and that `build/index.html`'s
  `GHL_BUILD_FORM` is still unset, ready for Run R. Full detail and next steps in
  `<Master_Kit>/_BUILD-LOG/RUN-X-report.md` ("needs Chrome restart" at top).

# RUN X (terminal A, GHL browser UI): fixes from the Run P and Run Q audits, then Run R

Written by Cowork 2026-09-13. Same rules as every GHL run (app.ridethehightide.com only, one tab, Chrome in front,
never the in-app refresh link, </> source dialog with a triple click first, reload and re-read after every save,
unique phone + plus-addressed email on test contacts, delete them after, no dashes, never enable SMS or HIPAA).
Dead UI rule: one low-stakes click test first; if a page does not respond after one Cmd+R, stop cleanly, write the
report with "needs Chrome restart" at the top, and end. Copy this file to `_briefs/RUN-X-terminal-A.md`, log there,
commit and push after each part. Report: `<Master_Kit>/_BUILD-LOG/RUN-X-report.md`.

## Part 1: three fixes in the cadence workflows (decisions made, do not ask)
1. "Post-Presentation Email" (304a9fa4-a256-4015-b767-031070f4186f): the Wait node labelled "Wait 3 days" that is
   configured for 3 minutes is a bug. Set it to 3 days (the spec is Email 2 at +2 hours, Email 3 at +3 days,
   Email 4 at +7 days; check the other two waits match and fix them too if not). Publish, reload, re-read.
2. "Call: not now" (ff950be3-829d-4a51-8f9a-825db660796e): remove `quiet` from the suppression gate. The Long
   Tail loop ends by adding `not-now` precisely so that quiet contacts enter the 45-day rhythm; with `quiet` in the
   gate the hand-off is suppressed (Run P test 1 showed this). The gate keeps reply received, booked, client-current,
   do-not-prospect, partner, dnc. Publish, reload, re-read.
3. Construction branch drop-off: in both workflows the construction If/Else branch ends after the audit email, so
   construction contacts lose the rest of the chain. In "Post-Presentation Email", after the audit email's Last Touch
   Date + recent-touch, use Copy action to duplicate the None branch's remaining chain (Wait 4 days, Gate 3, LT-3,
   ..., Gate 6, Add tag not-now) into the construction branch. In "Call: not now", duplicate whatever follows 45-B in
   the None branch (its task, the wait, 45-C and onward, through Add tag loop-restart) into the construction branch.
   Publish both, reload, re-read, and confirm the branch counts in the report.

## Part 2: link repoints and clean-up
4. The "Time and Cost Savings calculator" is a real, separate tool (Master Kit `06 Calculators and Tools/
   Atlas_One_Time_Savings_Discovery.html`). Terminal B is publishing it at
   `https://forms.atlasonesolutions.com/tools/time-savings/`. If curl returns 200, repoint the "Time and Cost
   Savings" links in E0 and in the three Q-1 sends to that URL (the Retention Cost Calculator link stays in LT-4 and
   45-C). If 404, leave the links as they are and note it.
5. Delete the test contact "Run S Test Co" (phone 8015553335, email muddybudmods+runs5363335@gmail.com).
6. Add the "Build this document for me" and "Service sign-up" tags (document-build, service-signup) only if Run R
   below gets built; otherwise skip.

## Part 3: Run R
Then execute Run R exactly as written in `_briefs/RUN-A-batch-2026-09-12.md` (forms C1 and C2, the two intake
workflows, seed tests, paste the C2 URL into `GHL_BUILD_FORM` in `repo:build/index.html`, push, confirm the forward
page). The read-only research from RUN-R-report.md (existing fields to reuse, Form B's native Advanced styling, the
Show/Hide Fields pattern) is already done; use it. Sites > Forms was the module that died last time: run the click
test on Sites > Forms specifically before building.

Report: `RUN-X-report.md` with Part 1 confirmations (node values read back after reload), Part 2 results, and the
Run R closeout (form ids, URLs, workflow ids, fields created, questions).
