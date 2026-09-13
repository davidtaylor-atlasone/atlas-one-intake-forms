
/* ============ Export deck (.pptx): ten slides, numbers from page state only (Run AC, 2026-09-13) ============ */
var TIERSET=[
 ['Essential',99,0,'setup waived','Under 20 employees, one state, under five hours a month of back office work. No benefits renewal to manage yet.','The tools, the annual audit and its guarantee, the compliance calendar, software at member pricing, email support.'],
 ['Professional',399,495,'setup $495, often waived','Twenty to fifty employees, or five to fifteen hours a month. The owner is still the back office.','A real person by phone, next business day, three hands on hours a month. Handbook and safety manual kept current. Benefits and workers comp renewals managed. A quarterly review.'],
 ['Enterprise',999,995,'setup $995, waived on annual','Forty to a hundred employees, or more than fifteen hours a month. You want it run, not advised.','A dedicated contact, same day reply, eight hands on hours. Full coordination across all six divisions. Open enrollment, hires and exits, COBRA and ACA handled. Every renewal with a written recommendation.'],
 ['Concierge',1900,1500,'setup $1,500','The honest answer to "who runs operations" is "me, at night."','Your fractional COO. A standing monthly strategy hour with the numbers prepared. The AI Email Assistant and AI Task Agent included. Same day response, unlimited within a written scope. Every document built for you.']
];
function tierPicked(){var m=E().services.filter(function(a){return a[0]==='mem'&&a[6];})[0];if(!m)return null;
 var lbl=(m[1]||'').toLowerCase();var t=TIERSET.filter(function(x){return lbl.indexOf(x[0].toLowerCase())>=0;})[0];
 return {row:m,tier:t||null,price:n(m[3]),setup:n(m[4])};}
function freqLabel(v){return {52:'weekly',26:'every two weeks',24:'twice a month',12:'monthly',4:'quarterly',1:'annually'}[String(n(v))]||'';}
function h1(s,txt,dark){s.addText(txt,{x:0.6,y:0.5,w:12.1,h:0.7,fontFace:HD,fontSize:28,color:dark?WHT:NAVY});}
function sub(s,txt,dark){s.addText(txt,{x:0.62,y:1.2,w:12,h:0.45,fontFace:BD,fontSize:13,color:dark?'C9D2EA':MUT});}
function stat(pptx,s,x,y,w,h,fill,label,big,small,labelColor,bigColor,smallColor){
 s.addShape(pptx.ShapeType.rect,{x:x,y:y,w:w,h:h,fill:{color:fill},line:{type:'none'},rectRadius:0.08});
 s.addText(label,{x:x+0.25,y:y+0.2,w:w-0.5,h:0.35,fontFace:BD,bold:true,fontSize:10.5,color:labelColor,charSpacing:1});
 s.addText(big,{x:x+0.25,y:y+0.55,w:w-0.5,h:0.85,fontFace:HD,fontSize:30,color:bigColor});
 if(small)s.addText(small,{x:x+0.25,y:y+1.4,w:w-0.5,h:0.4,fontFace:BD,fontSize:11.5,color:smallColor});}
function pageNo(s,i,dark){s.addText(i+' / 10',{x:11.7,y:7.02,w:1.0,h:0.3,fontFace:BD,fontSize:9,color:dark?'9FB0D8':MUT,align:'right'});}
function buildDeck10(){
 harvest();var e=E();var co=e.company.name||'Your Company';
 var peo=payrollMonthly();var pc=perCheck();
 var bl=benList();var benSum=bl.reduce(function(s,b){return s+b.cost;},0);
 var son=svcOn();var svcSum=son.reduce(function(s,a){return s+n(a[3]);},0);
 var setupSum=son.reduce(function(s,a){return s+n(a[4]);},0);
 var recurring=peo+benSum+svcSum;var disc=discountAmt(recurring);var grand=recurring-disc;
 var cur=n($('cur').value);var owner=(e.company.contacts[0]&&e.company.contacts[0].name)||'';
 var wq=n($('wcQuote').value),wp=n($('wcPremium').value);
 var th=n($('tsHours').value),tr=n($('tsRate').value),tsoft=n($('tsSoft').value),timeVal=th*tr+tsoft;
 var tp=tierPicked();
 var pptx=new PptxGenJS();pptx.layout='LAYOUT_WIDE';pptx.author='Atlas One Solutions';pptx.company='Atlas One Solutions';pptx.title='Atlas One proposal for '+co;var s;
 /* 1 cover */
 s=pptx.addSlide();s.background={color:NAVY};
 s.addShape(pptx.ShapeType.rect,{x:0.6,y:0.55,w:0.62,h:0.62,fill:{color:PERI},rectRadius:0.09,line:{type:'none'}});
 s.addText([{text:'A',options:{color:WHT}},{text:'1',options:{color:NAVY}}],{x:0.6,y:0.55,w:0.62,h:0.62,fontFace:BD,bold:true,fontSize:22,align:'center',valign:'middle'});
 s.addText('ATLAS ONE SOLUTIONS',{x:1.35,y:0.6,w:9,h:0.5,fontFace:BD,bold:true,fontSize:13,color:PERI,charSpacing:2,valign:'middle'});
 s.addText('Your back office, one relationship, one number',{x:0.6,y:2.3,w:12,h:1.0,fontFace:HD,fontSize:38,color:WHT});
 s.addText('Prepared for '+co,{x:0.62,y:3.45,w:12,h:0.5,fontFace:BD,fontSize:20,color:'C9D2EA'});
 if(owner)s.addText('Attention: '+owner,{x:0.62,y:4.0,w:12,h:0.4,fontFace:BD,fontSize:14,color:'9FB0D8'});
 s.addText('One Call Solves Everything.',{x:0.62,y:5.7,w:12,h:0.5,fontFace:HD,fontSize:20,color:PERI});
 s.addText(todayStr()+(e.company.preparer?('   Prepared by '+e.company.preparer):''),{x:0.62,y:6.25,w:12,h:0.4,fontFace:BD,fontSize:12,color:'9FB0D8'});
 pageNo(s,1,true);
 /* 2 situation */
 s=pptx.addSlide();s.background={color:OFF};h1(s,'Where '+co+' is today');sub(s,'What we heard in discovery. Correct anything that is off and the numbers move with it.');
 var facts=[];
 if(e.company.industry)facts.push(['Industry',e.company.industry]);
 if(ee()>0)facts.push(['Employees',String(ee())+(e.states.length?(' across '+e.states.map(function(x){return x.st;}).join(', ')):'')]);
 if(gross()>0)facts.push(['Monthly gross payroll',usd(gross())+(freqLabel($('pr').value)?(', paid '+freqLabel($('pr').value)):'')]);
 if(e.employees.schedules.length)facts.push(['Pay schedules',e.employees.schedules.map(function(x){return (x.note?x.note+': ':'')+x.freq+(x.ee?(' ('+x.ee+')'):'');}).join('; ')]);
 if(e.wc.carrier||wp>0)facts.push(['Workers comp today',(e.wc.carrier||'current carrier')+(wp>0?(', '+usd(wp)+' per year'):'')]);
 if(e.wc.codes.length)facts.push(['Class codes',e.wc.codes.map(function(w){return (w.code||'')+(w.desc?(' '+w.desc):'');}).join('; ')]);
 if(cur>0)facts.push(['Current all in back office spend',usd(cur)+' per month, '+usd(cur*12)+' per year']);
 if(bl.length)facts.push(['Benefits in place or wanted',bl.map(function(b){return b.label;}).join(', ')]);
 if(e.company.contacts.length)facts.push(['Your team on this',e.company.contacts.map(function(c){return c.name+(c.role?(' ('+c.role+')'):'');}).join(', ')]);
 if(!facts.length)facts.push(['Discovery','Fill in the company, employees and current spend in the Cockpit and this slide fills itself.']);
 var fr=facts.slice(0,9).map(function(f){return [{text:f[0],options:{bold:true,color:NAVY,align:'left',fill:{color:WHT}}},{text:f[1],options:{color:NAVY,align:'left',fill:{color:WHT}}}];});
 s.addTable(fr,{x:0.6,y:1.8,w:12.1,colW:[3.6,8.5],rowH:0.48,fontFace:BD,fontSize:13,border:{type:'solid',color:SOFT,pt:1},valign:'middle'});
 if(e.notes)s.addText(e.notes,{x:0.62,y:1.85+0.48*Math.min(facts.length,9)+0.15,w:12,h:0.8,fontFace:BD,fontSize:12,color:MUT,valign:'top'});
 foot(s,false);pageNo(s,2,false);
 /* 3 itemized quote */
 s=pptx.addSlide();s.background={color:OFF};h1(s,'Your itemized quote');sub(s,'Every line priced on its own. Nothing is bundled where you cannot see it.');
 var body=[[{text:'Item',options:{bold:true,color:WHT,fill:{color:NAVY},align:'left'}},{text:'Monthly',options:{bold:true,color:WHT,fill:{color:NAVY},align:'right'}},{text:'One time setup',options:{bold:true,color:WHT,fill:{color:NAVY},align:'right'}}]];
 body.push([{text:payrollLabel().replace(/ — /g,': '),options:{color:NAVY,bold:true}},{text:usd(peo),options:{align:'right',color:NAVY,bold:true}},{text:'',options:{}}]);
 if(benSum>0)body.push([{text:'Benefits (employer share of premiums)',options:{color:NAVY}},{text:usd(benSum),options:{align:'right',color:NAVY,bold:true}},{text:'',options:{}}]);
 var shown=son.slice(0,9);shown.forEach(function(a){body.push([{text:a[1].replace(/ — /g,': '),options:{color:NAVY}},{text:usd(n(a[3])),options:{align:'right',color:NAVY,bold:true}},{text:n(a[4])>0?usd(n(a[4])):'',options:{align:'right',color:MUT}}]);});
 if(son.length>9)body.push([{text:(son.length-9)+' more service line(s), see the itemized summary',options:{color:MUT}},{text:usd(son.slice(9).reduce(function(t,a){return t+n(a[3]);},0)),options:{align:'right',color:NAVY,bold:true}},{text:usd(son.slice(9).reduce(function(t,a){return t+n(a[4]);},0)),options:{align:'right',color:MUT}}]);
 if(disc>0)body.push([{text:'Discount',options:{color:NAVY}},{text:'minus '+usd(disc),options:{align:'right',color:NAVY,bold:true}},{text:'',options:{}}]);
 body.push([{text:'Total monthly, all in',options:{bold:true,color:WHT,fill:{color:NAVY},fontFace:HD,fontSize:14}},{text:usd(grand),options:{align:'right',bold:true,color:WHT,fill:{color:NAVY},fontFace:HD,fontSize:14}},{text:setupSum>0?usd(setupSum):'',options:{align:'right',bold:true,color:WHT,fill:{color:NAVY},fontFace:HD,fontSize:14}}]);
 s.addTable(body,{x:0.6,y:1.8,w:12.1,colW:[7.6,2.25,2.25],rowH:0.4,fontFace:BD,fontSize:12.5,border:{type:'solid',color:SOFT,pt:1},valign:'middle'});
 s.addText('Annual, all in: '+usd(grand*12)+(setupSum>0?('. Setup fees are one time and shown separately.'):''),{x:0.62,y:6.45,w:12,h:0.4,fontFace:BD,fontSize:12,color:MUT});
 foot(s,false);pageNo(s,3,false);
 /* 4 PEO separate */
 s=pptx.addSlide();s.background={color:OFF};h1(s,'Payroll and PEO, kept on its own line');sub(s,'Payroll is a transaction. It is priced separately so you always see what it costs and what it covers.');
 stat(pptx,s,0.6,1.85,6.0,2.1,NAVY,payrollLabel().replace(/ — /g,': ').toUpperCase(),usd(peo)+' per month',(ee()>0?ee()+' employees, ':'')+usd(peo*12)+' per year','9FB0D8',WHT,'C9D2EA');
 if(pc>0)stat(pptx,s,6.9,1.85,5.8,2.1,PERI,'PER EMPLOYEE, PER CHECK',usd(pc),'what each pay run costs, per person',NAVY,NAVY,NAVY);
 else stat(pptx,s,6.9,1.85,5.8,2.1,SOFT,'WHY SEPARATE','Clarity',"you never wonder what payroll costs inside a bundle",MUT,NAVY,MUT);
 s.addText('Handled behind the scenes',{x:0.6,y:4.25,w:12,h:0.4,fontFace:HD,fontSize:16,color:NAVY});
 var cx=0.6,cy=4.75;CHIPS.forEach(function(c){var w=Math.min(4.2,0.3+c.length*0.095);if(cx+w>12.7){cx=0.6;cy+=0.5;}if(cy>6.6)return;
  s.addShape(pptx.ShapeType.rect,{x:cx,y:cy,w:w,h:0.4,fill:{color:WHT},line:{color:SOFT,width:1},rectRadius:0.2});
  s.addText(c,{x:cx,y:cy,w:w,h:0.4,fontFace:BD,fontSize:10.5,color:NAVY,align:'center',valign:'middle'});cx+=w+0.15;});
 foot(s,false);pageNo(s,4,false);
 /* 5 savings and ROI */
 s=pptx.addSlide();s.background={color:NAVY};h1(s,'What you pay now against Atlas One',true);
 if(cur>0){var diff=(cur-grand)*12,save=diff>=0;
  sub(s,save?'The difference is savings you keep every year.':'The difference is the added investment for what is new.',true);
  stat(pptx,s,0.6,1.85,5.9,2.2,NAVY2,'YOUR CURRENT SPEND',usd(cur)+' per month',usd(cur*12)+' per year','9FB0D8',WHT,'C9D2EA');
  stat(pptx,s,6.8,1.85,5.9,2.2,PERI,'WITH ATLAS ONE, ALL IN',usd(grand)+' per month',usd(grand*12)+' per year',NAVY,NAVY,NAVY);
  s.addShape(pptx.ShapeType.rect,{x:0.6,y:4.4,w:12.1,h:0.9,fill:{color:save?PERI:NAVY2},line:{color:save?PERI:'3A4A70',width:1},rectRadius:0.08});
  s.addText((save?'Estimated savings: ':'Added investment: ')+usd(Math.abs(diff))+' per year'+(save&&grand>0?('  ('+Math.round(diff/(grand*12)*100)+'% return on the annual investment)'):''),{x:0.6,y:4.4,w:12.1,h:0.9,fontFace:HD,fontSize:22,color:save?NAVY:WHT,align:'center',valign:'middle'});
 }else{sub(s,'Enter the current all in monthly spend in the Cockpit and the comparison fills in here.',true);
  stat(pptx,s,0.6,1.85,12.1,2.2,PERI,'WITH ATLAS ONE, ALL IN',usd(grand)+' per month',usd(grand*12)+' per year',NAVY,NAVY,NAVY);}
 if(wq>0){var ws=wp-wq;s.addText('Workers comp'+(e.wc.carrier?(' with '+e.wc.carrier):'')+': '+(wp>0?(usd(wp)+' per year today. '):'')+'Atlas One quote: '+usd(wq)+' per year.'+(wp>0?(ws>=0?(' Estimated WC savings of '+usd(ws)+' per year.'):(' WC difference of '+usd(Math.abs(ws))+' per year.')):''),{x:0.62,y:5.55,w:12,h:0.8,fontFace:BD,fontSize:13,color:'C9D2EA',valign:'top'});}
 foot(s,true);pageNo(s,5,true);
 /* 6 time value */
 s=pptx.addSlide();s.background={color:OFF};h1(s,'The time we hand back');
 if(th>0||tsoft>0){sub(s,'Hours you stop spending on the back office, priced at your own hourly value, plus software you no longer pay for.');
  stat(pptx,s,0.6,1.85,3.85,2.1,NAVY,'HOURS BACK EACH MONTH',th+' hrs',tr>0?('at '+usd(tr)+' an hour'):'', '9FB0D8',WHT,'C9D2EA');
  stat(pptx,s,4.72,1.85,3.85,2.1,PERI,'VALUE BACK EACH MONTH',usd(timeVal),tsoft>0?('includes '+usd(tsoft)+' of software replaced'):'',NAVY,NAVY,NAVY);
  stat(pptx,s,8.85,1.85,3.85,2.1,SOFT,'EACH YEAR',usd(timeVal*12),'reinvested in the business',MUT,NAVY,MUT);
  if(e.timeSavings.note)s.addText(e.timeSavings.note,{x:0.62,y:4.3,w:12,h:1.6,fontFace:BD,fontSize:13.5,color:MUT,valign:'top'});
 }else{sub(s,'Most owners give a third of their week to admin: payroll questions, vendor calls, renewals, paperwork.');
  stat(pptx,s,0.6,1.85,3.85,2.1,NAVY,'OF AN OWNER WEEK','33%','goes to back office admin','9FB0D8',WHT,'C9D2EA');
  stat(pptx,s,4.72,1.85,3.85,2.1,PERI,'HOURS RECLAIMED','15 to 25','a month once consolidated, typical',NAVY,NAVY,NAVY);
  stat(pptx,s,8.85,1.85,3.85,2.1,SOFT,'SAVED ACROSS VENDORS','15 to 30%','when shopped together, not one at a time',MUT,NAVY,MUT);
  s.addText('Enter hours saved and the hourly rate in the Cockpit to replace these typical figures with '+co+'’s own.',{x:0.62,y:4.3,w:12,h:0.6,fontFace:BD,fontSize:12,color:MUT});}
 foot(s,false);pageNo(s,6,false);
 /* 7 guarantee */
 s=pptx.addSlide();s.background={color:NAVY};
 s.addText('THE AUDIT GUARANTEE',{x:0.6,y:0.7,w:12,h:0.4,fontFace:BD,bold:true,fontSize:13,color:PERI,charSpacing:2});
 s.addText('Two times your first year membership in documented savings or risk removed, or there is nothing to buy.',{x:0.6,y:1.4,w:12.1,h:1.9,fontFace:HD,fontSize:32,color:WHT,valign:'top'});
 s.addText('The audit comes first. Every vendor, policy, plan and subscription, written up with numbers, before you decide anything. If the findings do not cover the membership twice over, we say so and you walk away with the report.',{x:0.62,y:3.6,w:11.6,h:1.4,fontFace:BD,fontSize:15,color:'C9D2EA',valign:'top'});
 var gp=[['1','The 30 minute Back Office Audit','Bring the vendor list, the last payroll invoice, the renewal dates.'],['2','The written findings','Every line with a number: what it costs, what the market charges, what is exposed.'],['3','Your decision','Join, or keep the report. Either way you leave with the numbers.']];
 gp.forEach(function(g,i){var x=0.6+i*4.1;s.addShape(pptx.ShapeType.rect,{x:x,y:5.15,w:3.9,h:1.55,fill:{color:NAVY2},line:{color:'3A4A70',width:1},rectRadius:0.08});
  s.addText(g[0],{x:x+0.2,y:5.25,w:0.5,h:0.5,fontFace:HD,fontSize:20,color:PERI});s.addText(g[1],{x:x+0.7,y:5.27,w:3.1,h:0.45,fontFace:BD,bold:true,fontSize:12,color:WHT});s.addText(g[2],{x:x+0.7,y:5.7,w:3.1,h:0.95,fontFace:BD,fontSize:10.5,color:'C9D2EA',valign:'top'});});
 foot(s,true);pageNo(s,7,true);
 /* 8 membership tier */
 s=pptx.addSlide();s.background={color:OFF};
 if(tp&&tp.tier){var t=tp.tier;h1(s,'Your membership: '+t[0]);sub(s,'Picked for '+co+' from where the business is today. Tiers move up any month and down at renewal.');
  stat(pptx,s,0.6,1.85,5.9,2.1,NAVY,t[0].toUpperCase()+' MEMBERSHIP',usd(tp.price||t[1])+' per month',(tp.setup>0?('setup '+usd(tp.setup)):t[3]),'9FB0D8',WHT,'C9D2EA');
  s.addShape(pptx.ShapeType.rect,{x:6.8,y:1.85,w:5.9,h:2.1,fill:{color:WHT},line:{color:SOFT,width:1},rectRadius:0.08});
  s.addText('THE FIT',{x:7.05,y:2.05,w:5.4,h:0.35,fontFace:BD,bold:true,fontSize:10.5,color:MUT,charSpacing:1});
  s.addText(t[4],{x:7.05,y:2.4,w:5.4,h:1.45,fontFace:BD,fontSize:12.5,color:NAVY,valign:'top'});
  s.addText('What changes at this tier',{x:0.6,y:4.25,w:12,h:0.4,fontFace:HD,fontSize:16,color:NAVY});
  s.addText(t[5],{x:0.62,y:4.7,w:12,h:1.0,fontFace:BD,fontSize:13,color:NAVY,valign:'top'});
  s.addText('Every tier includes: a named person who knows your setup, the annual Back Office Audit and its guarantee, renewals managed, the tools, software at member pricing, the compliance calendar, every division at member rates.',{x:0.62,y:5.75,w:12,h:0.9,fontFace:BD,fontSize:11,color:MUT,valign:'top'});
 }else{h1(s,'Which membership, quickly');sub(s,tp?('A membership line is on the quote at '+usd(tp.price)+' per month. Pick the tier in the Cockpit to name it here.'):'Three questions pick the tier: how many employees, who handles a renewal today, how many hours a month the owner gives the back office.');
  TIERSET.forEach(function(t,i){var x=0.6+i*3.05;s.addShape(pptx.ShapeType.rect,{x:x,y:1.85,w:2.9,h:4.6,fill:{color:i===1?NAVY:WHT},line:{color:SOFT,width:1},rectRadius:0.08});
   s.addText(t[0],{x:x+0.2,y:2.0,w:2.5,h:0.45,fontFace:HD,fontSize:16,color:i===1?WHT:NAVY});
   s.addText(usd(t[1])+' a month',{x:x+0.2,y:2.45,w:2.5,h:0.4,fontFace:BD,bold:true,fontSize:12.5,color:i===1?PERI:NAVY});
   s.addText(t[3],{x:x+0.2,y:2.8,w:2.5,h:0.35,fontFace:BD,fontSize:10,color:i===1?'C9D2EA':MUT});
   s.addText(t[4],{x:x+0.2,y:3.25,w:2.5,h:1.5,fontFace:BD,fontSize:10.5,color:i===1?'C9D2EA':NAVY,valign:'top'});
   s.addText(t[5],{x:x+0.2,y:4.75,w:2.5,h:1.6,fontFace:BD,fontSize:9.5,color:i===1?'C9D2EA':MUT,valign:'top'});});}
 foot(s,false);pageNo(s,8,false);
 /* 9 next steps */
 s=pptx.addSlide();s.background={color:OFF};h1(s,'Next steps');sub(s,'Four steps from this deck to a running back office. You approve each one.');
 var steps=[['This week','Say yes to the 30 minute Back Office Audit. Bring the vendor list, the last payroll invoice and the renewal dates.'],['Week 1','Written findings with numbers. Sign the service agreement'+(tp&&tp.tier?(' and the '+tp.tier[0]+' membership'):'')+'. Setup and onboarding begin.'],['Weeks 2 to 4','Payroll and benefits transition on your schedule, never mid cycle. Workers comp'+(wq>0?' bound at the quoted premium':' reviewed')+'. Documents built.'],['Day 30 and after','One number to call. Renewals worked 60 to 90 days out. Quarterly review of the numbers on this deck.']];
 steps.forEach(function(st,i){var y=1.85+i*1.15;s.addShape(pptx.ShapeType.rect,{x:0.6,y:y,w:12.1,h:1.0,fill:{color:WHT},line:{color:SOFT,width:1},rectRadius:0.08});
  s.addShape(pptx.ShapeType.rect,{x:0.6,y:y,w:0.09,h:1.0,fill:{color:PERI},line:{type:'none'}});
  s.addText(String(i+1),{x:0.85,y:y+0.2,w:0.6,h:0.6,fontFace:HD,fontSize:24,color:PERI});
  s.addText(st[0],{x:1.5,y:y+0.12,w:2.6,h:0.75,fontFace:BD,bold:true,fontSize:13,color:NAVY,valign:'middle'});
  s.addText(st[1],{x:4.1,y:y+0.1,w:8.4,h:0.8,fontFace:BD,fontSize:12,color:NAVY,valign:'middle'});});
 s.addText('Setup fees are one time and often waived on an annual plan; annual plans get two months free.',{x:0.62,y:6.5,w:12,h:0.4,fontFace:BD,fontSize:10.5,color:MUT});
 foot(s,false);pageNo(s,9,false);
 /* 10 contact */
 s=pptx.addSlide();s.background={color:NAVY};
 s.addShape(pptx.ShapeType.rect,{x:0.6,y:0.55,w:0.62,h:0.62,fill:{color:PERI},rectRadius:0.09,line:{type:'none'}});
 s.addText([{text:'A',options:{color:WHT}},{text:'1',options:{color:NAVY}}],{x:0.6,y:0.55,w:0.62,h:0.62,fontFace:BD,bold:true,fontSize:22,align:'center',valign:'middle'});
 s.addText('One Call Solves Everything.',{x:0.6,y:2.0,w:12,h:0.9,fontFace:HD,fontSize:36,color:WHT});
 s.addText('Questions on any line of this deck: one call, one person, an answer the same day.',{x:0.62,y:3.0,w:11.6,h:0.6,fontFace:BD,fontSize:15,color:'C9D2EA'});
 var cc=[['CALL OR TEXT','385-213-7177'],['EMAIL','David@AtlasOneSolutions.com'],['WEB','AtlasOneSolutions.com']];
 cc.forEach(function(c,i){var x=0.6+i*4.1;s.addShape(pptx.ShapeType.rect,{x:x,y:4.0,w:3.9,h:1.3,fill:{color:NAVY2},line:{color:'3A4A70',width:1},rectRadius:0.08});
  s.addText(c[0],{x:x+0.25,y:4.15,w:3.4,h:0.35,fontFace:BD,bold:true,fontSize:10.5,color:'9FB0D8',charSpacing:1});s.addText(c[1],{x:x+0.25,y:4.5,w:3.5,h:0.6,fontFace:BD,bold:true,fontSize:15,color:WHT,valign:'middle'});});
 s.addText((e.company.preparer||'David Taylor')+', Atlas One Solutions',{x:0.62,y:5.7,w:12,h:0.4,fontFace:BD,bold:true,fontSize:14,color:WHT});
 s.addText('Prepared for '+co+' on '+todayStr()+'.',{x:0.62,y:6.15,w:12,h:0.4,fontFace:BD,fontSize:12,color:'9FB0D8'});
 foot(s,true);pageNo(s,10,true);
 var safe=co.replace(/[^A-Za-z0-9]+/g,'_').replace(/^_+|_+$/g,'')||'Client';
 pptx.writeFile({fileName:'Atlas_One_Deck_'+safe+'.pptx'});
}
$('btnDeck10').onclick=function(){run(function(){buildDeck10();});};
