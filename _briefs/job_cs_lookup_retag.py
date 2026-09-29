# Retags GHL contacts whose status changed in the 2026-09-28 Cornerstone CRM lookup.
# Removes old book-status tags and status-review, adds the new status tag (plus client-current
# or removes it). Adds a short note with the reason. Usage: python job_cs_lookup_retag.py plan|run
import sys, json, csv
import job_ag2_load as j
RUN = len(sys.argv) > 1 and sys.argv[1] == 'run'
changed = json.load(open('/tmp/cs_lookup_changed.json'))
why = {}
import openpyxl
wb = openpyxl.load_workbook(j.BOOK_PATH, read_only=True)
rows = list(wb['Book'].iter_rows(values_only=True)); ix = {k: i for i, k in enumerate(rows[0])}
for r in rows[1:]: why[r[ix['Company']]] = (r[ix['Status']], r[ix['Why']], r[ix['Needs your review']])
ids = {}
for c in changed:
    if c[3]: ids.setdefault(c[0], set()).add(c[3])
names = {c[0] for c in changed}
for r in csv.DictReader(open(j.LOG_PATH)):
    if r['company'] in names and r['contact_id'] and r['result'].startswith('ok'):
        ids.setdefault(r['company'], set()).add(r['contact_id'])
ALL = set(j.STATUS_TAG.values()) | {'client-current', 'status-review'}
n = 0
for comp, cids in sorted(ids.items()):
    status, reason, review = why[comp]
    want = {j.STATUS_TAG[status]} | ({'client-current'} if status in j.CLIENT_CURRENT_STATUSES else set())
    if review: want.add('status-review')
    for cid in cids:
        sc, c = j.api('GET', f'/contacts/{cid}')
        if sc != 200: print('MISSING', comp, cid, sc); continue
        have = set((c.get('contact') or {}).get('tags') or [])
        rm = sorted((have & ALL) - want); add = sorted(want - have)
        print(comp, '|', status, '| remove', rm, '| add', add)
        if RUN and (rm or add):
            if rm: j.api('DELETE', f'/contacts/{cid}/tags', body={'tags': rm})
            if add: j.api('POST', f'/contacts/{cid}/tags', body={'tags': add})
            j.api('POST', f'/contacts/{cid}/notes', body={'userId': j.DAVID_USER_ID,
                  'body': f'Status check 2026-09-28: {status}. {reason}'})
            n += 1
print('updated', n)
