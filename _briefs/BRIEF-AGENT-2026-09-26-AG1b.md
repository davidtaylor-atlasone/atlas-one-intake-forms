# BRIEF-AGENT (Run AG1b, 2026-09-26): fix the master book so it is safe to load. READ ONLY.

Terminal: AGENT. Written by Cowork after auditing AG1 (`_BUILD-LOG/COWORK-AUDIT-run-AG1-2026-09-26.md`, read it
first). Same rules as AG1: read only in every source, no GHL writes, no file moves, no employee level files
(census, payroll, W-2, W-4, I-9, SSN, DOB, enrollment, direct deposit), no FEINs, rates, commissions or bank
details in outputs, nothing with client data in git. Reuse your AG1 scripts; fix them, do not start over.
Back up the RUN-AGENT-report.md sitting there to `_to_delete/superseded-2026-09-26/run-ag1-report/` first.

## Fix 1: Cornerstone truth
`~/Downloads/cornerstone-book-2026-09-26.json` (David's Cornerstone Connect export: accounts, contacts, notes,
tasks; formatted values use the key suffix `@OData.Community.Display.V1.FormattedValue`). If it is missing, stop
and write "needs the Cornerstone export" at the top of the report. Otherwise:
- A company is a Cornerstone record ONLY if it is in this file (or in "DT Clients - CSR.xlsx"). Status from the
  file: comm_accounttype Active or Pending Initial Payroll, or stage Active Client or Enrollment = Cornerstone
  Client; Terminated = Former Client; stage Sales or Underwriting and not lost = Prospect open; Lost or Not
  Onboarded with stage Lost = Lost.
- Fill from the file: CSR (_comm_clientservicesrepresentative_value), contract type (comm_contracttype),
  referral partner (_comm_broker_value), effective date (comm_effectivedate), employees (comm_employeecount),
  address, main phone, website, services (craff_benefitsstatus, comm_k for 401k, craff_timeandattendancestatus,
  craff_backgroundcheckstatus, craff_drugscreeningstatus, comm_paycard), Cornerstone entity code
  (_comm_peo_value: CIP, CU, CCG, CESIV). Contacts from `contacts`, notes and tasks from `notes`/`tasks`
  (key `acct` = accountid).
- Rows in "Client CSR List for David 9.9.25.xlsx" that are NOT in the export go to a new tab "Cornerstone
  verify" and are not load ready. David decides whether they are his.

## Fix 2: Zoho is Teamworks, never Cornerstone
Every Zoho file (ZOHO Reports, all "Zoho client info" copies, Closed Deals, Sales Deals, the iCloud ZOHO
information folder) is Teamworks Group's CRM, which continued under G&A after the acquisition. Map: Closed Won
= "Former Teamworks client" unless the company has a G&A client folder or an Active rating in G&A CRM Accounts
Update (then G&A Client). Closed Lost and variants = Lost. Open deals and leads = Prospect open or Lead. Never
set PEO = Cornerstone from a Zoho row. Recompute the Conflicts tab after this; list HARD conflicts (real
folders on both sides) separately at the top.

## Fix 3: contacts and notes
- Gather every contact per company from: the Cornerstone export, G&A CRM Accounts Update (any contact, email,
  phone columns), the Zoho Sales Deals report copy with data, the iCloud ZOHO information Contacts and Leads
  files, and the fresh GHL snapshot. Contacts tab: one row per person, company, source.
- Link Zoho notes (Notes_Accounts, Notes_Contacts, Notes_Deals, Parent ID) to companies through any export that
  carries Zoho record IDs (look for Record Id, Account Id, Deal Id, Contact Id columns in every Zoho file,
  including the iCloud ones). Notes tab: company, date, source, text (strip HTML, cap 4,000 characters). Report
  how many notes linked and how many could not be.

## Fix 4: load readiness
Add column "Load ready" = yes only when the company has a real status AND at least one contact with an email
or a phone. Name only rows go to a tab "Needs contact" and are never created in GHL. Recount load-plan.md with
this rule and with the Cornerstone and Teamworks fixes. Match to GHL by email, then phone, then email domain,
then name.

## Outputs
`master-book-v2-2026-09-26.xlsx` (tabs: Book, Cornerstone verify, Needs contact, Conflicts, Contacts, Notes,
Sources), updated load-plan.md and summary json. Move v1 master-book-2026-09-26.xlsx to
`_to_delete/superseded-2026-09-26/master-book-v1/`. Report RUN-AGENT-report.md with counts before and after each
fix, and at the end these questions for David: which Zoho Notes_Deals copy is current; which Teamworks Group
One Drive Transfer folder is the real one; the HARD conflicts list (company, both folders) for his call.
