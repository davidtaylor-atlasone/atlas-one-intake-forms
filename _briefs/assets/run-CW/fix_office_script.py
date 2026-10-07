import sys,re
from pptx import Presentation
import docx
R=[("Per company / per month, setup $995, waived on annual","Per company / per month, setup $995, often waived"),
   ("are often waived on an annual start.","are often waived."),
   ("$995 waived on annual for Enterprise","$995 often waived for Enterprise"),
   ("waived on annual","often waived")]
def fix_par(p):
    t="".join(r.text for r in p.runs)
    n=t
    for a,b in R: n=n.replace(a,b)
    if n==t: return 0
    # try run level first
    done=False
    for r in p.runs:
        o=r.text
        for a,b in R: r.text=r.text.replace(a,b) if False else r.text
    p.runs[0].text=n
    for r in p.runs[1:]: r.text=""
    return 1
def walk_tf(tf):
    c=0
    for p in tf.paragraphs: c+=fix_par(p)
    return c
def shapes(shs):
    c=0
    for sh in shs:
        if sh.shape_type==6: c+=shapes(sh.shapes)
        if sh.has_text_frame: c+=walk_tf(sh.text_frame)
        if getattr(sh,"has_table",False) and sh.has_table:
            for row in sh.table.rows:
                for cell in row.cells: c+=walk_tf(cell.text_frame)
    return c
for path in sys.argv[1:]:
    if path.endswith(".pptx"):
        pr=Presentation(path); c=0
        for sl in pr.slides:
            c+=shapes(sl.shapes)
            if sl.has_notes_slide: c+=walk_tf(sl.notes_slide.notes_text_frame)
        if c: pr.save(path)
        print(path.split("/")[-1],c)
    else:
        d=docx.Document(path); c=0
        def doc_pars(d):
            for p in d.paragraphs: yield p
            for t in d.tables:
                for row in t.rows:
                    for cell in row.cells:
                        for p in cell.paragraphs: yield p
        for p in doc_pars(d): c+=fix_par(p)
        if c: d.save(path)
        print(path.split("/")[-1],c)
