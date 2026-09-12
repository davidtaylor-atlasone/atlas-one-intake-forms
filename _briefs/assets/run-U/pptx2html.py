#!/usr/bin/env python3
"""Approximate renderer: python-pptx shapes -> one HTML page per slide (absolute boxes), for Chromium screenshots.
Also reports text boxes whose rendered text is likely to overflow (measured in the browser afterwards)."""
import sys, os, base64, html, json
import pptx
from pptx.util import Emu
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
E=9525.0
FONTS=open('/private/tmp/claude-501/sp/fontfaces.css').read()
def px(v): return v/E
def color_of(font, default):
    try:
        if font.color and font.color.type is not None and font.color.rgb is not None: return str(font.color.rgb)
    except Exception: pass
    return default
def fill_css(sh):
    try:
        f=sh.fill
        if f.type==1: return 'background:#%s;'%str(f.fore_color.rgb)
    except Exception: pass
    return ''
def line_css(sh):
    try:
        ln=sh.line
        if ln.fill.type==1 and ln.width: return 'border:%.1fpx solid #%s;'%(max(1,px(ln.width)),str(ln.color.rgb))
    except Exception: pass
    return ''
def run_html(r, base_size, base_color):
    f=r.font; size=f.size.pt if f.size else base_size
    st='font-size:%.1fpx;'%(size*96/72)
    if f.bold: st+='font-weight:700;'
    if f.italic: st+='font-style:italic;'
    if f.name: st+="font-family:'%s',sans-serif;"%f.name
    st+='color:#%s;'%color_of(f, base_color)
    return '<span style="%s">%s</span>'%(st, html.escape(r.text).replace('\n','<br>'))
def shape_html(sh, out):
    l,t,w,h=px(sh.left or 0),px(sh.top or 0),px(sh.width or 0),px(sh.height or 0)
    base='position:absolute;left:%.1fpx;top:%.1fpx;width:%.1fpx;height:%.1fpx;box-sizing:border-box;'%(l,t,w,h)
    if sh.shape_type==MSO_SHAPE_TYPE.GROUP:
        for s2 in sh.shapes: shape_html(s2,out); return
    if sh.shape_type==MSO_SHAPE_TYPE.PICTURE:
        try: blob=sh.image.blob; mime=sh.image.content_type
        except Exception: out.append('<div style="%sborder:1px dashed #999"></div>'%base); return
        out.append('<img src="data:%s;base64,%s" style="%sobject-fit:contain">'%(mime,base64.b64encode(blob).decode(),base)); return
    if sh.has_table if hasattr(sh,'has_table') else False:
        tb=sh.table; rows=[]
        for r in tb.rows:
            cells=[]
            for c in r.cells:
                txt=''.join(run_html(rn,10,'23304D') for p in c.text_frame.paragraphs for rn in p.runs) or '&nbsp;'
                bg=''
                try:
                    if c.fill.type==1: bg='background:#%s;'%str(c.fill.fore_color.rgb)
                except Exception: pass
                cells.append('<td style="%spadding:3px 6px;border:1px solid #DBE4ED;vertical-align:middle">%s</td>'%(bg,txt))
            rows.append('<tr>'+''.join(cells)+'</tr>')
        out.append('<table style="%sborder-collapse:collapse;font-size:10px">%s</table>'%(base,''.join(rows))); return
    st=base+fill_css(sh)+line_css(sh)
    try:
        if sh.shape_type==MSO_SHAPE_TYPE.AUTO_SHAPE and sh.auto_shape_type is not None and 'ROUND' in str(sh.auto_shape_type): st+='border-radius:6px;'
        if sh.shape_type==MSO_SHAPE_TYPE.AUTO_SHAPE and 'OVAL' in str(sh.auto_shape_type): st+='border-radius:50%;'
    except Exception: pass
    inner=''
    if sh.has_text_frame and sh.text_frame.text.strip():
        tf=sh.text_frame
        bp=tf._txBody.find('{http://schemas.openxmlformats.org/drawingml/2006/main}bodyPr')
        ins={k:px(int(bp.get(k))) for k in ('lIns','tIns','rIns','bIns') if bp.get(k) is not None}
        pad='padding:%.1fpx %.1fpx %.1fpx %.1fpx;'%(ins.get('tIns',3.6),ins.get('rIns',7.2),ins.get('bIns',3.6),ins.get('lIns',7.2))
        anchor=bp.get('anchor','t'); jc={'t':'flex-start','ctr':'center','b':'flex-end'}.get(anchor,'flex-start')
        autofit=[c.tag.split('}')[1] for c in bp]
        paras=[]
        for p in tf.paragraphs:
            al={PP_ALIGN.CENTER:'center',PP_ALIGN.RIGHT:'right',PP_ALIGN.JUSTIFY:'justify'}.get(p.alignment,'left')
            runs=''.join(run_html(r,18,'23304D') for r in p.runs) or '&nbsp;'
            sa=p.space_after.pt if p.space_after else 0; sb=p.space_before.pt if p.space_before else 0
            lvl=p.level or 0
            paras.append('<div style="text-align:%s;margin:%.1fpx 0 %.1fpx %dpx;line-height:1.2">%s</div>'%(al,sb*96/72,sa*96/72,lvl*18,runs))
        wrap='white-space:pre-wrap;word-wrap:break-word;' if bp.get('wrap','square')!='none' else 'white-space:nowrap;'
        inner='<div class="tf" data-autofit="%s" style="display:flex;flex-direction:column;justify-content:%s;width:100%%;height:100%%;%s%s"><div class="tx">%s</div></div>'%(','.join(autofit),jc,pad,wrap,''.join(paras))
    out.append('<div class="sh" data-name="%s" style="%s">%s</div>'%(html.escape(sh.name),st,inner))
def render(pptx_path, outdir):
    os.makedirs(outdir,exist_ok=True)
    p=pptx.Presentation(pptx_path); W,H=px(p.slide_width),px(p.slide_height)
    paths=[]
    for i,s in enumerate(p.slides,1):
        out=[]
        bg=''
        try:
            if s.background.fill.type==1: bg='background:#%s;'%str(s.background.fill.fore_color.rgb)
        except Exception: pass
        for sh in s.shapes: shape_html(sh,out)
        doc='<!doctype html><html><head><meta charset="utf-8"><style>%s body{margin:0;background:#888} .slide{position:relative;width:%.0fpx;height:%.0fpx;background:#fff;overflow:hidden;font-family:"DM Sans",sans-serif;color:#23304D;%s} .sh{overflow:visible}</style></head><body><div class="slide">%s</div></body></html>'%(FONTS,W,H,bg,''.join(out))
        fp=os.path.join(outdir,'slide-%02d.html'%i); open(fp,'w').write(doc); paths.append(fp)
    return paths, W, H
if __name__=='__main__':
    paths,W,H=render(sys.argv[1],sys.argv[2]); print(len(paths),'slides',W,H)
