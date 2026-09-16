# RUN-GHL report (Run BC, 2026-09-16)

Scope this run: Part 15 (BQ-1 #3 in "Seasonal touches 2026-27"), Part 16 (Documents & Contracts templates), Part 17
(Payments > Products audit and additions). Parts 1-14 were completed in prior runs (BA/BB) and are not repeated here.

## Part 15: "Seasonal touches 2026-27" (workflow id `52f414cb-b63e-4425-80c9-adea42a210e3`)

Found that the "BQ-1 #3" Send Email action already existed in the workflow (a leftover Quick Compose placeholder
from an earlier "Copy all actions from here" pass that built the quarterly BQ-1/Q-1 cadence forward through
2027-09-01), positioned exactly where the brief said to add one, with the correct subject already in place. Rather
than add a duplicate node, I switched that existing action from Quick Compose to Template, picked `A1 | BQ-1 |
bq-1`, kept Subject "The easiest time to switch bookkeepers is right now" and From Name "David Taylor, Atlas One
Solutions" (both already correct).

**Read back after save and reload:** opened the workflow fresh, navigated to the BQ-1 #3 node, confirmed the
Create Email mode shows the branded template preview (logo, DM Sans body, "The easiest time to switch bookkeepers
is right now" subject, David Taylor signature block with 380-225-5217). Publish state unchanged (workflow stayed
Published). No other node in the workflow was touched.

## Part 16: Documents & Contracts templates (Payments > Documents & Contracts > Templates)

Source folder used: `2. Atlas 1 Solutions Marketing/A1_Sales/A1 Agreements/2026-09-15 masters/` (the real, non
`_INTERNAL`, masters folder named in the brief). That folder had `Atlas_One_Master_Client_Services_Agreement.pdf`,
`Atlas_One_Hold_Harmless_and_Acknowledgement.pdf`, and all 9 `Atlas_One_*_Schedule.pdf` files needed for this part.
It did NOT yet have `Sample_Proposal_Software_and_Licenses.pdf` (GHL-JOBS Run BA item), but that file is not one of
the 11 templates this part calls for, so it did not block anything.

Built 11 templates, in the required order, each via New > Upload existing PDF's, then on the PDF's last page added
four fields: a Signature field (assigned to Contact) and a Text Field labeled "Printed Name (Client)" for the
client, a Date field labeled "Date Signed" (assigned to Contact), and a second Signature field assigned to
"David Taylor (You)" for Atlas One. Saved each and confirmed the "Template saved successfully" toast:

1. Atlas_One_Master_Client_Services_Agreement
2. Atlas_One_Hold_Harmless_and_Acknowledgement
3. Atlas_One_AI_Services_Schedule
4. Atlas_One_Bookkeeping_Schedule
5. Atlas_One_Certified_Payroll_Schedule
6. Atlas_One_COI_Tracking_Schedule
7. Atlas_One_Document_Services_Schedule
8. Atlas_One_Membership_Schedule
9. Atlas_One_Payroll_to_GL_Converter_Schedule
10. Atlas_One_Software_and_Licenses_Schedule
11. Atlas_One_WC_Audit_Recovery_Schedule

No product or price was attached to any template. No document was created for a real (or test) contact. Nothing
was sent. Screenshot of the Master Client Services Agreement's signature page saved to
`_briefs/assets/run-BC/shots/template-01-master-csa-signature-page.png` in the forms repo.

Two pricing notes surfaced while reading the source PDFs (informational only, no action taken):
- The Atlas_One_Master_Client_Services_Agreement and Atlas_One_Hold_Harmless_and_Acknowledgement PDFs both carry
  the banner "ATTORNEY REVIEW PENDING, DO NOT SEND FOR SIGNATURE UNTIL DAVID CLEARS THIS DOCUMENT." Building the
  template is fine (no send happened), but David should clear these before either is ever used for a real
  signature.
- The Atlas_One_COI_Tracking_Schedule PDF's own pricing table still reads "[__] a month, price pending David's
  confirmation" - that schedule is not price-final yet. Not part of this run's product list, flagging for
  awareness only.

## Part 17: Payments > Products audit and additions

Read-only pass first: 21 existing products, all matched the decided price list exactly (membership $99 / $399 /
$999 (+ $995 setup or $11,988 annual) / $1,900; setups $495 / $995 / $1,500; AI Email Assistant $249 / $499, extra
mailbox $75, setup $750 standard / $999 complex; AI Task Agent $199 standalone or $99 bundled, setup $500). Nothing
needed correcting, so no existing product was edited or deleted.

Then created the 10 missing products (Create Product > Pricing tab, Recurring/Monthly unless noted):

- Payroll to GL Converter: monthly payroll - $50/mo
- Payroll to GL Converter: semi-monthly or bi-weekly payroll - $75/mo
- Payroll to GL Converter: weekly payroll - $125/mo
- Payroll to GL Converter: setup - $250 one time
- Payroll to GL Converter: extra entity or state - $25/mo
- Certified payroll: per active job - $125/mo
- Microsoft 365 Business Basic, per user - $7/mo
- Microsoft 365 Business Standard, per user - $14/mo
- Microsoft 365 Business Premium, per user - $22/mo
- Microsoft 365 Copilot, per user - $21/mo

**Read back after save:** reloaded the Products list, product count moved from 21 to 31, and all 10 new rows show
the correct name and price. No product was attached to any Documents & Contracts template.

## Assumptions

1. Part 15's "add Send Email" instruction was satisfied by switching an already-existing Quick Compose placeholder
   node (built by a prior run's "Copy all actions from here" pass) to the named template, rather than inserting a
   brand new action, since a new node in the same spot would have duplicated the send. The end state (a Send Email
   with template `A1 | BQ-1 | bq-1` right after the Wait until 2027-09-01 node) matches what was asked for.
2. `Sample_Proposal_Software_and_Licenses.pdf` still missing from the masters folder did not block Part 16, since
   none of the 11 named templates needed it; noted for GHL-JOBS to pick up separately.
3. Left the field labels as plain English ("Printed Name (Client)", "Date Signed") rather than matching internal
   variable-style names, since the brief only specified the four field types and who they belong to, not exact
   label text.
4. Did not touch the ATTORNEY REVIEW PENDING banner or the COI Tracking pricing placeholder inside the PDFs
   themselves; that is content GHL-JOBS/Cowork owns, this run only builds the signature fields on top of it.
5. For the new Microsoft 365 and Payroll to GL Converter / Certified payroll products, no description or product
   image was added since the brief only specified name and price; only Setup was left one-time, everything else
   monthly recurring per the brief's own wording.

## Skipped

Nothing in Parts 15-17 was skipped.

## Questions for David

1. The Master Client Services Agreement and Hold Harmless PDFs both still carry the "ATTORNEY REVIEW PENDING, DO
   NOT SEND FOR SIGNATURE" banner. When is that review expected to clear, so the sign-and-bill build can move to
   actually sending these templates?
2. The Atlas_One_COI_Tracking_Schedule pricing is still a placeholder ("price pending David's confirmation"). What
   should the per-month contingency or flat price be, so that line can be finalized before it is ever used?
3. Should the 10 new products (Payroll to GL Converter lines, Certified payroll, Microsoft 365 lines) get product
   images/descriptions to match the rest of the catalog, or is name + price enough for now since they exist mainly
   to back the sign-and-bill system's document/product linkage?
