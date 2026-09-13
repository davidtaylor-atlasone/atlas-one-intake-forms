// Run Z: the Run Y sample on the Time Savings tool (rate 40, first task 2 hrs, first subscription $120), dump outputs.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs';
const [file,out]=process.argv.slice(2); const b=await chromium.launch();
const pg=await b.newPage({viewport:{width:1440,height:900}}); const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
await pg.route('**/*', r => r.request().url().startsWith('file://') ? r.continue() : r.abort());
await pg.goto('file://'+file); await pg.waitForTimeout(400);
const res=await pg.evaluate(()=>{
  const set=(el,v)=>{el.value=v; el.dispatchEvent(new Event('input',{bubbles:true})); el.dispatchEvent(new Event('change',{bubbles:true}));};
  set(document.getElementById('rate'),40);
  const t=document.querySelector('#tasks tr'); set(t.querySelector('input.c'),2);
  const s=document.querySelector('#soft tr'); set(s.querySelector('input.c'),120);
  const outs={}; ['hrs','timeSave','softYr','taskHrs','grand'].forEach(id=>outs[id]=document.getElementById(id).textContent.trim());
  outs.resText=document.querySelector('.res')?.innerText.replace(/\s+/g,' ').trim();
  outs.tableText=[...document.querySelectorAll('table')].map(t=>t.innerText.replace(/\s+/g,' ').trim()).join(' || ');
  return outs;});
res.errors=errs; fs.writeFileSync(out,JSON.stringify(res,null,1)); console.log(file.split('/').pop(),JSON.stringify(res).slice(0,300));
await b.close();
