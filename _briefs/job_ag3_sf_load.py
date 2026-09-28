#!/usr/bin/env python3
"""Run AG3 Job 2: load Cowork's prepared Salesforce file into GoHighLevel (contacts + one
note per account). Reads GHL_PIT from .env via job_ag2_load. Writes real data in every mode
except `plan` -- read BRIEF-AGENT.md (2026-09-27, AG3 section) before touching this.

Input: sf-load-2026-09-27.json (built by sf_build_load.py, do not rebuild it here).
Reuses job_ag2_load's api/search/note/tag/create/update/DND functions -- does not copy them.
"""
import json
import sys

import job_ag2_load as base

MK = base.MK
SF_LOAD_PATH = f"{MK}/_INTERNAL (do not share)/Book of Business/sf-load-2026-09-27.json"
LOG_PATH = f"{MK}/_INTERNAL (do not share)/Book of Business/sf-load-log-2026-09-27.csv"
NOTE_TITLE = "G&A Salesforce import 2026-09"


def load_rows():
    with open(SF_LOAD_PATH) as f:
        return json.load(f)


def row_key(row):
    # sfContactId is the stable identity for a row across reruns and across book versions.
    return row.get("sfContactId") or f"{row.get('companyName')}|{row.get('email') or row.get('phone')}"


def build_plan(row):
    """Read-only. Rule: search by email; search by phone ONLY when the row has no email --
    this is the AG2 fix for the referral-partner shared-phone false match (see item 6,
    5B USA LLC / Real Eyes). Never falls back to phone when an email is present."""
    email = row.get("email") or None
    phone_norm = base.normalize_phone(row.get("phone")) if row.get("phone") else None

    existing = None
    match_method = None
    if email:
        existing = base.search_by_email(email)
        if existing:
            match_method = "email"
    elif phone_norm:
        existing = base.search_by_phone(phone_norm)
        if existing:
            match_method = "phone"

    custom_fields = []
    employees = row.get("employees")
    if employees not in (None, "", 0):
        custom_fields.append({"id": base.CF_EMPLOYEE_COUNT, "fieldValue": employees})

    note_body = None
    if row.get("isMain") and row.get("note"):
        note_body = base.mask_pii(row["note"])

    return {
        "company": row.get("companyName"), "existing": existing, "match_method": match_method,
        "first": row.get("firstName"), "last": row.get("lastName"), "email": email,
        "phone_norm": phone_norm, "addr1": row.get("address1"), "city": row.get("city"),
        "state": row.get("state"), "postal": row.get("postalCode"), "website": row.get("website"),
        "company_name": row.get("companyName"), "tags": row.get("tags") or [],
        "custom_fields": custom_fields, "note_body": note_body, "dnd_email": bool(row.get("dndEmail")),
    }


def execute_plan(plan, dry_run=False):
    existing = plan["existing"]
    if existing:
        contact_id = existing["id"]
        update_body = {}
        if base.blank(existing.get("firstName")) and plan["first"]:
            update_body["firstName"] = plan["first"]
        if base.blank(existing.get("lastName")) and plan["last"]:
            update_body["lastName"] = plan["last"]
        if base.blank(existing.get("email")) and plan["email"]:
            update_body["email"] = plan["email"]
        if base.blank(existing.get("phone")) and plan["phone_norm"]:
            update_body["phone"] = plan["phone_norm"]
        if base.blank(existing.get("address1")) and plan["addr1"]:
            update_body["address1"] = plan["addr1"]
        if base.blank(existing.get("city")) and plan["city"]:
            update_body["city"] = plan["city"]
        if base.blank(existing.get("state")) and plan["state"]:
            update_body["state"] = plan["state"]
        if base.blank(existing.get("postalCode")) and plan["postal"]:
            update_body["postalCode"] = plan["postal"]
        if base.blank(existing.get("website")) and plan["website"]:
            update_body["website"] = plan["website"]
        if base.blank(existing.get("companyName")) and plan["company_name"]:
            update_body["companyName"] = plan["company_name"]
        existing_cf = {cf.get("id"): cf.get("value") for cf in existing.get("customFields", [])}
        fill_cf = [cf for cf in plan["custom_fields"] if base.blank(existing_cf.get(cf["id"]))]
        if fill_cf:
            update_body["customFields"] = fill_cf

        status1, detail1 = base.update_contact_fields(contact_id, update_body, dry_run=dry_run)
        if status1 == "failed":
            return "failed", contact_id, detail1

        new_tags = [t for t in plan["tags"] if t not in (existing.get("tags") or [])]
        status2, detail2 = base.add_tags(contact_id, new_tags, dry_run=dry_run)
        if status2 == "failed":
            return "failed", contact_id, detail2

        detail3 = "no note (not the account's main row)"
        if plan["note_body"]:
            status3, detail3 = base.post_note_idempotent(contact_id, NOTE_TITLE, plan["note_body"], dry_run=dry_run)
            if status3 == "failed":
                return "failed", contact_id, detail3

        detail4 = "no dnd change"
        if plan["dnd_email"]:
            status4, detail4 = base.set_dnd_email_only(contact_id, dry_run=dry_run)
            if status4 == "failed":
                return "failed", contact_id, detail4

        return ("ok-would-update" if dry_run else "ok-updated"), contact_id, f"{detail1}; {detail2}; {detail3}; {detail4}"
    else:
        create_body = {"locationId": base.LOCATION_ID, "assignedTo": base.DAVID_USER_ID,
                        "tags": plan["tags"], "source": NOTE_TITLE, "companyName": plan["company_name"]}
        for k, v in (("firstName", plan["first"]), ("lastName", plan["last"]), ("email", plan["email"]),
                     ("phone", plan["phone_norm"]), ("address1", plan["addr1"]), ("city", plan["city"]),
                     ("state", plan["state"]), ("postalCode", plan["postal"]), ("website", plan["website"])):
            if v:
                create_body[k] = v
        if plan["custom_fields"]:
            create_body["customFields"] = plan["custom_fields"]

        status1, contact_id, detail1 = base.create_contact(create_body, dry_run=dry_run)
        if status1 == "failed":
            return "failed", None, detail1
        if dry_run:
            note_bit = f"note len={len(plan['note_body'])}" if plan["note_body"] else "no note"
            dnd_bit = "would set dnd-email" if plan["dnd_email"] else "no dnd"
            return "ok-would-create", None, f"{detail1}; {note_bit}; {dnd_bit}"

        detail3 = "no note (not the account's main row)"
        if plan["note_body"]:
            status3, detail3 = base.post_note_idempotent(contact_id, NOTE_TITLE, plan["note_body"], dry_run=dry_run)
            if status3 == "failed":
                return "failed", contact_id, detail3

        detail4 = "no dnd change"
        if plan["dnd_email"]:
            status4, detail4 = base.set_dnd_email_only(contact_id, dry_run=dry_run)
            if status4 == "failed":
                return "failed", contact_id, detail4

        return "ok-created", contact_id, f"{detail1}; {detail3}; {detail4}"


def process_row(row, dry_run=False):
    try:
        plan = build_plan(row)
        return execute_plan(plan, dry_run=dry_run)
    except Exception as e:
        return "failed", None, f"exception: {e}"


def pick_test20(rows):
    picked = []
    by_id = set()

    def take(pred, n):
        c = 0
        for r in rows:
            if c >= n:
                break
            k = row_key(r)
            if k in by_id:
                continue
            if pred(r):
                picked.append(r)
                by_id.add(k)
                c += 1

    take(lambda r: r.get("label") == "Client", 5)
    take(lambda r: "book-sf-touched" in (r.get("tags") or []), 5)
    take(lambda r: "book-sf-intent" in (r.get("tags") or []), 5)
    take(lambda r: r.get("dndEmail"), 5)
    return picked


def main():
    args = sys.argv[1:]
    mode = args[0] if args else "plan"
    plan_n = int(args[1]) if mode == "plan" and len(args) > 1 else 10

    rows = load_rows()
    done = base.load_csv_log(LOG_PATH)

    if mode == "plan":
        targets = rows[:plan_n]
        print(f"PLAN (read-only, writes nothing): {len(targets)} of {len(rows)} rows")
        for row in targets:
            plan = build_plan(row)
            action = "UPDATE existing" if plan["existing"] else "CREATE new"
            match = f" (matched by {plan['match_method']})" if plan["existing"] else ""
            fields = {k: v for k, v in {
                "firstName": plan["first"], "lastName": plan["last"], "email": plan["email"],
                "phone": plan["phone_norm"], "companyName": plan["company_name"],
            }.items() if v}
            note_bit = f"note_len={len(plan['note_body'])}" if plan["note_body"] else "no note (not main row)"
            dnd_bit = " DND-EMAIL" if plan["dnd_email"] else ""
            print(f"{row_key(row)} | {plan['company']} | {action}{match} | fields={fields} | tags={plan['tags']} | {note_bit}{dnd_bit}")
        return

    if mode == "test20":
        targets = pick_test20(rows)
    else:
        targets = [r for r in rows if row_key(r) not in done]

    print(f"Processing {len(targets)} rows (mode={mode}, total={len(rows)}, already done={len(done)})")
    for row in targets:
        k = row_key(row)
        result_kind, contact_id, detail = process_row(row)
        base.append_log(k, row.get("companyName"), "create-or-update", contact_id, f"{result_kind}: {detail}", log_path=LOG_PATH)
        print(f"{k} | {row.get('companyName')} | {result_kind} | {contact_id} | {str(detail)[:160]}")


if __name__ == "__main__":
    main()
