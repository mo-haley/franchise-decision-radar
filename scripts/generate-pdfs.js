#!/usr/bin/env node
/**
 * generate-pdfs.js
 *
 * Converts HTML reports → PDFs using Playwright headless Chromium.
 * Uses @media print styles already present in the HTML.
 *
 * Usage:
 *   node scripts/generate-pdfs.js                  # all files in reports/
 *   node scripts/generate-pdfs.js file1.html ...   # specific filenames (basename only)
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const ROOT = path.resolve(__dirname, '..');
const INPUT_DIR = path.join(ROOT, 'reports');
const OUTPUT_DIR = path.join(ROOT, 'site', 'reports');

async function generatePDF(browser, htmlFile) {
  const inputPath = path.join(INPUT_DIR, htmlFile);
  const outputFile = htmlFile.replace(/\.html$/, '.pdf');
  const outputPath = path.join(OUTPUT_DIR, outputFile);

  const page = await browser.newPage();
  try {
    await page.goto(`file://${inputPath}`, { waitUntil: 'networkidle' });
    await page.pdf({
      path: outputPath,
      format: 'Letter',
      printBackground: true,
      margin: { top: '0', right: '0', bottom: '0', left: '0' },
    });
    const { size } = fs.statSync(outputPath);
    console.log(`  ✓  ${outputFile}  (${(size / 1024).toFixed(0)} KB)`);
    return { file: outputFile, ok: true, size };
  } catch (err) {
    console.error(`  ✗  ${outputFile}  ERROR: ${err.message}`);
    return { file: outputFile, ok: false };
  } finally {
    await page.close();
  }
}

async function main() {
  // Determine which HTML files to process
  let targets;
  if (process.argv.length > 2) {
    targets = process.argv.slice(2).map(f => path.basename(f));
  } else {
    targets = fs.readdirSync(INPUT_DIR).filter(f => f.endsWith('.html')).sort();
  }

  if (targets.length === 0) {
    console.error('No HTML files found.');
    process.exit(1);
  }

  // Validate inputs
  const missing = targets.filter(f => !fs.existsSync(path.join(INPUT_DIR, f)));
  if (missing.length) {
    console.error(`Missing input files:\n  ${missing.join('\n  ')}`);
    process.exit(1);
  }

  fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  console.log(`Generating ${targets.length} PDF(s) → ${OUTPUT_DIR}\n`);

  const browser = await chromium.launch();
  const results = [];
  for (const f of targets) {
    results.push(await generatePDF(browser, f));
  }
  await browser.close();

  const failed = results.filter(r => !r.ok);
  console.log(`\n${results.length - failed.length}/${results.length} PDFs generated successfully.`);
  if (failed.length) {
    console.error(`Failed:\n  ${failed.map(r => r.file).join('\n  ')}`);
    process.exit(1);
  }
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
