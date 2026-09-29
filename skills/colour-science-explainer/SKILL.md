---
name: colour-science-explainer
description: Explains the physics and biology of colour at the right level for the learner, including light and wavelength, why objects look coloured, rods and cones, why red + green light looks yellow, additive (RGB) vs subtractive (CMYK) mixing, pigment vs dye, metamerism, fluorescence, afterimages, colour constancy and colour blindness. Use when someone asks why or how colour works, wants a colour-science explanation, notes or a demo for Graphics, Multimedia, Visual Arts, Textiles or D&T, or asks things like "why do screens use RGB but printers use CMYK?" or "why do fabrics match in the shop but not outside?". For converting colour codes use colour-codes-and-conversion. For choosing palettes use colour-palette-builder.
---

# Colour science explainer

Explain *why* colour behaves the way it does, then connect it to something the learner designs, prints, dyes or sees on a screen.

## How to answer

1. **Pitch it.** Work out who is asking (Stage 4 student, HSC student, teacher, designer) and what they need (a quick answer, notes, a demo or a misconception fix). If it's unclear, default to a Stage 5 student level. Use Australian spelling.
2. **Use the three-stage model as the spine.** Colour = **light source → object → observer**. Change any one stage and the colour changes. Most "weird colour" questions are answered by asking which stage changed. *(af78)*
3. **Explain the mechanism, then the consequence.** Use one concrete image per idea. For example, red + green light makes the brain get the same cone signal as real yellow light, *so* screens only need three sub-pixels.
4. **Tie it to practice.** End with what it means for their work: screen vs print files, dye matching under a standard light, choosing accessible traffic-light colours, and so on.
5. **Correct misconceptions explicitly** when they're relevant. See the list below.
6. **Offer a demo** from `references/demos.md` when the person is teaching or learning the concept for the first time.

Get facts and numbers from `references/concepts.md`. Don't invent statistics. Where a figure is an estimate (such as "18 decillion colours"), say so.

## High-value misconceptions to correct

| Misconception | Correction |
|---|---|
| "Objects have colour." | Objects **reflect some wavelengths and absorb the rest**. The colour we see is what's reflected. White reflects all, black absorbs all, which is why black gets hot. |
| "The primary colours are red, yellow, blue." | RYB is the *traditional artist's* model. Light primaries are **RGB** (additive). The optimal pigment/ink primaries are **CMY(K)** because they give a larger gamut. |
| "Mixing all colours gives black." | Only for *subtractive* (ink, paint). Mixing all *light* gives **white**. |
| "Red + green = brown." | With paint, yes, roughly. With light it gives **yellow**, because it triggers the red and green cones exactly like yellow light does. |
| "A red object under blue light is always black." | The textbook answer is black, but a **shiny** red object shows specular (mirror) reflection of the blue light, and a **fluorescent** one can re-emit a different colour. |
| "If two fabrics match, they'll always match." | Not under a different light: that's **sample (illuminant) metamerism**. |
| "Watts tell you how bright a bulb is." | Watts measure electrical power. **Lumens** measure light output. |
| "Everyone sees the same colour." | **Observer metamerism**, colour-vision deficiency, age-yellowed lenses and context (simultaneous contrast, colour constancy) all change what people perceive. |

## Output formats

- **Quick answer:** 3–6 sentences covering the mechanism, then the consequence, then the link to practice.
- **Student notes:** headings, key terms in bold with one-line definitions, a labelled table (e.g. additive vs subtractive), 3 check-for-understanding questions, and an answer key if asked.
- **Teacher explainer:** the concept, a common misconception, a demo, and a hinge question to check understanding.

If the person wants a full workbooklet or learning sequence, hand off to the `content-booklet-builder` skill if it's available, and use this skill's references as the content source.

## Use it in connected tools (Adobe, Canva and others)

For visuals, find tools by keyword before promising anything. With **Adobe Express** or **Canva** connected, build the diagram, poster or slide there (additive/subtractive Venn, spectrum, three-stage model), following `references/applying-in-tools.md`. **Unsplash** is useful for photos (autumn leaves, prisms, hi-vis vests). If nothing is connected, draw an SVG or HTML diagram. Label every colour by name so it survives greyscale printing.
