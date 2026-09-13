#!/usr/bin/env python3
"""Compare before/after sample captures: numbers must be identical; the word diff may only be dash rewrites."""
import json, sys, re, difflib
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2]))
ALLOWED_INS = {'to', '…'}
tot_bad = 0
for f in A:
    a, b = A[f], B.get(f)
    if not b: print('MISSING after', f); continue
    bad = []
    if a['loadErrors'] != b['loadErrors']: bad.append(f"loadErrors {a['loadErrors']} -> {b['loadErrors']}")
    if len(a['errors']) != len(b['errors']): bad.append(f"errors {len(a['errors'])} -> {len(b['errors'])}")
    for k in a['shots']:
        na, nb = a['numbers'][k], b['numbers'].get(k)
        if na != nb:
            sm = difflib.SequenceMatcher(None, na, nb or [])
            d = [(t, na[i1:i2], (nb or [])[j1:j2]) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal']
            bad.append(f"numbers differ in {k}: {d[:4]}")
        ta = re.findall(r"[\w$%/'…]+", a['shots'][k]['text'] + a['shots'][k]['values'])
        tb = re.findall(r"[\w$%/'…]+", b['shots'][k]['text'] + b['shots'][k]['values'])
        sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
        for t, i1, i2, j1, j2 in sm.get_opcodes():
            if t == 'equal': continue
            dele, ins = ta[i1:i2], tb[j1:j2]
            if all(w in ALLOWED_INS for w in ins) and all(w in ('—','–','-') for w in dele): continue
            bad.append(f"words {k}: -{dele[:6]} +{ins[:6]}")
    status = 'OK ' if not bad else 'DIFF'
    tot_bad += bool(bad)
    print(status, f[:58].ljust(58), f"in {a['filled']} clk {a['clicked']} loadErr {len(a['loadErrors'])}/{len(b['loadErrors'])} err {len(a['errors'])}/{len(b['errors'])}")
    for x in bad[:8]: print('     ', x[:300])
print('files with differences:', tot_bad)
