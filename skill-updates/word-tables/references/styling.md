# Table Styling, Pagination and Accessibility

All styles come from the shared workbooklet template (see the
`workbooklet-style-system` skill). Apply them by name. Never recreate a style with
direct formatting (bold, size, font, colour).

Colours are **role tokens** (Light, Pale, Dark and so on). Each token has a
Greyscale value and a Bestae value, and is applied as a **theme colour**. The same
table then works in both colour layers. Values are in
`workbooklet-style-system/references/colour-layers.md`.

## Headings and text

The three heading levels form the table's hierarchy:

| Level | Style | Used for |
|---|---|---|
| Primary | **Heading 4** | The table's primary headings: the header row (column headings). Also a title directly above the table, when one is needed. |
| Secondary | **Heading 5** | Table subheadings: group rows, sub-header cells under a spanning heading. |
| Minor | **Heading 9** | Minor headings and labels: row labels, small labels inside cells. |
| — | Table Text (12 pt) | Body text in cells: Normal without paragraph spacing. |

- **Headings on dark fills.** Heading 4, 5 and 9 are black. On a Dark or
  Darkest fill, use `White Table Heading (12pt)` in their place. Never colour a
  heading white by hand.
- **Rubrics** in the marks + criteria format use the `MARKING CRITERIA` table
  style, with `White Table Heading (12pt)` in the header row, as the print
  design system specifies.
- **Headings that don't fit.** Heading 4 is 16 pt. If a column heading wraps
  awkwardly, shorten the wording ("Definition", not "Definition of the term") or
  give the column more width. Never drop to a smaller style to make it fit.
- **Minimum text size in tables: 10 pt.** Don't shrink text to make a table fit.
  Change the widths, the orientation or the structure instead.
- **Titles above tables.** Often the surrounding section heading already
  introduces the table, and no separate title is needed. When one is, it has
  "keep with next" on so it stays with the table.

## Fills and contrast

| Cell role | Fill token | Greyscale | Word theme colour | Text |
|---|---|---|---|---|
| Header row (default) | Light | `#E3E4E3` | Background 2 | Heading 4 (black) |
| Header row (strong emphasis, rubrics) | Dark | `#4C4D4C` | Accent 6 | `White Table Heading (12pt)` |
| Vertical category column | Dark | `#4C4D4C` | Accent 6 | `White Table Heading (12pt)` |
| Sub-header or group row | Pale | `#CACBCA` | Accent 1 | Heading 5 (black) |
| Row label cells | Light | `#E3E4E3` | Background 2 | Heading 9 (black) |
| Body and response cells | Paper | `#FFFFFF` | Background 1 | Table Text (black) |

In the Bestae layer, the same theme colours become the domain's Tint (Light,
Pale) and Shadow (Dark). Nothing in the table needs changing.

- **Always pick fills from the Theme Colours rows**, never "More colours…".
  Otherwise the table won't recolour when the layer changes.
- Use one header-row treatment consistently within a workbooklet, except for
  rubrics.
- **White text only on Dark or Darkest.** Black text on Paper, Light and Pale.
  For Bestae domain 4, Dark is Dark Gold `#8A6400` (white text, 5.4:1): use it for
  header rows and bold labels, not long body text (see `colour-layers.md`).
- **Never put body text on the Accent token.** It's for bars and rules.
- Don't use banded (alternating) row shading in response tables: it prints
  unevenly and makes writing on shaded rows harder.

## Borders

Default borders for an information table (the `Table 2` table style):

| Border | Weight | Colour |
|---|---|---|
| Outer and internal borders between white cells | 0.5 pt | Dark token (Accent 6) |
| Outer border of a table that must stand out | 1 pt | Dark token (Accent 6) |
| Borders between or around filled cells | 0.5 pt | Paper (white), so fills read as solid blocks |

Context-sensitive colour means the border matches the cells either side of it: a
dark line between white cells, a white line between filled cells.

**Borderless structures** suit layout tables and simple two-column label/content
lists, where alignment alone groups the content. Keep borders wherever students
write in cells, so each answer space is clearly bounded.

**Creep in booklets.** Don't run borders to the outside page edge, and keep them
6 mm clear of the fold (the print design system's rule).

## Thick white separators

A thick white separator is a **3 pt white border** used to split a table into
visible groups without adding lines.

Use it:

- between vertical category groups;
- between the header row and a filled first body row;
- between adjacent dark-filled cells that need to read as separate blocks.

Don't use it between ordinary white body rows: it won't be visible there.

## Images in tables

- Image columns are at least 4 cm wide, and 5 cm or more where students need to
  see detail.
- **Standard images** sit inside the cell padding with the image width = column
  width − padding. Keep one consistent height across a row of images.
- **Edge-to-edge images** fill the cell completely. Set that cell's padding to
  0 mm and the image width to exactly the column width. Use edge-to-edge for
  image-led comparison tables. Use standard for images placed next to text.
- Crop images to a common aspect ratio within a comparison, so differences come
  from the content, not the framing.
- **Insert images inline** (in line with text), never floating or "in front of
  text". Floating images inside tables drift when the table is edited or
  repaginated.
- **Size images to their column in the document**, not by dragging handles.
  Check the image width against the column width minus padding.
- **Resolution:** at least 300 ppi at the printed size. A 9 cm wide image needs
  about 1060 pixels across.
- **Check in greyscale.** Colour images print in grey. If the task depends on
  colour differences (hue, a colour scheme), say so next to the image and
  describe the colours in words.
- **Captions and credits** go in the cell under the image in the `Caption`
  style, not in a separate row of their own unless every image has one.
- Every image needs alt text (see Accessibility).

## Student response space

Set response rows as **minimum heights ("at least")**, never exact heights, so a
row grows if content needs more space instead of hiding it.

| Response type | Minimum row height |
|---|---|
| One word, a number, a tick | 1 cm |
| One sentence | 2 cm |
| Short paragraph | 3 lines per mark on the `Writing Lines` style (3 lines ≈ 20 mm, one row module) |
| Sketch or diagram | 6.6 cm (3 row modules) or more |

Response cells are white with a visible border.

## Pagination

- **Never split a row across pages.** Turn on "Allow row to break across pages:
  off" (`cantSplit`) for every row.
- **Keep a complete table on one page** wherever reasonably possible. Keep the
  Heading 4 heading with the table.
- **Long tables:** repeat the header row on every page, and split only at a
  logical boundary (between groups, never mid-group).
- **Rows taller than a page:** restructure. See `landscape-tables.md`, "Landscape
  pages are short".
- **Booklets:** after adding or moving tables, check that the page count is still
  a multiple of 4.

## Accessibility

- **Mark header rows** as headers ("Repeat as header row" / `tblHeader`), so they
  repeat on each page and screen readers announce them.
- **Alt text on every table:** a title and a one-sentence description of what
  the table shows.
- **Alt text on every image.** Mark purely decorative images as decorative.
- **Never carry meaning by shade alone.** In greyscale print especially,
  categories need words, not just a darker fill.
- **Merge cells only where the merge carries meaning**, such as a vertical
  category group or a header spanning its sub-columns. Never merge just for
  visual layout.
- **No empty rows, columns or cells used for spacing.** Use cell padding,
  paragraph spacing or white separators instead. Empty cells meant as response
  space are fine.
- **Reading order:** a table must make sense read left to right, top to bottom,
  one row at a time.
- **Layout tables** (borderless tables used only to position content) have no
  header row, and their content must read in a sensible order when linearised.
  Prefer paragraphs, columns or text boxes where they do the job.
