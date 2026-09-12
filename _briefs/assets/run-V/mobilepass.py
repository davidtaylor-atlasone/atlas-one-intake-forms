#!/usr/bin/env python3
"""Run V job 2: additive mobile layout CSS for the Retention Cost Calculator (EN/ES) and Vendor Consolidation Savings (EN/ES).
No calculation code is touched. Idempotent (skips a file that already carries the block)."""
import sys, re, os
MARK='a1mobile-2026-09-12'
RET_CSS='''
<style id="%s">
/* Mobile layout pass (2026-09-12, additive): one column under 700 px, 44 px touch targets on touch screens. */
@media (max-width:700px){
  .grid{grid-template-columns:1fr !important;}
  .inline{flex-wrap:wrap;}
  .bar-row{grid-template-columns:1fr 90px;}
  .bar-row .name{grid-column:1 / -1; margin-bottom:-6px;}
  .industrybar select{min-width:0; width:100%%;}
  .hbar{padding:12px 16px;}
  header,.wrap,.foot,.afoot,.industrybar{padding-left:16px; padding-right:16px;}
  .summary{padding:18px 16px;}
  .card{padding:16px;}
  .out .big{font-size:24px;}
  .ratio{padding:14px;}
}
@media (max-width:700px), (pointer:coarse){
  input[type=number],select,.a1printbtn,.cta-band a{min-height:44px;}
  .prefix span{top:50%%; transform:translateY(-50%%);}
  summary{padding:12px 0;}
}
</style>
'''%MARK
VC_CSS='''
/* Mobile layout pass (2026-09-12, additive): the vendor table becomes stacked rows under 700 px, 44 px touch targets. */
@media (max-width:700px){
  .wrap{padding:20px 16px 32px}
  .hbar{padding:12px 16px}
  .card{padding:16px 14px}
  #vcards{grid-template-columns:1fr !important}
  .card table{min-width:0 !important;margin-top:4px !important}
  .card table thead{display:none}
  .card table,.card table tbody,.card table tr,.card table td{display:block;width:100%%}
  .card table tr{display:grid;grid-template-columns:1fr auto;gap:4px 12px;align-items:center;border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin-top:10px}
  .card table td{padding:0 !important}
  .card table td:nth-child(1){font-weight:700;font-size:15px !important}
  .card table td:nth-child(2){justify-self:end}
  .card table td:nth-child(3),.card table td:nth-child(4){grid-column:1 / -1;margin-top:4px}
  .card table td:nth-child(3)::before,.card table td:nth-child(4)::before{display:block;font-size:11.5px;color:var(--mut);text-transform:uppercase;letter-spacing:.04em;margin-bottom:3px}
  .card table td:nth-child(3)::before{content:"%s"}
  .card table td:nth-child(4)::before{content:"%s"}
}
@media (max-width:700px),(pointer:coarse){
  input[type=number],.a1printbtn,.cta-band a{min-height:44px}
  .prefix span{top:50%%;transform:translateY(-50%%)}
  .chk{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;margin:-8px 0;cursor:pointer;vertical-align:middle}
  .chk input{width:24px !important;height:24px !important}
}
/* %s */
'''
def patch(path):
    s=open(path,encoding='utf-8').read()
    if MARK in s: print('already patched',os.path.basename(path)); return
    name=os.path.basename(path)
    if name.startswith('Retention Cost'):
        assert '</head>' in s
        s=s.replace('</head>',RET_CSS+'</head>',1)
    else:
        es='Espanol' in name
        css=VC_CSS%(('Costo mensual' if es else 'Monthly cost'),('Hrs/mes gestionándolo' if es else 'Hrs / mo managing it'),MARK)
        assert s.count('</style></head>')==1
        s=s.replace('</style></head>',css+'</style></head>',1)
        n=0
        def wrap(m):
            nonlocal n; n+=1; return '<label class="chk">'+m.group(0)+'</label>'
        s=re.sub(r'<input type="checkbox" id="\w+_on"[^>]*>',wrap,s); assert n==12, n
    open(path,'w',encoding='utf-8').write(s); print('patched',name)
for p in sys.argv[1:]: patch(p)
