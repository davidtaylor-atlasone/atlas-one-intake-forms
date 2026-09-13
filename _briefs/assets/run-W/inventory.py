#!/usr/bin/env python3
"""Count em dashes, en dashes and spaced hyphens in VISIBLE copy of HTML files.
Classifies each occurrence: text (text node outside script/style), attr (placeholder/title/alt/aria-label/value/label/content),
js (string literal inside <script> or inline handler), other (CSS, JS code, comments, base64, other attrs).
Usage: inventory.py [--dump] file...   (--dump prints each visible occurrence with context)"""
import re, sys, json, html

DASH_RE = re.compile(r'—|–|&mdash;|&ndash;|&#8212;|&#8211;|&#x2014;|&#x2013;|\\u2014|\\u2013| - ', re.M)
VIS_ATTRS = {'placeholder','title','alt','aria-label','aria-placeholder','value','label','text','data-en','data-es','data-default','data-placeholder','data-label','data-title','data-tip','data-tooltip','data-text','data-empty'}
CSS_CONTENT = re.compile(r'content\s*:\s*["\'][^"\']*["\']')

def kind(m):
    s = m.group(0)
    if s in ('—','&mdash;','&#8212;','&#x2014;','\\u2014'): return 'em'
    if s in ('–','&ndash;','&#8211;','&#x2013;','\\u2013'): return 'en'
    return 'hy'

def js_strings(src, i=0, stop=None):
    """Return (list of (start,end,text) string literals, index) scanning JS from i. If stop is set, returns when the
    matching closing brace of a template ${ } expression is found. Skips comments and (roughly) regex literals."""
    n = len(src); out = []; depth = 0
    while i < n:
        c = src[i]
        if stop and c == '{': depth += 1
        if stop and c == '}':
            if depth == 0: return out, i
            depth -= 1
        if c == '/' and i+1 < n and src[i+1] == '/':
            j = src.find('\n', i); i = n if j < 0 else j+1; continue
        if c == '/' and i+1 < n and src[i+1] == '*':
            j = src.find('*/', i+2); i = n if j < 0 else j+2; continue
        if c in '"\'':
            q = c; j = i+1
            while j < n:
                if src[j] == '\\': j += 2; continue
                if src[j] == q or src[j] == '\n': break
                j += 1
            out.append((i, j+1, src[i+1:j])); i = j+1; continue
        if c == '`':
            j = i+1; chunk = j
            while j < n:
                if src[j] == '\\': j += 2; continue
                if src[j] == '`': break
                if src[j] == '$' and j+1 < n and src[j+1] == '{':
                    if j > chunk: out.append((chunk-1, j, src[chunk:j]))
                    sub, k = js_strings(src, j+2, stop=True)
                    out.extend(sub); j = k+1; chunk = j; continue
                j += 1
            if j > chunk: out.append((chunk-1, j, src[chunk:j]))
            i = j+1; continue
        if c == '/':
            k = i-1
            while k >= 0 and src[k] in ' \t\n': k -= 1
            if k < 0 or src[k] in '(,=:[!&|?{};+-*%<>~^' or src[max(0,k-5):k+1].endswith(('return','typeof')):
                j = i+1; incls = False
                while j < n:
                    if src[j] == '\\': j += 2; continue
                    if src[j] == '[': incls = True
                    elif src[j] == ']': incls = False
                    elif src[j] == '/' and not incls: break
                    elif src[j] == '\n': break
                    j += 1
                i = j+1; continue
        i += 1
    return (out, n) if stop else out

def scan(path):
    src = open(path, encoding='utf-8', errors='replace').read()
    counts = {'text':{'em':0,'en':0,'hy':0}, 'attr':{'em':0,'en':0,'hy':0}, 'js':{'em':0,'en':0,'hy':0}, 'other':{'em':0,'en':0,'hy':0}}
    hits = []
    def add(cat, m, ctx, off):
        counts[cat][kind(m)] += 1
        if cat != 'other':
            a = max(0, m.start()-50); b = min(len(ctx), m.end()+50)
            hits.append({'cat':cat,'kind':kind(m),'pos':off+m.start(),'line':src.count('\n',0,off+m.start())+1,'ctx':ctx[a:b].replace('\n',' ')})
    # tokenize html
    pos = 0; n = len(src)
    tag_re = re.compile(r'<!--.*?-->|<(script|style)\b[^>]*>.*?</\1\s*>|<!\[CDATA\[.*?\]\]>|<[^>]+>', re.S|re.I)
    for m in tag_re.finditer(src):
        # text before this tag
        text = src[pos:m.start()]
        if text.strip():
            for d in DASH_RE.finditer(text): add('text', d, text, pos)
        tok = m.group(0); lo = tok.lower()
        if tok.startswith('<!--') or tok.startswith('<![CDATA['):
            for d in DASH_RE.finditer(tok): add('other', d, tok, m.start())
        elif m.group(1):  # script or style block
            tagname = m.group(1).lower()
            open_end = tok.find('>')+1; body_end = lo.rfind('</'+tagname)
            body = tok[open_end:body_end]; boff = m.start()+open_end
            if tagname == 'style':
                for cm in CSS_CONTENT.finditer(body):
                    for d in DASH_RE.finditer(cm.group(0)): add('attr', d, cm.group(0), boff+cm.start())
                # rest is other
                cnt = sum(1 for _ in DASH_RE.finditer(body)) - sum(1 for cm in CSS_CONTENT.finditer(body) for _ in DASH_RE.finditer(cm.group(0)))
                counts['other']['em'] += cnt  # approx: css dashes are irrelevant anyway
            else:
                stype = re.search(r'type\s*=\s*["\']?([^"\'\s>]+)', tok[:open_end], re.I)
                if stype and stype.group(1).lower() not in ('text/javascript','module','application/javascript','javascript'):
                    # template / json blocks: treat as text-ish html
                    for d in DASH_RE.finditer(body): add('js', d, body, boff)
                else:
                    spans = js_strings(body); last = 0
                    for (s,e,t) in spans:
                        gap = body[last:s]
                        for d in DASH_RE.finditer(gap): add('other', d, gap, boff+last)
                        for d in DASH_RE.finditer(t): add('js', d, t, boff+s+1)
                        last = e
                    gap = body[last:]
                    for d in DASH_RE.finditer(gap): add('other', d, gap, boff+last)
        else:
            # ordinary tag: check visible attributes and inline handlers
            for am in re.finditer(r'([A-Za-z_:][-\w:.]*)\s*=\s*("([^"]*)"|\'([^\']*)\'|([^\s"\'>]+))', tok):
                name = am.group(1).lower(); val = am.group(3) if am.group(3) is not None else (am.group(4) if am.group(4) is not None else am.group(5))
                voff = m.start() + am.start(2) + (1 if am.group(3) is not None or am.group(4) is not None else 0)
                if name in VIS_ATTRS or (name == 'content' and 'og:' in tok):
                    # value only counts on input/button/option
                    if name == 'value' and not re.match(r'<\s*(input|button|option|textarea)\b', tok, re.I): 
                        for d in DASH_RE.finditer(val): add('other', d, val, voff)
                        continue
                    for d in DASH_RE.finditer(val): add('attr', d, val, voff)
                elif name.startswith('on'):
                    for (s,e,t) in js_strings(html.unescape(val)):
                        for d in DASH_RE.finditer(t): add('js', d, t, voff+s+1)
                else:
                    for d in DASH_RE.finditer(val): add('other', d, val, voff)
        pos = m.end()
    tail = src[pos:]
    for d in DASH_RE.finditer(tail): add('text', d, tail, pos)
    return counts, hits

if __name__ == '__main__':
    args = sys.argv[1:]; dump = '--dump' in args; args = [a for a in args if a != '--dump']
    rows = []
    for p in args:
        c, h = scan(p)
        vis = {k: c['text'][k]+c['attr'][k]+c['js'][k] for k in ('em','en','hy')}
        rows.append({'file':p.split('/')[-1] if 'tools/' not in p else p, 'path':p, 'counts':c, 'visible':vis, 'hits':h if dump else []})
        print(f"{vis['em']:5d} {vis['en']:5d} {vis['hy']:5d} | text {sum(c['text'].values()):4d} attr {sum(c['attr'].values()):4d} js {sum(c['js'].values()):4d} other {sum(c['other'].values()):4d} | {rows[-1]['file']}")
        if dump:
            for x in h: print(f"   [{x['cat']}/{x['kind']}] L{x['line']}: {x['ctx']}")
    json.dump(rows, open('/dev/stdout' if False else '/tmp/inv.json','w'), indent=1)
