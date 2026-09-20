import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import path from 'path';

const WB = process.argv[2];
const FIX = path.join(path.dirname(new URL(import.meta.url).pathname), 'fixtures', 'payroll');

async function run() {
  const browser = await chromium.launch();
  const results = {};

  async function loadFresh() {
    const page = await browser.newPage({ viewport: { width: 1200, height: 900 } });
    const errors = [];
    page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
    page.on('pageerror', err => errors.push(String(err)));
    await page.goto('file://' + WB);
    await page.evaluate(() => showStage(2));
    return { page, errors };
  }

  async function readStage2(page) {
    return await page.evaluate(() => ({
      headcount: P.audit.headcount,
      gross_annual: P.audit.payroll.gross_annual,
      employer_taxes_annual: P.audit.payroll.employer_taxes_annual,
      provider_fee_annual: P.audit.payroll.provider_fee_annual,
      provider_fee_per_check: P.audit.payroll.provider_fee_per_check,
      by_department: P.audit.payroll.by_department,
      payroll_admin: P.lines.payroll_admin,
      note: document.getElementById('s2note').textContent,
    }));
  }

  for (const name of ['a-modern-journal.csv', 'a-modern-journal.xlsx', 'b-legacy-register.csv', 'b-legacy-register.xlsx', 'c-peo-invoice.csv', 'c-peo-invoice.xlsx', 'd-suite-summary-transposed.csv', 'd-suite-summary-transposed.xlsx']) {
    const { page, errors } = await loadFresh();
    await page.setInputFiles('#s2file', path.join(FIX, name));
    await page.waitForTimeout(300);
    let data;
    try { data = await readStage2(page); } catch (e) { data = { error: String(e) }; }
    results[name] = { data, errors };
    await page.close();
  }

  // (e) pasted PEO invoice text
  {
    const { page, errors } = await loadFresh();
    const fs = await import('fs');
    const txt = fs.readFileSync(path.join(FIX, 'e-peo-invoice-pasted.txt'), 'utf8');
    await page.fill('#s2paste', txt);
    await page.click('#s2parsePaste');
    await page.waitForTimeout(300);
    let data;
    try { data = await readStage2(page); } catch (e) { data = { error: String(e) }; }
    results['e-peo-invoice-pasted.txt'] = { data, errors };
    await page.close();
  }

  // DecompressionStream stubbed test
  {
    const page = await browser.newPage();
    const errors = [];
    page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
    await page.addInitScript(() => { delete window.DecompressionStream; });
    await page.goto('file://' + WB);
    await page.evaluate(() => showStage(2));
    let alertText = null;
    page.on('dialog', async d => { alertText = d.message(); await d.accept(); });
    await page.setInputFiles('#s2file', path.join(FIX, 'a-modern-journal.xlsx'));
    await page.waitForTimeout(300);
    results['decompressionstream-stubbed'] = { alertText, errors };
    await page.close();
  }

  await browser.close();
  console.log(JSON.stringify(results, null, 2));
}
run();
