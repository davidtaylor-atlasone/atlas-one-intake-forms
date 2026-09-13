import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const [file, outdir] = process.argv.slice(2); fs.mkdirSync(outdir, { recursive: true });
const br = await chromium.launch(); const ctx = await br.newContext({ viewport: { width: 1440, height: 1000 }, acceptDownloads: true }); const pg = await ctx.newPage();
const errs = []; pg.on('pageerror', e => errs.push(e.message)); pg.on('dialog', d => { console.log('dialog:', d.message().slice(0, 60)); d.accept(); });
await pg.route('**/*', r => /^(file|data|blob):/.test(r.request().url()) ? r.continue() : r.abort());
await pg.goto('file://' + file);
const d = (n) => { const x = new Date(); x.setDate(x.getDate() + n); return x.toISOString().slice(0, 10); };
await pg.evaluate((d) => {
  S.gc = 'Ridgeline Concrete LLC'; S.proj = 'Job 2041 Lehi warehouse'; S.me = 'Jenna Ruiz'; S.mec = 'jenna@ridgelineconcrete.com';
  S.subs = [
    { id: 'a', name: 'Summit Electrical LLC', trade: 'Electrical', email: 'office@summitelec.com', phone: '801 555 0172', gl: 'yes', glx: d[0], wc: 'yes', wcx: d[1], wv: 'yes', hold: 'auto', notes: '' },
    { id: 'b', name: 'Wasatch Plumbing', trade: 'Plumbing', email: 'ap@wasatchplumbing.com', phone: '', gl: 'yes', glx: d[2], wc: 'yes', wcx: d[0], wv: 'yes', hold: 'auto', notes: '' },
    { id: 'c', name: 'Dahl Framing', trade: 'Framing', email: 'marcus@dahlframing.com', phone: '', gl: 'yes', glx: d[3], wc: 'no', wcx: '', wv: 'no', hold: 'auto', notes: '' },
    { id: 'd', name: 'Peak Drywall', trade: 'Drywall', email: '', phone: '', gl: 'no', glx: '', wc: 'yes', wcx: d[0], wv: 'yes', hold: 'release', notes: '' },
    { id: 'e', name: 'Canyon Roofing', trade: 'Roofing', email: 'x@canyonroof.com', phone: '', gl: 'yes', glx: d[0], wc: 'yes', wcx: d[0], wv: 'yes', hold: 'hold', notes: '' },
  ]; render();
}, [d(200), d(300), d(12), d(-5)]);
await pg.waitForTimeout(200);
const r = await pg.evaluate(() => ({ stats: document.getElementById('stats').innerText.replace(/\n/g, ' '), rows: [...document.querySelectorAll('#rows tr')].map(t => t.querySelector('input[data-k=name]').value + ' -> ' + t.querySelector('.st').textContent) }));
console.log(r.stats); r.rows.forEach(x => console.log('  ', x));
await pg.selectOption('#emailSub', '2'); await pg.waitForTimeout(100); console.log('--- email for Dahl Framing:\n' + await pg.textContent('#emailOut'));
await pg.selectOption('#emailSub', '1'); await pg.selectOption('#tone', 'hold'); await pg.waitForTimeout(100); console.log('--- hold email for Wasatch:\n' + (await pg.textContent('#emailOut')).slice(0, 500));
await pg.screenshot({ path: path.join(outdir, 'coi_1440.png'), fullPage: true });
let dlP = pg.waitForEvent('download'); await pg.click('#exportCsv'); let dl = await dlP; const csvPath = path.join(outdir, dl.suggestedFilename()); await dl.saveAs(csvPath); console.log('csv:\n' + fs.readFileSync(csvPath, 'utf8'));
dlP = pg.waitForEvent('download'); await pg.click('#saveJson'); dl = await dlP; const jp = path.join(outdir, dl.suggestedFilename()); await dl.saveAs(jp); console.log('json saved', dl.suggestedFilename(), fs.statSync(jp).size);
// clear then import csv back
await pg.click('#clearAll'); await pg.waitForTimeout(100); console.log('after clear rows:', await pg.$$eval('#rows tr', e => e.length));
await pg.setInputFiles('#fileCsv', csvPath); await pg.waitForTimeout(300); console.log('after csv import rows:', await pg.$$eval('#rows tr', e => e.length), await pg.evaluate(() => [...document.querySelectorAll('#rows .st')].map(s => s.textContent).join(', ')));
await pg.click('#clearAll'); await pg.setInputFiles('#fileJson', jp); await pg.waitForTimeout(300); console.log('after json load rows:', await pg.$$eval('#rows tr', e => e.length), 'gc:', await pg.inputValue('#gc'));
await pg.emulateMedia({ media: 'print' }); await pg.screenshot({ path: path.join(outdir, 'coi_print.png'), fullPage: true }); await pg.emulateMedia({ media: 'screen' });
await pg.setViewportSize({ width: 390, height: 844 }); await pg.waitForTimeout(200); console.log('sw390', await pg.evaluate(() => document.documentElement.scrollWidth)); await pg.screenshot({ path: path.join(outdir, 'coi_390.png'), fullPage: false });
console.log('errors', errs); await br.close();
