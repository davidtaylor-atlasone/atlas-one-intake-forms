#!/usr/bin/env python3
"""Run AC job 6: Atlas_One_COI_Tracker.html, phase 1 MVP. usage: build_coi_tracker.py <out.html>"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from a1shell import head, topbar
CSS = """
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:12px}@media(max-width:680px){.stats{grid-template-columns:1fr 1fr}}
.stat{border:1px solid var(--line);border-radius:12px;padding:12px 14px;background:#fff}.stat .v{font-family:'Horas';font-size:26px}.stat .l{font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.04em}
.stat.hold{background:var(--navy);color:#fff;border-color:var(--navy)}.stat.hold .l{color:#c9d2ea}
.tblwrap{overflow-x:auto;margin-top:10px}
table.subs{min-width:980px}table.subs td{padding:6px 5px}table.subs th{padding:6px 5px;white-space:nowrap}
table.subs input,table.subs select{padding:6px 7px;font-size:13px;border-radius:7px}
table.subs input[type=date]{min-width:128px}
.st{display:inline-flex;align-items:center;gap:6px;font-weight:700;font-size:12px;white-space:nowrap;padding:3px 9px;border-radius:20px;border:1.5px solid var(--navy)}
.st.clear{background:var(--tint);border-color:var(--tint)}.st.soon{background:#fff;border-style:dashed}.st.miss{background:#fff}.st.hold{background:var(--navy);color:#fff}
.st::before{font-size:11px}.st.clear::before{content:"\\25CF"}.st.soon::before{content:"\\25D1"}.st.miss::before{content:"\\25CB"}.st.hold::before{content:"\\25A0"}
.cell{display:flex;gap:4px;align-items:center}.cell select{width:64px}.cell input[type=date]{width:130px}
.due{font-size:10.5px;color:var(--muted);white-space:nowrap}
.rm{border:1px solid var(--line);background:#fff;border-radius:7px;cursor:pointer;padding:5px 8px;font-size:12px;color:var(--navy)}
.email{white-space:pre-wrap;font-family:'DM Sans';font-size:13px;background:var(--tint);border-radius:10px;padding:12px 14px;margin-top:8px;border:1px solid var(--line)}
.legend{display:flex;flex-wrap:wrap;gap:10px;font-size:12px;color:var(--muted);margin-top:8px}
.print{display:none}
@media print{.noprint,.top{display:none !important}.print{display:block}.tblwrap{overflow:visible}table.subs{min-width:0;font-size:11px}table.subs input,table.subs select{border:none;padding:0;background:transparent;font-size:11px}.cell select{width:auto}}
"""
BODY = r"""
<div class="wrap">
<div class="hero"><h1>Certificate of insurance tracker</h1><p>Every subcontractor, every certificate, every expiry date in one place. Missing or expired coverage flags the sub and holds payment until the certificate is on file. Works offline; save the file and reload it next time.</p></div>

<div class="card noprint">
  <h2>Your company and rules</h2><p class="sub">Used in the request emails and the printed report.</p>
  <div class="g4">
    <div><label>Your company</label><input id="gc" placeholder="Ridgeline Concrete LLC"></div>
    <div><label>Project or job (optional)</label><input id="proj" placeholder="Job name or number"></div>
    <div><label>Your name</label><input id="me" placeholder="Who signs the request"></div>
    <div><label>Your phone or email</label><input id="mec" placeholder="How subs reach you"></div>
  </div>
  <div class="g4" style="margin-top:10px">
    <div><label>Flag expiring within (days)</label><input id="win" inputmode="numeric" value="30"></div>
    <div><label>Require GL</label><select id="reqGL"><option value="1">Yes</option><option value="0">No</option></select></div>
    <div><label>Require WC</label><select id="reqWC"><option value="1">Yes</option><option value="0">No, owner only subs allowed</option></select></div>
    <div><label>Require signed waiver</label><select id="reqWV"><option value="1">Yes</option><option value="0">No</option></select></div>
  </div>
  <p class="hint">"Waiver" means the signed document your contract calls for: the subcontractor agreement with its waiver of subrogation, or the lien waiver for the pay application. Name it in the request email below.</p>
</div>

<div class="stats" id="stats"></div>

<div class="card">
  <div class="noprint" style="display:flex;flex-wrap:wrap;gap:8px;align-items:center;justify-content:space-between"><div><h2>Subcontractors</h2><p class="sub">Status is decided from the dates. Hold payment is set automatically for missing or expired coverage and can be forced or released by hand.</p></div>
    <div style="display:flex;gap:6px;flex-wrap:wrap"><button class="b" id="addSub">+ Add subcontractor</button><button class="b o" id="sortBtn">Sort by risk</button></div></div>
  <div class="print"><h2 id="pTitle">Certificate of insurance report</h2><p class="sub" id="pSub"></p></div>
  <div class="tblwrap"><table class="subs"><thead><tr><th>Status</th><th>Subcontractor</th><th>Trade</th><th>Email</th><th>Phone</th><th>General liability</th><th>Workers comp</th><th>Waiver</th><th>Hold</th><th class="noprint"></th></tr></thead><tbody id="rows"></tbody></table></div>
  <div class="legend"><span class="st clear">Clear</span> everything on file and current <span class="st soon">Expiring</span> a certificate expires inside the window <span class="st miss">Missing</span> a required item is not on file or has expired <span class="st hold">Hold payment</span> do not release the pay application</div>
</div>

<div class="card noprint">
  <h2>Request email</h2><p class="sub">Pick a sub. The text lists exactly what is missing or expiring and when. Copy it, or open it in your mail app.</p>
  <div class="g3"><div><label>Subcontractor</label><select id="emailSub"></select></div><div><label>Tone</label><select id="tone"><option value="first">First request</option><option value="second">Second request</option><option value="hold">Payment on hold</option></select></div><div style="display:flex;align-items:flex-end;gap:6px"><button class="b" id="copyEmail">Copy text</button><a class="b p" id="mailto" href="#" style="text-decoration:none;display:inline-block">Open in mail</a></div></div>
  <div class="email" id="emailOut">Add a subcontractor above to generate a request.</div>
</div>

<div class="card noprint">
  <h2>Save, load, import, export</h2><p class="sub">Nothing is stored anywhere but this device. Save the JSON file to your project folder and reopen it here next time.</p>
  <div style="display:flex;flex-wrap:wrap;gap:8px">
    <button class="b p" id="saveJson">Save file (.json)</button><button class="b" id="loadJson">Open file (.json)</button>
    <button class="b" id="exportCsv">Export CSV</button><button class="b" id="importCsv">Import CSV</button><button class="b o" id="template">Blank CSV template</button><button class="b o" id="clearAll">Clear all</button>
  </div>
  <input type="file" id="fileJson" accept=".json,application/json" style="display:none"><input type="file" id="fileCsv" accept=".csv,text/csv" style="display:none">
  <p class="hint">CSV columns: name, trade, email, phone, gl_on_file (yes/no), gl_expires (YYYY-MM-DD), wc_on_file, wc_expires, waiver_signed, hold (auto/hold/release), notes. Dates in any common format are read; they are written back as YYYY-MM-DD.</p>
</div>

<div class="help"><b>What is this for?</b> A construction client with 5 to 50 subs loses money two ways: a sub gets hurt or causes damage while uninsured and the general contractor's policy or workers comp audit picks up the bill, or the office spends hours every month chasing paper. This keeps the list, flags the gaps 30 days early, holds the pay application until the certificate is in, and writes the chase email. Phase 2 moves the chasing into automated reminders and the client portal. Not legal or insurance advice; your contract and your carrier decide what a compliant certificate is.</div>
</div>
<script>
function $(id){return document.getElementById(id);}
function esc(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');}
var S={gc:'',proj:'',me:'',mec:'',win:30,reqGL:'1',reqWC:'1',reqWV:'1',subs:[]};
function blank(){return {id:Date.now()+Math.random().toString(16).slice(2,6),name:'',trade:'',email:'',phone:'',gl:'no',glx:'',wc:'no',wcx:'',wv:'no',hold:'auto',notes:''};}
function today(){var d=new Date();d.setHours(0,0,0,0);return d;}
function days(x){if(!x)return null;var d=new Date(x+'T00:00:00');if(isNaN(d))return null;return Math.round((d-today())/86400000);}
function fmt(x){if(!x)return '';var d=new Date(x+'T00:00:00');return isNaN(d)?x:d.toLocaleDateString('en-US',{month:'short',day:'numeric',year:'numeric'});}
function evalSub(s){var win=+S.win||30;var issues=[],soon=[];
 function cov(on,exp,label,req){if(!req)return;if(on!=='yes')return issues.push(label+' certificate not on file');var d=days(exp);if(d===null)return issues.push(label+' certificate has no expiration date recorded');if(d<0)return issues.push(label+' certificate expired '+fmt(exp));if(d<=win)soon.push(label+' certificate expires '+fmt(exp)+' ('+d+' days)');}
 cov(s.gl,s.glx,'General liability',S.reqGL==='1');cov(s.wc,s.wcx,'Workers comp',S.reqWC==='1');
 if(S.reqWV==='1'&&s.wv!=='yes')issues.push('Signed waiver not on file');
 var auto=issues.length>0;var hold=s.hold==='hold'||(s.hold==='auto'&&auto);
 var st=hold?'hold':(issues.length?'miss':(soon.length?'soon':'clear'));
 return {issues:issues,soon:soon,hold:hold,st:st,autoHold:auto};}
var LBL={clear:'Clear',soon:'Expiring',miss:'Missing',hold:'Hold payment'};
function render(){
 $('gc').value=S.gc;$('proj').value=S.proj;$('me').value=S.me;$('mec').value=S.mec;$('win').value=S.win;$('reqGL').value=S.reqGL;$('reqWC').value=S.reqWC;$('reqWV').value=S.reqWV;
 var tb=$('rows');tb.innerHTML='';var c={clear:0,soon:0,miss:0,hold:0};
 S.subs.forEach(function(s,i){var e=evalSub(s);c[e.st]++;
  function covCell(on,exp,k){var d=days(exp);return '<div class="cell"><select data-k="'+k+'" data-i="'+i+'"><option value="no"'+(on!=='yes'?' selected':'')+'>No</option><option value="yes"'+(on==='yes'?' selected':'')+'>Yes</option></select><input type="date" data-k="'+k+'x" data-i="'+i+'" value="'+esc(exp)+'"'+(on!=='yes'?' disabled':'')+'></div>'+(on==='yes'&&d!==null?'<div class="due">'+(d<0?'expired '+(-d)+' days ago':d===0?'expires today':'in '+d+' days')+'</div>':'');}
  tb.innerHTML+='<tr><td><span class="st '+e.st+'" title="'+esc((e.issues.concat(e.soon)).join('; '))+'">'+LBL[e.st]+'</span></td>'+
   '<td><input data-k="name" data-i="'+i+'" value="'+esc(s.name)+'" placeholder="Company"></td><td><input data-k="trade" data-i="'+i+'" value="'+esc(s.trade)+'" placeholder="Trade" style="width:110px"></td>'+
   '<td><input data-k="email" data-i="'+i+'" value="'+esc(s.email)+'" placeholder="email" style="width:170px"></td><td><input data-k="phone" data-i="'+i+'" value="'+esc(s.phone)+'" placeholder="phone" style="width:120px"></td>'+
   '<td>'+covCell(s.gl,s.glx,'gl')+'</td><td>'+covCell(s.wc,s.wcx,'wc')+'</td>'+
   '<td><select data-k="wv" data-i="'+i+'" style="width:70px"><option value="no"'+(s.wv!=='yes'?' selected':'')+'>No</option><option value="yes"'+(s.wv==='yes'?' selected':'')+'>Yes</option></select></td>'+
   '<td><select data-k="hold" data-i="'+i+'" style="width:96px"><option value="auto"'+(s.hold==='auto'?' selected':'')+'>Auto'+(e.autoHold?' (hold)':' (release)')+'</option><option value="hold"'+(s.hold==='hold'?' selected':'')+'>Force hold</option><option value="release"'+(s.hold==='release'?' selected':'')+'>Release</option></select></td>'+
   '<td class="noprint"><button class="rm" data-x="'+i+'" title="Remove">✕</button></td></tr>';});
 $('stats').innerHTML='<div class="stat"><div class="v">'+S.subs.length+'</div><div class="l">Subcontractors</div></div><div class="stat"><div class="v">'+c.clear+'</div><div class="l">Clear</div></div><div class="stat"><div class="v">'+(c.soon)+'</div><div class="l">Expiring in '+(S.win||30)+' days</div></div><div class="stat hold"><div class="v">'+(c.hold)+'</div><div class="l">Payment on hold</div></div>';
 $('pTitle').textContent='Certificate of insurance report'+(S.gc?(': '+S.gc):'')+(S.proj?(', '+S.proj):'');$('pSub').textContent='Printed '+new Date().toLocaleDateString('en-US',{month:'long',day:'numeric',year:'numeric'})+'. '+S.subs.length+' subcontractors, '+c.hold+' on payment hold, '+c.soon+' expiring within '+(S.win||30)+' days.';
 var sel=$('emailSub');var prev=sel.value;sel.innerHTML=S.subs.map(function(s,i){return '<option value="'+i+'">'+esc(s.name||('Sub '+(i+1)))+'</option>';}).join('');if(prev&&sel.querySelector('option[value="'+prev+'"]'))sel.value=prev;
 bind();email();persist();
}
function bind(){
 document.querySelectorAll('#rows [data-k]').forEach(function(el){el.onchange=el.oninput=function(){var s=S.subs[+el.dataset.i];s[el.dataset.k]=el.value;if(el.dataset.k==='gl'||el.dataset.k==='wc'||el.dataset.k==='wv'||el.dataset.k==='hold'||el.type==='date')render();else{email();persist();}};});
 document.querySelectorAll('#rows [data-x]').forEach(function(el){el.onclick=function(){var s=S.subs[+el.dataset.x];if(s.name&&!confirm('Remove '+s.name+' from the list?'))return;S.subs.splice(+el.dataset.x,1);render();};});
}
function email(){var i=+$('emailSub').value;var s=S.subs[i];if(!s){$('emailOut').textContent='Add a subcontractor above to generate a request.';$('mailto').href='#';return;}
 var e=evalSub(s);var tone=$('tone').value;var items=e.issues.concat(e.soon);var gc=S.gc||'our company';var who=S.me||gc;
 var subj=(tone==='hold'?'Payment on hold: ':(tone==='second'?'Second request: ':'Request: '))+'insurance certificate for '+(s.name||'your company')+(S.proj?(', '+S.proj):'');
 var lines=['Hello '+(s.name||'there')+',',''];
 if(tone==='hold')lines.push('Your next payment from '+gc+' is on hold until the items below are on file. Nothing else is needed to release it.');
 else if(tone==='second')lines.push('Following up on our earlier request. '+gc+' cannot release payment for work'+(S.proj?(' on '+S.proj):'')+' until the items below are on file.');
 else lines.push('To keep you cleared for work'+(S.proj?(' on '+S.proj):'')+' and paid on time, '+gc+' needs the following from your insurance agent and your office:');
 lines.push('');
 if(items.length)items.forEach(function(x){lines.push('  1. '.replace('1',String(lines.filter(function(l){return /^  \d/.test(l);}).length+1))+x);});
 else lines.push('  Everything we require is on file. Thank you, no action needed.');
 lines.push('');
 if(e.issues.some(function(x){return /General liability|Workers comp/.test(x);})||e.soon.length){lines.push('Please have your agent send the certificate of insurance to '+(S.mec||who)+' with '+gc+' named as certificate holder'+(S.reqWV==='1'?' and additional insured where the contract requires it':'')+'. Ask for the renewal certificate before the current one expires so there is no gap.');}
 if(e.issues.some(function(x){return /waiver/i.test(x);}))lines.push('The signed waiver can be returned as a photo or scan by reply to this message.');
 lines.push('','Reply to this message or call if anything is unclear. Thank you for keeping the paperwork current so payments keep moving.','',who+(S.gc&&S.me?(', '+S.gc):''),S.mec||'');
 var txt=lines.join('\n').replace(/\n{3,}/g,'\n\n').trim();
 $('emailOut').textContent='Subject: '+subj+'\n\n'+txt;
 $('mailto').href='mailto:'+encodeURIComponent(s.email||'')+'?subject='+encodeURIComponent(subj)+'&body='+encodeURIComponent(txt);
}
function persist(){['gc','proj','me','mec','win','reqGL','reqWC','reqWV'].forEach(function(k){S[k]=$(k).value;});try{localStorage.setItem('a1coi',JSON.stringify(S));}catch(e){}}
['gc','proj','me','mec','win','reqGL','reqWC','reqWV'].forEach(function(k){$(k).onchange=function(){persist();render();};$(k).oninput=function(){persist();if(k==='gc'||k==='proj'||k==='me'||k==='mec')email();};});
$('emailSub').onchange=email;$('tone').onchange=email;
$('addSub').onclick=function(){S.subs.push(blank());render();var r=$('rows').querySelectorAll('tr');var last=r[r.length-1];if(last)last.querySelector('input[data-k="name"]').focus();};
$('sortBtn').onclick=function(){var o={hold:0,miss:1,soon:2,clear:3};S.subs.sort(function(a,b){return o[evalSub(a).st]-o[evalSub(b).st]||(a.name||'').localeCompare(b.name||'');});render();};
$('copyEmail').onclick=function(){var t=$('emailOut').textContent;try{navigator.clipboard.writeText(t);$('copyEmail').textContent='Copied';setTimeout(function(){$('copyEmail').textContent='Copy text';},1200);}catch(e){prompt('Copy:',t);}};
function dl(text,name,type){var blob=new Blob([text],{type:type});var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.appendChild(a);a.click();a.remove();}
function safe(){return (S.gc||'Atlas_One').replace(/[^A-Za-z0-9]+/g,'_').replace(/^_+|_+$/g,'');}
$('saveJson').onclick=function(){persist();dl(JSON.stringify({app:'Atlas One COI Tracker',version:1,saved:new Date().toISOString(),data:S},null,1),'COI_Tracker_'+safe()+'_'+new Date().toISOString().slice(0,10)+'.json','application/json');};
$('loadJson').onclick=function(){$('fileJson').click();};
$('fileJson').onchange=function(){var f=this.files[0];if(!f)return;var r=new FileReader();r.onload=function(){try{var o=JSON.parse(r.result);var d=o.data||o;if(!d.subs)throw 0;S=Object.assign({gc:'',proj:'',me:'',mec:'',win:30,reqGL:'1',reqWC:'1',reqWV:'1',subs:[]},d);render();}catch(e){alert('That file is not a COI Tracker file.');}};r.readAsText(f);this.value='';};
var COLS=['name','trade','email','phone','gl_on_file','gl_expires','wc_on_file','wc_expires','waiver_signed','hold','notes'];
function csvCell(v){v=String(v==null?'':v);return /[",\n]/.test(v)?'"'+v.replace(/"/g,'""')+'"':v;}
$('exportCsv').onclick=function(){var rows=[COLS.join(',')];S.subs.forEach(function(s){var e=evalSub(s);rows.push([s.name,s.trade,s.email,s.phone,s.gl,s.glx,s.wc,s.wcx,s.wv,s.hold,s.notes].map(csvCell).join(',')+','+csvCell(LBL[e.st]));});rows[0]+=',status';dl(rows.join('\r\n'),'COI_Tracker_'+safe()+'.csv','text/csv');};
$('template').onclick=function(){dl(COLS.join(',')+'\r\nExample Electric LLC,Electrical,office@example.com,801 555 0100,yes,2027-03-31,yes,2027-01-15,yes,auto,\r\n','COI_Tracker_template.csv','text/csv');};
function parseCsv(t){var rows=[],row=[],cell='',q=false;for(var i=0;i<t.length;i++){var ch=t[i];if(q){if(ch==='"'){if(t[i+1]==='"'){cell+='"';i++;}else q=false;}else cell+=ch;}else{if(ch==='"')q=true;else if(ch===','){row.push(cell);cell='';}else if(ch==='\n'||ch==='\r'){if(ch==='\r'&&t[i+1]==='\n')i++;row.push(cell);rows.push(row);row=[];cell='';}else cell+=ch;}}if(cell.length||row.length){row.push(cell);rows.push(row);}return rows.filter(function(r){return r.some(function(c){return c.trim();});});}
function toISO(v){v=String(v||'').trim();if(!v)return '';var d=new Date(v);if(/^\d{1,2}\/\d{1,2}\/\d{2,4}$/.test(v)){var p=v.split('/');var y=p[2].length===2?'20'+p[2]:p[2];d=new Date(y,+p[0]-1,+p[1]);}if(isNaN(d))return '';return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function yn(v){return /^(y|yes|true|1|x)$/i.test(String(v||'').trim())?'yes':'no';}
$('importCsv').onclick=function(){$('fileCsv').click();};
$('fileCsv').onchange=function(){var f=this.files[0];if(!f)return;var r=new FileReader();r.onload=function(){var rows=parseCsv(r.result);if(rows.length<2){alert('No rows found.');return;}var hdr=rows[0].map(function(h){return h.trim().toLowerCase().replace(/\s+/g,'_');});function col(r,names){for(var k=0;k<names.length;k++){var j=hdr.indexOf(names[k]);if(j>=0)return r[j]||'';}return '';}
  var added=0;rows.slice(1).forEach(function(r){var s=blank();s.name=col(r,['name','subcontractor','company','vendor']);s.trade=col(r,['trade','scope']);s.email=col(r,['email','e-mail']);s.phone=col(r,['phone','mobile']);
   s.gl=yn(col(r,['gl_on_file','gl','general_liability']));s.glx=toISO(col(r,['gl_expires','gl_expiration','gl_exp']));s.wc=yn(col(r,['wc_on_file','wc','workers_comp']));s.wcx=toISO(col(r,['wc_expires','wc_expiration','wc_exp']));s.wv=yn(col(r,['waiver_signed','waiver']));var h=String(col(r,['hold'])).toLowerCase();s.hold=(h==='hold'||h==='release')?h:'auto';s.notes=col(r,['notes']);if(s.name){S.subs.push(s);added++;}});
  render();alert(added+' subcontractor(s) imported.');};r.readAsText(f);this.value='';};
$('clearAll').onclick=function(){if(!confirm('Clear every subcontractor from this list? Save the file first if you want to keep it.'))return;S.subs=[];render();};
try{var saved=JSON.parse(localStorage.getItem('a1coi')||'null');if(saved&&saved.subs)S=saved;}catch(e){}
render();
</script>
</body></html>
"""
out = sys.argv[1]
html = head('Atlas One: COI Tracker', CSS) + '<body>' + topbar('Certificate of insurance tracker') + BODY
open(out, 'w', encoding='utf-8').write(html); print('wrote', out, len(html.encode()), 'bytes')
