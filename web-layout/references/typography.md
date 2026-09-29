# Web typography

## Font

- **Lato** is the house font. General sites load it from Google Fonts (weights 300, 400, 700, 900
  and Light Italic); Canvas uses its own Lato Extended.
- **Cap-height ratios** are read from the Google Fonts files with fontTools and match the InDesign
  measurements exactly: Light 0.7075, Regular 0.7165, Bold 0.723, **Black 0.7285**.
- **Any font can be swapped in.** Read its OS/2 `sCapHeight ÷ unitsPerEm` per weight, update
  `CAP_RATIO` in `scripts/tokens.py`, then regenerate the CSS.

## Rhythm

- Everything sits on a **5 px baseline**. Every leading and every space is a multiple of 5 px.
- **Paragraphs** are spaced by one line (25 px).
- **Grid items** are spaced by one gutter, then snapped to the next row line.

## Headings

- ALL CAPS Lato Black. The cap height is a 5 px step.
- Size = cap ÷ 0.7285, rounded to 1 decimal px.
- Leading = 1.5 × cap, rounded up to a 5 px step.
- Headings are trimmed to cap height and baseline (`text-box: trim-both cap alphabetic`), so the
  caps start exactly on a row line. The block is then padded to end on a row line.
- **Sizes step down per container** (drawn from 5 px cap steps, never below body size):

| Level | 1200 / 1020 | 760 | 360 |
|---|---|---|---|
| Title | cap 60 → 82.4 / 90 | cap 50 → 68.6 / 75 | cap 30 → 41.2 / 45 |
| H1 | cap 40 → 54.9 / 60 | cap 30 → 41.2 / 45 | cap 25 → 34.3 / 40 |
| H2 | cap 30 → 41.2 / 45 | cap 25 → 34.3 / 40 | cap 20 → 27.5 / 30 |
| H3 | cap 20 → 27.5 / 30 | cap 20 → 27.5 / 30 | cap 15 → 20.6 / 25 |
| H4 | cap 15 → 20.6 / 25 | cap 15 → 20.6 / 25 | cap 15 → 20.6 / 25 |
| H5 | 18 / 25 Black caps label, +0.1em tracking | same | same |

- **Subheading:** Lato Light caps at the H2 size.
- **Browser support:** Firefox didn't support `text-box` when this was written. There, headings
  keep their half-leading above the caps; the row snap still holds, but the caps sit a few px
  lower.

### Why not "caps fill rows" as in print

- **The gutter is too big relative to the row.** Print rows are about 7× the gutter (20 mm / 3 mm);
  web rows can be as little as 1× (760 C is 30 / 30). With the gutter as the gap between heading
  lines, H3 onwards comes out at zero or negative size on most presets.
- **So on the web, cap heights come in 5 px steps and the heading block snaps to rows instead.**

## Body and supporting styles

| Style | Size / leading (px) | Weight |
|---|---|---|
| Body | 18 / 25 (139%) | Regular |
| Small | 16 / 25 | Regular |
| Condensed (tables) | 18 / 20 | Regular |
| Lead | 20 / 25 | Light (Regular on dark fills) |
| Caption | 16 / 25, #333333 | Regular |
| Label | 16 / 25 caps, +0.1em | Bold |

- **Never under 16 px.**
- **White text** is never Light.

## Canvas

- Canvas has no media queries, so it uses the 760 heading scale at every screen size.
- Canvas strips `text-transform` and `font-weight`. So:
  - type headings in capitals
  - set weight through the `font` shorthand: `font: 900 41.2px/45px 'Lato Extended', Lato, sans-serif`
- Canvas uses `<h1>` for the page title, so house H1 becomes `<h2>` in page content.
