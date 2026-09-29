# MCCNS colour usage guide

*This guide shows how to use the colours in the **Marist Catholic College North Shore Visual Identity Guidelines (Nov 2020)**. It does not change the brand: every colour, logo, typeface and rule below comes from the official guidelines. It adds only **how to combine them** so text stays readable and the palette stays balanced. Contrast ratios were checked against WCAG 2.x with `shared/colour_tools.py`.*

## The palette (unchanged)

| Role | Colour | HEX | RGB | CMYK | PMS |
|---|---|---|---|---|---|
| Primary | **MCC Navy** | `#001D3E` | 0, 29, 62 | 100, 60, 15, 75 | 282 C |
| Primary | **MCC Light Blue** | `#909DB2` (see note) | 144, 157, 178 | 30, 18, 5, 22 | 30% tint of 282 C |
| Secondary | **MCC Yellow** | `#FFCB05` | 255, 203, 5 | 0, 20, 100, 0 | 116 C |
| Secondary | **MCC Cerise** | `#A6214D` | 166, 33, 77 | 30, 100, 60, 10 | 220 C |

Typefaces (unchanged):
- **Gotham** (Medium, Book) for external and professionally designed material.
- **Garamond Semibold** for major headings, used sparingly.
- **Helvetica** for Word, PowerPoint, letters and emails. Never use Helvetica for external material.

> **⚠ Check with the school: the Light Blue values disagree.** The guideline's RGB (144, 157, 178), CMYK and printed swatch are a mid grey-blue, `#909DB2`. Its printed HEX, `#D9DDE2`, is a much paler blue-grey. The PDF's own drawn swatch, and the box behind the horizontal logo, both measure RGB 143, 157, 179 (≈ `#909DB2`), so `#D9DDE2` is almost certainly a misprint. This guide uses `#909DB2`, and still gives both results where they differ. Ask the marketing office to confirm.

## How the palette works

- **Structure:** a **navy family** (Navy and Light Blue, both PMS 282) carries the brand, and **two warm accents** (Yellow and Cerise) add energy. Navy and Light Blue are cool; Yellow and Cerise are warm. This is the classic "one colour family + accents" approach, and the warm/cool contrast is why the crest reads so strongly.
- **Proportion (60-30-10):**

| Share | Colours | Used for |
|---|---|---|
| **~60%** | White + MCC Light Blue | Page and slide backgrounds, panels. The logo sits on white or Light Blue (per the guide) |
| **~30%** | MCC Navy | Headings, body text, header and footer bars, reversed-logo backgrounds |
| **~10%** | MCC Yellow *or* MCC Cerise | Highlights, key numbers, dividers (the spear), buttons, one feature per page |

- Use **one accent per page or slide** where possible. Yellow and Cerise together are strong, so save the pair for the crest and major event material.
- **Mary's Monogram** at reduced opacity and **the spear** as a divider are the guide's own graphic elements. Keep them in Navy, Light Blue or one accent. Don't recolour the logo or crest (per the guide).

## Text and background pairings

✓ = passes 4.5:1 (body text). **Large** = passes 3:1 only, so use it for headings 24 px / 18 pt and up, or bold 19 px / 14 pt and up. ✗ = don't use.

| Background ↓ / Text → | Navy | Black | White | Yellow | Cerise |
|---|---|---|---|---|---|
| **White** | ✓ 16.9 | ✓ 21.0 | — | ✗ 1.5 | ✓ 7.1 |
| **Light Blue** `#909DB2` | ✓ 6.1 | ✓ 7.7 | ✗ 2.7 | ✗ 1.8 | ✗ 2.6 |
| *Light Blue if `#D9DDE2`* | *✓ 12.4* | *✓ 15.4* | *✗ 1.4* | *✗* | *✓ 5.2* |
| **Navy** | — | ✗ 1.3 | ✓ 16.9 | ✓ 11.1 | ✗ 2.4 |
| **Yellow** | ✓ 11.1 | ✓ 13.8 | ✗ 1.5 | — | ✓ 4.7 |
| **Cerise** | ✗ 2.4 | ✗ 3.0 | ✓ 7.1 | ✓ 4.7 | — |

### Rules that fall out of this
1. **Default text is Navy on White or Light Blue.** Black is fine for Word documents and letters.
2. **On Navy, use White (body) or Yellow (headings, highlights).** Yellow on Navy is the strongest accent pairing (11:1).
3. **On Cerise, use White.** Yellow on Cerise passes (4.7:1), but only just, so keep it for bold headings.
4. **Never set Yellow as text on White or Light Blue**, and never put White text on Yellow.
5. **Light Blue is a background, never a text colour.** White text on Light Blue fails (2.7:1). If the paler printed HEX turns out to be correct, the same rule applies even more strongly.
6. **Never set Cerise text on Navy or Navy text on Cerise** (2.4:1). Where Navy and Cerise blocks meet, separate them with White or Yellow, as the crest does.
7. **Don't rely on colour alone.** Cerise and Navy are both dark and print as similar dark greys, so label anything colour-coded (e.g. tabs, charts, house or year groups).

## Logo backgrounds (from the guide, restated)
- **Standard logo** on White or MCC Light Blue.
- **Reversed logo** (white, yellow or full colour) on a dark background, preferably MCC Navy.
- **Never** on busy photos or patterns, and never recoloured.
- **Mono logo:** Cerise (PMS 220), Navy (PMS 282), black or white. Contrast check: Cerise mono on White is 7.1:1 and Navy mono on White is 16.9:1.

## Where each colour value goes

| Medium | Use | Why |
|---|---|---|
| Print (professional) | **CMYK** values above | They match the printer's four plates |
| Uniforms, merchandise, signage | **PMS** 282 C, 116 C, 220 C | Single-colour mediums need an exact ink match |
| Word, PowerPoint, Canva, screens | **RGB** / **HEX** | Screens are additive (RGB). Set them as theme colours so staff pick from the palette, not by eye |
| Web | **HEX** | Shorter to write, and it's the same colour as the RGB value |

Bright on-screen Yellow (`#FFCB05`) can't be reproduced exactly in CMYK. Always use the guide's CMYK and PMS values for print rather than converting from RGB.

## Using MCCNS with BESTAE teaching colours

In school teaching resources, keep the two systems in separate layers so neither brand is altered:
- **MCCNS is the frame:** logo, header and footer bars, the cover and document titles, all in the MCCNS palette and fonts (Helvetica in Word and PowerPoint).
- **BESTAE domain colours are the content coding:** domain panels, tabs and activity labels inside the page, following BESTAE's own text-on-fill rules.
- Keep **MCC Cerise and BESTAE h1 jazzberry apart.** They are almost identical (`#A6214D` vs `#AC145A`, 1.02:1), so jazzberry would read as the school colour. Don't use jazzberry in MCCNS-framed resources.
- On greyscale printouts, label every domain and category by name.

## Swatch files (`swatches/`)
- `mccns.ase` for Illustrator, InDesign and Photoshop.
- `mccns.css` for Figma and the web.
- `mccns-canva-paste-list.txt` for a Canva brand kit.
- `mccns.gpl` for GIMP, Inkscape and Krita.
- `mccns.json`.

These use the exact values from the guide. The `.ase`, `.css`, `.gpl` and `.json` files include both Light Blue values, clearly named. The Canva list uses the swatch value `#909DB2` until the school confirms which is correct.
