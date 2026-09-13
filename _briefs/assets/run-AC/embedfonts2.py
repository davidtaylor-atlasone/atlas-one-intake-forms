#!/usr/bin/env python3
"""Run AC job 1: for kit tools that ask for DM Sans in CSS but never load it (no Google link, no @font-face),
embed DM Sans 400 and 700 (500 where used) as base64 TTF the way repo tools/self-assessment/index.html does.
Horas only if used and not already embedded. The <style id="a1fonts-2026-09-13"> block goes right before the
first <style> in <head> (or before </head>). Additive: nothing else in the file changes.
usage: embedfonts2.py <Master_Kit> <backup_dir> <file> [...]"""
import sys, os, re, io, json, base64, shutil
MK, BAK = sys.argv[1], sys.argv[2]
FONTS = os.path.join(MK, "A1_Final Brand", "3. Fonts")
def b64(p): return base64.b64encode(open(p, "rb").read()).decode("ascii")
DM = {w: b64(os.path.join(FONTS, "DM_Sans", "static", n)) for w, n in
      (("400", "DMSans-Regular.ttf"), ("500", "DMSans-Medium.ttf"), ("700", "DMSans-Bold.ttf"))}
HORAS = b64(os.path.join(FONTS, "Horas-Medium.ttf"))
def face(fam, data, weight):
    return "@font-face{font-family:'%s';src:url(data:font/ttf;base64,%s) format('truetype');font-weight:%s;font-display:swap}" % (fam, data, weight)
os.makedirs(BAK, exist_ok=True)
for path in sys.argv[3:]:
    name = os.path.basename(path)
    raw = io.open(path, encoding="utf-8", newline="").read()
    if re.search(r"@font-face\{[^}]*font-family:\s*['\"]?DM Sans", raw):
        print(json.dumps({"file": name, "skipped": "DM Sans already embedded"})); continue
    bak = os.path.join(BAK, name)
    assert not os.path.exists(bak), "backup exists " + name
    shutil.copy2(path, bak)
    assert io.open(bak, encoding="utf-8", newline="").read() == raw, "backup mismatch " + name
    uses500 = bool(re.search(r"font-weight\s*:\s*500\b", raw))
    usesHoras = bool(re.search(r"font-family\s*:[^;}]*Horas", raw))
    hasHoras = bool(re.search(r"@font-face\{[^}]*font-family:\s*'Horas'", raw))
    faces = [face("DM Sans", DM["400"], "400")]
    if uses500: faces.append(face("DM Sans", DM["500"], "500"))
    faces.append(face("DM Sans", DM["700"], "700"))
    if usesHoras and not hasHoras: faces.insert(0, face("Horas", HORAS, "400 700"))
    block = '<style id="a1fonts-2026-09-13">\n' + "\n".join(faces) + "\n</style>\n"
    m = re.search(r"<style\b", raw)
    if m: out = raw[:m.start()] + block + raw[m.start():]
    else:
        m = re.search(r"</head>", raw); assert m, "no </head> in " + name
        out = raw[:m.start()] + block + raw[m.start():]
    io.open(path, "w", encoding="utf-8", newline="").write(out)
    assert out.replace(block, "", 1) == raw
    print(json.dumps({"file": name, "faces": ["DM Sans 400"] + (["DM Sans 500"] if uses500 else []) + ["DM Sans 700"] + (["Horas 400-700"] if usesHoras and not hasHoras else []),
                      "before_bytes": len(raw.encode()), "after_bytes": len(out.encode())}))
