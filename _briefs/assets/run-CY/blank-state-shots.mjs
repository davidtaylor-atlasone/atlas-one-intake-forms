// Run CY: screenshot each builder's required state picker while blank (the required warning shows).
import { createRequire } from 'module'; import path from 'path'; import fs from 'fs';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PW_PATH || 'playwright');
const [TOOLS, OUT] = process.argv.slice(2);
fs.mkdirSync(path.join(OUT, 'shots'), { recursive: true });
const b = await chromium.launch();
for (const [id, file] of [['IC', 'Independent Contractor Agreement Builder (Atlas One).html'], ['W2', 'W-2 At-Will Employment Agreement Builder (Atlas One).html'], ['NDA', 'NDA Builder (Atlas One).html']]) {
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
  const p = await ctx.newPage();
  await p.goto('file://' + path.join(TOOLS, file));
  await p.waitForTimeout(600);
  const sel = p.locator('#govState');
  await sel.scrollIntoViewIfNeeded();
  await p.screenshot({ path: path.join(OUT, 'shots', `${id}-state-required-blank.png`) });
  const hint = await p.evaluate(() => (document.getElementById('govHint') || {}).textContent);
  console.log(id, 'hint:', hint);
  await ctx.close();
}
await b.close();
