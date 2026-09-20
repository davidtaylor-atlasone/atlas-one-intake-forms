import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs';
import path from 'path';

const VS = process.argv[2];
const WB = process.argv[3];
const OUT = process.argv[4]; // harbor output dir
const SHOTS = process.argv[5];
const FIX_PAYROLL = process.argv[6]; // fixtures/payroll dir
const FIX_VENDORS = process.argv[7]; // fixtures/vendors dir

const PULSE_EXPORT = {
  pulse: {
    code: 'HDG2609', client: 'Harbor Dental Group', round: 'Audit', sent: 12, responses: 7, score: 3.7,
    weakest: ['q3', 'q4'],
    averages: { q1: 3.9, q2: 4.2, q3: 3.1, q4: 3.4, q8: 4.1, q5: 2.3, q6: 1.8, q7: 1.1 },
    picks: { 'One login for everything': 4, 'Benefits explained in plain words': 3 },
    free_text: ['Fewer forms to sign every month.', 'More heads up before deadlines.'],
  },
};

async function main() {
  const browser = await chromium.launch();
  const allErrors = [];

  // Step 0: build the vendors payload from the Job 2 fixtures (a + b)
  const vpage = await browser.newPage();
  vpage.on('console', m => { if (m.type() === 'error') allErrors.push('vendor:' + m.text()); });
  await vpage.goto('file://' + VS);
  await vpage.setInputFiles('#file', [
    path.join(FIX_VENDORS, 'a-bank-checking-2026-06.csv'),
    path.join(FIX_VENDORS, 'a-bank-checking-2026-07.csv'),
    path.join(FIX_VENDORS, 'a-bank-checking-2026-08.csv'),
    path.join(FIX_VENDORS, 'b-card-2026-06.csv'),
    path.join(FIX_VENDORS, 'b-card-2026-07-fileA.csv'),
    path.join(FIX_VENDORS, 'b-card-2026-07-fileB.csv'),
    path.join(FIX_VENDORS, 'b-card-2026-08.csv'),
  ]);
  await vpage.waitForTimeout(400);
  const vendorsPayload = await vpage.evaluate(() => { STATE.company = 'Harbor Dental Group'; return buildAuditVendorsPayload(); });
  await vpage.close();

  // Step 1: drive the Workbench
  const page = await browser.newPage({ viewport: { width: 1200, height: 950 } });
  page.on('console', m => { if (m.type() === 'error') allErrors.push('wb:' + m.text()); });
  page.on('pageerror', e => allErrors.push('wb-pageerror:' + String(e)));
  await page.goto('file://' + WB);

  async function shot(name) {
    await page.screenshot({ path: path.join(SHOTS, name + '-desktop.png'), fullPage: true });
  }

  // Stage 1: client name + vendors hand off
  await page.evaluate(() => showStage(1));
  await page.evaluate((payload) => {
    P.client = 'Harbor Dental Group (SAMPLE, fictional)';
    P.as_of = 'September 2026';
    ingestVendorsPayload(payload);
  }, vendorsPayload);
  await page.waitForTimeout(200);
  await shot('harbor-01-stage1-vendors');
  console.error('DEBUG after stage1:', await page.evaluate(() => JSON.stringify(P.lines)));

  // Stage 2: payroll, Job 1 fixture (a), PEO model, $25 rate, biweekly
  await page.evaluate(() => showStage(2));
  await page.selectOption('#s2freq', 'biweekly');
  await page.selectOption('#s2model', 'peo');
  await page.setInputFiles('#s2file', path.join(FIX_PAYROLL, 'a-modern-journal.xlsx'));
  await page.waitForTimeout(200);
  await page.fill('#s2rate', '25');
  await page.waitForTimeout(200);
  await shot('harbor-02-stage2-payroll');

  // Stage 3: WC dec page (two class codes) and benefits (two tiers, no Section 125)
  await page.evaluate(() => showStage(3));
  await page.click('#wcAddClass');
  await page.click('#wcAddClass');
  await page.waitForTimeout(100);
  async function setRowField(tbodySel, rowIdx, field, value) {
    // Each edit re-renders the table (fresh DOM nodes), so always select fresh by data-i, never cache a handle.
    await page.$eval(tbodySel + ' tr[data-i="' + rowIdx + '"] input[data-f="' + field + '"]', (el, v) => {
      el.value = v; el.dispatchEvent(new Event('input', { bubbles: true }));
    }, value);
  }
  // Row 0: dental office code
  await setRowField('#wcClassRows', 0, 'code', '8021');
  await setRowField('#wcClassRows', 0, 'payroll_estimate', '650000');
  await setRowField('#wcClassRows', 0, 'rate', '0.85');
  // Row 1: clerical code
  await setRowField('#wcClassRows', 1, 'code', '8810');
  await setRowField('#wcClassRows', 1, 'payroll_estimate', '120000');
  await setRowField('#wcClassRows', 1, 'rate', '0.20');
  await page.fill('#wcMod', '1.05');
  await page.fill('#wcExpConst', '200');
  await page.fill('#wcExp', '2027-01-01');
  await page.fill('#wcRerated', '4200');
  await page.waitForTimeout(200);
  // Benefits: two tiers, employer share 65%, no Section 125
  await page.click('#benAddTier');
  await page.click('#benAddTier');
  await page.waitForTimeout(100);
  await setRowField('#benTierRows', 0, 'tier', 'Employee Only');
  await setRowField('#benTierRows', 0, 'rate', '410');
  await setRowField('#benTierRows', 0, 'enrolled', '5');
  await setRowField('#benTierRows', 1, 'tier', 'Employee + Family');
  await setRowField('#benTierRows', 1, 'rate', '980');
  await setRowField('#benTierRows', 1, 'enrolled', '4');
  await page.fill('#benRenewal', '2027-01-01');
  await page.fill('#benEmployerPct', '65');
  await page.selectOption('#benSec125', 'no');
  await page.waitForTimeout(200);
  await shot('harbor-03-stage3-wc-benefits');
  console.error('DEBUG after stage3:', await page.evaluate(() => JSON.stringify(P.lines)));

  // Stage 4: paste the worked pulse export
  await page.evaluate(() => showStage(4));
  await page.evaluate((pulseExport) => { document.getElementById('pulsePasteJson').value = JSON.stringify(pulseExport); }, PULSE_EXPORT);
  await page.click('#pulseIngestJson');
  await page.waitForTimeout(200);
  await shot('harbor-04-stage4-pulse');

  // Stage 6: offer (rule based tier) first, so Stage 5's 2x test reads the real membership fee
  await page.evaluate(() => showStage(6));
  await page.evaluate(() => { P._feesFromBench = true; renderStage6(); renderStage5(); });
  await page.waitForTimeout(200);
  const offerState = await page.evaluate(() => ({ tier: P.audit.offer.tier, also_tier: P.audit.offer.also_tier, headcount: P.audit.headcount }));
  await shot('harbor-06-stage6-offer');

  // Stage 5: Total Impact and the three fixes (re-shown now that the fee is set)
  await page.evaluate(() => showStage(5));
  await page.waitForTimeout(200);
  const s5gate = await page.evaluate(() => document.getElementById('s5gate').textContent);
  await shot('harbor-05-stage5-total-impact');

  const prospect = await page.evaluate(() => ({ client: P.client, as_of: P.as_of, lines: P.lines, atlas_one_fees: P.atlas_one_fees, reconcile_against: P.reconcile_against, audit: P.audit }));
  fs.writeFileSync(path.join(OUT, 'Harbor_Dental_Group.json'), JSON.stringify(prospect, null, 2));

  await page.close();
  await browser.close();

  console.log(JSON.stringify({ s5gate, offerState, errors: allErrors }, null, 2));
}

main();
