// Run W: one deterministic sample run per tool. Fills every input, fires the calculate/generate buttons,
// captures the visible text and every number on the page, so before/after can be compared.
// usage: node sample.mjs <out.json> file...
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs';
const [out, ...files] = process.argv.slice(2);
const b = await chromium.launch(); const res = {};
for (const f of files) {
  const pg = await b.newPage({ viewport: { width: 1440, height: 900 } });
  const errs = []; pg.on('pageerror', e => errs.push(String(e.message).slice(0, 200)));
  pg.on('dialog', d => d.dismiss().catch(()=>{}));
  await pg.route('**/*', r => r.request().url().startsWith('file://') ? r.continue() : r.abort());
  await pg.addInitScript(() => { window.print = () => {}; window.open = () => null; window.alert = () => {}; window.confirm = () => true; window.prompt = () => null;
    const _fetch = window.fetch; window.fetch = () => Promise.reject(new Error('blocked')); });
  try { await pg.goto('file://' + f, { waitUntil: 'load', timeout: 60000 }); } catch (e) { errs.push('goto: ' + e.message); }
  await pg.waitForTimeout(600);
  const loadErrors = errs.slice();
  const fill = async () => pg.evaluate(() => {
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
        else { const ph = (el.placeholder || ''); el.value = /\$|\d/.test(ph) && /^[\d\$.,%\s\-–]+$/.test(ph) ? String(10 + (i % 7) * 5) : 'Sample ' + i; }
        fire(el); n++;
      } catch (e) {}
    });
    return n;
  });
  const clickCalc = async () => pg.evaluate(() => {
    const bad = /print|download|save|send|email|submit|copy|reset|clear|delete|remove|open|load|import|upload|pdf|csv|json|logo|mail|start over|duplicate|new |add |camera|scan|share|book|call|export/i;
    const good = /calc|generat|build|preview|update|compute|estimat|run|apply|see |show|results|score|analy|compare|check my|get my|reveal/i;
    let c = 0;
    document.querySelectorAll('button, a.btn, [role=button], input[type=button]').forEach(bt => {
      const t = (bt.textContent || bt.value || '').trim(); if (!t || bad.test(t) || !good.test(t)) return;
      try { bt.click(); c++; } catch (e) {}
    });
    return c;
  });
  const capture = () => pg.evaluate(() => {
    const txt = document.body.innerText;
    const vals = [...document.querySelectorAll('input, textarea, select')].filter(e => e.type !== 'hidden').map(e => e.value).join('\n');
    return { text: txt, values: vals };
  });
  const filled = await fill(); await pg.waitForTimeout(300);
  const clicked = await clickCalc(); await pg.waitForTimeout(600);
  const shots = {};
  // multi-tool pages: walk every tool through select(k) (Business Tools)
  const multi = await pg.evaluate("(typeof TOOLS!=='undefined' && typeof select==='function') ? Object.keys(TOOLS).filter(k=>TOOLS[k]&&typeof TOOLS[k].init==='function') : null");
  if (multi) {
    for (const k of multi) {
      await pg.evaluate('select(' + JSON.stringify(k) + ')'); await pg.waitForTimeout(150);
      await fill(); await pg.waitForTimeout(250);
      shots[k] = await capture();
    }
  } else {
    shots.main = await capture();
  }
  const numbers = {}; for (const [k, v] of Object.entries(shots)) numbers[k] = (v.text + '\n' + v.values).match(/[\$]?\d(?:[\d,]*\d)?(?:\.\d+)?%?/g) || [];
  res[f.split('/').pop()] = { filled, clicked, loadErrors, errors: errs, shots, numbers };
  console.log(f.split('/').pop().slice(0, 60).padEnd(60), 'inputs', filled, 'clicked', clicked, 'loadErrors', loadErrors.length, 'errors', errs.length, 'tools', Object.keys(shots).length, errs.slice(0, 2).join(' | '));
  await pg.close();
}
await b.close();
fs.writeFileSync(out, JSON.stringify(res));
