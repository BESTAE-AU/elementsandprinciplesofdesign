---
name: word-tables
description: Table design system for Word (.docx) workbooklets, worksheets and handouts. Covers table and column widths, portrait vs landscape pages, cell padding, heading styles, greyscale fills and borders, response space, pagination and accessibility. Use whenever creating, formatting or checking any table-shaped content in a Word document, including rubrics, marking criteria, matrices, comparison charts, graphic organisers, glossaries, specification tables, image comparisons and student response tables, or when deciding whether content should sit on a landscape page.
---

# Word Tables

One table design system for Word workbooklets. It applies to every table, on
every page, in every orientation.

## The one rule to remember

**Portrait = 19 / 18 cm. Landscape = 27 / 26 cm.** Everything else carries
across unchanged.

| Page orientation | Preferred width | Alternative width |
|---|---:|---:|
| **A4 Portrait** | **19 cm** (190 mm) | **18 cm** (180 mm) |
| **A4 Landscape** | **27 cm** (270 mm) | **26 cm** (260 mm) |

These widths are the working grid for the table. Within that grid, divide the
columns according to the **type, quantity and relationship of the information**,
not into equal shares.

Why these widths: 19 cm is exactly the workbooklet's 190 mm content area, so a
full-width table lines up with the text above and below it. 27 cm stays inside
the landscape content area on both flat printouts and booklets (see
`references/landscape-tables.md`), so the same table works in either.
Orientation changes the available width. It does **not** change the design
system.

## How this skill fits with the print design system

When the document uses the Greyscale Workbooklet template, the
`greyscale-print-design-system` skill and this skill work together:

| Topic | Governed by |
|---|---|
| Page size, portrait margins, header/footer distance, booklet rules (multiple of 4 pages, creep, fold clearance) | Print design system |
| Typeface, type scale, named styles, greyscale palette | Print design system |
| Table widths, column widths, orientation choice, landscape pages, cell padding, borders, response space, table pagination, table accessibility | **This skill** |

Where the two seem to disagree:

- **Units.** The print system works in millimetres; these rules are written in
  centimetres. They are the same measurements: 19 cm = 190 mm. Convert with
  cm × 10 = mm, or cm × 28.3465 = points for Office.js.
- **The 12-column grid.** Information tables use whole-centimetre columns and
  do **not** snap to the 14 mm grid modules. Their outer edge still aligns with
  the grid because 19 cm = the 190 mm content area. Use the print system's grid
  spans and spacer columns only for **layout blocks** that must line up with
  other blocks on the grid (for example, a 3-up image panel).
- **Alignment.** Information tables are centred. A 19 cm table fills the content
  area, so centred and left-aligned look identical. An 18 cm table sits 5 mm in
  from each margin. Grid layout blocks stay left-aligned, as the print system
  says.
- **Colour.** "The established palette" means the print system's greyscale
  tokens. Anything with hue is off-system.

## Workflow

1. **Name the table's job** (comparison, classification, rubric, response and so
   on) with `references/table-types.md`. That decides the structure and which
   column gets the width.
2. **Choose the orientation** from the information architecture. Default to
   portrait. Use the tests in `references/landscape-tables.md` ("Choosing
   portrait or landscape").
3. **Choose the table width.** Try the preferred width (19 / 27 cm) first. Apply
   the tie-break in `references/sizing.md` to decide whether the alternative
   (18 / 26 cm) is better.
4. **Size the columns** for their content, above the minimum widths in
   `references/sizing.md`. Check that they add up exactly to the table width.
5. **Style the table**: headings, fills, borders, separators, response space.
   See `references/styling.md`.
6. **Check pagination and accessibility**. See `references/styling.md`.
7. **Build it** with the values in `references/word-implementation.md`. For a
   landscape table in a portrait document, isolate it in its own section.
8. **Verify**: render to PDF and run the checklist at the end of
   `references/word-implementation.md`.

## Reference files

| File | Read it when |
|---|---|
| `references/table-types.md` | First, for every table: is a table right, what job it does, typical structure and orientation by type |
| `references/portrait-tables.md` | Any portrait table: geometry, 19/18 cm structures, column limits, transposing, height |
| `references/sizing.md` | Choosing table width, column widths, minimum widths, cell padding, the vertical category column |
| `references/landscape-tables.md` | Deciding portrait vs landscape, or putting any table on a landscape page (geometry, height limits, booklet rotation) |
| `references/styling.md` | Headings, fills, borders, white separators, images, response space, pagination, accessibility |
| `references/word-implementation.md` | Writing the .docx: twip/point values, table XML, Office.js notes, section breaks, verification |
| `references/worked-examples.md` | Before sizing a table you're unsure about: three examples with the reasoning shown |

`evals/evals.json` holds test prompts for checking the skill.

## Non-negotiables (quick check)

- Table width is 19 or 18 cm (portrait) or 27 or 26 cm (landscape).
- Columns are whole centimetres, or 0.5 cm steps where justified, and add up
  exactly to the table width.
- No column is below its minimum width.
- AutoFit is off (fixed layout), so Word can't resize columns.
- Header rows repeat on each page and are marked as headers.
- Rows never split across pages.
- No meaning carried by shade alone.
- No blank pages and no orientation leaks from section breaks.
