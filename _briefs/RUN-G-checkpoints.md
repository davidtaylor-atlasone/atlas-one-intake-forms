# Run G checkpoints (prospecting workflows W0 to W7)

Run started 2026-09-08. Working at app.ridethehightide.com, location AzTPxnK2vSUj19jYoDmR.

## Standing decisions for this run (David's instructions override the brief)
- **Nothing is Published.** Every workflow is saved as **Draft**. The brief and runbook say Publish
  after each test; David reserves publishing as the one production step after Cowork audits.
- **Committing to git at each checkpoint.** The brief says "commit nothing to git"; David asked for
  a commit per checkpoint. Checkpoint notes live here; the audit report also goes to
  prospecting-workflows-W1-W7-REPORT.md.
- Every Send SMS action is built and left **disabled**.
- No `open`/`open -R`/osascript. One Chrome tab only.

## Checkpoint 1: fields and tags

### Navigation finding
Direct URL loads of /settings/* spin forever ("If you are having issues loading the app").
In-app navigation (Dashboard, then click Settings, then the left menu) loads fine. All settings
work in this run was done by clicking, not by typing URLs.

### Custom fields
Already existed in the Prospecting folder (created Sep 08 by an earlier pass), verified not rebuilt:

| Field | Type | Options read back |
|---|---|---|
| Lead Lane | Dropdown (single) | A Referral, B Trigger, C Inbound, D Cold, E Lost |
| Brand Identity | Dropdown (single) | Atlas One, Cornerstone |
| Vertical | Dropdown (single) | Audiology, Dental Ortho Optometry ENT, Construction, Technology, Hospitality, Professional Services, Other |
| Trigger Type | Dropdown (single) | WC renewal, Benefits renewal, New location, Hiring, Ownership change, Vendor complaint, Other |

Created this checkpoint (all Contact object, Prospecting folder). Field count went 747 to 758.

| Field | Type | Key |
|---|---|---|
| Personal Line | Multi line | {{contact.personal_line}} |
| Vertical Opener | Multi line | {{contact.vertical_opener}} |
| Vertical Proof | Multi line | {{contact.vertical_proof}} |
| Vertical Tool | Single line | {{contact.vertical_tool}} |
| Referral Partner Name | Single line | {{contact.referral_partner_name}} |
| Trigger Date | Date picker | {{contact.trigger_date}} |
| Last Touch Date | Date picker | {{contact.last_touch_date}} |
| Next Touch Date | Date picker | {{contact.next_touch_date}} |
| Benefits Renewal Date | Date picker | {{contact.benefits_renewal_date}} |
| Sequence Step | Number | {{contact.sequence_step}} |
| Lifted Suppression | Checkbox (option "Yes") | {{contact.lifted_suppression}} |

Vertical Proof was first created as Single line by mistake; GHL will not let you change a field's
type after creation, so it was deleted and rebuilt as Multi line. Key survived unchanged.

### Tags (11 created, count 11 to 22)
sms consent, cell verified, cooling 30d, cooling 60d, cooling 90d, hold 6m, dnc,
sequence active, batch ready, reply received, not interested.

**GHL lowercases every tag name on save.** The runbook's capitalisation (`SMS consent`,
`Sequence Active`, `DNC`) cannot be preserved. Workflow steps will reference the lowercase forms.
No contact has been tagged `sms consent` and none will be.

### Deviations and assumptions logged at checkpoint 1
1. **WC Renewal Date does not exist under that name.** The runbook says it "already exists from
   Form A; reuse". What exists is **`Workers' Comp Policy Expiration Date`** (Date picker, folder
   Form | Form 1, key {{contact.workers_comp_policy_expiration_date}}). Assumed that is the same
   thing and will be used for W3a's WC branch. Not duplicated.
2. **Benefits Renewal Date did not exist as a date.** Form A has `Benefits Renewal Month`
   (Single line, a month name). A month string cannot drive W3a's minus 120/90/60 date offsets,
   so a real `Benefits Renewal Date` date picker was created. Form A still writes the month field;
   the two are not connected yet. See deferred question 1.
3. **Referral Partner is an Opportunity dropdown**, not a contact text field, so it cannot hold an
   arbitrary referrer name and will not merge reliably into a contact triggered email. Created
   `Referral Partner Name` (contact, single line) for the email merge and left the Opportunity
   dropdown alone for pipeline reporting. Templates use {{contact.referral_partner_name}}.
4. **The brief says 24 templates; the runbook table enumerates 23.** Built 23.

### Templates prepared offline (not yet loaded into GHL)
23 bodies generated from the live "Booking: confirm and remind" Email C1 HTML as the wrapper base,
so header logo, periwinkle table button, text signature, ONE CALL SOLVES EVERYTHING line and Lehi
footer match Run E exactly. Checked programmatically: zero em or en dashes in any subject or body;
the three W7 bodies contain no "Atlas One", no "atlasonesolutions", no "Hearvana", and no credit
mechanics. W7 uses a Cornerstone text wordmark in the header because no Cornerstone logo asset
exists in the source files (deferred question 2).
