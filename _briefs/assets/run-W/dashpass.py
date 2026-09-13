#!/usr/bin/env python3
"""Run W dash pass. Rewrites em dashes, en dashes and spaced hyphens in VISIBLE copy (text nodes, visible attributes,
JS string literals) with commas, periods, colons, parentheses, "to", or a rephrase. Never touches CSS, JS code,
comments, data attributes other than the bilingual data-en/data-es, URLs or numbers.
Usage: dashpass.py --review file...   -> prints before/after per unit (no writes)
       dashpass.py --apply  file...   -> rewrites files in place
Overrides: a JSON file next to this script (overrides.json) maps exact unit text -> replacement."""
import re, sys, json, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inventory as inv

OVR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'overrides.json')
OVERRIDES = json.load(open(OVR_PATH)) if os.path.exists(OVR_PATH) else {}

EM = '—'; EN = '–'
ENT_EM = re.compile(r'&mdash;|&#8212;|&#x2014;|\\u2014'); ENT_EN = re.compile(r'&ndash;|&#8211;|&#x2013;|\\u2013')
TAG = re.compile(r'<[^>]+>')
CONJ = {'and','or','but','so','which','not','nor','yet','y','o','pero','ni','e','u','sino','including','plus','then','because','while','with','without','even','especially','usually','typically','often','sometimes','if','unless','as','like'}
RANGE_L = r'(?:[\d%×½¼¾kKM]|am|pm|AM|PM)'
RANGE_R = r'(?:[\$\d½¼¾~]|\+)'
WORD_RANGES = {('low','high'),('Mon','Fri'),('Monday','Friday'),('mon','fri'),('Jan','Dec'),('D1','D7'),('1B','1D')}

def words(s):
    s = TAG.sub(' ', s)
    return [w for w in re.findall(r"[\w'’]+", s) if re.search(r'\w', w)]

def fix_unit(text, cat, lctx='', rctx=''):
    if text in OVERRIDES: return OVERRIDES[text]
    t = ENT_EM.sub(EM, text); t = ENT_EN.sub(EN, t)
    # 1. bare placeholders (alone, or alone inside a tag, or a placeholder number with a unit suffix)
    t = re.sub(r'(>\s*\$?)—(\s*<)', r'\1…\2', t)
    t = re.sub(r'(>\s*)–(\s*<)', r'\1-\2', t)
    m = re.match(r'(\s*)[—–](\s*(?:/|%|vs\b|days\b|hrs\b|hours\b|months\b|per\b|pts\b|points\b))', t)
    if m: t = m.group(1) + '…' + t[m.end(1)+1:]
    if EM not in t and EN not in t and ' - ' not in t: return t
    if re.fullmatch(r'\s*\$?\s*—\s*', t): return t.replace(EM, '…')
    if re.fullmatch(r'\s*–\s*', t): return (' to ' if cat == 'js' else (t.replace(EN, 'to') if ' ' in t else '-'))  # bare en dash: a range separator, or a number-format separator in a box
    # 2. wrapped "— text —"
    m = re.fullmatch(r'(\s*)[—–]\s*(.*?)\s*[—–](\s*)', t)
    if m: return f"{m.group(1)}({m.group(2)}){m.group(3)}"
    # 2b. wrapped "— text —" inside markup (option labels in templates)
    t = re.sub(r'(^|>)(\s*)[—–]\s*([^—–<>]{1,60}?)\s*[—–](\s*)(?=<|$)', r'\1\2(\3)\4', t)
    if EM not in t and EN not in t and ' - ' not in t: return t
    # 3. numeric / word ranges
    t = re.sub(rf'(?<=[\d%×½¼¾kKM])\s*[–—]\s*(?={RANGE_R})', ' to ', t)
    t = re.sub(rf'(?<=[ap]m)\s*[–—]\s*(?={RANGE_R})', ' to ', t, flags=re.I)
    t = re.sub(r'(?<=[\d])\s*[–—]\s*(?=[\d])', ' to ', t)
    for a, b in WORD_RANGES:
        t = t.replace(f'{a}{EN}{b}', f'{a} to {b}').replace(f'{a} {EN} {b}', f'{a} to {b}').replace(f'{a}{EM}{b}', f'{a} to {b}')
    # JS separator chunks like " – " between two date/number expressions
    if re.fullmatch(r'\s*[–]\s*', t): return t.replace(EN, 'to')
    if re.fullmatch(r'\s*[–]\s*\$', t): return t.replace(EN, 'to')
    # remaining en dashes with spaces behave like em dashes; unspaced word–word en dash -> " to "
    t = re.sub(r'(?<=[A-Za-z])–(?=[A-Za-z])', ' to ', t)
    t = t.replace(EN, EM)
    # 4. spaced hyphen: treat as em dash
    t = t.replace(' - ', ' ' + EM + ' ')
    if EM not in t: return t
    # 4b. "text — aside —" (second dash trailing, a value follows): parenthetical
    m = re.fullmatch(r'(.*?\S)\s*—\s*(.+?)\s*—(\s*)', t, re.S)
    if m and words(m.group(1)) and words(m.group(2)) and not re.search(r'[.!?]\s', m.group(2)):
        if ',' in m.group(2): return m.group(1) + ' (' + m.group(2) + ')' + m.group(3)
        return m.group(1) + ', ' + m.group(2) + ',' + m.group(3)
    # 4c. leading dash inside a hint/sub span that follows a space: "(text)"
    if re.match(r'\s*—', t) and re.search(r'\s<(span|em|i|small|sub|sup)\b[^>]*>$', lctx):
        rest = re.sub(r'^\s*—\s*', '', t)
        m = re.match(r'(.*?)(\s*)$', rest, re.S)
        return '(' + m.group(1) + ')' + m.group(2)
    # 5. trailing dash: "Label —" or "Label — " -> "Label:" / "Label: "
    t = re.sub(r'\s*—(\s*)$', r':\1', t) if re.search(r'\S\s*—\s*$', t) else t
    # 6. leading dash: "— text" (continuation chunk) -> ", text"
    if re.match(r'\s*—', t):
        rest = re.sub(r'^\s*—\s*', '', t)
        lead = re.match(r'\s*', t).group(0)
        lw = words(re.split(r'[.!?;:]\s', TAG.sub(' ', lctx))[-1]); rw = words(rest)
        if rw and rw[0].lower() in CONJ: sep = ', '
        elif cat == 'js' and re.search(r'[+}]\s*[\'"]?$', lctx.rstrip()): sep = ': ' if len(rw) <= 4 else ', '
        elif lw and len(lw) <= 5 and not lctx.rstrip().endswith(','): sep = ': '
        else: sep = ', '
        t = lead.rstrip(' ') + sep + rest if lead.strip('\n') == lead else lead + sep.lstrip() + rest
        if not lead: t = sep + rest
        t = t if t.strip() else t
    # 7/8. mid dashes, sentence by sentence
    out = []; pos = 0
    # split into sentences at boundaries so pairing is judged within a sentence
    parts = re.split(r'((?<=[.!?])\s+(?=[A-ZÁÉÍÓÚ¿¡"“(<])|(?<=<br>)|(?<=<br/>)|(?<=\\n)|(?<=\n))', t)
    res = []
    for sent in parts:
        if sent is None: continue
        n = sent.count(EM)
        if n == 0: res.append(sent); continue
        segs = re.split(r'\s*—\s*', sent)
        if n == 2 and len(segs) == 3 and words(segs[2]) and words(segs[0]):
            # parenthetical: parentheses when it carries its own commas, otherwise commas both sides
            if ',' in segs[1] or ';' in segs[1]:
                res.append(segs[0].rstrip() + ' (' + segs[1].strip() + ')' + ('' if re.match(r'[,.;:!?)]', segs[2]) else ' ') + segs[2].lstrip()); continue
            res.append(segs[0] + ', ' + segs[1] + (', ' if not re.match(r'[,.;:!?)]', segs[2]) else '') + segs[2]); continue
        cur = segs[0]
        for k in range(1, len(segs)):
            left = cur; right = segs[k]
            # left = text since last clause boundary within this sentence
            lw = words(re.split(r'[.!?;:]\s', left)[-1]); rw = words(right); cont = False
            hm = re.search(r'<(span|em|i|small|sub|sup)\b[^>]*>\s*$', left)
            if hm and re.search(r'^\s*\S', right) and ('</' + hm.group(1) + '>') in right:
                inner, close = right.split('</' + hm.group(1) + '>', 1)
                cur = left.rstrip() + '(' + inner.strip() + ')' + '</' + hm.group(1) + '>' + close
                continue
            if k == 1 and sent is parts[0] and cat != 'attr' and not re.search(r'<\w', left) and '>' not in re.sub(r'</\w+>', '', left) and not re.search(r'[.!?;:]\s', TAG.sub(' ', left)):
                if cat == 'js' and re.search(r'([+}]\s*[\'"]?|\+\s*)$', lctx.rstrip()): lw = ['_'] * 4 + lw; cont = True
                elif cat != 'js' and not lctx.rstrip().endswith('>') or re.search(r'</\w+>$', lctx.rstrip()):
                    lw = words(re.split(r'[.!?;:]\s', TAG.sub(' ', lctx))[-1])[-8:] + lw if not re.search(r'\n\s*$', lctx) else lw
            if left.rstrip().endswith('(') or re.search(r'\(\s*[\w/ ]+$', left) and k == 1 and len(lw) <= 2:
                sep = ': '
            elif rw and rw[0].lower() in CONJ: sep = ', '
            elif left.rstrip().endswith(','): sep = ' '
            elif len(lw) <= 5 and not re.search(r'[,]\s*$', left): sep = ': '
            elif k == 1 and not cont and len(lw) <= 7 and len(words(sent)) <= 11 and not re.search(r'[.!?]', TAG.sub('', sent).rstrip('.!? ')) and not re.search(r'[,]\s*$', left): sep = ': '
            else: sep = ', '
            if sep == ': ' and right.startswith(':'): sep = ''
            cur = left.rstrip() + sep + right.lstrip() if right.strip() else left.rstrip() + sep.rstrip()
        res.append(cur)
    t = ''.join(res)
    return t

def units(path):
    """Yield (cat, start, end, text) visible units that contain a dash, absolute offsets into the file."""
    src = open(path, encoding='utf-8').read()
    out = []
    tag_re = re.compile(r'<!--.*?-->|<(script|style)\b[^>]*>.*?</\1\s*>|<!\[CDATA\[.*?\]\]>|<[^>]+>', re.S|re.I)
    pos = 0
    def add(cat, s, e):
        txt = src[s:e]
        if inv.DASH_RE.search(txt): out.append((cat, s, e, txt))
    for m in tag_re.finditer(src):
        if m.start() > pos: add('text', pos, m.start())
        tok = m.group(0); lo = tok.lower()
        if tok.startswith('<!--') or tok.startswith('<![CDATA['): pass
        elif m.group(1):
            tagname = m.group(1).lower(); open_end = tok.find('>')+1; body_end = lo.rfind('</'+tagname)
            body = tok[open_end:body_end]; boff = m.start()+open_end
            if tagname == 'style':
                for cm in inv.CSS_CONTENT.finditer(body): add('attr', boff+cm.start(), boff+cm.end())
            else:
                stype = re.search(r'type\s*=\s*["\']?([^"\'\s>]+)', tok[:open_end], re.I)
                if stype and stype.group(1).lower() not in ('text/javascript','module','application/javascript','javascript'):
                    add('js', boff, boff+len(body))
                else:
                    for (s,e,tx) in inv.js_strings(body):
                        q = body[s]
                        if q in '"\'': add('js', boff+s+1, boff+e-1)
                        else: add('js', boff+s+1, boff+e)  # template chunk: (chunk-1, j) -> text is [chunk, j)
        else:
            for am in re.finditer(r'([A-Za-z_:][-\w:.]*)\s*=\s*("([^"]*)"|\'([^\']*)\'|([^\s"\'>]+))', tok):
                name = am.group(1).lower()
                quoted = am.group(3) is not None or am.group(4) is not None
                vs = m.start() + am.start(2) + (1 if quoted else 0); ve = m.start() + am.end(2) - (1 if quoted else 0)
                if name in inv.VIS_ATTRS or (name == 'content' and 'og:' in tok):
                    if name == 'value' and not re.match(r'<\s*(input|button|option|textarea)\b', tok, re.I): continue
                    add('attr', vs, ve)
                elif name.startswith('on'):
                    val = src[vs:ve]
                    for (s,e,tx) in inv.js_strings(val):
                        add('js', vs+s+1, vs+e-(1 if val[s] in '"\'' else 0))
        pos = m.end()
    if pos < len(src): add('text', pos, len(src))
    return src, out

def process(path, apply=False, review=None):
    src, us = units(path)
    us.sort(key=lambda u: u[1])
    # drop overlaps (template chunk nesting can double count); keep outermost first
    cleaned = []; last_end = -1
    for u in us:
        if u[1] < last_end: continue
        cleaned.append(u); last_end = u[2]
    new = src; changes = []
    for cat, s, e, txt in reversed(cleaned):
        rep = fix_unit(txt, cat, src[max(0,s-160):s], src[e:e+80])
        if cat == 'js' and ("'" in rep and "'" not in txt): rep = rep.replace("'", "\\'")
        if rep != txt:
            changes.append((cat, s, txt, rep)); new = new[:s] + rep + new[e:]
    if review is not None:
        for cat, s, txt, rep in reversed(changes):
            line = src.count('\n', 0, s)+1
            review.write(f"### {os.path.basename(path)} L{line} [{cat}]\n- {txt.strip()[:400]}\n+ {rep.strip()[:400]}\n")
    if apply and new != src:
        open(path, 'w', encoding='utf-8').write(new)
    return len(changes)

if __name__ == '__main__':
    args = sys.argv[1:]; apply = '--apply' in args; args = [a for a in args if not a.startswith('--')]
    rv = open('/tmp/dash_review.md', 'w') if not apply else None
    for p in args:
        n = process(p, apply=apply, review=rv)
        print(f"{n:5d} units {'rewritten' if apply else 'proposed'} | {os.path.basename(p)}")
