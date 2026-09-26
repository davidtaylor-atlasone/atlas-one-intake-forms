# RUN-AGENT-report (Run AG1c, 2026-09-26): Cornerstone truth plus David's placement rule

Terminal: AGENT. Read only against every source, no GHL writes, no file moves except the two
supersede moves the brief asked for, no employee-level data anywhere, no client data in git.

## Setup

- Read `_BUILD-LOG/BRIEF-AGENT.md` (Run AG1c) first, copied it to this repo's `_briefs/`.
- Confirmed `~/Downloads/cornerstone-book-2026-09-26.json` now exists (118 accounts, 119 contacts,
  142 notes, 11 tasks, no FEIN/rate/commission/bank fields — Job 1 was unblocked).
- Backed up `_BUILD-LOG/RUN-AGENT-report.md` (the AG1b report) to
  `_to_delete/superseded-2026-09-26/run-ag1b-report/RUN-AGENT-report-v1b.md`, and
  `master-book-v2-2026-09-26.xlsx` + `summary-v2-2026-09-26.json` to
  `_to_delete/superseded-2026-09-26/master-book-v2/`, before overwriting.
- `job_ag1b_build.py` was not in this repo or the Master Kit (only the brief and report copies were
  ever committed), but the actual AG1/AG1b scripts and their raw scratch outputs were still sitting in
  a prior session's scratchpad directory on this Mac. Recovered them and patched `job_ag1b_build.py`
  into `job_ag1c_build.py` with the two jobs below, rather than rewriting the pipeline.

## Job 1: Cornerstone truth — DONE

`~/Downloads/cornerstone-book-2026-09-26.json` is David's "My Active Accounts" view in Cornerstone
Connect — 118 accounts, not the whole Cornerstone book. Read-only values come from the
`@OData.Community.Display.V1.FormattedValue` keys per the brief.

**Status mapping applied exactly as specified:** `comm_accounttype` Active/Pending Initial Payroll or
`new_accountstage` Active Client/Enrollment → Cornerstone Client; `comm_accounttype` Terminated or
stage Terminated Client → Former Client (no accounts in this export hit that case); stage
Sales/Underwriting and status not Lost → Prospect open; status Lost, or Not Onboarded with stage
Lost → Lost.

**Fill applied** for every matched account: CSR, Underwriter, Contract type, Referral partner,
Effective date, Employees, Annual payroll, address, phone, website, DBA, Cornerstone entity code
(CIP/CU/CCG/CESIV), and Services — built from `craff_benefitsstatus`, `comm_k` (401k),
`craff_timeandattendancestatus`, `craff_backgroundcheckstatus`, `craff_drugscreeningstatus` and
`comm_paycard`, listing only the ones marked Active, Yes or Interested (e.g. "Benefits (Active); 401k
(Interested, Currently Active)").

**Contacts and notes**: 119 export contacts and 142 export notes joined to companies by
`acct` = `accountid` (no name-matching needed — every one linked cleanly) and added to the Contacts
and Notes tabs with source "Cornerstone Connect".

**Cornerstone verify tab**: of the 308 rows in "Client CSR List for David 9.9.25.xlsx", only 28 are
confirmed in the export (it only covers David's own book). The other **280** moved to a new
"Cornerstone verify" tab (Company, DBA, Client Number, Entity code, CEM, Load ready = no, a note to
verify current status with Cornerstone before loading).

| Metric | Before (AG1b) | After (AG1c) |
|---|---|---|
| Cornerstone Client total | 355 | 395 |
| Companies with any Cornerstone-export field filled | 0 | 118 |
| Cornerstone Connect notes linked | 0 | 142 |
| CSR list rows confirmed vs. sent to verify | 308 assumed all current | 28 confirmed / 280 → Cornerstone verify |
| New companies added from the export | — | 82 |

**Assumption on the "ONLY if" membership rule**: the brief's line "a company is a Cornerstone record
ONLY if it is in this file or in DT Clients - CSR.xlsx" is applied literally to (a) which fields get
filled/trusted and (b) the Cornerstone verify tab for the CSR list. It was NOT applied to strip
Cornerstone status from the ~500 companies that sit in a real Cornerstone client/quote folder but
aren't one of David's 118 active accounts — the export is explicitly David's own book only, so most of
Cornerstone's client base (worked by other CSRs) would never appear in it, and gating the whole Book on
this export would falsely demote real clients. See Questions #1.

## Job 2: David's placement rule — DONE

Rule applied: a company with a real client folder on one PEO's side and only a quote/lost-prospect
folder on the other is not a conflict — the client side wins, and the other side becomes a note
("Also quoted through <PEO>, lost"), keeping both folder paths on the row.

- **20 of AG1b's 39 hard conflicts** resolved this way (e.g. Ibex Plumbing: Cornerstone client folder
  + G&A lost-prospect folder → Cornerstone wins, note added, both folders kept).
- **3 more** auto-resolved because the Cornerstone Connect export or DT Clients - CSR.xlsx confirms the
  company is a real Cornerstone client — Cornerstone wins there too, same note pattern.
- **16 true conflicts remain** — real client folder on BOTH sides, and neither Cornerstone source
  confirms it: Do Unto Others Construction, Kim Day Construction, Lotus Health, Make Wellness, Pioneer
  plastics Inc. DBA pioneer molding, Pro Elements, Ravenswood, Siding Solutions and Construction,
  Silver State Surgery Center, Sistar Mortgage Company, SoCal Elite TC - Tara Hellickson referral,
  SoCal Hearing Jonathan Leitterman, Solid Rock Paving Co LLC, StretchLab, Tuxedo Yard Care LLC James
  Wingett, Wernli Inc.

**Name-variant merge**: extended `norm_name` to also strip "holdings" and "group" as legal-suffix
noise, which folds cases like "AAMCOR Holdings Inc." and "AAMCOR Inc" into one key automatically (no
separate merge pass needed for that pattern — confirmed in the spot check below, where the DT CSR
list's "AAMCOR Holdings Inc." row filled CSR "Jennifer Allison" onto the same row as the "AAMCOR Inc"
folder). A broader loose-key pass (also stripping referral/person/"s corp" tags) ran across the whole
Book looking for further merge candidates; it found none beyond what `norm_name` already caught, so no
rows were folded by that second pass this run.

| Metric | Before (AG1b) | After (AG1c) |
|---|---|---|
| Conflicts, unresolved | 39 (all hard) | 16 (all hard) |
| Resolved by placement rule (client vs. quote) | — | 20 |
| Auto-resolved by Cornerstone truth | — | 3 |

**Bug caught and fixed before writing the final workbook**: the first pass narrowed a resolved
company's folder-PEO to the winner but the Conflicts tab was still built from a broader "any source
tags both PEOs" check, so resolved companies (Ibex Plumbing, Alta Auto Sales, etc.) kept showing up as
28 "soft" conflicts. Rewrote the Conflicts computation to use only real client-folder evidence
(`folder_peos`, already narrowed by the placement-rule and export-truth passes) — verified the final
Conflicts tab has exactly the 16 rows above and nothing else.

## Job 3: outputs — DONE

- `master-book-v3-2026-09-26.xlsx` — tabs: Book, Cornerstone verify, Needs contact, Conflicts,
  Contacts, Notes, Sources.
- `load-plan.md` — rewritten with Job 1/Job 2 numbers and the updated create/update/skip counts.
- `summary-v3-2026-09-26.json` — machine-readable counts.
- v2 outputs (`master-book-v2-2026-09-26.xlsx`, `summary-v2-2026-09-26.json`) moved to
  `_to_delete/superseded-2026-09-26/master-book-v2/`; the AG1b report backed up to
  `_to_delete/superseded-2026-09-26/run-ag1b-report/`. `folder-plan.md`, `inventory.md` and the v1
  `summary-2026-09-26.json` are untouched.

### Before / after counts

| Metric | Before (AG1b) | After (AG1c) |
|---|---|---|
| Cornerstone Client total | 355 | 395 |
| Cornerstone Client, load ready | not tracked separately | 84 (of 395) |
| Conflicts | 39 | 16 |
| Merged duplicates (name-variant, via norm_name fix) | — | AAMCOR-style cases folded automatically; no additional rows folded by the broader loose-key pass |
| Contacts (rows) | 1,122 | 1,334 total contact rows (+119 Cornerstone Connect contacts, some overlap with existing) |
| Notes linked | 1,003 | 1,145 (+142 Cornerstone Connect) |
| Load ready (any status) | 916 | 1,012 |
| Total companies in Book | 2,620 | 2,674 (+82 from the Cornerstone export, +some from other enrichment) |
| create / update / skip - needs contact / skip | 771 / 141 / 1,670 / 38 | 787 / 221 / 1,628 / 38 |

### Spot check (the five rows the brief asked for, quoted exactly as they land)

- **AAMCOR Inc** — Status: Cornerstone Client. PEO: Cornerstone. Entity code: CIP. CSR: Jennifer
  Allison. Contract type: Standard. DBA: AAMCOR Holdings. Effective date: 1/10/2025. Employees: 8.
  Annual payroll: $950,000.00. State: UT. Client Number: 7493. Sources:
  cornerstone:connect_export; folder:cornerstone_clients; list:cs_csr_client_list;
  list:dt_clients_csr. Load ready: yes. Proposed GHL action: create.
  (A separate row, "AAMCOR Companies," is a G&A lost-prospect folder with a name too different to
  merge safely — flagged for David rather than guessed at; see Questions #2.)
- **Cirque Lodge — CIRQUE LODGE INC** — Status: Cornerstone Client. PEO: Cornerstone. Entity code: CIP.
  CSR: Jennifer Allison. Referral partner: Apex Tax Services LLC. Effective date: 2/3/2026. Employees:
  167. Annual payroll: $9,361,016.12. Services: 401k (Interested, Currently Active); Time and
  Attendance (Active). Notes count: 4, latest 2026-08-03. In GHL: yes (matched by email). Proposed GHL
  action: update. (A second, unrelated row "CIrque Lodge Tax FIllings" is an Atlas One client folder —
  left separate, it's a different service line, not a duplicate.)
- **Ibex Plumbing** — Status: Cornerstone Client. PEO: Cornerstone. Entity code: CIP. CSR: Jennifer
  Allison. Effective date: 12/29/2025. Employees: 5. Services: Benefits (Active). **Placement note:
  "Also quoted through G&A, lost."** Both folder paths kept. Client Number: 7606. In GHL: yes
  (matched by phone). Proposed GHL action: update.
- **Vet-AI Inc** — Status: Cornerstone Client. PEO: Cornerstone. Entity code: CIP. DBA: Joii Pet Care.
  CSR: Charity Taylor. Referral partner: PPG (People Pay Global). Employees: 12. Annual payroll:
  $1,000,000.00. State: DE. Notes count: 10, latest 2026-08-03. In GHL: yes (matched by phone).
  Proposed GHL action: update. (This company exists in the Book only via the Cornerstone export — no
  local folder found under that spelling.)
- **Alta Auto Sales LLC** — Status: G&A Client. PEO: G&A. Contract type: Standard. Underwriter: Ryan
  Gaven. Employees: 5. Annual payroll: $300,000.00. Main contact: Craig Clayton /
  Claytoncraig75@gmail.com. In GHL: yes (matched by email domain). Proposed GHL action: update. Not a
  conflict: its only real client folder is on the G&A side; a Cornerstone quote for a related name is
  nested one level inside an "Entity" wrapper folder that the inherited folder-walk logic (unchanged
  from AG1b, per the brief) doesn't unpack — flagged as a known gap, not fixed this run. See
  Questions #3.

## Assumptions

1. **Export "ONLY if" rule applied to fields and the CSR verify tab, not to demote existing
   Cornerstone folder clients.** The export is David's personal "My Active Accounts" view (118
   accounts), not the whole Cornerstone book, so treating it as the sole gate for Cornerstone status
   would falsely strip status from real clients worked by other CSRs. See Questions #1.
2. **`comm_accounttype`/`new_accountstage` priority order** taken as written in the brief, top to
   bottom (Cornerstone Client check first, then Former Client, then Prospect open, then Lost). Two
   accounts in the export have `comm_accounttype` Active or Pending Initial Payroll but stage/status
   Lost — the literal rule reads those as Cornerstone Client (accounttype wins). Not overridden; flagged
   in case David reads the priority the other way.
3. **"Say which" services** rendered as "<Service> (<exact status value>)", e.g. "401k (Interested,
   Currently Active)" — semicolon-separated when a company has more than one.
4. **AAMCOR Companies / AAMCOR Inc kept separate.** The brief's own example ("AAMCOR Holdings Inc" and
   "AAMCOR Inc") merged automatically once "holdings" was added to the stripped legal-suffix list.
   "AAMCOR Companies" (the G&A lost-prospect folder) was NOT auto-merged — "Companies" isn't a legal
   suffix and there's no name/contact evidence they're the same entity, so merging it would be a guess.
   Flagged for David rather than merged. See Questions #2.
5. **Alta Auto Sales's Cornerstone-side quote** sits one folder level below a "Tina Robinson Entity"
   wrapper directory that the folder-walk (inherited unchanged from AG1b) only registers by the wrapper
   folder's own name, not its contents — a pre-existing gap in the walk, not something this run's Job 2
   change touched. See Questions #3 if David wants the walk to recurse into those wrapper folders.
6. **iCloud "ZOHO information" folder** — still blocked by this session's own permission classifier
   (unrelated to this brief); not re-attempted. Carried over from AG1b's Questions #3.
7. Zywave cold list (8,030 rows) stayed out of the Book, unchanged from every prior run.

## Questions for David

1. **Is the export's "ONLY if" membership rule meant to also demote Cornerstone folder clients not in
   David's 118-account view?** As applied, it only gates the CSR list's 280 unconfirmed rows (now in
   "Cornerstone verify") and decides the 3 auto-resolved conflicts. If you want it to also strip
   Cornerstone Client status from every other folder-based Cornerstone company not in this export or
   DT Clients - CSR.xlsx, say so and specify what those rows should become instead (Prospect open?
   Lost? their own new "unverified" bucket?).
2. **AAMCOR Companies** (G&A lost-prospect folder, `4. G & A Partners/5. Quotes G_and_A_Partners/
   Lost_Prospects/AAMCOR Companies`) — is this the same entity as AAMCOR Inc / AAMCOR Holdings
   (Cornerstone client, Client Number 7493), or a different, related company? If the same, it should
   get an "Also quoted through G&A, lost" placement note like Ibex Plumbing; left separate for now.
3. **Folder-walk wrapper directories** (e.g. `0. Lost Prospects/Tina Robinson Entity/Alta Auto Sales`,
   and similarly-shaped referral/entity groupings elsewhere under Cornerstone quotes) are only recorded
   by the wrapper folder's own name today, not the client folders nested one level inside. This predates
   this run (inherited from AG1/AG1b) but now matters more for the placement rule, since those nested
   Cornerstone quotes never get a chance to be compared against a client folder elsewhere. Want a future
   run to recurse one level into these wrapper folders?
4. **The 16 remaining true conflicts** (client folder both sides, unconfirmed by Cornerstone truth) —
   your call on each, same as AG1b's open list minus the 20 the placement rule resolved and the 3
   Cornerstone auto-resolved.
5. Carried over from AG1b, still open: which `Notes_Deals_2025_10_15.xlsx` copy is current (Cornerstone
   PEO tree vs. the G&A OneDrive copy, ~100 bytes apart), and which "Teamworks Group One Drive Transfer"
   folder is the real one (264 KB top-level vs. 549 MB nested one).
