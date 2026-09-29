---
name: workbooklet-style-system
description: "The single shared style system for Britt's printed teaching resources: Greyscale workbooklets, Bestae-branded lessons and booklets, and InDesign / Adobe Express layouts. Defines one set of paragraph styles (Title, Subtitle, Heading 1–9, Normal and the workbooklet styles) with identical names, fonts, sizes and roles everywhere, plus two interchangeable colour layers (Greyscale and Bestae). Use whenever creating, restyling, auditing or converting a workbooklet, worksheet, lesson, assessment booklet or template in Word, or building a matching InDesign or Adobe Express layout, or when asked which heading or style to use for something."
---

# Workbooklet Style System

One type system, one page grid, two colour layers.

| Layer | What it controls | Same in Greyscale and Bestae? |
|---|---|---|
| **Type system** | Style names, typeface, weights, sizes, capitals, alignment, spacing, what each heading level is *for* | **Yes: identical** |
| **Page and grid** | A4, margins, 12 × 12 grid, table widths (see `word-tables`) | **Yes: identical** |
| **Colour layer** | Fills, borders, banners, accent colour | **No: Greyscale tokens or Bestae tokens, mapped role for role** |

A heading means the same thing and looks the same in every document. Only the
colour of fills and banners changes between Greyscale and Bestae. Heading text is
always black (or white on a dark fill), in both layers.

Adobe layouts use the **same style names and specifications**. Word content can
then be placed into InDesign and pick up the matching paragraph styles
automatically.

## The heading system at a glance

All headings are Lato, ALL CAPS and black. Sizes are in points.

| Style | Font | Size | Align | Used for |
|---|---|---:|---|---|
| **Title** | Lato Bold | 78 | Centre | Cover only: the booklet or phase name (IDENTIFY, INSPIRATION) |
| **Subtitle** | Lato Light | 33 | Centre | Cover only: task line, STUDENT NAME, CLASS |
| **Heading 1** | Lato Black | 52 | Centre | Subject name on the cover (TEXTILES); a major part divider |
| **Heading 2** | Lato Bold | 36 | Centre | A section of the booklet (CHOOSE YOUR DESIGN SITUATION, STATEMENT OF INTENT). In lesson documents, the lesson title |
| **Heading 3** | Lato Light | 20 | Centre | Introduction or sub-section within a section (WHAT YOU NEED TO KNOW) |
| **Heading 4** | Lato Black | 16 | Centre | An activity or task (1. INSPIRATION STATEMENT); the header row of a table |
| **Heading 5** | Lato Black | 12 | Centre | A step inside an activity (STEP 1: IDENTIFY THE END USE); table subheadings |
| **Heading 6** | Lato Light | 16 | Centre | A category label that should read lighter than Heading 4 (colour names, option names) |
| **Heading 7** | Lato Medium | 12 | Centre | A small callout or box heading on a light fill |
| **Heading 8** | Lato Heavy | 10 | **Left** | A prompt label above writing space (MY TARGET MARKET NEEDS:, TIPS:) |
| **Heading 9** | Lato Heavy | 10 | Centre | Labels inside tables (WHO / WHAT / WHEN, option names) |

Every other style (Normal, the question and answer styles, writing lines, table
styles, the white heading styles for dark fills) is in
`references/style-spec.md`.

## Rules

1. **Choose headings by role, not by look.** Pick the level from the "Used for"
   column. Never pick a level because its size happens to fit.
2. **Never format headings by hand.** No manual bold, size, font or colour. If a
   heading needs to be white on a dark fill, use `Heading 1 White` or
   `White Table Heading (12pt)`. Don't recolour a normal heading.
3. **Lato family only.** In Word, the theme fonts are set to Lato too, so nothing
   falls back to Aptos, Calibri, Montserrat, Open Sans or Gotham.
4. **Colour comes from the colour layer, never from heading text.** Fills and
   banners use role tokens (see `references/colour-layers.md`). The same document
   can then be moved between Greyscale and Bestae by swapping the colour layer.
5. **Tables follow `word-tables`:** header row in Heading 4, subheadings in
   Heading 5, labels in Heading 9.
6. **Pages follow the print system:** A4, 12 × 12 grid, booklet or flat margins,
   page count a multiple of 4 for booklets (see `greyscale-print-design-system`).
   **This skill replaces that skill's palette and heading table**, which were out
   of date (see `references/audit-and-migration.md`).

## Workflow

1. **New document:** start from the unified template. If none exists yet, restyle
   the document to `references/style-spec.md`.
2. **Choose the colour layer:** Greyscale for photocopied or mono-printed
   booklets; Bestae for colour-printed or on-screen lessons. For Bestae, choose
   the domain colour (see `references/colour-layers.md`).
3. **Apply styles by role** using the table above.
4. **Tables:** apply `word-tables`, with fills from the chosen colour layer.
5. **Check:**
   - no direct formatting on headings;
   - no fonts outside the Lato family;
   - no hex colours outside the chosen layer;
   - white text only on fills that pass the contrast rule.
6. **Adobe:** when laying out in InDesign or Adobe Express, follow
   `references/adobe.md` so the styles and colours match.

## Reference files

| File | Read it when |
|---|---|
| `references/style-spec.md` | Setting up or checking styles: full specifications for every paragraph, character and table style, with Word XML values |
| `references/colour-layers.md` | Choosing fills, banners or borders; switching between Greyscale and Bestae; checking text contrast |
| `references/adobe.md` | Building or checking an InDesign document or Adobe Express design that should match the Word booklets |
| `references/audit-and-migration.md` | Updating the existing templates and booklets: what differs today and how to fix it |
