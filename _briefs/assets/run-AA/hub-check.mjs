import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs';
const [outdir, hub] = process.argv.slice(2);
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1440, height: 900 } });
const errs = []; pg.on('pageerror', e => errs.push(String(e.message)));
await pg.route('**/*', r => r.request().url().startsWith('file://') ? r.continue() : r.abort());
await pg.goto('file://' + hub, { waitUntil: 'load' }); await pg.waitForTimeout(500);
const r = await pg.evaluate(() => {
  const count = document.getElementById('count').textContent;
  const card = [...document.querySelectorAll('article.card')].find(x => /Time and Cost Savings Discovery/.test(x.textContent));
  const a = card ? card.querySelector('a[href*="Time_Savings"]') : null;
  return { count, cards: document.querySelectorAll('article.card').length, cat: card ? card.closest('.cat').getAttribute('data-cat') : null, found: !!card, href: a ? a.getAttribute('href') : null, text: card ? card.textContent.replace(/\s+/g, ' ').trim().slice(0, 200) : null };
});
r.errors = errs; console.log(JSON.stringify(r, null, 1));
await pg.screenshot({ path: `${outdir}/Tools_Hub_1440.png`, fullPage: false });
fs.writeFileSync(`${outdir}/_hub-log.json`, JSON.stringify(r, null, 1)); await b.close();
