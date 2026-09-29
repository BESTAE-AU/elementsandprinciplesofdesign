# House design tokens (shared)

**This file is identical in every house design skill.** Change it in one, then copy it to the others:
- `indesign-parameters`: InDesign print and slides
- `greyscale-print-design-system`: Word workbooklets and handouts
- `canvas-pages`: Canvas LMS HTML pages

It holds what all three media share. Anything medium-specific (exact type sizes, spacing, alignment,
file mechanics) stays in each skill.

## 1. Which skill for which medium

| Making… | Use | It covers |
|---|---|---|
| An InDesign document, template, poster or slide deck | **indesign-parameters** | Grid presets for A4/A3/slides, grid-locked type, object and paragraph styles, K swatches, the document builder |
| A Word document from the Greyscale Workbooklet template | **greyscale-print-design-system** | Word page setup, grid tables, named workbooklet styles, booklet printing |
| A Canvas page | **canvas-pages** | Table-based RCE HTML, domain colours, validation |

When a request spans media (e.g. "make the worksheet in InDesign and a matching Canvas page"),
use each skill for its own part and keep these tokens the same across both.

## 2. Grid (print)

A4 portrait, 12 columns × 12 rows, all whole millimetres:

| | Flat printout | Saddle-stitched booklet |
|---|---|---|
| Margins | top 12, bottom 12, left 10, right 10 | top 12, bottom 12, inside 12, outside 8 |
| Live area | 190 × 273 | 190 × 273 |
| Columns | 14 mm, 2 mm gutter | same |
| Rows | 20 mm, 3 mm gutter (rhythm unit 23 mm) | same |

Span = `n × module + (n − 1) × gutter`. Common widths: 2 across 94, 3 across 62, 4 across 46, 6 across 30, full 190.
This is **preset A of A4 portrait** in indesign-parameters. Other sizes and presets live there.

## 3. Typeface

- **Lato only** (default house font). Never substitute Aptos, Calibri, Arial or Times.
- Headings: **ALL CAPS**, typed as capitals or set with a caps style, and a **heavy weight (Lato Black)**.
- Subheadings and lead text: **Lato Light**.
- Body: **Lato Regular, 12 pt** in print (slides: 18 px minimum body, never under 16 px).
- Exact heading sizes, leading and alignment are **medium-specific**. InDesign locks them to the grid rows and left-aligns. The Word template keeps its own scale and centred headings. Canvas uses HTML defaults and inline sizes.

## 4. Contrast (all media)

| Use | Minimum |
|---|---|
| All text (house standard) | **7:1** |
| Large text (≥ 18 pt, or ≥ 14 pt bold) and secondary text, absolute floor | 4.5:1 |
| Meaningful graphics, icons, borders | 3:1 |

- **Text is always the highest-contrast colour available** on whatever it sits on. Text colour never varies to show hierarchy.
- **Never use colour or shade alone to carry meaning.** Always add a label, icon or position.
- **Print:** check greys with ink dot gain (the worse result counts). `indesign-parameters/scripts/grid.py --contrast TEXT_K BG_K` does this.

## 5. Greyscale (K steps are the source of truth)

Print uses black ink in 10% steps. Screen and Word use the hex equivalents.

| Token | Hex (screen/Word) | Text on it | Role |
|---|---|---|---|
| K 0 (Paper) | #FFFFFF | K 100 | Page |
| K 10 | #E6E6E6 | K 100 (secondary K 80) | Lowest shade; default light panel; table banding |
| K 20 | #CCCCCC | K 100 (secondary K 80) | Callouts, Key Term highlight |
| K 30 – K 60 | #B3B3B3 · #999999 · #808080 · #666666 | **No text** | Graphics only: bars, icons, chart fills, placeholders, borders (K 50+ for meaningful lines) |
| K 70 | #4D4D4D | White | Panel |
| K 80 | #333333 | White | Panel; **secondary text colour** (captions, footnotes) on light backgrounds |
| K 90 | #1A1A1A | White | Highest shade; table header rows |
| K 100 | #000000 | White | Body and heading text; **small, very important accents only** as a fill |

- Most things have **no background**. Shading is optional emphasis, running from K 90 (highest) to K 10 (lowest).
- **Reversed (white) text:** only on K 70–100. At least 12 pt Regular or 10 pt Bold, never in Light or Thin weights.
- **Photocopied resources:** K 10 may disappear, so use K 20 for light panels.

Old Word-template greys and their replacements:

| Old | Was | Now |
|---|---|---|
| Pale #CACBCA | Block text, module fills | K 20 #CCCCCC |
| Accent 1 #969896 / Accent 2 #878785 | Light table shading | K 40 / K 50 (graphics only; no text) |
| Accent 3 #767776 | Shading | K 60 (graphics only) |
| Accent 4 #585958 / Accent 5 #494A49 | Dark fills with white text | K 70 #4D4D4D |
| Accent 6 #383938 | Darkest table shading | K 80 #333333 (or K 90 for table headers) |
| Muted #5E5E5E | Captions, references | **K 80 #333333** (the old value is only 6.5:1) |
| Link #5E5E5E (was #898A89) | Hyperlinks | **K 100, underlined** |

## 6. Domain colours (colour print, slides and Canvas)

Colour is chosen by the **learning domain** of the content. Each domain has three colours:
- **H**, the accent: banners, divider bars, left borders, pill labels, highlights
- **S**, the shade: strong borders, dark blocks, heading treatments
- **T**, the tint: soft panels and table backgrounds

| Domain | Slug | H | S | T |
|---|---|---|---|---|
| Critical Thinking | `critical-thinking` | TOMATO #FF585D | ESPRESSO #551C25 | SOFT BLUSH #F5DADF |
| Creative Thinking, Problem Solving and Innovation | `creative-thinking-problem-solving-and-innovation` | ROYAL ORANGE #F19C49 | DARK LEATHER #4F2C1D | APRICOT #FFDFB4 |
| Communication | `communication` | CORN #F3EA5D | DARK GOLD #8A6400 | BUTTERMILK #F7F4A2 |
| Self-Management and Organisation | `self-management-and-organisation` | LIME #C5E86C | ZUCCHINI #1C4220 | LIME CREAM #E8F6C4 |
| Responsibility and Stewardship | `responsibility-and-stewardship` | SEAGREEN #00B2A2 | SHERWOOD #024638 | SWANS DOWN #D7EFE7 |
| Practical Skills and Technical Application | `practical-skills-and-technical-application` | DENIM #326295 | NIGHT #041E42 | CRUSHED ICE #D2DCE8 |
| Knowledge and Conceptual Understanding | `knowledge-and-conceptual-understanding` | TWILIGHT #514689 | DARK INDIGO #201547 | PERIWINKLE #DCD3E7 |
| Independent Learning and Collaboration | `independent-learning-and-collaboration` | VALENTINE PINK #E56DB1 | PLUM #621244 | POWDER PINK #F7D0E6 |

Unmapped groups (use only if the user gives a domain for them): 1H JAZZBERRY #AC145A, 1S MULBERRY #651C32,
1T PIGGY PINK #EEDAEA; 7H BONDI BLUE #007F98 (white text, 4.7:1), 7S CYPRUS #003540, 7T MYSTIC #DCEBEC.

### Text colour on each domain colour (WCAG, sRGB)

The highest-contrast text colour for every swatch:

| Swatch | Text | Ratio | Allowed |
|---|---|---|---|
| **All T tints** | black | 14.5–18.4 | All text ✓ |
| ESPRESSO, DARK LEATHER, ZUCCHINI, SHERWOOD, NIGHT, DARK INDIGO, PLUM (S) | white | 10.8–16.7 | All text ✓ |
| **DARK GOLD (Communication S)** | white | **5.4** | Large text and graphics only (headers, banners, bold labels). Replaced MUSTARD #CFB500 on 29 Sept 2026, which was too light to act as a shade |
| CORN, LIME, ROYAL ORANGE, SEAGREEN, VALENTINE PINK (H) | black | 7.2–16.7 | All text ✓ |
| TWILIGHT (Knowledge H) | white | 8.1 | All text ✓ |
| **TOMATO (Critical Thinking H)** | black | **6.8** | Large text and graphics only |
| **DENIM (Practical Skills H)** | white | **6.3** | Large text and graphics only |

- Neutral text for web and slides: #222222 (15.9:1) or #333333 (12.6:1) on white or T tints. #555555 (7.5:1) only for secondary text.
- **Print:** these are screen (sRGB) colours. For colour printing, convert through the document's CMYK profile and check the proof. If the school has official CMYK or Pantone values for these colours, those override the conversion.
- **Photocopying:** domain colours collapse to greys. Anything that must survive a mono photocopy needs its meaning carried by a label, icon or position.
