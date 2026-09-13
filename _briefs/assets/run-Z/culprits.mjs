// Run Z: at 390 px, list the deepest elements wider than the viewport (the ones that force the overflow), with their CSS width/min-width.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
const files=process.argv.slice(2); const b=await chromium.launch();
for (const f of files){
  const pg=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:1,isMobile:true,hasTouch:true});
  await pg.route('**/*', r => r.request().url().startsWith('file://') ? r.continue() : r.abort());
  await pg.goto('file://'+f); await pg.waitForTimeout(400);
  const r=await pg.evaluate(()=>{const vw=document.documentElement.clientWidth; const wide=el=>{const bb=el.getBoundingClientRect(); return bb.right>vw+1||bb.width>vw+1;};
    const out=[]; document.querySelectorAll('body *').forEach(el=>{ if(!wide(el)) return; if([...el.children].some(wide)) return; const bb=el.getBoundingClientRect(); const cs=getComputedStyle(el);
      const path=[]; let e=el; while(e && e!==document.body && path.length<4){path.unshift(e.tagName.toLowerCase()+(e.id?'#'+e.id:'')+(e.className&&typeof e.className==='string'?'.'+e.className.trim().split(/\s+/).join('.'):'')); e=e.parentElement;}
      out.push({path:path.join(' > ').slice(0,140),w:Math.round(bb.width),right:Math.round(bb.right),disp:cs.display,width:cs.width,minw:cs.minWidth,ws:cs.whiteSpace,txt:(el.textContent||'').trim().slice(0,40)});});
    return {sw:document.documentElement.scrollWidth,out};});
  console.log('\n##',f.split('/').pop(),'scrollWidth',r.sw,'deepest wide elements',r.out.length);
  r.out.slice(0,40).forEach(o=>console.log('  ',JSON.stringify(o)));
  await pg.close();
}
await b.close();
