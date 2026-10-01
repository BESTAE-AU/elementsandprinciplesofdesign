# Colour Theory: Knowledge File

*Compiled 1 Oct 2026 for Claude Projects. A self-contained reference for colour theory across Graphics Technology, Multimedia, Visual Arts / Visual Design, Textiles and Design & Technology (NSW Stage 4–6). It also covers the four brand palettes used in Britt's work (BESTAE, MCCNS, MBE Creative Studio, Greyscale Workbooklet).*

**How to use this file**
- It holds the same content as the seven colour-theory skills: science, codes, palette building, contrast, harmony, psychology, teaching. If those skills are installed, prefer them for hands-on tasks. Mentions of `scripts/colour_tools.py` refer to the helper script inside the skills. Without it, calculate contrast with any WCAG checker.
- **Source codes** in brackets (e.g. *(oDn)*, *(Co75)*) are the first characters of each source video's YouTube ID. See section 10 for titles and links.
- Use Australian spelling. Contrast ratios are WCAG 2.x: **4.5:1** for body text, **3:1** for large text (24 px+, or 19 px+ bold) and UI marks.
- Treat colour-psychology claims as cultural tendencies, not laws. Never use colour as the only way to carry meaning.
- **Section 12 (brand palettes) is current as of 1 Oct 2026.** The live source of truth for each brand is its Claude design system (links in section 12).

## Contents
1. Colour science: light, eyes and materials
2. Demos and experiments
3. Colour codes: RGB, HEX, HSB, CMYK, Pantone
4. Vocabulary, harmonies and fixing problems
5. Building a palette: the 7-step process
6. Contrast and accessibility
7. Analysing a colour scheme
8. Colour psychology, meaning and brand rationale
9. Teaching colour theory: activities and question bank
10. Video map: the 20 source videos
11. Applying colour in Canva, Adobe and other tools
12. Brand palettes: BESTAE, MCCNS, MBE Creative Studio, Greyscale Workbooklet
13. Quick reference

## 1. Colour science: light, eyes and materials

The codes in brackets are sources (the first characters of each YouTube video ID). UZ5 and l8 are TED-Ed (Colm Kelleher), x7t is GPB *Physics in Motion*, af78 is the Royal Institution (Andrew Hanson, NPL), -b2 is The Visual Center and TGc is Barrett Kaufman.

### 1. What colour is (physics)
- Light behaves as a wave. **Colour is how we perceive the frequency/wavelength of light.** Low frequency (long wavelength) is red and high frequency (short wavelength) is violet. The continuous band between them is the **visible spectrum**. (UZ5, x7t)
- Humans see roughly **380/390–780/790 nm** (1 nm = one billionth of a metre). Beyond red is infrared and beyond violet is ultraviolet. The eye's lens filters UV because it would damage the retina. (x7t, af78)
- Visible light oscillates about **4×10¹⁴ times per second** ("400 million million"), far too fast to see as a wave. Analogy: a bobbing cork, where period is the time for one wave and frequency is waves per second. (UZ5)
- **Objects reflect some wavelengths and absorb the rest.** Absorbed energy becomes heat. White reflects all and black absorbs all. (UZ5, x7t)
- Newton showed that **white light is a mixture of all visible wavelengths**, and a prism refracts it into a spectrum. Black is the absence of light. (x7t)
- **Transparent** materials let all light through. **Translucent** ones diffuse it, so objects can't be seen clearly (e.g. frosted glass). **Opaque** ones let none through. (x7t)
- **Luminance** is light reflected from a surface (cd/m²). **Lumens** measure light output/brightness in a direction. **Watts** measure electrical power. Brightness falls with the square of distance from the source. (x7t)
- People can reportedly distinguish about **18 decillion** colours (an estimate). (x7t)
- **Three-stage process:** light source, then object (absorbs, reflects, transmits, scatters), then observer (eye or camera). (af78)

### 2. How we see colour (biology and perception)
- The retina has **rods** (about 120 million, one type, sensitive in low light, no colour) and **cones** (about 6–7 million, three types roughly sensitive to red, green and blue). (l8, x7t)
- **Red + green light looks yellow:** real yellow light stimulates both the red and green cones. Red and green light together send the *same signal*, so the brain sees yellow even though no yellow wavelength is present. With only three cone types, R, G and B can fake almost any colour, which is why TVs and screens only need RGB. (l8)
- **No colour in the dark:** only the rods are working, and one sensor type can only report light or no light. (l8)
- The eye is **most sensitive to green**, so less energy is needed for green to look as bright as red or blue. (af78)
- **Observer metamerism:** two people see the same pair of samples differently. **Sample (illuminant) metamerism:** two items match under one light but not another, e.g. clothes that match in the shop but not outside. Only samples with identical spectral reflectance match under all lights. (af78)
- **Afterimages and opponent colours:** stare at a colour, look away, and you see its opposite. Maxwell used afterimages to study colour vision. (af78)
- **CIE 1931 standard observer:** a model of human colour matching built from experiments with 17 observers. It is still embedded in cameras, screens, projectors and the traffic-light standard. (af78)
- **Colour blindness:** there are three types (three cone types can go wrong). Traffic-light colours are chosen so the common types don't confuse red and green lights. (af78)
- **Context changes perception:**
  - *Colour constancy*: the brain refers everything to the whitest thing in the scene. "The dress" is explained by different assumptions about the lighting.
  - *Memory colour*: "if it's a banana it must be yellow".
  - *Simultaneous contrast*: neighbours change each other. Van Gogh put green next to orange and yellow stars in blue skies.
  - The *checker-shadow illusion*: A and B are identical in shade.
  - *Size*: swatches mislead, because a small chip looks different from a whole wall.
  - *Ageing*: the lens yellows, so less blue is seen.
  - Colour sensitivity is concentrated in the central **2°** of vision (a thumbnail at arm's length). (af78)
- Our response to light is **non-linear**: equal steps of light energy don't look like equal steps of brightness. (af78)

### 3. Additive vs subtractive
| | Additive | Subtractive |
|---|---|---|
| Source | Light emitted | Light reflected/absorbed by pigment, dye, ink |
| Primaries | Red, Green, Blue | Cyan, Magenta, Yellow (+ Key/black) |
| Mix all | White | Black in theory. K is added because it's more efficient |
| More colour = | Brighter | Darker |
| Used by | Monitors, phones, TVs, cameras, scanners, projectors | Printers, paint, pastels, pencils, ink, dye |

(TGc, -b2, x7t)
- Secondary colours of light: R+G = yellow, R+B = magenta, G+B = cyan. **These are the subtractive primaries.**
- **Complementary colours of light** mix to white: green + magenta, blue + yellow, red + cyan. Each pair is one primary plus the secondary made from the other two. (x7t)
- **Coloured-shadow demo:** with R, G and B lights on a wall, a rod blocking the green light leaves a magenta (R+B) shadow. Subtracting one additive primary from white gives a subtractive primary. (-b2)
- A **colour model** is a system for making many colours from a small set of primaries. RYB is the traditional artist's wheel. CMY gives a larger mixing gamut. For digital colour management, RGB is what matters. (-b2)
- In film and photography, a "subtractive" look means the image gets darker (or at least not brighter) as it gets more colourful. (TGc)

### 4. Materials (useful for Textiles and Visual Arts)
- **Pigments:** usually inorganic, **insoluble**, suspended in a medium and sitting on the surface. Examples: cadmium sulfide (cadmium yellow), chromium(III) oxide (chrome green), iron(III) oxide (red ochre). (x7t)
- **Dyes:** traditionally from plants and insects. They **dissolve** in a medium and the material is soaked in it, so the dye bonds with the fibre. (x7t)
- **Chlorophyll** absorbs red and blue and reflects green. As leaves die, carotenoids show (orange), then anthocyanins (red to violet, changing with pH). The flower names "violet" and "pink" are also colour names. (x7t, af78)
- **Fluorescence:** absorbs high-energy (blue/UV) light and re-emits lower-energy light, which is why hi-vis vests look yellow under almost any light. **Specular reflection:** shiny surfaces mirror the light source's colour. (af78)

### 5. Why colour is measured (industry link)
Branding consistency across web, mugs, print and clothing. Quality control (car resprays, paint, orange juice that looks "off" on the shelf). Legal and safety requirements (road markings, traffic lights). The UK's National Physical Laboratory (NPL) does this work. (af78)

## 2. Demos and experiments

| Demo | What you need | Steps | Concept shown | Source |
|---|---|---|---|---|
| **Afterimage** | Projector or screen, image with inverted colours (e.g. a flag), white wall | Stare at the centre dot for 30 s without moving your eyes, then look at a white wall and blink | Opponent/complementary colours, cone fatigue | af78 |
| **Coloured shadows** | Three torches with R, G, B gels (or three phone screens set to pure R, G, B), a pencil or rod | Overlap all three on a white wall to get white. Hold the rod in front and ask students to predict each shadow's colour *before* revealing it | Additive mixing. Removing one primary from white gives C, M or Y | -b2 |
| **Screen zoom** | Phone camera macro, or a drop of water on a screen | Look closely at a white area of the screen | Screens are made of R, G, B sub-pixels | TGc, llA |
| **Prism spectrum** | Prism or old CD, bright white light | Split the light and name the order of colours | White = all wavelengths. Red has the longest wavelength and violet the shortest | x7t, af78 |
| **Coloured objects under coloured light** | Red and green tape, a spectrum or coloured torches | Move the objects through the spectrum and find the point where they look equally bright | Reflectance, green sensitivity, observer differences | af78 |
| **Hi-vis under blue light** | Hi-vis vest, blue torch | Shine blue light on it: it still looks yellow | Fluorescence | af78 |
| **Metamerism in textiles** | Fabric or thread pairs that nearly match; daylight, LED and fluorescent light | Compare the pairs under each light and record matches | Illuminant metamerism, why industry uses standard light boxes | af78 |
| **Checker-shadow illusion** | Image of Adelson's checker shadow | Ask "are A and B the same?", then mask the surroundings to reveal they are | Context and colour constancy | af78 |
| **Pigment vs dye** | Pigment paint and a fabric dye on calico | Paint one sample and dye one. Rub and wash both, then compare | Insoluble pigment sits on the surface; dye bonds with the fibre | x7t |
| **Leaf chromatography** | Leaves, alcohol, filter paper | Separate the pigments | Chlorophyll, carotenoids, anthocyanins | x7t, af78 |

### Hinge questions
1. A leaf looks green. Which wavelengths does it absorb? *(Mostly red and blue.)*
2. On a screen, which two sub-pixels light up to make yellow? *(Red and green.)*
3. Why does a printer have a black cartridge if C + M + Y makes black? *(It's more efficient and gives a truer black.)*
4. Two shirts matched in the shop but not in sunlight. What's this called? *(Illuminant/sample metamerism.)*
5. Blocking the blue light in an RGB shadow demo gives which shadow colour? *(Yellow: R + G.)*

## 3. Colour codes: RGB, HEX, HSB, CMYK, Pantone

### RGB
- Each channel (red, green, blue) runs 0–255, which is **256 levels** (0% to 100% intensity). It suits screens because pixels are made of R, G and B sub-pixels.
- Format: `rgb(R, G, B)`. Pure red is `rgb(255, 0, 0)` and pure blue is `rgb(0, 0, 255)`.
- Darker versions of a colour have **lower numbers across the board**. A colour with no black in it has at least one channel near 255.

### HEX (hexadecimal, base 16)
- `#RRGGBB`: two digits each for red, green and blue. It's **just another way of writing RGB**. At 7 characters it's much shorter than the ~17 characters of `rgb(...)`, so it's used in CSS and JavaScript.
- Why base 16? 256 = 16 × 16, so each channel fits exactly in two base-16 digits.
- Digits: 0–9, then A = 10, B = 11, C = 12, D = 13, E = 14, F = 15. **A hex code can never contain G–Z.**
- Shorthand: `#FA0` means `#FFAA00`.

#### RGB → HEX by hand (per channel)
1. Divide the value by 16.
2. The whole-number part is the **first digit** (convert 10–15 to A–F).
3. Multiply the remainder (the decimal part) by 16. That's the **second digit**.

Worked example, `rgb(184, 52, 224)`:
- Red 184 ÷ 16 = 11.5. 11 = **B**, and 0.5 × 16 = **8**, giving **B8**.
- Green 52 ÷ 16 = 3.25. **3**, and 0.25 × 16 = **4**, giving **34**.
- Blue 224 ÷ 16 = 14. 14 = **E**, and 0 × 16 = **0**, giving **E0**.
- Result: **#B834E0**, a bright purple leaning blue.

#### HEX → RGB by hand
Each pair = (first digit × 16) + second digit. `B8` = 11 × 16 + 8 = 184.

### HSB / HSL
Hue (0–360° around the wheel), Saturation (grey to vivid), Brightness (HSB) or Lightness (HSL). This is how designers refine a colour in Illustrator or Figma: lowering saturation adds grey, lowering brightness adds black (a shade), and in HSL raising lightness adds white (a tint). (Co75)

### CMYK
- Cyan, magenta, yellow and key (black), each written as a percentage. The four channels match the four printing plates.
- Format: `cmyk(59%, 0%, 24%, 31%)`. A higher K means darker.
- Converting from screen colour depends on the colour profile and paper, so any formula is approximate.

### Pantone
- An industry-standard colour-matching system for reproducing colour exactly across printers and factories.
- The same ink looks different on **coated vs uncoated** stock, so Pantone swatches specify the substrate (e.g. "C" vs "U").
- Essential for packaging, merchandise and brand guidelines. A brand identity deck should show HEX, RGB and CMYK for each colour, plus a Pantone slide if there's packaging. (9jm)

## 4. Vocabulary, harmonies and fixing problems

### Vocabulary (YeI, _2LL, x0s)
- **Hue:** colour family or position on the wheel. The traditional RYB wheel has 12 main hues (primary, secondary, tertiary).
- **Saturation** (intensity, chroma): vivid to greyed-out.
- **Value** (lightness, luminosity): light to dark.
- **Tint** = + white. **Shade** = + black. **Tone** = + grey.
- **Temperature:** warm (red, orange, yellow) feels energetic and cosy, and is harder to use over large areas. Cool (green, blue, violet) feels calm and clean, and works at scale (blue and purple suit big backgrounds). Individual hues shift too: a warm red leans to yellow, a cool red to blue.
- **3×3 spectrum grid** (oDn): luminosity (light, medium, dark) × saturation (muted, midtone, bright). The centre cell (medium midtone) is the **danger zone** for contrast.

### Harmonies (YeI, _2LL, x0s, Co75)
| Harmony | Construction | Character | Tip |
|---|---|---|---|
| Monochromatic | One hue, varied tints, tones and shades | Cohesive, guaranteed to match | Low contrast, so less ideal for marketing. Film example: *The Grand Budapest Hotel* pink |
| Analogous | 2–4 neighbours on the wheel | Calm, natural | One dominant colour plus accents. *Kung Fu Panda* |
| Complementary | Opposites (red/green, blue/orange, purple/yellow) | Strong contrast, vibrant | About **80/20**, never 50/50. Vary tint and tone. *Blade Runner 2049* |
| Split-complementary | Hue + the two either side of its complement | Contrast with more variety | One dominant colour |
| Triadic | Three evenly spaced hues | Bold, striking | Primary triads are most vibrant. Secondary or tertiary triads can look muddy |
| Tetradic (rectangle) | Two complementary pairs | Rich, hardest to balance | Let one colour dominate and test a lot |
| Square | Four evenly spaced hues | Powerful or overwhelming | About 80% dominant, 20% accents. *Inside Out* |
| Double split-complementary | e.g. yellows and oranges opposite blues and purples | Rich | Needs finessing (Headspace) |
| One colour + black and white | Single hue with neutrals | Sharp, iconic | Dortmund, Inter Milan, Notion's red CTA on a black-and-white site |

General tips: pick **one dominant colour**, use **few colours**, and borrow palettes from nature, art and ads, then make them your own.

### Fixing problems (_2LL, eXc)
- **Vibrating colours** (two saturated colours of similar value side by side, e.g. pink on vivid blue): change the lightness, darkness or saturation of one, or swap the accent.
- **Unreadable text:** go back to black/near-black or white/near-white text. Don't set type in saturated colours.
- **Too busy:** add neutrals (black, white, grey, beige) so the remaining colour stands out.
- **Wrong mood:** bright feels fun and modern, desaturated feels business-like. Shift the saturation before changing the hue.

### Worked 60-30-10 analysis (eXc)
Paul Rand poster: about 60% white, 25% yellow, 10% red and green, 5% blue and black. Lots of hues work because each is used sparingly. Exercise: draw a 1000 px bar and split it 600/300/100 before designing.

### Contrast rules (oDn)
- Contrast is the *difference between two colours*. One colour alone has no contrast.
- WCAG scale: 1:1 (identical) to 21:1 (black on white). The ratio is the same whichever colour is the background.
- **4.5:1** is the minimum for body text, 3:1 for large text and UI graphics, and 7:1 is the AAA level.
- 4-step balance process: (1) choose the vibe or mood board, (2) add colours that fit, (3) check there's at least one light and one dark, (4) test all pairs.

### Brand examples to cite (Co75)
- **Good:** Fender and Cowboy (quiet UI, colourful product), Sweetgreen (analogous greens, a small yellow accent for the CTA), Notion (a red CTA on black and white), Stripe (a gradient adds appeal to a technical product), Burts Crisps and Oddbox-style cans (colour codes the flavour), Brooklyn Brewery Pulp Art (summery, tones match).
- **Overloaded:** Pill, Biome (too many interface colours competing with the packaging).

## 5. Building a palette: the 7-step process

A palette is a set of colours **with jobs**: every colour has a role, a proportion and rules for where it goes. (Flux Academy Co75, The Futur eXc / V-SD, The Colour Palette Studio oDn / D98.)

### Act 1: Build the brief (don't skip this)

Get answers to these four questions from the person, or infer them and state your assumptions:
1. **Constraints:** existing brand guidelines? A must-use colour? Print limits (spot colours, one-colour screen print, fabric dye)? Accessibility requirements?
2. **Guidance:** existing materials, a written brief, a mood board, competitors?
3. **Action:** what should the viewer *do* (buy, sign up, read, find the exit)?
4. **Feeling:** what should they *feel*, and what moment are they in? Who is the audience (age, culture, place)?

If the brief is thin and the stakes are real (a client brand or an assessed project), ask 2–3 targeted questions before building. For a quick exploration, state the assumptions and go.

### Act 2: Select colours

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

### Act 3: Rules and review

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

### Special cases

- **Client must-have colour** (D98): start minimal with the client colour plus a light neutral and a dark neutral. **Respect the colour's vibe**: for a warm peach, use a juicy warm brown and a soft beige rather than pure black and white. Then match it to a style (cottagecore, bright & warm, retro 70s, modern romantic) and expand. Don't force it into a style it doesn't fit (peach in "woodsy & rustic" sticks out).
- **Fixing a chaotic design** (eXc): list every colour, group them into 60/30/10 buckets, move the vivid ones to the 10% bucket, rebuild backgrounds from neutrals and the secondary, and simplify illustrations to primary and secondary colours with a touch of accent.
- **Colourful products** (Fender, Cowboy bikes, Oddbox-style cans): keep the interface quiet so the product is the hero. Don't copy every packaging colour into the UI (Pill and Biome show why).
- **Textiles or print-limited jobs:** fewer colours means fewer screens or dyes and lower cost. Check colours under the lighting they'll be sold and worn in (metamerism). Specify Pantone or TCX references where exact matching matters.

## 6. Contrast and accessibility

### Thresholds (WCAG 2.x)

| Ratio | Meaning |
|---|---|
| ≥ 7:1 | AAA: best for long reading and low-vision users |
| ≥ 4.5:1 | **AA for body text**, the standard minimum from the source video |
| ≥ 3:1 | Large text (about 24 px regular or 19 px bold and up) and UI parts such as icons and input borders |
| < 3:1 | Fail. Decorative use only |

The scale runs from 1:1 (same colour) to 21:1 (black and white). The ratio is identical whichever colour is the background.

### Reading the result

A **balanced palette** has at least two colours, **at least one light and one dark** colour, and at least one pair at 4.5:1 or higher. If the only light and dark colours sit in the **danger zone** (medium luminosity with midtone saturation), expect no accessible pairs.

### Fixing failures: the smallest change first

1. Keep the hue and move **one** colour's lightness away from the other: lighter toward the light-muted corner, darker toward the dark corner. Re-run `contrast` after each nudge. Report the new hex and ratio. (oDn: moving a pink toward light-muted took a pair from 3.14 to 5.32.)
2. If the colour is a brand colour that can't move, change its **partner** instead (e.g. use a near-black warm brown instead of the mid-tone text).
3. If a pair still fails, restrict it: large headings only, decorative only, or never together.
4. Don't let colour carry meaning alone. Add icons, labels or underlines, because red vs green is invisible to common colour-vision deficiencies.

## 7. Analysing a colour scheme

### Steps

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

### Reference examples (x0s, Visme)

| Work | Harmony | Why it works |
|---|---|---|
| *Blade Runner 2049* poster | Complementary (orange/teal-blue) | Dramatic contrast, with one colour dominant |
| *Kung Fu Panda* poster | Analogous warm (red, orange, yellow) | Warm, energetic, unified |
| *The Grand Budapest Hotel* | Monochromatic pink | Cohesive, whimsical, but low contrast |
| *Inside Out* poster | Square (one colour per emotion) | Works because of the dominant background and the character-coded colours |
| Headspace | Double split-complementary (yellow/orange vs blue/purple) | Friendly and rich, and finessed with tints |
| Paul Rand poster | Many hues, mostly white (~60%) | Each hue is used sparingly (eXc) |
| Borussia Dortmund | One colour + black and white | Iconic and instantly recognisable |

### Writing it up

- **Quick:** name the harmony, give the evidence (which hues and where), then the effect.
- **Folio or annotation:** use the pattern *identify, then describe, then explain the effect on the viewer, then justify or evaluate*. Use subject vocabulary (hue, value, saturation, tint, shade, tone, warm/cool, dominant, accent, contrast). Keep it in the student's voice if you're modelling student work, and label it as a model.
- **Comparing two works:** use a table (harmony, dominant hue, value range, saturation, temperature, mood, how colour directs the eye).

For accessibility or legibility of text in the work, also run `colour-contrast-audit`. For meanings of individual colours, see `colour-psychology-rationale`.

## 8. Colour psychology, meaning and brand rationale

### Principles to state honestly

- Colour associations are **tendencies shaped by culture and context, not laws**. Effects of a single colour in isolation are modest. Say so when the person treats a claim as fact.
- **Colour never works alone** (Co75). Type, layout and imagery must all point the same way for the intended mood to land.
- The same hue changes meaning with **saturation and value**: bright feels youthful and fun, muted feels mature and premium, dark yellow can feel sickly, and hot pink is not the same as blush.
- **Culture, place and audience** can reverse a meaning: political parties, religions, sports teams, mourning colours. Flag any that are relevant to the design's location.
- Research claims from the source videos should be attributed as reported findings ("one study found…"), not stated as universal truths. That includes the red-before-a-test and black-uniform-penalty studies and the "up to 90% of first impressions" figure.

### Workflows

#### A. Choose a colour for a brand or project (WjQ's 5 steps, plus Co75)
1. **Personality:** 3–5 adjectives for the brand (playful, sleek, trustworthy…).
2. **Audience:** who they are, what they should feel and what they should do.
3. **Shortlist 2–3 hues** from `references/meanings.md` that match. Note the risks and the competitor colours in the category (a new cola would face Coca-Cola red).
4. **Tune it** (HSB) for the audience, then **test**: mock-ups, A/B comparisons and feedback.
5. **Consistency:** apply it everywhere. Then **tell the story**: what the colour means for *this* brand.

Hand off to `colour-palette-builder` to grow the chosen hue into a full palette.

#### B. Write a colour rationale (design justification, folio, pitch)
Use this structure, 80–200 words per colour or for the palette:
1. **Brief link:** audience, purpose, desired feeling or action.
2. **Choice:** the colour name and hex code, and its role (dominant, secondary or accent, with proportion).
3. **Why:** the psychological or cultural association, plus the specific *value and saturation* decision, plus an example of a comparable brand.
4. **Function:** contrast and legibility (cite ratios if you have them), how it guides action (e.g. the accent is reserved for CTAs), and print or textile reproduction (CMYK or Pantone, metamerism).
5. **Evaluation:** any trade-off or risk and how it was managed.

When writing for a student, match their stage level and voice, and label it as a model or scaffold. Don't write assessable work for them to submit as their own.

#### C. Critique a brand's colour
Consider fit with personality and audience, differentiation from competitors, consistency across touchpoints, legibility, and cultural fit. Contrast it with the case studies in `references/meanings.md`: successes (McDonald's, Tiffany, Netflix, Starbucks) against failures (Pepsi 2009, Katy Perry's *Witness*).

#### D. Brand identity deck: colour section (9jm, Jack Watson)
- Deck order: introduction (goals and problem), then brand overview (strategy and audience), then wordmark and logo breakdown (with reasons), then **colour and typography** (how they express personality), then brand in action (mock-ups). This order builds trust and cuts revisions.
- Colour slides: split-grid blocks for each colour showing **HEX, RGB and CMYK**, a short rationale beside them, a **Pantone** slide if there's packaging, then an in-use slide.
- Illustrator setup: 1920×1080 artboards. Grid from a rectangle 120 px in from the top and bottom, then *Object › Path › Split Into Grid* for 6 rows × 12 columns with 30 px gutters, then convert to guides (Cmd+5). Type scale: start at 12 pt and multiply by 1.618. Global palette changes via *Edit › Recolor Artwork*.
- Hand off to `colour-codes-and-conversion` for the code values.

### Everyday applications (mpK)
- Study spaces: avoid red, prefer calm greens, greys and whites.
- Kitchens: yellow for cheer.
- Relaxing rooms: blue.
- Shopping: notice the orange and red "buy now" buttons designed to prompt urgency. Good for a media-literacy discussion.


Sources: mpK (Psych2Go), WjQ (Ana The Marketeer), x0s (Visme), 6Ten (Lindsay Marsh), Co75 (Flux Academy).

| Colour | Common associations | Typical uses | Cautions and notes |
|---|---|---|---|
| **Red** | Energy, passion, urgency, appetite, love, excitement, danger, anger | CTAs, fast food and drink (McDonald's, Coca-Cola), Netflix, stop signs, sale tags | Grabs attention and is easily overused. Raises heart rate. One study found students shown a red participant number before a test scored about 20% lower than those shown green. Meaning can be positive or negative, so clarify it with words |
| **Orange** | Enthusiasm, creativity, adventure, vitality, urgency | "Buy now" buttons, outdoor and adventure brands | Bright orange for highlights, a shaded orange for warm backgrounds. Pairs with blue (complements). Spiritual enlightenment in Buddhism |
| **Yellow** | Optimism, happiness, youth, logic and creativity, caution | Children's products, IKEA, Snapchat, McDonald's arches, hazard signs | Hard to read as text or on white. Easily overused (with pink, the least-used colour in design). Dark yellows can feel sickly. Can signal anxiety, so it's rare in healthcare |
| **Green** | Nature, growth, health, freshness, clean, money, calm | Eco ("going green"), cleaning, finance and stock gains, Starbucks, healthcare | Easy on the eyes and good for focus. New beginnings and happiness in India, paradise in Islam |
| **Cyan** | Clean and organic plus calm, optimism | Biotech, startups | Less common, so it can differentiate |
| **Blue** | Trust, stability, calm, intelligence, loyalty, professionalism | Banks, tech (Facebook, LinkedIn, Samsung), healthcare, corporate, uniforms | The most-used brand colour and the most-preferred colour overall. Works in large areas. Can mean sadness ("feeling blue") or coldness. Lighter is gentle, darker is authoritative |
| **Purple / violet** | Royalty, luxury, mystery, spirituality, wisdom, sophistication | Cadbury, Hallmark, hospitality, some healthcare, youthful gradients | Historically a rare and expensive dye. Complements yellow (purple dominant, yellow as highlight). Use sparingly unless the brand is regal or spiritual |
| **Pink** | Care, nurture, compassion, romance, calm, playfulness | Cosmetics, baby products, gifts, some tech | Calming (used in some prisons and hospitals). The gender stereotype is fading, but research the audience. Light pinks work in large areas, hot pinks don't |
| **Brown** | Earthy, reliable, natural, comfortable, grounded | Hershey's, UPS, kraft packaging, natural-ingredient products | The tint must look clean, not dirty |
| **Black** | Power, elegance, luxury, authority, formality, mourning | Chanel, Nike, premium cards and cars | One study found teams in black uniforms receive more penalties. A strong background with bright foregrounds |
| **White** | Purity, cleanliness, minimalism, clarity | Apple, hospitals, labs, bridal wear | White space stops designs feeling overwhelming. Mourning colour in some East Asian cultures |
| **Grey** | Neutral, balanced, timeless, professional | Backgrounds, UI | Lets other colours shine. Can feel dull if it's the only colour |
| **Silver / gold / metallics** | Modern, high-tech, glamour, prestige | Tech, cars, luxury | Hard to reproduce on screen and paper, so talk to the printer about special inks or foils |

### Brand case studies (WjQ)
- **McDonald's (red and yellow):** red grabs attention and is linked with appetite, and yellow adds happiness. The result feels fast, fun and satisfying. The logo stayed red and yellow even as interiors went muted.
- **Tiffany & Co. (Tiffany blue):** chosen in the 19th century to stand out. The colour is now *trademarked* and stands for exclusivity and trust.
- **Netflix (red and black):** excitement plus a cinematic, dramatic feel. The palette was kept from DVD rental to global streaming.
- **Starbucks (green):** growth, health and sustainability, even for sugary drinks.
- **Pepsi 2009 (failure):** a pale, pastel blue rebrand meant to feel modern looked less trustworthy and didn't stand out next to Coca-Cola red. Pepsi moved back to a bolder blue.
- **Celebrity "eras":** Taylor Swift's *Red* (heartbreak, passion), Charli XCX's neon green *brat* (bold, experimental, became a meme), Beyoncé's silver *Renaissance* (futurism, elegance). **Katy Perry's *Witness*** switched to black and white and didn't match fans' expectation of bold, playful colour (a failure).
- Claim to attribute: "up to 90% of first impressions of a brand are based on colour alone" (a reported figure).

### Industry quick-picks (6Ten, mpK)
- Finance: blue, green
- Healthcare: blue, green, purple (avoid yellow)
- Food: red, yellow, orange
- Eco: green, brown
- Luxury: black, purple, gold
- Kids: yellow, bright primaries
- Tech: blue, cyan, purple gradients
- Hospitality: purple
- Cleaning: green, blue, white

## 9. Teaching colour theory: activities and question bank

| Activity | Concept | Source | Steps | Extension |
|---|---|---|---|---|
| **Afterimage experiment** | Opponent colours, cone fatigue | af78 | Show an inverted-colour flag. Students stare at the centre dot for 30 s, then look at a white wall. Record the colours they see and match them to complements on the wheel | Explain why designers use complementary pairs for maximum contrast |
| **Coloured-shadow prediction** | Additive mixing | -b2 | Three R, G, B torches (or phone screens) at a wall. Students predict each shadow colour on a mini whiteboard before the reveal | "How are the yellow and cyan shadows made?" (the video's own challenge) |
| **Red + green = yellow puzzle** | Cone signals | l8 | Show overlapping R and G light. Ask "where's the yellow light?" Watch l8 and explain it in one sentence | Link it to screen sub-pixels (zoom in on a phone screen) |
| **Hex-code maths challenge** | Base 16, RGB to HEX | llA | Convert 3 random RGB colours by hand (÷16, remainder ×16), then check in Illustrator or Photoshop | Hex to RGB in reverse. Why can a hex code never contain G? |
| **RGB vs CMYK sort** | Additive vs subtractive | TGc, -b2, x7t | Card sort: monitor, printer, projector, paint, camera, scanner, pencils, TV, fabric dye | Why do bright screen colours look dull when printed? (gamut) |
| **Colour wheel build** | Primary, secondary, tertiary; tint, shade, tone | YeI, _2LL | Paint or digitally build a 12-hue wheel, then one hue as a tint, shade and tone strip | Warm vs cool versions of the same hue |
| **Palette ratio bar** | 60-30-10 | eXc, V-SD | Draw a 1000 px bar split 600/300/100 with the palette before designing a poster or web page | Analyse a Paul Rand poster's ratio (≈60/25/10/5) |
| **Pairing grid** | Rules of use | eXc | For each background colour, test text, link and button colours. Keep what's legible and write the rules down | Redesign a chaotic landing page using only the rules |
| **Contrast audit** | WCAG 4.5:1 | oDn | Test every text and background pair in a palette (or the school website) with a checker. Keep ≥ 4.5 | Fix a failing pair by moving one colour's lightness. Record the before and after ratios |
| **Danger-zone sort** | 3×3 luminosity × saturation grid | oDn | Place swatches on the 3×3 grid. Find the palettes with no light or no dark colour | Build a balanced two-colour palette from opposite corners |
| **Film-poster harmony hunt** | Harmonies | x0s | Identify the harmony in *Blade Runner 2049*, *Kung Fu Panda*, *Grand Budapest Hotel* and *Inside Out* posters | Find their own example and justify the proportion (80/20) |
| **Brand colour case study** | Psychology and branding | WjQ | Compare McDonald's, Tiffany, Netflix and Starbucks with Pepsi 2009, then justify a colour for a student brand using the 5 steps | Katy Perry *Witness* vs Beyoncé *Renaissance*: colour as an era |
| **Client colour challenge** | Building around a must-use colour | D98 | Give a random "client colour". Students build a minimal (colour + light neutral + dark neutral) and an expanded palette that respects its vibe | Show what not to do: put it in a mismatched style |
| **Same hue, two audiences** | HSB refinement | Co75 | One green for a teen streetwear brand and one for a 40s mature brand. Adjust only saturation and brightness | Present the rationale linked to the brief questions |
| **2-3-4 colour build-up** | Emotion and combinations | 6Ten | Make 2-, 3-, then 4-colour combos and reflect on the emotion each creates | Warm and cool contrast vs analogous calm |
| **Metamerism in textiles** | Illuminant metamerism | af78 | Compare fabric or thread pairs under daylight, LED and fluorescent light, and record matches | Why do industries use standard light boxes and Pantone TCX? |
| **Pigment vs dye** | Materials | x7t | Paint one calico sample with pigment and dye another. Rub and wash both, then compare | Link to natural dyeing (plants, insects) and fabric printing units |
| **Checker-shadow and "the dress"** | Colour constancy | af78 | Show the illusion, then mask it to reveal A = B. Discuss why people saw the dress differently | Implications for product photography and online shopping |
| **Everyday colour audit** | Applied psychology | mpK | Photograph 5 "buy now" buttons, signs or rooms and explain their colour choices | Design the colour scheme for a study space and justify it |

### Quick-recall question bank
1. Which colour of visible light has the longest wavelength? *(Red.)*
2. What are the additive primaries? And the subtractive? *(RGB. CMY(K).)*
3. Tint, shade, tone: what is added to each? *(White, black, grey.)*
4. What is the minimum WCAG contrast ratio for body text? *(4.5:1.)*
5. Convert `rgb(255, 0, 0)` to hex. *(#FF0000.)*
6. Name the harmony: blue and orange. *(Complementary.)*
7. In 60-30-10, what is the 10% for? *(Accent: calls to action.)*
8. Why does a black T-shirt get hot in the sun? *(It absorbs all wavelengths and the energy becomes heat.)*
9. What is the difference between a pigment and a dye? *(Pigment is insoluble and suspended on the surface. Dye dissolves and bonds with the fibre.)*
10. Why did Pepsi's 2009 pale-blue logo fail? *(It looked less trustworthy and didn't stand out against Coca-Cola red.)*

## 10. Video map: the 20 source videos

Source codes are the first characters of each YouTube ID.

### Playlist A: colour science and theory basics
https://www.youtube.com/playlist?list=PLfZQYiOZUy0NKt00f9VzNUiugipoVOu2b

| Code | Title (channel, length) | URL | Best for |
|---|---|---|---|
| l8 | How we see color (TED-Ed, ~3.5 min) | https://www.youtube.com/watch?v=l8_fZPHasdo | Rods and cones, red + green = yellow, why TVs use RGB |
| YeI | Color Theory Basics: Color Wheel & Harmonies (Sarah Renae Clark, ~6.5 min) | https://www.youtube.com/watch?v=YeI6Wqn4I78 | Primary, secondary, tertiary; hue, saturation, value, temperature; 6 harmonies; tips |
| _2LL | Beginning Graphic Design: Color (GCFGlobal, ~6 min) | https://www.youtube.com/watch?v=_2LLXnUdUIc | Harmonies, do's and don'ts (vibrating colours, readability, neutrals) |
| TGc | Additive vs Subtractive Color Theory Pt 2 (Barrett Kaufman, ~2 min) | https://www.youtube.com/watch?v=TGcuO44te5A | Flashlight analogy, printer CMYK, "subtractive" in film |
| UZ5 | What is color? (TED-Ed, ~3 min) | https://www.youtube.com/watch?v=UZ5UGnU7oOI | Waves and frequency (cork), reflect vs absorb |
| x7t | What Is Color? Physics in Motion (GPB, ~9.5 min) | https://www.youtube.com/watch?v=x7tpOkfNIHE | Spectrum in nm; transparent, translucent, opaque; lumens vs watts; chlorophyll; additive complements; pigment vs dye |
| -b2 | Color Models Explained (The Visual Center, ~6.5 min) | https://www.youtube.com/watch?v=-b2pAEHEQZc | Colour models, coloured-shadow demo, CMY vs RYB gamut |

### Playlist B: applying colour in design, branding and psychology
https://www.youtube.com/playlist?list=PLfZQYiOZUy0OJN-XLq86AJPUapDGUagWT

| Code | Title (channel, length) | URL | Best for |
|---|---|---|---|
| eXc | How to Apply a Color Palette to Your Design (The Futur, ~13 min) | https://www.youtube.com/watch?v=eXcKOqviLE0 | 60-30-10 ratio bar, Paul Rand poster, pairing grid, fixing a landing page |
| D98 | How to Turn a Color into a Brand Color Palette (Color Palette Studio, ~8 min) | https://www.youtube.com/watch?v=D98e7wllIGg | Client must-have colour, warm neutrals, style matching |
| oDn | How to Balance a Color Palette (Color Palette Studio, ~12 min) | https://www.youtube.com/watch?v=oDnjzPMFQMg | WCAG 4.5:1, 1–21 scale, 3×3 grid, danger zone, 4 steps |
| llA | How Graphic Designers Quantify Color (Color Palette Studio, ~17.5 min) | https://www.youtube.com/watch?v=llAPurpYuo4 | RGB, hex maths worked example, CMYK, Pantone |
| Co75 | How To Select Colors: Step By Step (Flux Academy, ~41 min) | https://www.youtube.com/watch?v=Co75kmQtbaA | Full process: brief, hue, HSB, palette, tone matching, rules, review; many brand examples |
| V-SD | The 60-30-10 Rule (The Futur, ~2 min) | https://www.youtube.com/watch?v=V-SD_zV9S2c | Quick ratio explainer |
| KMS | How to Choose Colors: Easy 3-Step Process (Flux Academy) | https://www.youtube.com/watch?v=KMS3VwGh3HY | ⚠ No usable transcript. Chapters: dominant colour, add two more, apply. Preview before use |
| 9jm | Brand Identity Presentation in Illustrator (Jack Watson, ~14.5 min) | https://www.youtube.com/watch?v=9jmOg0i5Jwo | Deck order, grid, golden-ratio type, HEX/RGB/CMYK/Pantone slides, Illustrator shortcuts |
| mpK | Every Color Psychology Explained in 8 Minutes (Psych2Go) | https://www.youtube.com/watch?v=mpK3A_m1-rE | 13 colours, research snippets, everyday uses |
| WjQ | Color Psychology in Marketing & Branding (Ana The Marketeer, ~11.5 min) | https://www.youtube.com/watch?v=WjQqVzDcgfA | Brand case studies, celebrity eras, Pepsi and Katy Perry failures, 5 steps |
| x0s | Marketing Color Psychology (Visme, ~14 min) | https://www.youtube.com/watch?v=x0smq5ljlf4 | Tints, shades and tones; warm and cool; harmonies with film posters; 80/20; metallics |
| af78 | The Physics and Psychology of Colour (Royal Institution, ~36 min) | https://www.youtube.com/watch?v=af78RPi6ayE | Metamerism, fluorescence, CIE 1931, colour blindness, afterimages, constancy, illusions |
| 6Ten | The Psychology of Color in Design (Lindsay Marsh, ~8.5 min) | https://www.youtube.com/watch?v=6Ten8xjkXhw | Colours by industry, warm vs cool at scale, 2-3-4 colour exercise |

## 11. Applying colour in Canva, Adobe and other tools

These skills produce **tool-neutral results**: named hex codes with roles, proportions, pairing rules and a rationale. This guide explains how to carry those results into whatever the person designs in. The same process works for any plugin or connector.

### Ground rules

1. **Discover, don't assume.** Connectors differ between accounts and change over time. Look for tools by keyword (e.g. search "canva brand", "adobe colour", "express", "wordpress theme") before promising anything. Use the tool names below as examples, not guarantees.
2. **Do the colour thinking first, then apply it.** Settle the palette, its roles and contrast checks with these skills *before* calling a design tool. Design tools execute; they don't replace the rules. Give the tool the same hex codes, roles and 60-30-10 proportions.
3. **Follow each connector's own rules.** Some servers require an initialisation or playbook call first (Adobe for creativity: `adobe_mandatory_init`, then `create_visual_design_express_skill` for any visual design). Read and obey the playbook it returns.
4. **Ask before anything outward-facing or hard to undo:** publishing a Canva brand template, overwriting a brand kit, changing a live WordPress theme, sharing files.
5. **Re-check after applying.** Export or preview the result and audit the real colours (`colour_tools.py audit`). A tool may have substituted or tinted them.
6. **No connector? Hand over files.** Use `colour_tools.py export` for `.ase`, `.css`, `.gpl`, `.json` or a Canva paste list, plus written steps for applying them by hand.

### Handover pack (produce this before any tool call)

```
Palette name, harmony
Role | Name | HEX | RGB | (CMYK / Pantone if print) | proportion | allowed on
Pairing rules: bg -> text / link / button (from audit, ratios shown)
Don'ts: e.g. accent never as body text, no pink on blue
Mood words (3-5) and fonts, if chosen
```

### Canva (connector)

- **Read the existing brand first:** `list-brand-kits`. If the brand has a kit, build around its colours rather than inventing new ones (treat it as a "client must-have colour" in `colour-palette-builder`).
- **New designs:** `generate-design` / `generate-design-structured` or `create-design`. Put the handover pack in the prompt: hex codes with roles, "60% #…, 30% #…, 10% accent #… for buttons only", and the text colour rules.
- **Existing designs:** `read-design`, then `edit-design` to recolour according to the rules. `get-design-dataset` / `autofill-design` for data-driven templates.
- **Brand templates:** `create-brand-template-draft`, then `publish-brand-template` only after the person confirms.
- **Colour review of a design:** `read-design` or `export-design` (PNG), then estimate the colours, then use `colour-harmony-analyser` and `colour-contrast-audit`, then `comment-on-design` with concrete fixes (hex, ratio, where).
- Canva brand kits can't be written through every connector. If there's no write tool, give the `--format canva` list for pasting into *Brand › Colours*.

### Adobe (Adobe for creativity connector: Express, Firefly, Photoshop-style image tools, fonts)

- **Start:** `adobe_mandatory_init`, then `create_visual_design_express_skill` for posters, slides, social posts and similar. Author the design with the palette as CSS custom properties (`colour_tools.py export --format css`), then use `export_html_to_express` after its readiness check.
- **Recolour images to the palette:** `image_apply_color_overlay`, `image_apply_monochromatic_tint` (monochromatic schemes, duotone-style), `image_adjust_hsl` / `image_adjust_single_color_saturation` (tone-matching photos to the palette's saturation), `change_background_color`, `image_adjust_color_temperature` (warm/cool mood).
- **Type to match the mood:** `font_recommend`, `suggest_type_palettes` / `get_type_palette`.
- **Mood boards:** `create_firefly_board`, `boards_add_items_to_board`. Add the swatch strip and ratio bar next to the imagery.
- **Illustrator / Photoshop / InDesign desktop** (no direct connector): give the `.ase` file. Load it via *Swatches panel › Open Swatch Library › Other Library* (Illustrator) or *Swatches › Import Swatches* (Photoshop). In Illustrator, *Edit › Edit Colors › Recolor Artwork* applies a palette globally, which is useful for brand decks (see `colour-psychology-rationale`).
- **Print:** state that CMYK values from the script are approximate and that the document profile or printer decides. Recommend Pantone for packaging.

### Other connectors that often exist

| Tool | Use it to |
|---|---|
| WordPress.com | Read `theme.presets` in the site editor context, then map palette roles to the theme's colour slots (background, foreground, primary, secondary, accent). Draft changes and preview before publishing. Run a contrast audit on the pairs the theme will actually use |
| Unsplash | Find imagery for the mood board that fits the palette's hue and temperature. Describe the colours in the search ("muted teal, warm beige, soft light") |
| Microsoft 365 / Google Drive / Dropbox | File the palette handover, `.ase` and style-guide doc where the person keeps resources. Follow any filing skill they have (e.g. a knowledge-sync or Dropbox resource skill) |
| Word / PowerPoint skills (docx, pptx) | Style guides, colour slides (HEX, RGB, CMYK, Pantone per swatch) and student handouts |
| Figma (if connected) or any CSS tool | Paste the `--format css` variables or create colour styles named by role |
| Shopify | Map the palette to theme settings (buttons get the accent) and check contrast on product pages |

### Teaching resources and greyscale printing

If a resource will be printed in greyscale (e.g. with a greyscale print design system), colour can't carry meaning on the page:
- Label every swatch with its **name and hex code**.
- Show harmonies as **wheel diagrams with labelled positions**, not colour alone.
- Use value (light/dark) tasks, which print well.
- Put the full-colour version in the digital copy, Canvas page or slide deck.

## 12. Brand palettes (current as of 1 Oct 2026)

Each brand has its own Claude design system. Read it for full detail.

| Brand | Purpose | Design system |
|---|---|---|
| BESTAE | Britt's teaching brand: domain-of-learning colours | https://claude.ai/artifact/9M7CWe736AqQGqWXudNdT6 |
| MCCNS | Marist Catholic College North Shore school brand (2020 guidelines, never altered) | https://claude.ai/artifact/G6i4tRCPKbEKhM5PwcBNF5 |
| MBE Creative Studio | Britt's freelance creative business | https://claude.ai/artifact/2ptfHF8cDnoeLt3RDdtzWi |
| Greyscale Workbooklet | Print layer for worksheets, booklets and exams | https://claude.ai/artifact/AHsqwt586J6rMJDpkqSdL8 |

**How they combine:**
- BESTAE and MBE never mix.
- In school resources, MCCNS is the frame (logo, header and footer bars, titles) and BESTAE domain colours sit inside the content.
- When anything is printed in greyscale, write the domain or category **name** on every coded panel, because the colour meaning is lost.

### BESTAE

Three ten-colour families: **H** (strong accents), **S** (deep shades for headers and dark text), **T** (light tints for panels). Base: `surface` #FFFFFF; `ink` #041E42 (= S8); `link` #326295 (denim, underlined); `link-on-t9` #201547.

| Set | Domain of learning | H (strong) | S (shade) | T (tint) | Text on H |
|---|---|---|---|---|---|
| 1 | *(brand default / unassigned)* | Jazzberry #AC145A | Mulberry #651C32 | Piggy Pink #EEDAEA | white |
| 2 | Critical Thinking | Tomato #FF585D | Espresso #551C25 | Soft Blush #F5DADF | ink |
| 3 | Creative Thinking, Problem Solving & Innovation | Royal Orange #F19C49 | Dark Leather #4F2C1D | Apricot #FFDFB4 | ink |
| 4 | Communication | Corn #F3EA5D | **Dark Gold #8A6400** | Buttermilk #F7F4A2 | ink |
| 5 | Self-Management & Organisation | Lime #C5E86C | Zucchini #1C4220 | **Lime Cream #E8F6C4** | ink |
| 6 | Responsibility & Stewardship | Seagreen #00B2A2 | Sherwood #024638 | Swans Down #D7EFE7 | ink |
| 7 | *(unassigned)* | **Bondi Blue #007F98** | Cyprus #003540 | Mystic #DCEBEC | white |
| 8 | Practical Skills & Technical Application | Denim #326295 | Night #041E42 | **Crushed Ice #D2DCE8** | white |
| 9 | Knowledge & Conceptual Understanding | Twilight #514689 | Dark Indigo #201547 | Periwinkle #DCD3E7 | white |
| 10 | Independent Learning & Collaboration | Valentine Pink #E56DB1 | Plum #621244 | **Powder Pink #F7D0E6** | ink |

*Bold = changed Sept 2026. The old values were Mustard #CFB500, Bondi #008EAA, Lime Cream #EFF4A4, Crushed Ice #D5EBEE and Powder Pink #F2DEE9.*

**Rules:**
- **Text on fills:** white only on H1, H7, H8, H9 and every S shade. Ink on every other H.
- **Dark Gold** with white is 5.4:1, so use it for headers and bold labels, not long body text.
- On a tint, text and icons use ink or the matching S colour, never the matching H.
- Links on Periwinkle use #201547.
- One domain set per resource. Knowledge-domain templates default to Twilight with Periwinkle.
- **Proportion:** surface or the domain tint ~60%, the domain's H fills and S headings ~30%, one highlight ~10%.
- Tomato, Valentine Pink and Seagreen print as the same grey, and Twilight and Denim as similar dark greys. Always label domains.
- Type: Lato only.

### MCCNS (school brand, do not alter)

| Colour | HEX | RGB | CMYK | PMS |
|---|---|---|---|---|
| MCC Navy (primary) | #001D3E | 0 29 62 | 100 60 15 75 | 282 C |
| MCC Light Blue (primary) | #909DB2 | 144 157 178 | 30 18 5 22 | 30% tint of 282 C |
| MCC Yellow (secondary) | #FFCB05 | 255 203 5 | 0 20 100 0 | 116 C |
| MCC Cerise (secondary) | #A6214D | 166 33 77 | 30 100 60 10 | 220 C |

*The 2020 guideline prints Light Blue's HEX as #D9DDE2. That is a misprint: its RGB, CMYK and drawn swatch all measure #909DB2.*

**Rules:**
- **Proportion:** white and Light Blue ~60%, Navy ~30%, one accent (Yellow **or** Cerise) ~10% per page.
- **Text:** Navy on white or Light Blue. White or Yellow on Navy (Yellow 11.1:1 for headings). White on Cerise. Navy on Yellow.
- **Never:**
  - Yellow text on white (1.5:1).
  - White text on Light Blue (2.7:1).
  - Cerise and Navy on each other (2.4:1). Separate them with white or yellow.
- **Logo:** standard on white or Light Blue; reversed on Navy; never recoloured, stretched or on busy backgrounds. Clear space = height of "M". Minimum widths: horizontal 57 mm, vertical and crest 20 mm.
- **Type:** Gotham (Medium/Book) for external material. Garamond Semibold for major headings, sparingly. Helvetica for internal Word and PowerPoint only.
- The SCS endorsed logo goes on all external marketing, bottom right or centre, at 50% of the school logo's size.
- Keep BESTAE Jazzberry out of MCCNS work, because it's nearly identical to Cerise.

### MBE Creative Studio

Mood: biophilic, with one pink "bloom". Cream #F3E9E2 (page), white #FFFFFF (cards), deep green #13342C (`ink`, `surface-900`, `brand-primary`), muted green #3F4F47, pink `accent-bloom` #FF3EB5 (the logo colour), peach `accent-warm` #FFA06A, `border` #DED1C6. Added Sept 2026: **`accent-bloom-deep` #E3008C** and **`border-strong` #A48061**.

**Rules:**
- **Proportion:** cream and white ~60%, deep green ~30%, peach under 10%, pink about 5% (one bloom per view).
- **Text:** deep green on cream (11.3:1) or white (13.5:1). Cream or white on deep green. Deep green on peach (6.7:1). Never muted green, white or cream on peach.
- **Pink:** never as a background or as text on light grounds. Large CTAs use pink with a deep-green bold label of 19 px or more (4.25:1). Small pink CTAs use #E3008C with white text (4.5:1). The logo always stays #FF3EB5.
- **Borders:** `border` for decorative dividers only (1.25:1). Inputs and focus rings use #A48061 (3.0:1 on cream). White cards on cream need a border or shadow.
- **Type:** Gill Sans Nova for body and UI. Santorini script (the logo face) for short, large accents only.

### Greyscale Workbooklet (print)

| Token | HEX | Text on it |
|---|---|---|
| Ink | #000000 | — |
| Pale | #CACBCA | Ink (12.9) |
| Accent 1 / 2 | #969896 / #878785 | Ink (7.2 / 5.8) |
| Accent 3 | #767776 | **No text** (black 4.67, white 4.50: both at the edge) |
| Accent 4 / 5 / 6 | #585958 / #494A49 / #383938 | White (7.0 / 8.9 / 11.6) |
| Muted | #5E5E5E | Captions on paper (6.5); use Ink on Pale |
| Link | **#5E5E5E** (was #898A89) | Always underlined |
| Link followed | #343433 | — |

**Rules:**
- **Coding set:** only Pale, Accent 2, Accent 4 and Accent 6 mark categories. Neighbouring accents blur together in print.
- **Proportion:** ~60% paper, ~30% light structure, ~10% dark emphasis.
- Lato only. A4 on a 12 × 12 mm grid (190 × 273 mm content area). Booklets: page count a multiple of 4, and keep 6 mm clear either side of the fold.

## 13. Quick reference

- **Colour** = perceived wavelength. Objects reflect some wavelengths and absorb the rest. There are three stages: light source, then object, then observer.
- **Additive (light):** RGB, all together make white. Screens.
- **Subtractive (ink, paint, dye):** CMY(K), all together make black. Print.
- **Hue / saturation / value. Tint** = + white, **shade** = + black, **tone** = + grey.
- **Harmonies:**
  - Monochromatic: cohesive.
  - Analogous: calm.
  - Complementary: vibrant, about 80/20.
  - Split-complementary.
  - Triadic: bold.
  - Tetradic / square: let one colour dominate.
  - One colour + neutrals: sharp and iconic.
- **60-30-10:** dominant / secondary / accent (the accent is for calls to action).
- **Contrast:** 4.5:1 for body text, 3:1 for large text and UI, 7:1 for AAA. The scale runs from 1:1 to 21:1.
- **A balanced palette** has at least one light and one dark colour, and stays out of the mid-tone danger zone.
- **HEX by hand:** value ÷ 16. The whole number is the first digit; the remainder × 16 is the second. Digits 0–9 then A–F. Example: `rgb(184,52,224)` = `#B834E0`.
- **Codes:** RGB/HEX for screens, CMYK for print, Pantone for exact matching (coated vs uncoated).
- **Metamerism:** colours that match under one light but not another, so use standard light boxes for textiles.
- **Never rely on colour alone.** Label it, because of colour blindness and greyscale printing.
