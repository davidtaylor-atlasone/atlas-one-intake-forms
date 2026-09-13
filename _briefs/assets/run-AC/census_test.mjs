import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const [file, outdir] = process.argv.slice(2); fs.mkdirSync(outdir, { recursive: true });
const br = await chromium.launch(); const ctx = await br.newContext({ viewport: { width: 1440, height: 1000 }, acceptDownloads: true }); const pg = await ctx.newPage();
const errs = []; pg.on('pageerror', e => errs.push(e.message)); pg.on('dialog', d => d.accept());
await pg.route('**/*', r => /^(file|data|blob):/.test(r.request().url()) ? r.continue() : r.abort());
await pg.goto('file://' + file);
await pg.click('label[data-val="small"]'); await pg.click('[data-panel="1"] [data-next]');
await pg.fill('[name=companyName]', 'Ridgeline Concrete LLC'); await pg.fill('[name=zip]', '84043'); await pg.fill('[name=effectiveDate]', '2027-01-01'); await pg.fill('[name=eligible]', '8');
await pg.click('[data-panel="2"] [data-next]');
await pg.click('#coverageChips .chip:nth-child(1)'); await pg.selectOption('[name=multiPlan]', 'two'); await pg.click('[data-panel="3"] [data-next]');
console.log('addr cols visible at 8 EE:', await pg.$eval('th.addr-col', e => getComputedStyle(e).display));
// fill first row + add spouse and child
const rows = await pg.$$('#censusBody tr'); await rows[0].$eval('.c-first', e => e.value = 'Marcus'); await rows[0].$eval('.c-last', e => e.value = 'Dahl'); await rows[0].$eval('.c-dob', e => e.value = '04/02/1981'); await rows[0].$eval('.c-gender', e => e.value = 'Male'); await rows[0].$eval('.c-zip', e => e.value = '84043'); await rows[0].$eval('.c-tier', e => e.value = 'Family');
await rows[0].$eval('.c-ssn', e => { e.focus(); e.value = '123456789'; e.dispatchEvent(new Event('input', { bubbles: true })); e.blur(); });
console.log('ssn shown masked:', await rows[0].$eval('.c-ssn', e => e.value));
await rows[0].$eval('.row-add[data-rel=Spouse]', e => e.click()); await rows[0].$eval('.row-add[data-rel=Child]', e => e.click());
const all = await pg.$$('#censusBody tr'); console.log('rows now', all.length, 'classes', await pg.$$eval('#censusBody tr', t => t.map(x => x.className)));
await all[1].$eval('.c-first', e => e.value = 'Jenna'); await all[1].$eval('.c-dob', e => e.value = '1983'); await all[2].$eval('.c-first', e => e.value = 'Leo'); await all[2].$eval('.c-dob', e => e.value = '9');
console.log('count text:', await pg.textContent('#empCount'));
// switch to 12 employees -> address columns show
await pg.$eval('[name=eligible]', e => { e.value = '12'; e.dispatchEvent(new Event('input', { bubbles: true })); }); await pg.waitForTimeout(50); console.log('addr cols visible at 12 EE:', await pg.$eval('th.addr-col', e => getComputedStyle(e).display));
await pg.screenshot({ path: path.join(outdir, 'census_step4_1440.png'), fullPage: true });
// payload
const payload = await pg.evaluate(() => { const f = document.getElementById('downloadCsv'); return null; });
const data = await pg.evaluate(() => { // reach collectData through the review builder: rebuild and read the DOM is indirect, so re-implement by calling the button handler that logs? Instead expose via a temporary hook.
  return null; });
// Download CSV and check SSN is there; then inspect review to confirm SSN absent
await pg.click('[data-panel="4"] [data-next]'); await pg.fill('[name=contactName]', 'Marcus Dahl'); await pg.fill('[name=contactEmail]', 'marcus@example.com'); await pg.click('#buildReview');
const review = await pg.textContent('#reviewOut'); console.log('review has SSN digits?', /123456789|\*\*\*-\*\*-6789/.test(review), '| employees line:', review.match(/Employees entered\s*\S+[^\n]*/)[0].slice(0, 60));
const dlP = pg.waitForEvent('download'); await pg.click('#downloadCsv'); const dl = await dlP; const csvPath = path.join(outdir, dl.suggestedFilename()); await dl.saveAs(csvPath);
const csv = fs.readFileSync(csvPath, 'utf8'); console.log('csv has SSN:', csv.includes('123456789'), '| header:', csv.split('\n').find(l => l.startsWith('First')).trim()); console.log(csv.split('\n').slice(-5).join('\n'));
await pg.screenshot({ path: path.join(outdir, 'census_review_1440.png'), fullPage: true });
// CSV import: old 8-col format
await pg.click('[data-panel="5"] [data-back]');
fs.writeFileSync(path.join(outdir, 'old_format.csv'), 'First,Last/ID,DOB or Age,Gender,ZIP,Tier,Tobacco,Dependents\r\nJane,Doe,04/12/1985,Female,84101,EE+Spouse,N,1\r\n');
await pg.setInputFiles('#csvFile', path.join(outdir, 'old_format.csv')); await pg.waitForTimeout(200); console.log('old csv:', await pg.textContent('#csvStatus'));
const last = (await pg.$$('#censusBody tr')).slice(-1)[0]; console.log('  imported ->', await last.$eval('.c-first', e => e.value), await last.$eval('.c-rel', e => e.value), await last.$eval('.c-zip', e => e.value), await last.$eval('.c-tier', e => e.value));
// new template
const tpl = await pg.$eval('#csvTemplate', a => decodeURIComponent(a.getAttribute('href').split(',')[1])); fs.writeFileSync(path.join(outdir, 'template.csv'), tpl);
await pg.setInputFiles('#csvFile', path.join(outdir, 'template.csv')); await pg.waitForTimeout(200); console.log('template csv:', await pg.textContent('#csvStatus'), '| classes tail', (await pg.$$eval('#censusBody tr', t => t.map(x => x.className))).slice(-4).join(','));
await pg.setViewportSize({ width: 390, height: 844 }); await pg.waitForTimeout(100); console.log('sw390', await pg.evaluate(() => document.documentElement.scrollWidth)); await pg.screenshot({ path: path.join(outdir, 'census_390.png') });
console.log('errors', errs); await br.close();
