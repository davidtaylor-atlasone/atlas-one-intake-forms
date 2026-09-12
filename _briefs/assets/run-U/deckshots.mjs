import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const dir=path.resolve(process.argv[2]), out=path.resolve(process.argv[3]); fs.mkdirSync(out,{recursive:true});
const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1280,height:720}});
const files=fs.readdirSync(dir).filter(f=>f.endsWith('.html')).sort(); const report=[];
for (const f of files){
  await pg.goto('file://'+path.join(dir,f)); await pg.waitForTimeout(120);
  const ov=await pg.evaluate(()=>{const r=[]; document.querySelectorAll('.sh').forEach(s=>{const tf=s.querySelector('.tf'); if(!tf) return; const tx=tf.querySelector('.tx'); const box=s.getBoundingClientRect(); const cs=getComputedStyle(tf); const inner=box.height-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom); const innerW=box.width-parseFloat(cs.paddingLeft)-parseFloat(cs.paddingRight); const th=tx.scrollHeight, tw=tx.scrollWidth; if(th>inner+2||tw>innerW+2) r.push({name:s.dataset.name,text:tx.textContent.trim().slice(0,60),boxH:Math.round(inner),textH:Math.round(th),boxW:Math.round(innerW),textW:Math.round(tw)});}); return r;});
  await pg.screenshot({path:path.join(out,f.replace('.html','.png')), clip:{x:0,y:0,width:1280,height:720}});
  report.push({slide:f,overflow:ov});
}
fs.writeFileSync(path.join(out,'overflow.json'),JSON.stringify(report,null,1));
for (const r of report) if(r.overflow.length) console.log(r.slide, r.overflow.map(o=>`${o.name} "${o.text}" box ${o.boxW}x${o.boxH} text ${o.textW}x${o.textH}`).join(' || '));
console.log('done',files.length);
await b.close();
