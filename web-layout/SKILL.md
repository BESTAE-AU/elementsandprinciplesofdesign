---
name: web-layout
description: House rules for laying out web pages on a whole-number 12-column grid, for general websites, Canvas LMS pages, Shopify, WordPress, Google Sites, Squarespace, Wix and Adobe Express/Canva web pages. Stepped containers (360 / 760 / 1020 / 1200 px) with presets A–D where every module, gutter and margin is a 5 px step and rows are 1:1 ratio modules; Lato type on a 5 px baseline (body 18 / 25) with ALL CAPS Lato Black headings sized from cap height in 5 px steps; greyscale K and learning-domain colour at 7:1 contrast. Ships a grid solver, generated CSS tokens and utilities, Canvas inline-style snippets with a sanitiser checker, and a sample page with a grid overlay. Use this skill whenever the user is building, planning, checking or fixing a web page, Canvas page, website section, landing page or HTML layout, asks what widths/columns/gutters/margins/breakpoints to use on screen, how big web headings or body text should be, or wants CSS, HTML or Canvas code that follows the house design system, even if they don't say "grid" or "skill". Companion to indesign-parameters (print and slides), greyscale-print-design-system (Word) and canvas-pages; all share references/house-tokens.md.
---

# Web layout

The web part of the house design system. The rules are the same as print and slides:
whole numbers, a grid built from the margins inwards, 12 columns, type locked to a rhythm,
and 7:1 contrast. `references/house-tokens.md` is shared across all four skills and must stay
identical.

## Workflow

1. **Ask before building** with pop-up multiple-choice questions (AskUserQuestion), recommended
   option first, only for what the request hasn't settled:
   platform (see `references/platforms.md`), preset (A default), and page content.
2. **Show the maths** for any grid you use: `margin + 12 × module + 11 × gutter + margin = container`.
   Run `scripts/tokens.py table` for the approved presets, or `scripts/grid.py WIDTH` to solve
   a new width. Never hand-calculate.
3. **Build** from `assets/house-web.css` (general sites) or `assets/canvas-snippets.html` (Canvas).
   Never edit the CSS by hand: change `scripts/tokens.py` and regenerate
   (`python3 scripts/tokens.py css > assets/house-web.css`).
4. **Verify** before handing over:
   - Canvas HTML: `python3 scripts/check_canvas.py FILE.html` must report 0 problems.
   - General sites: `node scripts/verify_page.js page.html` must pass at every width, then look at
     the page with the grid overlay (`.hw-show-grid`) and check that text contrast is at least 7:1
     (`references/colour.md`).

## Core numbers (full detail in references)

| Container | Pitch | A | B | C | D |
|---|---|---|---|---|---|
| 1200 | 90 | 80 / 10 / M 65 | 70 / 20 / M 70 | 60 / 30 / M 75 | 50 / 40 / M 80 |
| 1020 | 80 | 70 / 10 / M 35 | 60 / 20 / M 40 | 50 / 30 / M 45 | 40 / 40 / M 50 |
| 760 | 60 | 50 / 10 / M 25 | 40 / 20 / M 30 | 30 / 30 / M 35 | = C |
| 360 | 25 | 15 / 10 / M 35 | = A | = A | = A |

Each cell is module / gutter / margin in px. Rows are 1:1, so row = module.
The container snaps to the largest step that fits the screen and is centred.

- **Type:** body 18 / 25 Lato Regular. Headings are ALL CAPS Lato Black, with the cap height a 5 px step.
  See `references/typography.md`.
- **Colour:** greyscale K steps plus learning-domain H / S / T colours. See `references/colour.md`.

## References

- `references/grid.md`: grid rules, why gutters must be 10 / 20 / 30 / 40, ratio rows, row snapping.
- `references/typography.md`: type scale per container, heading method, text styles.
- `references/colour.md`: web colour rules and verified contrast ratios.
- `references/platforms.md`: Canvas, Shopify, WordPress, plain HTML and site builders.
- `references/house-tokens.md`: shared tokens across all four skills (includes the Web section).

## Scripts and assets

- `scripts/grid.py`: solves every whole-number 12-column grid for a width (`--ratio`, `--gutter`, margins).
- `scripts/tokens.py`: approved presets, checked with the grid equation. `table` prints them; `css` writes the CSS.
- `scripts/check_canvas.py`: checks inline styles against the Canvas sanitiser allowlist.
- `scripts/verify_page.js`: renders a page at 1440 / 1100 / 800 / 390 / 360 (all presets at 1440) and fails if any
  grid item is off a row line or the page scrolls sideways. Needs Playwright.
- `assets/house-web.css`: tokens and utilities (`.hw-page`, `.hw-container`, `.hw-grid`, `.hw-span-N`,
  `.hw-md-span-N`, `.hw-lg-span-N`, `.hw-rows-N`, `.hw-ratio-*`, type, panels, tables, overlay).
- `assets/snap.js`: pads each grid item so it ends on a row line (general sites only; Canvas can't run it).
- `assets/canvas-snippets.html`: Canvas-safe wrapper, headings, wrapping cards, 12-column grid, panels, table.
- `assets/sample.html`: demo page with preset switcher and grid overlay.
- `examples/canvas-typography-lesson.html`: a full Canvas lesson page (Typography 1: type anatomy) built from the snippets.
