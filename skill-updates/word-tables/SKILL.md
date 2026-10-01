---
name: word-tables
description: Table design system for Word (.docx) workbooklets, worksheets and handouts. Covers table and column widths, portrait vs landscape pages, cell padding, heading styles, Greyscale or Bestae fills and borders, response space, pagination and accessibility. Use whenever creating, formatting or checking any table-shaped content in a Word document, including rubrics, marking criteria, matrices, comparison charts, graphic organisers, glossaries, specification tables, image comparisons and student response tables, or when deciding whether content should sit on a landscape page.
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

## Principles

These principles drive every rule in this skill. When a situation isn't covered,
reason from them.

1. **Structure follows information.** Decide what the table is for and how
   students will read it before choosing any dimension. Orientation, width and
   column sizes serve that structure, never the other way round.
2. **One system, two widths.** Portrait and landscape share every rule except the
   width grid. Landscape is an extension, not a separate style.
3. **Intentional, not equal.** Every column width is a decision about how much
   space its content needs. Equal columns are right only when the content is
   genuinely parallel (comparison items, grade levels).
4. **Examples, not presets.** The example structures and default values show good
   decisions. They aren't a menu to pick from. Size for the actual content.
5. **Clarity over convenience.** Don't switch orientation, shrink text or drop to
   the alternative width to avoid making a proper decision. Change the structure
   instead.
6. **Consistency across the booklet.** Tables in one workbooklet should look like
   they belong together: the same widths, header treatment, borders and spacing.
7. **Readable in print and accessible.** Everything must work in greyscale on
   paper and make sense to a screen reader.

Where a rule's default value (a padding, a border weight, a row height) clearly
works against these principles for a particular table, depart from it. State
the reason in your reply to the user.

## How this skill fits with the other design skills

Three skills work together:

| Topic | Governed by |
|---|---|
| Page size, portrait margins, header/footer distance, 12 × 12 grid, booklet rules (multiple of 4 pages, creep, fold clearance) | `greyscale-print-design-system` |
| Typeface, style names and sizes, what each heading level is for, colour layers (Greyscale and Bestae), Adobe matching | `workbooklet-style-system` |
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
- **Colour.** "The established palette" means the role tokens of the
  document's colour layer, Greyscale or Bestae, applied as theme colours (see
  `workbooklet-style-system`). Anything outside the chosen layer is off-system.

## Workflow

1. **Name the table's job** (comparison, classification, rubric, response and so
   on) with `references/table-types.md`. That decides the structure and which
   column gets the width.
2. **Choose the orientation** from the information architecture. Default to
   portrait. Use the tests in `references/landscape-tables.md` ("Choosing
   portrait or landscape").
3. **Choose the table width.** Try the preferred width (19 / 27 cm) first. Apply
   "Preferred or alternative width?" in `references/sizing.md`. Move to the
   alternative (18 / 26 cm) only when it gives a clearly cleaner structure.
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
