#!/usr/bin/env python3
"""Builds tools/pitch/index.html from slides.json (Run AT, 2026-09-15).

slides.json is the extracted text of every slide in the 16-slide Prospect
Pitch Deck (python-pptx, one run: `python3 extract_slides.py` regenerates
it from the source pptx if the deck changes). This script never types deck
copy directly into the HTML; every sentence that reaches the page is
pulled out of slides.json by slide/line index (see SLIDE_TEXT below) and
run through fix_dashes() to satisfy the no-dashes brand rule, the one
transformation this script is allowed to make to deck copy. The two
Membership tier lines for Enterprise and Concierge are the one exception:
that text is a website decision (2026-09-13) overriding the deck, not deck
copy, so it is written directly.

Run:  python3 build.py
"""
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

with io.open(os.path.join(HERE, "slides.json"), encoding="utf-8") as f:
    SLIDES = json.load(f)  # 1-indexed by ["index"], body is 0-indexed

with io.open(os.path.join(HERE, "_fonts_faces.css"), encoding="utf-8") as f:
    FONTS_CSS = f.read()

with io.open(os.path.join(HERE, "_fullmark.svg"), encoding="utf-8") as f:
    LOGO_SVG = f.read()

AGREEMENTS_PRICES = os.path.join(HERE, "..", "agreements", "prices.json")
with io.open(AGREEMENTS_PRICES, encoding="utf-8") as f:
    PRICES = json.load(f)


def S(slide_no):
    return SLIDES[slide_no - 1]["body"]


DASH_NUM_RE = re.compile(r"(\d)\s*[–—]\s*(\d)")
DASH_SPACED_RE = re.compile(r"\s*[–—]\s*")


def fix_dashes(text):
    """The deck was written before the no-dashes brand rule. A number
    range (10-20) becomes "10 to 20"; every other em/en dash, always used
    here as a pause or an explanation, becomes a comma. Brand rule:
    CLAUDE.md, 'No dashes in copy'."""
    text = DASH_NUM_RE.sub(r"\1 to \2", text)
    text = DASH_SPACED_RE.sub(", ", text)
    return text


def T(slide_no, i):
    return fix_dashes(S(slide_no)[i])


def split_item(text):
    """Deep-dive bullets in the deck are 'Title  detail sentence' (a
    double space where the line break used to be)."""
    text = fix_dashes(text)
    if "  " in text:
        title, rest = text.split("  ", 1)
        return title.strip(), rest.strip()
    return text, ""


def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


# --------------------------------------------------------------- content
# Tab 1: Overview (slide 1)
OVERVIEW = {
    "h1": T(1, 1),
    "sub": T(1, 2),
    "body": T(1, 3),
    "prepared_template": T(1, 4),
    "contact": T(1, 5),
}

# Tab 2: The problem (slides 2, 3)
PROBLEM = {
    "h1": T(2, 0),
    "sub": T(2, 1),
    "points": [(T(2, 3), T(2, 4)), (T(2, 6), T(2, 7)), (T(2, 9), T(2, 10))],
    "stats": [(T(3, 1), T(3, 2)), (T(3, 3), T(3, 4)), (T(3, 5), T(3, 6))],
    "closing": T(3, 7),
}

# Tab 3: Six divisions (slides 4, 5, 11, 12, 13)
SOLUTION_INTRO = {
    "h1": T(4, 1),
    "body": T(4, 2),
    "points": [T(4, 4), T(4, 5), T(4, 6)],
}
DIVISIONS = [
    {"title": T(5, 2), "desc": T(5, 3), "detail": [split_item(S(11)[3]), split_item(S(11)[5]), split_item(S(11)[7]), split_item(S(11)[9])]},
    {"title": T(5, 4), "desc": T(5, 5), "detail": [split_item(S(12)[3]), split_item(S(12)[5])]},
    {"title": T(5, 6), "desc": T(5, 7), "detail": [split_item(S(12)[7]), split_item(S(12)[9])]},
    {"title": T(5, 8), "desc": T(5, 9), "detail": [split_item(S(13)[3])]},
    {"title": T(5, 10), "desc": T(5, 11), "detail": [split_item(S(13)[5])]},
    {"title": T(5, 12), "desc": T(5, 13), "detail": [split_item(S(13)[7]), split_item(S(13)[9])]},
]

# Tab 4: How it works (slide 6)
HOW = {
    "h1": "How it works",
    "sub": T(6, 1),
    "steps": [(T(6, 2), T(6, 3), T(6, 4)), (T(6, 5), T(6, 6), T(6, 7)), (T(6, 8), T(6, 9), T(6, 10))],
}

# Tab 5: A sample number (slides 7, 8)
IMPACT = {
    "h1": T(7, 0),
    "body": T(7, 1),
    "meter_labels": [(T(7, 2), T(7, 3)), (T(7, 4), T(7, 5)), (T(7, 6), T(7, 7)), (T(7, 8), T(7, 9))],
    "sample_h1": T(8, 0),
    "sample_body": T(8, 1),
    "sample_stats": [(T(8, 2), T(8, 3)), (T(8, 4), T(8, 5)), (T(8, 6), T(8, 7)), (T(8, 8), T(8, 9))],
    "sample_close": T(8, 10),
}

# Tab 6: Proof (slide 9)
PROOF = {
    "h1": T(9, 0),
    "items": [(T(9, 2), T(9, 3)), (T(9, 5), T(9, 6)), (T(9, 8), T(9, 9))],
}

# Tab 7: Membership (slide 10, tiers overridden per website decision 2026-09-13)
MEMBERSHIP = {
    "h1": T(10, 0),
    "sub": T(10, 1),
    "essential": {"title": T(10, 2), "price": T(10, 3), "desc": T(10, 4),
                  "setup": PRICES["membership"]["essential"]["price"]},
    "professional": {"title": T(10, 5), "price": T(10, 6), "desc": T(10, 7),
                      "setup": PRICES["membership"]["professional"]["price"]},
    "built_around": "Built around your business. Starts with a 30 minute Back Office Audit.",
    "note": T(10, 14),
}

# Tab 8: Next step (slides 14, 15)
NEXT = {
    "h1": T(14, 0),
    "steps": [(T(14, 1), T(14, 2), T(14, 3)), (T(14, 4), T(14, 5), T(14, 6)), (T(14, 7), T(14, 8), T(14, 9))],
    "headline": f"{T(14, 10)} {T(14, 11)} {T(14, 12)}",
    "note": T(14, 13),
    "tagline": T(15, 1),
    "closing": T(15, 2),
    "signature": T(15, 3),
    "contact": T(15, 4),
}

# --------------------------------------------------------- TIM math (JS)
# Same LINES/compute() model as A1_Sales/Total Impact Model/Atlas_One_Total_Impact_Model.html,
# fed with the same 25-employee sample line items as that file's SAMPLE constant
# (which is the deck's own slide 8 numbers, reconciled there to $13,117 net), then
# scaled by employee count. No new formula: gross = sum(included lines), net = gross - fee.
TIM_JS = """
var TIM_SAMPLE_LINES = {payroll_admin:4200, health_premium:7600, section_125:1900, wc_premium:3100, software_stack:1600};
var TIM_SAMPLE_HOURS_PER_MO = 22, TIM_SAMPLE_EE = 25, TIM_SAMPLE_GAPS = 3;
var TIM_FEE_MONTHLY = 399, TIM_FEE_SETUP = 495; /* Professional membership, same as the deck sample */
function timMoney(n){ n = Math.round(n); var a = Math.abs(n).toLocaleString("en-US"); return (n<0? "($"+a+")" : "$"+a); }
function timCompute(ee){
  var scale = Math.max(ee, 1) / TIM_SAMPLE_EE;
  var gross = 0;
  for (var k in TIM_SAMPLE_LINES) gross += TIM_SAMPLE_LINES[k] * scale;
  var fee = -(TIM_FEE_MONTHLY * 12) - TIM_FEE_SETUP;
  var net = gross + fee;
  var hours = Math.round(TIM_SAMPLE_HOURS_PER_MO * scale);
  return {gross: gross, fee: -fee, net: net, hours: hours, gaps: TIM_SAMPLE_GAPS};
}
"""

TABS = [
    ("overview", "Overview"),
    ("problem", "The problem"),
    ("divisions", "Six divisions"),
    ("how", "How it works"),
    ("impact", "A sample number"),
    ("proof", "Proof"),
    ("membership", "Membership"),
    ("next", "Next step"),
]

BOOK_URL = "https://api.leadconnectorhq.com/widget/groups/book-david"
PDF_HREF = "Atlas_One_Prospect_Pitch_Deck_First_Meeting.pdf"


def book_btn(extra_class=""):
    return (f'<a class="btn book {extra_class}" href="{BOOK_URL}" target="_blank" rel="noopener">'
            f'Book the 30 minute Back Office Audit</a>')


def points_grid(points):
    out = ['<div class="points">']
    for i, (t, d) in enumerate(points, 1):
        out.append(f'<div class="point"><span class="pn">{i}</span><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></div>')
    out.append('</div>')
    return "".join(out)


def stat_row(stats):
    out = ['<div class="stats">']
    for big, small in stats:
        out.append(f'<div class="stat"><div class="big">{esc(big)}</div><div class="small">{esc(small)}</div></div>')
    out.append('</div>')
    return "".join(out)


def build_overview():
    return f"""
    <section class="tabpanel" id="tab-overview">
      <div class="hero">
        <div class="mark">{LOGO_SVG}</div>
        <h1>{esc(OVERVIEW['h1'])}</h1>
        <p class="sub">{esc(OVERVIEW['sub'])}</p>
        <p class="lede">{esc(OVERVIEW['body'])}</p>
        <p class="prepared" id="preparedLine">{esc(OVERVIEW['prepared_template'])}</p>
        <p class="contact">{esc(OVERVIEW['contact'])}</p>
        <div class="cta-row">{book_btn()}<a class="btn ghost" href="{PDF_HREF}" download>Download PDF</a></div>
      </div>
    </section>"""


def build_problem():
    return f"""
    <section class="tabpanel" id="tab-problem">
      <h1>{esc(PROBLEM['h1'])}</h1>
      <p class="sub">{esc(PROBLEM['sub'])}</p>
      {points_grid(PROBLEM['points'])}
      {stat_row(PROBLEM['stats'])}
      <p class="closing">{esc(PROBLEM['closing'])}</p>
      <div class="cta-row">{book_btn()}</div>
    </section>"""


def build_divisions():
    cards = []
    for i, d in enumerate(DIVISIONS):
        detail_items = "".join(
            f'<li><b>{esc(t)}</b> {esc(r)}</li>' for t, r in d["detail"] if t
        )
        cards.append(f"""
        <div class="divcard" data-div="{i}">
          <button class="divhead" type="button" aria-expanded="false">
            <span class="dt">{esc(d['title'])}</span>
            <span class="chev">+</span>
          </button>
          <p class="dd">{esc(d['desc'])}</p>
          <ul class="detail" hidden>{detail_items}</ul>
        </div>""")
    return f"""
    <section class="tabpanel" id="tab-divisions">
      <h1>{esc(SOLUTION_INTRO['h1'])}</h1>
      <p class="lede">{esc(SOLUTION_INTRO['body'])}</p>
      <div class="divgrid">{''.join(cards)}</div>
      <p class="hint">Tap a division for the detail behind it.</p>
      <div class="cta-row">{book_btn()}</div>
    </section>"""


def build_how():
    steps = "".join(
        f'<div class="step"><span class="sn">{esc(n)}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
        for n, t, d in HOW["steps"]
    )
    return f"""
    <section class="tabpanel" id="tab-how">
      <h1>{esc(HOW['h1'])}</h1>
      <p class="sub">{esc(HOW['sub'])}</p>
      <div class="steps">{steps}</div>
      <div class="cta-row">{book_btn()}</div>
    </section>"""


def build_impact():
    meters = "".join(
        f'<div class="meter"><div class="ml">{esc(l)}</div><div class="ms">{esc(s)}</div></div>'
        for l, s in IMPACT["meter_labels"]
    )
    return f"""
    <section class="tabpanel" id="tab-impact">
      <h1>{esc(IMPACT['h1'])}</h1>
      <p class="lede">{esc(IMPACT['body'])}</p>
      <div class="meters">{meters}</div>
      <div class="samplebox">
        <h2 id="impactHeading">{esc(IMPACT['sample_h1'])}</h2>
        <p class="sub" id="impactSub">{esc(IMPACT['sample_body'])}</p>
        <div class="stats" id="impactStats">
          <div class="stat"><div class="big" id="stFound">{esc(IMPACT['sample_stats'][0][0])}</div><div class="small">{esc(IMPACT['sample_stats'][0][1])}</div></div>
          <div class="stat"><div class="big" id="stHours">{esc(IMPACT['sample_stats'][1][0])}</div><div class="small">{esc(IMPACT['sample_stats'][1][1])}</div></div>
          <div class="stat"><div class="big" id="stGaps">{esc(IMPACT['sample_stats'][2][0])}</div><div class="small">{esc(IMPACT['sample_stats'][2][1])}</div></div>
          <div class="stat"><div class="big" id="stFee">{esc(IMPACT['sample_stats'][3][0])}</div><div class="small">{esc(IMPACT['sample_stats'][3][1])}</div></div>
        </div>
        <p class="closing" id="impactClose">{esc(IMPACT['sample_close'])}</p>
      </div>
      <div class="cta-row">{book_btn()}</div>
    </section>"""


def build_proof():
    cards = "".join(
        f'<div class="proofcard"><span class="check">&#10003;</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
        for t, d in PROOF["items"]
    )
    return f"""
    <section class="tabpanel" id="tab-proof">
      <h1>{esc(PROOF['h1'])}</h1>
      <div class="proofgrid">{cards}</div>
      <div class="cta-row">{book_btn()}</div>
    </section>"""


def build_membership():
    e, p = MEMBERSHIP["essential"], MEMBERSHIP["professional"]
    return f"""
    <section class="tabpanel" id="tab-membership">
      <h1>{esc(MEMBERSHIP['h1'])}</h1>
      <p class="sub">{esc(MEMBERSHIP['sub'])}</p>
      <div class="tiers">
        <div class="tier">
          <h3>{esc(e['title'])}</h3>
          <div class="price">{esc(e['price'])}</div>
          <p>{esc(e['desc'])}</p>
          <p class="setup">{esc(e['setup'])}</p>
        </div>
        <div class="tier feat">
          <h3>{esc(p['title'])}</h3>
          <div class="price">{esc(p['price'])}</div>
          <p>{esc(p['desc'])}</p>
          <p class="setup">{esc(p['setup'])}</p>
        </div>
        <div class="tier built">
          <h3>Enterprise</h3>
          <p class="builtline">{esc(MEMBERSHIP['built_around'])}</p>
        </div>
        <div class="tier built">
          <h3>Concierge</h3>
          <p class="builtline">{esc(MEMBERSHIP['built_around'])}</p>
        </div>
      </div>
      <p class="note">{esc(MEMBERSHIP['note'])}</p>
      <div class="cta-row">{book_btn()}</div>
    </section>"""


def build_next():
    steps = "".join(
        f'<div class="step"><span class="sn">{esc(n)}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
        for n, t, d in NEXT["steps"]
    )
    return f"""
    <section class="tabpanel" id="tab-next">
      <h1>{esc(NEXT['h1'])}</h1>
      <div class="steps">{steps}</div>
      <h2 class="bigline">{esc(NEXT['headline'])}</h2>
      <p class="sub">{esc(NEXT['note'])}</p>
      <div class="closingblock">
        <p class="tagline">{esc(NEXT['tagline'])}</p>
        <p>{esc(NEXT['closing'])}</p>
        <p class="signature">{esc(NEXT['signature'])}</p>
        <p class="contact">{esc(NEXT['contact'])}</p>
      </div>
      <div class="cta-row">{book_btn()}<a class="btn ghost" href="{PDF_HREF}" download>Download PDF</a></div>
    </section>"""


PANEL_BUILDERS = {
    "overview": build_overview, "problem": build_problem, "divisions": build_divisions,
    "how": build_how, "impact": build_impact, "proof": build_proof,
    "membership": build_membership, "next": build_next,
}

CSS = """
* { box-sizing: border-box; }
:root {
  --navy: #23304D; --peri: #788DE3; --paper: #FAFAF8; --mist: #DBE4ED;
  --bg: var(--paper); --card: var(--paper); --card-border: var(--mist);
  --text: var(--navy); --text-soft: rgba(35,48,77,0.78);
  --stat-bg: var(--navy); --stat-text: var(--paper);
  --built-bg: var(--mist); --line: var(--mist);
  --btn-book-bg: var(--navy); --btn-book-text: var(--paper);
  --mark-ink: var(--navy);
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: var(--navy); --card: rgba(250,250,248,0.06); --card-border: rgba(120,141,227,0.4);
    --text: var(--paper); --text-soft: rgba(250,250,248,0.78);
    --stat-bg: var(--peri); --stat-text: var(--navy);
    --built-bg: rgba(219,228,237,0.14); --line: rgba(120,141,227,0.4);
    --btn-book-bg: var(--peri); --btn-book-text: var(--navy);
    --mark-ink: var(--paper);
  }
}
html, body { margin: 0; padding: 0; }
body {
  background: var(--bg); color: var(--text);
  font-family: 'DM Sans', -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  font-size: 16px; line-height: 1.5;
}
h1, h2, h3 { font-family: 'Horas', Georgia, serif; margin: 0 0 8px 0; color: var(--text); }
h1 { font-size: 30px; letter-spacing: -0.02em; line-height: 1.12; }
h2 { font-size: 22px; }
h3 { font-size: 17px; }
p { margin: 0 0 10px 0; }
a { color: var(--text); }
.sub { font-size: 17px; color: var(--text); opacity: 0.85; margin-bottom: 14px; }
.lede { max-width: 62ch; font-size: 15px; }
.closing { font-style: italic; opacity: 0.85; margin-top: 14px; }
.note { font-size: 13px; font-style: italic; opacity: 0.75; }

header.top {
  position: sticky; top: 0; z-index: 20;
  background: var(--bg); border-bottom: 2px solid var(--line);
  padding: 10px 20px;
}
.topinner { max-width: 1180px; margin: 0 auto; display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
.brandmark { display: flex; align-items: center; gap: 10px; }
.brandmark svg { height: 30px; width: auto; display: block; }
.brandtext { display: flex; flex-direction: column; line-height: 1.1; }
.brandtext .name { font-family: 'Horas', Georgia, serif; font-size: 15px; font-weight: 700; }
.brandtext .tag { font-size: 10.5px; font-style: italic; color: var(--peri); }
.forwhom { font-size: 13px; opacity: 0.8; margin-left: auto; }
nav.tabs { display: flex; gap: 4px; flex-wrap: wrap; margin-top: 8px; }
nav.tabs button {
  font-family: 'DM Sans', sans-serif; font-size: 13.5px; font-weight: 700;
  background: transparent; border: none; border-bottom: 3px solid transparent;
  color: var(--text); opacity: 0.65; padding: 8px 10px; cursor: pointer;
}
nav.tabs button[aria-selected="true"] { opacity: 1; border-bottom-color: var(--peri); }
select.tabselect { display: none; width: 100%; font-size: 15px; padding: 10px; margin-top: 8px;
  border: 1.5px solid var(--line); border-radius: 6px; background: var(--card); color: var(--text);
  font-family: 'DM Sans', sans-serif; }

main { max-width: 1180px; margin: 0 auto; padding: 26px 20px 60px 20px; min-height: 60vh; }
.tabpanel { display: none; }
.tabpanel.active { display: block; }

.hero { max-width: 760px; }
.hero .mark { margin-bottom: 10px; }
.hero .mark svg { height: 46px; width: auto; }
.prepared { font-weight: 700; margin-top: 16px; }
.contact { font-size: 14px; opacity: 0.8; }

.cta-row { margin-top: 22px; display: flex; gap: 12px; flex-wrap: wrap; }
.btn { display: inline-block; text-decoration: none; font-weight: 700; font-size: 14.5px;
  padding: 12px 18px; border-radius: 7px; }
.btn.book { background: var(--btn-book-bg); color: var(--btn-book-text); }
.btn.ghost { background: transparent; color: var(--text); border: 1.5px solid var(--text); }

.points { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 18px 0; }
.point { display: flex; gap: 10px; background: var(--card); border: 1px solid var(--card-border); border-radius: 8px; padding: 14px; }
.point .pn { font-family: 'Horas', Georgia, serif; font-size: 20px; color: var(--peri); font-weight: 700; }
.point h3 { font-size: 15px; margin-bottom: 4px; }
.point p { font-size: 13.5px; margin: 0; }

.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 14px; margin: 16px 0; }
.stat { background: var(--stat-bg); color: var(--stat-text); border-radius: 8px; padding: 16px; }
.stat .big { font-family: 'Horas', Georgia, serif; font-size: 26px; }
.stat .small { font-size: 12.5px; opacity: 0.9; margin-top: 4px; }

.divgrid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 16px 0 6px 0; }
.divcard { background: var(--card); border: 1px solid var(--card-border); border-radius: 8px; padding: 12px 14px; }
.divhead { all: unset; display: flex; justify-content: space-between; align-items: center; width: 100%; cursor: pointer; }
.divhead .dt { font-family: 'Horas', Georgia, serif; font-size: 15.5px; font-weight: 700; }
.divhead .chev { color: var(--peri); font-size: 18px; font-weight: 700; }
.divcard .dd { font-size: 13px; margin: 6px 0 0 0; }
.divcard .detail { margin: 10px 0 0 0; padding-left: 18px; font-size: 12.5px; }
.divcard .detail li { margin-bottom: 5px; }
.divcard[data-open="true"] .chev { transform: rotate(45deg); }
.hint { font-size: 12.5px; opacity: 0.7; }

.steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 18px 0; }
.step { background: var(--card); border: 1px solid var(--card-border); border-radius: 8px; padding: 16px; }
.step .sn { font-family: 'Horas', Georgia, serif; font-size: 22px; color: var(--peri); }
.step p { font-size: 13.5px; margin: 4px 0 0 0; }

.meters { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 16px 0; }
.meter { background: var(--built-bg); border-radius: 8px; padding: 12px; }
.meter .ml { font-weight: 700; font-size: 14px; }
.meter .ms { font-size: 12px; margin-top: 2px; }

.samplebox { background: var(--card); border: 1.5px solid var(--peri); border-radius: 10px; padding: 18px; margin-top: 18px; }

.proofgrid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 18px 0; }
.proofcard { background: var(--card); border: 1px solid var(--card-border); border-radius: 8px; padding: 16px; }
.proofcard .check { color: var(--peri); font-size: 20px; font-weight: 700; }
.proofcard p { font-size: 13.5px; }

.tiers { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 18px 0 8px 0; }
.tier { background: var(--card); border: 1px solid var(--card-border); border-radius: 8px; padding: 16px; }
.tier.feat { border-color: var(--peri); border-width: 2px; }
.tier .price { font-family: 'Horas', Georgia, serif; font-size: 22px; margin: 4px 0; }
.tier p { font-size: 13px; }
.tier .setup { font-size: 11.5px; opacity: 0.7; font-style: italic; }
.tier.built { display: flex; flex-direction: column; justify-content: center; background: var(--built-bg); }
.tier.built .builtline { font-size: 13px; font-weight: 700; margin: 0; }

.bigline { margin-top: 8px; }
.closingblock { margin-top: 20px; border-top: 1px solid var(--line); padding-top: 16px; }
.closingblock .tagline { font-family: 'Horas', Georgia, serif; font-size: 18px; color: var(--peri); }
.signature { font-weight: 700; margin-top: 8px; margin-bottom: 0; }

footer.site { border-top: 2px solid var(--line); padding: 18px 20px 30px 20px; text-align: center; }
footer.site p { font-size: 12.5px; opacity: 0.75; margin: 2px 0; }

@media (max-width: 760px) {
  nav.tabs { display: none; }
  select.tabselect { display: block; }
  .points, .divgrid, .steps, .proofgrid { grid-template-columns: 1fr; }
  .meters { grid-template-columns: repeat(2, 1fr); }
  .tiers { grid-template-columns: 1fr; }
  h1 { font-size: 24px; }
  .forwhom { margin-left: 0; width: 100%; order: 3; }
}

@media print {
  header.top, footer.site .cta-row, nav.tabs, select.tabselect { display: none !important; }
  .tabpanel { display: block !important; page-break-after: always; }
  .cta-row { display: none !important; }
  body { background: var(--paper); color: var(--navy); }
  .stat { background: var(--navy); color: var(--paper); }
}
"""

JS = """
(function(){
  var params = new URLSearchParams(location.search);
  var company = (params.get('for') || '').trim();
  var industry = (params.get('industry') || '').trim();
  var eeParam = parseInt(params.get('ee'), 10);
  var ee = isNaN(eeParam) || eeParam <= 0 ? null : eeParam;

  if (company) {
    document.getElementById('preparedLine').textContent = 'Prepared for ' + company;
    document.querySelectorAll('.forwhom').forEach(function(el){ el.textContent = 'Prepared for ' + company; });
  }

  """ + TIM_JS + """
  if (ee) {
    var c = timCompute(ee);
    var industryWord = industry ? (industry.charAt(0).toUpperCase() + industry.slice(1) + ' ') : '';
    document.getElementById('impactHeading').textContent = 'Your sample number: ' + ee + '-employee ' + (industry ? industry : '') + ' company';
    document.getElementById('impactSub').textContent = 'An illustrative first year for a ' + ee + '-person ' + industryWord.toLowerCase() + 'company, scaled from the Total Impact Model. Your Audit replaces every figure here with your own, net of my fee.';
    document.getElementById('stFound').textContent = timMoney(c.gross);
    document.getElementById('stFound').nextElementSibling && (document.getElementById('stFound').parentElement.querySelector('.small').textContent = 'found across payroll, benefits, comp and software overlap (illustrative)');
    document.getElementById('stHours').textContent = c.hours + ' hrs / mo';
    document.getElementById('stHours').parentElement.querySelector('.small').textContent = 'handed back to the owner and the office manager (illustrative)';
    document.getElementById('stGaps').textContent = c.gaps + ' gaps';
    document.getElementById('stFee').textContent = timMoney(c.fee);
    document.getElementById('stFee').parentElement.querySelector('.small').textContent = 'Professional membership for the year, shown, never hidden';
    document.getElementById('impactClose').textContent = '= ' + timMoney(c.net) + ' net in year one, plus the hours. Yours comes from the Audit.';
  }

  var tabs = Array.prototype.slice.call(document.querySelectorAll('nav.tabs button'));
  var select = document.querySelector('select.tabselect');
  var panels = {};
  document.querySelectorAll('.tabpanel').forEach(function(p){ panels[p.id.replace('tab-','')] = p; });

  function activate(key, push){
    Object.keys(panels).forEach(function(k){
      panels[k].classList.toggle('active', k === key);
    });
    tabs.forEach(function(b){ b.setAttribute('aria-selected', b.getAttribute('data-tab') === key ? 'true' : 'false'); });
    if (select) select.value = key;
    if (push !== false) history.replaceState(null, '', '#' + key);
  }

  tabs.forEach(function(b){
    b.addEventListener('click', function(){ activate(b.getAttribute('data-tab')); });
  });
  if (select) select.addEventListener('change', function(){ activate(select.value); });

  document.querySelectorAll('.divhead').forEach(function(btn){
    btn.addEventListener('click', function(){
      var card = btn.closest('.divcard');
      var detail = card.querySelector('.detail');
      var open = card.getAttribute('data-open') === 'true';
      document.querySelectorAll('.divcard').forEach(function(c){
        c.setAttribute('data-open', 'false');
        c.querySelector('.detail').hidden = true;
        c.querySelector('.divhead').setAttribute('aria-expanded', 'false');
      });
      if (!open) {
        card.setAttribute('data-open', 'true');
        detail.hidden = false;
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  var initial = (location.hash || '').replace('#', '');
  if (!panels[initial]) initial = 'overview';
  activate(initial, false);
})();
"""


def build():
    tab_buttons = "".join(
        f'<button type="button" data-tab="{key}" aria-selected="{"true" if i == 0 else "false"}">{esc(label)}</button>'
        for i, (key, label) in enumerate(TABS)
    )
    tab_options = "".join(f'<option value="{key}">{esc(label)}</option>' for key, label in TABS)
    panels = "".join(PANEL_BUILDERS[key]() for key, _ in TABS)

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Atlas One, Prepared For You</title>
<style>
{FONTS_CSS}
{CSS}
</style>
</head>
<body>
<header class="top">
  <div class="topinner">
    <div class="brandmark">
      {LOGO_SVG}
      <div class="brandtext"><span class="name">ATLAS ONE SOLUTIONS</span><span class="tag">One Call Solves Everything.</span></div>
    </div>
    <span class="forwhom"></span>
  </div>
  <div class="topinner">
    <nav class="tabs" role="tablist">{tab_buttons}</nav>
    <select class="tabselect" aria-label="Choose a section">{tab_options}</select>
  </div>
</header>
<main>
{panels}
</main>
<footer class="site">
  <p>Atlas One Solutions LLC &middot; Lehi, Utah &middot; Serving businesses in all 50 states</p>
  <p><a href="tel:+13802255217">380-225-5217</a> &middot; <a href="mailto:David@AtlasOneSolutions.com">David@AtlasOneSolutions.com</a></p>
</footer>
<script>
{JS}
</script>
</body>
</html>
"""
    out_path = os.path.join(HERE, "index.html")
    with io.open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", out_path, len(html), "bytes")


if __name__ == "__main__":
    build()
