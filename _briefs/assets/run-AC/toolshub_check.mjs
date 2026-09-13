import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const [hub, q, shot] = process.argv.slice(2);
const br = await chromium.launch(); const pg = await br.newPage({ viewport: { width: 1280, height: 900 } });
const errs = []; pg.on('pageerror', e => errs.push(e.message));
await pg.route('**/*', r => /^(file|data|blob):/.test(r.request().url()) ? r.continue() : r.abort());
await pg.goto('file://' + hub); await pg.fill('#search', q); await pg.waitForTimeout(250);
const links = await pg.$$eval('#hub a[href]', els => els.map(e => ({ t: e.textContent.trim().slice(0, 50), href: e.getAttribute('href') })).filter(l => !/^https?:|^tel:|^mailto:/.test(l.href)));
for (const l of links) { const p = decodeURIComponent(l.href); console.log(l.t, '|', fs.existsSync(path.resolve(path.dirname(hub), p)) ? 'resolves' : 'MISSING ' + p); }
await pg.screenshot({ path: shot }); console.log('count', await pg.textContent('#count'), 'errors', errs); await br.close();
