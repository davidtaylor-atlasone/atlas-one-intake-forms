# RUN-GHL Report — Run AW, 2026-09-15

**NEEDS CHROME RESTART.** This run could not make any GHL UI changes; it hit the same dead-UI bug documented in
Runs AP, AR, AS, AT and AV before it could start Part 10. David needs to fully quit Chrome (Cmd+Q, not just close
the window) and relaunch before the next GHL terminal run.

## What happened

1. Copied the brief to `_briefs/BRIEF-GHL-2026-09-15.md` per the terminal rules.
2. Confirmed from the live log that Parts 0 to 4 are complete (Run AU built Parts 0 to 3; Run AV completed Part 4:
   the three portal custom fields plus the `locations/customFields.readonly` scope on the "Atlas One apps" private
   integration). Run AV then hit the same dead-UI bug at the start of Part 5 and stopped.
3. This run's brief reorders the remaining work: Part 10 first (WSA/W7 template copy), then Parts 5, 6, 7, 8, 9.
4. Opened the Chrome tab at `app.ridethehightide.com/` (never a direct URL) per the dead-UI rule. The dashboard
   loaded correctly. Clicked into Marketing (loaded, Social Planner rendered with real scheduled-post data).
   Clicked the Emails tab (loaded, Statistics sub-tab rendered with real campaign numbers: 40 delivered, 0
   bounced, 5% clicked).
5. Clicked the "Templates" sub-tab (needed to open W7-1/W7-2/W7-3 for Part 10). The click did not register: the
   URL stayed on `/marketing/emails/statistics` and the page content did not change.
6. Console check confirmed `FirebaseError: Missing or insufficient permissions` firing again (same error signature
   as every prior dead-UI report this month).
7. Did one Cmd+R reload of the tab and retried the exact same click once, per the rule. Still dead, same console
   error, same unchanged URL.
8. Stopped per the rule rather than repeating failed clicks. No template, workflow, form, or setting was touched
   or changed this run.

## Built

Nothing. No GHL changes were made this run.

## Assumptions

1. Treated this as the same known platform/session bug (not a new issue) since the console signature, the
   specific tab-click-not-registering symptom, and the one-reload-then-stop behavior all match Runs AP, AR, AS,
   AT and AV exactly. Did not attempt alternate workarounds (e.g. navigating by pasting a direct URL into the
   address bar) because the dead-UI rule explicitly says never to navigate the tab to a URL directly and to stop
   cleanly instead.
2. Left the brief's Part 10, 5, 6, 7, 8, 9 order intact for the next run rather than reordering, since nothing
   was completed here to change that sequencing.

## Skipped

All of Part 10 (WSA/W7 template copy: templates 6aa0a9f855d1ce8973c141a2, 6aa0a9f955d1ce8973c141a8,
6aa0a9fb6ec737a976fa481f) and all of Parts 5, 6, 7, 8, 9 — none were reached.

## Questions for David

1. This is the sixth run in a row (AP, AR, AS, AT, AV, now AW) to hit the identical
   `FirebaseError: Missing or insufficient permissions` dead-click bug in the GHL web UI, always after a few
   in-app navigations. Restarting Chrome between runs has not reliably cleared it (Run AV's brief noted Chrome
   was fully quit before that run, and it still recurred). Is this a stale Firebase auth/session token issue on
   this Chrome profile specifically, or a GHL-side session limit? Worth checking whether logging out and back
   into GHL (rather than just restarting Chrome) clears it, or whether a second/incognito profile avoids it
   entirely.
2. Part 10 (WSA/W7 copy) and all of Parts 5 to 9 remain fully undone. Next run should start exactly where this
   one stopped: Chrome fully quit and relaunched first, then Part 10, then Parts 5, 6, 7, 8, 9 in that order.
