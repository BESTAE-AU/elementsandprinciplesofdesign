---
name: typeface-selection-rationale
description: Chooses, pairs and justifies typefaces for a brand, poster, website, app, packaging, folio or student design project, using type psychology (the personality of serif, slab, sans, geometric, rounded, script and display faces), the heading-vs-body ("extrovert vs introvert") rule and three pairing strategies. It writes the typography rationale for a design justification, folio, brand guideline or client presentation. Use when someone asks "what font should I use?", "do these fonts go together?", "suggest a font pairing", "why does this brand use this font?", needs free Google Fonts alternatives, wants a written justification of font choices, or is building the typography page of a brand identity deck, even if they only say "fonts" or "type". For defining sizes, leading and paragraph styles use type-system-builder. For colour choices use colour-palette-builder and colour-psychology-rationale.
---

# Typeface selection and rationale

Source method: the "Typography" playlist (CAN, DSP, ENV, CPS). Font personalities and a vetted list of free and premium options are in `references/font-library.md`. Read it before recommending specific fonts.

## The process

1. **Read the brief.** Get, or sensibly assume and state:
   - Audience (age, culture, expertise) and what they should *feel*. Type is read through the viewer's background, so the audience decides (ENV).
   - Three brand or project adjectives (e.g. "calm, trustworthy, modern").
   - Medium: print, screen or both; body text length; any required languages or numerals.
   - Constraints: licensing budget (free vs paid), software (Canva, Adobe, Word, web), existing brand fonts.
2. **Match tone of voice.** Fonts are tones of voice (DSP). Map the adjectives to a category using the personality table in `references/font-library.md`. Do the **bank test** (ENV): would this font make the audience trust *this* organisation to do *this* job?
3. **Pick an extrovert heading font.** It carries the personality: display, script, slab, a characterful serif or a distinctive sans (CPS). Check it at the actual heading size and with the real words.
4. **Pick an introvert body font.** Its job is to deliver information, so it should be calm, legible and "dare I say boring" (CPS). Check: a large enough x-height, clear distinctions between I/l/1 and O/0, real bold and italic, and enough weights. Sans serif is the default for screens; serif suits long print reading (CAN).
5. **Pair using one of three strategies** (CAN, CPS):
   - **One family, several styles:** bold, caps and regular of one typeface. Safest and most cohesive.
   - **Same category:** e.g. a bold rounded sans heading with a lighter condensed sans body. Make the difference obvious, not slight.
   - **Contrasting categories:** e.g. a geometric sans heading with a traditional serif body. Works best when the two share a trait (similar x-height, round forms, or the same era).
   - **Superfamilies** (DM Sans + DM Serif, IBM Plex Sans + Serif) are built to pair.
   Limit to **two families** (three at most, with the third for a special role such as numbers or code). Avoid two scripts or two display faces together.
6. **Test it.** Set a real headline, subhead and paragraph. Do the squint test (CAN). Check small sizes, bold weights and the characters the brand uses (numbers, €, macrons, etc.). Check licensing: Google Fonts are free for commercial use, but premium fonts need the right licence for print, web or app.
7. **Write the rationale.**

## Rationale format

For each font:
- **Role** (logo, headings, body, buttons/labels).
- **Category and features** in technical terms (e.g. "geometric sans serif, round bowls, large x-height, 9 weights").
- **Effect on the audience** linked to the brief's adjectives ("its round letterforms feel friendly and youthful, suiting a Year 7 audience").
- **Practical reason** (legibility at small sizes, screen rendering, free licence, available in Canva).
- **Why the pair works** and which strategy it uses.

For HSC and folio work, use the verb frame: *identify* the feature → *explain* its effect → *justify* against the brief. Mention an alternative that was rejected and why; this shows evaluation.

## Critiquing an existing brand's choice

Name the category and features, link them to the brand values and audience, note any tension (e.g. a sterile sans making fashion brands look alike, per DSP), and suggest what an alternative would communicate instead.

## Tools

- **Canva:** brand kit fonts; check a font exists in Canva before recommending it for Canva-only users.
- **Adobe:** Adobe Fonts through Creative Cloud; the Adobe connector's `font_recommend`, `font_search` and `font_preview` tools can suggest and preview pairings. `get_type_palette` / `suggest_type_palettes` produce ready-made pairings.
- **Word / Google Docs:** stick to installed or Google Fonts so files open elsewhere.
- House print styles (Lato workbooklets) come from `workbooklet-style-system`. Don't override them unless asked.

## Hand-offs

- Sizes, leading, tracking, type scale and style sheets: `type-system-builder`.
- Term definitions: `typography-fundamentals-explainer`.
- Colour for the same brief: `colour-palette-builder` and `colour-psychology-rationale`.
