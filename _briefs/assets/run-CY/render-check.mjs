// Run CY render check. Usage: node render-check.mjs "<Master_Kit>" "<A1_Sales>" "<out dir>"
// Chromium and WebKit, 1440 and 390: COMMAND and Sales Kit load clean (scrollWidth equals viewport,
// zero console errors, zero non file requests). Then each agreement builder is filled once with a non
// Utah state and the Governing Law clause is screenshot. Also checks the blank state is required.
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
const require = createRequire(import.meta.url);
const { chromium, webkit } = require(process.env.PW_PATH || 'playwright');
const [MK, SALES, OUT] = process.argv.slice(2);
fs.mkdirSync(path.join(OUT, 'shots'), { recursive: true });
const results = { loads: [], builders: [] };

const pages = [
  ['COMMAND', path.join(MK, 'Atlas One COMMAND.html')],
  ['SalesKit', path.join(SALES, 'Atlas One Sales Kit.html')],
];
const TOOLS = path.join(MK, '06 Calculators and Tools (NEW Aug 2026)');

for (const [bname, bt] of [['chromium', chromium], ['webkit', webkit]]) {
  const browser = await bt.launch();
  for (const [label, file] of pages) {
    for (const w of [1440, 390]) {
      const ctx = await browser.newContext({ viewport: { width: w, height: 900 } });
      const page = await ctx.newPage();
      const errors = [], nonFile = [];
      page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
      page.on('pageerror', e => errors.push(String(e)));
      page.on('request', r => { if (!r.url().startsWith('file://') && !r.url().startsWith('data:') && !r.url().startsWith('blob:')) nonFile.push(r.url()); });
      await page.goto('file://' + file, { waitUntil: 'load' });
      await page.waitForTimeout(1500);
      const sw = await page.evaluate(() => document.documentElement.scrollWidth);
      const title = await page.title();
      results.loads.push({ browser: bname, page: label, width: w, scrollWidth: sw, ok: sw <= w, title, errors, nonFile });
      if (bname === 'chromium') await page.screenshot({ path: path.join(OUT, 'shots', `${label}-${w}.png`) });
      await ctx.close();
    }
  }
  // builders
  const builders = [
    ['IC', 'Independent Contractor Agreement Builder (Atlas One).html', 'Texas'],
    ['IC-DC', 'Independent Contractor Agreement Builder (Atlas One).html', 'District of Columbia'],
    ['W2', 'W-2 At-Will Employment Agreement Builder (Atlas One).html', 'Ohio'],
    ['NDA', 'NDA Builder (Atlas One).html', 'Florida'],
  ];
  for (const [id, file, state] of builders) {
    for (const w of [1440, 390]) {
      const ctx = await browser.newContext({ viewport: { width: w, height: 900 } });
      const page = await ctx.newPage();
      const errors = [], nonFile = [];
      page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
      page.on('pageerror', e => errors.push(String(e)));
      page.on('request', r => { if (!r.url().startsWith('file://') && !r.url().startsWith('data:') && !r.url().startsWith('blob:')) nonFile.push(r.url()); });
      await page.goto('file://' + path.join(TOOLS, file), { waitUntil: 'load' });
      await page.waitForTimeout(800);
      const sw = await page.evaluate(() => document.documentElement.scrollWidth);
      // blank state first
      const blank = await page.evaluate(() => {
        const sel = document.getElementById('govState');
        const doc = document.getElementById('contract') || document.getElementById('document') || document.getElementById('out') || document.body;
        const txt = (doc.innerText || '');
        const btn = document.getElementById('printBtn') || document.querySelector('.printGate');
        return { value: sel.value, optionCount: sel.options.length, hasDC: [...sel.options].some(o => o.value === 'District of Columbia'),
                 hasUtahSelected: sel.value === 'Utah', required: sel.required, invalid: sel.getAttribute('aria-invalid'),
                 stateBlankInDoc: /State of \[State\]/.test(txt), printDisabled: btn ? btn.disabled : null };
      });
      // pick the state
      await page.selectOption('#govState', state);
      await page.evaluate(() => {
        const g = document.getElementById('hhGate'); if (g && !g.checked) { g.checked = true; g.dispatchEvent(new Event('change', { bubbles: true })); }
      });
      await page.waitForTimeout(300);
      const after = await page.evaluate((st) => {
        const doc = document.getElementById('contract') || document.getElementById('document') || document.getElementById('out') || document.body;
        const txt = doc.innerText || '';
        const btn = document.getElementById('printBtn') || document.querySelector('.printGate');
        const gl = [...txt.matchAll(/[^.\n]*(governed by|governing law|laws of)[^.\n]*\./gi)].map(m => m[0].trim());
        const venue = [...txt.matchAll(/[^.\n]*(courts located in|administered in|venue)[^.\n]*\./gi)].map(m => m[0].trim());
        return { govClauses: gl, venueClauses: venue, printDisabled: btn ? btn.disabled : null, mentionsStateInClause: gl.some(x => x.includes(st)) };
      }, state);
      // screenshot the Governing Law clause
      const shot = path.join(OUT, 'shots', `${id}-${bname}-${w}.png`);
      const h = page.locator('h3:has-text("Governing Law"), h4:has-text("Governing Law")').first();
      if (await h.count()) {
        await h.scrollIntoViewIfNeeded();
        const box = await h.evaluate(el => { const r = el.getBoundingClientRect(); return { y: r.top }; });
        await page.screenshot({ path: shot });
      } else {
        await page.screenshot({ path: shot });
      }
      results.builders.push({ browser: bname, builder: id, width: w, state, scrollWidth: sw, scrollOk: sw <= w, blank, after, errors, nonFile });
      await ctx.close();
    }
  }
  await browser.close();
}
fs.writeFileSync(path.join(OUT, 'render-results.json'), JSON.stringify(results, null, 1));
const badLoads = results.loads.filter(r => !r.ok || r.errors.length || r.nonFile.length);
const badB = results.builders.filter(r => !r.scrollOk || r.errors.length || r.nonFile.length || !r.after.mentionsStateInClause);
console.log('loads', results.loads.length, 'bad', badLoads.length, '| builders', results.builders.length, 'bad', badB.length);
for (const b of badLoads) console.log('BAD LOAD', JSON.stringify(b).slice(0, 400));
for (const b of badB) console.log('BAD BUILDER', JSON.stringify(b).slice(0, 600));
