---
name: type-system-builder
description: Builds a typographic system, meaning the hierarchy of text styles (display, H1–H3, body, caption/label, button) with exact sizes, weights, leading, tracking, line length and spacing, from a type scale (major third, perfect fourth, golden ratio 1.618 and so on). It outputs a style spec ready for InDesign or Word paragraph styles, Canva/Adobe Express text styles or CSS (px/rem). It also handles unit conversion (pt, px, rem, pica, mm), leading and line-length calculations, and grids (12-column web; 2, 3 or 6-column print). Use when someone asks how big headings and body text should be, what leading or letter-spacing to use, wants a type scale, style sheet, paragraph styles, a CSS typography setup, "make my text hierarchy consistent", or is setting up a poster, booklet, slide deck, website or brand guideline's type page. For choosing which fonts, use typeface-selection-rationale.
---

# Type system builder

Source method: DesignSpo's typographic system (headings, paragraphs, buttons, labels; the smaller the text, the lighter and more open it gets) and Canva's hierarchy and spacing rules (leading 120–150%, 45–75 characters per line, left-aligned body). Use `scripts/type_tools.py` for every number, rather than mental maths, so specs are consistent.

```bash
python3 scripts/type_tools.py scale --base 16 --ratio major-third --steps 6 --small   # screen, px
python3 scripts/type_tools.py scale --base 10 --unit pt --ratio perfect-fourth --steps 5 --small  # print
python3 scripts/type_tools.py convert 12pt          # also 16px, 1.5rem, 3pica, 4.2mm
python3 scripts/type_tools.py leading 11pt
python3 scripts/type_tools.py measure --width 85 --size 10          # print column: mm + pt
python3 scripts/type_tools.py measure --width 680 --size 18 --screen # web column: px
python3 scripts/type_tools.py contrast "#555555" "#FFFFFF"
```

## Process

1. **Context.** Medium (print page size or screen), viewing distance (a handout at 40 cm vs a poster at 3 m vs a slide at the back of a room), fonts (from `typeface-selection-rationale` if not yet chosen), and how many text levels the content really needs. Two or three heading levels are usually enough (DSP).
2. **Set the body size first**, because everything else scales from it:
   - Print handouts and booklets: 10–12 pt. Captions 8–9 pt minimum.
   - Screen: 16 px (1 rem) minimum; 17–20 px for reading-heavy pages.
   - Slides (1920 × 1080): 24–32 px body minimum; headings 40–72 px.
   - Posters: body readable from 1–2 m is roughly 24–36 pt; titles 72 pt+.
   - Adjust for the font's x-height: large x-height faces can go a touch smaller.
3. **Choose a scale ratio.** A small ratio (1.125–1.25) suits dense documents and UIs. A medium ratio (1.333–1.5) suits editorial and presentation work. The golden ratio (1.618) gives dramatic posters and brand decks. Run `scale`, then round to whole or half sizes. The script's step names are only placeholders, so map the steps to the levels you actually need (e.g. with three headings, step 4 might become H1).
4. **Assign styles.** For each level set font, weight, size, leading, tracking, case, colour and space above and below:
   - Bigger text: heavier weight, **tighter** leading (100–120%) and slightly **negative** tracking.
   - Smaller text: regular weight, **looser** leading (140–150%) and neutral or slightly positive tracking.
   - **Buttons:** bolder than body, with slightly wider tracking to avoid looking squashed (DSP).
   - **Labels and captions:** smaller, and may use lower contrast *if it still passes 4.5:1*.
   - **All caps:** always add tracking (+50 to +100 in InDesign, 0.05–0.1 em).
   - Use real weights from the family, not faux bold (CAN).
5. **Line length and grid.** Aim for 45–75 characters per line (about 66). Use `measure` to pick column widths. Web: 12-column grid with body text across about 6–8 columns, capped with `max-width: 66ch`. Print: 2 columns on A4, 3 for magazine layouts, 6 for newspapers. Posters can use golden-ratio divisions (DSP).
6. **Spacing rhythm.** Space above a heading should be larger than below it, so the heading "belongs" to its text. A simple system: space-before = 1–2 × body leading; space-after = 0.5 × body leading. In InDesign, align to a baseline grid equal to the body leading.
7. **Alignment.** Left-align body text (CAN). Centre only short headings, invitations and poster titles. Avoid justified text in narrow columns (rivers).
8. **Check.** Squint test (does the right thing win?). Contrast check for each text colour (`contrast`). Print a test page at 100% or view on a real phone.

## Output: the style spec

Always give a table like this, then the tool-specific version the user needs.

| Style | Font / weight | Size | Leading | Tracking | Case | Space before / after | Colour |
|---|---|---|---|---|---|---|---|
| H1 | DM Serif Display Regular | 39 px (2.441 rem) | 47 px (120%) | −0.01 em | Sentence | 0 / 16 px | #1A1A1A |
| Body | DM Sans Regular | 16 px (1 rem) | 23 px (145%) | 0 | Sentence | 0 / 12 px | #333333 (12.6:1) |

Tool versions:
- **InDesign or Word:** list as paragraph styles, Based On "Body". Tracking in InDesign units (1/1000 em). Leading in pt. For the house workbooklet styles defer to `workbooklet-style-system` and `indesign-parameters`, and only add what they don't cover.
- **CSS:** custom properties plus element rules, with sizes in rem, unitless `line-height`, `letter-spacing` in em, and `max-width` in ch. Offer `clamp()` for fluid headings.
- **Canva or Adobe Express:** a short list of text styles to save in the brand kit (Heading, Subheading, Body), noting that Canva's line spacing is a multiplier (1.4) and letter spacing is roughly in thousandths of an em (check visually).

## Hand-offs

- Which fonts: `typeface-selection-rationale`. Definitions: `typography-fundamentals-explainer`.
- Checking an existing design: `typography-critique-audit`.
- Colour contrast in depth: `colour-contrast-audit`.
- Word tables: `word-tables`. Print booklets: `greyscale-print-design-system`.
