#!/usr/bin/env python3
"""Read back the 10 dry-run contacts from GHL and verify fields, tags, DND, notes."""
import json
import os
import sys
import time
import urllib.request

REPO = "/Users/davidtaylor/Projects/atlas-one-intake-forms"
API_BASE = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"


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
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}


def api(method, path):
    req = urllib.request.Request(f"{API_BASE}{path}", headers=HEADERS, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


rows = []
with open(sys.argv[1]) as f:
    import csv
    for r in csv.DictReader(f):
        rows.append(r)

for r in rows:
    cid = r["contact_id"]
    c = api("GET", f"/contacts/{cid}")["contact"]
    notes = api("GET", f"/contacts/{cid}/notes")
    note_list = notes.get("notes", [])
    print("=" * 80)
    print(f"{r['company']} ({r['action']}) -> {cid}")
    print(f"  name: {c.get('firstName')} {c.get('lastName')} | email: {c.get('email')} | phone: {c.get('phone')}")
    print(f"  address: {c.get('address1')}, {c.get('city')}, {c.get('state')} {c.get('postalCode')}")
    print(f"  tags: {c.get('tags')}")
    print(f"  dnd: {c.get('dnd')} dndSettings: {c.get('dndSettings')}")
    print(f"  assignedTo: {c.get('assignedTo')}")
    print(f"  customFields: {c.get('customFields')}")
    print(f"  notes: {len(note_list)} note(s), title(s): {[n.get('title') for n in note_list]}")
    if note_list:
        body = note_list[0].get("body", "")
        print(f"  first note preview (200 chars): {body[:200]!r}")
    time.sleep(0.25)
