---
name: indesign-parameters
description: House rules for laying out A4/A3 print documents (portrait and landscape) and 1920 × 1080 slides in Adobe InDesign: single-sheet vs booklet margins, four 12-column × 12-row grid presets (A–D) with every value a whole mm (print) or 5 px step (digital), row and half-row alignment, text-frame widths and settings (Cap Height first baseline, auto-size height from top, zero inset), a 78-style object style library, all-caps headings body styles (print 12/10 pt, slides 18/16 px) that lock to rows, in any font (default Lato), and greyscale K colour with contrast checks. Use this skill whenever the user is creating, setting up, planning, checking or fixing an A4 or A3 layout or a slide layout, worksheet, handout, booklet, poster or document in InDesign, asks what margins/columns/gutters/grid to use, how wide a text box should be, or wants a layout spec, template or ExtendScript for A4 or A3 — even if they don't say "grid" or "skill".
---

# InDesign Parameters

These are a designer's house rules for A4 and A3 print layouts (portrait and landscape) and 1920 × 1080 presentation slides. The whole system rests on one idea: **every measurement is a whole millimetre**. Margins, column widths, row heights, gutters and text-frame sizes all land on clean numbers so objects snap precisely, frames can be typed in exactly, and nothing drifts by fractions of a millimetre across pages. When you apply or adapt these rules, protect that property — if a change would produce a fractional column or row, say so and offer a whole-mm alternative instead.

All units are millimetres. Set InDesign's units to mm (Preferences › Units & Increments) before anything else.

## Related skills and shared tokens

This skill is one of three that share the house design system. **`references/house-tokens.md`** holds what they share: the grid, Lato, contrast rules, the K greyscale, and the learning-domain colours. The file is identical in each skill.

| Medium | Skill |
|---|---|
| InDesign print and slides | **this skill** |
| Word documents from the Greyscale Workbooklet template | **greyscale-print-design-system** |
| Canvas LMS pages | **canvas-pages** |

If a request is for Word or Canvas, use that skill for the build, with the same tokens. If a request spans media (e.g. an InDesign worksheet and a matching Canvas page), use each skill for its part. Exact type sizes, spacing and alignment are medium-specific: InDesign locks them to the grid and left-aligns headings, while the Word template has its own scale and centred headings. When editing `house-tokens.md`, copy the change into the other two skills.

## Grid principles (apply to every grid)

1. **Every module is a whole number of millimetres** (print) **or pixels** (digital). A module is one column × one row cell. Its width, its height, and both gutters must all be whole mm (or whole px). Never accept 12.17 mm, 20.33 mm and so on, even though InDesign will happily calculate them.
2. **The grid is built from the margins inwards.** Columns and rows fill the live area (the space inside the margins) exactly. The first column starts on the left/inside margin, the last one ends on the right/outside margin, and the same applies to rows between the top and bottom margins. No leftover space and no grid lines outside the margins.

These two rules together mean margins, module and gutter depend on each other:

```
live width  = page width  − left margin − right margin   = columns × module width  + (columns − 1) × gutter
live height = page height − top margin  − bottom margin  = rows    × module height + (rows − 1)    × gutter
```

### Working out a grid (any page size or grid count)

1. Start from the ideal margin: **10 mm on every side** for single sheets. Booklets are the exception: they need at least **12 mm inside** (binding) and **8 mm outside**.
2. Work out the live width/height, then try the preferred gutter: `module = (live − (count − 1) × gutter) ÷ count`.
3. If the module is a whole number, done.
4. If not, **adjust the margins**, not the module, by the smallest amount that makes the module whole. Keep margins as close to 10 mm as possible (never under 8 mm on a single sheet) and split any change evenly between both sides. With 12 columns, the margin total is tied to the gutter, so sometimes the only way to get margins near 10 mm is a different gutter. On large sheets like A3, a wider gutter is fine and often looks better.
5. If no small margin change works, try the next gutter value and repeat.
6. Before finalising, check: `count × module + (count − 1) × gutter + both margins = page size`. Show this check whenever you give a grid.

## 1. Choose the page size and document type

| Size | Code | Page (W × H) | Reference file |
|---|---|---|---|
| A4 portrait | A4P | 210 × 297 | `references/A4P.md` |
| A4 landscape | A4L | 297 × 210 | `references/A4L.md` |
| A3 portrait | A3P | 297 × 420 | `references/A3P.md` |
| A3 landscape | A3L | 420 × 297 | `references/A3L.md` |

| Type | When | Facing pages | Side margins |
|---|---|---|---|
| **Single sheet** | Loose pages, handouts, posters, anything not bound | Off | Left / Right |
| **Booklet** | Stapled, saddle-stitched, wire or coil bound, so it needs extra room at the spine | On | Inside / Outside (inside always the larger) |

If the user doesn't say which type, ask or infer it: more than 2 pages that will be bound means booklet, otherwise single sheet.

**Margins:** the ideal is **10 mm on every side** for single sheets. Every preset gets as close to 10 mm as whole-mm modules allow (8–14 mm). Booklets are the exception: the inside margin is at least 12 mm for binding and the outside at least 8 mm. In most presets the booklet just moves space from the outside to the inside, so the column grid is identical for both types. Where a sheet's margins are too small to do that (some A3 presets), the booklet uses a column **1 mm narrower** to make room. The *Booklet col* column in the table shows this.

## 2. Choose a grid preset (12 columns × 12 rows)

12 columns is used because it divides evenly into 1, 2, 3, 4, 6 and 12 equal layout columns, so one grid supports every combination through a document (2 across on one page, 3 across on the next, a 4-across strip below). Every size has the same four presets, from tight (A) to open (D). A4 presets use the gutters listed below. A3 presets use wider gutters in places (up to 8 mm), because that's what keeps A3 margins near 10 mm, and a larger sheet carries wider gutters comfortably.

**Which preset to use:**
- **A: Standard.** On A4, 2 mm column gutter and 3 mm row gutter. Tight, with the most content per page. Worksheets, handouts, dense booklets. Use this when the user doesn't specify.
- **B: Even 3.** On A4, 3 mm gutters both ways, so spacing between boxes and images is identical in both directions. Close to A in feel.
- **C: Medium.** On A4, 4 mm gutters both ways (7 mm on A3), more breathing room. General documents, reports, newsletters.
- **D: Open.** On A4, 6 mm gutters both ways (8 mm on A3), airy and spacious. Posters, covers, feature pages, anything with lots of images.

### All presets at a glance (mm)

| Size | Preset | Column / gutter | Row / gutter | Sheet L / R | Top / bottom | Booklet in / out | Booklet col |
|---|---|---|---|---|---|---|---|
| A4P | A | 14 / 2 | 20 / 3 | 10 / 10 | 12 / 12 | 12 / 8 | 14 |
| A4P | B | 13 / 3 | 20 / 3 | 10 / 11 | 12 / 12 | 12 / 9 | 13 |
| A4P | C | 12 / 4 | 19 / 4 | 11 / 11 | 12 / 13 | 13 / 9 | 12 |
| A4P | D | 10 / 6 | 17 / 6 | 12 / 12 | 13 / 14 | 14 / 10 | 10 |
| A4L | A | 21 / 2 | 13 / 3 | 11 / 12 | 10 / 11 | 13 / 10 | 21 |
| A4L | B | 20 / 3 | 13 / 3 | 12 / 12 | 10 / 11 | 14 / 10 | 20 |
| A4L | C | 19 / 4 | 12 / 4 | 12 / 13 | 11 / 11 | 14 / 11 | 19 |
| A4L | D | 17 / 6 | 10 / 6 | 13 / 14 | 12 / 12 | 15 / 12 | 17 |
| A3P | A | 21 / 2 | 30 / 4 | 11 / 12 | 8 / 8 | 13 / 10 | 21 |
| A3P | B | 20 / 3 | 28 / 6 | 12 / 12 | 9 / 9 | 14 / 10 | 20 |
| A3P | C | 17 / 7 | 27 / 7 | 8 / 8 | 9 / 10 | 16 / 12 | **16** |
| A3P | D | 16 / 8 | 26 / 8 | 8 / 9 | 10 / 10 | 17 / 12 | **15** |
| A3L | A | 30 / 4 | 21 / 2 | 8 / 8 | 11 / 12 | 16 / 12 | **29** |
| A3L | B | 28 / 6 | 20 / 3 | 9 / 9 | 12 / 12 | 17 / 13 | **27** |
| A3L | C | 27 / 7 | 17 / 7 | 9 / 10 | 8 / 8 | 18 / 13 | **26** |
| A3L | D | 26 / 8 | 16 / 8 | 10 / 10 | 8 / 9 | 12 / 8 | 26 |

Where a margin pair is uneven, the extra 1 mm deliberately goes to the **bottom** (a slightly heavier bottom margin looks more balanced), the **right** on single sheets, or the **inside** on booklets (more room for binding). Keep it that way round; don't swap it.

Why A4's 297 mm side sits at 11–14 mm rather than 10: with 12 modules and A4 gutters of 2–6 mm, whole-mm modules on a 297 mm side only work out with margins totalling 23–27 mm. Getting to 10 mm there would need an 11 mm gutter. Landscape A4 rows are short (10–13 mm), which is expected: use multi-row spans for anything taller than a line or two.

Use one preset per document so every page shares the same grid. If the user wants something outside these (a different size, gutter or column count), build a new grid with the method in *Grid principles* and check it with the script.

## 3. Span sizes

A frame spanning *n* columns is `n × column + (n − 1) × gutter` wide: the columns plus the gutters *between* them, never the outer gutters. Rows work the same way.

For full tables of widths and heights for every span, plus the common page divisions (2, 3, 4 and 6 across), read the reference file for the page size, e.g. `references/A4P.md`. Look sizes up rather than recalculating by hand.

`scripts/grid.py` holds the presets and does the maths:

```
python3 scripts/grid.py                           # list every size and preset
python3 scripts/grid.py A4P C                     # full spec and span tables for one preset
python3 scripts/grid.py A3L D --cols 8 --rows 3   # exact size of a frame spanning 8 cols × 3 rows
python3 scripts/grid.py A3P C --cols 6 --booklet  # booklet width, where the booklet column differs
```

The span tables in the reference files are for single sheets. For a booklet whose column is marked **bold** (narrower) in the table above, recalculate widths with the booklet column, or use `--booklet`.

The script also checks every preset adds up to its page size, so if presets are ever edited, run it to confirm nothing has broken, then regenerate the reference files with `python3 scripts/grid.py --markdown A4P > references/A4P.md` (and so on for each size).

A single-column span (12 across) is available but not recommended for text on A4, because it's too narrow to read. Asymmetric splits are encouraged where they suit the content (e.g. 8 + 4, or 9 + 3), as long as the spans add up to 12 grid columns.

## 4. Setting the grid up in InDesign

1. **File › New › Document**: enter the page width and height from section 1 and set the orientation. Facing Pages on for booklets, off for single sheets.
2. **Margins and Columns** (in the New Document dialog, or Layout › Margins and Columns): enter the preset's margins. Untick the chain link so the margins can differ. Columns: **12**, Column Gutter: the preset's column gutter.
3. Rows go on the parent page: **Layout › Create Guides** → Rows: **12**, Gutter: the preset's row gutter, Columns: 0, **Fit Guides to: Margins**. Do this on the parent (A-Parent) so every page inherits it.
4. Check a module: draw a Rectangle Frame snapped to one column and one row. W and H should read exactly the preset's column width and row height (e.g. 14 × 20 for A4P A). A decimal in either field means the margins or gutter are wrong. Fix them instead of accepting the fraction.

### Building a document automatically

`scripts/build_indd.py` generates an InDesign script from the calculator's numbers and, on macOS with InDesign installed, runs it directly. It builds:
- the page, margins, 12 columns and 12 row guides on the parent page
- the K swatches (in a Greyscale group)
- every paragraph, character, object (78 position styles and Panels), cell and table style
- the Answer Lines object style
- the parent-page footer and page number

With `--sample`, it also lays out a two-page example (a handout and a worksheet). It saves the .indd, exports a PDF and PNG previews, and writes a build log. The log includes the font's real cap ratios measured inside InDesign.

```
python3 scripts/build_indd.py A4P A --out ~/Desktop/My-Template.indd --run            # template only
python3 scripts/build_indd.py A4P A --out ~/Desktop/Sample.indd --sample --run         # with sample pages
```

Without `--run` it just writes the .jsx, which can be run from InDesign's Scripts panel. Always read the build log afterwards and view the PNGs before handing the file over. If a measured cap ratio differs from `fonts.json`, update the font entry and rebuild.

Scripting pitfalls, already handled in the builder:
- Write the .jsx as UTF-8 **with a BOM**, or names containing – and · are garbled.
- Object styles made by script **don't inherit Based On settings**. Set the text-frame options on every style.
- **Never set a frame's stroke weight to 0.** On an unstroked frame, that turns on a 1 pt black stroke. Set the stroke colour to None instead.
- The property names are `numberingLists`, `sameParaStyleSpacing` and `TransformPositionReference.PAGE_MARGIN_REFERENCE`.

Margins and Columns always divides the space between the margins, so columns are built from the margins automatically. For rows, **Fit Guides to: Margins** is essential. If it's left on *Page*, the rows are measured from the paper edge and won't line up with the margins.

## Digital layouts (pixels)

The same principles apply on screen, with **pixels** in place of millimetres: every column, row, gutter and margin is a whole pixel, and the grid is built from the margins inwards. On screen there's no binding, so there are no booklet margins. Pixels give far more freedom than mm, so digital presets also keep **margins equal on all four sides** and **gutters equal across and down**.

Two extra rules for digital:
- **Ideal margin is about 100 px** on a 1920 × 1080 slide. Presets use 95–110 px.
- **Every value is a multiple of 5 px** (columns, rows, gutters and margins), so numbers are quick to type and remember and spans stay on round numbers. When building a new digital grid, search only multiples of 5. Doubling to 4K (3840 × 2160) keeps everything whole.

### Presentations: 1920 × 1080 (16:9), code PRES

| Preset | Column / gutter | Row / gutter | Margins (all sides) | Live area |
|---|---|---|---|---|
| A: Standard | 135 / 10 | 65 / 10 | 95 | 1730 × 890 |
| B | 125 / 20 | 55 / 20 | 100 | 1720 × 880 |
| C: Medium | 115 / 30 | 45 / 30 | 105 | 1710 × 870 |
| D: Open | 105 / 40 | 35 / 40 | 110 | 1700 × 860 |

A is tight with the most room for content, D is the most open. (On screen, B is simply the step between A and C. The "Even 3" name only describes its print gutters.) Rows are short on a 16:9 slide, so titles, text blocks and images will usually span several rows.

Full span tables and common slide divisions are in `references/PRES-1920x1080.md`. The calculator works the same way: `python3 scripts/grid.py PRES C --cols 4 --rows 6`.

### Setting up a slide in InDesign

1. **File › New › Document**, Intent: **Web** (or Mobile), units **Pixels**, Width 1920, Height 1080, Facing Pages off.
2. **Margins and Columns**: all four margins set to the preset margin (the chain link can stay on). Columns: **12**, Gutter: the preset gutter.
3. **Layout › Create Guides** on the parent page: Rows **12**, Gutter the preset gutter, Columns 0, **Fit Guides to: Margins**.
4. Check a module: a frame snapped to one column and one row should read exactly the preset's column width × row height (e.g. 135 × 65 px for A).

The alignment and text-frame rules below apply to digital layouts too. Slides use **full rows only**: half rows can't land on multiples of 5 px with ~100 px margins. Slide body text is never smaller than 16 px (section 7).

## 5. Aligning text boxes and objects to the grid

Everything on the page sits on the grid. The two directions follow different rules.

### Horizontal (x axis): whole columns only

Every text box, image and object starts on the left edge of a column and ends on the right edge of a column. Its width is always a whole column span from the tables (e.g. 4 columns = 62 mm on A4P A). **There are no half columns** and nothing starts or stops inside a gutter.

### Vertical (y axis): full rows, or half rows

The **top** of every text box should sit on the top of a row. When content needs finer placement, it can instead sit on a **half-row line**, but only one built so that the gutter inside the row matches the grid's gutter.

A half row splits one row module into two half modules with a normal gutter between them:

```
half module      = (row height − row gutter) ÷ 2
half-row offset  = half module + row gutter        (distance from the row's top to the half-row line)
```

Example, A4L A (row 13, gutter 3): half module = (13 − 3) ÷ 2 = **5**, and the half-row line sits **8** mm below the top of each row. The row reads as 5 + 3 + 5 = 13.

Measured from the top of the page, row *n* starts at `top margin + (n − 1) × (row + gutter)`, and its half-row line (n.5) is `(row + gutter) ÷ 2` further down. Half rows use the same numbering as a "Rows" layer in InDesign: 1, 1.5, 2, 2.5 … 12, 12.5.

**Both numbers must be whole** (mm for print, multiples of 5 px for digital). That only happens when the row height and row gutter are both odd or both even. Grids were not changed to force this, so **half rows are only available on some presets**:

| Size | Half rows? | Half module / half-row line |
|---|---|---|
| A4 portrait (all presets) | No: full rows only | – |
| A4 landscape A, B | Yes | 5 / +8 mm |
| A4 landscape C | Yes | 4 / +8 mm |
| A4 landscape D | Yes (very small half module) | 2 / +8 mm |
| A3 portrait A / B / C / D | Yes | 13 / 11 / 10 / 9, line at +17 mm |
| A3 landscape A, B | No: full rows only | – |
| A3 landscape C / D | Yes | 5 / 4, line at +12 mm |
| Slides 1920 × 1080 (all presets) | No: full rows only | – |

On a "full rows only" grid, every text box top sits on a row line and never at n.5. Don't invent a half position and don't round one. If a user asks for half rows there, explain why they aren't whole and suggest a size or preset where they are. `python3 scripts/grid.py A4L A --half 3.5` gives the exact position of any row or half-row line.

Objects with a fixed height (images, boxes, rules) that start on a half-row line should also end on a row or half-row line. Their height is then a number of half modules plus the gutters between them: `k × half module + (k − 1) × gutter`.

**Setting up half-row guides in InDesign:** on the parent page, run **Layout › Create Guides** a second time with Rows **24** and the **same row gutter**, Fit Guides to Margins. Because 24 half modules plus 23 gutters exactly fill the same space, this adds the half-row lines without moving the full rows. Put these guides on their own layer (e.g. "Rows", named 1, 1.5, 2 …) so they can be hidden when not needed.

## 6. Text-frame rules

These rules keep text sitting exactly on the grid and make frames predictable to move and restyle. Every text frame gets the same **Text Frame Options** (Object › Text Frame Options, ⌘B):

| Tab › setting | Value | Why |
|---|---|---|
| **General › Columns:** Fixed Number, 1 | Width = the exact column-span width | The frame's width is always a whole column span from the tables (e.g. 4 columns = 62 mm on A4P A). Frames start and end on column edges (section 5). Never eyeball or stretch to an in-between width. |
| **General › Inset Spacing** | 0 on all four sides | Spacing comes from the grid, not padding inside frames. Any inset pulls the text off the column edges. |
| **Baseline Options › First Baseline › Offset** | **Cap Height** | The tops of the capital letters sit exactly on the top edge of the frame. With the frame top on a row line, the visible text lines up with the row line, not with invisible space above the letters. |
| **Auto-Size › Auto-Sizing** | **Height Only** | Width stays locked to the column span; only height changes with the text. |
| **Auto-Size › Reference point** | **Top** (top-centre) | The frame grows downward as text is added, so its top edge stays fixed on the row line where it was placed. |

Other rules:
- **Top edge on a row line or a valid half-row line** (section 5).
- **Headings and body text live in separate frames.** A heading frame and its paragraph frame are two objects, each auto-sizing independently. Headings can then be moved, restyled or spanned differently (e.g. a heading across 12 columns over body text in 2 × 6) without reflowing the body.
### Object styles

Frames are never set up by hand. Every document gets one **base style** plus a library of **position styles** in folders, so a frame snaps to the right width and column just by applying a style.

**Base style: `Text – Grid`** (top level). This holds every text setting from the table above: Text Frame General Options (1 column, inset 0), Baseline Options (First Baseline Cap Height) and Auto-Size (Height Only, top-centre). It has no size or position.

**Position styles** are each **Based On `Text – Grid`**, so they inherit the text settings. Each one only adds **Size and Position Options**:
- **Size › Adjust: Width Only.** Width = the column span width.
- **Position › Adjust: X Offset Only.** X Offset = the distance from the left margin to the first column. Reference: **Page Margin**, reference point left.
- **Height and Y are left alone.** Auto-size controls the height, and the designer places the top on a row line (section 5).

**The library covers every option on a 12-column grid:** every span from 1 to 12 columns at every possible starting column, 78 styles in all. Each style goes in the **coarsest division it lines up with**, so the everyday styles sit in small folders and the unusual ones are tucked away:

| Folder | What's in it | Styles |
|---|---|---|
| (top level) | Text – Grid (base), Full Width | 1 + 1 |
| **2 Columns** | 1/2 Page – Left, Right | 2 |
| **3 Columns** | 1/3 Page – Left, Centre, Right · 2/3 Page – Left, Right | 5 |
| **4 Columns** | 1/4 Page – Left, Cols 4–6, Cols 7–9, Right · 1/2 Page – Centre · 3/4 Page – Left, Right | 7 |
| **6 Columns** | 1/6 Page ×6 · 1/3 Page – Cols 3–6, 7–10 · 1/2 Page – Cols 3–8, 5–10 · 2/3 Page – Centre · 5/6 Page – Left, Right | 13 |
| **12 Columns** | Everything that only lines up with single columns: 1/12, 5/12, 7/12, 11/12, plus 1/6, 1/4, 1/3, 1/2, 2/3, 3/4 and 5/6 spans at off-division starts. Sub-foldered by fraction (e.g. 12 Columns › 5/12) | 50 |

A style "lines up with" a division when both its start and its width fall on that division's boundaries. For example, 1/2 Page – Centre (columns 4–9) starts and ends on quarter lines, so it lives in 4 Columns, not 2 Columns.

**Naming rule:** `{fraction} Page – {position}`, with the fraction always reduced (8 columns = 2/3, 6 columns = 1/2, 9 columns = 3/4, 5 columns = 5/12).
- **Left**: starts at column 1.
- **Right**: ends at column 12.
- **Centre**: equal space either side.
- Otherwise, the column range: **Cols 4–6**, or **Col 2** for a single column.

Every name is unique. Styles always sit inside their folder, never loose at the top level. The full list with column ranges is in `references/object-styles.md`.

A separate **Panels** folder holds the shaded panel styles (Panel – K 10 … K 90, Accent – K 100). See section 8 and `references/colour.md`.

Single-column (1/12) styles are for small items like numbers, icons or labels, not body text. They're too narrow to read on A4 and slides.

Width and X values depend on the size and preset. Get them for all 78 styles with:

```
python3 scripts/grid.py --styles A4P A              # add --booklet for booklet documents
```

Example, A4P A: 1/2 Page – Right = width 94 mm, X 96 mm; 1/3 Page – Centre = width 62 mm, X 64 mm; 3/4 Page – Right = width 142 mm, X 48 mm.

X is measured from the page margin, so the same styles work on both left and right pages of a facing-pages booklet. In booklets whose column is narrower than the single sheet's (some A3 presets), use the `--booklet` values. If a heading needs a different span from its body text, apply a different position style to the heading frame.

## 7. Paragraph styles

Heading sizes come from the grid, not from a type scale. Each heading fits a set number of lines exactly into a set number of rows. The visible gap between lines always equals the **row gutter**, the same gap as between rows. Headings are **all caps**, so the capital letters are exactly what fills the rows. With First Baseline set to Cap Height (section 6), the caps of the first line sit exactly on the row line where the frame starts.

| Style | Fits | Cap height | Font |
|---|---|---|---|
| **Title** | 1 line in 1 row | `row` (the caps are exactly one row tall) | Heavy (Lato Black) |
| **Subheading** | 2 lines in 1 row | `(row − gutter) ÷ 2` | **Light (Lato Light)** |
| **Heading 1** | 3 lines in 2 rows | `(2 × row − gutter) ÷ 3` | Heavy (Lato Black) |
| **Heading 2** | 2 lines in 1 row | `(row − gutter) ÷ 2` | Heavy (Lato Black) |
| **Heading 3** | 3 lines in 1 row | `(row − 2 × gutter) ÷ 3` | Heavy (Lato Black) |
| **Heading 4** | 4 lines in 1 row | `(row − 3 × gutter) ÷ 4` | Heavy (Lato Black) |
| **Heading 5** | 5 lines in 1 row | `(row − 4 × gutter) ÷ 5` | Heavy (Lato Black) |

**Font: Lato by default, or whichever font the user asks for.** All paragraph styles use the document font. It's **Lato** unless the user names another, and the rules adapt to whatever font is used:
- **Title and Heading 1–5:** the font's **heaviest weight** (Black, else Heavy/ExtraBold, else Bold) by default. A lighter bold can be chosen if the design wants it. Use the same weight for all of them so the hierarchy comes from size. For Lato: **Black**.
- **Subheading:** the font's **light weight closest to 300** (Light, else ExtraLight/UltraLight, else Thin). For Lato: **Light**.
- If the font has no bold-to-black weight or no light-to-thin weight, say so and ask. Don't fake it with a faux bold, a lighter colour or a second family.

Subheading and Heading 2 are the same size on purpose. Weight is what tells them apart: the light Subheading typically sits under a heavy Title or Heading 1, while the heavy Heading 2 opens a section.

General formula: `cap height = (rows spanned − (lines − 1) × gutter) ÷ lines`, where "rows spanned" is the span height from section 3.

**Leading** (InDesign measures it baseline to baseline) = **cap height + row gutter**. This also means headings that run to more lines keep landing on the grid: every *n*th line starts exactly on a row line.

**Font size** comes from the cap height and the font's **cap ratio** (cap height ÷ point size). Every font has a different ratio, and it often differs slightly between weights of the same font, so each style uses its own weight's ratio. Otherwise the caps won't fill the row exactly.

```
font size (pt) = cap height (mm) ÷ cap ratio × 2.8346
```

Cap ratios are stored per font and weight in `references/fonts.json`. Lato is stored already:

| Lato weight | Thin | Light | Regular | Bold | Black |
|---|---|---|---|---|---|
| Cap ratio | 0.7000 | 0.7075 | 0.7165 | 0.7230 | 0.7285 |

These come from the Lato font files (OS/2 cap height ÷ 2000). Black was then **measured in InDesign 2026 with Adobe Fonts Lato** (100 pt H outline): 0.7285, not the Google file's 0.7255. The other weights matched exactly.

**When the user asks for a different font**, add it before calculating anything. `scripts/fontcaps.py` reads each weight's cap height straight from the font files (the OS/2 cap height, or the height of the capital H outline for older fonts), picks the default heavy and light weights, and saves the font:

```
python3 scripts/fontcaps.py --find "Avenir Next" --save        # fonts installed on this Mac (incl. activated Adobe Fonts)
python3 scripts/fontcaps.py --google "Montserrat" --save       # download from Google Fonts
python3 scripts/fontcaps.py path/to/*.otf --save               # font files the user provides
python3 scripts/fontcaps.py --list                             # fonts already saved
```

It skips italic and condensed/extended styles, and handles .ttf, .otf, .ttc collections and variable fonts. For variable fonts and CFF-outline (.otf) fonts without a stored cap height, check the result in InDesign. If nothing can be read, measure by hand: type a capital H at 100 pt, Type › Create Outlines, and read its height in mm. Cap ratio = that height ÷ 35.278. Also do this check if headings sit visibly off the rows, e.g. with an Adobe Fonts build that differs from the file measured.

Then calculate the heading table for that font:

```
python3 scripts/grid.py --type A4P A                                   # default font (Lato Black / Lato Light)
python3 scripts/grid.py --type A4P A --font "Avenir Next"              # another saved font, its default weights
python3 scripts/grid.py --type A4P A --font "Avenir Next" --heavy Bold --light Thin   # choose weights
```

It gives cap height, font size and leading. **All type values are whole numbers or 1 decimal** (e.g. 78.1 pt, 32.6 pt), never longer decimals. Rounding a heading size to 1 decimal moves its cap height by at most about 0.01 mm, which is invisible, so headings still fill their rows.

**Heading leading follows the same rules as body text.** A heading's leading (cap height + gutter) is the same as `rows × (row + gutter) ÷ lines`, so it locks to the rows like body text does. For example, Heading 4 is 4 lines per row, which on A4 portrait is 16.3 pt, identical to Body. As with body text:
- The leading is **a whole number or 1 decimal**.
- On print, the rounding error must not push text more than **0.25 mm** off the rows. Headings are short, so this is measured over the heading's own lines. Within its designed block the drift is at most about 0.06 mm.
- On slides (px), the leading must come out exact.

The calculator's **Stays on grid** column shows how long a heading can run before the rounding drift reaches 0.25 mm (e.g. A4 portrait Heading 5 at 13 pt holds for 3 rows, 18 lines). A heading should never run that long. If one does, split it or use a larger heading style. A heading whose leading can't meet these rules is marked, like one that's too small to read.

**Where headings don't fit.** Small headings need rows that are tall compared to their gutter. When a style's cap height is 0 or less (the gutters alone fill the row), or too small to read (under about 1.4 mm / 10 px cap height), the calculator marks it. Don't create that style for that preset; tell the user and suggest a preset with taller rows or narrower gutters. It mainly affects Heading 3–5 on presets with wide gutters (A4P D, A4L C/D, A3L C/D) and most headings on slide presets C and D.

**Paragraph style settings** for every heading:
- **Basic Character Formats:** Font Family: the document font (**Lato** by default). Font Style: its heavy weight, or its light weight for Subheading. Size and Leading from the calculator. Case: **All Caps**.
- **Indents and Spacing:** Space Before and Space After 0 (spacing comes from placing frames on rows). Align to Grid: None.
- Keep headings in a **Headings** paragraph style group, each in its own frame (section 6) using a position object style.

### Body text (print: A4 and A3)

Three paragraph styles (the same three are used on slides at larger sizes; see below) for running text, all in the document font's **Regular** weight (Lato Regular by default), in normal sentence case, not all caps:

| Style | Size | Leading aim | Tracking | Use |
|---|---|---|---|---|
| **Body** | **12 pt** | ~135% (range 120–150%) | 0 | Main reading text |
| **Body Condensed** | 12 pt | ~115% (range 105–125%) | −10 | Same size, packed tighter: dense text, lists, boxes |
| **Body Small** | **10 pt** | ~135% (range 120–150%) | 0 | Captions, notes, footnotes, secondary info |

**Leading locks to the rows.** Lines repeat on the grid's row pitch (row height + row gutter), so a whole number of lines fits each row:

```
leading = (row + row gutter) × rows ÷ lines
```

**Leading is always a whole number or 1 decimal.** Rows are whole millimetres and 1 mm = 2.8346… pt, so on print the exact leading is never a clean point value. The skill rounds it to 1 decimal. That's only allowed where the rounding error adds up to **no more than 0.25 mm over a full page of text** (invisible). If the rounded leading drifts more, try a different line count. On slides (px), the leading must divide exactly to a whole number or 1 decimal.

To find a line count that meets this, the lines may lock to 1, 2, 3 or 4 rows. The text then comes back in step with the grid after that many rows. Pick the option closest to the style's leading aim, preferring fewer rows. With First Baseline at Cap Height and the frame top on a row line, the first line's caps sit on the row line, and the text lands back on a row line at the end of each cycle.

| Size | Row + gutter | Body (12 pt) | Body Condensed (12 pt) | Body Small (10 pt) |
|---|---|---|---|---|
| A4 portrait | 23 mm | **16.3 pt**, 4 per row (136%) | **14.5 pt**, 9 per 2 rows (121%) | **14.5 pt**, 9 per 2 rows (145%) |
| A4 landscape | 16 mm | **15.1 pt**, 3 per row (126%) | **13.6 pt**, 10 per 3 rows (113%) | **13.6 pt**, 10 per 3 rows (136%) |
| A3 portrait | 34 mm | **17 pt**, 17 per 3 rows (142%) | **13.3 pt**, 29 per 4 rows (111%) | **13.3 pt**, 29 per 4 rows (133%) |
| A3 landscape A, B | 23 mm | **16.3 pt**, 4 per row (136%) | **14.5 pt**, 9 per 2 rows (121%) | **14.5 pt**, 9 per 2 rows (145%) |
| A3 landscape C, D | 24 mm | **17 pt**, 4 per row (142%) | **13.6 pt**, 5 per row (113%) | **13.6 pt**, 5 per row (136%) |

Drift over a full page ranges from 0.01 mm (16.3 pt on A4 portrait) to 0.23 mm (15.1 pt on A4 landscape). A3 portrait has no clean fit within 1 row. Its 34 mm pitch only gives 1-decimal leading over 3–4 row cycles.

The row + gutter total is the same for every preset of a size (except A3 landscape C/D), so body styles are the same across presets. Landscape A4 fits fewer lines per row because its rows are shorter. Body Condensed and Body Small share a leading on print, so lines of the two styles align side by side. Check any size or preset with:

```
python3 scripts/grid.py --body A4L C
```

Paragraph style settings (keep them in a **Body** style group):
- **Basic Character Formats:** document font, Regular, size, leading and tracking from the tables. Case: Normal.
- **Indents and Spacing:** Space Before 0. Space After either 0, or **exactly one line** (that style's leading) so the next paragraph stays on the rhythm. Never an in-between amount. Align to Grid: None.
- Body text goes in its own frame, separate from headings, with the top on a row line (or a valid half-row line, section 5).
- If the user wants a different body size, keep the same method: aim, range, whole or 1-decimal leading within 0.25 mm drift, fewest rows.

### Body text (slides: 1920 × 1080)

On slides, **no paragraph text is smaller than 16 px**. The same method applies. Every slide preset has the same row + gutter total (**75 px**), so the styles are identical across presets A–D:

| Style | Size | Tracking | Lines | Leading | Of size |
|---|---|---|---|---|---|
| **Body** | **18 px** | 0 | **3 per row** | **25 px** | 139% |
| **Body Condensed** | 18 px | −10 | 15 per 4 rows | **20 px** | 111% |
| **Body Small** | **16 px** | 0 | 10 per 3 rows | **22.5 px** | 141% |

Body at 18 px is the size whose leading lands closest to 135% while locking to the rows. If the user wants bigger slide text, sizes up to 20 px also fit 3 lines per row at 25 px leading (20 px = 125%). Above that, the next fit is 5 lines per 2 rows at 30 px leading (22 px = 136%). In InDesign pixel documents, 1 px = 1 pt, so enter these values directly as the size and leading.

```
python3 scripts/grid.py --body PRES A
```

### All other styles and housekeeping

Beyond headings and body text, the system includes:
- **Lists:** Bullet, Bullet Level 2, Numbered, Numbered Level 2, Bullet/Numbered Condensed, Checklist, Step, Definition
- **Supporting:** Lead (16 pt Light), Caption (Light, Body Small), Label (all caps, +100), Pull Quote (24 pt Light Italic), Block Quote, Footnote
- **Worksheet:** Learning Intention, Success Criteria, Question, Question Part, Instruction, Answer Line (solid black rules spaced to the rows)
- **Page:** Page Number, Running Footer (the only items allowed in the margin)
- **Character styles:** Bold, Italic, Key Term, Link, Marks, Step Label

Every one follows the same rules: whole or 1-decimal sizes and leading that lock to the rows, whole-mm indents, and left-aligned text with hyphenation off. Their base styles are set up so changing the font once updates everything.

**Read `references/paragraph-styles.md` before creating or checking any of these styles.** It has the settings, the housekeeping rules (Based On chain, Next Style, Keep Options, style groups) and the reasons for them. Get the exact numbers for a size and preset with:

```
python3 scripts/grid.py --sheet A4P A        # every paragraph and character style, ready to enter
```

## 8. Colour (greyscale K)

Print uses black ink only: **K 0, 10, 20 … 100** (swatches `K 10` … `K 90`, plus [Paper] and [Black]). Accessibility is non-negotiable, so every text/background pair is checked for contrast, including the darkening that happens in print. **Read `references/colour.md` before choosing or checking any colour.** The core rules:

- **Text is always the highest-contrast colour on whatever it sits on:**
  - **K 100** on paper, K 10 and K 20
  - **white** on K 70–100
  - Text colour never varies to show hierarchy. The one exception is secondary text (Caption, Footnote, Running Footer) at **K 80**.
- **Most things have no background.** Shading is optional emphasis. When used, it shows hierarchy from **K 90 (highest) to K 10 (lowest)**. **K 100** is reserved for small, very important accents. **K 10** is the default light panel.
- **No text on K 30–K 60.** Those shades are for graphics only (bars, dividers, icons, charts).
- **Contrast targets** (worst case with print dot gain):
  - **7:1** for all text as the house standard
  - 4.5:1 floor for secondary and large text
  - 3:1 for meaningful graphics (K 50 or darker)
- **Reversed (white) text:** only on K 70–100, at least 12 pt Regular or 10 pt Bold. Never in Light/Thin weights.
- **Never use shade alone to carry meaning.** Add a label or icon.
- **Panels:** object styles in a **Panels** folder (Panel – K 10 … K 90, Accent – K 100). Exact column span × whole rows, inset one gutter (column gutter left/right, row gutter top/bottom).
- **Tables:** header row K 90 with white Bold caps, body rows Body Condensed with 0.5 pt K 50 rules, optional K 10 banding.
- **Photocopied resources:** use K 20 instead of K 10 for light panels.
- **Colour documents:** the learning-domain colours (H accent, S shade, T tint) replace the greys. See `references/colour.md` section 10 and `house-tokens.md`. Add them with `build_indd.py --domain <slug>`.

```
python3 scripts/grid.py --contrast 80 20     # check any text/background pair
python3 scripts/grid.py --sheet A4P A        # includes panel, table and Key Term settings
```

## 9. When producing a layout spec or checking a layout

When asked to plan or specify a page, state the page size, preset and document type first, then give each element as: element · column span (start–end) · frame width · row start (a row number, or n.5 for a half row) · and for fixed-height items, the height. Example (A4P, preset A):

| Element | Columns | Width | Row start |
|---|---|---|---|
| Page title | 1–12 | 190 | 1 |
| Intro paragraph | 1–8 | 126 | 2 |
| Image | 9–12 | 62 × 89 (4 rows) | 2 |

When reviewing an existing layout, flag: fractional or off-grid widths, frames with inset spacing, first baseline not set to Cap Height, fixed-height text frames or auto-size not anchored at the top, tops that sit off the row and half-row lines, anything starting or ending inside a column or gutter, headings sharing a frame with body text, body styles at the wrong size (print: Body 12, Condensed 12, Small 10 pt; slides: 18, 18, 16 px, never under 16) or with leading that doesn't lock to the rows, type sizes or leading with more than 1 decimal place, paragraph spacing that isn't 0 or one full line, headings not all caps, not in the document font, in the wrong weight (Subheading light, the rest heavy), sized with the wrong font's cap ratio or with sizes/leading that don't fit the rows or aren't whole/1 decimal, text that isn't the highest-contrast colour for its background (K 100 on K 0–20, white on K 70–100, K 80 only for secondary text), any text on K 30–60, contrast below 7:1 for text, reversed Light/Thin or undersized text, large K 100 areas, shade used alone to carry meaning, frames without an object style or with local overrides to width/X, styles sitting outside their column folder or named inconsistently, margins or gutters that don't match a preset for the document type, mixed presets within one document, and 1-column text frames.
