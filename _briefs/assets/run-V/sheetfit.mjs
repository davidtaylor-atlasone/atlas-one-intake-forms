// Screenshot each division sheet page and report the gap between the platform pills and the footer.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs';
const [outdir,...files]=process.argv.slice(2); const b=await chromium.launch();
for (const f of files){ const pg=await b.newPage({viewport:{width:900,height:1150},deviceScaleFactor:1.5});
  await pg.goto('file://'+f); await pg.waitForTimeout(400);
  const r=await pg.evaluate(()=>{const p=document.querySelector('.page').getBoundingClientRect(); const pl=document.querySelector('.plat').getBoundingClientRect(); const ft=document.querySelector('.foot').getBoundingClientRect(); const fine=document.querySelector('.fine').getBoundingClientRect(); return {pageBottom:Math.round(p.bottom),platBottom:Math.round(pl.bottom),footTop:Math.round(ft.top),gap:Math.round(ft.top-pl.bottom),fineBottom:Math.round(fine.bottom)};});
  const base=f.split('/').pop().replace('.html','');
  const page=await pg.$('.page'); await page.screenshot({path:`${outdir}/${base}.png`});
  console.log(base, JSON.stringify(r)); await pg.close(); }
await b.close();
