---
name: colour-contrast-audit
description: Audits colour pairs or a whole palette for readability and accessibility. It calculates WCAG contrast ratios for every pair, places each colour on the 3x3 luminosity × saturation grid, flags missing light or dark colours and "danger zone" mid-tones, and suggests the smallest fix that makes a failing pair pass. Use when someone asks "is this readable?", "does this pass WCAG / accessibility?", "check my colours", wants a contrast matrix or a list of compliant text/background pairs, or is marking or reviewing a student's poster, slide, website or UI for legibility.
---

# Colour contrast audit

Source method: The Colour Palette Studio, *How to Balance a Colour Palette* (oDn), and The Futur's background × text × link × button pairing grid (eXc).

## Run it

```bash
python3 scripts/colour_tools.py audit "#F5EBDD" "#E8967A" "#5A3325" "#9A7B8F"
python3 scripts/colour_tools.py contrast "#1D4ED8" "#FFFFFF"
```

`audit` prints each colour's 3×3 cell, every pair sorted by contrast ratio with its WCAG level, the number of pairs that pass, and a list of issues. Add `--json` if you need to post-process the output.

If you're given an image instead of hex codes, identify the main colours by eye, say that the values are estimates, and audit those. Ask for the real hex codes if the result is borderline.

## Thresholds (WCAG 2.x)

| Ratio | Meaning |
|---|---|
| ≥ 7:1 | AAA: best for long reading and low-vision users |
| ≥ 4.5:1 | **AA for body text**, the standard minimum from the source video |
| ≥ 3:1 | Large text (about 24 px regular or 19 px bold and up) and UI parts such as icons and input borders |
| < 3:1 | Fail. Decorative use only |

The scale runs from 1:1 (same colour) to 21:1 (black and white). The ratio is identical whichever colour is the background.

## Reading the result

A **balanced palette** has at least two colours, **at least one light and one dark** colour, and at least one pair at 4.5:1 or higher. If the only light and dark colours sit in the **danger zone** (medium luminosity with midtone saturation), expect no accessible pairs.

## Fixing failures: the smallest change first

1. Keep the hue and move **one** colour's lightness away from the other: lighter toward the light-muted corner, darker toward the dark corner. Re-run `contrast` after each nudge. Report the new hex and ratio. (oDn: moving a pink toward light-muted took a pair from 3.14 to 5.32.)
2. If the colour is a brand colour that can't move, change its **partner** instead (e.g. use a near-black warm brown instead of the mid-tone text).
3. If a pair still fails, restrict it: large headings only, decorative only, or never together.
4. Don't let colour carry meaning alone. Add icons, labels or underlines, because red vs green is invisible to common colour-vision deficiencies.

## Output

1. A table of pairs: background, foreground, ratio, and the result for body text, large text and not recommended.
2. A **pairing guide per background** (eXc): for each background, which colours to use for body text, links and buttons.
3. Issues and proposed fixes with the new hex values and their re-tested ratios.
4. For marking feedback: 2–3 specific, kind, actionable comments (what works, what fails and why, and what to change).

## Use it in connected tools (Adobe, Canva and others)

Auditing in place:
- **Canva:** `read-design` or `export-design`, then audit, then `comment-on-design` with each failing pair (hex, ratio, suggested replacement hex).
- **Adobe Express:** preview or export, then audit.
- **WordPress:** read the theme presets, then audit the pairs the theme actually uses.

Always audit the colours *as rendered*, not just the intended ones. Recipe details are in `references/applying-in-tools.md`.
