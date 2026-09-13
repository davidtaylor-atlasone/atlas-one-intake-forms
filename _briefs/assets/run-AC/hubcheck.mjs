import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const [hub, q, shot] = process.argv.slice(2);
const br = await chromium.launch(); const pg = await br.newPage({ viewport: { width: 1280, height: 800 } });
const errs = []; pg.on('pageerror', e => errs.push(e.message));
await pg.goto('file://' + hub); await pg.fill('#search', q); await pg.waitForTimeout(200);
const cards = await pg.$$eval('.doc', els => els.map(e => ({ t: e.querySelector('.t').textContent, href: e.querySelector('a.b').getAttribute('href') })));
for (const c of cards) { const p = decodeURIComponent(c.href); const abs = path.resolve(path.dirname(hub), p); console.log(c.t, '|', fs.existsSync(abs) ? 'resolves' : 'MISSING ' + abs); }
await pg.screenshot({ path: shot }); console.log('errors', errs); await br.close();
