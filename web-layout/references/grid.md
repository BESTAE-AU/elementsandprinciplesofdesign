# Web grid

## Rules

1. **Whole 5 px steps.** Every module, gutter and margin is a multiple of 5 px. CSS outputs rem
   (1rem = 16 px, so 5 px = 0.3125rem), which lets the grid scale when a user changes browser
   text size. Media queries are in em for the same reason.
2. **Built from the margins inwards:** `2 × margin + 12 × module + 11 × gutter = container`.
   If a value would be fractional, change the margin, never the module.
3. **12 columns at every size.** Spans are always whole columns. There are no half columns.
4. **Gutters are 10, 20, 30 or 40 px.** With equal margins, an odd multiple of 5 (15, 25, 35)
   always leaves half a pixel, because 11 × 15 = 165 is odd. These are the same gutters as slide
   presets A–D, so the web presets use the same letters.
5. **Stepped container, not fluid.** 768 and 1024 have no whole grid (neither is a multiple of 10).
   The container snaps to the largest step that fits (360 / 760 / 1020 / 1200) and is centred,
   so the grid is whole at every screen size. Below 360 px the page scrolls sideways rather
   than break the grid.
6. **Ratio rows.** Rows are 1:1 modules (row = module), so the vertical pitch equals the
   horizontal pitch. Gutters are equal both ways.
7. **Same pitch across presets.** At each container, A to D share one pitch. Each step adds 10 to
   the gutter, takes 10 off the module and adds 5 to each margin (as on the slides).

## Presets

| Container | Pitch | A | B | C | D |
|---|---|---|---|---|---|
| 1200 | 90 | 65 + 12 × 80 + 11 × 10 + 65 | 70 + 12 × 70 + 11 × 20 + 70 | 75 + 12 × 60 + 11 × 30 + 75 | 80 + 12 × 50 + 11 × 40 + 80 |
| 1020 | 80 | 35 + 12 × 70 + 11 × 10 + 35 | 40 + 12 × 60 + 11 × 20 + 40 | 45 + 12 × 50 + 11 × 30 + 45 | 50 + 12 × 40 + 11 × 40 + 50 |
| 760 | 60 | 25 + 12 × 50 + 11 × 10 + 25 | 30 + 12 × 40 + 11 × 20 + 30 | 35 + 12 × 30 + 11 × 30 + 35 | capped to C |
| 360 | 25 | 35 + 12 × 15 + 11 × 10 + 35 | = A | = A | = A |

- **D is capped to C at 760.** It would give 20 px modules with 40 px gutters, so the gutters would be wider than the columns.
- **Every preset collapses to A at 360.** Only two whole options exist on mobile:
  - 15 / 10 / M 35: a live area of 290 px (80%), chosen.
  - 20 / 10 / M 5: margins too tight to use.

## Spans

- `.hw-span-N`: every size. Items default to the full 12 columns.
- `.hw-md-span-N`: 760 and up. `.hw-lg-span-N`: 1020 and up.
- On mobile nearly everything spans 12. Use `md` and `lg` to split into columns on larger screens.
- Useful splits (always whole columns): 6 + 6, 4 + 4 + 4, 3 × 4, 4 + 8, 3 + 9, 8 + 4.

## Row snapping

- **Grid items have no margins.** The gutter does the spacing.
- **Fixed-height blocks** (media, panels) use `.hw-rows-N`, which spans N rows:
  height = N × row + (N − 1) × gutter.
- **Text blocks grow with their content.** `assets/snap.js` pads each grid item so it ends on a
  row line, and the next item starts on the next one. Verified at 1440 / 1100 / 800 / 390 / 360
  px for all four presets: every item starts on a row line.
- **Canvas can't run scripts.** There, headings sit in normal flow on the 5 px baseline, and
  row snapping is not guaranteed.

## Ratio blocks

- Media use `.hw-ratio-1-1`, `-4-3`, `-3-4`, `-3-2` or `-16-9` on whole-column spans.
- Their height isn't a whole row, so snapping pads the block to the next row line.
- **For exact rows, use `.hw-rows-N` instead.** Page grid rows only come out whole for other
  ratios when the module allows it. For example, 4:3 needs a module that is a multiple of 20
  (80 × 60 works for A at 1200, but 70 wouldn't).

## Solving a new width

```
python3 scripts/grid.py 1440 --gutter 10,20,30,40 --margin-min 20 --margin-max 120
python3 scripts/grid.py 1200 --ratio 4:3
```
