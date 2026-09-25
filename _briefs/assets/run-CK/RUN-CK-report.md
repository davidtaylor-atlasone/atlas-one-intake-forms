# RUN-CK report (put the Cornerstone identity back on the three WSA templates)

First line: Run CJ's brief wrongly called the Cornerstone signature on the WSA W7 templates a
vendor-name defect and rebranded all three to Atlas One. That was wrong: WSA Partnership Plus
material is Cornerstone branded by design, and the "never name a vendor or PEO" rule does not
apply to it. This run reversed exactly the three identity edits Run CJ made on P-W7-1, P-W7-2 and
P-W7-3, verified all three live, read (did not edit) the W7 workflow's email sender configuration,
and added a guard line to email-templates-map.md so the next audit does not repeat this. No sends,
no workflow published or unpublished, nothing deleted. (Note: this file previously held Run CH's
report; that copy is preserved at
`_to_delete/superseded-2026-09-24/run-ch-report/RUN-CH-report-was-RUN-GHL-report.md` before this
run overwrote it, per the brief's instruction to write to this exact filename.)

## Job 1: revert the identity lines on P-W7-1, P-W7-2, P-W7-3

Before touching anything, confirmed on disk that all three files in
`p-templates-2026-09-23/p-w7-*.html` still carried Run CJ's wrong Atlas One identity (Founder,
Atlas One Solutions / 380-225-5217 / David@AtlasOneSolutions.com), then copied those three wrong
files to `Master_Kit/_to_delete/superseded-2026-09-24/p-w7-wrong-atlas-identity/` before editing.

Reverted the disk masters programmatically (three plain string replacements per file: identity
line, phone, email), leaving everything else in the templates untouched, including the Zoom
scheduler booking link (`scheduler.zoom.us/david-taylor-qp71rc`), which is the correct Cornerstone
booking calendar for WSA and was never part of the defect.

Pasted each corrected file into its live template in the Vibe Editor: opened the template, clicked
into the Monaco source editor (clicking the code-role element rather than the textarea directly
avoids the overlay-intercept timeout earlier runs also hit), Cmd+A, filled with the corrected HTML,
confirmed the change in both the raw source panel and the live preview pane, clicked Save
template, and confirmed the "Saved" toast for each of the three.

### Before and after identity lines

| Template | Id | Before (Run CJ, wrong) | After (this run, correct) |
|---|---|---|---|
| P-W7-1 WSA Email 1 | `6aa0a9f855d1ce8973c141a2` | Founder, Atlas One Solutions / 380-225-5217 / David@AtlasOneSolutions.com | PEO Partner & Business Consultant, Cornerstone PEO / (801) 358-8547 / david.taylor@cornerstonepeo.com |
| P-W7-2 WSA Email 2 | `6aa0a9f955d1ce8973c141a8` | same as above | same as above |
| P-W7-3 WSA Email 3 | `6aa0a9fb6ec737a976fa481f` | same as above | same as above |

### Live fetch verification

After saving, re-opened each template fresh in the Vibe Editor (a fresh open triggers the
`GET /emails/builder/data/<locationId>/<templateId>` call) and read the JSON response body straight
from the browser's network log, the same live-saved `editorData` field the app itself renders from.

| Template | updatedAt (UTC) | Cornerstone PEO | (801) 358-8547 | cornerstonepeo.com | Atlas One | Zak |
|---|---|---|---|---|---|---|
| P-W7-1 | 2026-09-25T00:54:21.636Z | present | present | present | zero | zero |
| P-W7-2 | 2026-09-25T00:56:12.907Z | present | present | present | zero | zero |
| P-W7-3 | 2026-09-25T00:58:00.413Z | present | present | present | zero | zero |

No other "Atlas One" text was found in any of the three bodies (Run CJ's own Job 2 audit had
already noted P-W7-1's line about prospects "running ADP or Gusto plus an accountant plus a
broker" as the prospect's own likely vendor, not Atlas One's; that line is untouched and correctly
left alone).

Screenshots: `_briefs/assets/run-CK/shots/p-w7-1-before.png`, `p-w7-1-saved.png`, `p-w7-2-saved.png`,
`p-w7-3-saved.png`.

## Job 2: read only, the W7 workflow's email sender (no edits made)

Found the workflow: **"W7 WSA handoff (Cornerstone)"** (id `04e13657-82b9-4c96-8367-0bcfde1e79ee`),
status Published. Opened it, used Fit to Screen to see the whole tree, and inspected each node with
"Email" in its name. No edits were made and the workflow was not published or unpublished at any
point (its own Save button showed "Saved" and disabled throughout the visit, confirming nothing in
the builder changed).

The workflow does not send the customer-facing WSA emails automatically. For each of the three WSA
emails it instead has an **internal Notification action** (type: Email) that pings David, paired
with a Task node carrying the same instruction, telling David to send the actual P-W7-N template to
the contact by hand.

| Step | Action name | From name | From email | Reply to | Subject | Recipient |
|---|---|---|---|---|---|---|
| Email 1 | Notify David send WSA Email 1 | blank | blank | (no field on this action type) | Send WSA Email 1 as Cornerstone | Particular user: David Taylor |
| Email 2 | Notify David send WSA Email 2 | blank | blank | (no field on this action type) | Send WSA Email 2 as Cornerstone | Particular user: David Taylor |
| Email 3 | Notify David send WSA Email 3 | blank | blank | (no field on this action type) | Send WSA Email 3 as Cornerstone | Particular user: David Taylor |

GHL's own note under the From name/From email fields: "If 'From Name' and 'From email' fields are
empty then Email will be sent using Default Values" (the account/location default sender, not
configured per-action here). This internal Notification action type has no separate Reply-To field
at all, unlike a customer Send Email action.

Each notification's message body is instructional text to David, e.g. "Send WSA Email 1 to this
contact from david.taylor@cornerstonepeo.com. Use the P-W7-1 WSA Email 1 wording. Cornerstone
identity only, PEO scope only, present the credit total only." That is copy telling David what
address to send from by hand, not a configured email header, so it does not answer "what is the
sender" in the technical sense the brief is asking about.

Whether these internal notifications' From name/From email should be explicitly set to the
Cornerstone identity (rather than falling back to account defaults) is David's decision; see
Questions for David.

## Job 3: guard line added

Added one line to `_BUILD-LOG/email-templates-map.md`, directly under the three P-W7 rows:

> WSA templates are Cornerstone branded by design. Do not rebrand to Atlas One. The Cornerstone
> name, cornerstonepeo.com email and 801 number are correct here.

## Assumptions

1. Treated Run CJ's saved (wrong) versions of P-W7-1/2/3 as the "before" state to back up and
   revert, since that is what was actually live at the start of this run, matching the brief's
   description of what Cowork's audit found.
2. Left the Zoom scheduler link untouched in all three templates per the brief's explicit
   instruction, even though it also lives under the `scheduler.zoom.us` domain (not a name-brand
   PEO reference, and it is the real functional WSA booking calendar).
3. Treated "the W7 workflow's email sender" (Job 2) as the three "Notify David" internal
   notification actions, since those are the only "Email" type actions anywhere in this workflow;
   there is no separate outbound Send Email action that fires automatically to the WSA contact.
4. Reported "no field on this action type" for Reply-To rather than leaving the column blank,
   since GHL's internal Notification: Email action genuinely has no Reply-To setting in its UI (a
   customer-facing Send Email action would show one); this is a fact about the action type, not a
   missed value.
5. Backed up the RUN-CH copy that was sitting under this filename to
   `_to_delete/superseded-2026-09-24/run-ch-report/` before overwriting, rather than losing it,
   since the brief only says to write THIS run's report to this name, not to discard the old one.

## Skipped

Nothing skipped. All three Job 1 templates fixed, saved, and live-verified. Job 2 was read only by
design. Job 3's single line was added and nothing else in email-templates-map.md was touched.

## Questions for David

1. Job 2 found the three "Notify David send WSA Email N" internal notifications all use blank
   From name / From email (falling back to account default values) rather than an explicit
   Cornerstone identity. Do you want those two fields set explicitly to
   "David Taylor, Cornerstone PEO" / `david.taylor@cornerstonepeo.com` so the notification email
   itself (not just its instructional body text) carries the Cornerstone identity, or is the
   current default-sender behavior fine since these are internal notifications to you, not
   customer-facing sends?
2. This run backed up Run CJ's wrong Atlas One versions of P-W7-1/2/3 to
   `_to_delete/superseded-2026-09-24/p-w7-wrong-atlas-identity/` rather than deleting them, per the
   hard-stop rule. No action needed unless you want them cleared out at some point.
