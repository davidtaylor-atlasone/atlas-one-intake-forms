"""AG2 follow up (Cowork, 2026-09-28).
1. Retries the Book rows that failed in the AG2 full load:
   - GHL refused a second contact with a phone another contact already has (related companies, same owner):
     create without the phone, and write the phone plus the other contact's name into the note.
   - bad phone formats: drop the phone.
   - no email, phone or name at all: use the company name as the last name (tag no-contact-name is already on).
2. PeoplePay Global referrals: tag ppg-referral and a pinned-style note "PPG referral" naming the PPG rep(s),
   because every PPG client is worked through the PPG rep, not the client.
Usage: python job_ag2_followup.py plan | run
"""
import sys, re, json, csv, collections
import job_ag2_load as j

PPG_TITLE = "PPG referral"
PPG_RE = re.compile(r"PPG|peoplepay|people pay", re.I)

def last_results():
    res = {}
    for r in csv.DictReader(open(j.LOG_PATH)):
        res[r["company"]] = r
    return res

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "plan"
    dry = mode != "run"
    j.load_env()
    headers, rows, notes_idx, contacts_idx = j.load_book()
    book = {r[headers.index("Company")]: dict(zip(headers, r)) for r in rows if r[headers.index("Company")]}
    last = last_results()
    out = collections.Counter()
    # ---------- 1. retry failures ----------
    FORCE_NEW = {"Black Tree Gaming"}  # was merged onto the Real Eyes contact through an AG1 id; give it its own
    for comp, lr in last.items():
        if (lr["result"].startswith("ok") and comp not in FORCE_NEW) or comp not in book:
            continue
        rd = dict(book[comp])
        if comp in FORCE_NEW:
            rd["GHL Contact ID"] = None
        plan = j.build_plan(rd, notes_idx, contacts_idx)
        if comp in FORCE_NEW and plan["existing"] and plan["existing"]["id"] == "D4hSx5MMWqWu00PPaSuK":
            plan["existing"] = None
        msg = lr["result"]
        extra = []
        m = re.search(r'"contactName": "([^"]*)", "contactId": "([^"]+)", "matchingField": "phone"', msg)
        if m or "duplicated contacts" in msg or "calling code" in msg or "too long to be a phone" in msg:
            if plan["phone_norm"]:
                extra.append(f"Phone on file: {plan['phone_norm']}" + (f" (same number as GHL contact {m.group(1) or 'no name'} {m.group(2)}, a related company)" if m else " (format GHL rejects)"))
            plan["phone_norm"] = None
            if plan["existing"] and m and plan["existing"]["id"] == m.group(2):
                plan["existing"] = None
        if not plan["first"] and not plan["last"] and not plan["email"] and not plan["phone_norm"]:
            plan["last"] = comp
        if extra:
            plan["note_body"] = "\n".join(extra) + "\n\n" + plan["note_body"]
        status, cid, detail = j.execute_plan(plan, dry_run=dry)
        out["retry-" + status] += 1
        print(f"RETRY | {comp} | {status} | {cid} | {detail[:160]}")
        if not dry:
            j.append_log(comp, comp, "retry", cid or "", f"{status}: {detail}")
    # ---------- 2. PPG referrals ----------
    last = last_results()
    def core(n):
        n = re.sub(r"(?i)\b(ppg|referral|referal|people ?pay( global)?|g and a|with cs peo|us|usa|llc|inc|ltd|corp|plc|dba|the|jasmine)\b", " ", str(n))
        n = re.sub(r"[^a-z0-9 ]", " ", n.lower())
        return " ".join(n.split()[:2])
    seen = {}
    for c2, lr2 in last.items():
        if lr2["result"].startswith("ok") and lr2.get("contact_id"):
            seen.setdefault(core(c2), lr2["contact_id"])
    for comp, rd in book.items():
        blob = " ".join(str(rd.get(k) or "") for k in ("Company", "Referral partner", "Folder path(s)", "Sources", "Main contact email"))
        reps = [c for c in contacts_idx.get(comp, []) if "peoplepay" in json.dumps(c, default=str).lower()]
        if not (PPG_RE.search(blob) or reps) or comp in ("PPG", "PeoplePay Global"):
            continue
        lr = last.get(comp)
        if (not lr or not lr["result"].startswith("ok") or not lr["contact_id"]) and core(comp) in seen:
            lr = {"contact_id": seen[core(comp)], "result": "ok"}
            print(f"PPG SAME COMPANY | {comp} -> existing {lr['contact_id']}")
        if not lr or not lr["result"].startswith("ok") or not lr["contact_id"]:
            # PPG referrals are worked through the PPG rep, so a company with no client contact still belongs in GHL
            plan = j.build_plan(dict(rd, **{"GHL Contact ID": None}), notes_idx, contacts_idx)
            if plan["existing"]:
                ex_co = j._norm_co(plan["existing"].get("companyName") or "")
                if ex_co and ex_co != j._norm_co(comp):
                    plan["existing"] = None
            if not (plan["first"] or plan["last"] or plan["email"] or plan["phone_norm"]):
                plan["last"] = comp
            st, cid, det = j.execute_plan(plan, dry_run=dry)
            if st == "failed" and "phone" in (det or ""):
                plan["phone_norm"] = None
                if not (plan["first"] or plan["last"] or plan["email"]):
                    plan["last"] = comp
                st, cid, det = j.execute_plan(plan, dry_run=dry)
            out["ppg-load-" + st] += 1
            print(f"PPG LOAD | {comp} | {st} | {cid} | {(det or '')[:100]}")
            if dry or not cid:
                continue
            j.append_log(comp, comp, "ppg-load", cid, f"{st}: {det}")
            lr = {"contact_id": cid}
            seen[core(comp)] = cid
        who = "; ".join(" ".join(str(x) for x in (c if isinstance(c, (list, tuple)) else c.values()) if x) for c in reps) or "rep not recorded in the book, see the Salesforce or Cornerstone record"
        body = (f"PPG REFERRAL (PeoplePay Global). All communication goes through the PPG sales rep, not the client directly.\n"
                f"PPG rep(s): {who}\nPPG USA line: (212) 424-6015")
        cid = lr["contact_id"]
        s1, d1 = j.add_tags(cid, ["ppg-referral"], dry_run=dry)
        s2, d2 = j.post_note_idempotent(cid, PPG_TITLE, body, dry_run=dry)
        out["ppg-" + s2] += 1
        print(f"PPG | {comp} | {cid} | {s1} | {s2}")
    print(json.dumps(out))

if __name__ == "__main__":
    main()
