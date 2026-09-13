#!/usr/bin/env python3
"""Run AC: shared brand shell for new kit tools. Fonts embedded as base64 (Horas TTF, DM Sans woff2 400/500/700,
the same subsets the PEO vs ASO tool carries). Four colours. No external requests."""
import os, base64
HERE = os.path.dirname(os.path.abspath(__file__))
def b64(name): return base64.b64encode(open(os.path.join(HERE, 'fonts', name), 'rb').read()).decode('ascii')
def fontcss():
    return ("@font-face{font-family:'Horas';src:url(data:font/ttf;base64,%s) format('truetype');font-weight:400 700;font-display:swap}\n" % b64('Horas.ttf') +
            "".join("@font-face{font-family:'DM Sans';src:url(data:font/woff2;base64,%s) format('woff2');font-weight:%s;font-display:swap}\n" % (b64('DMSans-%s.woff2' % w), w) for w in ('400', '500', '700')))
BASE_CSS = """
:root{--navy:#23304D;--navy2:#2c3c60;--peri:#788DE3;--perih:#96A6EC;--off:#FAFAF8;--soft:#DBE4ED;--muted:#5b6577;--line:#cdd8e6;--tint:#eef1fb}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:'DM Sans',system-ui,-apple-system,sans-serif;color:var(--navy);background:var(--off);line-height:1.5;letter-spacing:-.006em;-webkit-font-smoothing:antialiased}
h1,h2,h3,.d{font-family:'Horas','DM Sans',serif;font-weight:500;letter-spacing:-.02em}
.top{position:sticky;top:0;z-index:10;background:var(--navy);color:#fff;display:flex;align-items:center;gap:10px;padding:11px 15px;padding-top:max(11px,env(safe-area-inset-top))}
.mark{width:34px;height:34px;border-radius:9px;background:var(--peri);display:grid;place-items:center;flex:none}
.mark span{font-weight:700;font-size:15px;color:#fff}.mark span b{color:var(--navy)}
.tt{font-family:'Horas';font-size:16px;line-height:1.05}.ts{font-size:10px;color:var(--perih);font-weight:600}
.tbtns{margin-left:auto;display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}
.b{border:1px solid #3a4a70;background:var(--navy2);color:#fff;font-weight:600;font-size:12.5px;padding:8px 12px;border-radius:8px;cursor:pointer;font-family:'DM Sans';white-space:nowrap}
.b.p{background:var(--peri);border-color:var(--peri)}
.b.o{background:#fff;color:var(--navy);border-color:var(--line)}
.b:active{transform:translateY(1px)}
.wrap{max-width:1120px;margin:0 auto;padding:16px 15px 70px}
.hero{background:linear-gradient(135deg,var(--navy),var(--navy2));color:#fff;border-radius:16px;padding:22px 24px}
.hero h1{font-size:26px;margin:0 0 6px}.hero p{margin:0;color:#c9d2ea;font-size:14.5px}
.card{background:#fff;border:1px solid var(--line);border-radius:13px;padding:16px 18px;margin-top:14px}
.card h2{font-size:16px;margin:0 0 2px}.card .sub{color:var(--muted);font-size:12px;margin:0 0 10px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:10px}.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
@media(max-width:680px){.g2,.g3,.g4{grid-template-columns:1fr 1fr}}
@media(max-width:430px){.g3,.g4{grid-template-columns:1fr}}
label{font-size:11.5px;font-weight:600;color:var(--muted);display:block;margin-bottom:3px}
input,select,textarea{border:1px solid var(--line);border-radius:9px;padding:9px 10px;font-size:15px;font-family:'DM Sans';width:100%;color:var(--navy);background:#fff}
input:focus,select:focus,textarea:focus{outline:2px solid var(--perih);outline-offset:-1px}
select{-webkit-appearance:none;appearance:none;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='12' height='8'><path d='M1 1l5 5 5-5' stroke='%235b6577' stroke-width='2' fill='none'/></svg>");background-repeat:no-repeat;background-position:right 11px center;padding-right:28px}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{border:1px solid var(--line);border-radius:20px;padding:5px 11px;font-size:12.5px;cursor:pointer;background:#fff;user-select:none}
.chip.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.chip.on::before{content:"\\2713\\00a0";font-weight:700}
.callout{border:1px solid var(--line);border-left:4px solid var(--peri);background:#fff;border-radius:10px;padding:12px 15px;margin-top:12px;font-size:13.5px}
.hint{font-size:11px;color:var(--muted);margin-top:8px}
.mini{font-size:10px;color:var(--muted)}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);padding:6px 8px;border-bottom:2px solid var(--soft)}
td{padding:7px 8px;border-bottom:1px solid #eef1f6;vertical-align:top}
.tag{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.03em;padding:2px 8px;border-radius:20px;border:1px solid var(--navy);color:var(--navy)}
.tag.solid{background:var(--navy);color:#fff}.tag.tint{background:var(--tint);border-color:var(--tint)}.tag.peri{background:var(--peri);border-color:var(--peri);color:#fff}
.help{border:1px dashed var(--line);border-radius:12px;padding:12px 15px;margin-top:14px;font-size:13px;color:var(--muted);background:#fff}
@media print{.top{display:none}body{background:#fff}.card,.callout{break-inside:avoid}.noprint{display:none !important}}
"""
def head(title, extra_css=''):
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">\n'
            '<title>%s</title>\n<style>\n%s%s%s</style></head>' % (title, fontcss(), BASE_CSS, extra_css))
def topbar(subtitle, buttons_html=''):
    return ('<div class="top"><div class="mark"><span>A<b>1</b></span></div><div><div class="tt">Atlas One Solutions</div><div class="ts">%s</div></div>'
            '<div class="tbtns">%s<button class="b p" onclick="window.print()">Print / Save PDF</button></div></div>' % (subtitle, buttons_html))
