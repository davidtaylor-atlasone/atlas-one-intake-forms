"""Cowork 2026-09-28: undo the AG2 rows that were merged into an unrelated contact.
Cause: AG1 recorded a "GHL Contact ID" found by matching the EMAIL DOMAIN (gmail.com, yahoo.com, outlook.com ...),
and the loader fell back to that id when email and phone found nothing. So 40 companies landed on someone else.
Fix per wrong row: create the company's own contact (normal rules, dup-phone retry).
Fix per victim contact: company name, tags and the import note go back to the victim's own company;
address and website that came from a wrong row are cleared.
Usage: python job_ag2_unmerge.py plan | run
"""
import sys, re, json, csv, collections, copy
import job_ag2_load as j

FREE = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com", "msn.com", "live.com",
        "comcast.net", "me.com", "att.net", "q.com", "ymail.com", "sbcglobal.net"}
OUR_TAGS = set(j.STATUS_TAG.values()) | {"book-import-2026-09", "client-current", "no-contact-name", "status-review"}

def dom(e):
    e = str(e or "").lower().strip()
    return e.split("@")[1] if "@" in e else ""

def main():
    dry = (sys.argv[1] if len(sys.argv) > 1 else "plan") != "run"
    j.load_env()
    headers, rows, notes_idx, contacts_idx = j.load_book()
    ix = {h: i for i, h in enumerate(headers)}
    rd = {r[0]: dict(zip(headers, r)) for r in rows if r[0]}
    log = {}
    for r in csv.DictReader(open(j.LOG_PATH)):
        log[r["company"]] = r
    wrong, victims = [], collections.defaultdict(list)
    for comp, d in rd.items():
        gid, meth = d.get("GHL Contact ID"), str(d.get("GHL match method") or "")
        lr = log.get(comp)
        if gid and meth == "email domain" and lr and lr["contact_id"] == gid:
            wrong.append(comp); victims[gid].append(comp)
    out = collections.Counter()
    # ---- victims first: put each back to its own company ----
    for vid, comps in victims.items():
        v = j.get_contact(vid)
        if not v:
            continue
        vemail = str(v.get("email") or "").lower()
        own = next((c for c, d in rd.items() if str(d.get("Main contact email") or "").lower() == vemail and c not in comps), None)
        own_plan = None
        if own:
            dd = dict(rd[own]); dd["GHL Contact ID"] = vid
            own_plan = j.build_plan(dd, notes_idx, contacts_idx)
        upd = {}
        wrong_addr = {j.parse_address(rd[c]["Address"])[0] for c in comps} - {None, ""}
        wrong_site = {str(rd[c].get("Website") or "") for c in comps} - {""}
        cur_co = str(v.get("companyName") or "")
        if cur_co in comps:
            upd["companyName"] = own if own else None
        if v.get("address1") and v.get("address1") in wrong_addr:
            upd.update({"address1": None, "city": None, "state": None, "postalCode": " "})
        if v.get("website") and v.get("website") in wrong_site:
            upd["website"] = None
        want = set(own_plan["tags"]) if own_plan else set()
        drop = [t for t in (v.get("tags") or []) if t in OUR_TAGS and t not in want]
        add = [t for t in want if t not in (v.get("tags") or [])]
        print(f"VICTIM {vid} {v.get('firstName','')} {v.get('lastName','')} own={own} | fix {list(upd)} | drop {drop} | add {add} | wrongly merged {len(comps)}")
        if not dry:
            if upd:
                j.api("PUT", f"/contacts/{vid}", body=upd); j.throttle()
            if drop:
                j.api("DELETE", f"/contacts/{vid}/tags", body={"tags": drop}); j.throttle()
            if add:
                j.add_tags(vid, add)
            for n in j.get_notes(vid) or []:
                if n.get("title") == j.NOTE_TITLE:
                    body = own_plan["note_body"] if own_plan else "This import note belonged to another company and was loaded here by mistake. Nothing to see for this contact."
                    if n.get("body") != body:
                        j.api("PUT", f"/contacts/{vid}/notes/{n['id']}", body={"body": body}); j.throttle()
        out["victims"] += 1
    # ---- wrong rows: give each company its own contact ----
    for comp in wrong:
        d = dict(rd[comp]); d["GHL Contact ID"] = None
        plan = j.build_plan(d, notes_idx, contacts_idx)
        if plan["existing"] and plan["existing"]["id"] in victims:
            plan["existing"] = None
        st, cid, det = j.execute_plan(plan, dry_run=dry)
        m = re.search(r'"contactName": "([^"]*)", "contactId": "([^"]+)", "matchingField": "phone"', det or "")
        if st == "failed" and (m or "phone" in (det or "")):
            plan["note_body"] = f"Phone on file: {plan['phone_norm']} (GHL already has this number on another contact)\n\n" + plan["note_body"]
            plan["phone_norm"] = None
            if not (plan["first"] or plan["last"] or plan["email"]):
                plan["last"] = comp
            st, cid, det = j.execute_plan(plan, dry_run=dry)
        out[st] += 1
        print(f"ROW {comp} | {st} | {cid} | {(det or '')[:120]}")
        if not dry:
            j.append_log(comp, comp, "unmerge", cid or "", f"{st}: {det}")
    print(json.dumps(out))

if __name__ == "__main__":
    main()
