---
name: colour-codes-and-conversion
description: Converts and explains colour codes (RGB 0–255, HEX #RRGGBB, HSB/HSL, CMYK percentages, Pantone), including the by-hand base-16 working for RGB to hex and hex to RGB, and which code to use for screen, web/CSS, print or packaging. Use when someone gives a colour code and wants it in another format, asks how hex codes work, wants a hex-maths worksheet or answer key, or asks whether to use RGB, CMYK or Pantone for a job. For whether two colours are readable together use colour-contrast-audit.
---

# Colour codes and conversion

## Tool

`scripts/colour_tools.py` uses only the Python standard library. Run it for exact numbers rather than doing the arithmetic in your head:

```bash
python3 scripts/colour_tools.py convert "rgb(184,52,224)"   # or "#B834E0"
```

It prints HEX, RGB, HSB, HSL, approximate CMYK, the colour's position on the artist's wheel, and the **step-by-step hex working**. Add `--json` if you need to process the output further.

If you can't run code, use the method in `references/codes.md`.

## How to respond

1. **Give the answer first**, e.g. `#B834E0` = `rgb(184, 52, 224)`.
2. **Show the working** when the person is learning, or asks "how". Use the teaching method from the source video (llA): divide by 16, the whole number is the first digit, and the remainder × 16 is the second digit.
3. **Say which code suits the job:**
   - Screen, UI, video, social: **RGB** or **HEX** (HEX is shorter to write, which suits CSS).
   - Adjusting a colour logically in Illustrator, Photoshop or Figma: **HSB** sliders (hue, saturation, brightness).
   - Commercial print: **CMYK**. The script's CMYK is a naive conversion, so **always confirm with the document's colour profile or the printer**, because real values depend on the paper and profile.
   - Packaging, merchandise, anything printed at multiple factories: **Pantone**, and specify coated or uncoated stock (the same ink looks different on each).
4. **Flag out-of-gamut risk.** Very saturated screen colours (bright RGB greens, blues and oranges) often can't be printed in CMYK and will look duller. Recommend a soft proof, or choosing a Pantone.

## Worksheets and answer keys

For a practice set, pick varied RGB values (include one with a 0 remainder and one containing A–F digits), run `convert` on each, and give students a blank table (RGB | ÷16 | first digit | remainder×16 | second digit | hex). Put the answer key on a separate page. The llA extension challenge is: convert a random colour by hand, then check it in Illustrator or Photoshop's colour picker.

## Use it in connected tools (Adobe, Canva and others)

To load colours into design software, export a swatch file:

```bash
python3 scripts/colour_tools.py export "Brand Blue=#1F3D5A" "Accent=#F2A541" --format ase --out brand.ase
```

`.ase` works in Illustrator, Photoshop and InDesign. `--format css` suits Figma or the web, `canva` gives a paste list for a Canva brand kit, and `gpl` suits GIMP, Inkscape and Krita. With a Canva or Adobe connector, apply the codes directly. See `references/applying-in-tools.md`.
