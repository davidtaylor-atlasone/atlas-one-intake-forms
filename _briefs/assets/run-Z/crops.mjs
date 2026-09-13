// Run Z: crop the regions the mobile pass restructured, at 390 px, after the sample fill.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
const [outdir, file, ...sels] = process.argv.slice(2); const b = await chromium.launch();
const pg = await b.newPage({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
await pg.route('**/*', r => r.request().url().startsWith('file://') ? r.continue() : r.abort());
await pg.goto('file://' + file); await pg.waitForTimeout(500);
if (process.env.FILL) await pg.evaluate(() => { let i = 0; document.querySelectorAll('input[type=text],input:not([type]),textarea').forEach(el => { i++; if (!el.value) { el.value = 'Sample ' + i; el.dispatchEvent(new Event('input', { bubbles: true })); } }); });
await pg.waitForTimeout(300);
const base = file.split('/').pop().replace(/\.html$/, '').replace(/[^A-Za-z0-9]+/g, '_').slice(0, 40);
for (const s of sels) { const el = await pg.$(s); if (!el) { console.log('no', s); continue; } const bb = await el.boundingBox(); const clip = { x: 0, y: Math.max(0, bb.y - 40), width: 390, height: Math.min(1400, bb.height + 80) }; const name = `${outdir}/${base}__${s.replace(/[^A-Za-z0-9]+/g, '_')}.png`; await pg.screenshot({ path: name, fullPage: true, clip }); console.log(name, Math.round(bb.height)); }
await b.close();
