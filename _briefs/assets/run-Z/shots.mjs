// Run Z (from Run W): render every changed tool at 390 px (mobile, touch) and 1440 px, full page, record scrollWidth and JS errors.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs';
const [outdir, ...files] = process.argv.slice(2); fs.mkdirSync(outdir, { recursive: true });
const b = await chromium.launch(); const log = [];
for (const f of files) {
  const base = f.split('/').pop().replace(/\.html$/, '').replace(/[^A-Za-z0-9]+/g, '_').slice(0, 50);
  for (const w of [390, 1440]) {
    const pg = await b.newPage({ viewport: { width: w, height: w === 390 ? 844 : 900 }, isMobile: w === 390, hasTouch: w === 390 });
    const errs = []; pg.on('pageerror', e => errs.push(String(e.message).slice(0, 120)));
    await pg.route('**/*', r => r.request().url().startsWith('file://') ? r.continue() : r.abort());
    await pg.goto('file://' + f, { waitUntil: 'load', timeout: 60000 }); await pg.waitForTimeout(500);
    const sw = await pg.evaluate(() => document.documentElement.scrollWidth);
    await pg.screenshot({ path: `${outdir}/${base}_${w}.png`, fullPage: true });
    log.push({ file: f.split('/').pop(), w, scrollWidth: sw, errors: errs });
    console.log(base.padEnd(52), w, 'scrollWidth', sw, errs.length ? 'ERRORS ' + errs.join(' | ') : '');
    await pg.close();
  }
}
await b.close(); fs.writeFileSync(`${outdir}/_render-log.json`, JSON.stringify(log, null, 1));
