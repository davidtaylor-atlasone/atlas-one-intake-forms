# COI collection and sub payment hold: phase 2 spec (GHL automation and client portal plug in)

Written by Claude Code, Run AC, 2026-09-13. Phase 1 (the self contained tracker) is built:
`06 Calculators and Tools (NEW Aug 2026)/Atlas_One_COI_Tracker.html`. This page is the spec for what comes next. Spec, not a build.

## Research findings (30 minutes, 2026-09-13)

What the market charges and does. Sources are vendor pages and vendor authored comparisons, so treat the numbers as
directional and confirm before quoting them to anyone.

| Product | What it does | What it costs (as published or reported) | Who it fits |
|---|---|---|---|
| myCOI (illumend) | Full service COI tracking: licensed reviewers read every certificate line by line, endorsement checks, automated reminders, one way Procore integration, new AI review tool | Custom enterprise contract, reported $5,000 to $7,500 and up a year; another guide reports $1,500 to $3,000 a year or $30 to $60 per vendor; reported 200 certificate minimum | Enterprise, 200 plus vendors, dedicated risk staff |
| Jones (getjones.com) | Construction and commercial real estate; fully managed review, 1,800 plus construction endorsements indexed, bidirectional Procore and Viewpoint Vista | Custom annual quote, reported $3,500 to $8,000 a year; no self service | Enterprise GCs and property managers |
| TrustLayer | AI reads and verifies documents, real time carrier validation, subs need logins; human review is an upgrade tier | Enterprise quote, reported $4,000 and up a year | Larger construction and multi industry |
| Billy (billyforinsurance.com) | Built for GCs: COI plus lien waiver tracking, subs upload without a login, AI review assistant on every plan, managed or self service, bidirectional Procore, Sage, CMiC, Autodesk | Custom annual licence, reported from about $2,500 a year | Mid market GCs, 20 to 150 subs |
| CertFocus (Vertikal RMS) | Self service or full service with credentialed reviewers | Self service $7,500 annual minimum at $6 to $8 per vendor; full service $10,000 minimum at $13 to $29 per vendor; implementation $3,500 to $4,800; vendor pay option $85 to $150 per vendor a year | Mid to enterprise |
| SubDoc, C2COI, SmartCompliance (small end) | Self service trackers with OCR and reminders; SubDoc lets subs upload by magic link and has a free tier for 3 vendors, $20 to $55 a month above that | $0 to $4,000 a year | 1 to 150 subs |
| GHL native (what Atlas One already pays for) | Contacts with custom fields and file uploads, date based workflow triggers, email and SMS reminders, forms and surveys for document upload, pipelines for "certificate status", tasks to a human | Included in the existing GHL subscription; no per vendor fee | Exactly the 5 to 50 sub client, if Atlas One builds the snapshot |

What a construction client with 5 to 50 subs actually needs (from the same sources and from the way the market splits):
one list of subs with the three items that matter (general liability with expiry, workers comp with expiry, the signed
waiver), a flag 30 days before anything lapses, a hard stop on the pay application when something is missing, and a
chase email that names exactly what is missing so the sub's agent can send it without a phone call. They do not need
endorsement forensics, carrier API verification or a vendor login portal; every tool that adds those costs $2,500 to
$10,000 a year and is priced for 100 plus vendors. The gap in the market is the $0 to $99 a month tier done well, and
Atlas One can fill it with GHL plus the tracker, then sell it inside the membership.

## Phase 2A: GHL automation (terminal A builds; this is the brief for it)

Objects
- Contact type "Subcontractor" (tag `sub`), linked to the client by a custom field `client_company` (single line) and
  optionally the client's contact id.
- Custom fields on the sub contact (folder "COI"): `coi_gl_on_file` (yes/no), `coi_gl_expires` (date),
  `coi_wc_on_file` (yes/no), `coi_wc_expires` (date), `coi_waiver_signed` (yes/no), `coi_hold` (dropdown auto / hold /
  release), `coi_status` (dropdown clear / expiring / missing / hold), `coi_gl_file` and `coi_wc_file` (file upload),
  `coi_last_request` (date), `coi_request_count` (number).
- Pipeline "COI status" with stages Clear, Expiring, Missing, Hold. One opportunity per sub, moved by workflow.
- Form "Certificate upload" (public, no login): sub name, email, GL certificate file, WC certificate file, expiry dates,
  waiver upload. Prefilled link per sub. Submission writes the fields above.

Workflows
1. **New sub added** (trigger: tag `sub` added or form "New subcontractor" submitted): send the first request email
   (the tracker's text), set `coi_last_request`, `coi_request_count` = 1, stage Missing, task to the client's office
   contact "confirm sub added".
2. **Expiry chase** (trigger: `coi_gl_expires` or `coi_wc_expires` is 30 days away; second trigger at 14 days; third at
   1 day): email the sub with the specific certificate and date; at 14 days add SMS only if the sub is tagged
   `SMS consent` (rule 27, never cold text); at 0 days move stage to Missing and set `coi_hold` = hold; notify the
   client by email "payment hold on <sub>".
3. **Certificate received** (trigger: form "Certificate upload" submitted): write the fields, move stage to Clear or
   Expiring by the dates, set `coi_hold` = auto, notify the client, stop any running chase.
4. **Weekly digest** to the client (Monday 7 am): count by stage, list of holds and expiring subs, link to the
   portal page. One email, no per sub noise.
5. **Escalation** when `coi_request_count` reaches 3 with no upload: task to David, "call the sub or the agent".

Rules carried over: emails built through the source dialog with table buttons (rule 23); no dashes; nothing sends
until David enables the workflow; SMS only to consented numbers; the certificate files stay in GHL, never emailed
around.

## Phase 2B: client portal plug in (`~/Projects/atlas-one-portal`)

- New page "Subcontractors" (route `/subs`), visible when the client contact carries the tag `service-coi`.
- API `GET /api/subs`: search GHL contacts tagged `sub` whose `client_company` matches the client's company; return
  name, trade, the six COI fields, status, hold, last request. `POST /api/subs/:id/request`: adds a note and a task
  (no email from the portal; the GHL workflow sends). `POST /api/subs`: creates the sub contact with tag `sub` and
  `client_company`, which fires workflow 1.
- Table with the same status by form as the tracker (filled circle, half circle, empty circle, square), a "Hold"
  column, and a "Send request" button per row. CSV export uses the tracker's column set so the two tools round trip.
- Payment hold surface: the Requests page already files a note and a task; add a "Release payment hold" request type
  that flips `coi_hold` to release and records who asked.
- Scopes needed on the Private Integration: contacts.readonly, contacts.write, opportunities.readonly,
  opportunities.write (for the pipeline stage), locations/customFields.readonly.

## Pricing idea (for David, not decided)

Inside the membership at Professional and above; standalone at $49 a month for up to 25 subs and $99 a month for up to
100, setup $250 (the tracker import plus GHL snapshot). That undercuts every named competitor by a factor of five and
costs Atlas One nothing per vendor. Numbers are a proposal; see Questions for David in RUN-AC-report.md.

## Sources
- https://www.vertikalrms.com/article/how-much-does-coi-tracking-software-cost-2026-pricing-guide/
- https://subdoc.io/blog/best-coi-tracking-software-2026
- https://billyforinsurance.com/resources/billy-vs-jones-vs-trustlayer-vs-mycoi-coi-tracking-software/ (Billy authored)
- https://www.softwareadvice.com/insurance/mycoi-profile/
- https://policymanagerhub.com/blog/jones-coi-tracking-review
