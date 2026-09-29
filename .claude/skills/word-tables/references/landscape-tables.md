# Landscape Page Tables

This is an **extension** of the table design system, not a separate visual style.
Landscape orientation changes the available width. It does not change the
underlying design rules.

---

## Landscape page geometry

Page size: A4 landscape, 29.7 × 21 cm.

Margins depend on how the document is bound, matching the portrait rules in the
print design system:

| Binding | Margins | Usable width | Usable height |
|---|---|---:|---:|
| **Flat printout** | 1 cm on all four sides | 27.7 cm | 19 cm |
| **Saddle-stapled booklet** | 1.2 cm on all four sides | 27.3 cm | 18.6 cm |

Why 1.2 cm in a booklet: a landscape page is printed rotated on a portrait sheet.
Its left and right edges become the sheet's top and bottom (12 mm in the print
system). Its top or bottom edge lands against the spine, which needs 12 mm and
must keep text and rules at least 6 mm clear of the fold. 1.2 cm all round
satisfies every edge whichever way the page is rotated.

Keep the header and footer distances the same as the template's portrait
sections (12.5 mm).

Don't normally use the full usable width. Use:

**27 cm — preferred/default landscape table width**

or

**26 cm — alternative landscape table width**

Both fit in both bindings. Choose between them with the width rules in
`sizing.md`: keep 27 cm unless 26 cm gives a clearly cleaner structure.

---

## Preferred landscape table width

For landscape pages, try a **27 cm table first**.

27 cm suits:

- larger comparison tables;
- tables with numerous columns;
- detailed rubrics;
- wide classification tables;
- side-by-side examples;
- tables combining images and text;
- specifications;
- processes; or
- other information that benefits from additional horizontal space.

Use **26 cm** where it gives cleaner column divisions or better visual balance.

Don't use landscape just because a table is large. First decide whether the
information is genuinely easier to understand in a wider format.

---

## Landscape column widths

The same column-width rules and minimum widths as portrait apply (see
`sizing.md`).

### Examples of valid 27 cm structures

- 13.5 + 13.5 cm
- 9 + 9 + 9 cm
- 6 + 9 + 12 cm
- 5 + 7 + 15 cm
- 4 + 8 + 15 cm
- 3 + 6 + 8 + 10 cm
- 6 + 6 + 7 + 8 cm
- 4.5 + 4.5 + 6 + 6 + 6 cm
- 1 + 13 + 13 cm
- 1 + 8 + 9 + 9 cm
- 1 + 6.5 + 6.5 + 6.5 + 6.5 cm

### Examples of valid 26 cm structures

- 13 + 13 cm
- 8 + 9 + 9 cm
- 6 + 8 + 12 cm
- 5 + 7 + 14 cm
- 4 + 10 + 12 cm
- 5 + 6 + 7 + 8 cm
- 1 + 25 cm
- 1 + 5 + 10 + 10 cm
- 1 + 5 + 5 + 5 + 5 + 5 cm

These are examples only, not fixed presets. Size columns for the actual content.
A leading 1 cm column is the vertical category column (see `sizing.md`).

---

## Use the extra width strategically

Landscape gives substantially more horizontal space. That doesn't mean every
column should get wider.

The extra width can allow:

- more categories to appear side by side;
- longer descriptions to wrap over fewer lines;
- images to be displayed at a useful size;
- comparisons to stay together;
- a vertical category column to be added;
- related information to stay on the same page; or
- a complex table to become easier to scan.

Don't share the extra width equally if some columns don't need it. A short label
column can stay 2–4 cm wide while a detailed explanation column gets
substantially more space.

---

## Landscape pages are short

A landscape page gains width but loses height. Usable height is 19 cm (flat) or
18.6 cm (booklet), against 27.3 cm in portrait. After a table title
and a header row, allow roughly **16 cm for the table body**.

So a wide table fits fewer rows, and keeping the whole table on one page gets
harder. When a landscape table doesn't fit on one page, try these in order:

1. **Rebalance widths.** Give more width to the columns that wrap most, so rows
   get shorter.
2. **Tighten response space**, but only if it stays adequate for the task (see
   `styling.md`).
3. **Split at a logical boundary**, such as between category groups, never
   mid-group. Repeat the header row on the next page.
4. **Reconsider the orientation.** If the table is long rather than wide,
   portrait may suit it better.

**A single row taller than the page** can't meet "never split a row". Restructure
it: break the content into several rows, or move the long content to its own
table or section. Allow a row to split only as a last resort, and flag it for
review.

---

## Portrait and landscape use the same design system

Changing the page orientation does **not** change the table design rules. All of
these still apply:

- intentional column sizing and minimum widths;
- whole-centimetre dimensions wherever practical, with 0.5 cm steps where
  justified;
- centred table alignment;
- Heading 4 for primary table headings;
- Heading 5 for table subheadings;
- Heading 9 for minor headings and labels;
- the supplied Word template and its styles;
- the greyscale palette;
- high-contrast fills and text;
- context-sensitive border colours;
- appropriate internal and external borders, or a borderless structure where it
  works;
- thick white separators where appropriate;
- image sizing and edge-to-edge image rules;
- adequate student response space;
- no splitting of individual rows across pages;
- complete tables on one page wherever reasonably possible;
- logical pagination for genuinely long tables; and
- accessibility and readability requirements.

---

## Choosing portrait or landscape

Choose the orientation from the **information architecture**, not the amount of
content. Default to portrait.

### Numeric test: consider landscape if any of these is true at 19 cm

- A column would fall below its minimum width (see `sizing.md`).
- The table has **more than 5 content columns** (not counting a vertical
  category column).
- **3 or more images** must be compared side by side, each at 5 cm or wider.
- A rubric or matrix has **4 or more achievement-level columns** plus a
  criterion column.

Passing the test means *consider* landscape, not *use* it. Then check the
judgement criteria below.

### Prefer portrait when:

- the table works effectively at 19 cm or 18 cm;
- the information is primarily read down the page;
- there are relatively few columns;
- descriptions benefit from deeper rather than wider cells;
- the table is long rather than wide (see "Landscape pages are short");
- the table is part of a normal portrait workbooklet sequence.

### Use landscape when:

- the information has many meaningful columns;
- students need to compare several categories at the same time;
- portrait would make columns too narrow;
- images need to be compared side by side;
- a rubric or matrix needs substantial horizontal space;
- portrait would cause excessive text wrapping;
- the wider view materially improves students' understanding of relationships.

Don't switch to landscape just to avoid deciding the column widths properly.

---

## Mixed-orientation documents

Where only one or a few tables genuinely need landscape, the rest of the
workbooklet stays portrait.

Use section breaks so the landscape pages don't change the orientation or margins
of the surrounding portrait pages.

Ensure that:

- the landscape section begins cleanly on a new page;
- the table stays centred;
- page headers and footers stay consistent with the template;
- page numbering stays continuous;
- the following pages return correctly to portrait;
- section breaks don't create any blank pages; and
- for booklets, the total page count is still a multiple of 4.

See `word-implementation.md` for the mechanics.

### Landscape pages in saddle-stapled booklets

- **Keep the rotation consistent.** Every landscape page in a booklet should turn
  the same way, so students always rotate the booklet in the same direction to
  read it. Printer drivers and PDF imposition usually rotate landscape pages
  automatically. Check the direction on a printed proof.
- **Prefer right-hand (odd-numbered) pages** for a single landscape page, so the
  table sits on the more visible page of the spread. Plan the content to land it
  there. Don't force it with an odd-page section break, because that can insert
  hidden blank pages.
- **Consider a facing pair.** When two landscape tables belong together, place
  them on the two pages of one spread.
- **Proof before printing.** Word's Book fold setting applies to the whole
  document. If a landscape section doesn't print correctly with Book fold on,
  export to PDF and let the print imposition place the pages.
