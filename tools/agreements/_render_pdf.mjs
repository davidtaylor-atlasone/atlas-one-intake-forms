// Renders one local HTML file to one PDF file with headless Chromium.
// Used by generate.py instead of LibreOffice headless conversion, which on
// this machine silently substitutes fonts (see the note at the top of
// generate.py). Usage: node _render_pdf.mjs <in.html> <out.pdf>
import { chromium } from "file:///Users/davidtaylor/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs";
import { pathToFileURL } from "node:url";

const [, , inHtml, outPdf] = process.argv;
if (!inHtml || !outPdf) {
  console.error("usage: node _render_pdf.mjs <in.html> <out.pdf>");
  process.exit(1);
}

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto(pathToFileURL(inHtml).href, { waitUntil: "networkidle" });
await page.emulateMedia({ media: "print" });
await page.pdf({
  path: outPdf,
  format: "Letter",
  printBackground: true,
  margin: { top: "0in", bottom: "0in", left: "0in", right: "0in" },
});
await browser.close();
