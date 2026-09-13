// Run AA: render the NDA Builder at 390 and 1440 px, confirm the logo upload control sits inside .panel.form
// and the "Book a call" banner link is visible (in viewport, not covered). Also viewport-only shots of the top.
import { chromium } from '/Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs';
import fs from 'fs';
const [outdir, file, label] = process.argv.slice(2); fs.mkdirSync(outdir, { recursive: true });
const b = await chromium.launch(); const log = [];
for (const w of [390, 1440]) {
  const pg = await b.newPage({ viewport: { width: w, height: w === 390 ? 844 : 900 }, isMobile: w === 390, hasTouch: w === 390 });
  const errs = []; pg.on('pageerror', e => errs.push(String(e.message).slice(0, 160)));
  await pg.route('**/*', r => r.request().url().startsWith('file://') ? r.continue() : r.abort());
  await pg.goto('file://' + file, { waitUntil: 'load', timeout: 60000 }); await pg.waitForTimeout(600);
  const r = await pg.evaluate(() => {
    const ctl = document.querySelector('.a1-logo-ctl');
    const form = document.querySelector('.panel.form');
    const book = [...document.querySelectorAll('#atlas-cta-banner a')].find(a => /book a call/i.test(a.textContent));
    const rect = el => { const x = el.getBoundingClientRect(); return { top: Math.round(x.top), left: Math.round(x.left), w: Math.round(x.width), h: Math.round(x.height) }; };
    const cs = ctl ? getComputedStyle(ctl) : null;
    // what element is on top at the centre of the Book a call button?
    let topEl = null; if (book) { const bx = book.getBoundingClientRect(); const e = document.elementFromPoint(bx.left + bx.width / 2, bx.top + bx.height / 2); topEl = e ? (e === book || book.contains(e) ? 'book-a-call' : (e.tagName + (e.id ? '#' + e.id : '') + (e.className ? '.' + String(e.className).replace(/\s+/g, '.') : ''))) : null; }
    return {
      scrollWidth: document.documentElement.scrollWidth,
      ctlExists: !!ctl, ctlInsideForm: !!(ctl && form && form.contains(ctl)), ctlPosition: cs ? cs.position : null, ctlRect: ctl ? rect(ctl) : null,
      ctlPrevSibling: ctl && ctl.previousElementSibling ? ctl.previousElementSibling.tagName + ' "' + ctl.previousElementSibling.textContent.trim().slice(0, 40) + '"' : null,
      formRect: form ? rect(form) : null,
      bookExists: !!book, bookRect: book ? rect(book) : null, bookVisible: !!(book && book.offsetParent !== null), bookTopElement: topEl,
    };
  });
  await pg.screenshot({ path: `${outdir}/NDA_Builder_${label}_${w}_top.png`, fullPage: false });
  await pg.screenshot({ path: `${outdir}/NDA_Builder_${label}_${w}.png`, fullPage: true });
  log.push({ w, ...r, errors: errs }); console.log(w, JSON.stringify({ ...r, errors: errs }));
  await pg.close();
}
await b.close(); fs.writeFileSync(`${outdir}/_nda-${label}-log.json`, JSON.stringify(log, null, 1));
