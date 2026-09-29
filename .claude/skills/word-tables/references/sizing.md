# Table and Column Sizing

## Table width

| Page orientation | Preferred width | Alternative width |
|---|---:|---:|
| A4 Portrait | 19 cm | 18 cm |
| A4 Landscape | 27 cm | 26 cm |

Start with the preferred width.

### Preferred or alternative width?

**Keep the preferred width (19 / 27 cm)** whenever the columns can be sized
properly for their content in whole or half centimetres.

Two equal columns at 9.5 + 9.5 cm are a valid 19 cm table. Don't drop to 18 cm
just to avoid a half centimetre.

**Move to the alternative width (18 / 26 cm)** only when it gives a clearly
cleaner or more logical structure. For example:

- **The preferred width can't be divided in 0.5 cm steps.** Three equal columns:
  19 cm would need 6.33 cm each, so use 18 cm = 6 + 6 + 6.
- **The preferred width forces a column to be wider than its content needs**,
  just to use up the space, and the alternative removes that empty space.
- **The alternative lines up the columns with a related table** on the same page
  or spread. For example, a response table directly under an 18 cm reference
  table uses the same column boundaries.

Before switching, try redistributing at the preferred width. Often moving 1 cm
from one column to another resolves the problem. For example, an A–E rubric at
27 cm can be 7 + 4 + 4 + 4 + 4 + 4 (see `worked-examples.md`).

Why: the preferred width keeps tables lined up with the content area and with
each other across a booklet. The alternative exists to serve the information
structure, not to avoid a half centimetre.

## Column widths

Columns:

- do not need to be equal;
- should reflect the amount and function of their content;
- should be whole centimetres wherever practical;
- may use 0.5 cm steps where that gives a better structure;
- should never use arbitrary decimals (4.37 cm, 6.2 cm); and
- must add up exactly to the table width.

### Minimum column widths

A column narrower than this cannot hold its content legibly at the table's
minimum font size (10 pt):

| Column content | Minimum width |
|---|---:|
| Rotated vertical category label | 1 cm |
| Numbers, marks, ticks, single letters (A–E) | 1.5 cm |
| Short labels (1–3 words), headings | 2.5 cm |
| Sentences or explanations | 3 cm |
| Student written responses | 4 cm |
| Images | 4 cm (5 cm or more where detail matters) |

If a table cannot meet these minimums at 19 cm, first check whether a column can
be removed, merged or moved to a second table. Only then consider landscape (see
`landscape-tables.md`).

### Use the width where the text is

Give short label columns only what they need (typically 2–4 cm). Give the
remaining width to the columns with the most text or the most student writing.
Don't share spare width equally.

## Cell padding

Padding comes out of each column's width, so narrow columns lose a large share
of their space to it. Word's default is about 1.9 mm left and right.

House padding:

| Cell type | Left / right | Top / bottom |
|---|---:|---:|
| Standard cells | 2 mm | 1 mm |
| Columns 1.5 cm wide or narrower | 1 mm | 1 mm |
| Edge-to-edge image cells | 0 mm | 0 mm |

Content space = column width − left padding − right padding. A 1 cm column with
standard padding has only 6 mm of space; with 1 mm padding it has 8 mm.

Set padding on the table as a whole (table-level cell margins) and override it
only on the narrow or image columns that need it.

## The vertical category column

Several example structures start with a 1 cm column (for example 1 + 13 + 13 cm
or 1 + 5 + 10 + 10 cm). This is the **vertical category column**: a narrow band
down the left edge that names the group the rows beside it belong to, such as
"Elements" and "Principles", or "Before", "During" and "After".

Use it when rows fall into two or more named groups and students need to see the
grouping at a glance. Don't use it for a table with only one group; use a
header row or a title instead.

Specification:

- **Width:** 1 cm (up to 1.5 cm for labels longer than about 15 characters).
- **Text direction:** rotated, reading bottom to top.
- **Merged:** merged vertically across all the rows in its group, one merged cell
  per group.
- **Fill and text:** a dark fill (Accent 4–6) with the `White Table Heading (12pt)`
  style, or a Pale / Accent 1–2 fill with Heading 9. Never white text on a light
  fill.
- **Padding:** 1 mm on all sides.
- **Separation:** a thick white separator between groups (see `styling.md`).
- **Header row:** the header-row cell above it is left empty, or labelled
  "Category" if the table is read by a screen reader.
- **Label length:** keep labels short enough to fit the height of the merged
  group. If a label won't fit, widen the column rather than shrinking the text.
