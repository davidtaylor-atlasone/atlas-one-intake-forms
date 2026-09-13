// Run AB: for each tool render three ways at 1440 px and compare.
//   A  before file, network blocked            (what the kit looked like offline: fallback face)
//   B  before file, Google css2 answered locally with the same brand TTFs (stand-in for online)
//   C  after file, network blocked             (what we ship)
// Records: rendered font (CDP CSS.getPlatformFontsForNode) on body and sample text nodes, computed
// font-family on body, scrollWidth/Height, a layout fingerprint (every element's rounded rect),
// JS errors, non-file requests. Expect C: DM Sans everywhere DM Sans is asked for, no serif, and
// C layout == B layout.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const [outdir, fontsDir, beforeDir, afterDir, ...names] = process.argv.slice(2); fs.mkdirSync(outdir, { recursive: true });
const b64 = f => fs.readFileSync(path.join(fontsDir, f)).toString('base64');
const localCss = [['400', 'DM_Sans/static/DMSans-Regular.ttf'], ['500', 'DM_Sans/static/DMSans-Medium.ttf'], ['700', 'DM_Sans/static/DMSans-Bold.ttf']]
  .map(([w, f]) => `@font-face{font-family:'DM Sans';src:url(data:font/ttf;base64,${b64(f)}) format('truetype');font-weight:${w};font-display:swap}`).join('\n');
const SAMPLE = 'body,h1,h2,h3,p,label,button,th,td,input,select,li,a,span,small,b,strong';
const br = await chromium.launch(); const results = [];
async function render(file, mode, shot) {
  const pg = await br.newPage({ viewport: { width: 1440, height: 900 } });
  const errs = []; pg.on('pageerror', e => errs.push(String(e.message).slice(0, 160)));
  const reqs = []; pg.on('request', r => { if (!r.url().startsWith('file://')) reqs.push(r.url().slice(0, 90)); });
  await pg.route('**/*', r => {
    const u = r.request().url();
    if (u.startsWith('file://')) return r.continue();
    if (mode === 'B' && u.startsWith('https://fonts.googleapis.com/css2')) return r.fulfill({ status: 200, contentType: 'text/css', body: localCss });
    return r.abort();
  });
  await pg.goto('file://' + file, { waitUntil: 'load', timeout: 90000 });
  await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(600);
  const cdp = await pg.context().newCDPSession(pg); await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
  const { root } = await cdp.send('DOM.getDocument', { depth: -1 });
  // sample up to 40 text-bearing elements that ask for DM Sans (or inherit it), plus body
  const handles = await pg.evaluate((SAMPLE) => {
    const out = []; const seen = new Set();
    for (const el of document.querySelectorAll(SAMPLE)) {
      if (out.length >= 40) break;
      const t = (el.childNodes[0] && el.childNodes[0].nodeType === 3 ? el.childNodes[0].textContent : '').trim();
      if (el !== document.body && !t) continue;
      const r = el.getBoundingClientRect(); if (el !== document.body && (r.width === 0 || r.height === 0)) continue;
      const ff = getComputedStyle(el).fontFamily; const key = el.tagName + '|' + ff; if (seen.has(key) && el !== document.body) continue; seen.add(key);
      el.setAttribute('data-a1probe', String(out.length)); out.push({ i: out.length, tag: el.tagName.toLowerCase(), family: ff.slice(0, 60), weight: getComputedStyle(el).fontWeight, text: t.slice(0, 30) });
    } return out; }, SAMPLE);
  for (const h of handles) {
    const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: `[data-a1probe="${h.i}"]` });
    const { fonts } = await cdp.send('CSS.getPlatformFontsForNode', { nodeId });
    h.rendered = fonts.map(f => `${f.familyName}${f.isCustomFont ? '' : ' (system)'}:${f.glyphCount}`).join(', ');
  }
  await pg.evaluate(() => document.querySelectorAll('[data-a1probe]').forEach(e => e.removeAttribute('data-a1probe')));
  const layout = await pg.evaluate(() => {
    const els = document.querySelectorAll('body *'); let s = '';
    for (const e of els) { const r = e.getBoundingClientRect(); s += `${e.tagName}:${Math.round(r.left * 2) / 2},${Math.round(r.top * 2) / 2},${Math.round(r.width * 2) / 2},${Math.round(r.height * 2) / 2};`; }
    return { count: els.length, fingerprint: s, sw: document.documentElement.scrollWidth, sh: document.documentElement.scrollHeight }; });
  const bodyFamily = await pg.evaluate(() => getComputedStyle(document.body).fontFamily);
  const first = f => f.replace(/^["']/, '').split(/["']?\s*,/)[0].trim();
  const body = handles.find(h => h.tag !== 'body' && first(h.family) === 'DM Sans' && h.rendered);   // first DM Sans text element: stands in for body
  const dmAsked = handles.filter(h => first(h.family) === 'DM Sans' && h.rendered);   // asks for DM Sans first and has glyphs
  const dmRendered = dmAsked.filter(h => /^DM Sans( Medium)?:/.test(h.rendered));
  const dmMissed = dmAsked.filter(h => !/^DM Sans( Medium)?:/.test(h.rendered)).map(h => `${h.tag}:${h.rendered}`);
  const serif = handles.filter(h => /Times|Georgia|serif\b/i.test(h.rendered) && !/DM Serif/i.test(h.family));
  await pg.screenshot({ path: shot, fullPage: false });
  const rec = { mode, bodyFamily: bodyFamily.slice(0, 60), bodyRendered: body ? body.rendered : null, dmAsked: dmAsked.length, dmRendered: dmRendered.length,
    dmMissed, serifRendered: serif.length, serifSamples: serif.slice(0, 3).map(h => `${h.tag}:${h.rendered}`), sw: layout.sw, sh: layout.sh, elements: layout.count, errors: errs, nonFileRequests: reqs, samples: handles };
  await pg.close(); return [rec, layout.fingerprint];
}
for (const name of names) {
  const base = name.replace(/\.html$/, '').replace(/[^A-Za-z0-9]+/g, '_').slice(0, 45);
  const [A, fA] = await render(path.join(beforeDir, name), 'A', `${outdir}/${base}_A_before_offline.png`);
  const [B, fB] = await render(path.join(beforeDir, name), 'B', `${outdir}/${base}_B_before_localfonts.png`);
  const [C, fC] = await render(path.join(afterDir, name), 'C', `${outdir}/${base}_C_after_offline.png`);
  const sameLayout = fB === fC;
  let diff = 0; if (!sameLayout) { const a = fB.split(';'), c = fC.split(';'); for (let i = 0; i < Math.max(a.length, c.length); i++) if (a[i] !== c[i]) diff++; }
  const rec = { file: name, A, B, C, layout_B_equals_C: sameLayout, layout_diff_elements: diff, A_body_rendered: A.bodyRendered, C_body_rendered: C.bodyRendered };
  results.push(rec);
  console.log(name.padEnd(48), 'C body:', C.bodyRendered, '| DM asked/rendered', C.dmAsked + '/' + C.dmRendered, '| serif', C.serifRendered, '| B==C layout', sameLayout, diff ? '(' + diff + ' rects differ)' : '', '| errs', C.errors.length, '| reqs', C.nonFileRequests.length, '| A body:', A.bodyRendered);
}
fs.writeFileSync(`${outdir}/_fontcheck-log.json`, JSON.stringify(results, null, 1)); await br.close();
