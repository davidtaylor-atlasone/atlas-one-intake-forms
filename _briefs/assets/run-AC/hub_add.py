#!/usr/bin/env python3
"""Run AC: add rows to the Master Hub ITEMS array (front of the array so they show first in their category).
usage: hub_add.py <hub.html> <json rows file>   rows: [[cat, name, desc, path, kind], ...]. Backs up the hub once per day."""
import sys, io, json, os, shutil, datetime
hub, rows = sys.argv[1], json.load(open(sys.argv[2]))
s = io.open(hub, encoding='utf-8', newline='').read()
bak_dir = '/Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-13/master-hub-before'
os.makedirs(bak_dir, exist_ok=True)
bak = os.path.join(bak_dir, 'Atlas_One_MASTER_HUB.html')
if not os.path.exists(bak): shutil.copy2(hub, bak)
key = 'var ITEMS=['
i = s.find(key); assert i > 0
added = []
for r in rows:
    if r[3] in s: print('already present:', r[1]); continue
    added.append(json.dumps(r, ensure_ascii=False) + ', ')
s = s[:i + len(key)] + ''.join(added) + s[i + len(key):]
io.open(hub, 'w', encoding='utf-8', newline='').write(s)
print('added', len(added), 'rows to', hub)
