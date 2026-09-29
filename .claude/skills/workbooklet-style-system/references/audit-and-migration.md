# Audit and Migration

This audit covers the files in Google Drive as of September 2026 and lists the
changes needed to bring them onto the shared system.

Files checked:
- Greyscale booklets: Identify Booklet, Develop Booklet, Design Inspiration
  Booklet;
- Bestae Word Style Kit3;
- MULTIMEDIA WORKBOOK;
- Bestae Template.pptx;
- the InDesign booklet (Untitled-2.idml).

## 1. Heading styles: Greyscale vs Bestae today

| Style | Greyscale booklets | Bestae Style Kit | Shared system |
|---|---|---|---|
| Title | Lato Bold 78, centre | Lato Bold 36, left | **Lato Bold 78, centre** |
| Subtitle | Lato Light 33, centre | Lato Light 16, left | **Lato Light 33, centre** |
| Heading 1 | Lato Black 52, centre | Lato Black 26, left | **Lato Black 52, centre** |
| Heading 2 | Lato Bold 36 (Develop: Lato Heavy), centre | Lato Bold 22, left | **Lato Bold 36, centre** |
| Heading 3 | Lato Light 20, centre | Lato Light 20, left | **Lato Light 20, centre** |
| Heading 4 | Lato Black 16, centre | Lato Bold 18, left | **Lato Black 16, centre** |
| Heading 5 | Lato Black 12, centre | Lato **Thin** 18, left | **Lato Black 12, centre** |
| Heading 6 | Lato Light 16, centre | Lato Bold 16, left | **Lato Light 16, centre** |
| Heading 7 | Lato Medium 12 (Identify: white, no font) | Lato Black 12, left | **Lato Medium 12, centre** |
| Heading 8 | Varies: Heavy 12 left / Heavy 10 left / Bold 10 centre | Lato Light 12, left | **Lato Heavy 10, left** |
| Heading 9 | Lato Heavy 10, centre | Lato Heavy 10, left | **Lato Heavy 10, centre** |

The shared system keeps the Greyscale booklet values. They are what the booklets
and the InDesign file already use. The Bestae Style Kit takes these sizes and
centring.

**Effect on Bestae lesson documents:** lesson headings get much bigger if they
stay on Heading 1 (26 → 52 pt). Move them down one level, following the lesson
mapping in `style-spec.md`: lesson heading → Heading 2 (36 pt).

## 2. Other problems found

| Problem | Where | Fix |
|---|---|---|
| **Theme fonts are Aptos.** Anything set to "+Body" or "+Headings" falls back to Aptos | All three Greyscale booklets | Design → Fonts → Customise: Lato / Lato. Save as "Workbooklet Lato" |
| **Theme fonts are Montserrat ExtraBold / Open Sans** | Bestae Style Kit, MULTIMEDIA WORKBOOK | As above |
| **Gotham Book** in Normal, Title, Heading 2, Heading 6 | MULTIMEDIA WORKBOOK | Restyle the document to the shared styles |
| **Bestae theme puts brand colours in `dk1`/`lt1`**, so "Text 1" is Jazzberry and "Background 1" is Tomato | Bestae Style Kit | Replace with the Bestae domain theme sets in `colour-layers.md` |
| **Headings made white by hand** (Heading 1 "TASK", Heading 7 in dark cells) | Identify, Design Inspiration | Apply `Heading 1 White` / `White Table Heading (12pt)` |
| **Direct formatting on headings** (manual fonts, sizes and colours, e.g. Arial on lesson headings, 165 manual colours in Design Inspiration) | Bestae Style Kit, Identify, Design Inspiration | Select all → Ctrl+Space clears manual character formatting. Then re-apply the styles |
| **Off-palette fills**: MARKING CRITERIA header `#AAAAAA`, Possible Answers `#E4E5E3`, Example Response `#525454` | Greyscale template styles | Pale, Light and Dark theme tokens respectively |
| **The print skill's palette is out of date.** It lists Accent 1–6 as `#969896`…`#383938`; the real Word theme is `#CACBCA`…`#4C4D4C` with Background 2 `#E3E4E3` | `greyscale-print-design-system` skill | Use `colour-layers.md` from this skill. The print skill's page, grid and booklet rules still apply |
| **Duplicate style names for the same job**: Question Format / 2. Question Format, and so on | Bestae vs Greyscale | Rename per `style-spec.md` |
| **Writing Lines spacing differs**: Bestae 2.0 vs Greyscale 1.5 | Bestae Style Kit | 1.5 (Greyscale) |
| **Normal spacing differs**: 0 after in the booklets, 3.5 mm in the template | Greyscale booklets | Normal = 3.5 mm after. Use **Table Text** (0 after) inside tables |
| **Margins drift**: 12.7 mm (Bestae); 12/10 mm, 12/8 mm, 12/12/8/12 mm (booklets) | Various | Booklet 12/12/12/8 mm or flat 12/12/10/10 mm only |
| **Bestae Template.pptx** holds the palette as CSS text, not as theme colours | Bestae Template.pptx | Rebuild its theme from the Bestae domain sets, and set its fonts to Lato |

## 3. Migration order

Work through it in this order, so each step builds on a fixed base.

1. **Build two master templates** from the Greyscale booklet template:
   - `Workbooklet – Greyscale.dotx`: theme fonts Lato, colour set Greyscale for
     Printing, styles per `style-spec.md`;
   - `Workbooklet – Bestae.dotx`: an identical copy, with the colour set
     `Bestae – 1 Jazzberry` and the other nine domain colour sets saved in the
     template;
   - keep the Bestae-only content styles (MAGIS, Marist Values and so on) in the
     Bestae template only.
2. **Fix the InDesign template** using the table in `adobe.md`, and add the
   swatches.
3. **Set up the Adobe Express Brand Kit** (see `adobe.md`).
4. **Existing booklets:** attach the new template (Developer → Document Template
   → tick "Automatically update document styles"). Then fix the manual white
   headings and the direct formatting. The fills already use theme colours, so
   they will pick up a Bestae colour set without further work.
5. **Update the `greyscale-print-design-system` skill** so its heading table and
   palette point here, avoiding two conflicting sources.

## 4. Quick conformance check for any document

- [ ] Theme fonts are Lato / Lato.
- [ ] Only the shared style names are used, plus the Bestae-only content styles
      in Bestae documents.
- [ ] No manual font, size or colour on any heading.
- [ ] Every fill is a theme colour (`w:themeFill`), from the chosen layer's
      slots.
- [ ] White text only on Dark or Darkest, or on Main colours 1, 8 and 9.
- [ ] Captions use the Caption style in Muted.
- [ ] Margins are booklet or flat values only.
- [ ] Tables pass the `word-tables` checks.
