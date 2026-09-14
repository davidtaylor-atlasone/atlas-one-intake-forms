# RUN-GHL report (Run AL, 2026-09-13)

NEEDS CHROME RESTART. This run ended when a Cmd+R reload of the "Seasonal touches 2026-27" workflow left the
page blank white with console error `FirebaseError: Missing or insufficient permissions` (plus a session-recording
error), and the editor did not land after the one reload the run rules allow. Per the dead-UI rule this stops the
run here. Everything below Part 3's seasonal inserts (BQ-1, BYE-2), all of Part 4, and all of Part 5 is not done.

Terminal: GHL (the only session allowed in the GoHighLevel browser UI). Brief: `BRIEF-GHL.md` (Run AL: Parts 1-5
in one run), full text also copied to `_briefs/BRIEF-GHL-2026-09-13.md` in the repo. Hand-off mode (Part 0) was
used once, for opening "Seasonal touches 2026-27" the first time it was needed; every other workflow (Post-
Presentation Email, Call: not now, Books: after the call, and the later re-open of Seasonal touches) was reached
by in-app search and click without another hand-off wait.

## Part 1: Q-1 link text fixes (done)

In "Seasonal touches 2026-27", all three Q-1 sends (2027-03-01, 2027-06-01, 2027-09-01) had their generic "here"
links replaced with the specified display text, keeping each link's original URL and dark blue (#23304D) style:
- "See the calculator here" -> "See the calculator"
- "Take the assessment here" -> "Take the two minute assessment"
- "Fifteen minutes here" -> "Book fifteen minutes"

Each of the three was saved, previewed, and screenshotted:
- `_briefs/assets/run-AL/shots/q1-1-links.jpg`
- `_briefs/assets/run-AL/shots/q1-2-links.jpg`
- `_briefs/assets/run-AL/shots/q1-3-links.jpg`

## Part 2: construction dead-end fix (done)

In both "Post-Presentation Email" and "Call: not now", every "Vertical construction check" If/Else that sent
construction contacts to their audit email then straight to END now instead continues into a copy of the same
downstream chain (from the next Wait node through the final Add tag) that the None branch already runs, so
construction contacts get the full cadence instead of stopping after one email. Reloaded and re-read both
workflows after the change; branch and node counts on each match the None branch they were copied from.

## Part 3: "Books: after the call" plus seasonal inserts (partly done)

### "Books: after the call" (new workflow, id `9c1eae4a-80d6-444b-9c12-65e7a834834d`) - built end to end, in Draft

Trigger: Tag added `books-interest`. Re-entry: off (matches "Call: not now" and the Long Tail loop). Node order,
confirmed by reload and re-read after every save:

Trigger -> Gate 0 (Suppressed: 7-segment OR of reply received, booked, client-current, do-not-prospect, partner,
dnc, quiet / None) -> **B-1** (subject "What Atlas One bookkeeping actually looks like, {{contact.first_name}}")
-> Last Touch Date = today (B-1) -> Tag recent-touch (B-1) -> Wait 3 days -> Gate 1 (same 7-segment pattern) ->
**B-2** (subject "What falling behind on the books actually costs") -> LTD (B-2) -> Tag recent-touch (B-2) ->
Wait 4 days -> Gate 2 (same pattern) -> **B-3** (subject "A proof point, no names attached") -> LTD (B-3) -> Tag
recent-touch (B-3) -> Wait 7 days -> Gate 3 (same pattern) -> **B-4** (subject "Should I close your file,
{{contact.first_name}}?") -> LTD (B-4) -> Tag recent-touch (B-4) -> Wait 3 days -> Gate 4 (same pattern) -> on the
None branch, Add tag `not-now` -> END (Suppressed branch also ends). "Call: not now" already triggers on tag
added `not-now`, so no further action was added there. Every Gate 0-4 was built by copying the prior gate's
structure and renaming, so all five carry the identical 7-segment Suppressed condition.

All four email bodies (B-1 through B-4) were pasted from `cadence-emails-2026-09-13/b-1.html` through `b-4.html`
via the Source Code dialog and verified end to end in the WYSIWYG preview (logo, body copy, button and URL,
signature block, tagline, disclosure lines, address line) before saving each action. From name "David Taylor,
Atlas One Solutions", from email david@atlasonesolutions.com throughout, per the brief.

Workflow is left in **Draft**, per the brief: "Publish 'Books: after the call' only after the test in Part 5
passes." Part 5 was not reached this run (see below), so it is still in Draft.

### Seasonal inserts into "Seasonal touches 2026-27" (`52f414cb-b63e-4425-80c9-adea42a210e3`) - 1 of 3 done

Read the existing node order first and it matched RUN-P-report.md: YE-1 2026-11-01, YE-2 2026-11-15, YE-3
2026-12-01, YE-4 2026-12-15, then Q-1 x3 on 2027-03-01/06-01/09-01.

**BYE-1 - done.** Inserted immediately before the existing YE-1 block, as its own Wait node (same date, same
09:00:00 AM time, same "On this date and time" / "Skip all outbound communication actions till next wait or
event start date action" settings as the existing Wait): `Wait until 2026-11-01 (BYE-1)` -> `Condition` (a fresh
6-segment gate: `OR(booked, client-current, do-not-prospect, partner, dnc, recent-touch)`, matching the seasonal
cooldown pattern in the brief) -> **BYE-1** email (subject "January is the easiest month to start clean books",
body from `bye-1.html`, verified in the WYSIWYG preview) -> Last Touch Date = today (BYE-1) -> Tag recent-touch
(BYE-1) -> END. Saved, and confirmed intact by one reload before the workflow became unreachable (see below).

**BQ-1 (x3, before each Q-1 block) - not done.**
**BYE-2 (new date 2027-01-05, between YE-4 and the first Q-1 block) - not done.**

Both were read and are ready to build next run: `bq-1.html` (subject "The easiest time to switch bookkeepers is
right now") for BQ-1, `bye-2.html` (subject "Start the year with a clean set of books") for BYE-2. Same 6-segment
gate pattern as BYE-1 applies to all three.

## Part 4: Run R (forms and intake workflows) - not started

Not reached this run.

## Part 5: tests, cleanup, publish "Books: after the call" - not started

Not reached this run. "Books: after the call" therefore remains in Draft.

## Assumptions

1. For "Books: after the call", built the Suppressed gate as the exact same 7-segment structure used by the
   Long Tail loop and "Call: not now" (copied node by node), per the brief's explicit instruction, rather than
   re-deriving it from scratch.
2. For each seasonal insert's own Wait node, matched the existing Wait's exact settings (date/time picker mode,
   09:00:00 AM, "On this date and time", "Skip all outbound communication actions till next wait or event start
   date action") rather than a bare timer, since the brief said to reuse the same Wait node if GHL allows two
   sends off one Wait, and a duplicate Wait node was needed instead - matching every other setting on it seemed
   the safer choice than guessing at a different configuration.
3. When copying the "Condition" gate for BYE-1's own suppression check, the copy briefly duplicated a segment
   (both an edited copy and the original both read "client-current") before the extra was deleted down to the
   intended 6 segments (booked, client-current, do-not-prospect, partner, dnc, recent-touch). Verified the final
   segment count and every tag value against the brief's `OR(client-current, do-not-prospect, partner, dnc,
   booked, recent-touch)` spec before saving.
4. Mid-build, pasting a copied gate action once briefly showed "Error while saving the workflow - your version is
   outdated" banners on both the "Books: after the call" workflow (twice) and once more when saving BYE-1's
   email; each time the node had actually been added or saved correctly (confirmed by dismissing the banner and
   reloading), so these were treated as transient/cosmetic per the pattern already documented in earlier runs,
   not as failures.

## Questions for David

1. **Same-date pair suppression, carried over from the brief.** Every send in the Books cadence and now BYE-1
   sets `recent-touch`, and every gate checks `recent-touch`. Placing BYE-1 immediately before the existing YE-1
   send (same date) means whichever of the pair fires first will suppress the other for that day - only the
   first email of each pair goes out. This is the same accepted behavior YE-3 already relies on. Should BQ-1 and
   BYE-2 keep this same-day, first-wins design once built, or would you rather move one member of each pair one
   day later so both fire? (One line date change either way, not decided in this run.)
2. **The Seasonal touches editor needs a look before the next run continues.** After saving BYE-1's Tag
   recent-touch action, a normal reload of "Seasonal touches 2026-27" left the page blank white with a Firebase
   permissions error in the console. The workflow itself was confirmed correct and saved just before that
   (screenshot/read-back done), but the editor tab is unusable until Chrome is restarted. Please restart Chrome
   (or the extension) before the next GHL terminal run picks this back up, so it can re-open "Seasonal touches
   2026-27" and finish BQ-1 (x3) and BYE-2, then move on to Part 4 and Part 5.
3. Same open question carried from Run AK's answers section is now resolved (both Books workflows built this
   run, Q-1 links fixed, Email 3 left out of Post-Presentation Email) - no new open items from those answers.
