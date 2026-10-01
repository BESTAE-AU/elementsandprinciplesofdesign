# Matching Adobe Layouts

InDesign documents and Adobe Express designs use the **same style names,
specifications, grid and colour tokens** as the Word templates. That gives two
practical benefits:

1. A booklet made in InDesign and one made in Word look like the same series.
2. Word text placed into InDesign maps onto the InDesign styles automatically,
   because the style names match.

## InDesign document setup

These values already match the existing InDesign booklet file (Untitled-2.idml).

| Setting | Value |
|---|---|
| Page size | A4, 210 × 297 mm |
| Facing pages | On (booklets); off for flat printouts |
| Margins, booklet | Top 12, bottom 12, inside 12, outside 8 mm |
| Margins, flat | Top 12, bottom 12, left 10, right 10 mm |
| Columns | 12, gutter 2 mm (column width 14 mm) |
| Baseline / row grid | 12 rows of 20 mm with 3 mm gutters (Layout → Create Guides: 12 rows, 3 mm gutter, fit to margins) |
| Bleed | 5 mm when anything runs to the page edge; otherwise 0 |

## Paragraph styles

Create these names exactly: the same spelling, capitals and spaces as Word.

| InDesign paragraph style | Font / style | Size | Leading | Case | Align | Colour |
|---|---|---:|---:|---|---|---|
| **Normal** (based on [Basic Paragraph]) | Lato Regular | 12 | 14 | — | Left | Text |
| **Title** | Lato Bold | 78 | 78 | All caps | Centre | Text |
| **Subtitle** | Lato Light | 33 | 38 | All caps | Centre | Text |
| **Heading 1** | Lato Black | 52 | 52 | All caps | Centre | Text |
| **Heading 1 White** | Lato Black | 52 | 52 | All caps | Centre | Paper |
| **Heading 2** | Lato Bold | 36 | 36 | All caps | Centre | Text |
| **Heading 3** | Lato Light | 20 | 23 | All caps | Centre | Text |
| **Heading 4** | Lato Black | 16 | 18 | All caps | Centre | Text |
| **Heading 5** | Lato Black | 12 | 14 | All caps | Centre | Text |
| **Heading 6** | Lato Light | 16 | 18 | All caps | Centre | Text |
| **Heading 7** | Lato Medium | 12 | 14 | All caps | Centre | Text |
| **Heading 8** | Lato Heavy | 10 | 12 | All caps | Left | Text |
| **Heading 9** | Lato Heavy | 10 | 12 | All caps | Centre | Text |
| **White Table Heading (12pt)** | Lato Bold | 12 | 14 | All caps | Centre | Paper |
| **Caption** | Lato Italic | 10 | 12 | — | Left | Muted |
| **Table Text** | Lato Regular | 12 | 14 | — | Left | Text |
| **2. Question Format** | Lato Regular | 12 | 14 | — | Left, 7 mm hanging indent, 8.5 mm before | Text |
| **4. Marks** | Lato Bold | 18 | 22 | All caps | Right | Text |

Space after: 3.5 mm on Normal and on Heading 3 to Heading 9. 0 on Title,
Subtitle, Heading 1 and Heading 2, whose spacing is set by grid position.

**InDesign-only styles** are allowed where Word has no equivalent. Base them on a
shared style so they inherit the type:

- **Mini Label (Left)** / **Mini Label (Right)**: Lato Regular 6 pt, all caps.
  For page furniture only (running labels, page references), never for content
  students must read.
- **Condensed Text**: Lato Regular 10 pt. For dense captions or annotations only.
  Don't use it for instructions.

### Fixes needed in the existing InDesign file

| Style | Now | Change to |
|---|---|---|
| [No paragraph style] / [Basic Paragraph] | Minion Pro 12, fully justified | Lato Regular 12, left aligned |
| Title | Lato Black 78 | Lato Bold 78 |
| Heading 1 | Size only (52), font inherited | Lato Black 52, all caps, centred |
| Heading 2 | Size only (36), font inherited | Lato Bold 36, all caps, centred |
| Heading 3 | Lato Bold 24 | Lato Light 20 |
| Heading 4 | Lato Bold 16 | Lato Black 16 |
| Paragraph Text | Lato, no size | Rename to **Normal**, Lato Regular 12 / 14 |
| Heading 5–9, Subtitle, Caption, White Table Heading (12pt) | Missing | Add from the table above |

## Colour swatches

Create one swatch per role token, named after the token. That way, swapping
between Greyscale and Bestae in InDesign is also a swatch edit.

### Greyscale swatches (print as black ink only)

For mono printing, define the Greyscale tokens as **K-only CMYK** swatches.
Converting from RGB would print the greys as a mix of all four inks.

| Swatch | Hex (screen) | CMYK for print |
|---|---|---|
| Light | `#E3E4E3` | 0 0 0 11 |
| Pale | `#CACBCA` | 0 0 0 21 |
| Accent | `#767776` | 0 0 0 54 |
| Dark | `#4C4D4C` | 0 0 0 70 |
| Darkest | `#343433` | 0 0 0 80 |
| Muted | `#5E5E5E` | 0 0 0 63 |

These K values approximate the screen greys. Proof one page on the actual
printer and adjust once for the whole set.

### Bestae swatches

- Create Light, Pale, Accent, Dark and Darkest swatches using the **hex values of
  the chosen domain** (see `colour-layers.md`) in RGB.
- Let InDesign convert to CMYK on export, using the printer's profile.
- Proof bright colours before a print run: Corn, Lime, Tomato and Valentine Pink
  shift most in CMYK.

## Adobe Express

Express has no paragraph styles, but its **Brand Kit** can hold fonts, text
styles and colours:

| Brand Kit item | Set to |
|---|---|
| Fonts | Lato (Regular, Light, Bold, Black, Heavy) |
| Title text style | Lato Bold, all caps (maps to Title / Heading 1) |
| Heading text style | Lato Bold, all caps (maps to Heading 2) |
| Subheading text style | Lato Black, all caps (maps to Heading 4) |
| Body text style | Lato Regular (maps to Normal) |
| Colours | The role tokens of the layer: Greyscale set, or the domain's Bestae set |

Build Express designs at A4 with the same 12 mm / 8 mm margins when they sit
alongside a printed booklet. For slides and social graphics, use the fonts and
colours only; the grid and sizes don't apply.

## Word → InDesign workflow

1. Write and style the content in Word using only the shared styles.
2. In InDesign: File → Place, tick **Show Import Options**, then choose
   **Preserve styles and formatting**. For style name conflicts, choose **Use
   InDesign Style Definition**.
3. Because the names match, Heading 4 in Word becomes Heading 4 in InDesign.
   There's no manual restyling.
4. Tables come across as InDesign tables. Re-apply cell fills from the swatches
   if they arrive as plain colours.
