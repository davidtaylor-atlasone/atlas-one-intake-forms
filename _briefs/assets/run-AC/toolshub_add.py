#!/usr/bin/env python3
"""Run AC: add entries to the Tools Hub TOOLS array (right after 'const TOOLS = ['). Backs up once.
usage: toolshub_add.py <hub.html> <json file>  rows: [{"cat":..,"name":..,"tag":..,"desc":..,"file":..}, ...]"""
import sys, io, json, os, shutil
hub, rows = sys.argv[1], json.load(open(sys.argv[2]))
s = io.open(hub, encoding='utf-8', newline='').read()
bak_dir = '/Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-13/tools-hub-before'
os.makedirs(bak_dir, exist_ok=True); bak = os.path.join(bak_dir, 'Atlas One — Tools Hub.html')
if not os.path.exists(bak): shutil.copy2(hub, bak)
key = 'const TOOLS = ['; i = s.find(key); assert i > 0
added = ''
for r in rows:
    if r['file'] in s: print('already present:', r['name']); continue
    added += '\n {' + ', '.join('%s:%s' % (k, json.dumps(v, ensure_ascii=False)) for k, v in r.items()) + '},'
s = s[:i + len(key)] + added + s[i + len(key):]
io.open(hub, 'w', encoding='utf-8', newline='').write(s); print('added', added.count('\n'), 'tools')
