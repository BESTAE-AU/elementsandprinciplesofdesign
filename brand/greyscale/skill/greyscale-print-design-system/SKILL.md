---
name: greyscale-print-design-system
description: Apply the Greyscale Workbooklet print design system — 12×12 modular grid, Lato type scale, greyscale-only palette, metric page setup and saddle-stitch booklet rules — to a Word document. All measurements in millimetres.
---

Design system captured from **Greyscale Workbooklet.dotm** (en-AU). Print-first, greyscale only, **all measurements in millimetres**.

Type sizes stay in points — that's the unit for type. Everything spatial (page, margins, grid, indents, spacing) is millimetres.

## When to use
- Applying the greyscale workbooklet house style to a document
- New worksheets, workbooklets, exam papers or handouts joining the existing printed set
- Laying out anything on the 12-column grid
- Checking a document for conformance before it goes to print

Do NOT use for on-screen/colour deliverables — the palette is deliberately desaturated.

---

## 1. Page setup

Page is **A4 portrait, 210 × 297 mm**. Header / footer distance **12.5 mm**. Gutter **0**.

Margins depend on how the document is bound. Establish which it is before setting anything.

**Saddle-stapled booklet** (folded and stapled through the centre spine):

| Margin | Millimetres |
|---|---|
| Top | 12 |
| Bottom | 12 |
| Inside (spine) | 12 |
| Outside | 8 |

**Flat printout** (loose sheet, not bound):

| Margin | Millimetres |
|---|---|
| Top | 12 |
| Bottom | 12 |
| Left | 10 |
| Right | 10 |

Both variants total 20 mm horizontally and 24 mm vertically, so the **content area is 190 × 273 mm either way** — the grid below is identical for both.

Office.js takes points, so convert on the way in — **mm × 2.8346 = points**. For a booklet the inside/outside values go to `leftMargin` / `rightMargin`; Word maps them to Inside/Outside once Book fold is on.

```javascript
const mm = v => v * 2.8346;
const booklet = true;                       // false for a flat printout
const secs = context.document.sections;
secs.load("items");
await context.sync();
const ps = secs.items[0].pageSetup;
ps.pageWidth  = mm(210); ps.pageHeight = mm(297);
ps.topMargin  = mm(12);  ps.bottomMargin = mm(12);
ps.leftMargin = mm(booklet ? 12 : 10);      // inside when Book fold is on
ps.rightMargin = mm(booklet ? 8  : 10);     // outside
ps.headerDistance = mm(12.5); ps.footerDistance = mm(12.5);
await context.sync();
```
**Done when:** read-back divided by 2.8346 returns the mm values above.

## 2. Modular grid — 12 × 12

Content area **190 × 273 mm**. Both axes divide exactly; there is no rounding to absorb.

- **Columns:** 12 modules of **14 mm**, gutter **2 mm** → 12 × 14 + 11 × 2 = 190
- **Rows:** 12 modules of **20 mm**, gutter **3 mm** → 12 × 20 + 11 × 3 = 273
- Vertical rhythm unit is therefore **23 mm** (module + gutter)

**Column spans** — set a table column to these widths:

| Modules | Width (mm) | Divides page into |
|---|---|---|
| 1 | 14 | 12 up |
| 2 | 30 | 6 up |
| 3 | 46 | 4 up |
| 4 | 62 | 3 up |
| 6 | 94 | 2 up |
| 12 | 190 | full width |

**Row spans:**

| Modules | Height (mm) |
|---|---|
| 1 | 20 |
| 2 | 43 |
| 3 | 66 |
| 4 | 89 |
| 6 | 135 |
| 12 | 273 (full page) |

Formula for any span: `n × module + (n − 1) × gutter`.

### Building a grid table

Word tables have no gutter concept. Two ways to fake it:

**Spacer columns — exact, use this for anything aligning to the page edge.** Real 2 mm gutter columns between content columns, borders off. A 4-up block is 7 columns: 46 / 2 / 46 / 2 / 46 / 2 / 46.

```javascript
// n = number of content columns; span = content width in mm; gutter = 2
function gridWidths(n, span, gutter = 2) {
  const w = [];
  for (let i = 0; i < n; i++) { w.push(span); if (i < n - 1) w.push(gutter); }
  return w;                                  // e.g. [46,2,46,2,46,2,46]
}

const mm = v => v * 2.8346;
const widths = gridWidths(4, 46);
const carrier = body.insertParagraph("", "End");
carrier.styleBuiltIn = "Normal";
carrier.load("isListItem");
await context.sync();
if (carrier.isListItem) { carrier.detachFromList(); await context.sync(); }

const t = carrier.insertTable(1, widths.length, "After", [widths.map(() => "")]);
t.horizontalAlignment = "Left";
t.getBorder("All").type = "None";
widths.forEach((w, c) => {
  const cell = t.getCell(0, c);
  cell.columnWidth = mm(w);
  cell.shadingColor = c % 2 === 0 ? "#CACBCA" : "#FFFFFF";  // spacers stay white
});
t.rows.load("items");
await context.sync();
t.rows.items[0].preferredHeight = mm(66);    // 3 row modules
await context.sync();
```
**Done when:** `getCell(0,0).columnWidth / 2.8346` returns the span in mm (±0.02 rounding is normal) and the spacer cell returns 2.

**Cell padding as gutter — quick, internal use only.** Uniform 1 mm left/right cell padding on a 12-column table puts 2 mm between cells, but also insets both outer edges by 1 mm, so the block no longer sits flush to the margin. Never use it for anything meant to align to the page edge.

### Grid constraints in Word

- **AutoFit must be off.** Word silently re-proportions columns as soon as content is typed. Always write explicit `cell.columnWidth` values, and re-read them after adding content.
- **Row heights are a minimum, not a lock.** `preferredHeight` sets a floor; a row grows if its content is taller. The column grid holds rigidly; the row grid is a rhythm you design to, not something Word enforces.
- **Hold vertical rhythm through paragraph spacing**, not row heights — make space-before + line spacing + space-after add up to the 23 mm module, rather than trying to pin rows.
- **Floating objects:** Layout → Align → Grid Settings, snap 2 mm horizontal / 1 mm vertical, lands objects on module boundaries by hand.
- Set `t.horizontalAlignment = "Left"` and leave table indent at 0, or the whole block drifts off the left margin.

## 3. Saddle-stitch booklet rules

A4 pages printed **two-up on A3 landscape**, folded once through the centre and stapled on the fold.

**Page count must be a multiple of 4.** Count before print; pad with a blank or an extra writing-lines page.

**Book fold is set in the Word UI, not programmatically.** Office.js exposes no book-fold property. Tell the user: **Layout → Page Setup dialog → Margins tab → Multiple pages: Book fold**, Sheets per booklet: All.

**Creep (push-out).** Inner spreads sit further out once folded — ~1 mm per 8 sheets on 80 gsm, so a 32-page booklet pushes out about 2 mm. Therefore:
- Never run writing lines or table borders hard to the outside edge
- Leave the central **6 mm either side of the fold** clear of text and rules
- Page numbers go in the outside-bottom corner, not centred

At an 8 mm outside margin the trim edge is tight — proof it, as some desktop printers can't image within 10 mm of the paper edge and will clip or scale.

**Imposition is the printer's job.** Keep pages in reading order 1, 2, 3…

## 4. Typeface — Lato family only

Never substitute Aptos, Calibri or Times New Roman.
- **Lato** — body, most headings
- **Lato Light** — Subtitle, H3, H6, Quote, Intense Quote, Subtle Emphasis
- **Lato Medium** — H7, Emphasis
- **Lato Semibold** — Example Response, Subtle Reference
- **Lato Black** — H1, H4, H5, TOC Heading, Intense Reference
- **Lato Heavy** — H9
- **Consolas** — code/plain-text styles only

## 5. Greyscale palette

| Token | Hex | Used by |
|---|---|---|
| Ink | #000000 | Body text and headings |
| Accent 1 | #969896 | Lightest table shading |
| Accent 2 | #878785 | |
| Accent 3 | #767776 | |
| Accent 4 | #585958 | |
| Accent 5 | #494A49 | |
| Accent 6 | #383938 | Darkest table shading |
| Muted | #5E5E5E | Caption, Subtle/Intense Reference |
| Link | #5E5E5E | Hyperlink, underlined (followed #343433). Changed from #898A89 (3.5:1) on 29 Sept 2026 |
| Pale | #CACBCA | Block Text, grid module fills |
| Reverse | #FFFFFF | Text on Accent 4–6 fills only |

Anything with hue is off-system — flag it rather than inserting it.

### Colour usage rules (contrast-checked, WCAG 4.5:1 for body text)

| Fill | Text on it | Never |
|---|---|---|
| Paper (white) | Ink 21 · Muted 6.5 · Link 6.5 · Link-followed 12.5 | — |
| Pale | Ink 12.9 | Muted / Link 4.0 · White 1.6 |
| Accent 1 / 2 | Ink 7.2 / 5.8 | White 2.9 / 3.6 |
| Accent 3 | Either is at the edge (Ink 4.67, White 4.50). Use for fills, bars and rules, or bold 14 pt+ only | Body text |
| Accent 4 / 5 / 6 | White 7.0 / 8.9 / 11.6 | Ink 3.0 / 2.4 / 1.8 |

- **Short version:** Ink on Pale and Accents 1–2; White on Accents 4–6; no text on Accent 3.
- **The coding set:** only Pale, Accent 2, Accent 4 and Accent 6 mark categories. Neighbouring accents are only 1.24–1.3:1 apart, and toner spread closes the gap further. Label coded rows and panels in words too.
- **Links:** always underline them. On Pale, set links in Ink. Update the Hyperlink style in Greyscale Workbooklet.dotm to #5E5E5E.
- **Captions on Pale panels** use Ink, not Muted.
- **Proportion:** about 60% paper, 30% light structure (Pale, Accents 1–2, Ink text), 10% dark emphasis (Accents 4–6).
- When converting a colour resource (BESTAE or MCCNS) to this system, put the domain or category name on every coded panel, because colour meaning is lost in greyscale.
- Step 6 of §8 (sweep for off-system formatting) now includes: text on Accent 3, Ink on Accents 4–6, White on Accents 1–3 or Pale, and adjacent-step shading used as a code.

## 6. Type scale (all headings centred, black)

| Style | Font | Size | Weight |
|---|---|---|---|
| Title | Lato | 78 pt | Bold |
| Subtitle | Lato Light | 33 pt | Regular |
| Heading 1 | Lato Black | 52 pt | Bold (keep with next) |
| Heading 2 | Lato | 36 pt | Bold |
| Heading 3 | Lato Light | 20 pt | Regular |
| Heading 4 | Lato Black | 16 pt | Bold |
| Heading 5 | Lato Black | 12 pt | Bold |
| Heading 6 | Lato Light | 16 pt | Regular |
| Heading 7 | Lato Medium | 12 pt | Regular |
| Heading 8 | Lato | 10 pt | Bold |
| Heading 9 | Lato Heavy | 10 pt | Bold |
| TOC Heading | Lato Black | 16 pt | Bold |
| Normal | Lato | 12 pt | Regular, left |

**Normal** spacing: 3.5 mm after, 4.9 mm line spacing.

## 7. Workbooklet styles

Apply by name — `para.style = "<name>"` — never rebuild with direct formatting.

| Style | Type | Indent | Space before / after | Line |
|---|---|---|---|---|
| `2. Question Format` | Lato 12 pt | 7 mm | 8.5 / 0 mm | 4.9 mm |
| `3. Multiple Choice Answers Format` | Lato 12 pt | 6 mm | 2.1 / 2.1 mm | 4.9 mm |
| `4. Marks` | Lato 18 pt bold, **right** | 0 | 0 / 3.5 mm | 4.9 mm |
| `Writing Lines` | Lato 14 pt | 2 mm | 0 / 0 mm | 6.35 mm |
| `5. Writing Lines` | Lato 14 pt | 2 mm | 0 / 4.2 mm | 6.35 mm |
| `Possible Answers` | Lato 12 pt bold | 0 | 2.1 / 2.1 mm | 4.2 mm |
| `Example Response` | Lato Semibold 12 pt bold, **white** | 0 | 2.1 / 2.1 mm | 4.2 mm |
| `White Table Heading (12pt)` | Lato 12 pt bold, **white** | 0 | 0 / 0 mm | 4.2 mm |

`Example Response` and `White Table Heading (12pt)` are white — only ever on Accent 4–6 fills.

**Table style `MARKING CRITERIA`** — the rubric table. `table.style = "MARKING CRITERIA"; table.headerRowCount = 1;`

```
MARKS | CRITERIA
2     | Describes … and explains …
1     | Lists or briefly identifies … with limited explanation.
0     | Does not identify …
```

Writing-lines blocks: at 6.35 mm line spacing, three lines ≈ one row module (20 mm). Size the block to the mark allocation — roughly 3 lines per mark for short response, which keeps answer space on the row grid.

## 8. Applying to a document

1. Determine booklet vs flat printout, then set page setup (§1). **Done when:** margins read back at the mm values for that variant.
2. Booklets only — confirm page count is a multiple of 4. **Done when:** total pages % 4 === 0.
3. Lay blocks on the grid (§2) using span widths from the tables. **Done when:** column widths read back at the span mm values.
4. Apply named styles — question stems → `2. Question Format`, mark boxes → `4. Marks`, answer space → `Writing Lines`. **Done when:** no workbooklet content is left on `Normal`.
5. Apply `MARKING CRITERIA` to rubric tables and `White Table Heading (12pt)` to their header cells. **Done when:** `table.style` reads back correctly.
6. Sweep for off-system formatting: non-Lato fonts, any colour with hue, hand-rolled bold+size fake headings, off-grid column widths, content within 6 mm of the fold.
7. `verify_doc_visual` — check white-on-grey still reads when printed mono, writing lines haven't collapsed, columns still align, and nothing has drifted into the spine.
8. Booklets only — remind the user to switch on **Book fold** in Layout → Page Setup before printing.

## 9. Rules
- New documents: base on **Greyscale Workbooklet.dotm**, don't restyle a blank doc.
- Never set `body.font.name` globally — it only stamps existing paragraphs. Set `para.style` per paragraph.
- All spatial measurements in **millimetres**; convert with `mm × 2.8346` when writing to Office.js.
- Always re-read `columnWidth` after content lands — AutoFit will have moved it.
- Spelling and conventions: **en-AU**.
