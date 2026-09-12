import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
const [outdir,...files]=process.argv.slice(2); const b=await chromium.launch();
for (const f of files){ const base=f.split('/').pop().replace(/\.html$/,'').replace(/[^A-Za-z0-9]+/g,'_');
  for (const w of [390,1440]){ const pg=await b.newPage({viewport:{width:w,height:w===390?844:900},isMobile:w===390,hasTouch:w===390});
    await pg.goto('file://'+f); await pg.waitForTimeout(300);
    // measure the checkbox labels (touch target) too
    const chk=await pg.evaluate(()=>{const l=document.querySelector('.chk'); if(!l) return null; const r=l.getBoundingClientRect(); return [Math.round(r.width),Math.round(r.height)];});
    await pg.screenshot({path:`${outdir}/${base}_${w}.png`,fullPage:true}); console.log(base,w,'chk label',chk); await pg.close(); } }
await b.close();
