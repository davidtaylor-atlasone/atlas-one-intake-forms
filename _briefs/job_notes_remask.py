"""Cowork 2026-09-28: re-mask SSNs and FEINs in notes already posted by the book and Salesforce loads.
The first mask missed numbers glued to the next word ("98-1916334Owner"). Only notes whose body changes are rewritten.
Usage: python job_notes_remask.py plan | run
"""
import sys, csv, json, collections
import job_ag2_load as j

SF_LOG = j.LOG_PATH.replace("ag2-load-log-2026-09-27.csv", "sf-load-log-2026-09-27.csv")

def main():
    dry = (sys.argv[1] if len(sys.argv) > 1 else "plan") != "run"
    j.load_env()
    ids = set()
    for path in (j.LOG_PATH, SF_LOG):
        try:
            for r in csv.DictReader(open(path)):
                if r.get("contact_id"): ids.add(r["contact_id"])
        except FileNotFoundError:
            pass
    c = collections.Counter()
    for cid in sorted(ids):
        for n in j.get_notes(cid) or []:
            body = n.get("body") or ""
            new = j.mask_pii(body)
            if new == body:
                continue
            c["to_fix"] += 1
            if dry:
                continue
            st, resp = j.api("PUT", f"/contacts/{cid}/notes/{n['id']}", body={"body": new})
            j.throttle()
            c["fixed" if st in (200, 201) else f"failed_{st}"] += 1
            if st not in (200, 201):
                print("FAILED", cid, n["id"], st, json.dumps(resp)[:200])
        c["contacts"] += 1
    print(json.dumps(c))

if __name__ == "__main__":
    main()
