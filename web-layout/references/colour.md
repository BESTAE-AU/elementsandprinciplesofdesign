# Web colour

The same colours as print (source of truth: `house-tokens.md`), light mode only.
Contrast ratios below are calculated with the WCAG 2 formula.

## Text

- **House standard:** 7:1 for all text. Absolute floor: 4.5:1 for large or secondary text.
  Meaningful graphics: 3:1.
- **Text colour:** #222222 by default. Use #333333 for captions and secondary text.
- **#555555 only on white** (7.46:1). It fails 7:1 on K 10 (5.97) and K 20 (4.64).
- **Never use colour alone to carry meaning.** Always name the domain or state in text.

## Greyscale fills

| Fill | Text | Ratio |
|---|---|---|
| K 0 #FFFFFF | #222222 / black | 15.91 / 21.0 |
| K 10 #E6E6E6 | #222222 / black | 12.75 / 16.83 |
| K 20 #CCCCCC | #222222 / black | 9.91 / 13.08 |
| K 30–60 | **no text** (graphics only) | — |
| K 70 #4D4D4D | white | 8.45 |
| K 80 #333333 | white | 12.63 |
| K 90 #1A1A1A | white | 17.40 |
| K 100 #000000 | white | 21.0 (small accents only) |

- **Most things have no background.** Panels run from K 90 (highest emphasis) to K 10 (lowest).
- **White text** is never Light, and never under 16 px.

## Learning domains

| Domain | T tint + black | S shade + text | H accent on white |
|---|---|---|---|
| Critical Thinking | 15.98 | white 13.30 | 3.09 |
| Creative Thinking | 16.47 | white 12.28 | 2.19 |
| Communication | 18.42 | **black** 10.26 | 1.25 |
| Self-Management | 18.15 | white 11.35 | 1.39 |
| Responsibility | 17.39 | white 10.85 | 2.66 |
| Practical Skills | 16.95 | white 16.54 | 6.33 |
| Knowledge | 14.51 | white 16.67 | 8.12 |
| Independent Learning | 16.40 | white 12.43 | 2.94 |

- **T tints:** black text. **S shades:** white text, except Mustard #CFB500, which takes black.
- **H accents are decoration only on white** (bars and rules beside text that names the domain).
  - Five of the eight fall below 3:1 on white, so they can't carry meaning alone.
  - Tomato's often-quoted 6.8:1 is against black, not white (3.09).
  - For a meaningful bar or icon, use the S shade.
- **Only Knowledge (8.12) clears 7:1 as text on white.** Practical Skills (6.33) is large text only.
