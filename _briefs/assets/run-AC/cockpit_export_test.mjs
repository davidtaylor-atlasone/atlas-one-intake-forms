// Run AC job 3: open the Cockpit offline, load a sample prospect into page state, click "Export deck (.pptx)",
// save the download, screenshot the page at 1440 and 390.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const [file, outdir] = process.argv.slice(2); fs.mkdirSync(outdir, { recursive: true });
const br = await chromium.launch(); const ctx = await br.newContext({ viewport: { width: 1440, height: 900 }, acceptDownloads: true });
const pg = await ctx.newPage(); const errs = []; pg.on('pageerror', e => errs.push(String(e.message)));
pg.on('console', m => { if (m.type() === 'error' && !/Unsafe attempt/.test(m.text())) errs.push('console: ' + m.text()); });
const reqs = []; pg.on('request', r => { if (!/^(file|data|blob):/.test(r.url())) reqs.push(r.url()); });
await pg.route('**/*', r => /^(file|data|blob):/.test(r.request().url()) ? r.continue() : r.abort());
pg.on('dialog', d => { errs.push('dialog: ' + d.message()); d.dismiss(); });
await pg.goto('file://' + file, { waitUntil: 'load' });
await pg.evaluate(() => {
  const e = blankEntity();
  e.company = { name: 'Ridgeline Concrete LLC', industry: 'Construction', website: 'ridgelineconcrete.com', fein: '', referrer: 'Brittney (BRJ)', preparer: 'David Taylor',
    contacts: [{ role: 'Owner', name: 'Marcus Dahl', phone: '801 555 0142', email: 'marcus@ridgelineconcrete.com' }, { role: 'Office manager', name: 'Jenna Ruiz', phone: '', email: '' }] };
  e.employees = { ee: '38', gross: '182000', freq: '26', schedules: [] };
  e.states = [{ st: 'UT', ee: '30' }, { st: 'ID', ee: '8' }];
  e.wc = { carrier: 'Travelers', premium: '61400', quote: '52900', codes: [{ st: 'UT', code: '5213', desc: 'Concrete construction', payroll: '1500000', rate: '6.10' }] };
  e.payroll = { model: 'peo_check', rate: '18', brands: ['atlasOne'] };
  e.benefits = [{ type: 'Health insurance', label: '', total: '21400', employer: '12800' }, { type: 'Dental', label: '', total: '1900', employer: '950' }, { type: 'Group life', label: '', total: '0', employer: '0' }];
  const on = { mem: 1, certpay: null, screen: null, hbCustom: null, safeCustom: null, aiemail: 0 };
  e.services.forEach(a => { if (a[0] in on) { a[6] = true; const oi = on[a[0]]; if (oi !== null && a[7]) { a._opt = oi; a[1] = a[7][oi][0]; a[3] = a[7][oi][1]; if (a[7][oi].length > 2) a[4] = a[7][oi][2]; } } });
  e.timeSavings = { hours: '22', rate: '85', soft: '340', note: 'No more chasing timecards across two states, one invoice instead of nine, certified payroll filed for you, WC audit handled.' };
  e.cur = '9800'; e.discType = 'pct'; e.discVal = '5'; e.tgt = '30'; e.notes = 'Bidding two public jobs in Q1, needs WH-347 from January. Wants dental added for foremen.';
  ENT = [e]; curE = 0; fill();
});
await pg.waitForTimeout(400);
const summary = await pg.evaluate(() => ({ sum: document.getElementById('sum').innerText, save: document.getElementById('save').textContent, sw: document.documentElement.scrollWidth }));
console.log(summary.sum.replace(/\n/g, ' | ')); console.log('savings/yr', summary.save);
await pg.screenshot({ path: path.join(outdir, 'cockpit_1440.png'), fullPage: false });
const dlP = pg.waitForEvent('download', { timeout: 60000 });
await pg.click('#btnDeck10');
const dl = await dlP; const target = path.join(outdir, dl.suggestedFilename()); await dl.saveAs(target);
console.log('downloaded', dl.suggestedFilename(), fs.statSync(target).size, 'bytes');
// mobile
await pg.setViewportSize({ width: 390, height: 844 }); await pg.waitForTimeout(300);
const sw = await pg.evaluate(() => document.documentElement.scrollWidth); console.log('scrollWidth at 390:', sw);
await pg.screenshot({ path: path.join(outdir, 'cockpit_390.png'), fullPage: false });
console.log('errors', errs, 'non-file requests', reqs.length);
await br.close();
