// Run AC: render each file offline (only file:// allowed) at 1440 and 390 px. Record the computed font on body,
// the rendered face (CDP CSS.getPlatformFontsForNode) of text elements that ask for DM Sans, scrollWidth at 390,
// JS errors, non-file requests. Screenshot both widths.
//   node verify.mjs <outdir> <file> [<file> ...]
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const [outdir, ...files] = process.argv.slice(2); fs.mkdirSync(outdir, { recursive: true });
const SAMPLE = 'h1,h2,h3,p,label,button,th,td,li,a,span,small,b,strong,input,select';
const br = await chromium.launch(); const results = [];
async function render(file, width) {
  const pg = await br.newPage({ viewport: { width, height: width < 500 ? 844 : 900 }, deviceScaleFactor: 1 });
  const errs = []; pg.on('pageerror', e => errs.push(String(e.message).slice(0, 160)));
  pg.on('console', m => { if (m.type() === 'error' && !/Unsafe attempt to load URL file:/.test(m.text())) errs.push('console: ' + m.text().slice(0, 160)); });  // the 'Unsafe attempt' line is Playwright's route.continue() on file://, confirmed absent without routing
  const reqs = []; pg.on('request', r => { if (!r.url().startsWith('file://') && !r.url().startsWith('data:') && !r.url().startsWith('blob:')) reqs.push(r.url().slice(0, 100)); });
  await pg.route('**/*', r => { const u = r.request().url(); return (u.startsWith('file://') || u.startsWith('data:') || u.startsWith('blob:')) ? r.continue() : r.abort(); });
  await pg.goto('file://' + file, { waitUntil: 'load', timeout: 120000 });
  await pg.evaluate(() => document.fonts.ready).catch(() => {}); await pg.waitForTimeout(700);
  const cdp = await pg.context().newCDPSession(pg); await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
  const { root } = await cdp.send('DOM.getDocument', { depth: -1 });
  const handles = await pg.evaluate((SAMPLE) => {
    const out = []; const seen = new Set();
    for (const el of document.querySelectorAll(SAMPLE)) {
      if (out.length >= 30) break;
      const t = (el.childNodes[0] && el.childNodes[0].nodeType === 3 ? el.childNodes[0].textContent : '').trim(); if (!t) continue;
      const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
      const ff = getComputedStyle(el).fontFamily; const key = el.tagName + '|' + ff; if (seen.has(key)) continue; seen.add(key);
      el.setAttribute('data-a1probe', String(out.length)); out.push({ i: out.length, tag: el.tagName.toLowerCase(), family: ff.slice(0, 60), weight: getComputedStyle(el).fontWeight, text: t.slice(0, 30) });
    } return out; }, SAMPLE);
  for (const h of handles) {
    const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: `[data-a1probe="${h.i}"]` });
    const { fonts } = await cdp.send('CSS.getPlatformFontsForNode', { nodeId });
    h.rendered = fonts.map(f => `${f.familyName}${f.isCustomFont ? '' : ' (system)'}:${f.glyphCount}`).join(', ');
  }
  await pg.evaluate(() => document.querySelectorAll('[data-a1probe]').forEach(e => e.removeAttribute('data-a1probe')));
  const first = f => f.replace(/^["']/, '').split(/["']?\s*,/)[0].trim();
  const dmAsked = handles.filter(h => first(h.family) === 'DM Sans');
  const dmRendered = dmAsked.filter(h => /^DM Sans( Medium| SemiBold| 9pt)?:/.test(h.rendered));
  const horasAsked = handles.filter(h => first(h.family) === 'Horas');
  const horasRendered = horasAsked.filter(h => /^Horas/.test(h.rendered));
  const serif = handles.filter(h => /Times|Georgia/.test(h.rendered) && !/Serif/i.test(h.family));
  const m = await pg.evaluate(() => ({ bodyFamily: getComputedStyle(document.body).fontFamily.slice(0, 60), sw: document.documentElement.scrollWidth, bsw: document.body.scrollWidth, sh: document.documentElement.scrollHeight, title: document.title, dmCheck: document.fonts.check('16px "DM Sans"') }));
  const base = path.basename(file).replace(/\.html$/, '').replace(/[^A-Za-z0-9]+/g, '_').slice(0, 45);
  await pg.screenshot({ path: `${outdir}/${base}_${width}.png`, fullPage: false });
  await pg.close();
  return { width, ...m, bodyRendered: dmAsked[0] ? dmAsked[0].rendered : (handles[0] ? handles[0].rendered : null), dmAsked: dmAsked.length, dmRendered: dmRendered.length, horasAsked: horasAsked.length, horasRendered: horasRendered.length, serif: serif.length, errors: errs, nonFileRequests: reqs, samples: handles };
}
for (const f of files) {
  const d = await render(f, 1440); const m = await render(f, 390);
  const rec = { file: path.basename(f), desktop: d, mobile: m };
  results.push(rec);
  const ok = d.dmAsked === d.dmRendered && d.serif === 0 && d.errors.length === 0 && d.nonFileRequests.length === 0 && m.sw <= 390;
  console.log((ok ? 'OK  ' : 'LOOK') + ' ' + path.basename(f).padEnd(60), '| body', d.bodyFamily.slice(0, 22).padEnd(22), '->', String(d.bodyRendered).slice(0, 22).padEnd(22), '| DM', d.dmAsked + '/' + d.dmRendered, '| Horas', d.horasAsked + '/' + d.horasRendered, '| serif', d.serif, '| err', d.errors.length, '| req', d.nonFileRequests.length, '| sw390', m.sw, '| sh', d.sh);
  if (d.errors.length) console.log('     errors:', d.errors.slice(0, 3));
  if (d.nonFileRequests.length) console.log('     reqs:', d.nonFileRequests.slice(0, 3));
}
fs.writeFileSync(`${outdir}/_verify-log.json`, JSON.stringify(results, null, 1)); await br.close();
