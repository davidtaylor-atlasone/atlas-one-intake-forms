import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
const [file, outdir] = process.argv.slice(2);
const br = await chromium.launch(); const pg = await br.newPage({ viewport: { width: 1440, height: 1000 } });
const errs = []; pg.on('pageerror', e => errs.push(e.message));
await pg.goto('file://' + file);
const S = [
  ['Solo S corp owner', { entity: 'smllc', ee: '0', who: 'owner', cov: 'indiv', goal: 'owner' }],
  ['Solo C corp owner', { entity: 'ccorp', ee: '0', who: 'owner' }],
  ['12 EE construction wants it all', { entity: 'scorp', ee: '12', who: 'both', cov: 'grp_shock', goal: 'all' }, ['UT', 'ID']],
  ['30 EE renewal shock cap cost', { entity: 'scorp', ee: '30', cov: 'grp_shock', goal: 'cap', budget: '350' }],
  ['Happy with plan', { entity: 'scorp', ee: '40', cov: 'grp_happy' }],
  ['Healthy 25 EE wants cheaper', { entity: 'scorp', ee: '25', cov: 'grp_shock', goal: 'cheap', health: 'clean' }],
  ['80 EE large group', { entity: 'ccorp', ee: '80', cov: 'grp_shock', goal: 'rich' }, ['UT', 'AZ', 'NV']],
  ['One employee', { entity: 'scorp', ee: '1', who: 'both', cov: 'none' }],
  ['600 lives', { entity: 'multi', ee: '600', cov: 'grp_shock', goal: 'rich' }],
];
for (const [name, vals, states] of S) {
  await pg.click('#btnClear');
  for (const [k, v] of Object.entries(vals)) { const tag = await pg.$eval('#' + k, e => e.tagName); if (tag === 'SELECT') await pg.selectOption('#' + k, v); else await pg.fill('#' + k, v); }
  for (const s of states || []) await pg.click(`.chip[data-st="${s}"]`);
  await pg.waitForTimeout(100);
  const r = await pg.evaluate(() => ({ route: document.getElementById('rName').textContent, ask: document.getElementById('rAsk').textContent, alts: [...document.querySelectorAll('.rt.alt .nm')].map(x => x.textContent), flags: document.querySelectorAll('.flag').length }));
  console.log(name.padEnd(36), '->', r.route, '| alts:', r.alts.join('; '), '| flags', r.flags);
  await pg.screenshot({ path: `${outdir}/routing_${name.replace(/[^A-Za-z0-9]+/g, '_')}.png`, fullPage: true });
}
console.log('errors', errs); await br.close();
