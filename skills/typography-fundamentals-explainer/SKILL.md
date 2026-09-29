---
name: typography-fundamentals-explainer
description: Explains typography concepts at the right level for the learner, including typeface vs font, type anatomy (baseline, cap height, x-height, ascender, descender, serif, counter), units (point, pica, pixel, em, rem), weight and width, tracking vs kerning vs leading, line length, alignment, type classifications (serif, slab, sans, geometric, script, handwritten, display, monospace) and a short history (Gutenberg, Jenson, Times New Roman, the first sans serifs). Use when someone asks what a typography term means, wants notes, a glossary, a definition, a worked explanation or model answers on type for Graphics Technology, Multimedia, Visual Design, Visual Arts or D&T, or asks things like "what's the difference between kerning and tracking?" or "why is 12 pt the same as 16 px?". For choosing fonts for a brief use typeface-selection-rationale. For setting up sizes, leading and styles use type-system-builder.
---

# Typography fundamentals explainer

Source notes: the "Typography" playlist (CAN = Canva *Understanding Typography*, DSP = DesignSpo *Ultimate Guide to Typography*, ENV = Envato Tuts+ *Psychology of Fonts*, CPS = The Color Palette Studio *My Favorite Body Fonts*). Full definitions, anatomy and history are in `references/glossary.md`. Read it before answering anything beyond a one-line definition.

## How to explain

1. **Find the level.** Stage 4 needs plain words and a concrete image. Stage 5 adds the correct term and one reason it matters. Stage 6 and teachers want precise definitions, numbers and the exceptions.
2. **Anchor to something they know.** The best analogies from the videos:
   - Baseline, x-height and cap line are the lines on **school handwriting paper** (DSP).
   - A typeface is a family and a font is one member: **Helvetica** vs **Helvetica Bold** (CAN).
   - Fonts are **tones of voice**: a silly font suits a clown, not a lawyer (DSP).
   - Heading fonts are extroverts, body fonts are introverts: the **SNL host vs the background actors** (CPS).
3. **Show, don't just tell.** Where it helps, give a tiny visual: a labelled ASCII diagram, a CSS snippet, or "type the word *AVATAR* and look at the gap between A and V".
4. **Separate the look-alike terms** explicitly. Students confuse these most:
   - **Tracking** (all letters, evenly) vs **kerning** (one pair) vs **leading** (between lines).
   - **Typeface** vs **font**.
   - **Script** (calligraphic, often joined) vs **handwritten** (a designer's own hand).
   - **Point size** (the body the letters sit in) vs how big a font *looks* (driven by its x-height).
5. **Finish with a check:** one hinge question or 2–3 quick-recall questions with answers.

## Accuracy notes (the videos slip in places)

Correct these gently if a student or source repeats them:
- **1 point = 1/72 inch**, not 1/12. 12 pt = 1 pica, 6 picas = 1 inch (DSP mixes these up).
- **1 CSS px = 1/96 inch = 0.75 pt**, so 16 px = 12 pt. DSP says "a pixel is worth 75 points", which is a slip for 0.75.
- **em** is relative to the *parent* element's font size. **rem** is relative to the *root* (html) size, 16 px by default. Users change it through browser font settings and zoom.
- **Contrast:** WCAG 1.0 dates from 1999, but the numeric contrast ratio came with WCAG 2.0 (2008). **4.5:1 is the AA minimum for body text**, 3:1 for large text, and 7:1 is the stricter AAA level DSP quotes.
- **"Sans serif is older than serif"** (DSP): unserifed *lettering* is ancient (e.g. Greek inscriptions), but sans serif *printing type* only appeared around 1816. Serifed roman type came first in print.
- **Times New Roman** (1931–32, Stanley Morison for *The Times*) was commissioned to replace an outdated, hard-to-read face. It was based on older roman models, so "made to look traditional" is only half the story.
- **Nicolas Jenson** (spelled with an *e*, not Jensen) cut his influential roman type in Venice in 1470. Call it "one of the first and most influential roman typefaces" rather than "the first serif".

## Output formats

- **Quick answer:** definition, one example, and why it matters to a designer (3–5 sentences).
- **Student notes or glossary:** term, plain definition, example, "don't confuse with". Pull from `references/glossary.md`.
- **Model answer:** use the syllabus verb (identify, describe, explain, justify) and include the technical term, a specific example and the effect on the reader.

## Hand-offs

- Choosing or justifying fonts for a brief: `typeface-selection-rationale`.
- Sizes, leading, tracking, scales and paragraph styles: `type-system-builder`.
- Critiquing a finished design: `typography-critique-audit`.
- Lessons and activities: `typography-teaching-activities`.
- Text/background colour contrast in depth: `colour-contrast-audit`.
