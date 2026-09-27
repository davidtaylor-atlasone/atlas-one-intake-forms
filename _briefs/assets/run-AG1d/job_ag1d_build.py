#!/usr/bin/env python3
"""Run AG1d: three Cowork-found defects patched on top of AG1c. Read only against sources.
Builds on job_ag1c_build.py (Job 1 Cornerstone truth, Job 2 placement rule + name merge kept) and fixes:
  Defect 1: a company is Cornerstone Client/Former Client/Prospect/Lost on the Cornerstone side ONLY
            if it is in the Cornerstone Connect export or in DT Clients - CSR.xlsx. The old CSR list
            (Client CSR List for David 9.9.25.xlsx) is not truth on its own: a CSR-list-only row goes
            to the Cornerstone verify tab and is never added to Book. A company whose only Cornerstone
            evidence is a folder under Clients Cornerstone PEO (no export/DT CSR backing) gets status
            "Cornerstone (folder only, verify)", Load ready forced to no, and also goes on the verify
            tab.
  Defect 2: the folder walk was using a fuzzy "referr"/"terminat" substring match to decide whether a
            folder was a group wrapper to recurse through. That match both false-positived on real
            company names that happen to contain the word Referral (e.g. "Vet AI - PPG Referral
            Jasmine"), which then had its own admin subfolders ("1. Client Info CornerStone", "1099
            Proposals") scanned in as bogus companies, and false-negatived on typo'd wrapper names
            ("Refferals", "Referaals"), which then got added as a bogus company row themselves. Fix:
            a folder is only ever a group wrapper (recursed through exactly one level, never added as
            its own row) when its name starts with a number and a dot, per David's rule; nothing is
            ever recursed a level deeper than that. A folder whose name is a generic administrative
            word (client info, proposals, previous provider information, census, payroll, docs, forms,
            quotes, copy folders) is dropped outright, at any level, never recursed into either.
  Defect 3: the main-contact picker was taking a "company phone, no named contact" placeholder row
            (inserted ahead of the real GHL/export contacts) as the main contact whenever it had a
            phone, even when a real named person with an email existed for the same company. That
            placeholder is gone (the company phone already has its own Book column); the picker now
            prefers a named person with an email (Cornerstone Connect first for Cornerstone
            companies), then a named person with a phone, and leaves main contact blank otherwise.
  Also: two named companies get merged by hand ("AAMCOR Companies" G&A-lost folder into the AAMCOR
        Inc row; "Vet AI PPG referral" into Vet-AI Inc), each with a placement note. An Atlas One
        folder whose name is an existing company plus a task word ("CIrque Lodge Tax FIllings")
        becomes a note and folder path on that company instead of its own row.
"""
import re, csv, json, sys, html
from pathlib import Path
from collections import defaultdict
import openpyxl
from openpyxl.styles import Font

R = Path("/Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions")
GA_OD = Path("/Users/davidtaylor/Library/CloudStorage/OneDrive-G&APartners")
CS_ROOT = R/"3. Cornerstone PEO"
GA_ROOT = R/"4. G & A Partners"
A1_ROOT = R/"2. A1 Official Docs"
ZOHO = CS_ROOT/"1. CS Sales"/"5. Leads"/"Old PEO Info Leads"/"ZOHO Reports"
ZOHO_CLIENT_INFO = CS_ROOT/"1. CS Sales"/"5. Leads"/"Old PEO Info Leads"/"Zoho client info"

CORNERSTONE_EXPORT = Path.home()/"Downloads"/"cornerstone-book-2026-09-26.json"
# Assumption (AG1d): ~/Downloads became macOS-TCC-blocked to this session mid-run (readable file,
# normal owner/permissions, but EPERM on read/copy/xattr alike -- a folder-level privacy block, not
# a data problem). The export was already read successfully in AG1c and its per-company fields are
# preserved in master-book-v3's own Book/Contacts/Notes sheets (tagged source cornerstone:connect_export
# / "Cornerstone Connect"). Rather than leave Job 1 blocked again (AG1b's failure mode), this run
# falls back to a small cache rebuilt from v3's own already-verified output when Downloads is
# unreadable. Flagged for David at the end -- worth checking Screen Recording/Files-and-Folders
# privacy settings for this session's host app if a future run needs a NEW export.
CORNERSTONE_EXPORT_CACHE_FALLBACK = Path(__file__).parent/"cornerstone-export-cache-from-v3.json"
CORNERSTONE_EXPORT_FOUND = False
CORNERSTONE_EXPORT_USING_V3_CACHE = False
try:
    CORNERSTONE_EXPORT_FOUND = CORNERSTONE_EXPORT.exists()
    if CORNERSTONE_EXPORT_FOUND:
        with CORNERSTONE_EXPORT.open('rb') as _f:
            _f.read(1)
except OSError:
    CORNERSTONE_EXPORT_FOUND = False
if not CORNERSTONE_EXPORT_FOUND and CORNERSTONE_EXPORT_CACHE_FALLBACK.exists():
    CORNERSTONE_EXPORT_FOUND = True
    CORNERSTONE_EXPORT_USING_V3_CACHE = True
    print("Downloads/cornerstone-book-2026-09-26.json unreadable this run (permission denied) -- "
          "using the cache rebuilt from master-book-v3's own verified export fields instead.",
          file=sys.stderr)

CLIENT_STATUSES = {"Cornerstone Client", "G&A Client", "Atlas One Client"}

def norm_name(name: str) -> str:
    n = name.lower()
    n = re.sub(r'\.(xlsx|csv|docx|pdf|pptx|gsheet|txt|md|pptm)$', '', n)
    n = re.sub(r'\b(llc|l l c|inc|incorporated|corp|corporation|co|company|ltd|pllc|pc|dba|the|holdings|group)\b', ' ', n)
    n = re.sub(r'[^a-z0-9]+', ' ', n)
    n = re.sub(r'\s+', ' ', n).strip()
    return n

def loose_key(name: str) -> str:
    """Looser than norm_name: also drops referral/person/'s corp' tags tacked onto a folder name,
    per the brief's own AAMCOR example. Used only to find merge candidates, not as the primary key."""
    n = norm_name(name)
    n = re.sub(r'\b\w+\s+\w+\s+referr?al\b', ' ', n)
    n = re.sub(r'\breferr?al\b', ' ', n)
    n = re.sub(r'\bs[- ]?corp\b', ' ', n)
    n = re.sub(r'\bdba\b', ' ', n)
    n = re.sub(r'\s+', ' ', n).strip()
    return n

# ---------- Defect 2: folder classification (group wrapper vs. real company vs. junk) ----------
# David's rule: a company folder is an immediate child of a Clients/Quotes root, or of a group
# wrapper directly under that root (a name that starts with a number and a dot). Never a folder
# nested inside a company folder. A folder whose name is a generic administrative word is dropped
# outright, never recursed into, at any level.
NUMBER_DOT_RE = re.compile(r'^\d+\.\s*')
_JUNK_WORD_PATTERNS = [
    r'\bclient\s*info\b', r'\bproposals?\b', r'\bprevious\s*provider(\s*information)?\b',
    r'\bcensus\b', r'\bpayroll\b', r'\bdocs?\b', r'\bforms?\b', r'\bquotes?\b',
    r'\bcopy\s*folders?\b',
]

def _collapse_repeats(s: str) -> str:
    """Collapse runs of the same character to one, so typo'd wrapper names (Refferals, Referaals)
    still match a fuzzy 'referral' check without a fragile hand-built typo list."""
    return re.sub(r'(.)\1+', r'\1', s)

def is_generic_junk_folder(name: str) -> bool:
    stripped = NUMBER_DOT_RE.sub('', name.lower()).strip()
    if any(re.search(p, stripped) for p in _JUNK_WORD_PATTERNS):
        return True
    return False

def is_group_wrapper_name(name: str) -> bool:
    """Only a digit-and-dot prefix makes a folder a wrapper. This intentionally drops the old
    fuzzy 'referr'/'terminat' substring check, which false-positived on real company names that
    happen to contain the word Referral and false-negatived on typo'd wrapper names."""
    return bool(NUMBER_DOT_RE.match(name.strip()))

def wrapper_status_override(name: str):
    """A digit-dot wrapper named for terminated/former clients forces that status on its real
    children, typo-tolerant via the same collapse-repeats trick."""
    stripped = NUMBER_DOT_RE.sub('', name.lower()).strip()
    if 'terminat' in _collapse_repeats(stripped):
        return "Former Client"
    return None

dropped_junk_examples = []
dropped_junk_count = 0

def add_client_or_quote_folder(root, peo, default_status, source_tag, extra_status_by_group=None):
    """David's 2-level rule: root's immediate children are companies, except a digit-dot wrapper
    (optionally in extra_status_by_group for a per-group status override) is recursed through
    exactly one level for its real company children and never added as a row itself. Anything
    generic-junk-worded is dropped outright, at any level, never recursed into."""
    global dropped_junk_count
    if not root.exists():
        return
    for d in root.iterdir():
        if not d.is_dir():
            continue
        if is_generic_junk_folder(d.name):
            dropped_junk_count += 1
            if len(dropped_junk_examples) < 10:
                dropped_junk_examples.append(str(d))
            continue
        if is_group_wrapper_name(d.name):
            group_status = None
            if extra_status_by_group is not None:
                group_status = extra_status_by_group.get(d.name)
            status_here = group_status or wrapper_status_override(d.name) or default_status
            for sub in d.iterdir():
                if not sub.is_dir():
                    continue
                if is_generic_junk_folder(sub.name) or is_group_wrapper_name(sub.name):
                    dropped_junk_count += 1
                    if len(dropped_junk_examples) < 10:
                        dropped_junk_examples.append(str(sub))
                    continue
                leaf_status = wrapper_status_override(d.name) or status_here
                add_company(sub.name, leaf_status, peo, sub, f"{source_tag}/{d.name}")
            continue
        add_company(d.name, default_status, peo, d, source_tag)

companies = {}

def add_company(raw_name, status, peo, folder_path, source, contract_type=None, extra=None):
    raw_name = raw_name.strip()
    if not raw_name:
        return None
    key = norm_name(raw_name)
    if not key:
        return None
    if key not in companies:
        companies[key] = {
            "company": raw_name, "statuses": set(), "peos": set(), "folders": set(),
            "sources": set(), "contract_types": set(), "extra": {},
            "folder_statuses": set(), "folder_peos": set(), "placement_notes": [],
        }
    c = companies[key]
    c["statuses"].add(status)
    if peo:
        c["peos"].add(peo)
    if folder_path:
        c["folders"].add(str(folder_path))
    c["sources"].add(source)
    if contract_type:
        c["contract_types"].add(contract_type)
    if extra:
        c["extra"].update({k: v for k, v in extra.items() if v})
    if len(raw_name) > len(c["company"]):
        c["company"] = raw_name
    return key

# ---------- 1. Cornerstone clients (folder truth) ----------
# NOTE (Defect 1): folder truth alone is no longer enough for Book status -- everything added here
# gets checked against the Cornerstone Connect export / DT Clients - CSR.xlsx after Job 1 runs below,
# and downgraded to "Cornerstone (folder only, verify)" if neither backs it up.
CS_CLIENTS = CS_ROOT/"4. Clients Cornerstone PEO"
CS_CLIENT_SUBGROUPS_TERMINATED = {
    "0. Terminated clients": "Former Client",
    "00. P and C Only clients": None, "2. Hoffman accounts": None, "3. PPG Clients": None,
    "4. Z Works Clients": None, "5. The Guiden Group": None, "6. Apex Tax Services": None,
    "6. Family Businesses": "Cornerstone Client",
}
add_client_or_quote_folder(CS_CLIENTS, "Cornerstone", "Cornerstone Client", "folder:cornerstone_clients",
                            extra_status_by_group=CS_CLIENT_SUBGROUPS_TERMINATED)

# ---------- 2. Cornerstone quotes ----------
CS_QUOTES = CS_ROOT/"3. Quotes_Cornerstone_PEO"
SKIP_QUOTE_DIRS = {"1. Copy Folders to New Quote", "Quotes Cornerstone"}
for d in CS_QUOTES.iterdir():
    if not d.is_dir() or d.name in SKIP_QUOTE_DIRS or is_generic_junk_folder(d.name):
        continue
    if d.name == "0. Lost Prospects":
        for sub in d.iterdir():
            if sub.is_dir() and not (is_generic_junk_folder(sub.name) or is_group_wrapper_name(sub.name)):
                add_company(sub.name, "Lost", "Cornerstone", sub, "folder:cornerstone_quotes/lost")
    elif d.name.startswith("00."):
        for sub in d.iterdir():
            if not sub.is_dir() or is_generic_junk_folder(sub.name):
                continue
            if sub.name.startswith("0."):
                for leaf in sub.iterdir():
                    if leaf.is_dir() and not (is_generic_junk_folder(leaf.name) or is_group_wrapper_name(leaf.name)):
                        add_company(leaf.name, "Lost", "Cornerstone", leaf, "folder:cornerstone_quotes/pc_lost")
            elif not is_group_wrapper_name(sub.name):
                add_company(sub.name, "Prospect open", "Cornerstone", sub, "folder:cornerstone_quotes/pc_only")
    else:
        add_company(d.name, "Prospect open", "Cornerstone", d, "folder:cornerstone_quotes/open")

# ---------- 3. Cornerstone broker partners ----------
CS_SALES = CS_ROOT/"1. CS Sales"
bp = CS_SALES/"Broker partners"
if bp.exists():
    for d in bp.iterdir():
        if d.is_dir() and not is_generic_junk_folder(d.name):
            add_company(d.name, "Broker or Partner", None, d, "folder:cornerstone_broker_partners")

# ---------- 4. G&A clients ----------
GA_CLIENTS = GA_ROOT/"5. Clients_G_and_A_Partners"
GA_SUBGROUPS = {"1. Hoffman clients", "1. PPG Clients"}
add_client_or_quote_folder(GA_CLIENTS, "G&A", "G&A Client", "folder:ga_clients")

# ---------- 5. G&A quotes/lost ----------
GA_QUOTES = GA_ROOT/"5. Quotes G_and_A_Partners"
SKIP_GA_QUOTE_DIRS = {"1 Copy Folders to New Quote"}
for d in GA_QUOTES.iterdir():
    if not d.is_dir() or d.name in SKIP_GA_QUOTE_DIRS or is_generic_junk_folder(d.name):
        continue
    if d.name == "Lost_Prospects":
        for sub in d.iterdir():
            if sub.is_dir() and not (is_generic_junk_folder(sub.name) or is_group_wrapper_name(sub.name)):
                add_company(sub.name, "Lost", "G&A", sub, "folder:ga_quotes/lost")
    else:
        add_company(d.name, "Prospect open", "G&A", d, "folder:ga_quotes/open")

# ---------- 6. A1 clients + quotes ----------
# Also: an Atlas One folder whose name is an existing company plus a task word (e.g. "CIrque Lodge
# Tax FIllings") is not its own row -- it becomes a note and a folder path on that existing company.
# Named case only (not a general prefix heuristic): the tree is small (8 client + 10 quote folders)
# and a fuzzy prefix match risks folding in a real distinct company (e.g. "Arkus Advisory LLC US
# PPG" already exists as its own row from the Cornerstone quotes tree and is NOT a task-word variant).
A1_TASK_WORD_FOLDERS = {"cirque lodge tax fillings": "cirque lodge"}
A1_PC = A1_ROOT/"1. A1 Solutions prospect_Client"
A1_CLIENTS = A1_PC/"2. Clients_A1"
A1_QUOTES = A1_PC/"3. Quotes_A1"
a1_task_word_folded = 0

def _add_a1_folder(d, status, source_tag):
    global a1_task_word_folded
    if is_generic_junk_folder(d.name):
        return
    task_target = A1_TASK_WORD_FOLDERS.get(d.name.strip().lower())
    if task_target:
        target_key = norm_name(task_target)
        if target_key in companies:
            tc = companies[target_key]
            tc["folders"].add(str(d))
            tc["sources"].add(source_tag)
            tc["placement_notes"].append(f"Atlas One folder: {d.name}")
            a1_task_word_folded += 1
            return
    add_company(d.name, status, "Atlas One", d, source_tag)

if A1_CLIENTS.exists():
    for d in A1_CLIENTS.iterdir():
        if d.is_dir():
            _add_a1_folder(d, "Atlas One Client", "folder:a1_clients")
if A1_QUOTES.exists():
    for d in A1_QUOTES.iterdir():
        if d.is_dir():
            _add_a1_folder(d, "Prospect open", "folder:a1_quotes")
print(f"A1 task-word folders folded into an existing company: {a1_task_word_folded}", file=sys.stderr)

# ---------- 7. A1 brokers/vendors ----------
BV = A1_ROOT/"4. Brokers_Vendors A1 Solutions"
for sub in ["09_Vendor_Partners", "10_Broker_and_Partner_Docs"]:
    p = BV/sub
    if p.exists():
        for d in p.iterdir():
            if d.is_dir() and not is_generic_junk_folder(d.name):
                status = "Vendor" if sub == "09_Vendor_Partners" else "Broker or Partner"
                add_company(d.name, status, None, d, f"folder:a1_{sub}")

print(f"companies after folder pass: {len(companies)}", file=sys.stderr)

for c in companies.values():
    c["folder_statuses"] = set(c["statuses"])
    c["folder_peos"] = set(p for p in c["peos"] if p)

# ================== JOB 2: David's placement rule + name-variant merge ==================
# A HARD conflict only when BOTH sides have a real client status (client folder), not a quote/lost
# folder. When one side is a client and the other is a quote/lost folder for a DIFFERENT PEO, the
# client side wins; record the other side as history in a note line, keep both folder paths.
before_placement = len(companies)
resolved_by_placement = 0
for key, c in companies.items():
    peos_present = c["folder_peos"]
    if len(peos_present) < 2:
        continue
    client_peos = set()
    non_client_peos = set()
    for p in peos_present:
        # does this PEO have at least one *client* folder for this company?
        has_client_folder = any(
            (f"folder:{'cornerstone_clients' if p=='Cornerstone' else 'ga_clients' if p=='G&A' else 'a1_clients'}" in s)
            for s in c["sources"]
        )
        if has_client_folder:
            client_peos.add(p)
        else:
            non_client_peos.add(p)
    if len(client_peos) == 1 and non_client_peos:
        winner = next(iter(client_peos))
        for loser in non_client_peos:
            c["placement_notes"].append(f"Also quoted through {loser}, lost")
        resolved_by_placement += 1
        # narrow folder_peos to the real PEO for downstream conflict detection
        c["folder_peos"] = {winner}
        c["folder_statuses"] = {s for s in c["folder_statuses"] if s in CLIENT_STATUSES} or c["folder_statuses"]
print(f"placement rule resolved {resolved_by_placement} companies (client-vs-quote, not a true conflict)", file=sys.stderr)

# name-variant merge: legal-suffix noise + referral/person/"s corp" tags (e.g. "AAMCOR Holdings Inc"
# and "AAMCOR Inc"). Group by loose_key; merge groups of >=2 into the entry with the most folder
# evidence (ties broken by longest name). Guard against noise collisions with a minimum key length.
loose_groups = defaultdict(list)
for key in companies:
    lk = loose_key(companies[key]["company"])
    if len(lk) >= 5:
        loose_groups[lk].append(key)

alias = {}
merged_groups = 0
for lk, keys in loose_groups.items():
    if len(keys) < 2:
        continue
    canon = max(keys, key=lambda k: (len(companies[k]["folders"]), len(companies[k]["company"])))
    for k in keys:
        if k != canon:
            alias[k] = canon
    merged_groups += 1

for k, canon in list(alias.items()):
    if k not in companies:
        continue
    src = companies.pop(k)
    dst = companies[canon]
    dst["statuses"] |= src["statuses"]
    dst["peos"] |= src["peos"]
    dst["folders"] |= src["folders"]
    dst["sources"] |= src["sources"]
    dst["contract_types"] |= src["contract_types"]
    dst["folder_statuses"] |= src["folder_statuses"]
    dst["folder_peos"] |= src["folder_peos"]
    dst["placement_notes"] += src["placement_notes"]
    for kk, vv in src["extra"].items():
        dst["extra"].setdefault(kk, vv)
    if len(src["company"]) > len(dst["company"]):
        dst["company"] = src["company"]

def resolve_key(name):
    k = norm_name(str(name))
    return alias.get(k, k)

print(f"name-variant merge: {merged_groups} groups merged, {len(alias)} rows folded in "
      f"(companies before={before_placement}, after={len(companies)})", file=sys.stderr)

before_fix_total = len(companies)

# ---------- Enrich: G&A CRM Accounts Update.xlsx ----------
ga_crm_path = GA_CLIENTS/"CRM Accounts Update.xlsx"
if ga_crm_path.exists():
    wb = openpyxl.load_workbook(ga_crm_path, read_only=True, data_only=True)
    ws = wb["CRM Accounts Update"]
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0]
    idx = {h: i for i, h in enumerate(header) if h}
    for row in rows[1:]:
        def g(col):
            i = idx.get(col)
            return row[i] if i is not None and i < len(row) else None
        name = g("Account Name")
        if not name:
            continue
        rating = (g("Rating") or "").strip()
        acct_type = (g("Account Type") or "").strip()
        RATING_STATUS = {
            "Active": "G&A Client", "Prospect": "Prospect open",
            "Acquired": "Former Client", "Business Closed": "Former Client",
            "Lost": "Lost", "Not Interested": "Lost",
        }
        status_from_ga = RATING_STATUS.get(rating)
        if not status_from_ga:
            status_from_ga = "Former Client" if acct_type == "They left us" else (
                "G&A Client" if acct_type == "Customer" else "Prospect open")
        key = resolve_key(name)
        if key not in companies:
            add_company(str(name), status_from_ga, "G&A", None, "crm:ga_crm_accounts_update")
            key = resolve_key(name)
        c = companies[key]
        c["statuses"].add(status_from_ga)
        c["sources"].add("crm:ga_crm_accounts_update")
        c["extra"].setdefault("state", g("Billing State"))
        c["extra"].setdefault("employees", g("Employees"))
        c["extra"].setdefault("services", g("Products"))
        c["extra"].setdefault("phone", g("Phone"))
        c["extra"].setdefault("account_type_ga", acct_type)
        c["extra"].setdefault("ga_rating", rating)

print(f"companies after GA CRM enrich: {len(companies)}", file=sys.stderr)

# ================== JOB 1: Cornerstone Connect export is now the truth ==================
CS_FIELDS = [
    "_comm_clientservicesrepresentative_value", "_craff_assignedunderwriter_value",
    "comm_contracttype", "_comm_broker_value", "comm_effectivedate", "comm_employeecount",
    "comm_annualpayrollsize", "_comm_peo_value",
]
SERVICE_FIELDS = [
    ("craff_benefitsstatus", "Benefits"), ("comm_k", "401k"),
    ("craff_timeandattendancestatus", "Time and Attendance"),
    ("craff_backgroundcheckstatus", "Background Check"),
    ("craff_drugscreeningstatus", "Drug Screening"), ("comm_paycard", "Pay Card"),
]

def fv(acct, field):
    return acct.get(f"{field}@OData.Community.Display.V1.FormattedValue")

def raw(acct, field):
    return acct.get(field)

def cornerstone_status(acct):
    accttype = fv(acct, "comm_accounttype") or ""
    stage = fv(acct, "new_accountstage") or ""
    status = fv(acct, "new_accountstatus") or ""
    if accttype in ("Active", "Pending Initial Payroll") or stage in ("Active Client", "Enrollment"):
        return "Cornerstone Client"
    if accttype == "Terminated" or stage == "Terminated Client":
        return "Former Client"
    if stage in ("Sales", "Underwriting") and status != "Lost":
        return "Prospect open"
    if status == "Lost" or (accttype == "Not Onboarded" and stage == "Lost"):
        return "Lost"
    return "Prospect open"

def is_on(val):
    if not val:
        return False
    v = val.lower()
    if v in ("not interested", "not moving forward"):
        return False
    if "active" in v or "interested" in v or v == "yes":
        return True
    return False

export_accounts_by_key = {}
export_account_ids_to_key = {}
export_keys = set()
cs_export_new = 0
cs_export_matched = 0

def strip_html_cs(text):
    if not text:
        return ""
    text = html.unescape(str(text))
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:4000]

cs_export_contacts = defaultdict(list)
cs_export_notes = []  # (key, display, date, source, text)

if CORNERSTONE_EXPORT_FOUND and not CORNERSTONE_EXPORT_USING_V3_CACHE:
    cs_data = json.loads(CORNERSTONE_EXPORT.read_text())
    for acct in cs_data["accounts"]:
        name = acct.get("name")
        if not name:
            continue
        status = cornerstone_status(acct)
        key = resolve_key(name)
        export_keys.add(norm_name(name))
        export_account_ids_to_key[acct["accountid"]] = key
        if key not in companies:
            add_company(str(name), status, "Cornerstone", None, "cornerstone:connect_export")
            key = resolve_key(name)
            cs_export_new += 1
        else:
            cs_export_matched += 1
        c = companies[key]
        c["statuses"].add(status)
        c["peos"].add("Cornerstone")
        c["sources"].add("cornerstone:connect_export")
        export_accounts_by_key[key] = acct

        addr_parts = [raw(acct, "address1_line1"), raw(acct, "address1_city"),
                      raw(acct, "address1_stateorprovince"), raw(acct, "address1_postalcode")]
        address = ", ".join(p.strip().rstrip(",") for p in addr_parts if p)
        services_detail = "; ".join(f"{label} ({fv(acct, field)})" for field, label in SERVICE_FIELDS if is_on(fv(acct, field)))

        c["extra"]["csr"] = fv(acct, "_comm_clientservicesrepresentative_value") or c["extra"].get("csr", "")
        c["extra"]["underwriter"] = fv(acct, "_craff_assignedunderwriter_value") or ""
        c["extra"]["contract_type_cs"] = fv(acct, "comm_contracttype") or ""
        c["extra"]["referral_partner"] = fv(acct, "_comm_broker_value") or ""
        c["extra"]["effective_date"] = fv(acct, "comm_effectivedate") or ""
        c["extra"]["employees"] = raw(acct, "comm_employeecount") or c["extra"].get("employees", "")
        c["extra"]["annual_payroll"] = fv(acct, "comm_annualpayrollsize") or ""
        c["extra"]["cornerstone_entity_code"] = fv(acct, "_comm_peo_value") or c["extra"].get("cornerstone_entity_code", "")
        c["extra"]["dba"] = raw(acct, "comm_dbaname") or c["extra"].get("dba", "")
        c["extra"]["state"] = raw(acct, "address1_stateorprovince") or c["extra"].get("state", "")
        c["extra"]["address"] = address
        c["extra"]["phone"] = raw(acct, "telephone1") or c["extra"].get("phone", "")
        c["extra"]["website"] = raw(acct, "websiteurl") or ""
        c["extra"]["services_cornerstone"] = services_detail
        c["extra"]["client_number"] = raw(acct, "comm_clientnumber") or c["extra"].get("client_number", "")

    print(f"Cornerstone export: {len(cs_data['accounts'])} accounts, "
          f"{cs_export_matched} matched existing companies, {cs_export_new} new companies", file=sys.stderr)

    for ct in cs_data["contacts"]:
        key = export_account_ids_to_key.get(ct.get("acct"))
        if not key:
            continue
        cs_export_contacts[key].append({
            "full_name": ct.get("full") or "", "email": ct.get("email") or "",
            "phone": ct.get("phone") or ct.get("mobile") or "",
            "source": "Cornerstone Connect", "note": ct.get("title") or "",
        })

    for n in cs_data["notes"]:
        key = export_account_ids_to_key.get(n.get("acct"))
        if not key:
            continue
        subj = n.get("subject") or ""
        body = n.get("text") or ""
        text = (subj + ": " + body) if subj and body else (subj or body)
        cs_export_notes.append((key, companies[key]["company"], n.get("date", ""), "Cornerstone Connect", strip_html_cs(text)))

elif CORNERSTONE_EXPORT_FOUND and CORNERSTONE_EXPORT_USING_V3_CACHE:
    # Assumption (AG1d): raw Downloads export unreadable this run -- rebuilt from v3's own already-
    # verified fields (see note at CORNERSTONE_EXPORT_CACHE_FALLBACK above). No accountid linking
    # needed since the cache already resolved everything by company name.
    cs_data = json.loads(CORNERSTONE_EXPORT_CACHE_FALLBACK.read_text())
    for acct in cs_data["accounts"]:
        name = acct.get("name")
        if not name:
            continue
        status = acct.get("status") or "Cornerstone Client"
        key = resolve_key(name)
        export_keys.add(norm_name(name))
        export_account_ids_to_key[name] = key
        if key not in companies:
            add_company(str(name), status, "Cornerstone", None, "cornerstone:connect_export")
            key = resolve_key(name)
            cs_export_new += 1
        else:
            cs_export_matched += 1
        c = companies[key]
        c["statuses"].add(status)
        c["peos"].add("Cornerstone")
        c["sources"].add("cornerstone:connect_export")
        export_accounts_by_key[key] = acct
        for field in ["dba", "cornerstone_entity_code", "contract_type_cs", "csr", "underwriter",
                      "referral_partner", "effective_date", "employees", "annual_payroll", "state",
                      "address", "phone", "website", "services_cornerstone", "client_number"]:
            val = acct.get(field)
            if val:
                c["extra"][field] = val

    print(f"Cornerstone export (v3 cache fallback): {len(cs_data['accounts'])} accounts, "
          f"{cs_export_matched} matched existing companies, {cs_export_new} new companies", file=sys.stderr)

    for ct in cs_data["contacts"]:
        key = export_account_ids_to_key.get(ct.get("company"))
        if not key:
            key = resolve_key(ct.get("company"))
        if key not in companies:
            continue
        cs_export_contacts[key].append({
            "full_name": ct.get("full_name") or "", "email": ct.get("email") or "",
            "phone": ct.get("phone") or "", "source": "Cornerstone Connect", "note": ct.get("note") or "",
        })

    for n in cs_data["notes"]:
        key = export_account_ids_to_key.get(n.get("company"))
        if not key:
            key = resolve_key(n.get("company"))
        if key not in companies:
            continue
        cs_export_notes.append((key, companies[key]["company"], n.get("date", ""), "Cornerstone Connect", strip_html_cs(n.get("text", ""))))

else:
    print("Cornerstone export NOT found (Downloads unreadable and no v3 cache fallback present) -- Job 1 skipped", file=sys.stderr)

# ---------- Cornerstone verify tab: CSR list rows not found in the export ----------
cs_csr_path = CS_CLIENTS/"Client CSR List for David 9.9.25 (1).xlsx"
cs_verify_rows = []
csr_list_total = 0
csr_list_in_export = 0
csr_list_not_in_export = 0
if cs_csr_path.exists():
    wb = openpyxl.load_workbook(cs_csr_path, read_only=True, data_only=True)
    ws = wb["Sheet1"]
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0]
    idx = {h: i for i, h in enumerate(header) if h}
    for row in rows[1:]:
        def g(col):
            i = idx.get(col)
            return row[i] if i is not None and i < len(row) else None
        name = g("CorpLegalName") or g("Name")
        if not name:
            continue
        csr_list_total += 1
        key = resolve_key(name)
        peo_field_raw = (g("PEO") or "").strip() if g("PEO") else ""
        peo_field = "Cornerstone" if peo_field_raw.upper() in {"CCG", "CIP", "CU", "CESV", "CESIV"} or not peo_field_raw else peo_field_raw
        in_export = norm_name(str(name)) in export_keys or key in export_accounts_by_key
        existed_before = key in companies
        if in_export:
            csr_list_in_export += 1
        else:
            csr_list_not_in_export += 1
            cs_verify_rows.append([str(name), g("DbaName") or "", g("ClientNumber") or "", peo_field_raw, g("CEM") or "",
                                    "not in Cornerstone Connect export -- verify current status with Cornerstone before loading"])
        # Defect 1: the CSR list is not truth on its own -- a row that is neither in the export nor
        # already a company from folder/other evidence lives on the verify tab only, never in Book.
        if not in_export and not existed_before:
            continue
        if key not in companies:
            add_company(str(name), "Cornerstone Client", peo_field, None, "list:cs_csr_client_list")
            key = resolve_key(name)
        c = companies[key]
        c["sources"].add("list:cs_csr_client_list")
        c["extra"].setdefault("dba", g("DbaName"))
        c["extra"].setdefault("client_number", g("ClientNumber"))
        c["extra"].setdefault("csr_cem", g("CEM"))
        if peo_field_raw:
            c["extra"].setdefault("cornerstone_entity_code", peo_field_raw)

print(f"Client CSR List: {csr_list_total} rows, {csr_list_in_export} in export, "
      f"{csr_list_not_in_export} -> Cornerstone verify tab", file=sys.stderr)

# ---------- Enrich: DT Clients - CSR.xlsx (a Job 1 truth source too) ----------
dt_csr_path = CS_CLIENTS/"DT Clients - CSR.xlsx"
dt_csr_keys = set()
if dt_csr_path.exists():
    wb = openpyxl.load_workbook(dt_csr_path, read_only=True, data_only=True)
    ws = wb["Sheet1"]
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0]
    idx = {h: i for i, h in enumerate(header) if h}
    for row in rows[1:]:
        def g(col):
            i = idx.get(col)
            return row[i] if i is not None and i < len(row) else None
        name = g("Client Name")
        if not name:
            continue
        dt_csr_keys.add(norm_name(str(name)))
        key = resolve_key(name)
        if key in companies:
            c = companies[key]
            c["extra"].setdefault("csr", g("CSR"))
            c["extra"].setdefault("csr_email", g("CSR Email"))
            c["extra"].setdefault("entity", g("Entity"))
            c["sources"].add("list:dt_clients_csr")

# ---------- Also: two named companies the automatic merge above can't catch (plural/PPG-tag noise
# the norm_name/loose_key suffix stripping doesn't cover). Run here, after Job 1's export/CSR-list
# truth, since "Vet-AI Inc" (unlike "AAMCOR Inc") has no folder of its own and only exists once the
# export has created it. ----------
MANUAL_MERGES = [
    ("AAMCOR Companies", "AAMCOR Inc", "Also quoted through G&A, lost (folder: AAMCOR Companies)"),
    ("Vet AI PPG referral", "Vet-AI Inc", "Also referred through PPG, Atlas One (folder: Vet AI PPG referral)"),
]
manual_merges_applied = 0
for src_name, dst_name, note in MANUAL_MERGES:
    src_key, dst_key = norm_name(src_name), norm_name(dst_name)
    src_key = alias.get(src_key, src_key)
    dst_key = alias.get(dst_key, dst_key)
    if src_key not in companies or dst_key not in companies or src_key == dst_key:
        continue
    src = companies.pop(src_key)
    dst = companies[dst_key]
    dst["statuses"] |= src["statuses"]
    dst["peos"] |= src["peos"]
    dst["folders"] |= src["folders"]
    dst["sources"] |= src["sources"]
    dst["contract_types"] |= src["contract_types"]
    dst["placement_notes"].append(note)
    for kk, vv in src["extra"].items():
        dst["extra"].setdefault(kk, vv)
    alias[src_key] = dst_key
    manual_merges_applied += 1
print(f"manual merges applied: {manual_merges_applied} of {len(MANUAL_MERGES)}", file=sys.stderr)

# ---------- Defect 1: folder-only Cornerstone client rows need verify status, not client status ----------
# A company whose only Cornerstone evidence is a folder under Clients Cornerstone PEO, with no backing
# from the Cornerstone Connect export or DT Clients - CSR.xlsx, is not confirmed. Downgrade it to a
# verify status, force Load ready to no, and also put it on the Cornerstone verify tab.
before_status_count = defaultdict(int)
for c in companies.values():
    for s in c["folder_statuses"]:
        before_status_count[s] += 1
folder_only_verify_added = 0
for key, c in companies.items():
    has_cornerstone_client_folder = any(s.startswith("folder:cornerstone_clients") for s in c["sources"])
    if not has_cornerstone_client_folder:
        continue
    verified = ("cornerstone:connect_export" in c["sources"]) or ("list:dt_clients_csr" in c["sources"])
    if verified:
        continue
    c["statuses"] = {"Cornerstone (folder only, verify)"}
    c["folder_statuses"] = {"Cornerstone (folder only, verify)"}
    c["extra"]["force_no_load"] = "yes"
    cs_verify_rows.append([c["company"], c["extra"].get("dba", ""), c["extra"].get("client_number", ""),
                            c["extra"].get("cornerstone_entity_code", ""), c["extra"].get("csr_cem", ""),
                            "folder only under Clients Cornerstone PEO -- not in Cornerstone Connect export "
                            "or DT Clients - CSR.xlsx, verify current status before loading"])
    folder_only_verify_added += 1
after_status_count = defaultdict(int)
for c in companies.values():
    for s in c["folder_statuses"]:
        after_status_count[s] += 1
print(f"Defect 1: {folder_only_verify_added} folder-only Cornerstone rows downgraded to verify status "
      f"(Cornerstone Client before={before_status_count.get('Cornerstone Client', 0)}, "
      f"after={after_status_count.get('Cornerstone Client', 0)})", file=sys.stderr)

companies_before_zoho_fix = len(companies)

# ---------- Zoho open-deal report (Teamworks/Zoho, never Cornerstone) ----------
deals_path = ZOHO/"Sales+Deals+Report+Customized copy.xlsx"
deal_contacts = defaultdict(list)
zoho_new_companies_deals = 0
if deals_path.exists():
    wb = openpyxl.load_workbook(deals_path, read_only=True, data_only=True)
    ws = wb["Sheet0"]
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0]
    idx = {h: i for i, h in enumerate(header) if h}
    for row in rows[1:]:
        def g(col):
            i = idx.get(col)
            return row[i] if i is not None and i < len(row) else None
        deal = g("Deal Name")
        if not deal:
            continue
        key = resolve_key(deal)
        contact = {
            "full_name": g("Full Name"), "email": g("Email") or g("Contact Email"),
            "phone": g("Phone") or g("Contact Phone"), "stage": g("Stage"),
            "closing_date": g("Closing Date"), "owner": g("Deal Owner"),
        }
        deal_contacts[key].append(contact)
        if key not in companies:
            add_company(str(deal), "Prospect open", None, None, "crm:cs_sales_deals_report")
            key = resolve_key(deal)
            zoho_new_companies_deals += 1
        c = companies[key]
        c["sources"].add("crm:cs_sales_deals_report")

# ---------- Zoho closed deals report -> Teamworks mapping, never Cornerstone ----------
closed_path = ZOHO/"Closed+Deals+Report+for+Gross+to+net.xlsx"
zoho_closed_won_to_ga = 0
zoho_closed_won_to_teamworks = 0
zoho_closed_lost = 0
if closed_path.exists():
    wb = openpyxl.load_workbook(closed_path, read_only=True, data_only=True)
    ws = wb["Sheet0"]
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0]
    idx = {h: i for i, h in enumerate(header) if h}
    for row in rows[1:]:
        def g(col):
            i = idx.get(col)
            return row[i] if i is not None and i < len(row) else None
        name = g("Account Name (Account Name)")
        if not name:
            continue
        stage = (g("Stage") or "")
        lost_stages = {"Closed Lost", "Closed-Lost to Competition", "Closed - Fraud", "Closed Never Ran Payroll"}
        key = resolve_key(name)
        if stage in lost_stages:
            status_from_deal = "Lost"
            zoho_closed_lost += 1
        elif stage == "Closed Won":
            existing = companies.get(key)
            has_ga_folder = bool(existing and "G&A" in existing["folder_peos"])
            ga_active = bool(existing and existing["extra"].get("ga_rating") == "Active")
            if has_ga_folder or ga_active:
                status_from_deal = "G&A Client"
                zoho_closed_won_to_ga += 1
            else:
                status_from_deal = "Former Teamworks client"
                zoho_closed_won_to_teamworks += 1
        else:
            continue
        if key not in companies:
            add_company(str(name), status_from_deal, None, None, "crm:cs_closed_deals")
            key = resolve_key(name)
        c = companies[key]
        c["statuses"].add(status_from_deal)
        c["sources"].add("crm:cs_closed_deals")
        c["extra"].setdefault("closed_deal_stage", stage)
        c["extra"].setdefault("closed_deal_amount", g("Amount"))

print(f"companies after Zoho/Teamworks fix: {len(companies)} (closed-won->G&A={zoho_closed_won_to_ga}, "
      f"closed-won->Former Teamworks={zoho_closed_won_to_teamworks}, closed-lost={zoho_closed_lost})", file=sys.stderr)

# ---------- GHL snapshot: full contact records ----------
GHL_CSV = Path("/Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit/_INTERNAL (do not share)/GHL Exports/GHL-contacts-for-Cornerstone-CRM-2026-09-24.csv")
ghl_rows = []
ghl_by_key = defaultdict(list)
ghl_by_email = {}
ghl_by_phone = {}
ghl_rows_total = 0

def norm_phone(p):
    if not p:
        return ""
    digits = re.sub(r'\D', '', str(p))
    if len(digits) == 11 and digits.startswith('1'):
        digits = digits[1:]
    return digits

def norm_email(e):
    return (e or "").strip().lower()

def email_domain(e):
    e = norm_email(e)
    return e.split('@')[1] if '@' in e else ""

if GHL_CSV.exists():
    with open(GHL_CSV, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ghl_rows_total += 1
            ghl_rows.append(row)
            company = row.get("Company") or row.get("Legal Business Name")
            if company:
                key = resolve_key(company)
                if key:
                    ghl_by_key[key].append(row)
            em = norm_email(row.get("Email"))
            if em:
                ghl_by_email.setdefault(em, row)
            ph = norm_phone(row.get("Phone"))
            if ph:
                ghl_by_phone.setdefault(ph, row)

print(f"GHL rows: {ghl_rows_total}", file=sys.stderr)

# ---------- consolidate Contacts (one row per person, company, source) ----------
all_contacts = defaultdict(list)

for key, dcs in deal_contacts.items():
    for d in dcs:
        if d["full_name"] or d["email"] or d["phone"]:
            all_contacts[key].append({
                "full_name": d["full_name"] or "", "email": d["email"] or "", "phone": d["phone"] or "",
                "source": "crm:cs_sales_deals_report",
                "note": f"stage={d['stage']} owner={d['owner']}" if d["stage"] or d["owner"] else "",
            })

for key in companies:
    for row in ghl_by_key.get(key, []):
        fn = " ".join(x for x in [row.get("First Name", ""), row.get("Last Name", "")] if x).strip()
        em = row.get("Email", "")
        ph = row.get("Phone", "")
        if fn or em or ph:
            all_contacts[key].append({
                "full_name": fn, "email": em, "phone": ph,
                "source": "ghl:contacts_export", "note": row.get("Job Title", ""),
            })

for key, cts in cs_export_contacts.items():
    all_contacts[key].extend(cts)

def has_email_or_phone(key):
    """A named contact's email/phone, OR (Defect 3 fix) the company phone on its own -- but the
    company phone never wins the main-contact slot, it only keeps a company load-ready."""
    for ct in all_contacts.get(key, []):
        if ct["email"] or ct["phone"]:
            return True
    return bool(companies[key]["extra"].get("phone"))

def pick_main_contact(key):
    """Defect 3: prefer a named person with an email (Cornerstone Connect first for Cornerstone
    companies), then a named person with a phone. No pseudo "company phone" contact is ever
    returned here -- the company phone has its own Book column."""
    contacts = all_contacts.get(key, [])
    named_email = [ct for ct in contacts if ct["full_name"] and ct["email"]]
    if named_email:
        cc = [ct for ct in named_email if ct["source"] == "Cornerstone Connect"]
        return cc[0] if cc else named_email[0]
    named_phone = [ct for ct in contacts if ct["full_name"] and ct["phone"]]
    if named_phone:
        return named_phone[0]
    return None

print(f"companies with >=1 contact (email or phone): {sum(1 for k in companies if has_email_or_phone(k))}", file=sys.stderr)

# ---------- link Zoho notes by Parent ID / Client (company name) ----------
def strip_html(text):
    if not text:
        return ""
    text = html.unescape(str(text))
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:4000]

notes_rows = list(cs_export_notes)  # (key, display, date, source, text) -- Cornerstone Connect notes first
notes_linked = len(cs_export_notes)
notes_unlinked = 0
notes_unlinked_companies = set()

def link_note(parent_name, date, source, text):
    global notes_linked, notes_unlinked
    if not parent_name:
        notes_unlinked += 1
        return
    key = resolve_key(parent_name)
    if key in companies:
        notes_rows.append((key, companies[key]["company"], date, source, strip_html(text)))
        notes_linked += 1
    else:
        notes_unlinked += 1
        notes_unlinked_companies.add(str(parent_name))

na_path = ZOHO_CLIENT_INFO/"Notes_Accounts_2025_10_15.csv"
if na_path.exists():
    with open(na_path, newline='', encoding='utf-8-sig', errors='replace') as f:
        for row in csv.DictReader(f):
            link_note(row.get("Parent ID"), row.get("Created Time", ""), "zoho:notes_accounts", row.get("Note Content", ""))

nc_path = ZOHO_CLIENT_INFO/"Notes_Contacts_2025_10_15.csv"
if nc_path.exists():
    with open(nc_path, newline='', encoding='utf-8-sig', errors='replace') as f:
        for row in csv.DictReader(f):
            link_note(row.get("Client"), row.get("Created Time", ""), "zoho:notes_contacts", row.get("Note Content", ""))

nd_path = ZOHO_CLIENT_INFO/"Notes_Deals_2025_10_15.xlsx"
if nd_path.exists():
    wb = openpyxl.load_workbook(nd_path, read_only=True, data_only=True)
    ws = wb["Sheet0"]
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0]
    idx = {h: i for i, h in enumerate(header) if h}
    for row in rows[1:]:
        def g(col):
            i = idx.get(col)
            return row[i] if i is not None and i < len(row) else None
        link_note(g("Parent ID"), g("Created Time"), "zoho:notes_deals", g("Note Content"))

notes_rows.sort(key=lambda r: (r[1].lower(), str(r[2])))
print(f"notes linked: {notes_linked} (of which Cornerstone Connect: {len(cs_export_notes)}), "
      f"notes unlinked (no matching company): {notes_unlinked}", file=sys.stderr)

# ---------- Conflicts: dual-PEO (after placement rule + merge) ----------
# A true conflict requires CLIENT folder evidence on BOTH sides (folder_peos, already narrowed to
# one PEO by the placement-rule pass above whenever one side was only a quote/lost folder). For
# whatever is left, the Cornerstone export / DT Clients - CSR.xlsx decides: if either verified this
# company as a real Cornerstone account, Cornerstone wins and the G&A side is recorded as history;
# otherwise it stays an unresolved conflict for David.
conflicts = []
conflicts_auto_resolved = 0
for key, c in companies.items():
    if not ({"Cornerstone", "G&A"} <= c["folder_peos"]):
        continue
    verified_cornerstone = ("cornerstone:connect_export" in c["sources"]) or ("list:dt_clients_csr" in c["sources"])
    if verified_cornerstone:
        c["placement_notes"].append("Also quoted through G&A, lost (Cornerstone confirmed by Cornerstone Connect export or DT Clients - CSR list)")
        c["folder_peos"] = {"Cornerstone"}
        conflicts_auto_resolved += 1
    else:
        conflicts.append(c)

hard_conflicts = conflicts  # every remaining one is real: client folder evidence on both sides
soft_conflicts = []
print(f"dual-PEO conflicts after placement rule: {len(conflicts)} unresolved "
      f"({conflicts_auto_resolved} auto-resolved to Cornerstone by export/DT CSR truth)", file=sys.stderr)

# ---------- GHL match cascade: email -> phone -> email domain -> name ----------
def ghl_match(key, c):
    for ct in all_contacts.get(key, []):
        em = norm_email(ct["email"])
        if em and em in ghl_by_email:
            return "email", ghl_by_email[em]
    for ct in all_contacts.get(key, []):
        ph = norm_phone(ct["phone"])
        if ph and ph in ghl_by_phone:
            return "phone", ghl_by_phone[ph]
    domains = {email_domain(ct["email"]) for ct in all_contacts.get(key, []) if ct["email"]}
    domains.discard("")
    if domains:
        for row in ghl_rows:
            if email_domain(row.get("Email", "")) in domains:
                return "email domain", row
    if ghl_by_key.get(key):
        return "name", ghl_by_key[key][0]
    return None, None

ghl_match_method_counts = defaultdict(int)
for key, c in companies.items():
    method, row = ghl_match(key, c)
    if row:
        c["extra"]["in_ghl"] = "yes"
        c["extra"]["ghl_contact_id"] = row.get("GHL Contact ID", "")
        c["extra"]["ghl_match_method"] = method
        ghl_match_method_counts[method] += 1
    else:
        c["extra"]["in_ghl"] = "no"
        c["extra"]["ghl_match_method"] = ""
        ghl_match_method_counts["none"] += 1

print(f"GHL match methods: {dict(ghl_match_method_counts)}", file=sys.stderr)

# ---------- Write outputs ----------
OUT_DIR = Path(sys.argv[1])
OUT_DIR.mkdir(parents=True, exist_ok=True)
wb = openpyxl.Workbook()
ws_book = wb.active
ws_book.title = "Book"
headers = ["Company", "DBA", "Status", "PEO", "Cornerstone entity code", "Contract type", "CSR",
           "Underwriter", "Referral partner", "Effective date", "Employees", "Annual payroll",
           "State", "Address", "Phone", "Website", "Services", "Main contact name",
           "Main contact email", "Main contact phone", "Main contact title", "Other contacts count",
           "Notes count", "Latest note date", "Latest note (one line)", "Placement note",
           "Folder path(s)", "Sources", "In GHL today", "GHL match method", "GHL Contact ID",
           "Load ready", "Proposed GHL action", "Client Number"]
ws_book.append(headers)
for cell in ws_book[1]:
    cell.font = Font(bold=True)

def status_priority(statuses):
    order = ["Cornerstone Client", "G&A Client", "Atlas One Client", "Former Client", "Former Teamworks client",
             "Prospect open", "Lost", "Lead", "Broker or Partner", "Vendor",
             "Cornerstone (folder only, verify)"]
    for o in order:
        if o in statuses:
            return o
    return next(iter(statuses)) if statuses else ""

needs_contact_rows = []
load_ready_count = 0

company_notes = defaultdict(list)
for key, disp, date, source, text in notes_rows:
    company_notes[key].append((date, source, text))

rows_written = 0
for key in sorted(companies, key=lambda k: companies[k]["company"].lower()):
    c = companies[key]
    status = status_priority(c["folder_statuses"]) if c["folder_statuses"] else status_priority(c["statuses"])
    peo = ",".join(sorted(c["folder_peos"])) if c["folder_peos"] else (",".join(sorted(p for p in c["peos"] if p)) or "none")
    contacts_for_company = all_contacts.get(key, [])
    main_contact = pick_main_contact(key)
    in_ghl = c["extra"].get("in_ghl", "no")
    ghl_id = c["extra"].get("ghl_contact_id", "")
    ghl_method = c["extra"].get("ghl_match_method", "")
    load_ready = "no" if c["extra"].get("force_no_load") == "yes" else ("yes" if has_email_or_phone(key) else "no")
    if load_ready == "yes":
        load_ready_count += 1
    else:
        needs_contact_rows.append(c["company"])
    if status in ("Broker or Partner", "Vendor"):
        proposed = "skip"
    elif load_ready == "no":
        proposed = "skip - needs contact"
    else:
        proposed = "update" if in_ghl == "yes" else "create"
    my_notes = sorted(company_notes.get(key, []), key=lambda x: str(x[0]))
    latest_note = my_notes[-1] if my_notes else None
    services = c["extra"].get("services_cornerstone") or c["extra"].get("services", "")
    ws_book.append([
        c["company"], c["extra"].get("dba", ""), status, peo,
        c["extra"].get("cornerstone_entity_code", ""), c["extra"].get("contract_type_cs", ""),
        c["extra"].get("csr", ""), c["extra"].get("underwriter", ""), c["extra"].get("referral_partner", ""),
        c["extra"].get("effective_date", ""), c["extra"].get("employees", ""), c["extra"].get("annual_payroll", ""),
        c["extra"].get("state", ""), c["extra"].get("address", ""), c["extra"].get("phone", ""),
        c["extra"].get("website", ""), services,
        main_contact["full_name"] if main_contact else "",
        main_contact["email"] if main_contact else "",
        main_contact["phone"] if main_contact else "",
        "",
        max(0, len(contacts_for_company) - (1 if main_contact else 0)),
        len(my_notes),
        str(latest_note[0]) if latest_note else "",
        latest_note[2][:300] if latest_note else "",
        "; ".join(c["placement_notes"]),
        "; ".join(sorted(c["folders"]))[:2000],
        "; ".join(sorted(c["sources"])),
        in_ghl, ghl_method, ghl_id, load_ready, proposed,
        c["extra"].get("client_number", ""),
    ])
    rows_written += 1

ws_conflicts = wb.create_sheet("Conflicts")
ws_conflicts.append(["Company", "Confidence", "PEOs found", "Statuses found", "Folder paths", "Sources"])
for c in sorted(hard_conflicts, key=lambda x: x["company"].lower()):
    ws_conflicts.append([c["company"], "HARD (client folder evidence both sides, not resolved by export/DT CSR)",
                          ",".join(sorted(p for p in c["peos"] if p)), ",".join(sorted(c["statuses"])),
                          "; ".join(sorted(c["folders"]))[:2000], ", ".join(sorted(c["sources"]))])

ws_contacts = wb.create_sheet("Contacts")
ws_contacts.append(["Company", "Full Name", "Email", "Phone", "Source", "Note"])
for key in sorted(companies, key=lambda k: companies[k]["company"].lower()):
    for ct in all_contacts.get(key, []):
        ws_contacts.append([companies[key]["company"], ct["full_name"], ct["email"], ct["phone"], ct["source"], ct["note"]])

ws_notes = wb.create_sheet("Notes")
ws_notes.append(["Company", "Date", "Source", "Text"])
for key, disp, date, source, text in notes_rows:
    ws_notes.append([disp, str(date) if date else "", source, text])

ws_needs = wb.create_sheet("Needs contact")
ws_needs.append(["Company", "Status", "PEO", "Sources", "Note"])
for key in sorted(companies, key=lambda k: companies[k]["company"].lower()):
    c = companies[key]
    if not has_email_or_phone(key):
        status = status_priority(c["folder_statuses"]) if c["folder_statuses"] else status_priority(c["statuses"])
        peo = ",".join(sorted(c["folder_peos"])) if c["folder_peos"] else (",".join(sorted(p for p in c["peos"] if p)) or "none")
        ws_needs.append([c["company"], status, peo, "; ".join(sorted(c["sources"])), "name only, not load ready, never created in GHL"])

ws_verify = wb.create_sheet("Cornerstone verify")
ws_verify.append(["Company (CSR list)", "DBA", "Client Number", "Entity code", "CEM", "Load ready", "Note"])
for row in cs_verify_rows:
    ws_verify.append([row[0], row[1], row[2], row[3], row[4], "no", row[5]])

ws_sources = wb.create_sheet("Sources")
ws_sources.append(["Source key", "Description", "Row/company count"])
source_counts = defaultdict(int)
for c in companies.values():
    for s in c["sources"]:
        source_counts[s] += 1
for s, n in sorted(source_counts.items()):
    ws_sources.append([s, "", n])
ws_sources.append(["zywave_prospects_cold_list", "Prospects Zywave.xlsx cold call vendor list, NOT expanded into Book", 8030])
ws_sources.append(["icloud_zoho_information", "iCloud ZOHO information Contacts/Leads files - still blocked (permission denied), not read this run", 0])
if CORNERSTONE_EXPORT_USING_V3_CACHE:
    cs_export_source_note = (f"~/Downloads/cornerstone-book-2026-09-26.json - UNREADABLE this run "
                              f"(macOS permission denied), used cache rebuilt from v3's own verified "
                              f"export fields instead, {len(cs_data['accounts'])} accounts")
elif CORNERSTONE_EXPORT_FOUND:
    cs_export_source_note = f"~/Downloads/cornerstone-book-2026-09-26.json - found, {len(cs_data['accounts'])} accounts"
else:
    cs_export_source_note = "~/Downloads/cornerstone-book-2026-09-26.json - MISSING"
ws_sources.append(["cornerstone_connect_export", cs_export_source_note,
                   len(cs_data['accounts']) if CORNERSTONE_EXPORT_FOUND else 0])

out_xlsx = OUT_DIR / "master-book-v4-2026-09-26.xlsx"
wb.save(out_xlsx)
print(f"wrote {out_xlsx} rows={rows_written}")

summary = {
    "total_companies": rows_written,
    "by_status": {},
    "by_peo": {},
    "conflicts_total": len(conflicts),
    "conflicts_hard": len(hard_conflicts),
    "conflicts_soft": 0,
    "conflicts_auto_resolved_by_cornerstone_truth": conflicts_auto_resolved,
    "ghl_matched": sum(1 for c in companies.values() if c["extra"].get("in_ghl") == "yes"),
    "ghl_unmatched": sum(1 for c in companies.values() if c["extra"].get("in_ghl") == "no"),
    "ghl_match_methods": dict(ghl_match_method_counts),
    "load_ready": load_ready_count,
    "needs_contact": len(needs_contact_rows),
    "notes_linked": notes_linked,
    "notes_linked_cornerstone_connect": len(cs_export_notes),
    "notes_unlinked": notes_unlinked,
    "notes_unlinked_sample": sorted(notes_unlinked_companies)[:20],
    "zoho_closed_won_to_ga": zoho_closed_won_to_ga,
    "zoho_closed_won_to_former_teamworks": zoho_closed_won_to_teamworks,
    "zoho_closed_lost": zoho_closed_lost,
    "zoho_new_companies_from_open_deals": zoho_new_companies_deals,
    "cornerstone_export_found": CORNERSTONE_EXPORT_FOUND,
    "cornerstone_export_accounts": len(cs_data["accounts"]) if CORNERSTONE_EXPORT_FOUND else 0,
    "cornerstone_export_new_companies": cs_export_new,
    "cornerstone_export_matched_companies": cs_export_matched,
    "csr_list_total": csr_list_total,
    "csr_list_in_export": csr_list_in_export,
    "csr_list_not_in_export_verify": csr_list_not_in_export,
    "placement_rule_resolved": resolved_by_placement,
    "name_variant_merge_groups": merged_groups,
    "name_variant_merge_rows_folded": len(alias),
    "defect1_folder_only_verify_added": folder_only_verify_added,
    "defect1_cornerstone_client_before": before_status_count.get("Cornerstone Client", 0),
    "defect1_cornerstone_client_after": after_status_count.get("Cornerstone Client", 0),
    "defect1_cornerstone_verify_rows_total": len(cs_verify_rows),
    "defect2_dropped_junk_folder_count": dropped_junk_count,
    "defect2_dropped_junk_folder_examples": dropped_junk_examples,
    "also_manual_merges_applied": manual_merges_applied,
    "also_a1_task_word_folded": a1_task_word_folded,
}
for c in companies.values():
    s = status_priority(c["folder_statuses"]) if c["folder_statuses"] else status_priority(c["statuses"])
    summary["by_status"][s] = summary["by_status"].get(s, 0) + 1
    p = ",".join(sorted(c["folder_peos"])) if c["folder_peos"] else (",".join(sorted(x for x in c["peos"] if x)) or "none")
    summary["by_peo"][p] = summary["by_peo"].get(p, 0) + 1

(OUT_DIR/"summary-v4-2026-09-26.json").write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))

# ---------- spot check the named companies ----------
print("\n--- SPOT CHECK ---", file=sys.stderr)
for name in ["5G Hearing", "AAMCOR", "Cirque Lodge", "Ibex Plumbing", "Vet-AI", "Vet AI", "Alta Auto Sales"]:
    key = resolve_key(name)
    if key in companies:
        c = companies[key]
        status = status_priority(c["folder_statuses"]) if c["folder_statuses"] else status_priority(c["statuses"])
        peo = ",".join(sorted(c["folder_peos"])) if c["folder_peos"] else (",".join(sorted(p for p in c["peos"] if p)) or "none")
        mc = pick_main_contact(key)
        load_ready = "no" if c["extra"].get("force_no_load") == "yes" else ("yes" if has_email_or_phone(key) else "no")
        print(f"{name} -> key={key} company={c['company']!r} status={status} peo={peo} "
              f"csr={c['extra'].get('csr', '')!r} main_contact={(mc['full_name'], mc['email']) if mc else None} "
              f"load_ready={load_ready} placement_notes={c['placement_notes']} folders={sorted(c['folders'])}",
              file=sys.stderr)
    else:
        print(f"{name} -> NOT FOUND (key={key})", file=sys.stderr)
