The Greyscale Workbooklet system is Brittany's print-first house style for worksheets, workbooklets, exam papers and handouts. It is captured from **Greyscale Workbooklet.dotm**. Everything is greyscale, set in Lato on a 12 × 12 modular grid, with **all spatial measurements in millimetres** and type sizes in points. Base new documents on the `.dotm` template and apply its named styles. Never restyle a blank document by hand. Use en-AU spelling throughout.

## Content fundamentals

Write for students working on paper. Question stems use `question`, answer options use `mc-answers`, mark boxes use `marks`, answer space uses `writing-lines` and model answers use `example-response`. Size writing space to the marks: about three lines per mark for short responses, and three lines ≈ one 20 mm row module. Rubrics use the `MARKING CRITERIA` table style (MARKS | CRITERIA) with `white-table-heading` header cells.

## Visual foundations: colour (greyscale only)

The palette is `ink`, six shading steps `accent-1` (lightest) to `accent-6` (darkest), `pale`, `muted`, `link`, `link-followed` and `reverse` (white). Anything with hue is off-system: flag it rather than inserting it.

**Proportion (60-30-10):** about 60% `reverse` paper, 30% light structure (`pale` panels, `accent-1`/`accent-2` table shading, `ink` text), and 10% dark emphasis (`accent-4`–`accent-6` header rows, example-response panels).

**Text on each fill** (WCAG, 4.5:1 for body text):

| Fill | Text | Never |
|---|---|---|
| `reverse` (paper) | `ink` 21 · `muted` 6.5 · `link` 6.5 · `link-followed` 12.5 | — |
| `pale` | `ink` 12.9 | `muted` 4.0 · `link` 4.0 · `reverse` 1.6 |
| `accent-1` | `ink` 7.2 | `reverse` 2.9 |
| `accent-2` | `ink` 5.8 | `reverse` 3.6 |
| `accent-3` | *either, at the edge* (`ink` 4.67, `reverse` 4.50). Fills, bars and rules only, or bold 14 pt+ | body text |
| `accent-4` | `reverse` 7.0 | `ink` 3.0 |
| `accent-5` | `reverse` 8.9 | `ink` 2.4 |
| `accent-6` | `reverse` 11.6 | `ink` 1.8 |

- **One rule to remember:** `ink` on `pale`, `accent-1` and `accent-2`; `reverse` on `accent-4`, `accent-5` and `accent-6`; nothing on `accent-3`.
- **The coding set:** when shading marks a category (mark bands, question types, domains), use only `pale`, `accent-2`, `accent-4` and `accent-6`. They are 2.2, 1.95 and 1.65:1 apart; neighbouring accents are only 1.24–1.3:1 and blur together in print. `accent-1`, `accent-3` and `accent-5` are for decoration and fills. Label every coded row or panel in words as well.
- **Links:** `link` is now `#5E5E5E` (6.5:1 on paper; it was `#898A89` at 3.5:1). Always underline links. On `pale`, set links in `ink` underlined. The Hyperlink style in `Greyscale Workbooklet.dotm` needs the same change.
- **Captions on `pale`** use `ink`, not `muted` (4.0:1).
- **Check the print:** after a test print, look at white-on-grey and grey panels on the actual printer. Tone gain makes darks heavier and can fill in `accent-3`.

## Visual foundations: typography

**Lato family only.** Never substitute Aptos, Calibri or Times New Roman. Consolas is for code and plain-text styles only.
- Weights: Lato for body and most headings. Lato Light for Subtitle, H3, H6, Quote, Intense Quote and Subtle Emphasis. Lato Medium for H7 and Emphasis. Lato Semibold for Example Response and Subtle Reference. Lato Black for H1, H4, H5, TOC Heading and Intense Reference. Lato Heavy for H9.
- All headings are centred and black (`title` 78 pt down to `h9` 10 pt). `normal` is Lato 12 pt, left-aligned, with 3.5 mm after and 4.9 mm line spacing.
- Apply styles by name. Never set a document-wide font, and never fake a heading with direct bold and size.

## Page, grid and binding

- **A4 portrait.** Top and bottom margins are `margin-top` and `margin-bottom` (12 mm). Side margins depend on the variant:
  - flat printouts: `margin-flat-side` 10 mm each side
  - saddle-stapled booklets: `margin-booklet-inside` 12 mm and `margin-booklet-outside` 8 mm
  - Header and footer distance is 12.5 mm.
- **Grid:** the content area is always 190 × 273 mm, divided into 12 columns (`col-module` 14 mm + `col-gutter` 2 mm) and 12 rows (`row-module` 20 mm + `row-gutter` 3 mm). The rhythm unit is 23 mm. Use the `col-span-*` and `row-span-*` widths. In Word, build gutters as real 2 mm spacer columns with AutoFit off, and re-read column widths after content lands.
- **Booklets:**
  - The page count must be a multiple of 4.
  - Keep `fold-clear-zone` (6 mm) either side of the fold free of text and rules.
  - Put page numbers in the outside-bottom corner.
  - Turn on **Book fold** in Layout › Page Setup before printing, and keep pages in reading order.

## Iconography and imagery

The template defines no icon set. Where an icon is needed, use a simple single-weight line icon in `ink`. Convert photographs to greyscale and check them in a test print. Never use colour to carry meaning.

## Relationship to the other systems

This is the **print layer** for BESTAE resources and for school resources framed in MCCNS branding. When a colour resource (BESTAE domain colours, MCCNS navy and cerise) is printed in greyscale, its colour meaning is lost. Put the domain or category **name** on every coded panel so the printed copy still makes sense.
