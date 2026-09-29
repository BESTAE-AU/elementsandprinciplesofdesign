---
name: word-tables
description: Table design system for Word (.docx) workbooklets — modular table widths, intentional column sizing, heading styles, borders, images, pagination and accessibility, for both A4 portrait and A4 landscape pages. Use whenever creating, formatting or checking a table in a Word document or workbooklet, choosing table or column widths, or deciding whether a table should sit on a landscape page.
---

# Word Tables

This skill defines one table design system for Word workbooklets. It applies to
every table, on every page, in every orientation.

## The one rule to remember

**Portrait = 19 / 18 cm. Landscape = 27 / 26 cm.** Everything else in the table
system carries across unchanged.

| Page orientation | Preferred width | Alternative width |
|---|---:|---:|
| **A4 Portrait** | **19 cm** | **18 cm** |
| **A4 Landscape** | **27 cm** | **26 cm** |

These widths set the working grid for the table. Within that grid, divide
columns according to the **type, quantity and relationship of the information**.
Don't default to equal columns.

Orientation changes the available width. It does **not** change the design
system.

## Core design system (applies in all orientations)

- Intentional column sizing. Columns reflect the amount and function of their
  content and do not need to be equal.
- Whole-centimetre column widths wherever practical. Use 0.5 cm increments only
  where they produce a better structure. Avoid arbitrary decimal widths.
- Column widths must add up exactly to the intended table width.
- Centred table alignment.
- Heading 4 for primary table headings.
- Heading 5 for table subheadings.
- Heading 9 for minor headings and labels.
- Use the supplied Word template and its styles.
- Use the established document colour palette.
- High-contrast fills and text.
- Border colours that suit the context.
- Suitable internal and external borders. Borderless structures are allowed where
  they work.
- Thick white separators where appropriate.
- Follow the image sizing and edge-to-edge image rules.
- Leave enough student response space.
- Never split an individual row across pages.
- Keep a complete table on one page wherever reasonably possible.
- Paginate genuinely long tables logically.
- Meet accessibility and readability requirements.

## Reference files

Load the file that matches the task:

- `references/landscape-tables.md`: sections 60–66. Landscape page geometry,
  27/26 cm widths, landscape column structures, how to use the extra width,
  choosing portrait or landscape, and mixed-orientation documents. **Read this
  before putting any table on a landscape page, or when deciding whether a
  table should be landscape.**
- `references/word-implementation.md`: exact OOXML / twip values for page size,
  margins, table and column widths, and section breaks for mixed-orientation
  documents. Read this when writing or editing the .docx itself.

## Workflow

1. Decide the orientation from the **information architecture**, not the amount
   of content (see `references/landscape-tables.md` §65). Default to portrait.
2. Try the preferred width first (19 cm portrait, 27 cm landscape). Use the
   alternative (18 cm / 26 cm) where it gives cleaner column divisions or better
   balance.
3. Size each column for its content. Check that the widths add up to the table
   width.
4. Apply the core design system above. It is identical in both orientations.
5. For a landscape table in a portrait document, isolate it in its own section
   (see `references/word-implementation.md`). Then check headers, footers, page
   numbering, the return to portrait, and that no blank pages were created.
