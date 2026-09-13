// Run Z item 7: one deterministic sample run per tool at 390 px and at 1440 px. Fills every field from a fixed
// pattern (Run W's fill), fires the calculate / generate / preview buttons (never print, save, send, download),
// then captures what the tool produced: every field value, the generated document's innerHTML (#out, #document,
// #doc, .document), body.textContent (CSS-independent) and getState() where the tool has one.
// usage: node sample.mjs <out.json> file...
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs';
const [out, ...files] = process.argv.slice(2);
const b = await chromium.launch(); const res = {};
for (const f of files) {
  for (const w of [390, 1440]) {
    const pg = await b.newPage({ viewport: { width: w, height: w === 390 ? 844 : 900 }, isMobile: w === 390, hasTouch: w === 390 });
    const errs = []; pg.on('pageerror', e => errs.push(String(e.message).slice(0, 200)));
    pg.on('dialog', d => d.dismiss().catch(()=>{}));
    await pg.route('**/*', r => r.request().url().startsWith('file://') ? r.continue() : r.abort());
    await pg.addInitScript(() => { window.print = () => {}; window.open = () => null; window.alert = () => {}; window.confirm = () => true; window.prompt = () => null;
      window.fetch = () => Promise.reject(new Error('blocked')); const D = Date; const fixed = new D(2026, 8, 12, 12, 0, 0); // fixed clock so date stamps match between runs
      window.Date = class extends D { constructor(...a) { super(...(a.length ? a : [fixed.getTime()])); } static now() { return fixed.getTime(); } }; });
    try { await pg.goto('file://' + f, { waitUntil: 'load', timeout: 60000 }); } catch (e) { errs.push('goto: ' + e.message); }
    await pg.waitForTimeout(600);
    const loadErrors = errs.slice();
    const filled = await pg.evaluate(() => {
      const fire = (el) => { el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); el.dispatchEvent(new Event('keyup', { bubbles: true })); };
      let i = 0, n = 0; const seen = new Set();
      document.querySelectorAll('input, select, textarea').forEach(el => {
        if (el.type === 'hidden' || el.type === 'file' || el.type === 'button' || el.type === 'submit' || el.disabled || el.readOnly) return;
        i++;
        try {
          if (el.tagName === 'SELECT') { if (el.options.length > 1) el.selectedIndex = (i % (el.options.length - 1)) + 1; }
          else if (el.type === 'checkbox') el.checked = (i % 2 === 0);
          else if (el.type === 'radio') { const g = el.name || el.closest('label,div')?.id || ''; if (!seen.has(g)) { el.checked = true; seen.add(g); } }
          else if (el.type === 'number' || el.type === 'range') { const mn = el.min !== '' ? +el.min : null, mx = el.max !== '' ? +el.max : null; let v = 7 + (i % 9) * 3; if (mn !== null && mx !== null) v = mn + Math.round((mx - mn) * 0.37); else if (mn !== null && v < mn) v = mn + 3; else if (mx !== null && v > mx) v = mx - 1; if (el.step && el.step !== 'any' && +el.step >= 1) v = Math.round(v); el.value = String(v); }
          else if (el.type === 'date') el.value = '2026-03-15';
          else if (el.type === 'time') el.value = '09:30';
          else if (el.type === 'email') el.value = 'sample' + i + '@example.com';
          else if (el.type === 'tel') el.value = '8015550100';
          else if (el.tagName === 'TEXTAREA') el.value = 'Sample text ' + i + '\nSecond line ' + i;
          else { const ph = (el.placeholder || ''); el.value = /\$|\d/.test(ph) && /^[\d\$.,%\s\-–…]+$/.test(ph) ? String(10 + (i % 7) * 5) : 'Sample ' + i; }
          fire(el); n++;
        } catch (e) {}
      });
      return n;
    });
    await pg.waitForTimeout(300);
    const clicked = await pg.evaluate(() => {
      const bad = /print|download|save|send|email|submit|copy|reset|clear|delete|remove|open|load|import|upload|pdf|csv|json|logo|mail|start over|duplicate|new |add |camera|scan|share|book|call|export|have atlas/i;
      const good = /calc|generat|build|preview|update|compute|estimat|run|apply|see |show|results|score|analy|compare|check my|get my|reveal/i;
      let c = 0;
      document.querySelectorAll('button, a.btn, [role=button], input[type=button]').forEach(bt => {
        const t = (bt.textContent || bt.value || '').trim(); if (!t || bad.test(t) || !good.test(t)) return;
        try { bt.click(); c++; } catch (e) {}
      });
      return c;
    });
    await pg.waitForTimeout(800);
    const cap = await pg.evaluate(() => {
      const values = [...document.querySelectorAll('input, textarea, select')].filter(e => e.type !== 'hidden').map(e => e.type === 'checkbox' || e.type === 'radio' ? (e.checked ? '1' : '0') : e.value).join('\n');
      const docs = {}; ['#out', '#document', '#doc', '.document', '#preview'].forEach(s => { const el = document.querySelector(s); if (el) docs[s] = el.innerHTML; });
      let state = null; try { if (typeof getState === 'function') state = JSON.stringify(getState()); } catch (e) { state = 'ERR ' + e.message; }
      return { values, docs, bodyText: document.body.textContent, state, scrollWidth: document.documentElement.scrollWidth };
    });
    const key = f.split('/').pop() + ' @' + w;
    res[key] = { filled, clicked, loadErrors, errors: errs, ...cap };
    console.log(key.slice(0, 70).padEnd(70), 'inputs', filled, 'clicked', clicked, 'errs', errs.length, 'docs', Object.keys(cap.docs).join(',') || '-', 'doc bytes', Object.values(cap.docs).reduce((a, s) => a + s.length, 0), 'state', cap.state ? cap.state.length : '-', 'sw', cap.scrollWidth, errs.slice(0, 1).join(''));
    await pg.close();
  }
}
await b.close();
fs.writeFileSync(out, JSON.stringify(res));
