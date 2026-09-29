# Worked Examples

Three tables sized from start to finish, with the reasoning shown. Follow the
reasoning, not the numbers: different content gives different widths.

---

## Example 1: A–E analytic rubric → landscape, 27 cm

**Content:** 4 criteria (Research, Ideation, Making, Evaluation), each described
at 5 achievement levels (A–E). Each descriptor is 1–3 sentences.

**Orientation.**
- Portrait at 19 cm: the criterion column needs about 3 cm, which leaves 16 cm
  for 5 level columns, or 3.2 cm each. That is barely above the 3 cm minimum for
  sentence columns, and the descriptors would wrap to 8+ lines.
- The numeric test is met (4 or more achievement-level columns plus a criterion
  column), and students need to compare across levels. → **Landscape.**

**Width.** The criterion column needs about 6–7 cm (a name plus a short
explanation). The level columns should be equal.
- 27 cm with a 6 cm criterion column leaves 4.2 cm per level column. That is not
  a 0.5 cm step.
- Before switching to 26 cm, redistribute at 27 cm: a 7 cm criterion column
  leaves exactly 4 cm per level. The criterion text benefits from the extra
  centimetre. → **27 cm**, the preferred width.
- (26 cm = 6 + 5 × 4 would also be valid. It's the better choice only if the
  criterion text is short enough that 7 cm would leave empty space.)

**Structure: 7 + 4 + 4 + 4 + 4 + 4 = 27 cm.**

| Column | Width | Twips |
|---|---:|---:|
| Criterion | 7 cm | 3969 |
| A | 4 cm | 2268 |
| B | 4 cm | 2268 |
| C | 4 cm | 2268 |
| D | 4 cm | 2268 |
| E | 4 cm | 2268 |
| **Total** | **27 cm** | 15309 → subtract 2 from the criterion column (3967) = **15307** |

**Styling.**
- Header row: rubrics take the strong-emphasis treatment, an Accent 6 fill with
  `White Table Heading (12pt)`. It is marked as a header row and repeats on each
  page.
- Criterion cells: Pale fill with Heading 9.
- Descriptor cells: white with Normal text.

**Height check.** 4 criteria × about 3 cm, plus a 1.2 cm header, is about
13.2 cm. That fits within the roughly 16 cm available for the table body, so the
table stays on one page.

---

## Example 2: Comparing three artworks → landscape, 27 cm

**Content:** 3 artworks shown side by side. Under each: artist, and how the
artwork uses line, shape and colour. Students add their own observation in a row
at the bottom.

**Orientation.**
- Portrait at 19 cm: 3 image columns of about 6.3 cm each, not whole
  centimetres. The images would also be small once the analysis rows are added.
- The numeric test is met: 3 images compared side by side, each at 5 cm or
  wider. The comparison is the point of the task. → **Landscape.**

**Width.**
- A 1 cm vertical category column lets the rows group into "Artwork" and
  "Analysis". That leaves 26 cm (at 27 cm) or 25 cm (at 26 cm) for 3 artwork
  columns. Neither divides into whole centimetres.
- Without the vertical category column: 27 cm = 9 + 9 + 9, all whole
  centimetres. → **27 cm, 9 + 9 + 9**, with row labels as Heading 5 group rows
  instead of a vertical column.

**Structure: 9 + 9 + 9 = 27 cm** (5102 + 5102 + 5102 = 15306 → add 1 to one
column = **15307**).

**Rows.**

| Row | Content | Height |
|---|---|---|
| 1 | Images, edge-to-edge (0 padding), cropped to a common ratio, alt text on each | at least 6.6 cm |
| 2 | Artist and title (Heading 9) | — |
| 3 | Pale group row: "Line, shape and colour" (Heading 5) | — |
| 4 | Analysis text (Normal) | — |
| 5 | "Your observation" response row, white with borders | at least 3 cm |

**Height check.** 6.6 + about 1 + about 1 + about 4 + 3 is about 15.6 cm. That
is just inside the roughly 16 cm available; keep the analysis concise.

---

## Example 3: 40-term glossary → portrait, 19 cm

**Content:** 40 design terms, each with a 1–2 sentence definition and space for
students to write an example.

**Orientation.**
- 3 columns, read down the page, and long rather than wide. The numeric test is
  not met. → **Portrait.** Landscape would halve the rows per page and double the
  page count.

**Width.**
- Term column: 3.5 cm is enough for the longest term ("Asymmetrical balance")
  on two lines, but 0.5 cm steps should be justified.
- Try 4 cm for the term, 9 cm for the definition, 6 cm for the example = 19 cm.
  The example column is above the 4 cm minimum for student responses.
  → **19 cm, 4 + 9 + 6**, all whole centimetres.

**Structure: 4 + 9 + 6 = 19 cm** (2268 + 5102 + 3402 = 10772 ✓, no adjustment
needed).

**Pagination.**
- 40 rows at about 2 cm each won't fit on one page. It is a genuinely long
  table.
- Header row (Term / Definition / Your example): Pale fill with Heading 4. It
  repeats on each page, and every row has `cantSplit`.
- Split alphabetically at a letter boundary, and add a Pale group row for each
  letter (Heading 5) so the page breaks fall between groups.

**Accessibility.** Table alt text: "Glossary of 40 design terms with
definitions and a space to write your own example."
