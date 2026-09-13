#!/bin/zsh
# Restore every changed file from the before-copies and re-run the pass (repeatable).
set -e
cd /Users/davidtaylor/Projects/atlas-one-intake-forms
MK="/Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit"
D="$MK/06 Calculators and Tools (NEW Aug 2026)"; B="$MK/_to_delete/superseded-2026-09-12/tools-before-dash-pass"
for f in "$B"/*.html; do cp "$f" "$D/$(basename "$f")"; done
cp "$B/repo-tools/retention-cost.html" tools/retention-cost/index.html
cp "$B/repo-tools/vendor-consolidation.html" tools/vendor-consolidation/index.html
cp "$B/repo-tools/wc-premium-check.html" tools/wc-premium-check/index.html
python3 _briefs/assets/run-W/dashpass.py --apply "$D"/*.html tools/*/index.html | awk '$1>0' | wc -l
python3 - "$D/Employee Handbook Builder (Bilingual 50-State).html" "$D/Safety Manual Builder (Bilingual OSHA).html" <<'PY'
import sys,re
for p in sys.argv[1:]:
    s=open(p,encoding='utf-8').read()
    m=re.search(r"replace\(/\^Section \\d\+\\s\*\[\\u2014-\]\\s\*/,''\)",s); assert m
    s=s[:m.start()]+m.group(0).replace('[\\u2014-]','[\\u2014:-]')+s[m.end():]
    open(p,'w',encoding='utf-8').write(s); print('shortGroup regex patched')
PY
sed -i '' '313s|<span class="dash">-</span>|<span class="dash">to</span>|' "$D/Cost of a Compliance Mistake (Atlas One).html"
sed -n '313p' "$D/Cost of a Compliance Mistake (Atlas One).html"
