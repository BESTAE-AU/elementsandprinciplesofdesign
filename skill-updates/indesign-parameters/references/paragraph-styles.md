# Paragraph and character style library

Rules for every style beyond the headings and body styles in SKILL.md section 7. Numbers change
with size and preset, so never copy them from memory. Generate the full sheet:

```
python3 scripts/grid.py --sheet A4P A            # add --font NAME for a non-default font
```

All sizes and leading are whole numbers or 1 decimal and lock to the rows, using the same method
as body text (SKILL.md section 7). Examples below are A4 portrait, Lato.

## Contents
1. Housekeeping (applies to every style)
2. Lists
3. Supporting text
4. Worksheet
5. Page furniture
6. Character styles
7. Not yet defined

---

## 1. Housekeeping

| Rule | Setting | Why |
|---|---|---|
| **Based On chain** | [Basic Paragraph] → **Body** → every body-type style. [Basic Paragraph] → **Heading base** → Title, Subheading, Heading 1–5. | Change the font or colour once in the base and every style follows. |
| **Alignment** | Left aligned (ragged right) everywhere. Never justified. | Even word spacing, easier reading. |
| **Hyphenation** | Off for every style | Whole words read more easily. School resources especially. |
| **Next Style** | Title → Subheading → Body; Heading 1–5 → Body; Label → Heading 3; Bullet → Bullet; Question → Answer Line | Typing flows naturally from one style into the next. |
| **Keep Options** | Headings, Label, Question: **Keep with Next 1 line**. Body-type styles: **Keep Lines Together**, at least 2 lines at start and end. | No stranded headings, widows or orphans. |
| **Balance Ragged Lines** | On for headings, Lead and Pull Quote | Even line lengths in short, large text. |
| **Align to Grid** | None | The leading does the locking. A baseline grid would fight it. |
| **Style groups** | Headings · Body · Lists · Supporting · Worksheet · Page | Easy to find in the panel. Mirrors the object style folders. |

## 2. Lists (group: Lists)

Lists take their size and leading from the Body styles, so they lock to the rows automatically.
Indents are whole mm (whole px on slides).

**Spacing:** Space After = one line (the style's leading), but **Space Between Paragraphs Using
Same Style = 0**. Items sit tight together, with exactly one blank line after the list.

| Style | Based on | Size / leading (A4P) | Left indent | First line | Tab | Marker |
|---|---|---|---|---|---|---|
| **Bullet** | Body | 12 / 16.3 pt | 5 mm | −5 mm | 5 mm | • |
| **Bullet Level 2** | Bullet | 12 / 16.3 pt | 10 mm | −5 mm | 10 mm | – (en dash) |
| **Numbered** | Body | 12 / 16.3 pt | 7 mm | −7 mm | 7 mm | 1. 2. 3. |
| **Numbered Level 2** | Numbered | 12 / 16.3 pt | 14 mm | −7 mm | 14 mm | a. b. c. |
| **Bullet Condensed** | Body Condensed | 12 / 14.5 pt | 5 mm | −5 mm | 5 mm | • |
| **Numbered Condensed** | Body Condensed | 12 / 14.5 pt | 7 mm | −7 mm | 7 mm | 1. 2. 3. |
| **Checklist** | Bullet | 12 / 16.3 pt | 7 mm | −7 mm | 7 mm | □ (U+25A1, in Lato) |
| **Step** | Numbered | 12 / 16.3 pt | 1 column + gutter (16 mm) | −16 mm | 16 mm | "Step 1" (numbering `Step ^#^t`, Step Label character style) |
| **Definition** | Body | 12 / 16.3 pt | 2 columns + gutters (32 mm) | −32 mm | 32 mm | Term in Bold, then a tab. Nested style: Bold through 1 Tab. |

- **Numbering restarts** after any heading: Restart Numbers at This Level After Any Previous Level, with headings in the same list.
- **Step and Definition indents are column positions**, so the text column lines up with a grid column. The calculator gives the value for each size.
- **Checklist:** use □, which Lato has. It lacks ☐ and ✓. With another font, check the glyph exists before using it.
- **Slides:** bullet indent 20 px (Level 2: 40 px), numbered indent 30 px (Level 2: 60 px).

## 3. Supporting text (group: Supporting)

| Style | Font | Size / leading (A4P) | Case / tracking | Use |
|---|---|---|---|---|
| **Lead** | Light | 16 / 21.7 pt (3 lines per row) | Sentence case | Opening paragraph under a Title or Heading 1 |
| **Caption** | Light | 10 / 14.5 pt (Body Small) | Sentence case | Under images, same column span, top on the row line below the image |
| **Label** | Heavy (Lato Black) | 10 / 14.5 pt | ALL CAPS, tracking +100 | Eyebrow above headings: "ACTIVITY 1", "WEEK 3" |
| **Pull Quote** | Light Italic | 24 / 32.6 pt (2 lines per row) | Sentence case | Quotes and key statements |
| **Block Quote** | Italic | 12 / 16.3 pt, left indent 1 column + gutter (16 mm) | Sentence case | Longer quoted passages. The indent lines up with column 2. |
| **Footnote** | Regular | 10 / 14.5 pt | Sentence case | References, sources, image credits |

- **Lead and Pull Quote are short text**, so their rounding drift is checked over 4 rows rather than a full page. The rule is otherwise the same as body text.
- **Pull Quote is sized like body text, not by cap height.** It's in sentence case, so descenders need real space between lines. Using a heading's cap-height fit would make the lines collide.
- **Slides:** Lead 24 / 30 px, Pull Quote 36 / 45 px.

## 4. Worksheet (group: Worksheet, print only)

| Style | Settings |
|---|---|
| **Learning Intention** / **Success Criteria** | Label style text. The items below use Checklist. |
| **Question** | Based on Numbered. Bold, Body size and leading. A **right indent tab** (Shift+Tab) pushes marks to the frame's right edge. Keep with Next. Next Style: Answer Line. |
| **Question Part** | Based on Numbered Level 2. Regular, format (a) (b) (c), right indent tab for marks |
| **Instruction** | Based on Body. Italic, e.g. "Read the extract, then answer questions 1–4." |
| **Answer Line** | Empty paragraph with **Paragraph Rule Below**: 0.5 pt, **solid black**, width Column, offset 0 (the rule sits on the baseline). Leading = answer line spacing. |

**Answer Lines object style** (Worksheet folder): like Text – Grid, but **First Baseline = Leading**. The first rule then sits one full line below the frame top, and every rule falls on the answer grid. Place the answer frame on the row after its question.

**How many lines:** an answer area of *n* rows holds **(lines per row × n) − 1** lines, e.g. 3 lines in 2 rows on A4 portrait. The last line sits inside the area and the next question starts clear of it. With a full (lines per row × n), the last rule lands exactly on the next question's row line.

**Answer line spacing** is the row pitch divided by *n*. Pick the spacing closest to 10 mm, within 8–12 mm and the 0.25 mm drift rule, so answer space is always a whole number of rows:

| Size | Spacing | Leading |
|---|---|---|
| A4 portrait | 11.5 mm, 2 per row | 32.6 pt |
| A4 landscape | 8 mm, 2 per row | 22.7 pt |
| A3 portrait | 8.5 mm, 4 per row | 24.1 pt |
| A3 landscape A/B | 11.5 mm, 2 per row | 32.6 pt |
| A3 landscape C/D | 12 mm, 2 per row | 34 pt |

## 5. Page furniture (group: Page, parent pages only)

| Style | Settings | Position |
|---|---|---|
| **Page Number** | Bold, Body Small size and leading | Bottom margin, at the outside edge of the live area (right on single sheets, outside on spreads) |
| **Running Footer** | Regular, Body Small size and leading | Bottom margin, at the left/inside edge of the live area |

These are the only items allowed outside the grid, in the margin. Their frames are vertically
centred in the bottom margin, and they still use zero inset and Cap Height.

## 6. Character styles

| Style | Settings |
|---|---|
| **Bold** | Font's Bold weight |
| **Italic** | Font's Italic |
| **Key Term** | Bold + colour (colour to be set with the colour system) |
| **Link** | Underline 0.5 pt, offset 1.5 pt |
| **Marks** | Regular, Body Small size, e.g. "(2 marks)" |
| **Step Label** | Bold, used by Step numbering |

Never apply manual formatting. Use a character style so it updates with the system.

## 7. Colour, reversed styles and tables

Colour rules are in `references/colour.md`. For paragraph and character styles:
- **Text colour** is K 100 in every style. Caption, Footnote and Running Footer are K 80 (secondary text).
- **Key Term:** Bold, K 100, on a K 20 highlight made with an underline: Underline On, weight = type size + 1, offset ≈ −0.3 × size, colour K 20 (for 12 pt: 13 pt weight, −3.6 pt offset). Check the highlight once by eye in the chosen font and adjust the offset in 0.1 pt steps if it sits high or low.
- **Reversed variants:** for text on K 70–100 panels, add `– Reversed` versions (colour [Paper]) of the styles allowed white. Group them in a *Reversed* style group. Never reverse Light/Thin styles (Subheading, Lead, Caption, Pull Quote), and nothing under 12 pt Regular or 10 pt Bold.
- **Table Header / Table Body** paragraph styles and the table cell styles are in colour.md section 6. `--sheet` prints their values.
