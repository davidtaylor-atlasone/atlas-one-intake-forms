// Report document scrollWidth vs viewport at 390px and list elements wider than the viewport.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
const files=process.argv.slice(2); const b=await chromium.launch();
for (const f of files){
  const pg=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:1,isMobile:true,hasTouch:true});
  const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
  await pg.goto('file://'+f); await pg.waitForTimeout(300);
  const r=await pg.evaluate(()=>{const vw=document.documentElement.clientWidth; const out=[];
    document.querySelectorAll('body *').forEach(el=>{const bb=el.getBoundingClientRect(); if(bb.right>vw+1||bb.width>vw+1){const cs=getComputedStyle(el); out.push({tag:el.tagName.toLowerCase(),id:el.id,cls:(el.className||'').toString().slice(0,50),w:Math.round(bb.width),right:Math.round(bb.right),disp:cs.display,minw:cs.minWidth});}});
    // small touch targets
    const small=[]; document.querySelectorAll('input,select,button,a,textarea,summary').forEach(el=>{const bb=el.getBoundingClientRect(); if(bb.width>0&&bb.height>0&&bb.height<44) small.push({tag:el.tagName.toLowerCase(),id:el.id,cls:(el.className||'').toString().slice(0,30),h:Math.round(bb.height),txt:(el.textContent||'').trim().slice(0,30)});});
    return {vw,sw:document.documentElement.scrollWidth,bodyW:document.body.scrollWidth,over:out.slice(0,25),overCount:out.length,small:small.slice(0,60),smallCount:small.length};});
  console.log('\n##',f.split('/').pop(),'viewport',r.vw,'scrollWidth',r.sw,'body',r.bodyW,'errors',errs);
  console.log('wide elements',r.overCount); r.over.forEach(o=>console.log('  ',JSON.stringify(o)));
  console.log('touch <44px',r.smallCount); r.small.forEach(o=>console.log('  ',JSON.stringify(o)));
  await pg.close();
}
await b.close();
