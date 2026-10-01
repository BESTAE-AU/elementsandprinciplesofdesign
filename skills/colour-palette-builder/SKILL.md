---
name: colour-palette-builder
description: Builds a purposeful, accessible colour palette from a design brief using a step-by-step professional process. The steps are brief questions, choosing a primary hue from psychology, refining with HSB, picking a harmony, matching tones, setting a 60-30-10 ratio and usage rules, testing contrast, and reviewing against the brief. It also handles building around a colour the client insists on, and fixing a chaotic palette. Use when someone needs colours for a brand, logo, poster, website, app, packaging, textile collection or student design project, says "what colours should I use", "make me a palette", "my colours clash" or "the client wants this colour", or needs usage rules for a style guide. Outputs hex codes with roles, ratios, pairing rules and a written rationale, plus swatch files (.ase, CSS, Canva list) and steps for applying the palette through Canva, Adobe Express/Firefly or other connected tools.
---

# Colour palette builder

A palette is a set of colours **with jobs**, not just a set of swatches. Every colour you deliver has a role, a proportion and rules for where it goes. This process is from Flux Academy (Co75), The Futur (eXc, V-SD) and The Colour Palette Studio (oDn, D98).

Tool: `scripts/colour_tools.py` (standard library only). Use it for `convert`, `harmony`, `audit` (contrast and balance) and `ratio`.

## Act 1: Build the brief (don't skip this)

Get answers to these four questions from the person, or infer them and state your assumptions:
1. **Constraints:** existing brand guidelines? A must-use colour? Print limits (spot colours, one-colour screen print, fabric dye)? Accessibility requirements?
2. **Guidance:** existing materials, a written brief, a mood board, competitors?
3. **Action:** what should the viewer *do* (buy, sign up, read, find the exit)?
4. **Feeling:** what should they *feel*, and what moment are they in? Who is the audience (age, culture, place)?

If the brief is thin and the stakes are real (a client brand or an assessed project), ask 2–3 targeted questions before building. For a quick exploration, state the assumptions and go.

## Act 2: Select colours

**Step 1: Choose a primary hue** (the answer a toddler would give: "green", "blue") based on psychology and associations. Use `colour-psychology-rationale` or `references/process.md` for meanings. Check **cultural, political, religious and sports-team** associations for the place the design will live. Remember that colour never works alone: type, layout and imagery must support the same mood.

**Step 2: Refine with HSB for the audience.** The same hue shifts meaning with saturation and brightness:
- Bright and saturated feels youthful, energetic and modern.
- Desaturated and darker feels mature, calm, premium and business-like.

Example (Co75): an eco clothing green that is vivid for a teen brand is muted and deepened for a 40s audience.

**Step 3: Build the palette with as few colours as possible.** Options, simplest first:
- **One colour + black and white** (or warm/cool neutrals). Very effective, e.g. Borussia Dortmund, Inter Milan, Brooklyn Brewery.
- **Monochromatic:** one hue in tints, tones and shades. Guaranteed to match, but has less contrast for marketing.
- **Analogous:** calm and natural. One dominant colour, the others as accents.
- **Complementary or split-complementary:** vibrant. Avoid 50/50, aim for about 80/20.
- **Triadic, tetradic, square:** bold but hard to balance. One colour must dominate.

Details are in `references/process.md`. Use `python3 scripts/colour_tools.py harmony <hexes>` to confirm the relationship you intended.

**Step 4: Match tones.** All chromatic colours should sit at **similar saturation and brightness** so they belong together. A pure RGB red next to a muted blue and beige looks wrong. Adjust the outliers, don't just add colours.

**Step 5: Balance light and dark** (oDn). A palette needs **at least two colours** and **at least one light and one dark colour**. Keep your only light and dark colours out of the mid-tone **danger zone**.

## Act 3: Rules and review

**Step 6: Set usage rules.**
- **60-30-10:** 60% dominant or primary (often neutrals or background), 30% secondary, 10% accent (the "wild card" for calls to action). Group tints and shades of one colour into the same bucket. It's a starting point, not a law. Show it with `ratio`, e.g. `python3 scripts/colour_tools.py ratio "#F5F0E6=60" "#1F3D5A=30" "#F2A541=10"`.
- **A pairing table per background:** for each likely background, which colour works for body text, links and buttons (eXc). Build it from the `audit` output.
- **Protect the accent:** use it for calls to action and key highlights only. Decorative elements use primary or secondary colours, or the accent loses its power.
- House rules such as: no coloured body text (black, or white on dark); which colour is for buttons; which colours never sit next to each other (e.g. pink on a vivid blue "vibrates").

**Step 7: Test and review.**
- Run `python3 scripts/colour_tools.py audit <all hexes>`. You need **4.5:1 or higher** for body text. Fix low contrast by moving one colour toward the light-muted or dark corner.
- **Functional?** Legible, consistent, guides the action, readable for common colour-vision deficiencies (don't rely on red vs green alone to carry meaning).
- **Appealing?** Does it deliver the feeling from Act 1?
- **Consistent** with any brand guidelines?
- **Answers the brief?** The brief becomes the rationale.

## Special cases

- **Client must-have colour** (D98): start minimal with the client colour plus a light neutral and a dark neutral. **Respect the colour's vibe**: for a warm peach, use a juicy warm brown and a soft beige rather than pure black and white. Then match it to a style (cottagecore, bright & warm, retro 70s, modern romantic) and expand. Don't force it into a style it doesn't fit (peach in "woodsy & rustic" sticks out).
- **Fixing a chaotic design** (eXc): list every colour, group them into 60/30/10 buckets, move the vivid ones to the 10% bucket, rebuild backgrounds from neutrals and the secondary, and simplify illustrations to primary and secondary colours with a touch of accent.
- **Colourful products** (Fender, Cowboy bikes, Oddbox-style cans): keep the interface quiet so the product is the hero. Don't copy every packaging colour into the UI (Pill and Biome show why).
- **Textiles or print-limited jobs:** fewer colours means fewer screens or dyes and lower cost. Check colours under the lighting they'll be sold and worn in (metamerism). Specify Pantone or TCX references where exact matching matters.

## Deliverable format

```
Palette: <name>  (harmony: <type>)
| Role | Name | HEX | RGB | Use for | Proportion |
|------|------|-----|-----|---------|------------|
| Primary / dominant | Warm Ivory | #F5F0E6 | 245,240,230 | backgrounds | 60% |
| Secondary | Deep Harbour | #1F3D5A | 31,61,90 | headings, nav, footer | 30% |
| Accent | Marigold | #F2A541 | 242,165,65 | buttons (Deep Harbour label), CTAs only; never as text on Ivory (1.8:1) | 10% |

Accessible pairs (≥4.5:1): <from audit>
Rules: <3–6 bullet rules>
Rationale: <2–4 sentences linking hue, value and saturation choices back to audience, action and feeling>
```

Show swatches visually when you can, e.g. an HTML or SVG swatch strip plus a 1000 px ratio bar split 600/300/100. For CMYK or Pantone equivalents, hand off to `colour-codes-and-conversion`.

## Put it to work in the person's tools

A palette is only finished when it's loaded where they design. Export it with the palette's own names:

```bash
python3 scripts/colour_tools.py export "Warm Ivory=#F5F0E6" "Deep Harbour=#1F3D5A" "Marigold=#F2A541" \
  --title "Harbour Cafe" --format ase --out harbour-cafe.ase     # Illustrator / Photoshop / InDesign
# --format css (Figma, web), canva (paste into a Canva brand kit), gpl (GIMP, Inkscape, Krita), json
```

Then follow `references/applying-in-tools.md` to apply it through whatever is connected: Canva brand kit or design, Adobe Express or Firefly, WordPress theme colours, or a Word or PowerPoint style guide.
