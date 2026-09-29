# Table Styling, Pagination and Accessibility

All styles come from the supplied Word template (Greyscale Workbooklet.dotm).
Apply them by name. Never recreate a style with direct formatting (bold, size,
font). The colour values are the print design system's greyscale tokens.

## Headings and text

| Use | Style |
|---|---|
| Primary table heading, placed above the table (not inside it) | Heading 4 |
| Subheadings within a table (a group heading row, a sub-header cell) | Heading 5 |
| Minor headings and labels (column headings on light fills, row labels) | Heading 9 |
| Headings on dark fills (Accent 4–6) | `White Table Heading (12pt)` |
| Body text in cells | Normal (12 pt) |
| Marking-criteria rubrics | Table style `MARKING CRITERIA` |

- **Minimum text size in tables: 10 pt.** Don't shrink text to make a table fit.
  Change the widths, the orientation or the structure instead.
- Keep the Heading 4 table heading on the same page as the table: its paragraph
  has "keep with next" on.

## Fills and contrast

| Cell role | Fill | Text |
|---|---|---|
| Header row | Accent 5 `#494A49` or Accent 6 `#383938` | `White Table Heading (12pt)` |
| Vertical category column | Accent 4–6 | `White Table Heading (12pt)` |
| Sub-header or group row | Pale `#CACBCA` | Heading 5 or Heading 9 (black) |
| Row label column (optional) | Pale `#CACBCA` | Heading 9 (black) |
| Body and response cells | White | Normal (black) |

- White text **only** on Accent 4–6. Black text on White, Pale and Accent 1–3.
- Accent 1–3 are mid-greys. Use them sparingly, and never behind body text
  students must read at length.
- Don't use banded (alternating) row shading in response tables: it prints
  unevenly and makes writing on shaded rows harder.

## Borders

Default borders for an information table:

| Border | Weight | Colour |
|---|---|---|
| Outer border | 1 pt | Accent 6 `#383938` |
| Internal borders between white cells | 0.5 pt | Accent 1 `#969896` |
| Borders between or around filled cells | 0.5 pt | White (so fills read as solid blocks) |

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
