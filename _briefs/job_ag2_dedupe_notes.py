#!/usr/bin/env python3
"""Run AG3 Job 3: find contacts with duplicate import notes (AG2 ran dryrun10 twice, so
the 10 test contacts each got the "Book of business import 2026-09" note added twice).
Default is list only. --apply deletes only the NEWER duplicate(s) of each title, keeps the
oldest, never touches any other note. David runs --apply, not this terminal (GHL write).
"""
import json
import sys

import job_ag2_load as base

TITLES = {"Book of business import 2026-09", "G&A Salesforce import 2026-09"}


def delete_note(contact_id, note_id, dry_run=True):
    if dry_run:
        return "ok-would-delete", f"would delete note {note_id}"
    status_code, resp = base.api("DELETE", f"/contacts/{contact_id}/notes/{note_id}")
    base.throttle()
    if status_code not in (200, 201):
        return "failed", f"delete failed {status_code}: {json.dumps(resp)[:300]}"
    return "ok-deleted", "deleted"


def find_dupes_for_contact(contact_id):
    """Returns {title: [note, ...]} for titles that appear more than once, oldest first."""
    notes = base.get_notes(contact_id)
    by_title = {}
    for n in notes:
        t = n.get("title")
        if t in TITLES:
            by_title.setdefault(t, []).append(n)
    dupes = {}
    for t, ns in by_title.items():
        if len(ns) > 1:
            ns_sorted = sorted(ns, key=lambda n: n.get("createdAt") or n.get("dateAdded") or "")
            dupes[t] = ns_sorted
    return dupes


def load_contact_ids():
    """Contact ids come from the two resumable load logs this run already wrote to, plus
    AG2's original dryrun10 log -- every contact_id any import run has touched."""
    ids = set()
    for path in (
        base.LOG_PATH,
        f"{base.MK}/_INTERNAL (do not share)/Book of Business/sf-load-log-2026-09-27.csv",
    ):
        import os
        if not os.path.exists(path):
            continue
        import csv
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                if row.get("contact_id"):
                    ids.add(row["contact_id"])
    return ids


def main():
    apply = "--apply" in sys.argv
    ids = load_contact_ids()
    print(f"Checking {len(ids)} contact ids from the load logs for duplicate import notes"
          f" (mode={'APPLY -- deletes newer duplicates' if apply else 'list only'})")
    total_dupe_contacts = 0
    total_deleted = 0
    for contact_id in sorted(ids):
        dupes = find_dupes_for_contact(contact_id)
        if not dupes:
            continue
        total_dupe_contacts += 1
        for title, ns in dupes.items():
            keep = ns[0]
            extra = ns[1:]
            print(f"contact {contact_id} | title='{title}' | {len(ns)} notes, keeping oldest {keep.get('id')}, "
                  f"{'deleting' if apply else 'would delete'} {len(extra)} newer")
            for n in extra:
                status, detail = delete_note(contact_id, n["id"], dry_run=not apply)
                print(f"  note {n.get('id')} | {status} | {detail}")
                if status == "ok-deleted":
                    total_deleted += 1
    print(f"Done. Contacts with duplicate import notes: {total_dupe_contacts}."
          f" {'Deleted' if apply else 'Would delete'}: {total_deleted if apply else 'see above'}")


if __name__ == "__main__":
    main()
