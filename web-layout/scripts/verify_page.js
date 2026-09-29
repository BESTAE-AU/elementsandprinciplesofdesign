#!/usr/bin/env node
/* Render a house web page and check the grid.
   Usage: node verify_page.js PAGE.html [--fonts DIR]
   Needs Playwright (npm i playwright). --fonts serves Lato from a local folder holding
   Google's lato.css and its woff2 files, for sandboxes where the browser can't reach Google Fonts.
   For each width (and each preset at 1440) it reports: container, margin, module, gutter,
   items off a row line (must be 0) and sideways page scroll (must be false). */
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const file = path.resolve(process.argv[2]);
const fi = process.argv.indexOf('--fonts'), fonts = fi > 0 ? path.resolve(process.argv[fi + 1]) : null;
(async () => {
  const b = await chromium.launch(fs.existsSync('/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    ? { executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' } : {});
  let failed = false;
  for (const w of [1440, 1100, 800, 390, 360]) {
    for (const preset of (w === 1440 ? ['a', 'b', 'c', 'd'] : ['a'])) {
      const p = await b.newPage({ viewport: { width: w, height: 900 } });
      if (fonts) {
        await p.route('https://fonts.googleapis.com/**', r => r.fulfill({ contentType: 'text/css', body: fs.readFileSync(path.join(fonts, 'lato.css'), 'utf8') }));
        await p.route('https://fonts.gstatic.com/**', r => r.fulfill({ contentType: 'font/woff2', body: fs.readFileSync(path.join(fonts, r.request().url().split('/').pop())) }));
      }
      await p.goto('file://' + file);
      await p.evaluate(pr => { document.body.classList.remove('hw-a', 'hw-b', 'hw-c', 'hw-d'); document.body.classList.add('hw-' + pr);
        window.dispatchEvent(new Event('resize')); }, preset);
      await p.waitForTimeout(500);
      const r = await p.evaluate(() => {
        const out = [];
        document.querySelectorAll('.hw-container').forEach(box => {
          const grid = box.querySelector('.hw-grid'); if (!grid) return;
          const cs = getComputedStyle(box), gs = getComputedStyle(grid);
          const mod = parseFloat(gs.gridTemplateColumns), gap = parseFloat(gs.columnGap), top = grid.getBoundingClientRect().top;
          const off = [...grid.children].filter(el => { const v = (el.getBoundingClientRect().top - top) / (mod + gap); return Math.abs(v - Math.round(v)) > 0.01; }).length;
          out.push({ container: box.getBoundingClientRect().width, margin: parseFloat(cs.paddingLeft), module: mod, gutter: gap, offRow: off });
        });
        return { grids: out, hscroll: document.documentElement.scrollWidth > innerWidth };
      });
      const bad = r.hscroll || r.grids.some(g => g.offRow);
      failed = failed || bad;
      console.log(`${bad ? 'FAIL' : 'ok  '} ${w} ${preset.toUpperCase()} ${JSON.stringify(r)}`);
      await p.close();
    }
  }
  await b.close();
  process.exit(failed ? 1 : 0);
})();
