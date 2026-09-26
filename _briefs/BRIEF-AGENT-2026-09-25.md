# BRIEF-AGENT (Run AG1, 2026-09-26): build David's master book of business. READ ONLY.

Terminal name: AGENT. Written by Cowork, chat "A1 AGENT operator".
Goal: one master list of every company David has ever touched (Cornerstone clients, G&A clients, prospects,
lost, former clients, leads, Teamworks and Zoho history, brokers and vendors), deduplicated, with status,
contacts, services and notes, plus a plan for loading it into GoHighLevel and a plan for tidying the folders.
THIS RUN WRITES NOTHING INTO GHL AND MOVES NO FILES. Loading and folder moves are Run AG2 and AG3, after
David approves the plans this run produces.

## Rules (read twice)
- Read only in every source folder. Never move, rename, delete or edit anything there.
- All outputs go in `<Master_Kit>/_INTERNAL (do not share)/Book of Business/` (create it). Nothing with client
  data goes in git.
- Company level data only. NEVER open or copy employee level files: census, payroll registers, W-2, W-4,
  I-9, direct deposit, benefit enrollment forms, anything with SSNs or dates of birth. Skip by file name
  (census, payroll, register, w2, w-2, w4, i9, i-9, ssn, dob, enrollment, direct deposit) and never print
  their contents. Never copy FEINs, admin rates, commission amounts or bank details into outputs.
- iCloud folders may be slow (files download on first read). If a folder refuses, log it and move on.

## Sources (paths on this Mac)
OneDrive root R = ~/Library/CloudStorage/OneDrive-AtlasOneSolutions
- Cornerstone clients: R/3. Cornerstone PEO/4. Clients Cornerstone PEO (and R/3. Cornerstone PEO/Clients Cornerstone,
  which looks like a duplicate copy: prove it by comparing file lists and sizes)
- Cornerstone quotes and lost: R/3. Cornerstone PEO/3. Quotes_Cornerstone_PEO (and "Quotes Cornerstone", likely duplicate)
- Cornerstone sales and leads: R/3. Cornerstone PEO/1. CS Sales (Broker partners, 5. Leads incl. Prospects Zywave.xlsx,
  Old PEO Info Leads/ZOHO Reports, Zoho client info)
- G&A: R/4. G & A Partners/5. Clients_G_and_A_Partners (about 320 company folders, CRM Accounts Update.xlsx),
  R/4. G & A Partners/5. Quotes G_and_A_Partners (Lost_Prospects), R/4. G & A Partners/My Drive G and A/Zoho client info
- Atlas One: R/2. A1 Official Docs/1. A1 Solutions prospect_Client (2. Clients_A1, 3. Quotes_A1),
  R/2. A1 Official Docs/4. Brokers_Vendors A1 Solutions
- ~/Library/CloudStorage/OneDrive-G&APartners/My Drive/Zoho client info
- Teamworks (iCloud): ~/Library/Mobile Documents/com~apple~CloudDocs/Personal/Davids Entities/Family businesses and docs/PEO Business/
  (ZOHO information, Teamworks Client info/.../Docent HR/Leads payroll, Morgan Leads, Teamworks Group One Drive Transfer/.../Leads payroll)
- Cornerstone CRM export: ~/Downloads/cornerstone-book-2026-09-26.json IF it exists (Cowork saves it when David
  says yes). 118 accounts with type, stage, status, CSR, underwriter, contract type, referral partner, PEO entity,
  services, contacts, notes, tasks. If missing, use the CS spreadsheets (Client CSR List for David 9.9.25,
  DT Clients - CSR.xlsx, David Taylor Cold Call Sourced Accounts wContacts.xlsx) and folder names, and say so.
- GHL today: rerun `_INTERNAL (do not share)/GHL Exports/export_for_cornerstone_crm.py` (read only API) for a fresh
  snapshot of the ~2,155 GHL contacts. If it fails, use the 2026-09-24 CSV beside it.

## Job 1: inventory
For every source: file count, size, company folders, spreadsheets found. Prove or disprove each suspected duplicate
folder pair (the two Cornerstone client folders, the two Cornerstone quote folders, the three Zoho client info
copies, the Teamworks Leads payroll copies). Output inventory.md.

## Job 2: read the structured sources
Every xlsx/csv above that holds companies, contacts, deals, notes or services (Zoho reports: Lead, Contact Report,
Contact Mailing List, Accounts by Services, Accounts by Industry, Open Deals, Lost Deals, Closed Deals, Notes
Report, Notes Deal, Notes_Accounts, Notes_Contacts, Notes_Deals, Sales Account report; CS CSR lists; G&A CRM
Accounts Update; Prospects Zywave; Teamworks lead lists; the Cornerstone CRM JSON). For each, record columns and
row counts. Company folders with no spreadsheet row still count as a company (name from the folder).

## Job 3: the master book
One row per company, deduplicated (normalize names: drop LLC, Inc, Corp, punctuation, DBA splits; also match on
email domain and phone). Columns: Company, DBA, Status (Cornerstone Client, G&A Client, Former Client, Prospect
open, Lost, Lead, Broker or Partner, Vendor), PEO (Cornerstone, G&A, Teamworks, none), Contract type, CSR,
Referral partner, Effective date, Employees, State, Services (benefits, 401k, workers comp, time and attendance,
background, drug screening, payroll only), Main contact name, email, phone, title, Other contacts count,
Notes count, Latest note date and a one line latest note, Folder path(s), Sources (which files it came from),
In GHL today (yes/no, GHL contact id), Proposed GHL action (create, update, skip). A company that shows as a
client with G&A must never be marked Cornerstone, and the reverse (David: some prospects are placed with G&A).
Outputs: master-book-2026-09-26.xlsx (tabs: Book, Contacts, Notes, Conflicts, Sources) and a one page summary
with counts by status and PEO.

## Job 4: GHL load plan (plan only)
load-plan.md: counts to create and update, the exact fields each GHL record gets, tags proposed (new tags only:
book-cs-client, book-ga-client, book-former-client, book-prospect, book-lost, book-lead, book-partner, book-vendor;
never client-current, never any tag a workflow uses), notes to attach, and the safety rule for AG2: every NEW
contact is created with Do Not Disturb on for email and SMS until the GHL chat confirms which workflows fire on
Contact Created. List any company that looks like it belongs to two PEOs under Conflicts for David.

## Job 5: folder tidy plan (plan only, move nothing)
folder-plan.md: a proposed clean structure (for example one Clients folder per PEO with subfolders Active,
Former, and one Prospects folder with Open, Lost; duplicates retired to _to_delete/superseded-2026-09-26/),
then every proposed move as a table (from, to, reason). Include how much space the duplicates take.

## Report
RUN-AGENT-report.md: counts per job, the file paths, duplicates found, sources that could not be read,
Assumptions, and Questions for David at the end.
