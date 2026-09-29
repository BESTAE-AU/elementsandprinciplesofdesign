# Texture activities

Each activity lists: concept · time · materials · steps · check · extension.

## 1. Mystery bag (hook)
- **Concept:** actual texture and precise vocabulary. **Time:** 10 min.
- **Materials:** cloth bags or boxes with objects inside (sandpaper, velvet, bubble wrap, pine cone, sponge, silk, brick offcut, corrugated card).
- **Steps:** without looking, a student feels an object and describes it using only texture words. The class guesses. Build a word wall from the adjectives, sorted into the groups in `glossary.md`.
- **Check:** "Give me a better word than 'rough' for the pine cone."
- **Extension:** describe the same object using only visual evidence from a photo. What's lost?

## 2. Texture rubbing hunt (frottage)
- **Concept:** actual texture becoming visual texture; Max Ernst's frottage. **Time:** 25 min.
- **Materials:** thin paper (bank or photocopy), crayons, graphite sticks, masking tape.
- **Steps:** collect 8–10 rubbings around school (bark, grates, leaves, brick, signage, shoe soles). Label each with its source and 2 adjectives. Back in class, cut and collage them into an invented creature or landscape, as Ernst did.
- **Check:** "Is your rubbing actual or visual texture?" (Visual. The paper is smooth, but the marks record an actual texture.)
- **Extension:** photograph the sources with raking light and compare the photo and the rubbing.

## 3. Mark-making sampler
- **Concept:** creating visual texture with line and dot. **Time:** 30–40 min.
- **Materials:** `texture_tools.py swatches` worksheet (A4, greyscale), fineliners (0.1–0.8), pencils.
- **Steps:** copy each example swatch into the practice box, then invent 4 of your own. Label each with a real surface it could represent.
- **Check:** "Which technique would you use for fur? For glass? Why?"
- **Extension:** draw a simple object (a shoe, a shell) using at least 3 textures, with a value scale from each technique.

## 4. Actual vs visual sort
- **Concept:** actual/visual and simulated/invented. **Time:** 15 min.
- **Materials:** 12 image cards or real items (embossed card, impasto painting, a wood-grain laminate, halftone comic, a knitted swatch, a photo of moss, a Van Gogh detail, a grunge poster).
- **Steps:** sort into a 2 × 2 grid (actual/visual × simulated/invented). Discuss the edge cases, such as laminate that is actual-smooth but visually wood.
- **Check:** hinge question. "A photograph of a rusty gate printed on glossy paper: actual or visual? Simulated or invented?" (Visual, simulated.)

## 5. Raking light experiment
- **Concept:** light reveals texture. **Time:** 15 min.
- **Materials:** phone torches or a desk lamp, textured objects, phones for photos.
- **Steps:** photograph the same surface lit from the front, then from a low side angle. Compare and explain the difference using "value" and "shadow".
- **Extension:** apply it to product photography. How would you light a knitted jumper for an online store?

## 6. Texture and mood
- **Concept:** texture communicates meaning. **Time:** 20 min.
- **Materials:** the same headline and simple layout set over 6 backgrounds (smooth gradient, kraft paper, concrete, velvet, grunge scratches, halftone).
- **Steps:** match each version to a brand (luxury perfume, skate shop, organic bakery, law firm, retro comic store, construction company) and justify with the sentence stems in `analysis.md`.
- **Extension:** redesign one version for a brand it currently mismatches.

## 7. Legibility over texture
- **Concept:** texture vs readability. **Time:** 20 min.
- **Materials:** a poster with text over a busy photo; the `text-over` command.
- **Steps:** estimate the lightest and darkest tones behind the words (using an eyedropper). Run `python3 scripts/texture_tools.py text-over <text> <light> <dark>`. Try three fixes: move the text, lower the texture's opacity, add the suggested scrim. Compare.
- **Check:** "Why can a texture pass on its average colour but still fail?" (The lightest or darkest patches behind the letters are what matter.)

## 8. Digital texture lab
- **Concept:** grain, noise, halftone, blend modes, clipping masks. **Time:** 1–2 lessons.
- **Materials:** Photoshop, Photopea, Canva or Adobe Express; free texture photos (Unsplash) or the class's own macro photos.
- **Steps:** (a) put a paper texture over a flat illustration using Multiply at 30–60% opacity; (b) clip a concrete texture into a bold heading; (c) add grain to a gradient; (d) turn a photo into halftone. Screenshot the layers panel for each.
- **Extension:** create a seamless texture from your own photo (*Filter › Other › Offset* in Photoshop, then heal the seams).

## 9. Typographic colour squint
- **Concept:** text blocks have texture. **Time:** 15 min.
- **Materials:** two versions of the same paragraph: one well set, one with loose justification, rivers and mixed weights.
- **Steps:** squint, or blur the image, and compare how even the grey is. Mark the rivers and blotches.
- **Link:** `typography-critique-audit`.

## 10. Tactile packaging or swing tag (make)
- **Concept:** actual texture and print finishes. **Time:** 2–3 lessons.
- **Steps:** design a small swing tag or box lid, then prototype a finish by hand: blind emboss with a stylus over a foam mat, a debossed "stamp", glossy clear nail varnish or PVA as "spot UV", textured card stock. Explain which finish a commercial printer would use.

## Subject tailoring

| Subject | Focus |
|---|---|
| **Visual Arts / Visual Design** | Mark-making, impasto, collage and assemblage, frottage, analysis of artworks through the frames; texture as meaning (Oppenheim, Kiefer, Gascoigne) |
| **Graphics Technology** | Rendering materials in drawings (timber, metal, glass, fabric) with pencil and marker; print finishes; texture in packaging and posters |
| **Multimedia** | Digital texture (grain, noise, halftone, overlays, blend modes); texture maps for 3D and games; texture and legibility on screens; compression and screen size |
| **Textiles** | Handle, fibre and yarn, woven vs knitted, pile and nap, surface decoration (embroidery, appliqué, quilting, felting, smocking); swatch samplers with annotations |
| **Timber / D&T** | Grain and figure, open vs close grain, sanding sequence, oils vs lacquers, knurling and grip; how texture affects function (grip, cleaning, safety) |

## Suggested sequence (about 5 lessons)

| # | Focus | Core activities |
|---|---|---|
| 1 | What texture is; actual vs visual; vocabulary | Mystery bag (1), then actual vs visual sort (4) |
| 2 | Making visual texture | Rubbing hunt (2), then mark-making sampler (3) |
| 3 | How texture is seen and what it means | Raking light (5), then texture and mood (6) |
| 4 | Texture in design and digital texture | Digital texture lab (8) or a subject-specific practical |
| 5 | Apply and evaluate | Legibility over texture (7), then a short design task with a written justification using the sentence stems |

## Differentiation

- **Support:** a word bank of 12 texture adjectives with pictures; a 2-column "can touch / only looks" table; sentence stems from `analysis.md`; partly completed swatch worksheet.
- **Extension:** research one artist's texture technique and replicate it respectfully (not First Nations cultural marks); build a seamless texture; write a 300-word comparative analysis; explain texture gradients and depth perception.

## Success criteria examples

- I can explain the difference between actual and visual texture using an example.
- I can create at least 4 visual textures with line and dot, and name a surface for each.
- I can describe a texture with precise adjectives and explain its effect on the viewer.
- I can use texture in a design without hurting the legibility of the text.
