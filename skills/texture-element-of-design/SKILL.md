---
name: texture-element-of-design
description: Explains, analyses and plans lessons on texture as an element of design, meaning the surface quality of something (how it feels, or looks like it would feel). Covers actual (tactile) vs visual (implied) texture, simulated vs invented texture, texture vs pattern, how light, value and scale reveal texture, mark-making techniques (hatching, stippling, frottage, sgraffito, impasto), texture in typography and layout, digital texture (grain, noise, halftone, overlays, blend modes), print finishes (emboss, deboss, foil, spot UV, soft-touch), textiles handle and weave, and timber grain and figure. Use when someone asks what texture is, wants notes, a glossary, model answers or a folio annotation on texture, wants to analyse an artwork, poster, product, garment or brand's use of texture, asks how to add or fix texture in a design (e.g. "my poster looks flat", "is this background too busy for the text?"), or wants texture lessons, activities, a mark-making worksheet or a sequence for Visual Arts, Visual Design, Graphics Technology, Multimedia, Textiles, Timber or D&T, even if they only say "surface", "tactile", "grainy" or "rough vs smooth".
---

# Texture (element of design)

Texture is the **surface quality** of a thing: how it feels to touch, or how it looks like it would feel. It is one of the elements of design, alongside line, shape, form, space, value and colour. Texture works on two senses at once. Designers use it to make things look real, add depth and hierarchy, create mood, signal quality and make things memorable.

Read the reference file for the job before answering anything beyond a one-line definition:

| Job | Read |
|---|---|
| Define or explain a term; notes, glossary, model answers | `references/glossary.md` |
| Analyse or critique the texture in a work; folio annotation | `references/analysis.md` |
| Lessons, activities, worksheets, sequences | `references/activities.md` |
| Add, change or check texture in Adobe, Canva, Photoshop, print or connected tools | `references/applying-in-tools.md` |

## 1. Explaining texture

1. **Find the level.**
   - **Stage 4:** plain words and something to touch: "texture is what the surface feels like, or looks like it would feel like."
   - **Stage 5:** add the correct terms (actual vs visual, simulated vs invented) and one reason texture matters in design.
   - **Stage 6 and teachers:** precise terms, how light and scale control texture, the history (frottage, impasto, skeuomorphism to flat design), and subject-specific language (handle, figure, finishes).
2. **Anchor to something they know.** Run a hand over a desk, jumper, brick wall or basketball. Then show a *photo* of the same thing. The photo is flat, but you still "feel" it. That gap is the difference between actual and visual texture.
3. **Separate the look-alike terms.** Students confuse these most:
   - **Actual (tactile)** vs **visual (implied)** texture: can you really feel it, or does it only look that way?
   - **Simulated (realistic)** vs **invented (abstract)** visual texture: does it copy a real surface, or is it a made-up surface built from marks?
   - **Texture** vs **pattern**: pattern is a *planned repeat* of a motif. Texture is the *surface quality*. A pattern seen small and dense enough reads as texture (a houndstooth jacket from across the room), so the difference is often about scale and intent.
   - **Texture** vs **value**: texture is usually *shown* through changes in value (light and shadow), but a smooth gradient is value, not texture.
   - **Grain** in photography or print (film grain, noise) vs **grain** in timber (the direction of the wood fibres) vs **grain** in fabric (the direction of the warp threads).
4. **Explain how texture is revealed.** We see texture through **light**. Low, raking light from the side casts tiny shadows and exaggerates texture. Flat, front-on light hides it. **Scale** matters too: sand is texture up close and a smooth beach from a plane.
5. **Finish with a check:** a hinge question or 2–3 quick-recall questions with answers. For example, "A photo of tree bark in a magazine: actual or visual texture?" (Visual. The page itself is smooth.)

## 2. Analysing texture in a work

Follow the full framework in `references/analysis.md`. In short:

1. **Identify** each texture: actual or visual, simulated or invented, and where it sits.
2. **Describe** it with precise adjectives from the vocabulary bank (coarse, glossy, matte, rough, pitted, fibrous, velvety, crackled…) and say *how it was made* (medium, technique, tool, finish).
3. **Explain the effect** on the viewer or user: realism, depth, emphasis, contrast, mood, era or authenticity, quality, invitation to touch.
4. **Evaluate:** does the texture serve the purpose or fight it? Common problems are texture behind text that hurts legibility, too many competing textures, texture at the wrong scale for the output (fine grain lost on screen, or blown up and pixelated in print), and "texture as decoration" with no link to the concept.
5. **Suggest** one or two specific fixes.

For **text over a textured background**, don't guess. Estimate the lightest and darkest tones in the texture behind the words and run:

```
python3 scripts/texture_tools.py text-over <text-hex> <lightest-hex> <darkest-hex> [more tones...]
```

It reports the worst-case WCAG contrast and, if that fails, the lowest-opacity scrim (a solid overlay) that makes every tone pass.

## 3. Creating and applying texture

Give **concrete, tool-specific** advice: which technique, which tool or setting, how strong, and where. See `references/applying-in-tools.md` for Adobe and Canva connector tools, Photoshop, Illustrator and InDesign steps, print finishes, and textiles and timber methods.

House rules for good texture use:
- **Purpose first.** Every texture should do a job (realism, mood, emphasis, brand story, tactile invitation). If you can't name the job, remove it.
- **One hero texture.** Let one texture dominate and keep others quiet, like a 60-30-10 approach with colour. Contrast a textured area with a smooth one, because texture only reads next to something smoother.
- **Protect legibility.** Keep body text on smooth or low-contrast areas. Use `text-over` to check. Lower the texture's opacity or add a scrim if needed.
- **Match the output.** Screens flatten fine texture and compression turns noise into mush. Print can carry real tactile finishes. Check at 100% and at the final size.
- **Greyscale printing.** Texture survives greyscale printing better than colour does, so it's a good way to separate areas on photocopied resources. Very fine, light textures disappear on a copier. Test one copy first.

## 4. Teaching texture

Choose activities from `references/activities.md`, adapted to the subject, stage and outcome type:
- *Know or understand* (vocabulary, actual vs visual).
- *Make* (mark-making, rubbings, samplers, digital texture).
- *Analyse or evaluate* (artworks, posters, products, garments).

Every activity has a check and an extension. The file includes a suggested 5-lesson sequence, notes for each subject, differentiation, and sentence stems.

For a printable mark-making worksheet (a greyscale A4 SVG with labelled example swatches, plus empty boxes for students to copy them), run:

```
python3 scripts/texture_tools.py swatches --out texture-swatches.svg            # examples + practice boxes
python3 scripts/texture_tools.py swatches --blank --out texture-practice.svg    # empty labelled boxes only
```

## Accuracy notes

Correct these gently if a student or source repeats them:
- **"Texture is only for things you can touch."** No. Most texture in graphic design is *visual* texture on a flat surface.
- **"Pattern and texture are the same thing."** They overlap but aren't the same. Pattern is a planned repeat; texture is surface quality. Many textures (sand, bark, noise) don't repeat at all.
- **Frottage** (rubbing over a textured surface) was developed as an art technique by **Max Ernst in 1925**. Children made rubbings long before that, but Ernst named it and used it to invent imagery.
- **Dürer's *Rhinoceros* (1515) is a woodcut, not an engraving.** It is a strong example of *invented* texture, because Dürer never saw the animal and imagined its hide as armour plates.
- **Skeuomorphism to flat design:** Apple's iOS 7 (2013) is the usual landmark for the move away from realistic textures (leather, felt, paper) in interfaces. Texture has since come back subtly, as grain, noise and paper effects.
- **First Nations art:** don't describe dot painting or cross-hatching (rarrk) in First Nations art as just "texture technique" or ask students to copy it. These marks can carry cultural knowledge and belong to particular communities. Teach them as the artist's cultural practice, name the artist and Country where known, and follow Creative Australia's *Protocols for using First Nations Cultural and Intellectual Property in the Arts*.

## Output formats

- **Quick answer:** definition, one concrete example and why it matters to a designer (3–5 sentences).
- **Student notes or glossary:** term, plain definition, example, "don't confuse with". Pull from `references/glossary.md`.
- **Model answer or annotation:** use the syllabus verb (identify, describe, explain, analyse, evaluate, justify) and include the technical term, specific evidence from the work and the effect on the viewer. Label it as a model. Keep it in the student's voice when you're modelling student work.
- **Comparison of two works:** a table (type of texture, how it was made, where it sits, dominant or supporting, effect, what it contrasts with).

## Hand-offs

- Colour and value inside a texture: `colour-harmony-analyser`. Text contrast in depth: `colour-contrast-audit`.
- Texture made from type (typographic colour): `typography-critique-audit`, `type-system-builder`.
- Full workbooklets: `content-booklet-builder`. Hands-on technique instruction (dry brush, emboss, a weave sample): `practical-skill-builder`.
- Assessment: `assessment-task-designer`, `marking-rubric-builder`, `nesa-exam-question-writer`.
- Print layout for worksheets: `greyscale-print-design-system`, `indesign-parameters`. Canvas pages: `canvas-course-builder`.
