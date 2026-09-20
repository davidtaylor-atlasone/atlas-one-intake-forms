import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import path from 'path';

const VS = process.argv[2];
const FIX = path.join(path.dirname(new URL(import.meta.url).pathname), 'fixtures', 'vendors');

async function run() {
  const browser = await chromium.launch();
  const results = {};

  async function loadFresh() {
    const page = await browser.newPage({ viewport: { width: 1200, height: 900 } });
    const errors = [];
    page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
    page.on('pageerror', err => errors.push(String(err)));
    await page.goto('file://' + VS);
    return { page, errors };
  }

  // (a) three bank checking files
  {
    const { page, errors } = await loadFresh();
    await page.setInputFiles('#file', [
      path.join(FIX, 'a-bank-checking-2026-06.csv'),
      path.join(FIX, 'a-bank-checking-2026-07.csv'),
      path.join(FIX, 'a-bank-checking-2026-08.csv'),
    ]);
    await page.waitForTimeout(400);
    const data = await page.evaluate(() => ({ rows: STATE.rows.map(r => ({ name: r.name, monthly: r.monthly, count: r.count })), raw: STATE.raw, sources: STATE.sourcesCount }));
    results['a-bank-3-files'] = { data, errors };
    await page.close();
  }

  // (b) card files with middle month duplicated across two files
  {
    const { page, errors } = await loadFresh();
    await page.setInputFiles('#file', [
      path.join(FIX, 'b-card-2026-06.csv'),
      path.join(FIX, 'b-card-2026-07-fileA.csv'),
      path.join(FIX, 'b-card-2026-07-fileB.csv'),
      path.join(FIX, 'b-card-2026-08.csv'),
    ]);
    await page.waitForTimeout(400);
    const data = await page.evaluate(() => ({ rows: STATE.rows.map(r => ({ name: r.name, monthly: r.monthly, count: r.count })), raw: STATE.raw, dupesRemoved: STATE.dupesRemoved, note: document.getElementById('parseNote').textContent }));
    results['b-card-dedupe'] = { data, errors };
    await page.close();
  }

  // (c) QuickBooks vendor summary xlsx
  {
    const { page, errors } = await loadFresh();
    await page.setInputFiles('#file', path.join(FIX, 'c-quickbooks-vendor-summary.xlsx'));
    await page.waitForTimeout(400);
    const periodWrapHidden = await page.evaluate(() => document.getElementById('periodMonthsWrap').hidden);
    const data = await page.evaluate(() => ({ rows: STATE.rows.map(r => ({ name: r.name, monthly: r.monthly })), summaryFiles: STATE.summaryFiles }));
    results['c-quickbooks-summary-xlsx'] = { data, periodWrapHidden, errors };
    await page.close();
  }

  // (d) Ramp csv and xlsx
  for (const name of ['d-ramp-transactions.csv', 'd-ramp-transactions.xlsx']) {
    const { page, errors } = await loadFresh();
    await page.setInputFiles('#file', path.join(FIX, name));
    await page.waitForTimeout(400);
    const data = await page.evaluate(() => ({ rows: STATE.rows.map(r => ({ name: r.name, monthly: r.monthly, count: r.count })) }));
    results[name] = { data, errors };
    await page.close();
  }

  // round trip: (a) + (b) together, Send to Audit payload, then feed into the Workbench
  {
    const { page, errors } = await loadFresh();
    await page.setInputFiles('#file', [
      path.join(FIX, 'a-bank-checking-2026-06.csv'),
      path.join(FIX, 'a-bank-checking-2026-07.csv'),
      path.join(FIX, 'a-bank-checking-2026-08.csv'),
      path.join(FIX, 'b-card-2026-06.csv'),
      path.join(FIX, 'b-card-2026-07-fileA.csv'),
      path.join(FIX, 'b-card-2026-07-fileB.csv'),
      path.join(FIX, 'b-card-2026-08.csv'),
    ]);
    await page.waitForTimeout(400);
    const payload = await page.evaluate(() => buildAuditVendorsPayload());
    results['roundtrip-payload'] = { payload, errors };
    await page.close();
  }

  await browser.close();
  console.log(JSON.stringify(results, null, 2));
}
run();
