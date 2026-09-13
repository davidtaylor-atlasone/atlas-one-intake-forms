#!/usr/bin/env python3
"""Run Z item 7: additive mobile layout CSS for the six tools that still scrolled sideways at 390 px.
One <style id="a1mobile-2026-09-12"> block per file, inserted right before </head>. No markup, no JavaScript,
no existing CSS is touched. Idempotent (skips a file that already carries the block)."""
import sys, os
MARK = 'a1mobile-2026-09-12'
TOUCH = '''@media (max-width:700px){
  input[type=text],input[type=date],input[type=number],input[type=email],input[type=tel],select{min-height:44px}
  .btn,button.btn{min-height:44px}
}'''
CSS = {
'Atlas_One_Onboarding_Tracker.html': '''
/* Mobile layout pass (Run Z, 2026-09-12, additive): the three tables become stacked rows under 700 px. */
@media (max-width:700px){
  .wrap{padding:0 14px 40px}
  .card{padding:14px 14px}
  .g4,.g3,.g2{grid-template-columns:1fr}
  table thead{display:none}
  table,table tbody{display:block;width:100%}
  table tbody tr{display:grid;grid-template-columns:1fr auto;gap:6px 10px;align-items:center;border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin-top:10px}
  table tbody td{display:block;padding:0;border:0}
  td input,td textarea,td select{border-color:var(--line);background:#fff;width:100%}
  .stat{width:100%}
  /* documents: label + key, then status | received, then notes; the remove button sits top right */
  #docs td:nth-child(1){grid-column:1;grid-row:1}
  #docs td:nth-child(5){grid-column:2;grid-row:1;justify-self:end}
  #docs td:nth-child(2){grid-column:1;grid-row:2}
  #docs td:nth-child(3){grid-column:2;grid-row:2}
  #docs td:nth-child(4){grid-column:1 / -1;grid-row:3}
  #docs td:nth-child(4)::before{content:"Notes";display:block;font-size:10.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;margin-bottom:2px}
  /* calls: date | remove, then what we covered */
  #calls td:nth-child(1){grid-column:1;grid-row:1}
  #calls td:nth-child(3){grid-column:2;grid-row:1;justify-self:end}
  #calls td:nth-child(2){grid-column:1 / -1;grid-row:2}
  #calls td:nth-child(2)::before{content:"What we covered";display:block;font-size:10.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;margin-bottom:2px}
  /* pricing lines: label | remove, then monthly | setup */
  #plines td:nth-child(1){grid-column:1;grid-row:1}
  #plines td:nth-child(4){grid-column:2;grid-row:1;justify-self:end}
  #plines td:nth-child(2){grid-column:1;grid-row:2}
  #plines td:nth-child(3){grid-column:2;grid-row:2}
  #plines td:nth-child(2)::before{content:"Monthly";display:block;font-size:10.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;margin-bottom:2px}
  #plines td:nth-child(3)::before{content:"Setup / one-time";display:block;font-size:10.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;margin-bottom:2px}
  td.num input{text-align:left}
  .rm{min-height:32px;min-width:32px}
}
''',
'Employee Benefits Options (Atlas One).html': '''
/* Mobile layout pass (Run Z, 2026-09-12, additive): the rate tables become stacked rows under 560 px. */
@media (max-width:560px){
  .wrap{padding:0 16px}
  .tier-top{padding:18px 16px 14px}
  .tier-body{padding:16px 16px 18px}
  .mec-wrap,.card,.step{padding:18px 16px}
  table.rates{display:block;border-radius:var(--radius-sm)}
  table.rates thead{display:none}
  table.rates tbody{display:block}
  table.rates tbody tr{display:grid;grid-template-columns:1fr 1fr;gap:8px 10px;padding:10px 12px;border-top:1px solid var(--line)}
  table.rates tbody tr:first-child{border-top:0}
  table.rates tbody td{display:block;padding:0;border:0;text-align:left}
  table.rates tbody td:first-child{grid-column:1 / -1;background:none;white-space:normal;font-size:14px;padding:0}
  table.rates tbody td:nth-child(n+2)::before{display:block;font-size:11px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;margin-bottom:3px}
  table.rates tbody td:nth-child(2)::before{content:"Employee"}
  table.rates tbody td:nth-child(3)::before{content:"Employee + Spouse"}
  table.rates tbody td:nth-child(4)::before{content:"Employee + Child(ren)"}
  table.rates tbody td:nth-child(5)::before{content:"Family"}
  .rate-cell{max-width:none;width:100%;text-align:left}
}
''',
'NDA Builder (Atlas One).html': '''
/* Mobile layout pass (Run Z, 2026-09-12, additive): one column that never exceeds the screen, under 700 px. */
@media (max-width:700px){
  .wrap{grid-template-columns:minmax(0,1fr);min-height:0}
  .panel{padding:18px 16px;min-width:0}
  .panel.form{overflow:visible}
  .topbar,.cta-banner,footer{padding-left:16px;padding-right:16px}
  .topbar{padding-top:14px;padding-bottom:14px}
  .seg{flex-wrap:wrap}
  .seg-opt{flex:1 1 45%}
  .a1-save .a1s-acts,.a1-logo-ctl .a1-acts{margin-left:0;flex-wrap:wrap}
  .a1-buildme,.btn-gold{white-space:normal}
  .toolbar-btns{flex-wrap:wrap}
  #document{padding:28px 18px}
  #document .sig-wrap{grid-template-columns:1fr;gap:22px}
}
''',
'W-2 At-Will Employment Agreement Builder (Atlas One).html': '''
/* Mobile layout pass (Run Z, 2026-09-12, additive): one column that never exceeds the screen, under 700 px. */
@media (max-width:700px){
  .workspace{grid-template-columns:minmax(0,1fr)}
  .form-pane{min-width:0;padding:16px 16px 40px}
  .preview-pane{padding:16px 12px}
  .topbar,.cta-banner{padding-left:16px;padding-right:16px}
  .header-actions{flex-wrap:wrap}
  .a1-save .a1s-acts,.a1-logo-ctl .a1-acts{margin-left:0;flex-wrap:wrap}
  .a1-buildme,.btn{white-space:normal}
  .doc-toolbar{flex-wrap:wrap}
  .document{padding:28px 18px}
  .document .terms-table td.k{width:auto}
  .sig-block{grid-template-columns:1fr;gap:22px}
}
''',
'Employee Handbook Builder (Bilingual 50-State).html': '''
/* Mobile layout pass (Run Z, 2026-09-12, additive): form above preview, one column, under 700 px. */
@media (max-width:700px){
  .topbar{flex-wrap:wrap;gap:8px 10px;padding:10px 14px;position:static}
  .topbar h1{flex:1 1 auto;font-size:1rem}
  .topbar .sp{display:none}
  .a1-buildme{white-space:normal;text-align:center}
  .app{grid-template-columns:minmax(0,1fr);height:auto}
  .formpanel{border-right:none;border-bottom:1px solid var(--line);overflow:visible;padding:16px 16px 24px}
  .toglist{max-height:320px}
  .a1-save .a1s-acts{margin-left:0;flex-wrap:wrap}
  .previewwrap{overflow:visible;padding:12px}
  .pagewrap{max-width:100%}
  .hb{padding:.45in .4in}
  .hb-cover{padding:.6in .3in;min-height:0}
  .hb-cover h1{font-size:28pt}
  .hb-cover-co{font-size:18pt}
  .hb-sign{flex-direction:column;gap:18px}
  .hb ul,.hb ol{margin-left:18px}
}
''',
}
CSS['Safety Manual Builder (Bilingual OSHA).html'] = CSS['Employee Handbook Builder (Bilingual 50-State).html']

def patch(path):
    s = open(path, encoding='utf-8').read()
    name = os.path.basename(path)
    if MARK in s: print('already patched', name); return
    css = CSS[name]
    block = '<style id="%s">%s%s\n</style>\n' % (MARK, css, TOUCH)
    assert s.count('</head>') == 1, name
    s = s.replace('</head>', block + '</head>', 1)
    open(path, 'w', encoding='utf-8').write(s); print('patched', name)

for p in sys.argv[1:]: patch(p)
