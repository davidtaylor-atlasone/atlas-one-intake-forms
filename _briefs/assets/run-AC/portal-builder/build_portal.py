#!/usr/bin/env python3
"""Atlas One PORTAL — the internal launcher for every tool in the Master Kit.

Rebuilt 2026-08-25. The previous version loaded each tool into an <iframe>.
Chrome treats every local file as its own opaque origin and refuses to embed
one local file inside another, so every tab rendered as an empty black frame.

This version uses nothing but plain <a href> links. No iframes, no
window.open(), no scripted navigation -- a user-initiated click on an anchor
is the one thing that has always worked from a file:// page and is the least
likely to be broken by a future browser change.

It MUST sit at the root of Atlas_One_Master_Kit, beside the numbered folders,
because every link is relative to it. Regenerate with:

    python3 build_portal.py "/path/to/Atlas_One_Master_Kit"
"""
import sys, os, html, urllib.parse, datetime

CAL = "06 Calculators and Tools (NEW Aug 2026)"
WEB = "01 Website Pages"
QQ  = "09 Quick Quote Tool"
AIE = "11 AI-Email-Assistant"
SALES = "../../A1_Sales"   # marketing tree, one level above HR_Docs
CC  = "Command Center"
BRJ = "05 Build Specs (for BRJ)"

# (section, tagline, [(file, folder, title, blurb, badge)])
SECTIONS = [
 ("Quoting & Proposals", "What goes in front of a prospect", [
  (f"{QQ}/Atlas_One_Quick_Quote.html", "Quick Quote",
   "Price any Atlas One service in front of a prospect. 99 services across all six divisions, every price adjustable, health comparison, and a searchable quote log.", "Internal"),
  (f"{CAL}/Atlas One Savings Summary (Atlas One).html", "Savings Summary",
   "One page that rolls the whole back office into a single annual number, the hours it gives back, and the exposure still open.", ""),
  (f"{CAL}/Health Quote Census Intake (Atlas One).html", "Health Quote Census",
   "Collect the census a carrier needs to quote — clean, in one pass.", ""),
  (f"{CAL}/Health Comparison Builder (Atlas One).html", "Health Comparison Builder",
   "Type in what they have today and what came back from the market. Writes the data file the comparison deck is built from — and enforces the single-carrier rule under 500 lives.", ""),
  (f"{CAL}/Atlas_One_Benefits_Routing_Tool.html", "Benefits Routing Tool",
   "Entity type, headcount, states, current coverage and budget in; the recommended route out (carrier partners, PEO plan, ICHRA, alternative funding, individual) with the two sentence why and the one question to ask next.", "Internal"),
  (f"{CAL}/Employee Benefits Options (Atlas One).html", "Benefits Options Presenter",
   "Walk a group through their plan choices side by side.", ""),
  (f"{CAL}/Atlas_One_COI_Tracker.html", "COI Tracker",
   "For construction clients with 5 to 50 subs: every subcontractor, every certificate, every expiry. Flags gaps 30 days early, holds payment until the certificate is on file, writes the request email. CSV in and out, save and reload, print.", ""),
  (f"{CAL}/COI to Workers Comp Premium Estimator (Atlas One).html", "COI → WC Premium Estimator",
   "Turn a certificate of insurance into a workers' comp premium estimate.", ""),
  (f"{CAL}/Atlas_One_Onboarding_Tracker.html", "Prospect Onboarding Tracker",
   "What they signed up for, pricing and deal terms, the facts gathered across calls, documents to collect, call log and the handoff notes for the setup team.", "Internal"),
 ]),
 ("Calculators & Diagnostics", "Lead magnets and discovery tools", [
  (f"{CAL}/Atlas One Calculators (53 tools).html", "53 Business Calculators",
   "Labor burden, workers' comp, PEO vs in-house, cost of a bad hire, tax and more.", ""),
  (f"{CAL}/Atlas One Business Tools (17 generators).html", "27 Business Generators",
   "Invoice, statement, credit app, lien waiver, business cards, toolbox talk and more. Fill in, export PDF.", ""),
  (f"{CAL}/Business Value Diagnostic (Atlas One).html", "Business Value Diagnostic",
   "Instant read on where value is leaking out of the business.", ""),
  (f"{CAL}/Business Infrastructure Audit (Atlas One).html", "Infrastructure Audit",
   "Six-division score of what is in place and what is missing.", ""),
  (f"{CAL}/Vendor Consolidation Savings (Atlas One).html", "Vendor Consolidation Savings",
   "What collapsing many vendors into one relationship is worth.", ""),
  (f"{CAL}/Atlas_One_Back_Office_Self_Assessment.html", "Back Office Self-Assessment",
   "Ten questions, two minutes. Scores time, money and risk, names the three biggest leaks, books the 30 minute audit. Free tool, also live at forms.atlasonesolutions.com/tools/self-assessment/.", ""),
  (f"{CAL}/Atlas_One_Time_Savings_Discovery.html", "Time and Cost Savings Discovery",
   "Fill in with the prospect: the tasks they still do by hand and the software they could drop, and see the hours and dollars that come back every year. Free tool, also live at forms.atlasonesolutions.com/tools/time-savings/.", ""),
  (f"{CAL}/Retention Cost Calculator (Atlas One).html", "Retention Cost Calculator",
   "The real cost of turnover, priced out.", ""),
  (f"{CAL}/Retention Scorecard (Atlas One).html", "Retention Scorecard",
   "Where retention risk actually sits.", ""),
  (f"{CAL}/Atlas_One_Compliance_Calendar.html", "Compliance Calendar by state",
   "Pick states and headcount and get the next twelve months of federal and state HR and payroll deadlines, each with a source and a confirm before relying note. Standing rules per state. Exports .ics and prints.", ""),
  (f"{CAL}/Compliance Risk Scorecard (Atlas One).html", "Compliance Risk Scorecard",
   "What is in place, partly in place, and not in place.", ""),
  (f"{CAL}/Cost of a Compliance Mistake (Atlas One).html", "Cost of a Compliance Mistake",
   "Unchecked exposure priced against published maximums.", ""),
 ]),
 ("Document Builders", "Paid, done-for-you services", [
  (f"{CAL}/Atlas_One_Build_This_For_Me.html", "Have Atlas One build this for me",
   "The forward page behind the button on every builder. Reads ?doc=, sends the prospect to the GHL build form (or the holding page with email and booking until that form exists).", ""),
  (f"{CAL}/Employee Handbook Builder (Bilingual 50-State).html", "Employee Handbook Builder",
   "Bilingual, all 50 states. Fill in once, pick a state, toggle policies, save as PDF.", "Premium"),
  (f"{CAL}/Safety Manual Builder (Bilingual OSHA).html", "Safety Manual Builder",
   "Bilingual OSHA safety manual — federal base plus state-plan flags.", "Premium"),
  (f"{CAL}/W-2 At-Will Employment Agreement Builder (Atlas One).html", "W-2 At-Will Agreement",
   "At-will employment agreement, built to the state.", "Premium"),
  (f"{CAL}/Independent Contractor Agreement Builder (Atlas One).html", "Contractor Agreement",
   "1099 independent contractor agreement builder.", "Premium"),
  (f"{CAL}/NDA Builder (Atlas One).html", "NDA Builder",
   "Mutual or one-way non-disclosure agreement.", "Premium"),
  (f"{CAL}/Disciplinary Write-Up Notice Generator (Atlas One).html", "Disciplinary Write-Up",
   "Documented, defensible performance notice.", ""),
  (f"{CAL}/Separation Letter Generator (Atlas One).html", "Separation Letter",
   "Termination and offboarding letter.", ""),
  (f"{CAL}/W-2 Employee Onboarding Packet (Bilingual).html", "W-2 Onboarding Packet",
   "Bilingual. W-4, I-9 and direct deposit in one packet.", ""),
  (f"{CAL}/Independent Contractor Onboarding Packet (Bilingual).html", "1099 Onboarding Packet",
   "Bilingual. W-9 and direct deposit.", ""),
  (f"{CAL}/Employee Benefits Package & Enrollment Guide (Bilingual) (Atlas One).html",
   "Enrollment Guide", "Bilingual benefits package and enrollment walkthrough.", ""),
 ]),
 ("Payroll & Accounting", "Premium paid tools", [
  (f"{CAL}/Certified Payroll Manager (Atlas One).html", "Certified Payroll Manager",
   "Multi-job certified payroll — federal WH-347, Oregon WH-38, portal entry sheets and job allocation.", "Premium"),
  (f"{CAL}/Certified Payroll Converter (WH-347) (Atlas One).html", "Certified Payroll Converter",
   "Convert a payroll report into WH-347 format.", "Premium"),
  (f"{CAL}/Payroll to GL Import Converter (Atlas One).html", "Payroll → GL Import",
   "Turn a payroll report into a QuickBooks Desktop .IIF or a Sage/Xero journal, with the client's chart of accounts validated before export.", "Premium"),
  (f"{CAL}/Meeting Bonus Import Builder (Atlas One).html", "Bonus Import Builder",
   "Turn an attendance or meeting tracker into a payroll bonus import file. Tier rules, validation, audit trail.", "Premium"),
 ]),
 ("Libraries & Reference", "Templates, safety and compliance", [
  (f"{WEB}/templates.html", "HR Template Library",
   "155 templates. Searchable, with an email gate for the premium downloads.", ""),
  (f"{WEB}/Labor Law Poster Center.html", "Labor Law Poster Center",
   "Federal posters plus a state picker — every link goes to the official free government source.", ""),
  (f"{BRJ}/Workforce Software Comparison (Atlas One).html", "Workforce Software Comparison",
   "Twelve platforms compared feature by feature, with pros and cons.", ""),
  (f"{BRJ}/PEO Comparison Tool (Atlas One).html", "PEO Comparison Tool",
   "How the PEOs stack up against each other.", ""),
 ]),
 ("AI & Operations", "The technology division", [
  (f"{SALES}/AI Services and Assistants/Atlas_One_AI_Email_Assistant_OnePager.html", "AI Email Assistant — one-pager",
   "Sell sheet. Essentials $249 / Professional $499 per month, setup $750, extra mailbox $75 (Aug 29 pricing).", ""),
  (f"{SALES}/AI Services and Assistants/Atlas_One_AI_Task_Agent_OnePager.html", "AI Task Agent — one-pager",
   "Sell sheet. $199 per month standalone, $99 bundled with the Email Assistant, $500 setup.", ""),
  (f"{AIE}/Atlas_One_AI_Email_Assistant_Client_Setup_Kit.html", "AI Email Assistant — Setup Kit",
   "What the client needs to do to go live.", ""),
  (f"{CC}/atlas-command-center.html", "Command Center",
   "Build tracker — what is done, what is open.", "Internal"),
 ]),
]


def build(master_kit_dir, out_name="Atlas One PORTAL.html"):
    present, missing = [], []
    for _, _, items in SECTIONS:
        for rel, *_ in items:
            (present if os.path.exists(os.path.join(master_kit_dir, rel)) else missing).append(rel)

    today = datetime.date.today().strftime("%B %-d, %Y") if os.name != "nt" else datetime.date.today().strftime("%B %d, %Y")
    parts = []
    for title, tagline, items in SECTIONS:
        live = [it for it in items if os.path.exists(os.path.join(master_kit_dir, it[0]))]
        if not live:
            continue
        cards = []
        for rel, name, blurb, badge in live:
            href = urllib.parse.quote(rel)
            folder = rel.rsplit("/", 1)[0]
            chip = f'<span class="badge">{html.escape(badge)}</span>' if badge else ""
            cards.append(
              f'<a class="card" href="{href}" target="_blank" rel="noopener" '
              f'data-find="{html.escape((name + " " + blurb + " " + folder).lower())}">'
              f'<span class="cname">{html.escape(name)}{chip}</span>'
              f'<span class="cblurb">{html.escape(blurb)}</span>'
              f'<span class="cpath">{html.escape(folder)}</span>'
              f'<span class="copen">Open &#8599;</span></a>')
        parts.append(
          f'<section class="sect"><h2>{html.escape(title)}</h2>'
          f'<p class="tag">{html.escape(tagline)}</p>'
          f'<div class="grid">{"".join(cards)}</div></section>')

    doc = TEMPLATE.replace("{{SECTIONS}}", "".join(parts)) \
                  .replace("{{COUNT}}", str(len(present))) \
                  .replace("{{DATE}}", today)
    out = os.path.join(master_kit_dir, out_name)
    tmp = out + ".tmp$"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(doc)
    os.replace(tmp, out)
    return out, present, missing


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Atlas One — All Tools Portal</title>
<style>
:root{
  --navy:#23304D; --peri:#788DE3; --soft:#DBE4ED; --paper:#FAFAF8;
  --ink:#17202F; --muted:#5C6780; --faint:#8A93A8; --line:#DEE4EE;
  --surface:#FFFFFF; --tint:#EEF1FC;
  --body:'DM Sans',system-ui,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;
  --mono:ui-monospace,'SFMono-Regular',Menlo,monospace;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--paper);color:var(--ink);font-family:var(--body);
  font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2.5px solid var(--peri);outline-offset:3px;border-radius:8px}

.mast{background:var(--navy);color:#fff;padding:22px 0 20px}
.wrap{max-width:1140px;margin:0 auto;padding:0 24px}
.mast .eyebrow{font-family:var(--mono);font-size:10.5px;letter-spacing:.2em;
  text-transform:uppercase;color:#A7B4DF;margin:0 0 5px}
.mast h1{font-size:25px;font-weight:600;letter-spacing:-.02em;margin:0}
.mast .sub{font-size:13.5px;color:#C3CCE8;margin:6px 0 0}

.bar{background:var(--surface);border-bottom:1px solid var(--line);
  position:sticky;top:0;z-index:5;padding:13px 0}
.bar .inner{display:flex;gap:14px;align-items:center;flex-wrap:wrap}
#q{flex:1 1 300px;font-family:inherit;font-size:15.5px;padding:12px 15px;
  border:1px solid var(--line);border-radius:10px;background:var(--paper);color:var(--ink)}
#q:focus{outline:none;border-color:var(--peri);background:#fff}
.count{font-family:var(--mono);font-size:12px;color:var(--faint);white-space:nowrap}

.note{background:var(--tint);border-left:4px solid var(--peri);
  padding:14px 18px;margin:20px 0 4px;border-radius:0 10px 10px 0;font-size:14px;color:var(--ink)}
.note b{color:var(--navy)}
.note code{font-family:var(--mono);font-size:12.5px;background:#fff;
  padding:2px 6px;border-radius:4px;border:1px solid var(--line)}

.sect{padding:30px 0 4px}
.sect h2{font-size:19px;font-weight:600;letter-spacing:-.015em;color:var(--navy);margin:0}
.sect .tag{font-size:13.5px;color:var(--muted);margin:3px 0 16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:14px}

.card{display:flex;flex-direction:column;gap:5px;background:var(--surface);
  border:1px solid var(--line);border-radius:12px;padding:17px 18px 15px;
  transition:border-color .12s,transform .12s,box-shadow .12s}
.card:hover{border-color:var(--peri);transform:translateY(-1px);
  box-shadow:0 1px 2px rgba(23,32,47,.05),0 10px 24px rgba(23,32,47,.08)}
.cname{font-weight:600;font-size:15.5px;color:var(--navy);display:flex;
  align-items:center;gap:8px;flex-wrap:wrap;line-height:1.3}
.badge{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;
  text-transform:uppercase;background:var(--peri);color:#fff;
  padding:2.5px 7px;border-radius:4px;font-weight:500}
.cblurb{font-size:13.2px;color:var(--muted);line-height:1.5;flex:1}
.cpath{font-family:var(--mono);font-size:10.5px;color:var(--faint);
  margin-top:6px;word-break:break-word}
.copen{font-size:12.5px;font-weight:600;color:var(--peri);margin-top:8px}

.empty{padding:40px 0;color:var(--muted);font-size:15px}
footer{padding:36px 0 46px;color:var(--faint);font-family:var(--mono);
  font-size:11.5px;line-height:1.8;border-top:1px solid var(--line);margin-top:32px}
@media print{.bar,.note,footer{display:none}.card{break-inside:avoid}}
</style>
</head>
<body>

<header class="mast">
  <div class="wrap">
    <p class="eyebrow">Atlas One Solutions &middot; Internal</p>
    <h1>All Tools Portal</h1>
    <p class="sub">Every tool, calculator, builder and library in the Master Kit &mdash; one click each.</p>
  </div>
</header>

<div class="bar">
  <div class="wrap inner">
    <input id="q" type="search" placeholder="Search tools — try “handbook”, “payroll”, “retention”…" autocomplete="off">
    <span class="count" id="count">{{COUNT}} tools</span>
  </div>
</div>

<div class="wrap">
  <p class="note"><b>Keep this file where it is.</b> It lives at the top of
  <code>Atlas_One_Master_Kit</code>, beside the numbered folders, and every link below is
  relative to that spot. If you copy it to your Desktop or Downloads the links stop
  resolving. Each card shows its folder, so if one ever fails you can see exactly where it
  was looking.</p>

  {{SECTIONS}}

  <p class="empty" id="none" style="display:none">Nothing matches that search.</p>

  <footer>
    ATLAS ONE SOLUTIONS &middot; ONE CALL SOLVES EVERYTHING<br>
    DAVID TAYLOR &middot; 385-213-7177 &middot; DAVID@ATLASONESOLUTIONS.COM<br>
    REBUILT {{DATE}} &middot; PLAIN LINKS, NO EMBEDDED FRAMES
  </footer>
</div>

<script>
/* Search only. Navigation is plain <a href> so it cannot be broken by script. */
(function(){
  var q = document.getElementById("q"),
      cards = [].slice.call(document.querySelectorAll(".card")),
      sects = [].slice.call(document.querySelectorAll(".sect")),
      none = document.getElementById("none"),
      count = document.getElementById("count"),
      total = cards.length;
  function run(){
    var terms = q.value.toLowerCase().split(/\s+/).filter(Boolean), shown = 0;
    cards.forEach(function(c){
      var hay = c.getAttribute("data-find"),
          hit = terms.every(function(t){ return hay.indexOf(t) > -1; });
      c.style.display = hit ? "" : "none";
      if(hit) shown++;
    });
    sects.forEach(function(s){
      var any = [].slice.call(s.querySelectorAll(".card")).some(function(c){
        return c.style.display !== "none"; });
      s.style.display = any ? "" : "none";
    });
    none.style.display = shown ? "none" : "";
    count.textContent = shown === total ? total + " tools" : shown + " of " + total;
  }
  q.addEventListener("input", run);
  q.addEventListener("keydown", function(e){ if(e.key === "Escape"){ q.value=""; run(); } });
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    mk = sys.argv[1] if len(sys.argv) > 1 else "."
    out, present, missing = build(mk)
    print("  wrote:", os.path.basename(out))
    print("  tools linked:", len(present))
    if missing:
        print("  skipped (file not present):", len(missing))
        for m in missing:
            print("     -", m)


# ---------------------------------------------------------------------------
# "What is this for?" (Run AC, 2026-09-13). One paragraph per tool, drawn from
# the tool's own header copy so the Portal never has to be hand edited when a
# tool's intro changes. Order of preference: <meta name="description">, the
# first paragraph in the hero or title band, the first <p> after the first <h1>
# or <h2>, the <title>. Tags are stripped, whitespace collapsed, dashes replaced.
# ---------------------------------------------------------------------------
import re as _re, html as _html

def _clean(t):
    t = _re.sub(r"<[^>]+>", " ", t)
    t = _html.unescape(t)
    t = t.replace("—", ",").replace("–", ",").replace(" ,", ",")
    t = _re.sub(r"\s+", " ", t).strip()
    return t

def header_copy(raw, fallback=""):
    """Return one plain text paragraph describing the tool, from its own header copy."""
    body = _re.sub(r"<style\b.*?</style>|<script\b.*?</script>|<!--.*?-->", " ", raw, flags=_re.S | _re.I)
    m = _re.search(r'<meta\s+name="description"\s+content="([^"]{30,})"', raw, _re.I)
    if m:
        return _clean(m.group(1))
    for pat in (r'<(?:div|header|section)[^>]*class="[^"]*(?:hero|title-band|intro|lede)[^"]*"[^>]*>.*?<p[^>]*>(.*?)</p>',
                r'<h1[^>]*>.*?</h1>\s*(?:<[^p][^>]*>\s*)*<p[^>]*>(.*?)</p>',
                r'<h2[^>]*>.*?</h2>\s*(?:<[^p][^>]*>\s*)*<p[^>]*>(.*?)</p>',
                r'<p[^>]*class="[^"]*(?:sub|lede|tagline|intro)[^"]*"[^>]*>(.*?)</p>'):
        m = _re.search(pat, body, _re.S | _re.I)
        if m:
            t = _clean(m.group(1))
            if 60 <= len(t) <= 600 and not _re.search(r"updates as you type", t, _re.I):
                return t
    # any explanatory paragraph in reading order: long enough to say something, not a UI instruction
    for m in _re.finditer(r"<p[^>]*>(.*?)</p>", body, _re.S | _re.I):
        t = _clean(m.group(1))
        if 80 <= len(t) <= 600 and not _re.search(r"updates as you type|click|select|choose|tap|enter your|fill in|required|Print / Save", t, _re.I):
            return t
    # nothing usable in the tool itself: the catalogue blurb, then the <title>
    if fallback:
        return fallback
    m = _re.search(r"<title>(.*?)</title>", raw, _re.S | _re.I)
    return _clean(m.group(1)) if m else ""
