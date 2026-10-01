# Design System Knowledge: Workbooklets, Tables and Branding

*Project knowledge for Britt's teaching projects (Multimedia, Textiles, Graphics,
D&T, Visual Arts and others). Last updated 1 October 2026. It summarises the
decisions made while building the `word-tables` and `workbooklet-style-system`
skills, so every project applies the same rules.*

---

## 1. Which skill does what

| Job | Skill |
|---|---|
| Headings, paragraph styles, fonts, colour layers (Greyscale / Bestae), page setup, 12 × 12 grid, booklet printing | `workbooklet-style-system` (replaces the retired `greyscale-print-design-system`) |
| Any table in Word: widths, columns, portrait or landscape, fills, borders, response space, pagination, accessibility | `word-tables` |
| InDesign grid presets, text frames, object styles | `indesign-parameters` |
| What goes *in* a booklet (sequence, activities) | `content-booklet-builder` / `practical-skill-builder`, then the two skills above for layout |
| Rubric content | `marking-rubric-builder`, then `word-tables` sizes the table |

---

## 2. The core rules in one page

### Headings: the same in Greyscale and Bestae

All headings are Lato, ALL CAPS, black and centred, except Heading 8, which is
left-aligned. Choose a heading by its **role**, never by how it looks.

| Style | Font / size | Role |
|---|---|---|
| Title | Lato Bold 78 | Cover: booklet or phase name (IDENTIFY) |
| Subtitle | Lato Light 33 | Cover: task line, STUDENT NAME, CLASS |
| Heading 1 | Lato Black 52 | Subject on the cover; TASK banners |
| Heading 2 | Lato Bold 36 | Booklet section; lesson title |
| Heading 3 | Lato Light 20 | Opening or sub-section |
| Heading 4 | Lato Black 16 | Activity or task; **table header row** |
| Heading 5 | Lato Black 12 | Step inside an activity; **table subheadings** |
| Heading 6 | Lato Light 16 | Lighter category label |
| Heading 7 | Lato Medium 12 | Small callout on a light fill |
| Heading 8 | Lato Heavy 10, left | Prompt label above writing lines |
| Heading 9 | Lato Heavy 10 | **Labels inside tables** |

- On dark fills, use `Heading 1 White` or `White Table Heading (12pt)`. Never
  recolour a heading by hand.
- Shared body styles:
  - Normal (Lato 12);
  - Table Text;
  - 2. Question Format;
  - 3. Multiple Choice Answers Format;
  - 4. Marks;
  - Writing Lines / 5. Writing Lines (line spacing 1.5, about 3 lines per mark);
  - Possible Answers;
  - Example Response;
  - Caption.
- Theme fonts must be **Lato / Lato**. No Aptos, Montserrat, Open Sans or Gotham.

### Colour: two interchangeable layers

Colour only goes on fills, banners and borders, never on heading text. Fills use
**Word theme colours**, so a document switches layer in one click (Design →
Colours).

| Role | Greyscale | Bestae (domain colour *n*) | Word theme slot |
|---|---|---|---|
| Light (label cells, default header row) | `#E3E4E3` | Tint *n*T | Background 2 |
| Pale (group rows) | `#CACBCA` | Tint *n*T | Accent 1 |
| Accent (bars and rules only) | `#767776` | Main *n*H | Accent 4 |
| Dark (dark header rows, borders) | `#4C4D4C` | Shadow *n*S | Accent 6 |
| Darkest (banners) | `#343433` | Shadow *n*S | Text 2 |

- **Contrast:**
  - White text goes only on Dark or Darkest.
  - Mustard (4S) is the exception: it needs **black** text.
  - On the Main colours, white text works only on 1 Jazzberry, 8 Denim and
    9 Twilight; all the others need black.
- **Bestae domains:**

  | # | Domain | Colour |
  |---|---|---|
  | 1 | Brand / default | Jazzberry |
  | 2 | Critical Thinking | Tomato |
  | 3 | Creative Thinking | Royal Orange |
  | 4 | Communication | Corn |
  | 5 | Self-Management | Lime |
  | 6 | Responsibility & Stewardship | Seagreen |
  | 7 | (unassigned) | Bondi Blue |
  | 8 | Practical Skills | Denim |
  | 9 | Knowledge | Twilight |
  | 10 | Independent Learning | Valentine Pink |

  Use one domain colour per document.

### Page and grid

- A4. Booklet margins 12 / 12 / 12 inside / 8 outside mm; flat printout
  12 / 12 / 10 / 10 mm. Both give a 190 × 273 mm content area.
- 12 × 12 grid: 14 mm columns with 2 mm gutters, 20 mm rows with 3 mm gutters.
- Booklets:
  - page count is a multiple of 4;
  - nothing within 6 mm of the fold;
  - page numbers go in the outside-bottom corner;
  - switch on Book fold before printing.

### Tables

- **The one rule: portrait = 19 / 18 cm, landscape = 27 / 26 cm.** Use the
  preferred width (19 or 27) unless the alternative is clearly cleaner.
  9.5 + 9.5 cm is a valid 19 cm table.
- **Columns:**
  - whole centimetres, or 0.5 cm steps where justified;
  - sized for their content, not equal by default;
  - must add up exactly to the table width.
- **Minimum column widths:**

  | Column content | Minimum |
  |---|---:|
  | Rotated category label | 1 cm |
  | Numbers | 1.5 cm |
  | Short labels | 2.5 cm |
  | Sentences | 3 cm |
  | Student responses, images | 4 cm |

- **Choosing landscape:** use it for information architecture, not size.
  Consider it when, at 19 cm:
  - a column would drop below its minimum;
  - there are more than 5 content columns;
  - 3 or more images are compared side by side; or
  - a rubric has 4 or more grade columns.

  Long tables stay portrait.
- **Landscape pages:** 1 cm margins (flat) or 1.2 cm (booklet), about 16 cm of
  height for the table body. Put the landscape table in its own section, keep
  page numbering continuous, and avoid blank pages.
- **Every table:**
  - centred, with AutoFit off;
  - header row repeats on each page;
  - rows never split across pages;
  - alt text on the table and its images;
  - response rows use minimum ("at least") heights;
  - text no smaller than 10 pt.
- **Rubrics:** A–E analytic rubrics are landscape, 27 cm = 7 + 4 + 4 + 4 + 4 + 4.
  The marks + criteria rubric is portrait, 3 + 16 cm, in the `MARKING CRITERIA`
  table style.

---

## 3. Decisions made and why

| Decision | Reason |
|---|---|
| Greyscale booklet sizes (78 / 52 / 36 …) became the shared heading scale | Already used by the real booklets and the InDesign file. The Bestae kit was the odd one out |
| Bestae lesson headings move from Heading 1 to Heading 2 | Heading 1 is now 52 pt, too big for every lesson heading |
| Colour as a layer on theme slots | The booklets already fill with Background 2 / Accent 6 / Text 2, so Bestae can be swapped in without restyling |
| Greys taken from the real "Greyscale for Printing" theme | The old print skill listed out-of-date greys (`#969896`…`#383938`) |
| Heading 4 / 5 / 9 used inside tables | Matches how the booklets already use them |
| "Gracedale design system" taken to mean **Greyscale** | Nothing called Gracedale exists in Drive (probably a voice-typing slip) |

---

## 4. Open items and known conflicts

- [ ] **InDesign headings.** `workbooklet-style-system` (adobe.md) says InDesign
      copies the Word heading sizes, centred. `indesign-parameters` says InDesign
      headings are left-aligned with their own grid-locked scale. Decide which
      wins, then update the other skill.
- [ ] **Templates not built yet.** The next step is `Workbooklet – Greyscale.dotx`
      and `Workbooklet – Bestae.dotx`, with all ten domain colour sets.
- [ ] **Fix the Bestae Word theme.** It currently makes Text 1 Jazzberry and
      Background 1 Tomato.
- [ ] **Fix the InDesign booklet file** (Untitled-2):
  - Basic Paragraph is Minion Pro and justified;
  - Heading 3 is Lato Bold 24;
  - Heading 4 is Lato Bold;
  - Heading 5–9 are missing.
- [ ] **Clean up the existing booklets:**
  - change theme fonts from Aptos to Lato;
  - replace hand-coloured white headings with the white styles;
  - the Multimedia Workbook uses Gotham Book.
- [ ] **Not yet checked in real Word:**
  - landscape section breaks (blank pages, page numbering);
  - the Bestae theme swap.

---

## 5. Where things live

- **Skills (source):** GitHub `bestae-au/elementsandprinciplesofdesign`, branch
  `claude/wizardly-clarke-ck85ei`, in `.claude/skills/`. The installed claude.ai
  versions are newer (they include the merged print-layout file).
- **Google Drive, Style Kits:Branding folder:**
  - Bestae Word Style Kit3.docx;
  - Bestae Template.pptx;
  - MCCNS Word Style Kit.docx.
- **Reference booklets (Greyscale):**
  - Identify Booklet.docx;
  - Develop Booklet.docx;
  - Design Inspiration Booklet.docx.
- **Bestae-style workbook:** MULTIMEDIA WORKBOOK.docx.
- **InDesign:** Untitled-2.idml / .indd (A4 facing pages, 12 columns, 2 mm
  gutter, 12 / 12 / 12 / 8 mm margins); Timeline Booklet Printout Planning.indd.
- **Teaching notes on grids:** Notes - Grid Systems - Layout.docx.
