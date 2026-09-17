# RUN-BI report (2026-09-17)

## STOPPED EARLY: publish toggle incident on "Post-Presentation Email"

This run stopped before any of Part 32a/32b/33's real edits because of an accidental click on the
workflow-level Draft/Publish switch. Details, in order:

1. Opened "Post-Presentation Email" via a fresh navigation (Automation > Workflows list > row click), confirmed
   Part 0 clear, confirmed Gate 1's full condition list by reading the panel (this was read only, needed as the
   reference pattern for Gates 2 to 5): 10 OR segments total, tags `reply received`, `booked`, `client-current`,
   `do-not-prospect`, `partner`, `dnc`, `cooling 30d`, `cooling 60d`, `cooling 90d`, `hold 6m`. This matches Run
   BH's Part 30b work on this same gate.
2. Tried to close the Gate 1 side panel. The click target resolved to a generic `.hr-switch__button` locator
   instead of the panel's X button, and landed on the top bar's "Draft / Publish" toggle switch instead, flipping
   it from Publish to Draft. No permission prompt fired on that click.
3. Immediately tried to click the switch back to Publish. That click WAS intercepted by the auto mode permission
   classifier and denied with reason "Production Deploy."
4. Every ghl-browser action after that (navigate, tab select) was also denied for the same reason. Only
   read only actions (screenshot, snapshot) still work.
5. Stopped per the hard stop rule: never try to route around the permission classifier. No further edits were
   attempted on this workflow or any other workflow this run.

**Current known state, unverified:** the open browser tab's DOM shows the Draft/Publish switch unchecked
(Draft), per the last screenshot taken (`INCIDENT-publish-toggle-state.png`). Whether that unpublish actually
reached GHL's server or was a local only UI click that never fired the underlying API call is unknown from this
session; every way of checking (reload, navigate elsewhere, open a fresh tab) is now blocked by the same
classifier response.

**What David needs to do:** open "Post-Presentation Email" in Automation > Workflows and confirm the top right
toggle reads Publish (not Draft). If it reads Draft, flip it back to Publish. This is the only real risk from
this run: while in Draft, this workflow would not fire on new pipeline stage changes, so contacts moving into
Sales/Setup Quote Gathering or PEO Census & documents collected would not get Email 1 to Email 5 of the post
presentation nurture until it is republished.

## Built this run
Nothing. Part 32a's only completed step was the read only confirmation of Gate 1's 10 conditions above (no
edits made to Gate 1 or any other gate). Parts 32b and 33 were not started.

## Verification
- Gate 1 condition list read back from the live panel (screenshot `_briefs/assets/run-BI/shots/gate1-panel.png`),
  matches Run BH's Part 30b report.
- Publish toggle state screenshots: `check-after-close-click.png`, `INCIDENT-publish-toggle-state.png`.

## Assumptions
1. Treated the unpublish click and the classifier denial of the re-publish click as a hard stop under the
   brief's "deploying to production" rule, since a publish/unpublish toggle is the same action type Run BH's
   report already flagged the classifier as blocking (publishing the new "Reply task closed" workflow). Reason:
   the brief and CLAUDE.md both say never route around the classifier, and both publishing and unpublishing a
   live workflow are the same class of action.
2. Did not attempt any other workaround (for example, a different selector or a keyboard Escape to close the
   panel) once the classifier began denying actions, on the assumption that the block is now scoped to this
   session rather than to the specific click, since a plain tab select was also denied.
3. Left the four other open tabs (form builder, Joel Gould's contact, custom fields, the Form A public URL)
   untouched; did not attempt to close them since browser_tabs actions are also being denied.

## Skipped
- Part 32a: Gates 2, 3, 4, and the LT-5 gate (two copies each of Gate 4 and Gate 5 exist, for the general and
  construction branches, so six gate edits were planned) — not started.
- Part 32b: retrying the Task Completed trigger's Add filters control on "Reply task closed" — not started.
- Part 33: Form D "Atlas One - Onboarding documents" and the "Intake: onboarding documents" workflow — not
  started.

## Questions for David
1. Please confirm "Post-Presentation Email" is back to Published (see above). If David does this himself, no
   reply needed here beyond confirming it is done; if it is somehow still on Draft and David does not want to
   flip it, say so and the next run will leave it.
2. Same permission classifier question Run BH already raised (publishing "Reply task closed"): does David want
   to grant a standing allowance for the GHL terminal to toggle a workflow's own Draft/Publish switch, or should
   every publish/unpublish keep landing on David's plate? This run's incident shows the classifier also blocks
   the *recovery* click (going back to Publish), not just the forward one, which is a sharper edge case worth a
   decision either way.
3. All of Run BI's actual scope (Parts 32a, 32b, 33) is still open. Cowork, please requeue it for the next run
   once the publish state above is confirmed clean.
