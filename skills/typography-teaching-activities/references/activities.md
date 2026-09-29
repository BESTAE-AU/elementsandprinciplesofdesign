# Typography activities

Each activity lists: concept · source video · time · materials · steps · check · extension.

## 1. Tone-of-voice match-up
- **Concept:** fonts communicate personality (DSP, ENV). **Time:** 15 min.
- **Materials:** cards with businesses (bank, clown, wedding photographer, eye doctor, camping brand, kids' clothing, tech start-up, law firm) and the same word set in 8 fonts (one per category).
- **Steps:** pairs match each business to a font, then justify one match aloud using a keyword from the personality table ("slab serif = strong, enduring").
- **Check:** "Why would a script font be a poor choice for an eye doctor?"
- **Extension:** find a real brand whose font breaks the expected match and argue whether it works.

## 2. Bank logotype vote
- **Concept:** fonts affect trust (ENV 1:01–2:03). **Time:** 10 min.
- **Materials:** one fictional bank name set in a formal serif and in a playful script.
- **Steps:** show both, vote with hands or a poll, watch ENV's segment, then discuss what else (colour, spacing) changes trust.
- **Check:** students write one sentence using "connotes" or "suggests".

## 3. Category sort and hunt
- **Concept:** classifications (CAN 4:14–6:21). **Time:** 20 min.
- **Materials:** printed or on-screen specimens, or phones for a photo hunt around school.
- **Steps:** sort specimens into serif, slab, sans, script, handwritten, display and monospace. Then photograph 5 real-world examples and label them.
- **Extension:** subdivide serifs (old-style, transitional, didone) or sans serifs (grotesque, geometric, humanist).

## 4. Anatomy labelling on handwriting paper
- **Concept:** baseline, cap line, x-height, ascender, descender, serif, counter (DSP 7:02–8:03). **Time:** 15 min.
- **Materials:** the word "Typography" printed large on 4-line handwriting paper, in a serif font.
- **Steps:** label the lines and parts, then compare the same word in a font with a large x-height and one with a small x-height at the same point size. Which looks bigger? Why?
- **Check:** hinge question: "Two fonts are both 12 pt but one looks bigger. What is the most likely reason?" (x-height).

## 5. Unit conversion challenge
- **Concept:** pt, px, rem, pica (DSP 5:02–7:02). **Time:** 15 min.
- **Steps:** students convert a list (12 pt → px; 24 px → rem; 18 pt → mm) using 1 in = 72 pt = 96 px. Then check the answers with `type_tools.py convert`. Discuss DSP's two slips (1/12 inch; "75 points").
- **Extension:** explain why rem respects users who set a bigger default font size.

## 6. Kerning game
- **Concept:** kerning vs tracking (CAN 6:21; DSP 10:04). **Time:** 15 min.
- **Materials:** badly kerned headlines and logos (e.g. "AVATAR", "WAVE", "Toy", "LATTE"), or an online kerning game such as *KernType*.
- **Steps:** fix the spacing by eye in Illustrator, Canva or on paper cut-outs, then compare with the Jessica Hische *Southern Living* example.
- **Check:** "Kerning or tracking? You want the whole heading looser." (tracking)

## 7. Line length and leading experiment
- **Concept:** readability (CAN 7:25). **Time:** 25 min.
- **Materials:** one paragraph set at 30, 60 and 100 characters per line, and at 100%, 130% and 180% leading.
- **Steps:** students rank each version for comfort, time themselves reading, then compare their results with the 45–75 characters and 120–150% guidelines.
- **Extension:** repeat on a phone screen vs A4 print.

## 8. Squint test critique
- **Concept:** hierarchy (CAN 3:13–4:14). **Time:** 15 min.
- **Steps:** swap posters or folio pages; each student squints and notes what they see 1st, 2nd and 3rd; the designer compares this with what they intended, then makes one change using size, weight, colour or space.
- **Check:** success criterion: "My intended focal point wins the squint test."

## 9. Build a type system
- **Concept:** type scales and styles (DSP 11:05–13:07). **Time:** 1–2 lessons.
- **Steps:** choose a base size and ratio, generate the scale with `type_tools.py scale`, then create paragraph or text styles for H1, H2, body, caption, button and label in InDesign, Word, Canva or CSS. Apply the styles to a one-page layout.
- **Extension:** compare a 1.25 scale with a 1.618 scale on the same layout. Which suits a report, and which a poster?

## 10. Heading/body pairing challenge
- **Concept:** extrovert vs introvert fonts and pairing strategies (CPS 0:00–4:05; CAN 8:28). **Time:** 1 lesson.
- **Steps:** given a brand brief, choose a heading font and a free Google body font, name the pairing strategy (one family, same category, contrasting, superfamily), mock up a headline and paragraph, and write a 100-word rationale.
- **Check:** peer review against the rationale format in `typeface-selection-rationale`.

## 11. History timeline
- **Concept:** where typefaces come from (DSP 1:00–2:01). **Time:** 20 min.
- **Steps:** order cards: calligraphy, Gutenberg (about 1450), Jenson's roman (1470), Garamond (1500s), Baskerville (1757), first sans serif type (about 1816), Times New Roman (1931–32), Helvetica (1957), web fonts and variable fonts. Discuss DSP's claim that "sans is older than serif" (true for lettering, not for printing type).

## 12. Accessibility check
- **Concept:** contrast and legibility (DSP 10:04–11:05). **Time:** 15 min.
- **Steps:** students test their text/background colours with `type_tools.py contrast` or WebAIM's checker and fix anything under 4.5:1 for body text. Combine with the colour unit.
- **Extension:** try Atkinson Hyperlegible or Lexend and discuss fonts designed for accessibility.
