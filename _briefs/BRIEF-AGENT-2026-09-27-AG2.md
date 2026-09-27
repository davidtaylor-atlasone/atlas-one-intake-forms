# BRIEF-AGENT (Run AG2, 2026-09-27): load the master book into GoHighLevel. APPROVED BY DAVID.

Terminal: AGENT. Written by Cowork after auditing AG1d (master-book-v4 is correct on the six spot checks; Cornerstone
Client 84 from the export only; verify tab separate; Ibex shows Mason Finch). This run WRITES to GoHighLevel, contacts
and notes only, through the Private Integration token the repo already uses (location AzTPxnK2vSUj19jYoDmR). It never
sends, never texts, never creates opportunities, never edits workflows, templates, fields, tags list, forms or settings.
Back up RUN-AGENT-report.md to `_to_delete/superseded-2026-09-27/run-ag1d-report/` first.

## Why the rules below (from the GHL trigger map, _BUILD-LOG/ghl-howto-facts-2026-09-25.md)
Published workflows that could fire from a data load: Tool-Lead Nurture (Contact Created with Lead Source "Website
Tool/Calculator", sends 2 emails); W2 Warm referral (Lead Lane set to "A Referral"); W3 Trigger sequence (Trigger Date
changed, sends emails); W3a Renewal calendar (WC or Benefits Renewal Date changed, sends emails); W5 Lost deal
re-approach (opportunity marked Lost); Won - Pay Referral Partner (pipeline stage Signed or Won); send-peo-form,
send-bk-form, not-now, loop-restart, batch ready, sequence active, audit-offer-sent tags; Seasonal touches (date based,
suppressed for client-current). W0 Set vertical lines only sets three fields and is safe.

## Hard rules
1. Only Book rows with Proposed GHL action create or update. Never the verify, Needs contact, Conflicts tabs.
2. Before each create, search GHL by email, then phone. If found, update that contact instead. Never a duplicate.
3. Set ONLY: first and last name, email, phone, company name, address, city, state, postal code, website, and these
   custom fields if they exist with this exact name: Employee Count, Current Payroll Provider, Vertical. NEVER set
   Lead Source to "Website Tool/Calculator", Lead Lane, Trigger Date, Trigger Type, WC Renewal Date, Benefits Renewal
   Date, Last Touch Date. Never overwrite a non empty field on an existing contact; fill blanks only.
4. Tags (add only): book-import-2026-09 on every record touched, plus one status tag: book-cs-client, book-ga-client,
   book-former-client, book-former-teamworks, book-prospect, book-lost, book-lead, book-atlas-client, book-partner, book-vendor. Active clients
   (Cornerstone Client, G&A Client, Atlas One Client) ALSO get client-current, which suppresses them from marketing
   cadences and seasonal touches (it starts only the 90 day pulse task). No other tag, ever.
5. NO Do Not Disturb. David decided 2026-09-27: nobody is blocked from email or text. Never set or change DND on
   any contact. The status tags in rule 4 are how he builds campaigns (clients vs prospects vs leads vs lost).
6. Assign every created contact to David.
7. Main contact on a referral partner's domain (peoplepayglobal.com, and any domain that belongs to a Broker or
   Partner row) is NOT the client contact: skip that person as the contact, put "Referral partner contact: name,
   email" in the note, and use the next named client contact, else company phone only.
8. One note per company on its contact: status, PEO, entity code, CSR, underwriter, contract type, referral partner,
   effective date, services, placement note, folder path, then every linked note (date and text) newest first,
   capped so the note stays under 60,000 characters. Title "Book of business import 2026-09".
9. Throttle to stay under GHL limits (about 5 calls a second, back off on 429). Log every call result to
   `_INTERNAL (do not share)/Book of Business/ag2-load-log-2026-09-27.csv` (row, action, contact id, result).
   Write resume support: rerunning skips rows already logged as ok.
10. Dry run first: first 10 rows (include AAMCOR, Cirque Lodge, Ibex Plumbing, 5G Hearing) for real, then read each
    back from GHL and verify fields, tags, DND and note. Only then continue with the rest.

## Job 2: brokers, partners and vendors
Book rows with status Broker or Partner or Vendor are no longer skipped. First enrich them: read the folders
R/2. A1 Official Docs/4. Brokers_Vendors A1 Solutions (09_Vendor_Partners, 10_Broker_and_Partner_Docs) and
R/3. Cornerstone PEO/1. CS Sales/Broker partners (its numbered category folders) for each partner or vendor company:
the person's name, email, phone and title from agreements, W-9 cover pages, signature blocks, email signatures and
contact sheets (PDF, docx, xlsx, txt, md, eml). Company level and contact person only; skip bank, tax ID and rate
pages. The numbered category folders (for example "2. Benefit Brokers", "8. HR Partners") are categories, not
companies: use the category as a note ("Partner type: Benefit broker"). Load them with the same search first rules,
tag book-import-2026-09 plus book-partner or book-vendor, never client-current, and one note with partner type,
agreements found (file names) and folder path. Skip any that already exist in GHL except to fill blank fields.

## After the load
Read back counts from GHL by tag. Report: created, updated, skipped, failed (with reasons), count per status tag,
count with client-current, and the four spot check contacts as they read in GHL. Rollback note: every touched
record carries book-import-2026-09. Questions for David at the end.
