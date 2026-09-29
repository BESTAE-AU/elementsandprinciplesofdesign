# House tokens (shared)

Shared across indesign-parameters, greyscale-print-design-system, canvas-pages and web-layout.
This file must be identical in every skill.

> Rebuilt from the handoff summary, because the canonical file wasn't available when web-layout was
> written. Replace sections 1–4 with the canonical text, and copy section 5 (Web) into the
> canonical file in every skill.

## 1. Principles

1. Whole numbers only: whole mm in print, multiples of 5 px on screen. If a value would be
   fractional, change the margins or gutter, never the module.
2. The grid is built from the margins inwards: `count × module + (count − 1) × gutter = live area`.
3. 12 columns. Everything aligns to whole columns; no half columns.
4. Vertical rhythm = row + gutter (the pitch). Half rows only where `(row − gutter) ÷ 2` is whole.
5. Type locks to the rhythm (rows in print and slides; the 5 px baseline and row snapping on the web).
6. Type values are whole or 1 decimal.
7. Accessibility: 7:1 for all text (house standard), 4.5:1 floor for large or secondary text,
   3:1 for meaningful graphics. Never colour alone.
8. Decisions are asked as pop-up multiple-choice questions, recommended option first.

## 2. Type

- Lato. Cap-height ratios (verified from the font files): Thin 0.700, Light 0.7075,
  Regular 0.7165, Bold 0.723, Black 0.7285.
- Headings are ALL CAPS in the heaviest weight (Lato Black). Subheadings are Lato Light caps.

## 3. Greyscale

K 0–100 in 10% steps: #FFFFFF, #E6E6E6, #CCCCCC, #B3B3B3, #999999, #808080, #666666, #4D4D4D,
#333333, #1A1A1A, #000000.

- **Text colour:** black on K 0–20, white on K 70–100, no text on K 30–60.
- **Secondary text:** K 80.
- **Fills:** shading runs from K 90 to K 10. K 100 is for small accents only.
- **White text:** at least 12 pt Regular or 10 pt Bold in print (16 px on the web), never Light.

## 4. Learning domains (H accent / S shade / T tint)

| Domain | H | S | T |
|---|---|---|---|
| Critical Thinking | #FF585D | #551C25 | #F5DADF |
| Creative Thinking | #F19C49 | #4F2C1D | #FFDFB4 |
| Communication | #F3EA5D | #CFB500 | #F7F4A2 |
| Self-Management | #C5E86C | #1C4220 | #EFF4A4 |
| Responsibility | #00B2A2 | #024638 | #D7EFE7 |
| Practical Skills | #326295 | #041E42 | #D5EBEE |
| Knowledge | #514689 | #201547 | #DCD3E7 |
| Independent Learning | #E56DB1 | #621244 | #F2DEE9 |

- **T tints:** black text. **S shades:** white text, except Mustard #CFB500, which takes black.
- **H accents on white** are decoration only (see web-layout `references/colour.md` for ratios).
- **Web neutrals:** #222222 and #333333 for text; #555555 for secondary text, on white only.

## 5. Web

- **Units:** 5 px steps, written in rem (1rem = 16 px). Media queries are in em.
- **Grid:** 12 columns at every size, with a stepped container that is centred and snaps to the largest step that fits.
- **Gutters:** 10 / 20 / 30 / 40 only (presets A–D, as on the slides).
- **Rows:** 1:1 ratio modules (row = module). Gutters are equal both ways.

| Container | Pitch | A | B | C | D |
|---|---|---|---|---|---|
| 1200 | 90 | 80 / 10 / M 65 | 70 / 20 / M 70 | 60 / 30 / M 75 | 50 / 40 / M 80 |
| 1020 | 80 | 70 / 10 / M 35 | 60 / 20 / M 40 | 50 / 30 / M 45 | 40 / 40 / M 50 |
| 760 | 60 | 50 / 10 / M 25 | 40 / 20 / M 30 | 30 / 30 / M 35 | = C |
| 360 | 25 | 15 / 10 / M 35 | = A | = A | = A |

Each cell is module / gutter / margin in px.

- **Body:** 18 / 25 px. Small 16 / 25, Condensed 18 / 20. Never under 16 px.
- **Headings:** cap height in 5 px steps, size = cap ÷ cap ratio, leading = 1.5 × cap rounded up to 5.

| Level | 1200 / 1020 | 760 | 360 |
|---|---|---|---|
| Title | 82.4 / 90 | 68.6 / 75 | 41.2 / 45 |
| H1 | 54.9 / 60 | 41.2 / 45 | 34.3 / 40 |
| H2 | 41.2 / 45 | 34.3 / 40 | 27.5 / 30 |
| H3 | 27.5 / 30 | 27.5 / 30 | 20.6 / 25 |
| H4 | 20.6 / 25 | 20.6 / 25 | 20.6 / 25 |
| H5 | 18 / 25 caps label | same | same |

- **Platform widths:**
  - Shopify: page width 1200 with house margins.
  - WordPress: `contentSize` 760, `wideSize` 1200.
  - Canvas: fluid, max 1200, 10 px gutters, 760 heading scale.
