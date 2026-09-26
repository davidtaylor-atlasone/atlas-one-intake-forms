# BRIEF-AGENT (Run AG1c, 2026-09-26): Cornerstone truth plus David's placement rule. READ ONLY.

Terminal: AGENT. Written by Cowork after auditing AG1b. Same rules as AG1 and AG1b: read only in every source,
no GHL writes, no file moves except retiring your own v2 outputs, no employee level files, no FEINs, rates,
commissions or bank details in outputs, nothing with client data in git. Build on job_ag1b_build.py; do not
start over. Back up the current RUN-AGENT-report.md to `_to_delete/superseded-2026-09-26/run-ag1b-report/` first.

## Job 1: Cornerstone truth (was Fix 1, now unblocked)
`~/Downloads/cornerstone-book-2026-09-26.json` now exists (checked by Cowork: 118 accounts, 119 contacts, 115 with
email, 142 notes, 11 tasks, no FEIN or rate fields). Accounts are raw Dataverse records; readable values sit in
keys ending `@OData.Community.Display.V1.FormattedValue` (use those for option sets and lookups). Contacts, notes
and tasks are already flat, joined to accounts by `acct` = accountid.
- A company is a Cornerstone record ONLY if it is in this file or in "DT Clients - CSR.xlsx".
- Status: comm_accounttype Active or Pending Initial Payroll, or new_accountstage Active Client or Enrollment =
  Cornerstone Client; comm_accounttype Terminated or stage Terminated Client = Former Client; stage Sales or
  Underwriting and status not Lost = Prospect open; Lost, or Not Onboarded with stage Lost = Lost.
- Fill: CSR (_comm_clientservicesrepresentative_value), Underwriter (_craff_assignedunderwriter_value), Contract
  type (comm_contracttype), Referral partner (_comm_broker_value), Effective date (comm_effectivedate), Employees
  (comm_employeecount), Annual payroll (comm_annualpayrollsize), address1_*, telephone1, websiteurl, DBA
  (comm_dbaname), Cornerstone entity code (_comm_peo_value: CIP, CU, CCG, CESIV), Services (craff_benefitsstatus,
  comm_k for 401k, craff_timeandattendancestatus, craff_backgroundcheckstatus, craff_drugscreeningstatus,
  comm_paycard; list only the ones marked Active, Yes or Interested and say which). Contacts and notes into the
  Contacts and Notes tabs with source "Cornerstone Connect".
- "Client CSR List for David 9.9.25.xlsx" rows NOT in the export: new tab "Cornerstone verify", Load ready = no.

## Job 2: David's placement rule (from David, 2026-09-26)
David quotes most prospects through more than one PEO. Whichever PEO he places them with, the folder goes to
that PEO's Clients folder; the other PEO's copy goes to its Lost quotes or lost clients folder. So a company
with folders on both sides is NOT a conflict when one side is a client folder and the other is a quote or lost
folder: the client side is the real PEO, and the other side is history (record it in a note line "Also quoted
through <PEO>, lost"). Apply this to the 39 HARD conflicts and to every dedupe decision. A true conflict is only
a company with CLIENT folders (or client status) on both sides; for those, the Cornerstone export decides if the
company is in it, otherwise list it for David. Also merge obvious same company variants (for example "AAMCOR
Holdings Inc" and "AAMCOR Inc", folder names with a person or "S corp" or "referral" tacked on) into one row,
keeping every folder path.

## Job 3: outputs
`master-book-v3-2026-09-26.xlsx` (tabs: Book, Cornerstone verify, Needs contact, Conflicts, Contacts, Notes,
Sources), updated load-plan.md and summary-v3 json. Move v2 xlsx and summary-v2 to
`_to_delete/superseded-2026-09-26/master-book-v2/`. Report with before and after counts for: Cornerstone
Client total and load ready, conflicts, merged duplicates, contacts, notes. Spot check and quote in the report
these five rows exactly as they land: AAMCOR, Cirque Lodge, Ibex Plumbing, Vet-AI, Alta Auto Sales.
Questions for David at the end (only ones still open).
