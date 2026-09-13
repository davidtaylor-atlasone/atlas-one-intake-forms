#!/usr/bin/env python3
"""Run AC job 4: Atlas_One_Benefits_Routing_Tool.html. Rules from 13 Benefits Strategy/Atlas_One_Member_Program_Spec_2026-08-29.docx
section 4 and 5 and BUILD-INDEX rules 14 and 20 plus the AHP note. usage: build_routing_tool.py <out.html>"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from a1shell import head, topbar
CSS = """
.routes{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:10px}
@media(max-width:900px){.routes{grid-template-columns:repeat(3,1fr)}}@media(max-width:560px){.routes{grid-template-columns:1fr 1fr}}
.rt{border:1px solid var(--line);border-radius:12px;padding:10px 12px;background:#fff;font-size:12px;color:var(--muted)}
.rt .nm{font-family:'Horas';font-size:14px;color:var(--navy);margin-bottom:2px}
.rt.pick{border:2px solid var(--peri);background:var(--tint)}.rt.pick .nm::before{content:"\\2192\\00a0"}
.rt.alt{border-style:dashed}.rt.alt .nm::before{content:"\\25CB\\00a0"}
.rt.out{opacity:.55}.rt.out .nm::before{content:"\\2715\\00a0"}
.result{background:var(--navy);color:#fff;border-radius:16px;padding:22px 24px;margin-top:14px}
.result .eyebrow{font-size:11px;font-weight:700;letter-spacing:.08em;color:var(--perih)}
.result h2{font-size:26px;margin:4px 0 8px;color:#fff}
.result p{margin:0 0 8px;font-size:14.5px;color:#c9d2ea}
.ask{background:var(--peri);color:var(--navy);border-radius:12px;padding:12px 16px;margin-top:12px}
.ask .l{font-size:11px;font-weight:700;letter-spacing:.06em}.ask .q{font-family:'Horas';font-size:17px;margin-top:2px}
.flags{margin-top:10px}.flag{display:flex;gap:8px;align-items:flex-start;font-size:13px;padding:6px 0;border-top:1px solid #3a4a70;color:#e6ebf5}
.flag::before{content:"\\25B2";color:var(--perih);font-size:10px;margin-top:4px;flex:none}
.say{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px}@media(max-width:600px){.say{grid-template-columns:1fr}}
.say div{border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:13px;background:#fff}
.say .no{border-left:4px solid var(--navy)}.say .ok{border-left:4px solid var(--peri)}
.say b{display:block;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:3px}
"""
BODY = r"""
<div class="wrap">
<div class="hero"><h1>Benefits routing: which door does this prospect walk through?</h1><p>Internal. Enter what you know from the call and read the route, the two sentence why, and the one question to ask next. Atlas One is how they get coverage, not what covers them.</p></div>

<div class="card">
  <h2>What we know</h2><p class="sub">Every field changes the route. Leave a field at "not sure" and the tool tells you to ask.</p>
  <div class="g3">
    <div><label>Entity type</label><select id="entity">
      <option value="">Not sure yet</option>
      <option value="sole">Sole proprietor, no entity</option>
      <option value="smllc">Single member LLC or S corp, owner is the only worker</option>
      <option value="scorp">S corp or LLC with W-2 employees</option>
      <option value="ccorp">C corp</option>
      <option value="partner">Partnership</option>
      <option value="nonprofit">Nonprofit</option>
      <option value="multi">Multi entity group (common ownership)</option></select></div>
    <div><label>W-2 employees, not counting the owner</label><input id="ee" inputmode="numeric" placeholder="0"></div>
    <div><label>Who needs coverage</label><select id="who">
      <option value="">Not sure yet</option>
      <option value="owner">Owner only</option>
      <option value="both">Owner and employees</option>
      <option value="ees">Employees only (owner is covered elsewhere)</option></select></div>
  </div>
  <div class="g3" style="margin-top:10px">
    <div><label>Current coverage</label><select id="cov">
      <option value="">Not sure yet</option>
      <option value="none">None today</option>
      <option value="grp_happy">Group plan, and they like it</option>
      <option value="grp_shock">Group plan, renewal shock or unhappy</option>
      <option value="peo">Group plan through a PEO today</option>
      <option value="ichra">ICHRA or a stipend today</option>
      <option value="indiv">Everyone buys their own (individual or spouse plans)</option></select></div>
    <div><label>Employer budget per employee per month ($)</label><input id="budget" inputmode="decimal" placeholder="e.g. 450"></div>
    <div><label>Main goal</label><select id="goal">
      <option value="">Not sure yet</option>
      <option value="all">Hand off the whole back office</option>
      <option value="cap">Cap the cost, stop renewal shock</option>
      <option value="rich">Richer benefits to recruit and keep people</option>
      <option value="cheap">Lowest premium for the same coverage</option>
      <option value="owner">Coverage for the owner, nothing else changes</option>
      <option value="keep">Keep the plan, fix everything around it</option></select></div>
  </div>
  <div style="margin-top:10px"><label>States with employees (tap each)</label><div class="chips" id="states"></div></div>
  <div class="g3" style="margin-top:10px">
    <div><label>Carrier program filed in every one of those states?</label><select id="filed"><option value="unk">Not confirmed</option><option value="yes">Yes, confirmed for each state</option><option value="no">No</option></select></div>
    <div><label>Group health history</label><select id="health"><option value="unk">Not sure</option><option value="clean">No large claims, mostly young or healthy</option><option value="mixed">Mixed</option><option value="high">Known high claims or ongoing conditions</option></select></div>
    <div><label>Prospect notes</label><input id="notes" placeholder="Anything to carry into the summary"></div>
  </div>
</div>

<div class="card">
  <h2>The five doors</h2><p class="sub">Arrow: the route. Circle: a fair alternative to name on the call. Cross: not available for this prospect.</p>
  <div class="routes" id="routes"></div>
</div>

<div class="result" id="result">
  <div class="eyebrow">RECOMMENDED ROUTE</div>
  <h2 id="rName">Fill in the entity type and the headcount</h2>
  <p id="rWhy">The route and the reason appear here as you type. Say the reason out loud on the call.</p>
  <div class="ask"><div class="l">THE ONE QUESTION TO ASK NEXT</div><div class="q" id="rAsk">How many W-2 employees are on payroll today, not counting you?</div></div>
  <div class="flags" id="rFlags"></div>
</div>

<div class="card noprint">
  <h2>Say it this way</h2><p class="sub">The compliance guardrails from the Member Program spec. The left column is a DOI complaint; the right column is the same idea said correctly.</p>
  <div class="say">
    <div class="no"><b>Never say</b>"The Atlas One health plan"</div><div class="ok"><b>Say instead</b>"Health coverage through Atlas One's carrier partners"</div>
    <div class="no"><b>Never say</b>"Our master plan"</div><div class="ok"><b>Say instead</b>"A master plan we place you into" (name the actual sponsor when asked)</div>
    <div class="no"><b>Never say</b>"Join our group and save 20%"</div><div class="ok"><b>Say instead</b>"We will quote you against your current plan and show you the difference in writing"</div>
    <div class="no"><b>Never say</b>"Members get health insurance"</div><div class="ok"><b>Say instead</b>"Members get benefits placement, comparison and enrollment support"</div>
    <div class="no"><b>Never say</b>"Guaranteed savings"</div><div class="ok"><b>Say instead</b>"Documented savings measured against your premiums at onboarding"</div>
    <div class="no"><b>Never say</b>"We are a PEO" or "we co-employ"</div><div class="ok"><b>Say instead</b>"We broker PEO. We place you with the right one and we manage it."</div>
  </div>
</div>

<div class="callout"><b>Standing rules encoded here.</b> Under 500 enrolled lives every plan in a fully insured offering comes off one carrier's shelf. Alternative funding replaces the funding model for the whole group; it is never a tier inside a carrier menu. Atlas One never holds the policy, never bears risk, never pays claims. Association health plans are closed to working owners with no employees (DOL rescission of the 2018 AHP rule, effective 29 April 2024). ICHRA needs no employer group plan and no minimum group size, but the person reimbursed must be a W-2 employee; owners of S corps, partnerships and sole proprietorships are generally not eligible to participate themselves. Never print who quoted a plan.</div>
<p class="hint">Internal decision aid, not legal or tax advice. The membership agreement, any multi employer arrangement and ICHRA owner eligibility go through counsel. Nothing typed here leaves the device.</p>
</div>
<script>
function $(id){return document.getElementById(id);}
function n(v){return parseFloat(String(v==null?'':v).replace(/[^0-9.\-]/g,''))||0;}
var STLIST=["UT","AZ","ID","NV","CO","WY","CA","OR","WA","TX","FL","NM","MT","OK","KS","NE","GA","NC","TN","Other"];
var st={};
var ROUTES=[
 ['carrier','Group plan through carrier partners','Small or large group, fully insured, one carrier under 500 lives. Carrier program or trust where the state is filed.'],
 ['peo','PEO plan through co-employment','Large group rates by joining the PEO’s single employer plan. Payroll moves with it.'],
 ['ichra','ICHRA','Employer sets a monthly dollar amount; each employee buys an individual plan and is reimbursed tax free.'],
 ['alt','Alternative funding, whole group','Level funded or reference based pricing for the entire group. Replaces the carrier menu, never sits inside it.'],
 ['indiv','Individual coverage','Marketplace or off exchange plan for the owner or each person, placed by Atlas One as broker.']
];
function pick(){
 var ent=$('entity').value,ee=n($('ee').value),who=$('who').value,cov=$('cov').value,budget=n($('budget').value),goal=$('goal').value,filed=$('filed').value,health=$('health').value;
 var states=Object.keys(st).filter(function(k){return st[k];});var multi=states.length>1;
 var ownerOnly=(ent==='sole'||ent==='smllc')||(ee===0&&(who==='owner'||ent!==''));
 var r={route:null,alts:[],out:[],why:'',ask:'',flags:[]};
 if(!ent||($('ee').value==='')){
  r.route=null;r.why='The entity type and the W-2 headcount decide the door. Everything else refines it.';
  r.ask=!ent?'Is the business an LLC, an S corp, a C corp, a partnership, or no entity at all?':'How many W-2 employees are on payroll today, not counting you?';
  render(r);return;}
 if(cov==='grp_happy'||goal==='keep'){
  r.route='keep';r.why='They like what they have, so we leave the health plan where it is and carve it out. We sell everything else: payroll, workers comp, bookkeeping, HR, technology, the membership.';
  r.ask='Who owns the health renewal today, and are you open to Atlas One quoting it in writing at the next renewal with no change until then?';
  r.alts=['carrier'];r.out=['peo','ichra','alt','indiv'];r.flags.push('Referral partner discipline: do not break a happy plan for one case. If a partner owns the benefits line, say so and move on.');
  render(r);return;}
 if(ownerOnly&&ee===0){
  r.route='indiv';r.out=['carrier','alt'];
  r.why='A working owner with no employees cannot join an association plan and, in nearly every state, cannot buy a group plan either. The clean route is an individual plan placed by Atlas One as broker, with the premium handled the right way for the entity on the tax return.';
  if(ent==='ccorp'){r.alts=['ichra','peo'];r.flags.push('C corp paying the owner W-2 wages: an ICHRA can reimburse the owner. Confirm with the CPA before promising it.');}
  else{r.alts=['peo'];r.flags.push('ICHRA does not work here: S corp shareholders over 2%, partners and sole proprietors cannot be reimbursed as participants. It becomes available the day they hire a W-2 employee.');}
  r.flags.push('If they want W-2 payroll and the whole stack for themselves, a PEO or employer of record route can carry the owner; price it honestly, it is rarely cheaper than an individual plan.');
  r.ask='Are you planning to hire a W-2 employee in the next twelve months, and is your spouse on payroll?';
  render(r);return;}
 if(ee>=1&&ee<=1){
  r.route=(goal==='cap'||cov==='indiv'||(budget>0&&budget<350))?'ichra':'carrier';
  r.alts=r.route==='ichra'?['carrier','indiv']:['ichra','indiv'];r.out=['peo','alt'];
  r.why=r.route==='ichra'?'One employee is enough for an ICHRA and the employer picks the monthly number, so cost is fixed from day one. A small group plan is possible with one non owner employee but the rate is the carrier’s, not theirs.':'With one non owner, non spouse employee most states allow a small group plan through our carrier partners, and it usually beats an individual plan for a two person group. Confirm the state’s minimum participation rule before quoting.';
  r.ask='Is the employee a non spouse, non owner working at least 30 hours, and what does the owner pay for coverage today?';
  render(r);return;}
 if(ee>=2&&ee<=50&&goal==='all'){
  r.route='peo';r.alts=['carrier','ichra'];r.out=['indiv'];if(health==='clean'&&ee>=5)r.alts.push('alt');
  r.why='Two to fifty W-2 employees who want the whole back office handled belong in the private labeled PEO plan: co-employment puts them on genuine large group rates and payroll, workers comp and HR move with it. The carve out flexibility means they keep their 401(k) or workers comp if a referral partner owns those lines.';
  r.ask='If payroll moved with the benefits, what would you need to see on the first invoice to say yes?';
  if(multi)r.flags.push(states.length+' states: the PEO route handles multi state payroll and filings in one place, which is the strongest argument for it here.');
  render(r);return;}
 if(goal==='cap'||cov==='grp_shock'&&(budget>0&&budget<400)){
  r.route='ichra';r.alts=['carrier','alt'];r.out=['indiv'];if(ee>=2&&ee<=50)r.alts.push('peo');
  r.why='They want the cost to be a number they choose rather than one a carrier hands them each October. An ICHRA is defined contribution: the employer fixes the monthly amount per class of employee and renewal shock stops.';
  r.flags.push('ICHRA honesty check: it does not lower premium through buying power. The win is the fixed contribution and no renewal shock. Say that plainly.');
  r.ask='If your health cost were a fixed dollar amount per employee that you set, what would that number be?';
  render(r);return;}
 if(ee>=5&&ee<500&&health==='clean'&&(goal==='cheap'||cov==='grp_shock')){
  r.route='alt';r.alts=['carrier','peo'];r.out=['indiv'];if(ee<=50)r.alts.push('ichra');
  r.why='A healthy group of this size can beat a fully insured renewal with a level funded or reference based design for the whole group. It replaces the funding model; the plan designs still come from one carrier partner and Atlas One never holds the risk.';
  r.flags.push('Alternative funding is never a tier next to fully insured options. Quote it as the whole menu or not at all.');
  r.ask='Can you get us the last twelve months of claims experience, or the renewal letter with the loss ratio?';
  render(r);return;}
 if(ee>=2){
  r.route='carrier';r.alts=[];r.out=['indiv'];
  if(ee<=50)r.alts.push('peo');if(ee<=50||goal==='cap')r.alts.push('ichra');if(health==='clean'&&ee>=5)r.alts.push('alt');
  var big=ee>=51;
  r.why=big?'Fifty one or more employees is a large group: we quote our carrier partners directly and the group is rated on itself. Under 500 enrolled lives every plan on the menu still comes off one carrier’s shelf.':'Two to fifty employees is small group: community rated through our carrier partners, or the carrier’s trust or program where the state is filed. One carrier for the whole menu under 500 lives.';
  if(filed==='yes')r.flags.push('Carrier program confirmed for every state: the aggregation benefit without co-employment. The carrier holds the policy, the filings and the risk.');
  else if(multi)r.flags.push(states.length+' states and the carrier program is not confirmed in each. Confirm the state list before you promise it, or route to the PEO plan which carries multi state on its own.');
  else r.flags.push('Carrier program or trust: confirm it is filed in '+(states[0]||'the state')+' before you promise it.');
  r.ask=big?'When is the renewal, and can you share the current census and the renewal letter?':'Who handles the renewal today, and would you move payroll if that made the plan cheaper?';
  render(r);return;}
 r.route='carrier';r.why='Default: quote the carrier partners in writing against whatever they have today.';r.ask='What are you paying today, per employee per month, and who is on the plan?';render(r);
}
var NAMES={carrier:'Group plan through carrier partners',peo:'PEO plan through co-employment',ichra:'ICHRA',alt:'Alternative funding for the whole group',indiv:'Individual coverage, placed by Atlas One',keep:'Leave the health plan where it is, carve it out'};
function render(r){
 $('routes').innerHTML=ROUTES.map(function(x){var cls='rt';if(r.route===x[0])cls+=' pick';else if(r.alts.indexOf(x[0])>=0)cls+=' alt';else if(r.out.indexOf(x[0])>=0)cls+=' out';
  var tag=r.route===x[0]?'Route':(r.alts.indexOf(x[0])>=0?'Alternative':(r.out.indexOf(x[0])>=0?'Not here':''));
  return '<div class="'+cls+'"><div class="nm">'+x[1]+'</div>'+(tag?'<span class="tag '+(r.route===x[0]?'peri':(r.alts.indexOf(x[0])>=0?'tint':''))+'">'+tag+'</span>':'')+'<div style="margin-top:4px">'+x[2]+'</div></div>';}).join('');
 $('rName').textContent=r.route?NAMES[r.route]:'Fill in the entity type and the headcount';
 $('rWhy').textContent=r.why;$('rAsk').textContent=r.ask;
 var f=r.flags.slice();var nts=$('notes').value.trim();if(nts)f.push('Notes: '+nts);
 var ee=n($('ee').value);if(ee>=500)f.push('500 or more enrolled lives: the single carrier rule no longer binds; a multi carrier menu is allowed.');
 $('rFlags').innerHTML=f.map(function(x){return '<div class="flag">'+x.replace(/</g,'&lt;')+'</div>';}).join('');
 try{localStorage.setItem('a1route',JSON.stringify({entity:$('entity').value,ee:$('ee').value,who:$('who').value,cov:$('cov').value,budget:$('budget').value,goal:$('goal').value,filed:$('filed').value,health:$('health').value,notes:$('notes').value,st:st}));}catch(e){}
}
$('states').innerHTML=STLIST.map(function(s){return '<span class="chip" data-st="'+s+'">'+s+'</span>';}).join('');
document.querySelectorAll('.chip').forEach(function(c){c.onclick=function(){st[c.dataset.st]=!st[c.dataset.st];c.classList.toggle('on',!!st[c.dataset.st]);pick();};});
['entity','ee','who','cov','budget','goal','filed','health','notes'].forEach(function(id){$(id).oninput=pick;$(id).onchange=pick;});
$('btnClear').onclick=function(){['entity','who','cov','goal'].forEach(function(id){$(id).value='';});['ee','budget','notes'].forEach(function(id){$(id).value='';});$('filed').value='unk';$('health').value='unk';st={};document.querySelectorAll('.chip').forEach(function(c){c.classList.remove('on');});pick();};
$('btnCopy').onclick=function(){var t='Benefits route for prospect: '+$('rName').textContent+'\n'+$('rWhy').textContent+'\nAsk next: '+$('rAsk').textContent;var f=[].slice.call(document.querySelectorAll('.flag')).map(function(x){return '- '+x.textContent;});if(f.length)t+='\n'+f.join('\n');
 try{navigator.clipboard.writeText(t);$('btnCopy').textContent='Copied';setTimeout(function(){$('btnCopy').textContent='Copy summary';},1200);}catch(e){prompt('Copy:',t);}};
try{var s=JSON.parse(localStorage.getItem('a1route')||'null');if(s){['entity','ee','who','cov','budget','goal','filed','health','notes'].forEach(function(id){if(s[id]!=null)$(id).value=s[id];});st=s.st||{};document.querySelectorAll('.chip').forEach(function(c){c.classList.toggle('on',!!st[c.dataset.st]);});}}catch(e){}
pick();
</script>
</body></html>
"""
out = sys.argv[1]
html = head('Atlas One: Benefits Routing Tool', CSS) + '<body>' + topbar('Benefits routing decision tool (internal)', '<button class="b o" id="btnClear">Clear</button><button class="b" id="btnCopy">Copy summary</button>') + BODY
open(out, 'w', encoding='utf-8').write(html)
print('wrote', out, len(html.encode()), 'bytes')
