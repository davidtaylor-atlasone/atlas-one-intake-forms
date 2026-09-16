# RUN AY report (GHL-JOBS terminal)

Small brief: one job, adding the client portal admin sign-in link to the Your queue group in Atlas One COMMAND.

## Built

- **`_INTERNAL (do not share)/catalogue.py`**: added a new link entry `client-portal-admin-sign-in`, "Client portal
  (admin sign-in)", `https://portal.atlasonesolutions.com`, blurb "The live client portal. Sign in as
  david@atlasonesolutions.com to see what any client sees and to switch their tools on.", division "Intake &
  Client", audience internal, `pinned=True`, `queue=True`, `queue_order=4` (placed right after the three AI Email
  Assistant queue links, which hold `queue_order=1,2,3`).
- Removed the `queue=True, queue_order=4` flags from `client-dashboard-ghl` ("Client Dashboard (GHL)"). The entry
  itself is untouched otherwise: still `pinned=True`, still lives in Intake & Client for anyone browsing that
  division directly.
- Ran `catalogue_check.py "<Master_Kit>"`: OK, 192 entries, all paths resolve (up from 186 before this run's edit;
  the count includes entries added in prior runs earlier today).
- Backed up the pre-run `Atlas One COMMAND.html` and `catalogue.py` (via the earlier `_to_delete` moves noted
  below) to `_to_delete/superseded-2026-09-16/pre-RunAY-backups/` before rebuilding.
- Rebuilt with `python3 "_INTERNAL (do not share)/build_command.py" "<Master_Kit>"`: wrote `Atlas One
  COMMAND.html`, 192 items. Title stamp confirmed: `Atlas One COMMAND: build Sep 15, 2026  6:46 PM`.
- Backed up the prior report to
  `_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunAX.md` per the brief.

## Verification

Rendered `Atlas One COMMAND.html` in headless Chromium (Playwright) at 1440x900 and 390x844:

- Clicked the "Start here" nav item at both sizes; the "Your queue" subsection under Start here shows exactly
  four rows, in this order: AI Email Assistant Approval Queue (LIVE), AI Email Assistant Tasks & Follow-ups
  (LIVE), AI Email Assistant Activity log (LIVE), then the new **Client portal (admin sign-in)** row, each
  marked pinned (star icon).
- `document.documentElement.scrollWidth` equalled the viewport width exactly at both 1440 and 390 (no horizontal
  overflow).
- Zero console errors or page errors at either width.
- Clicked the new row's Open button directly: it calls `window.open("https://portal.atlasonesolutions.com",
  "_blank", "noopener")`, confirmed by intercepting the resulting Playwright `page` event, which loaded
  `https://portal.atlasonesolutions.com/` in a new page/tab, exactly as the other queue links do.
- Screenshots: `_briefs/assets/run-AY/shots/command-desktop-start-here.png`,
  `_briefs/assets/run-AY/shots/command-mobile-start-here.png` (plus two earlier full-page shots from the first
  pass, `command-desktop.png` / `command-mobile.png`).

## Assumptions

1. **queue_order placement.** The brief said "queue_order after the three AI Email Assistant links." The three
   existing queue links use `queue_order=1,2,3` (not necessarily in file order) and the old Client Dashboard
   entry held `queue_order=4`. I gave the new link `queue_order=4` and simply removed the queue flag from Client
   Dashboard rather than renumbering anything, since order 4 was already vacated. No renumbering needed elsewhere.
2. **Client Dashboard entry left otherwise unchanged.** The brief said "remove the queue flag... keep it pinned."
   I removed both `queue=True` and `queue_order=4` (queue_order has no meaning without queue=True) and left
   `pinned=True` as instructed. Division, audience, blurb, path all untouched.
3. **192 total entries.** catalogue_check reported 192, not 186 as an earlier run's log entry from today implied.
   Other jobs earlier in the day (the Software and Licenses Schedule, discount features, etc.) added rows between
   then and now; this run's net change is +1 (the new link entry), verified by the pre-edit backup diff being a
   single insertion plus a two-field removal on the Client Dashboard dict.

## Skipped

Nothing in this brief was skipped. It was a single job.

## Questions for David

None. This run's instructions were unambiguous and did not require a judgment call beyond the one logged above
under Assumptions.
