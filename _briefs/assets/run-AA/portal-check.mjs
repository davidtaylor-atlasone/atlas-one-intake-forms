// Run AA: open the single-file Portal from file://, read the stamp, click the two new cards, confirm each tool renders inside the #frame iframe.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs';
const [outdir, portal] = process.argv.slice(2); fs.mkdirSync(outdir, { recursive: true });
const b = await chromium.launch(); const out = {};
const pg = await b.newPage({ viewport: { width: 1440, height: 900 } });
const errs = []; pg.on('pageerror', e => errs.push(String(e.message).slice(0, 160)));
const reqs = []; pg.on('request', r => reqs.push(r.url()));
await pg.route('**/*', r => r.request().url().startsWith('file://') ? r.continue() : r.abort());
await pg.goto('file://' + portal, { waitUntil: 'load', timeout: 120000 }); await pg.waitForTimeout(800);
out.title = await pg.title();
out.stamp = await pg.evaluate(() => (document.querySelector('.buildchip') || {}).textContent);
out.note = await pg.evaluate(() => (document.querySelector('.note') || {}).textContent.replace(/\s+/g, ' ').trim());
out.cards = await pg.evaluate(() => document.querySelectorAll('#cards .card').length);
await pg.screenshot({ path: `${outdir}/Portal_home_1440.png`, fullPage: false });
for (const [label, id] of [['onboarding_tracker', 't6'], ['time_savings', 't13']]) {
  await pg.evaluate(() => { const t = document.querySelector('.tab[data-cat=""]'); if (t) t.click(); }); await pg.waitForTimeout(300);
  const card = pg.locator(`#cards .card[data-tool="${id}"]`);
  const cardText = (await card.innerText()).replace(/\s+/g, ' ').trim();
  await card.click(); await pg.waitForTimeout(1200);
  const r = await pg.evaluate(() => {
    const f = document.getElementById('frame'); const d = f && f.contentWindow && f.contentWindow.document;
    const h1 = d && d.querySelector('h1'); const pill = document.querySelector('.pill.on');
    return { frameOn: !!(f && f.classList.contains('on')), frameSrcAttr: f ? (f.getAttribute('src') || '') : null,
      innerTitle: d ? d.title : null, innerH1: h1 ? h1.textContent.replace(/\s+/g, ' ').trim() : null,
      innerBodyChars: d && d.body ? d.body.innerHTML.length : 0, innerInputs: d ? d.querySelectorAll('input,select,textarea').length : 0,
      pillOn: pill ? pill.textContent.trim() : null, homeOff: document.querySelector('#home, .home') ? document.querySelector('#home, .home').classList.contains('off') : null };
  });
  await pg.screenshot({ path: `${outdir}/Portal_${label}_1440.png`, fullPage: false });
  out[label] = { card: cardText, ...r };
}
out.errors = errs; out.nonFileRequests = reqs.filter(u => !u.startsWith('file://'));
console.log(JSON.stringify(out, null, 1));
fs.writeFileSync(`${outdir}/_portal-log.json`, JSON.stringify(out, null, 1));
await b.close();
