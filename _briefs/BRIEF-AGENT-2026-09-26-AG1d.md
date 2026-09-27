# BRIEF-AGENT (Run AG1d, 2026-09-26): three defects Cowork found in v3. READ ONLY.

Terminal: AGENT. Same rules as AG1 to AG1c (read only, no GHL writes, no employee files, no FEIN/rates/
commission/bank, nothing with client data in git). Patch job_ag1c_build.py; do not start over. Back up the
current RUN-AGENT-report.md to `_to_delete/superseded-2026-09-26/run-ag1c-report/` first.

Cowork opened master-book-v3 on disk. Good: the export fields land (5G Hearing, AAMCOR Inc, Cirque, Ibex, Vet-AI
carry CSR, contract type, effective date, services); conflicts down to 16; nothing written to GHL. Three defects:

## Defect 1: Cornerstone Client still counts rows that are not David's
Book shows 395 Cornerstone Client, only 83 of them from the Cornerstone Connect export. 273 of the rest are the
SAME companies you also put on the "Cornerstone verify" tab, so they are listed twice and wrongly marked as
clients. Rule (repeat of AG1c): a company is Cornerstone Client, Former Client, Prospect or Lost on the Cornerstone
side ONLY if it is in the export or in "DT Clients - CSR.xlsx". A CSR list only row lives on the verify tab and
NOT in Book. A company whose only Cornerstone evidence is a folder under Clients Cornerstone gets status
"Cornerstone (folder only, verify)", Load ready no, and also goes on the verify tab.

## Defect 2: folder parser turns subfolders into companies
Book has rows like "1. Client Info CornerStone", "1099 Proposals", "2. Clients Previous Provider Information",
"1. Hoffman Refferals", "1. Z Works Refferals", "1. Mathew Matta Referaals". Rule: a company folder is an
immediate child of a Clients or Quotes root, or of a group wrapper directly under that root (names that start with
a number and a dot, like "3. PPG Clients", "0. Terminated clients", "2. Hoffman accounts"). NEVER a folder nested
inside a company folder. Drop any candidate that starts with a number and a dot, or whose name is a generic word
set (client info, proposals, previous provider, referrals, census, payroll, docs, forms, quotes, copy folders).
Apply to Cornerstone, G&A and Atlas One trees. Report how many rows this removes, with ten examples.

## Defect 3: the main contact skips the real person
Only 19 of 117 export companies show a main contact email, yet the export has 115 contacts with email. The main
contact picker takes the "company phone, no named contact" row first. Rule: main contact = a named person with an
email, preferring Cornerstone Connect for Cornerstone records, then any source; else a named person with a phone;
company phone only as the last fallback (put it in the Phone column, not as a person). Example that must come out
right: Ibex Plumbing main contact Mason Finch, info@ibexplumbingutah.com.

## Also
- Merge by placement: "AAMCOR Companies" (G&A lost) into the AAMCOR row with a placement note; "Vet AI PPG referral"
  into "Vet-AI Inc". Any Atlas One folder whose name is an existing company plus a task word (for example "Cirque
  Lodge Tax Fillings") becomes a note and a folder path on that company, not its own row.
- Outputs: master-book-v4-2026-09-26.xlsx, load-plan.md, summary-v4; move v3 files to
  `_to_delete/superseded-2026-09-26/master-book-v3/`. Report before and after counts for each defect and repeat the
  spot check (5G Hearing, AAMCOR, Cirque Lodge, Ibex Plumbing, Vet-AI, Alta Auto Sales) showing Status, PEO, CSR,
  main contact name and email, Load ready. Also confirm the committed build script holds no client data.
