#!/usr/bin/env python3
"""Run AG2: load master-book-v4 into GoHighLevel (contacts + notes only).
Reads GHL_PIT from .env. Writes real data -- read BRIEF-AGENT-2026-09-27-AG2.md rules before touching this.
"""
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import openpyxl

REPO = "/Users/davidtaylor/Projects/atlas-one-intake-forms"
MK = "/Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit"
BOOK_PATH = f"{MK}/_INTERNAL (do not share)/Book of Business/master-book-v4-2026-09-26.xlsx"
LOG_PATH = f"{MK}/_INTERNAL (do not share)/Book of Business/ag2-load-log-2026-09-27.csv"

LOCATION_ID = "AzTPxnK2vSUj19jYoDmR"
DAVID_USER_ID = "vTV2wRivyR9f9XWNook3"
API_BASE = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

CF_EMPLOYEE_COUNT = "jhys6ULyKSEL8pxXTdYt"
CF_CURRENT_PAYROLL_PROVIDER = "2Wg0Mpj4wO8GaJjZaqdo"

TAG_IMPORT = "book-import-2026-09"
STATUS_TAG = {
    "Cornerstone Client": "book-cs-client",
    "G&A Client": "book-ga-client",
    "Former Teamworks client": "book-former-teamworks",
    "Former Client": "book-former-client",
    "Prospect open": "book-prospect",
    "Lost": "book-lost",
    "Atlas One Client": "book-atlas-client",
    "Broker or Partner": "book-partner",
    "Vendor": "book-vendor",
}
CLIENT_CURRENT_STATUSES = {"Cornerstone Client", "G&A Client", "Atlas One Client"}

# Rule 7: referral partner domains. peoplepayglobal.com is named explicitly in the brief;
# the rest are every Broker/Partner/Vendor website or email domain found in the Book tab
# and the Atlas_One_Vendor_Partner_Directory.xlsx (Job 2 source). Logged as an Assumption
# in the report: this list is not automatically derived from GHL, it is a static set built
# once at the top of this run.
PARTNER_DOMAINS = {
    "peoplepayglobal.com", "microsoft.com", "one-cfo.com", "simpliverified.com",
    "smartbenefits.co", "deel.com", "bigredjelly.com", "quickbooks.intuit.com",
    "intuit.com", "cornerstonepeo.com", "gnapartners.com", "verohcm.com",
    "rowrowrow.io", "rhinoinsurance.com", "thecfpartners.com", "excelhealthplans.com",
    "amplifiedresourcegroup.com", "redirecthealth.com", "newjourneconsulting.com",
    "hoffmanandcompany.com", "experiencedpayrollpros.com", "apextax.net",
    "goreboot.com",
}


def load_env():
    env = {}
    with open(os.path.join(REPO, ".env")) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


TOKEN = load_env()["GHL_PIT"]

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Version": API_VERSION,
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}


def api(method, path, params=None, body=None, retries=5):
    url = f"{API_BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    data = json.dumps(body).encode() if body is not None else None
    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, headers=HEADERS, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                raw = resp.read().decode()
                return resp.status, (json.loads(raw) if raw else {})
        except urllib.error.HTTPError as e:
            raw = e.read().decode()
            try:
                parsed = json.loads(raw)
            except Exception:
                parsed = {"raw": raw}
            if e.code == 429 and attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            return e.code, parsed
        except urllib.error.URLError:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError("unreachable")


def throttle():
    time.sleep(0.22)  # ~4.5 calls/sec


def normalize_phone(raw):
    if not raw:
        return None
    digits = re.sub(r"[^\d]", "", str(raw))
    if not digits:
        return None
    if len(digits) == 10:
        return "+1" + digits
    if len(digits) == 11 and digits.startswith("1"):
        return "+" + digits
    if str(raw).strip().startswith("+"):
        return str(raw).strip()
    return "+" + digits


def domain_of(email_or_url):
    if not email_or_url:
        return None
    s = str(email_or_url).lower()
    m = re.search(r"@([\w.-]+)", s)
    if m:
        return m.group(1)
    m = re.search(r"([\w-]+\.[a-z]{2,})(?:/|$)", s.replace("http://", "").replace("https://", "").replace("www.", ""))
    if m:
        return m.group(1)
    return None


def parse_address(addr):
    if not addr:
        return None, None, None, None
    parts = [p.strip() for p in str(addr).split(",")]
    if len(parts) >= 4:
        return parts[0], parts[1], parts[2], parts[3]
    if len(parts) == 3:
        return parts[0], parts[1], None, parts[2]
    return addr, None, None, None


def search_by_email(email):
    if not email:
        return None
    status, data = api("GET", "/contacts/search/duplicate", params={"locationId": LOCATION_ID, "email": email})
    throttle()
    if status == 200:
        return data.get("contact")
    return None


def search_by_phone(phone):
    if not phone:
        return None
    status, data = api("GET", "/contacts/search/duplicate", params={"locationId": LOCATION_ID, "number": phone})
    throttle()
    if status == 200:
        return data.get("contact")
    return None


def get_contact(contact_id):
    if not contact_id:
        return None
    status, data = api("GET", f"/contacts/{contact_id}")
    throttle()
    if status == 200:
        return data.get("contact")
    return None


def blank(v):
    return v is None or (isinstance(v, str) and v.strip() == "")


def build_notes_index(wb):
    ws = wb["Notes"]
    idx = {}
    for r in ws.iter_rows(min_row=2, values_only=True):
        company, date, source, text = r
        if not company:
            continue
        idx.setdefault(company, []).append((date, source, text))
    for k in idx:
        idx[k].sort(key=lambda t: (t[0] or ""), reverse=True)
    return idx


def build_contacts_index(wb):
    ws = wb["Contacts"]
    idx = {}
    for r in ws.iter_rows(min_row=2, values_only=True):
        company, name, email, phone, source, note = r
        if not company:
            continue
        idx.setdefault(company, []).append({"name": name, "email": email, "phone": phone, "source": source, "note": note})
    return idx


def build_company_note(row_dict, notes_for_company, extra_note=None):
    lines = [
        f"Status: {row_dict['Status'] or ''}",
        f"PEO: {row_dict['PEO'] or ''}",
        f"Cornerstone entity code: {row_dict['Cornerstone entity code'] or ''}",
        f"CSR: {row_dict['CSR'] or ''}",
        f"Underwriter: {row_dict['Underwriter'] or ''}",
        f"Contract type: {row_dict['Contract type'] or ''}",
        f"Referral partner: {row_dict['Referral partner'] or ''}",
        f"Effective date: {row_dict['Effective date'] or ''}",
        f"Services: {row_dict['Services'] or ''}",
        f"Placement note: {row_dict['Placement note'] or ''}",
        f"Folder path(s): {row_dict['Folder path(s)'] or ''}",
    ]
    if extra_note:
        lines.append(extra_note)
    lines.append("")
    lines.append("Linked notes (newest first):")
    for date, source, text in notes_for_company:
        lines.append(f"[{date}] ({source}) {text}")
    body = "\n".join(lines)
    if len(body) > 60000:
        body = body[:59900] + "\n...(truncated at 60,000 characters)"
    return body


def pick_main_contact(row_dict, contacts_for_company):
    name = row_dict["Main contact name"]
    email = row_dict["Main contact email"]
    phone = row_dict["Main contact phone"]
    extra_note = None
    d = domain_of(email) if email else None
    if email and d in PARTNER_DOMAINS:
        skipped = f"Referral partner contact: {name}, {email}"
        alt = None
        for c in contacts_for_company:
            cd = domain_of(c.get("email"))
            if c.get("email") and cd not in PARTNER_DOMAINS:
                alt = c
                break
        if alt:
            name, email, phone = alt.get("name"), alt.get("email"), alt.get("phone")
        else:
            name, email = None, None
            phone = row_dict["Phone"]
        extra_note = skipped
    return name, email, phone, extra_note


def split_name(name):
    if not name:
        return None, None
    parts = str(name).strip().split()
    if len(parts) == 1:
        return parts[0], None
    return parts[0], " ".join(parts[1:])


def load_csv_log():
    done = set()
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, newline="") as f:
            for row in csv.DictReader(f):
                if row.get("result", "").startswith("ok"):
                    done.add(int(row["row"]))
    return done


def append_log(row_num, company, action, contact_id, result):
    is_new = not os.path.exists(LOG_PATH)
    with open(LOG_PATH, "a", newline="") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(["row", "company", "action", "contact_id", "result"])
        w.writerow([row_num, company, action, contact_id or "", result])


def process_row(row_num, headers, row, notes_idx, contacts_idx, dry_run_label=""):
    row_dict = dict(zip(headers, row))
    company = row_dict["Company"]
    proposed = row_dict["Proposed GHL action"]
    try:
        contacts_for_company = contacts_idx.get(company, [])
        name, email, phone, extra_note = pick_main_contact(row_dict, contacts_for_company)
        phone_norm = normalize_phone(phone) or normalize_phone(row_dict["Phone"])
        first, last = split_name(name)

        existing = None
        if email:
            existing = search_by_email(email)
        if not existing and phone_norm:
            existing = search_by_phone(phone_norm)
        if not existing and row_dict.get("GHL Contact ID"):
            existing = get_contact(row_dict["GHL Contact ID"])

        addr1, city, state, postal = parse_address(row_dict["Address"])
        if not state and row_dict.get("State"):
            state = row_dict["State"]

        status = row_dict["Status"]
        status_tag = STATUS_TAG.get(status)
        tags = [TAG_IMPORT] + ([status_tag] if status_tag else [])
        if status in CLIENT_CURRENT_STATUSES:
            tags.append("client-current")

        custom_fields = []
        employees = row_dict.get("Employees")
        if employees not in (None, ""):
            custom_fields.append({"id": CF_EMPLOYEE_COUNT, "fieldValue": employees})

        note_body = build_company_note(row_dict, notes_idx.get(company, []), extra_note)

        if existing:
            contact_id = existing["id"]
            update_body = {}
            if blank(existing.get("firstName")) and first:
                update_body["firstName"] = first
            if blank(existing.get("lastName")) and last:
                update_body["lastName"] = last
            if blank(existing.get("email")) and email:
                update_body["email"] = email
            if blank(existing.get("phone")) and phone_norm:
                update_body["phone"] = phone_norm
            if blank(existing.get("address1")) and addr1:
                update_body["address1"] = addr1
            if blank(existing.get("city")) and city:
                update_body["city"] = city
            if blank(existing.get("state")) and state:
                update_body["state"] = state
            if blank(existing.get("postalCode")) and postal:
                update_body["postalCode"] = postal
            if blank(existing.get("website")) and row_dict.get("Website"):
                update_body["website"] = row_dict["Website"]
            existing_cf = {cf.get("id"): cf.get("value") for cf in existing.get("customFields", [])}
            fill_cf = [cf for cf in custom_fields if blank(existing_cf.get(cf["id"]))]
            if fill_cf:
                update_body["customFields"] = fill_cf
            if update_body:
                status_code, resp = api("PUT", f"/contacts/{contact_id}", body=update_body)
                throttle()
                if status_code not in (200, 201):
                    return "failed", contact_id, f"update fields failed {status_code}: {json.dumps(resp)[:300]}"
            new_tags = [t for t in tags if t not in (existing.get("tags") or [])]
            if new_tags:
                status_code, resp = api("POST", f"/contacts/{contact_id}/tags", body={"tags": new_tags})
                throttle()
                if status_code not in (200, 201):
                    return "failed", contact_id, f"tags failed {status_code}: {json.dumps(resp)[:300]}"
            status_code, resp = api("POST", f"/contacts/{contact_id}/notes",
                                     body={"body": note_body, "title": "Book of business import 2026-09"})
            throttle()
            if status_code not in (200, 201):
                return "failed", contact_id, f"note failed {status_code}: {json.dumps(resp)[:300]}"
            return "ok-updated", contact_id, "updated"
        else:
            create_body = {"locationId": LOCATION_ID, "assignedTo": DAVID_USER_ID, "tags": tags,
                            "source": "Book of business import 2026-09"}
            if first:
                create_body["firstName"] = first
            elif not email and not phone_norm:
                create_body["firstName"] = company
            if last:
                create_body["lastName"] = last
            if email:
                create_body["email"] = email
            if phone_norm:
                create_body["phone"] = phone_norm
            if addr1:
                create_body["address1"] = addr1
            if city:
                create_body["city"] = city
            if state:
                create_body["state"] = state
            if postal:
                create_body["postalCode"] = postal
            if row_dict.get("Website"):
                create_body["website"] = row_dict["Website"]
            if custom_fields:
                create_body["customFields"] = custom_fields
            if not any(k in create_body for k in ("firstName", "lastName", "email", "phone")):
                return "skipped", None, "no name/email/phone available to create a contact"
            status_code, resp = api("POST", "/contacts/", body=create_body)
            throttle()
            if status_code not in (200, 201):
                return "failed", None, f"create failed {status_code}: {json.dumps(resp)[:300]}"
            contact_id = resp["contact"]["id"]
            status_code, resp = api("POST", f"/contacts/{contact_id}/notes",
                                     body={"body": note_body, "title": "Book of business import 2026-09"})
            throttle()
            if status_code not in (200, 201):
                return "failed", contact_id, f"note failed {status_code}: {json.dumps(resp)[:300]}"
            return "ok-created", contact_id, "created"
    except Exception as e:
        return "failed", None, f"exception: {e}"


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "dryrun10"
    wb = openpyxl.load_workbook(BOOK_PATH, read_only=True, data_only=True)
    ws = wb["Book"]
    headers = [c.value for c in next(ws.iter_rows(min_row=1, max_row=1))]
    all_rows = list(ws.iter_rows(min_row=2, values_only=True))
    notes_idx = build_notes_index(wb)
    contacts_idx = build_contacts_index(wb)

    done = load_csv_log()

    candidates = []
    for i, row in enumerate(all_rows, start=2):
        rd = dict(zip(headers, row))
        if rd["Proposed GHL action"] in ("create", "update"):
            candidates.append((i, row))

    if mode == "dryrun10":
        named = ["AAMCOR", "Cirque Lodge", "Ibex Plumbing", "5G Hearing"]
        picked = []
        for i, row in candidates:
            rd = dict(zip(headers, row))
            if any(n.lower() in (rd["Company"] or "").lower() for n in named):
                picked.append((i, row))
        others = [c for c in candidates if c not in picked]
        picked.extend(others[:10 - len(picked)])
        targets = picked[:10]
    else:
        targets = [c for c in candidates if c[0] not in done]

    print(f"Processing {len(targets)} rows (mode={mode}, total candidates={len(candidates)}, already done={len(done)})")
    for row_num, row in targets:
        rd = dict(zip(headers, row))
        company = rd["Company"]
        result_kind, contact_id, detail = process_row(row_num, headers, row, notes_idx, contacts_idx)
        append_log(row_num, company, rd["Proposed GHL action"], contact_id, f"{result_kind}: {detail}")
        print(f"row {row_num} | {company} | {result_kind} | {contact_id} | {detail[:120]}")


if __name__ == "__main__":
    main()
