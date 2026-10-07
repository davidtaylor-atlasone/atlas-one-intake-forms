import os,sys,re,json
MKT=os.path.expanduser("~/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing")
APPLY = "--apply" in sys.argv
SKIP=("_to_delete","_BUILD-LOG","node_modules",".git/","__pycache__","Book of Business","_briefs")
EXT=(".html",".py",".json",".md",".csv",".ts",".js",".txt",".css")
R=[
 ("</b>, waived on annual","</b>, often waived"),
 ("are often waived on an annual start.","are often waived."),
 ("$995 waived on annual for Enterprise","$995 often waived for Enterprise"),
 ("Setup fees are one time and are often waived on an annual plan; annual plans get two months free.","Setup fees are one time and are often waived."),
 ("Setup fees are one time and often waived on an annual plan; annual plans get two months free.","Setup fees are one time and often waived."),
 (" Annual plans get two months free.",""),
 ("Annual plans get two months free. ",""),
 ("$999 a month, $995 setup, waived on an annual plan","$999 a month, $995 setup, often waived"),
 ("setup $995, waived on annual","setup $995, often waived"),
 ("Setup $995, waived on annual","Setup $995, often waived"),
 ("(waived on annual)","(often waived)"),
 ("Is annual billing required?","Is the setup fee always charged?"),
 ("No. Annual billing waives the $995 setup fee, that is the only difference.","No. The $995 setup fee is often waived, and your Atlas One proposal states exactly what is due."),
 ('("2.", "Setup fee and annual option", "A one time setup fee applies at some tiers as shown below. "\n         "Setup is often waived at signing or on an annual plan; the Client\'s proposal states the exact setup "\n         "due, if any.")','("2.", "Setup fee", "A one time setup fee applies at some tiers as shown below. "\n         "Setup is often waived at signing; the Client\'s proposal states the exact setup "\n         "due, if any.")'),
 ('Annual plans are OPEN (David has not decided): print nothing about annual pricing.','Annual plans are OFF (David, 2026-10-06): never print two months free, 15% off annual, setup waived on annual, pay annually, or any annual plan offer.'),
]
changed=0
for dp,dn,fn in os.walk(MKT):
    dn[:]=[d for d in dn if d not in ("_to_delete","_BUILD-LOG","node_modules",".git","__pycache__","Book of Business","_briefs")]
    for f in fn:
        if not f.endswith(EXT) or ".bak" in f: continue
        p=os.path.join(dp,f)
        try: s=open(p,encoding="utf-8").read()
        except Exception: continue
        o=s
        for a,b in R: s=s.replace(a,b)
        if s!=o:
            changed+=1; print(("WROTE " if APPLY else "WOULD ")+p.replace(MKT,"")); 
            if APPLY: open(p,"w",encoding="utf-8").write(s)
print("files",changed)
