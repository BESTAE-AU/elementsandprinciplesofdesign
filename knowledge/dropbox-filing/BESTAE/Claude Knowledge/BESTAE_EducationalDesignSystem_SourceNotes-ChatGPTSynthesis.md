# BESTAE educational design system

> Source: ChatGPT knowledge collection (topic 38), imported and trimmed on 1 October 2026. Per-element boilerplate is removed because the element-of-design skills cover it. Treat as reference notes: check claims against current syllabus, policy and manufacturer documentation before use.

## BESTAE identity and educational purpose

BESTAE is the user's education brand, supporting student and teacher resources, planning, presentations, communications and reusable visual systems. Tone is polished, approachable, practical and professional. Student wording should be clear and encouraging; teacher resources should be structured and adaptable.

Do not invent programmes, policies, accreditation, prices, testimonials or claims of guaranteed results. Brand rules support communication; they do not themselves establish learning quality or accessibility.

## Authoritative palette from the BESTAE plugin

H colours provide stronger accents, S colours deep/supporting tones and T colours soft backgrounds. The following names and values reproduce the supplied brand system.

| Group | H colour | HEX | S colour | HEX | T colour | HEX |
|---|---|---|---|---|---|---|
| 1 | Jazzberry | #AC145A | Mulberry | #651C32 | Piggy Pink | #EEDAEA |
| 2 | Tomato | #FF585D | Espresso | #551C25 | Soft Blush | #F5DADF |
| 3 | Royal Orange | #F19C49 | Dark Leather | #4F2C1D | Apricot | #FFDFB4 |
| 4 | Corn | #F3EA5D | Mustard | #CFB500 | Buttermilk | #F7F4A2 |
| 5 | Lime | #C5E86C | Zucchini | #1C4220 | Lime Cream | #EFF4A4 |
| 6 | Seagreen | #00B2A2 | Sherwood | #024638 | Swans Down | #D7EFE7 |
| 7 | Bondi Blue | #008EAA | Cyprus | #003540 | Mystic | #DCEBEC |
| 8 | Denim | #326295 | Night | #041E42 | Crushed Ice | #D5EBEE |
| 9 | Twilight | #514689 | Dark Indigo | #201547 | Periwinkle | #DCD3E7 |
| 10 | Valentine Pink | #E56DB1 | Plum | #621244 | Powder Pink | #F2DEE9 |

The name “Crushed Ice” identifies the supplied 8T colour #D5EBEE; do not substitute a different colour found under that name elsewhere.

## Domain mapping

| Domain | Group | Typical learning |
|---|---|---|
| Critical thinking | 2 | Analyse, evaluate, compare, justify |
| Creative thinking, problem-solving and innovation | 3 | Generate, experiment, prototype, refine |
| Communication | 4 | Explain, annotate, document, present |
| Self-management and organisation | 5 | Plan, manage time/resources, follow procedures |
| Responsibility and stewardship | 6 | Ethics, sustainability, safety, culture, access |
| Practical skills and technical application | 8 | Make, construct, operate, test |
| Knowledge and conceptual understanding | 9 | Concepts, terminology, theory and principles |
| Independent learning and collaboration | 10 | Goals, initiative, feedback, teamwork, reflection |

These are the established brand learning domains, not official NESA outcomes. Groups 1 and 7 are not assigned as learning domains by default.

Knowledge-domain presentation prompts focus on Twilight #514689 and Periwinkle #DCD3E7, with white where needed. Do not introduce every palette colour into a single knowledge template.

## Presentation grid

Canvas: **1920 × 1080 px**, with **100 px margins**. Twelve columns are **125 px** wide with **20 px gutters**; twelve rows are **55 px** high with **20 px gutters**. Available content is **1720 × 880 px**.

For a box spanning C columns and R rows:

- Width = C × 125 + (C−1) × 20 px.
- Height = R × 55 + (R−1) × 20 px.
- x = 100 + (start column−1) × 145 px.
- y = 100 + (start row−1) × 75 px.

| Span | Width px | Height px |
|---|---|---|
| 1 | 125 | 55 |
| 2 | 270 | 130 |
| 3 | 415 | 205 |
| 4 | 560 | 280 |
| 5 | 705 | 355 |
| 6 | 850 | 430 |
| 7 | 995 | 505 |
| 8 | 1140 | 580 |
| 9 | 1285 | 655 |
| 10 | 1430 | 730 |
| 11 | 1575 | 805 |
| 12 | 1720 | 880 |

Width and height spans may differ. Example: a 4-column × 2-row card at column 1, row 3 has size **560 × 130 px**, x **100**, y **250**.

## A4 grid system

Landscape: 297 × 210 mm, 12 mm margins, twelve 20 mm columns with eleven 3 mm gutters. Width checks: 24 + 240 + 33 = 297 mm.

Portrait: 210 × 297 mm, 10 mm side margins and 12 mm top/bottom margins, twelve columns with 2 mm gutters and twelve rows with 3 mm gutters. Derived column width is **14 mm**; derived row height is **20 mm**. These are calculated from the supplied dimensions, not an additional independent brand instruction.

## Presentation typography

| Role | Family/style | Supplied size |
|---|---|---|
| Title | Lato Black | 133 pt |
| Subtitle | Lato Light | 57 pt |
| Heading | Lato Bold | 57 pt |
| Subheading | Lato Light | 34 pt |
| Section header | Lato Bold | 28 pt |
| Body | Lato Light | 26 pt |
| Caption | Lato Light | 16 pt |
| Quote | Lato Light | 26 pt |

The source specifies points while the canvas/grid uses pixels. Preserve units and verify the authoring application's actual sizing; do not equate pt and px silently. Light weights and small captions need real readability testing.

## Reusable templates

The user prefers one page/slide type at a time for Canva brand-template prompts. Use grid-aligned placeholder zones—heading, body, image, callout, teacher note, activity panel and diagram—unless a finished content deck is requested. Specify spans, dimensions and positions where useful.

Include title/opening, divider, explanation, comparison, process, media, activity and review arrangements. Reusability means variable content can fit without broken hierarchy.

## Contrast and evaluation

Dark shades generally support white text; pale tints support black or the matching shade. On highlights, calculate contrast for the actual pairing rather than rely on a blanket rule. Domain colour needs visible text labels and cannot carry all meaning alone.

Evaluate brand accuracy, hierarchy, grid geometry, content fit, teacher editability, access and learning purpose separately. Preserve the exact palette while adapting layout to the content.
