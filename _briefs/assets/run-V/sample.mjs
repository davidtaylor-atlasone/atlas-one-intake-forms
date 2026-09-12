// Run one sample calculation and dump every output number, so before/after can be compared.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs';
const [file,out]=process.argv.slice(2); const b=await chromium.launch();
const pg=await b.newPage({viewport:{width:1440,height:900}}); const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
await pg.goto('file://'+file); await pg.waitForTimeout(300);
const res=await pg.evaluate(()=>{
  const set=(id,v)=>{const el=document.getElementById(id); if(!el) return false; if(el.type==='checkbox'){el.checked=v; el.dispatchEvent(new Event('change',{bubbles:true}));} else {el.value=v; el.dispatchEvent(new Event('input',{bubbles:true}));} return true;};
  const used=[];
  // retention calculator sample
  for (const [id,v] of Object.entries({empSalary:52000,empPct:30,empHire:45,empRamp:90,empCustPerRep:250,empProd:60,empValue:900,empTeam:6,empChurn:35,cac:350,retMult:5,revCust:2400,margin:55,lifespan:4,acqSpend:9000,acqNew:20,acqDays:30,churn:18,totalCust:320,referrals:1.5})) if(set(id,v)) used.push(id);
  // vendor consolidation sample
  const cats=['payroll','books','tax','hr','ben','health','bizins','wc','it','pos','crm','adv'];
  cats.forEach((k,i)=>{ if(set(k+'_on', i%2===0)) used.push(k+'_on'); set(k+'_cost', 100+i*75); set(k+'_hrs', 1+i*0.5); });
  set('rate',75); set('eff',60);
  const outs={};
  document.querySelectorAll('.big,.out .row b,.bar-row .val,#ratioText,#doorText,#vcards,#vtext').forEach((el,i)=>{outs[(el.id||el.className||el.tagName)+'#'+i]=el.textContent.replace(/\s+/g,' ').trim();});
  return {used:used.length,outs};
});
res.errors=errs; fs.writeFileSync(out,JSON.stringify(res,null,1)); console.log(file.split('/').pop(),'inputs set',res.used,'outputs',Object.keys(res.outs).length,'errors',errs);
await b.close();
