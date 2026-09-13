// Run AB: open the Portal from file:// with the network blocked, click two of the fixed tools, and read the
// rendered font of text inside the tool iframe through CDP (DOM.getDocument pierce:true reaches the frame).
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs';
const [outdir, portal, ...pairs] = process.argv.slice(2);
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1440, height: 900 } });
const errs = []; pg.on('pageerror', e => errs.push(String(e.message).slice(0, 160)));
const reqs = []; pg.on('request', r => { if (!r.url().startsWith('file://')) reqs.push(r.url().slice(0, 90)); });
await pg.route('**/*', r => r.request().url().startsWith('file://') ? r.continue() : r.abort());
await pg.goto('file://' + portal, { waitUntil: 'load', timeout: 120000 }); await pg.waitForTimeout(800);
const out = { title: await pg.title(), stamp: await pg.evaluate(() => document.querySelector('.buildchip').textContent), tools: [] };
const cdp = await pg.context().newCDPSession(pg); await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
for (const pair of pairs) {
  const [label, id] = pair.split('=');
  await pg.evaluate(() => { const t = document.querySelector('.tab[data-cat=""]'); if (t) t.click(); }); await pg.waitForTimeout(300);
  await pg.locator(`#cards .card[data-tool="${id}"]`).click(); await pg.waitForTimeout(1500);
  const frame = pg.frames().find(f => f !== pg.mainFrame());
  await frame.evaluate(() => document.fonts.ready);
  const probes = await frame.evaluate(() => {
    const out = []; const seen = new Set();
    for (const el of document.querySelectorAll('h1,h2,p,label,th,td,button,b,strong,span,small')) {
      const t = (el.childNodes[0] && el.childNodes[0].nodeType === 3 ? el.childNodes[0].textContent : '').trim(); if (!t) continue;
      const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
      const ff = getComputedStyle(el).fontFamily; const key = el.tagName + '|' + ff; if (seen.has(key)) continue; seen.add(key);
      el.setAttribute('data-a1probe', String(out.length)); out.push({ i: out.length, tag: el.tagName.toLowerCase(), family: ff.slice(0, 50), weight: getComputedStyle(el).fontWeight, text: t.slice(0, 28) });
      if (out.length >= 14) break;
    } return { title: document.title, bodyFamily: getComputedStyle(document.body).fontFamily.slice(0, 50), probes: out, dmLoaded: document.fonts.check('16px "DM Sans"') }; });
  const { root } = await cdp.send('DOM.getDocument', { depth: -1, pierce: true });
  for (const h of probes.probes) {
    const { nodeIds } = await cdp.send('DOM.querySelectorAll', { nodeId: root.nodeId, selector: `[data-a1probe="${h.i}"]` });
    // with pierce the selector runs in the top document only; walk into the iframe's content document
    let nodeId = nodeIds[0];
    if (!nodeId) { const { nodeId: fid } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '#frame' }); const { node } = await cdp.send('DOM.describeNode', { nodeId: fid, depth: 0, pierce: true });
      const docId = (await cdp.send('DOM.requestNode', { objectId: (await cdp.send('DOM.resolveNode', { backendNodeId: node.contentDocument.backendNodeId })).object.objectId })).nodeId;
      nodeId = (await cdp.send('DOM.querySelector', { nodeId: docId, selector: `[data-a1probe="${h.i}"]` })).nodeId; }
    const { fonts } = await cdp.send('CSS.getPlatformFontsForNode', { nodeId });
    h.rendered = fonts.map(f => `${f.familyName}${f.isCustomFont ? '' : ' (system)'}:${f.glyphCount}`).join(', ');
  }
  await frame.evaluate(() => document.querySelectorAll('[data-a1probe]').forEach(e => e.removeAttribute('data-a1probe')));
  await pg.screenshot({ path: `${outdir}/Portal_${label}_1440.png`, fullPage: false });
  const dm = probes.probes.filter(p => /^"?DM Sans/.test(p.family)); const dmOk = dm.filter(p => /^DM Sans( Medium| 9pt| 9pt SemiBold)?:/.test(p.rendered));
  const serif = probes.probes.filter(p => /Times|Georgia/.test(p.rendered));
  out.tools.push({ label, id, innerTitle: probes.title, bodyFamily: probes.bodyFamily, dmLoaded: probes.dmLoaded, dmAsked: dm.length, dmRendered: dmOk.length, serifRendered: serif.length, probes: probes.probes });
  console.log(label, '|', probes.title, '| body:', probes.bodyFamily, '| fonts.check DM Sans:', probes.dmLoaded, '| DM asked/rendered', dm.length + '/' + dmOk.length, '| serif', serif.length);
  for (const p of probes.probes) console.log('   ', p.tag.padEnd(6), p.weight.padEnd(4), p.family.slice(0, 26).padEnd(27), '->', p.rendered, '|', p.text);
}
out.errors = errs; out.nonFileRequests = reqs; console.log('errors', errs, 'non-file requests', reqs);
fs.writeFileSync(`${outdir}/_portal-fontcheck-log.json`, JSON.stringify(out, null, 1)); await b.close();
