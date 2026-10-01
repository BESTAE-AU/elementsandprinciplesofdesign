# Knowledge: House design system, web layout

Project knowledge for any Claude project that makes web pages, Canvas pages or screen layouts
(e.g. Multimedia, Graphics, Visual Design, Canvas course building). Summarises the
**web-layout** skill built on 29 Sep – 1 Oct 2026. Repo: `BESTAE-AU/elementsandprinciplesofdesign`,
folder `web-layout/`, installable file `web-layout.skill`.

## How Britt works

- Ask decisions as **pop-up multiple-choice questions**, recommended option first, only for what isn't settled.
- Show **drafts in chat for approval** before anything goes into a skill or template.
- Show the **whole-number maths** (e.g. `65 + 12 × 80 + 11 × 10 + 65 = 1200`) and flag trade-offs honestly.
- **Verify, don't assume:** render pages, measure, and check contrast before handing over.
- Explain jargon in plain words (e.g. "canonical" = the master copy).
- Australian English.

## Which skill for which medium

| Making… | Skill |
|---|---|
| InDesign print (A4/A3) or 1920 × 1080 slides | indesign-parameters |
| Word workbooklets and handouts | greyscale-print-design-system / workbooklet-style-system |
| Table-based Canvas pages | canvas-pages |
| Web pages, Canvas pages on the web grid, Shopify, WordPress, site builders | **web-layout** |

All four share `house-tokens.md`, which must be identical in every skill. The current master is in
`web-layout/references/house-tokens.md`. It is the InDesign copy plus the web additions;
copy it into the other three skills.

## Shared principles

1. **Whole numbers only:** whole mm in print, **5 px steps** on screen. Fix fractions by changing the margins, never the module.
2. **The grid is built from the margins inwards:** `2 × margin + 12 × module + 11 × gutter = width`.
3. **12 columns** at every size, whole-column spans only.
4. **Type locks to a rhythm:** rows in print and slides; a 5 px baseline plus row snapping on the web.
5. **Contrast:** 7:1 for all text, a 4.5:1 floor for large or secondary text, 3:1 for meaningful graphics. Never colour alone.

## Web grid (decided)

- **Units:** 5 px steps, written as rem (1rem = 16 px). Media queries use em, so zoom works.
- **Container:** stepped, not fluid. It snaps to the largest of **360 / 760 / 1020 / 1200** that fits, and is centred.
  - 768 and 1024 have no whole grid because they aren't multiples of 10.
- **Gutters:** only **10 / 20 / 30 / 40** (presets A–D, matching the slides). Odd 5s leave half pixels.
- **Rows:** **1:1 ratio modules** (row = module). Gutters are equal both ways.

| Container | Pitch | A | B | C | D |
|---|---|---|---|---|---|
| 1200 | 90 | 80 / 10 / M 65 | 70 / 20 / M 70 | 60 / 30 / M 75 | 50 / 40 / M 80 |
| 1020 | 80 | 70 / 10 / M 35 | 60 / 20 / M 40 | 50 / 30 / M 45 | 40 / 40 / M 50 |
| 760 | 60 | 50 / 10 / M 25 | 40 / 20 / M 30 | 30 / 30 / M 35 | capped to C |
| 360 | 25 | 15 / 10 / M 35 | = A | = A | = A |

Each cell is module / gutter / margin in px.

- **Preset A is the default.**
- **D is capped to C at 760,** because it would give gutters wider than the columns.
- **Mobile is 15 / 10 / M 35 for every preset:** a 290 px live area, 80% of a 360 px screen.

## Web typography (decided)

- **Font:** Lato.
  - Cap ratios, verified from the font files and the same in Adobe and Google: Light 0.7075,
    Regular 0.7165, Bold 0.723, Black 0.7285.
- **Body:** 18 / 25 px (139%). Small 16 / 25, Condensed 18 / 20, Lead 20 / 25 Light. Never under 16 px.
- **Headings:** ALL CAPS Lato Black. The cap height is a 5 px step.
  - Size = cap ÷ 0.7285, to 1 decimal.
  - Leading = 1.5 × cap, rounded up to 5.
  - The heading block snaps to row lines.
- **"Caps fill rows"** (the print method) was tested and rejected for the web. Web gutters are too large
  compared with the rows, so H3 and smaller came out at zero size.

| Level | 1200 / 1020 | 760 | 360 |
|---|---|---|---|
| Title | 82.4 / 90 | 68.6 / 75 | 41.2 / 45 |
| H1 | 54.9 / 60 | 41.2 / 45 | 34.3 / 40 |
| H2 | 41.2 / 45 | 34.3 / 40 | 27.5 / 30 |
| H3 | 27.5 / 30 | 27.5 / 30 | 20.6 / 25 |
| H4 | 20.6 / 25 | 20.6 / 25 | 20.6 / 25 |
| H5 | 18 / 25 caps label | same | same |

## Web colour (decided)

- **Mode:** light only. Greyscale K steps plus learning-domain H / S / T colours, using the house text rules.
- **Text colour:** #222222 by default, #333333 for secondary text. #555555 only on pure white (7.46:1); it fails on K 10 and K 20.
- **Fills:** no text on K 30–60. White text only on K 70–100, and never Light.
- **Tints and shades:**
  - T tints take black text.
  - S shades take white text, except Mustard #CFB500, which takes black.
- **H accent fills:** black text on Corn, Lime, Royal Orange, Seagreen and Valentine Pink; white on Twilight.
  Tomato (6.8:1 with black text) and Denim (6.3:1 with white) are large text and graphics only.
- **H accents drawn on white** (bars, borders): only Tomato 3.09, Denim 6.33 and Twilight 8.12 reach 3:1.
  The others are decoration beside text that names the domain; use the S shade for a meaningful bar.

## Platforms

- **Canvas:**
  - **Allowed styles:** inline styles only. Allowed: `display: grid`, `grid-template-columns`, `grid-column`, `gap`,
    `flex`, `max-width`, and the `font` shorthand.
  - **Stripped:** `<style>`, classes, media queries, **`font-weight`**, `text-transform`,
    `letter-spacing`, `aspect-ratio` and `var()`. `calc()` is untested.
  - **So:** type headings in CAPITALS and set weight with `font: 900 41.2px/45px 'Lato Extended', Lato, sans-serif`.
  - **Layout:** max-width 1200, 10 px gutter, the **760 heading scale everywhere**, and wrapping cards
    (`flex: 1 1 290px`) that stack on phones.
  - Canvas makes the page title the h1, so house H1 = `<h2>` in page content.
  - Check every page with `scripts/check_canvas.py`.
- **Shopify (Dawn theme):** page width 1200, house margins via `.hw-container`, and Dawn's padding removed.
  If Dawn's 80 px padding is kept, the only whole grid is 12 × 50 + 11 × 40 = 1040.
- **WordPress:** set `contentSize` to 760 and `wideSize` to 1200 in theme.json, with root padding 0.
- **Plain HTML:** `house-web.css` and `snap.js`, with `<body class="hw-page hw-a">`.
- **Google Sites, Squarespace, Wix, Adobe Express / Canva web:** starting notes only, untested.

## Files in the skill

- `scripts/grid.py`: solves the whole-number grids for any width.
- `scripts/tokens.py`: the approved presets. It generates `assets/house-web.css`; never edit the CSS by hand.
- `scripts/check_canvas.py`: checks Canvas HTML against Canvas's allowlist.
- `scripts/verify_page.js`: renders a page at 5 widths and fails if items are off the rows or the page scrolls sideways.
- `assets/house-web.css`, `snap.js`, `sample.html` (preset switcher and grid overlay), `canvas-snippets.html`.
- `examples/canvas-typography-lesson.html`: "Typography 1: The anatomy of type", a full Canvas lesson page.

## Still to check

- Whether Canvas's Lato Extended has a Black (900) weight; if not, headings render Bold.
- How grid and flex layouts look in the Canvas mobile app.
- The WordPress theme.json setup, and the notes for the site builders.
- Copying the updated `house-tokens.md` into indesign-parameters, greyscale-print-design-system and canvas-pages.
