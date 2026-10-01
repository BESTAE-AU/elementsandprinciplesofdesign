# Colour: greyscale (K only)

The house palette for print is black ink only, in 10% steps. Every colour decision is checked
for contrast. Check any pair with:

```
python3 scripts/grid.py --contrast TEXT_K BG_K      # e.g. --contrast 80 20
```

## Contents
1. Swatches
2. How contrast is checked
3. Text colour
4. Backgrounds: the shading hierarchy
5. Panels
6. Tables
7. Reversed (white) text
8. Graphics and rules
9. Photocopying
10. Domain colour palette (colour documents)

---

## 1. Swatches

| Swatch | Values | Note |
|---|---|---|
| **K 0** | [Paper] | Page, and reversed (white) text |
| **K 10 … K 90** | C0 M0 Y0 K10 … K90, process | Name them exactly `K 10`, `K 20` … `K 90` |
| **K 100** | [Black] | Use the built-in [Black] so black text overprints cleanly |

Keep swatches in a **Greyscale** colour group. Never use [Registration] for anything visible.

## 2. How contrast is checked

- **Standard:** WCAG 2.2 contrast ratio.
- **Print allowance:** tints print darker than their percentage because ink spreads (dot gain). Every pair is checked twice, as specified and with ~15% mid-tone dot gain, and **the worse result counts**. On-screen figures are optimistic; paper decides.

| Requirement | Ratio |
|---|---|
| House standard for all text | **7:1** (AAA) |
| Absolute floor for secondary text | 4.5:1 |
| Large text (≥ 18 pt, or ≥ 14 pt bold) floor | 4.5:1 |
| Meaningful graphics, icons, borders | 3:1 |

On A4, large text covers Title, Heading 1–3, Subheading, Lead and Pull Quote. **Heading 4 and 5
are small text**: they're under 14 pt, even in Black.

## 3. Text colour

**Text colour doesn't vary by hierarchy.** Text is always the highest-contrast colour available on
whatever it sits on. Hierarchy comes from size, weight and position, never text shade.

| Text sits on | Text colour |
|---|---|
| Paper (K 0), K 10, K 20 | **K 100** |
| K 70, K 80, K 90, K 100 | **White ([Paper])** |

**One exception: secondary text** (Caption, Footnote, Running Footer) is **K 80** on paper and light
panels (12.6:1 on paper, 10.1:1 on K 10, 7.9:1 on K 20; all AAA). On dark panels it's white like everything else.

## 4. Backgrounds: the shading hierarchy

**Most things have no background.** The default is text straight on paper. A shaded background is
an optional emphasis, chosen per element. When used, shade shows hierarchy: **K 90 is the highest,
K 10 the lowest**, and K 100 is reserved for accents.

| Shade | Hierarchy | Text allowed on it |
|---|---|---|
| **K 100** | Accent: **small, very important items only** (tags, key icons, a single highlight bar). Never a large area. | White |
| **K 90** | Highest | White |
| **K 80** | ↓ | White |
| **K 70** | ↓ | White |
| **K 60 – K 30** | ↓ | **No text.** Graphics only: bars, dividers, icons, chart fills, image placeholders |
| **K 20** | ↓ | K 100 (secondary K 80) |
| **K 10** | Lowest. **Default light panel.** | K 100 (secondary K 80) |

No text is ever set on K 30–K 60. No text colour reaches 4.5:1 on K 50, and the others are marginal once printed.

## 5. Panels

A panel is a shaded text frame, applied with an object style from the **Panels** folder:

| Object style | Fill |
|---|---|
| Accent – K 100 | [Black], small items only |
| Panel – K 90 | K 90 |
| Panel – K 80 | K 80 |
| Panel – K 70 | K 70 |
| Panel – K 20 | K 20 |
| **Panel – K 10** | K 10 (default light panel) |

- **Size:** exact column span wide, and a **whole number of rows** tall (span heights from SKILL.md section 3). The frame sits on the grid like any object.
- **Padding:** Inset Spacing = **one column gutter left/right** and **one row gutter top/bottom** (e.g. 2 mm / 3 mm on A4P A). Whole numbers, tied to the grid.
- **Auto-Size off.** The panel's height stays on whole rows. If text overflows, add a row.
- Text inside keeps Cap Height first baseline and aligns to the panel's inner edge. **Text inside a panel is the one place that's offset from the column and row lines**, by exactly one gutter.
- Text inside uses the highest-contrast colour: **reversed styles on K 70–100**, normal styles on K 10–20.

## 6. Tables

| Part | Setting |
|---|---|
| **Header row** | Cell style *Table Header*: fill **K 90**, text in paragraph style *Table Header*: Bold, Body Condensed size and leading, ALL CAPS, tracking +25, **white** |
| **Body rows** | Cell style *Table Body*: no fill, bottom stroke **0.5 pt K 50**, text in *Table Body* (Body Condensed, K 100) |
| **Banding** (optional) | Cell style *Table Body Banded*: fill **K 10** on alternate rows |
| **Cell insets** | Column gutter left/right, row gutter top/bottom (same as panels) |
| **Columns** | Exact column-span widths |
| **Row height** | At Least (grows with text) |
| **Table style** | *Table*: header and body cell styles, alternating fills every other row |

The table frame uses a normal position object style, with its top on a row line.

## 7. Reversed (white) text

Styles allowed on K 70–100 get a **Reversed** variant in a *Reversed* style group, Based On the
original, colour [Paper]: e.g. `Title – Reversed`, `Heading 1 – Reversed`, `Body – Reversed`,
`Bullet – Reversed`, `Label – Reversed`.

- **Minimum size:** 12 pt Regular, or **10 pt Bold/Black** (so a 10 pt Label can sit on a K 100 accent tag).
- **Never reversed:** Light and Thin weights (Subheading, Lead, Caption, Pull Quote) and anything under the minimum size. Fine strokes fill in when printed white-on-dark.

## 8. Graphics and rules

| Use | Shade |
|---|---|
| Rules, borders or icons that **carry meaning** | **K 50 or darker** (≥ 3:1 on paper) |
| Decorative rules (no meaning) | Any |
| Answer lines | K 100, 0.5 pt |
| Table row rules | K 50, 0.5 pt |

**Never use shade alone to carry meaning** (e.g. "the dark boxes are the hard questions"). Always
add a label, icon or position cue as well.

## 9. Photocopying

- **K 10 can disappear on some photocopiers.** For resources that will be photocopied, use **K 20** for light panels and banding instead.
- **Mid-greys photocopy blotchily.** Dark panels photocopy best at K 80–90.
- Reversed text on dark panels holds up better in **Bold/Black** than Regular.

## 10. Domain colour palette (colour documents)

For colour print and slides, the house also uses the **learning-domain colours** shared with the
Canvas skill. The full palette and the text colour for each swatch are in `references/house-tokens.md`
section 6. Colour is chosen by the learning domain of the content, not for decoration.

**Adding them to a document:** `python3 scripts/build_indd.py A4P A --out … --domain <slug>` (or
`--domain all`) adds each domain as its own colour group of RGB swatches named as in the palette,
e.g. `8H DENIM`, `8S NIGHT`, `8T CRUSHED ICE`.

**Roles in InDesign:**

| Role | Colour | Used for |
|---|---|---|
| Tint panel | **T** | Replaces K 10/K 20 light panels. Text K 100. |
| Accent | **H** | Divider bars, left edge bars, pill labels, small highlights. Replaces K 100 accents. |
| Dark panel | **S** | Replaces K 70–90 dark panels and table headers. Text white. **Dark Gold (Communication S) is 5.4:1: headers and bold labels only.** |

- Greyscale rules still apply: most things have no background, text is the highest-contrast colour, and shade or colour never carries meaning alone.
- **Tomato and Denim** (H), and **Dark Gold** (Communication S) with white text, reach only 6.8:1, 6.3:1 and 5.4:1, so use them for large text (≥ 18 pt, or ≥ 14 pt bold) and graphics, never body text.
- Check any pair: `python3 scripts/grid.py --contrast-hex "#FFFFFF" "#326295"`. List every swatch: `python3 scripts/grid.py --domains`.
- **Colour printing:** these are screen colours. InDesign converts them through the document's CMYK profile on export. Check a printed proof. If the school has official CMYK or Pantone values, they override the conversion.
- Don't mix domain colours into a greyscale (K-only) document. Choose one palette per document.
