---
name: colour-harmony-analyser
description: Identifies and critiques the colour scheme in a set of colours, an image, poster, film still, brand or artwork. It names the harmony (monochromatic, analogous, complementary, split-complementary, triadic, tetradic, square, one colour + neutrals), warm vs cool balance, proportions (60-30-10 / 80-20), hue/value/saturation choices and the mood they create, and suggests improvements. Use when someone asks "what colour scheme is this?", wants a visual analysis of colour for Visual Arts, Graphics or Multimedia, is analysing film posters or an artist's use of colour, or needs model answers or annotation for a design folio.
---

# Colour harmony analyser

## Steps

1. **Get the colours.**
   - If hex codes are given, use them.
   - If you have an image, list the 3–7 dominant colours with estimated hex values and rough area percentages. Say that they are estimates, and group near-identical shades together.
2. **Classify.** Run `python3 scripts/colour_tools.py harmony <hexes>`. The script maps hues onto the traditional **RYB artist's wheel** (the one students are taught, where red/green, blue/orange and yellow/purple are complements), ignores neutrals, and reports the closest named harmony plus each colour's warm/cool temperature. Treat it as evidence, not a verdict: real designs are rarely geometrically exact. Say "a split-complementary scheme built on…" when it's close.
3. **Proportion.** Estimate the percentage of each colour. Compare the result with 60-30-10 (dominant, secondary, accent) or, for complementary schemes, 80/20. Optionally visualise it with `python3 scripts/colour_tools.py ratio "#hex=60" ...`.
4. **Analyse using the vocabulary:**
   - **hue** (which families)
   - **value** (the light/dark structure: where is the highest contrast, and is that where the eye goes?)
   - **saturation** (vivid vs muted, and whether the tones match)
   - **temperature** (warm advances and energises, cool recedes and calms)
   - **simultaneous contrast** (e.g. Van Gogh's complementary neighbours)
5. **Interpret.** Explain what mood or meaning the choices create and *how* (the evidence, then the effect), including cultural associations where relevant.
6. **Evaluate and suggest.** What works, what fights (vibrating complements at 50/50, too many equal-weight hues, mismatched tones, poor text contrast), and one or two specific fixes.

## Reference examples (x0s, Visme)

| Work | Harmony | Why it works |
|---|---|---|
| *Blade Runner 2049* poster | Complementary (orange/teal-blue) | Dramatic contrast, with one colour dominant |
| *Kung Fu Panda* poster | Analogous warm (red, orange, yellow) | Warm, energetic, unified |
| *The Grand Budapest Hotel* | Monochromatic pink | Cohesive, whimsical, but low contrast |
| *Inside Out* poster | Square (one colour per emotion) | Works because of the dominant background and the character-coded colours |
| Headspace | Double split-complementary (yellow/orange vs blue/purple) | Friendly and rich, and finessed with tints |
| Paul Rand poster | Many hues, mostly white (~60%) | Each hue is used sparingly (eXc) |
| Borussia Dortmund | One colour + black and white | Iconic and instantly recognisable |

## Writing it up

- **Quick:** name the harmony, give the evidence (which hues and where), then the effect.
- **Folio or annotation:** use the pattern *identify, then describe, then explain the effect on the viewer, then justify or evaluate*. Use subject vocabulary (hue, value, saturation, tint, shade, tone, warm/cool, dominant, accent, contrast). Keep it in the student's voice if you're modelling student work, and label it as a model.
- **Comparing two works:** use a table (harmony, dominant hue, value range, saturation, temperature, mood, how colour directs the eye).

For accessibility or legibility of text in the work, also run `colour-contrast-audit`. For meanings of individual colours, see `colour-psychology-rationale`.

## Use it in connected tools (Adobe, Canva and others)

If the work lives in **Canva** (`read-design` / `export-design`) or **Adobe** (asset preview), pull it through the connector rather than asking for a screenshot. To demonstrate a fix, produce a recoloured version, e.g. Adobe `image_apply_color_overlay` / `image_adjust_hsl` or Canva `edit-design` on a *copy*, and show the before and after. See `references/applying-in-tools.md`.
