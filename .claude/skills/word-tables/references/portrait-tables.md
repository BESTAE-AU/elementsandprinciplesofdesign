# Portrait Page Tables

Portrait is the default orientation for workbooklet tables. The landscape rules
(`landscape-tables.md`) extend this file; they don't replace it.

---

## Portrait page geometry

Page size: A4 portrait, 21 × 29.7 cm. Margins come from the print design system
and depend on how the document is bound:

| Binding | Top / bottom | Left / right | Usable width | Usable height |
|---|---|---|---:|---:|
| **Saddle-stapled booklet** | 1.2 / 1.2 cm | 1.2 inside / 0.8 outside | 19 cm | 27.3 cm |
| **Flat printout** | 1.2 / 1.2 cm | 1 / 1 cm | 19 cm | 27.3 cm |

The usable area is 19 × 27.3 cm (190 × 273 mm) in both cases.

---

## Portrait table width

**19 cm — preferred/default portrait table width.** It is exactly the content
area, so a 19 cm table lines up with the text and other blocks above and below
it.

**18 cm — alternative portrait table width.** It sits 5 mm in from each margin
when centred. Use it where it gives cleaner column divisions (see the tie-break
in `sizing.md`), or where a slightly inset table reads better, for example a
short reference table between paragraphs of text.

Don't use widths between or below these (17 cm, 18.5 cm, a table dragged to fit).
If a table seems to need less than 18 cm, it probably has too few columns to need
the full width. Keep 18 cm, and give the spare width to the column with the most
text or writing.

---

## Portrait column widths

The column rules and minimum widths in `sizing.md` apply.

### Examples of valid 19 cm structures

- 9.5 + 9.5 cm
- 6 + 13 cm
- 5 + 14 cm
- 4 + 15 cm
- 3 + 16 cm
- 5 + 7 + 7 cm
- 6 + 6 + 7 cm
- 4 + 7 + 8 cm
- 3 + 8 + 8 cm
- 4 + 5 + 5 + 5 cm
- 3 + 4 + 4 + 4 + 4 cm
- 1 + 9 + 9 cm
- 1 + 6 + 6 + 6 cm
- 1 + 4 + 14 cm

### Examples of valid 18 cm structures

- 9 + 9 cm
- 6 + 12 cm
- 5 + 13 cm
- 4 + 14 cm
- 6 + 6 + 6 cm
- 3 + 5 + 10 cm
- 4 + 7 + 7 cm
- 4.5 + 4.5 + 4.5 + 4.5 cm
- 3 + 5 + 5 + 5 cm
- 1 + 17 cm
- 1 + 8.5 + 8.5 cm
- 1 + 5 + 6 + 6 cm

These are examples only, not presets. Size columns for the actual content. A
leading 1 cm column is the vertical category column (see `sizing.md`).

### Portrait column limits

At 19 cm, a table with more than 5 content columns pushes at least one column
below its minimum width. Before moving to landscape, check whether:

- two columns can merge (for example "Term" and "Example" become "Term (example)");
- a column belongs in a separate table;
- the table can be transposed, so the many items run down the page and the few
  attributes run across it.

Transposing is often the best fix. Portrait has more height than width, so the
longer list should run down the page.

---

## Portrait height

Usable height is 27.3 cm. After a Heading 4 table heading and a header row, allow
roughly **24 cm for the table body**. That is 50% more than on a landscape page.
This is why long, narrow tables belong in portrait.

Keep a complete table on one page wherever reasonably possible. Split only
genuinely long tables, at a logical boundary, with the header row repeated (see
`styling.md`).
