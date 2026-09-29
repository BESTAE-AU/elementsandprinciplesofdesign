---
name: typography-critique-audit
description: Audits and critiques the typography in a poster, flyer, slide, website, app screen, logo, magazine spread, workbooklet or student folio page. It checks font choice against the audience and brief, hierarchy (squint test), number of fonts, faux bold, size, leading, tracking and kerning, line length, alignment, widows and orphans, text/background contrast (WCAG), and consistency against a type system. It then gives prioritised fixes and kind, specific marking feedback. Use when someone asks "what's wrong with the text on this?", "is this readable?", "critique my poster's typography", "give feedback on this student's layout", wants a typography analysis of a brand or artwork for Visual Design or Graphics, or needs model annotations for a folio, even if they only share an image and say "thoughts?". For colour-only contrast matrices use colour-contrast-audit.
---

# Typography critique and audit

Source criteria: the "Typography" playlist (CAN hierarchy, spacing and squint test; DSP type variables and contrast; ENV font personality; CPS heading vs body roles). Use `scripts/type_tools.py` for contrast ratios, line length and leading checks rather than guessing.

## Gather

1. What it is, who it's for, and what it must communicate (ask, or infer and state the assumption).
2. The output medium and viewing distance.
3. If only an image is available, estimate sizes and colours by eye and say they are estimates. Ask for the source file or hex codes when a verdict is borderline. In Canva use `read-design` or `export-design`; for PDFs extract the fonts list if possible.

## Check, in this order (big problems first)

| # | Check | Pass looks like | Common fix |
|---|---|---|---|
| 1 | **Message and tone** | Fonts match the audience and brief (the bank test, ENV). Display or script fonts are only used for short bursts | Swap to a category whose personality fits (see `typeface-selection-rationale`) |
| 2 | **Hierarchy** | Squint test: the most important item wins, then a clear second and third level (CAN) | Increase size or weight contrast between levels. Reduce competing bold items. Give headings more space above |
| 3 | **Number of fonts** | 1–2 families, 3 at most, each with a clear role | Merge roles into one family using weights |
| 4 | **Real weights** | No faux bold or italic; no stretched or squashed type | Choose the family's real Bold. Never distort letterforms to fit |
| 5 | **Readability of body text** | Suitable size for the medium; leading 120–150%; 45–75 characters per line; left-aligned (CAN) | Run `leading` and `measure`, then adjust the size or column width |
| 6 | **Spacing** | Even tracking; big headings slightly tightened; all caps tracked out; no awkward pairs (AV, To, WA) in headings or logos | Tighten or loosen tracking; kern the pair by hand (DSP) |
| 7 | **Contrast** | Body text ≥ 4.5:1, large text ≥ 3:1 (WCAG AA); no text over busy image areas | Run `contrast`; darken or lighten one colour, or add an overlay or panel behind text |
| 8 | **Alignment and grid** | Text shares clear edges; consistent margins; no random centring of long text | Snap to a grid; left-align body text |
| 9 | **Details** | No widows or orphans; consistent styles for the same level; correct quotes, dashes and apostrophes; no double spaces | Re-rag, rewrite or adjust tracking slightly; apply styles consistently |

Don't mark something as wrong just because it breaks a rule of thumb. Posters, logos and expressive work bend rules on purpose. Ask whether the choice *serves the message*, and say so when a rule break works.

## Output

1. **Overall verdict** in one or two sentences: what works and the single biggest issue.
2. **Findings table:** check, what I see (with evidence: sizes, ratios, character counts), impact on the reader, fix.
3. **Priority fixes** (top 3, in order), each with exact values ("increase the body from 9 pt to 11 pt with 15 pt leading").
4. **For student marking:** 2–3 comments using the frame *what works → what to change → why it matters to the reader*. Use kind, specific wording and the correct terms so the student learns the vocabulary. Link to the relevant outcome if the teacher gives it; for rubric-level feedback, hand off to `marking-rubric-builder`.
5. **For analysis or folio annotation** (Visual Design, Graphics): name the typeface category and features, then explain their effect and how they support the design's purpose, rather than stopping at "the font is nice".

## Hand-offs

- Rebuilding the hierarchy with exact styles: `type-system-builder`.
- Choosing replacement fonts: `typeface-selection-rationale`.
- Full palette contrast matrices: `colour-contrast-audit`.
- Explaining a term to the student: `typography-fundamentals-explainer`.
