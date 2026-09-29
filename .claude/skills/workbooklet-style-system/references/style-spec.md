# Style Specification

The master specification for every style. Greyscale and Bestae templates must
both match it exactly. Only the colour-layer tokens in the "Colour" column change
between them.

Units:
- Type sizes are in points.
- Spacing is in millimetres, with Word twips in brackets (1 mm ≈ 56.7 twips).
- In Word's `styles.xml`, `w:sz` is in **half-points** (78 pt = `156`).

## Document defaults

| Setting | Value |
|---|---|
| Theme fonts (heading and body) | **Lato / Lato** (not Aptos, Montserrat or Open Sans) |
| Default font | Lato 12 pt |
| Language | English (Australia) |
| Default paragraph spacing | 0 before, 3.5 mm (200) after, line spacing 1.15 (276, auto) |
| Theme colour set | The chosen colour layer (see `colour-layers.md`), with `dk1` = black and `lt1` = white in **both** layers |

## Headings

All headings use:
- **ALL CAPS**, applied through the style's capitals setting so the typed text
  stays in sentence case;
- colour **Text 1 (black)**;
- no hyphenation;
- 0 mm space before and 3.5 mm (200) after, unless stated otherwise;
- "keep lines together" on.

| Style | styleId | Font | Size | `w:sz` | Align | Line spacing | Keep with next | Outline level |
|---|---|---|---:|---:|---|---|---|---|
| Title | `Title` | Lato Bold | 78 | 156 | Centre | Single | Yes | Body text |
| Subtitle | `Subtitle` | Lato Light | 33 | 66 | Centre | 1.15 | Yes | Body text |
| Heading 1 | `Heading1` | Lato Black | 52 | 104 | Centre | Single | Yes | 1 |
| Heading 2 | `Heading2` | Lato Bold | 36 | 72 | Centre | Single | Yes | 2 |
| Heading 3 | `Heading3` | Lato Light | 20 | 40 | Centre | 1.15 | Yes | 3 |
| Heading 4 | `Heading4` | Lato Black | 16 | 32 | Centre | 1.15 | Yes | 4 |
| Heading 5 | `Heading5` | Lato Black | 12 | 24 | Centre | 1.15 | Yes | 5 |
| Heading 6 | `Heading6` | Lato Light | 16 | 32 | Centre | 1.15 | No | 6 |
| Heading 7 | `Heading7` | Lato Medium | 12 | 24 | Centre | Single | No | 7 |
| Heading 8 | `Heading8` | Lato Heavy | 10 | 20 | **Left** | 1.15 | Yes | 8 |
| Heading 9 | `Heading9` | Lato Heavy | 10 | 20 | Centre | 1.15 | No | 9 |

Font names are the actual Lato family members ("Lato Black", "Lato Heavy", "Lato
Light", "Lato Medium"). They are **not** "Lato" plus Word's bold button. The one
exception is Title and Heading 2, which use "Lato" with bold (Lato Bold).

### What each level is for

Choose the level by role. These examples come from the existing booklets.

| Level | Role | Examples |
|---|---|---|
| Title | Booklet or phase name, cover only, once per document | IDENTIFY · INSPIRATION · DEVELOP |
| Subtitle | Cover details | ASSESSMENT TASK 2 · STUDENT NAME · CLASS: |
| Heading 1 | Subject on the cover; a major divider, such as a TASK banner | MULTIMEDIA · TEXTILES · TASK |
| Heading 2 | Booklet section, usually starting a new page | SEMESTER 2 · WORKBOOKLET 1 · CHOOSE YOUR DESIGN SITUATION · STATEMENT OF INTENT · MARKING CRITERIA |
| Heading 3 | Opening or sub-section inside a section | WHAT YOU NEED TO KNOW · HISTORICAL, CULTURAL AND CONTEMPORARY |
| Heading 4 | An activity or task students complete; a table's header row | 1. INSPIRATION STATEMENT · UNPACK THE SITUATION · IDENTIFY YOUR TARGET MARKET |
| Heading 5 | A step or part inside an activity; table subheadings | STEP 1: IDENTIFY THE END USE · DESCRIBE YOUR TARGET MARKET · USEFUL SENTENCE STARTERS: |
| Heading 6 | Lighter category label | BLUE · ORANGE · AQUA |
| Heading 7 | Small callout heading on a light fill | (on a dark fill, use `White Table Heading (12pt)`) |
| Heading 8 | Prompt label above student writing space | MY TARGET MARKET NEEDS: · THEY NEED THIS BECAUSE: · TIPS: |
| Heading 9 | Labels inside tables | WHO · WHAT · WHEN · A SAFER WORLD FOR ALL |

### Lesson and program documents (Bestae lessons)

Lesson documents use the same levels, mapped by role:

| Lesson element | Style |
|---|---|
| Lesson heading | Heading 2 |
| Lesson goal / lesson focus labels | Heading 5 |
| Question section (MULTIPLE CHOICE, SHORT RESPONSE) | Heading 3 |
| Topic or outcome heading within a section | Heading 4 |
| Marking criteria | Heading 2 (new section) |
| Activity or task heading inside a lesson table | Heading 4 (or `White Table Heading (12pt)` on a dark fill) |

## White headings for dark fills

Use these only on fills that pass the contrast rule in `colour-layers.md`. They
replace the current practice of recolouring Heading 1 or Heading 7 white by hand.

| Style | Based on | Font | Size | Colour | Use |
|---|---|---|---:|---|---|
| `Heading 1 White` | Heading 1 | Lato Black | 52 | Background 1 (white) | TASK banners and other full-width dark banners. Keeps outline level 1, so it appears in navigation |
| `White Table Heading (12pt)` | — | Lato Bold | 12 | Background 1 (white) | Headings inside dark-filled table cells; the header row of rubrics |

## Body and workbooklet styles

| Style | Font | Size | Spacing and layout | Notes |
|---|---|---:|---|---|
| **Normal** | Lato | 12 | 0 before, 3.5 mm (200) after, line spacing 1.15 (276), left | Body text |
| **Table Text** | Lato | 12 | 0 before and after, single line, left | Body text inside table cells, so cells don't pick up paragraph spacing |
| **List Bullet** | Lato | 12 | Hanging bullet, 1 mm (57) after | Bulleted lists |
| **Caption** | Lato Italic | 10 | 0 before, 2 mm after | Colour: Muted `#5E5E5E` in both layers |
| **2. Question Format** | Lato | 12 | 8.5 mm (480) before, 0 after, 7 mm (397) hanging indent | Numbered question stem |
| **3. Multiple Choice Answers Format** | Lato | 12 | 2.1 mm (120) before and after, 6 mm (340) indent | A–D options |
| **4. Marks** | Lato Bold, CAPS | 18 | Right-aligned, 0 before, 3.5 mm after | Mark allocation (/3) |
| **Writing Lines** | Lato | 14 | Line spacing 1.5 (360), 2 mm (113) left/right mirrored indent, 1.5 pt bottom and between borders | Student writing space. About 3 lines per mark |
| **5. Writing Lines** | Lato | 14 | As Writing Lines, plus 1 mm (60) before | Writing lines directly under a question |
| **Possible Answers** | Lato Bold | 12 | 2.1 mm before and after, fill: Light token | Teacher answer key |
| **Example Response** | Lato Semibold | 12 | 2.1 mm before and after, fill: Dark token, white text | Model answer shown to students |

### Renamed Bestae styles

Rename these Bestae styles to the shared names above, so the two templates have
exactly one name per job:

| Bestae name today | Shared name |
|---|---|
| Question Format | 2. Question Format |
| Multiple Choice Answers Format | 3. Multiple Choice Answers Format |
| Allocated Marks Formatting | 4. Marks |
| Table Paragraph | Table Text |
| Writing Lines (line spacing 2.0) | Writing Lines (line spacing 1.5) |

Bestae-only content styles (MAGIS VALUES, Magis Approach, Marist Values, THE THREE
VIOLETS, Activities, Resources and the 1H–10T colour swatch styles) stay in the
Bestae template, but must be built on the shared styles (Lato, the same sizes as
the level they sit at).

## Table styles

| Table style | Borders | Header row | Body | Use |
|---|---|---|---|---|
| **Table 2** | 0.5 pt, Dark token, all borders | Heading 4 on the Light token (default), or `White Table Heading (12pt)` on the Dark token | Table Text, vertically centred | Default information and response tables |
| **MARKING CRITERIA** | 0.5 pt, Text 1 (black), all borders | Lato Black 12 CAPS, centred, on the Pale token | Table Text | Rubrics: MARKS \| CRITERIA |

Table widths, column sizing, padding and pagination come from the `word-tables`
skill.
