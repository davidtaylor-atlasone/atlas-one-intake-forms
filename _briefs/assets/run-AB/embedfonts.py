#!/usr/bin/env python3
"""Run AB: remove the Google Fonts links from a kit tool and embed DM Sans (and Horas where used and
not already embedded) the way repo tools/self-assessment/index.html does: one @font-face per face,
data:font/ttf;base64, format('truetype'), font-display:swap. Font bytes come from the brand folder
(A1_Final Brand/3. Fonts), which are byte-identical to the ones embedded in the self-assessment.

usage: embedfonts.py <Master_Kit> <backup_dir> <file> [<file> ...]
Prints one JSON line per file with what was done. Additive apart from the removed <link> tags."""
import sys, os, re, io, json, base64, shutil, hashlib

MK, BAK = sys.argv[1], sys.argv[2]
FONTS = os.path.join(MK, "A1_Final Brand", "3. Fonts")
def b64(p): return base64.b64encode(open(p, "rb").read()).decode("ascii")
DM = {w: b64(os.path.join(FONTS, "DM_Sans", "static", n)) for w, n in
      (("400", "DMSans-Regular.ttf"), ("500", "DMSans-Medium.ttf"), ("700", "DMSans-Bold.ttf"))}
HORAS = b64(os.path.join(FONTS, "Horas-Medium.ttf"))

def face(fam, data, weight):
    return "@font-face{font-family:'%s';src:url(data:font/ttf;base64,%s) format('truetype');font-weight:%s;font-display:swap}" % (fam, data, weight)

LINK_RE = re.compile(r"""[ \t]*<link\b[^>]*?(?:fonts\.googleapis\.com|fonts\.gstatic\.com)[^>]*?>[ \t]*\r?\n?""", re.S)

os.makedirs(BAK, exist_ok=True)
for path in sys.argv[3:]:
    name = os.path.basename(path)
    raw = io.open(path, encoding="utf-8", newline="").read()
    bak = os.path.join(BAK, name)
    shutil.copy2(path, bak)
    assert io.open(bak, encoding="utf-8", newline="").read() == raw, "backup mismatch " + name

    links = LINK_RE.findall(raw)
    assert links, "no google link in " + name
    # which faces does the file need?
    uses500 = bool(re.search(r"font-weight\s*:\s*500\b", raw))
    usesHoras = bool(re.search(r"font-family\s*:[^;}]*Horas", raw)) or "'Horas'" in raw
    hasHoras = bool(re.search(r"@font-face\{[^}]*font-family:\s*'Horas'", raw))
    faces = [face("DM Sans", DM["400"], "400")]
    if uses500: faces.append(face("DM Sans", DM["500"], "500"))
    faces.append(face("DM Sans", DM["700"], "700"))
    addHoras = usesHoras and not hasHoras
    if addHoras: faces.insert(0, face("Horas", HORAS, "400 700"))
    block = '<style id="a1fonts-2026-09-13">\n' + "\n".join(faces) + "\n</style>\n"

    # put the block where the stylesheet link was (the first css2 link); drop every google link
    m = re.search(r"""[ \t]*<link\b[^>]*?fonts\.googleapis\.com/css2[^>]*?>[ \t]*\r?\n?""", raw, re.S)
    assert m, "no css2 link in " + name
    out = raw[:m.start()] + "\0MARK\0" + raw[m.end():]
    out = LINK_RE.sub("", out)
    out = out.replace("\0MARK\0", block)
    assert "fonts.googleapis" not in out and "fonts.gstatic" not in out
    # additive check: strip the block and the removed links from the original and compare
    check = LINK_RE.sub("", raw)
    assert out.replace(block, "") == check, "non-additive change in " + name
    io.open(path, "w", encoding="utf-8", newline="").write(out)
    print(json.dumps({"file": name, "links_removed": len(links), "faces": ["Horas 400-700"] * addHoras + ["DM Sans 400"] + ["DM Sans 500"] * uses500 + ["DM Sans 700"],
                      "horas_already_embedded": hasHoras, "bytes_before": len(raw.encode("utf-8")), "bytes_after": len(out.encode("utf-8"))}))
