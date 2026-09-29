# Typography glossary

Source codes: CAN = Canva *Understanding Typography*, DSP = DesignSpo *Ultimate Guide to Typography*, ENV = Envato Tuts+ *Psychology of Fonts*, CPS = The Color Palette Studio *My Favorite Body Fonts*.

## Contents
1. Core ideas
2. Anatomy
3. Units and sizes
4. Spacing and layout
5. Classifications
6. A short history

## 1. Core ideas

| Term | Definition | Example / note |
|---|---|---|
| Typography | The art and science of arranging text so it is legible and appealing: from single letterforms to words, lines and blocks of body copy (DSP, CAN) | |
| Typeface | A designed family of letters, numerals and punctuation (CAN) | Helvetica |
| Font | One style, weight or width within a typeface (CAN) | Helvetica Bold. A family can hold one font or dozens |
| Body copy | The main running text: paragraphs, descriptions, bios (CAN, CPS) | |
| Legibility | How easily individual letters can be told apart | Depends on the typeface design |
| Readability | How easily a whole block of text can be read | Depends on how it is set: size, leading, line length, contrast |
| Hierarchy | Ordering text by importance so the reader knows what to read first (CAN) | Headline → subhead → body |
| Weight | Thickness of the strokes: thin, light, regular, medium, semibold, bold, black (DSP) | Sans families often have 9+ weights |
| Width | How wide the letters are: condensed, regular, wide, extended (CAN) | |
| Faux bold / italic | Software-thickened or slanted letters made by clicking B or I when the family has no real bold or italic (CAN) | Looks clumsy. Choose the real weight from the font list |
| Proportional | Letters take different widths (an *i* is narrower than an *m*) | Almost all fonts |
| Monospace | Every character is the same width (DSP) | Code, tables of numbers |
| Variable font | One font file with adjustable axes such as weight and width (DSP) | |

## 2. Anatomy

```
 cap line   ─ ─ ─ H ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
 ascender   ─ ─ ─ ─ ─ ─ ─ ─ ─ d ─ ─ ─ ─ ─ ─ ─ ─   (tops of b d h k l often rise above the cap line)
 x-height   ─ ─ ─ ─ ─ x ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   (height of lowercase x, a, o)
 baseline   ═══════════════════════════════════   (what letters sit on)
 descender  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ p ─ g ─ ─ ─ ─   (tails of g j p q y)
```

| Term | Definition |
|---|---|
| Baseline | The invisible line letters sit on, like the bottom line on school handwriting paper (DSP) |
| Cap height / cap line | The height of capital letters (DSP). A big baseline-to-cap gap can read as luxurious |
| x-height | The height of lowercase letters without ascenders, e.g. *x* (DSP). The dotted middle line on handwriting paper. A large x-height looks bigger and reads better small. A short one (e.g. Avenir, per CPS) looks "stocky" |
| Ascender / descender | The parts of lowercase letters that rise above the x-height (b, d, h) or drop below the baseline (g, p, y) |
| Serif | The small stroke or "foot" at the end of a main stroke (CAN) |
| Stroke / stem | The main lines of a letter; the stem is the main vertical |
| Counter | The enclosed or partly enclosed space inside a letter (o, e, a) |
| Bowl | The curved stroke that makes a counter (b, d, p) |
| Terminal | The end of a stroke without a serif |
| Ligature | Two or more letters joined into one glyph, e.g. *fi*, *fl* |
| Glyph | Any single drawn shape in a font |

## 3. Units and sizes

| Unit | Value | Used for |
|---|---|---|
| Point (pt) | 1/72 inch ≈ 0.353 mm | Print type size and leading |
| Pica (pc) | 12 pt = 1/6 inch | Column widths in print |
| CSS pixel (px) | 1/96 inch = 0.75 pt. A reference unit, not a physical screen pixel (DSP) | Screen sizes |
| em | Equal to the current element's font size (relative to its parent) | Spacing that scales with the text |
| rem | "Root em": relative to the html root size, 16 px by default (DSP) | Web type sizes; respects users' browser settings and zoom |
| ch | Width of the "0" character | Line length: `max-width: 66ch` |

Key conversion: **12 pt = 16 px = 1 rem** (default). Point size measures the invisible body of the type, not the height of any letter, which is why two fonts at 12 pt can look very different in size.

## 4. Spacing and layout

| Term | Definition | Rule of thumb |
|---|---|---|
| Tracking / letter-spacing | Even spacing across a whole word, line or block (CAN, DSP) | Inversely proportional to size: tighten big headlines slightly, loosen tiny text and all caps slightly. Add a little to bold buttons |
| Kerning | Adjusting the space between one specific pair of letters (CAN, DSP) | Fix awkward pairs such as AV, To, WA, LT in headings and logos. Example: Jessica Hische's re-kerned *Southern Living* logo |
| Leading / line height | Vertical distance from baseline to baseline (CAN, DSP). Named after strips of lead in metal type | 120–150% of the type size for body text. Tighter (100–120%) for large headings |
| Line length / measure | Characters per line (CAN) | 45–75 characters including spaces; about 66 is ideal |
| Alignment | How lines line up: left (flush left, ragged right), centred, right, justified (CAN) | Left-aligned is easiest to read in English. Centre and right for short bursts. Justified can create uneven "rivers" of space |
| Widow / orphan | A very short last line of a paragraph, or a single line stranded at the top or bottom of a column | Rewrite, re-rag or adjust tracking slightly |
| White space | Empty space around and between elements | Gives hierarchy room to work |
| Grid | Columns and rows that set where text and images sit (DSP) | Web 12 columns; newspapers about 6; magazines about 3; print pages often 2 |
| Contrast | Difference between text colour and background (DSP) | WCAG AA: 4.5:1 body text, 3:1 large text. AAA: 7:1 |

## 5. Classifications

| Category | Look | Personality (ENV, DSP) | Best use | Examples |
|---|---|---|---|---|
| Serif (old-style, transitional, modern/didone) | Small feet at stroke ends | Tradition, stability, intellect, formality, luxury | Long print reading, institutions, luxury brands | Garamond, Baskerville, Times New Roman, Merriweather, Bodoni (didone) |
| Slab serif | Heavy, block-like serifs | Strong, enduring, brash | Headers, automotive, outdoors | Rockwell, Roboto Slab |
| Sans serif (grotesque, neo-grotesque, humanist) | No serifs | Modern, clean, neutral, open, friendly | Screens, signage, packaging, UI, body copy on screen | Helvetica, Public Sans, DM Sans, Proxima Nova |
| Geometric sans | Built from circles and straight lines | Modern, elegant; rounded versions feel young and friendly | Fashion, fragrance, tech; kids' brands if rounded | Futura, Avenir, Poppins |
| Script | Joined, pen or brush strokes | Formal: romantic, elegant. Casual: friendly, fun | Invitations, short headings, logos | Great Vibes (formal), Pacifico (casual) |
| Handwritten | Based on real handwriting | Personal, playful, less elegant than script | Short, informal accents | |
| Display / decorative | Stylised, novelty, illustrative | Anything: a Western poster, a cosmic brand | Logos, titles, short bursts only. Never body copy, buttons or labels | |
| Monospace | Fixed-width characters | Technical, retro-computer | Code, data | Courier, IBM Plex Mono |

## 6. A short history

- **Hand lettering and calligraphy:** books were copied by hand in blackletter and other scripts.
- **About 1450, Gutenberg:** movable metal type in Europe. His type imitated blackletter calligraphy, which was dense and space-hungry (DSP).
- **1470, Nicolas Jenson (Venice):** one of the first and most influential roman typefaces, based on Italian humanist handwriting. Roman type became the print standard (DSP).
- **1500s, Claude Garamond:** refined old-style serifs still used today (EB Garamond, CPS).
- **1757, John Baskerville:** transitional serif with sharper contrast (Libre Baskerville, CPS).
- **About 1816, William Caslon IV:** the first sans serif printing type. Unserifed lettering itself is ancient.
- **1931–32, Times New Roman:** Stanley Morison for *The Times* newspaper, to replace an outdated face with a more legible, space-efficient one (DSP).
- **1957, Helvetica:** Max Miedinger and Eduard Hoffmann; the neutral Swiss neo-grotesque (CAN, CPS).
- **1990s onward:** screen fonts, web fonts and Google Fonts; **variable fonts** from 2016.
