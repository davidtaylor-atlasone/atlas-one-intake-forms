# Brief: build the Atlas One prospecting workflows in GoHighLevel (W0, W1 to W7, templates, fields)

Read all of this, then execute end to end. Batch questions to the very end; make the reasonable call and log it.
Work in ONE Chrome tab at **https://app.ridethehightide.com** (never app.gohighlevel.com; the builder does not
accept clicks there), sub-account Atlas One Solutions, location `AzTPxnK2vSUj19jYoDmR`. If pages render blank or
spin, the session logged out silently: look for `?logout=true` and sign in again, then continue.

The full click-by-click spec is the runbook next to this file:
`OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit/12 GHL Setup doccs/Atlas_One_GHL_Prospecting_Workflows_Runbook.md`
Follow it in order. This brief adds the rules, the checkpoints and the source files for the copy.

## Hard rules
1. No text message may send until Settings > Phone Numbers > Trust Center shows the A2P campaign **Approved**.
   Build every Send SMS action, then toggle it **disabled** on the card. Report the A2P status in the checkpoint.
2. Never tag `SMS consent` on any contact. Never enable HIPAA. Never rename a dropdown option (delete + re-add).
3. Save is not Publish. Publish each workflow only after its test passes; report which are Published.
4. Email bodies go in through the `</>` source dialog, never the rich editor. Subjects typed plain. **No dashes**
   anywhere in any subject or body (no em dashes, no hyphens used as dashes). Read the body back after saving and
   compare to the source; never save an action whose body does not match.
5. Filter every Form Submitted trigger to its specific form. Use one trigger per value (filters inside one trigger
   are ANDed).
6. Atlas One templates sign as David Taylor, Atlas One Solutions, 385-213-7177, David@AtlasOneSolutions.com, button
   to `https://api.leadconnectorhq.com/widget/bookings/back-office-audit-30`, signature link
   `https://api.leadconnectorhq.com/widget/groups/book-david`. The three W7 templates sign as David Taylor, Cornerstone
   PEO, (801) 358-8547, david.taylor@cornerstonepeo.com, link `https://scheduler.zoom.us/david-taylor-qp71rc`, and
   never mention Atlas One, Hearvana, or any credit match mechanics.
7. Use the branded wrapper Run E established (Marketing > Emails > Templates, any "C1" or booking email is the
   reference: logo header, periwinkle table button, text signature, "ONE CALL SOLVES EVERYTHING." line, Lehi footer).
   Logo URL:
   `https://storage.googleapis.com/highlevel-backend.appspot.com/location/AzTPxnK2vSUj19jYoDmR/form/Cxqawj85qg4ULUl64nMc/header-image/923a20f4-ffe6-4528-8245-d2f698889c5e.png`

## Where the copy comes from (read these files from OneDrive on this Mac; they are HTML, read the text)
- `A1_Sales/Atlas_One_Prospecting_Playbook_v1.html`: section 4 (cadences), section 5 (every email, voicemail, text
  and breakup, with the referral, trigger and consolidation variants), section 8 (the workflow map).
- `A1_Sales/Industry Playbooks/Atlas_One_Industry_Overlay_0N_*.html` (six files): each has "the lines that replace
  the generic ones" and an Email 1, 2, 3 and breakup for that vertical, plus the free tool that fits. Use them for
  W0's Vertical Opener / Vertical Proof / Vertical Tool values and for the W7 audiology emails (WSA channel, Cornerstone).
- Existing GHL emails to reuse, not rebuild: "Instant auto-reply", "Moving forward" (post-presentation), C1/C2/C3.

## Build order and checkpoints (stop and report after each; then continue)
Checkpoint 1: Part 1 fields and tags created; list each with its type and options, read back from Settings.
Checkpoint 2: Part 2 templates built (24); one test send of each to David@AtlasOneSolutions.com; report the ones
where the merge tags did not resolve or the button was not a button.
Checkpoint 3: W6, W6b, W0 Published; execution log screenshot of a test contact getting `Reply received`.
Checkpoint 4: W1 Published; Form A test submission produced auto-reply + CALL NOW task + Lead Lane C.
Checkpoint 5: W2, W7 Published; a test contact with Lead Lane A and Brand Identity = Cornerstone ran W7 and NOT W2,
and the Personal Line gate held Email 1 until the field was filled.
Checkpoint 6: W3, W3a Published; a test contact with WC Renewal Date 100 days out shows the minus-90 wait scheduled.
Checkpoint 7: W4, W5 Published; W4 test contact shows the nine steps in the log with business-day waits.
Checkpoint 8: old shells handled, two smart lists built, A2P status reported, SMS actions all disabled, final list
of every Published workflow with its trigger.

## What David does himself (tell him exactly, in plain words, at the end)
- Trust Center A2P registration (needs the EIN; the brief cannot type it).
- Adding david.taylor@cornerstonepeo.com as a verified sender in Settings > Email Services (clicks the link that
  arrives in that mailbox).
- Setting business hours in Settings > Business Profile if they are empty.
- The Monday batch: 25 names, Lead Lane D, Vertical, tag `Batch ready`; 20 a day for the first two weeks.

## Do not
- Do not build in Jotform, HubSpot or Zapier. Do not create a second sending domain. Do not touch the four booking
  workflows, the intake forms, the Won - Pay Referral Partner or Post-Presentation Email workflows except to leave
  them alone.
- Do not invent copy. If a template's source text is missing, use the Playbook's generic version and log it.

Commit nothing to git for this brief (it is all inside GHL). Write the checkpoint reports to
`~/Projects/atlas-one-intake-forms/_briefs/prospecting-workflows-W1-W7-REPORT.md` as you go, so Cowork can audit.
