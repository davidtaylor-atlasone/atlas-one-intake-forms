#!/usr/bin/env python3
"""Run Z: before/after sample captures must be byte identical in field values, generated documents, body text and state."""
import json, sys
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2])); bad = 0
for k in A:
    a, b = A[k], B.get(k)
    if not b: print('MISSING', k); bad += 1; continue
    diffs = [f for f in ('values', 'docs', 'bodyText', 'state', 'loadErrors', 'errors') if a[f] != b[f]]
    print(('OK  ' if not diffs else 'DIFF'), k[:72].ljust(72), 'sw', a['scrollWidth'], '->', b['scrollWidth'], ('  differs in: ' + ', '.join(diffs)) if diffs else '')
    bad += bool(diffs)
print('captures with differences:', bad)
