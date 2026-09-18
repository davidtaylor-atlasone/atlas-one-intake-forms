# RUN-GHL report: Run BO

David: publish Portal: document ready and Portal: document uploaded when ready.

Terminal: GHL (ghl-browser Playwright MCP only). Part 37 (portal document workflows) done end to end.
Prereq confirmed first: `RUN-GHL-JOBS-report.md` is Run BN and lists both template ids (`A1 | Portal | doc-ready`
= `6aacceeb9ed784b5dfd02b80`, `A1 | Internal | doc-uploaded` = `6aacceec9ed784b5dfd02b88`). Zero hard stops.

## Part 37a: "Portal: document ready" (new workflow, id `a2ae7f8f-471b-4efc-a305-bb3490bf2ce3`)

Built:
- Trigger: Contact Tag, event Tag added, tag `portal-doc-ready` (tag did not exist, created it).
- Action 1, Send Email: template `A1 | Portal | doc-ready`, From Name "David Taylor, Atlas One Solutions",
  From Email `David@AtlasOneSolutions.com` (per BUILD-INDEX rule 30/41: sending stays on the LeadConnector
  `lc.atlasonesolutions.com` subdomain automatically; the From Email field itself is the real
  `atlasonesolutions.com` address, matching every other workflow's Send Email node), Reply Address left empty,
  Subject "Your document is ready in the Atlas One portal".
- Action 2, Remove Contact Tag: `portal-doc-ready`.
- Save, left Draft.

Verification (fresh navigation: Workflows list showed Draft, reopened the workflow, reopened the Email
action): trigger reads `Tag added includes "portal-doc-ready"`, node order Contact Tag -> Email -> Remove
Tag -> END, Email action's From Name, From Email, Subject and template body all read back exactly as saved.
Screenshots: `_briefs/assets/run-BO/shots/part37a-portal-document-ready.png`,
`part37c-readback-doc-ready-canvas.png`, `part37c-readback-doc-ready-email-action.png`.

## Part 37b: "Portal: document uploaded" (new workflow, id `a0973659-45cb-4181-80a2-83ad525c1715`)

Built:
- Trigger: Contact Tag, event Tag added, tag `doc-uploaded` (tag did not exist, created it).
- Action 1, Send Internal Notification: type Email (the internal notification action supports a template
  directly, so no Quick-Compose workaround from Run BD Part 26 to 28 was needed), To User Type "Custom email",
  To Custom Email `David@atlasonesolutions.com`, template `A1 | Internal | doc-uploaded`, Subject "Document
  uploaded to the portal".
- Action 2, Remove Contact Tag: `doc-uploaded`.
- Save, left Draft.

Verification (fresh navigation): trigger reads `Tag added includes "doc-uploaded"`, node order Contact Tag ->
Internal Notification -> Remove Tag -> END, Internal Notification's type, To Custom Email, subject and
template all read back exactly as saved. Screenshots:
`_briefs/assets/run-BO/shots/part37c-readback-doc-uploaded-canvas.png`,
`part37c-readback-doc-uploaded-internal-notification.png`.

Neither workflow was tested live: a test send would email a real address, which is out of scope for this run.

## Assumptions

1. Both workflows were built at the top level, not inside an "Intake" folder as the brief allowed ("folder
   Intake if folders exist"): this GHL account's workflow list has no folders at all right now (only the
   "Create folder" button, no existing folder rows), so there was nothing to place them in.
2. Email action "From Email": left blank the two fields would use account Default Values, but the brief
   named a specific From Name, and the builder makes From Email mandatory once From Name is filled in. Used
   `David@AtlasOneSolutions.com`, the same address every other workflow's Send Email node uses per
   `TERMINAL-GHL-live.md` 2026-09-16 (Part 24d: "From email David@AtlasOneSolutions.com, both correct (not
   lc.)"; the lc. subdomain only shows up as GHL's own Reply-To rewrite, not as a From Email setting).
3. Both Subject lines ("Your document is ready in the Atlas One portal" and "Document uploaded to the
   portal") are new copy, not specified word for word in the brief; wrote them plain, no dashes, matching the
   templates' own content (client "Open my portal" / internal document-uploaded notice).
4. Internal Notification's To User Type: used "Custom email" (a real option in this builder) rather than the
   brief's fallback Quick-Compose workaround, since Internal Notification here supports a template directly
   and a Custom Email field for the destination address.
5. Both new tags (`portal-doc-ready`, `doc-uploaded`) were created inline the first time each was referenced
   (trigger, then again as the tag removed by the Remove Contact Tag action, same tag reused, not a second
   tag).

## Product note (not a brief item, logged for the record)

The trigger config panel's "Add filters" control and the workflow-tree "Add action" arrow attached to a
node's own header both had a UI quirk in this session: "Add filters" did not respond to a normal click until
dispatched directly on its inner element (worked once that was done, no further issue after); the "Add
action" arrow shown at the top of a node inserts a new action BEFORE that node, not after it, which reordered
both workflows once before being caught in the fresh-navigation read-back and corrected by deleting and
re-adding each Remove Tag action from the round plus-circle rendered between the correct two nodes instead.
Neither is a brief blocker; flagging in case it recurs on a future run.

## Skipped

Nothing skipped. Both workflows fully built, verified by fresh navigation, screenshotted.

## Questions for David

1. Both workflows are ready for you to review and publish when you're ready (see the line at the top of this
   report). No changes needed from GHL-JOBS or another run first.
2. Subject lines ("Your document is ready in the Atlas One portal" / "Document uploaded to the portal") were
   my own wording since the brief didn't specify them word for word — say if you want different copy.
