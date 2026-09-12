// Print each division sheet HTML to a one page Letter PDF beside it.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
const b=await chromium.launch();
for (const f of process.argv.slice(2)){ const pg=await b.newPage(); await pg.goto('file://'+f); await pg.waitForTimeout(500); await pg.emulateMedia({media:'print'});
  const out=f.replace(/\.html$/,'.pdf'); await pg.pdf({path:out,format:'Letter',printBackground:true,preferCSSPageSize:true,margin:{top:0,right:0,bottom:0,left:0}}); console.log('pdf',out.split('/').pop()); await pg.close(); }
await b.close();
