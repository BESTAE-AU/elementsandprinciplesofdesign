# Word Implementation Reference

Word stores most lengths in **twips** (dxa): 1 cm = 1440 / 2.54 ≈ **566.93
twips**. Office.js uses **points**: 1 cm = 28.3465 pt, 1 mm = 2.8346 pt. Border
widths in OOXML are in **eighths of a point** (`w:sz="8"` = 1 pt).

## Conversion table

| Measurement | Twips | Points |
|---|---:|---:|
| 1 mm | 57 | 2.83 |
| 2 mm | 113 | 5.67 |
| 0.5 cm | 283 | 14.17 |
| 1 cm | 567 | 28.35 |
| 1.2 cm (booklet landscape margin) | 680 | 34.02 |
| 12.5 mm (header/footer distance) | 709 | 35.43 |
| 18 cm (portrait alternative) | 10205 | 510.24 |
| 19 cm (portrait preferred) | 10772 | 538.58 |
| 26 cm (landscape alternative) | 14740 | 737.01 |
| 27 cm (landscape preferred) | 15307 | 765.36 |
| 21 cm (A4 short edge) | 11906 | 595.28 |
| 29.7 cm (A4 long edge) | 16838 | 841.89 |

Formulae: `twips = round(cm * 1440 / 2.54)`, `points = cm * 28.3465`.

| Border | `w:sz` |
|---|---:|
| 0.5 pt | 4 |
| 1 pt | 8 |
| 3 pt (thick white separator) | 24 |

## Column widths must add up exactly

Rounding each column separately can leave the total 1–2 twips off the table
width. To avoid this:

1. Convert each column's width to twips and round.
2. Add or subtract the difference on the **widest** column, so the columns add
   up exactly to the table's twip width.
3. Use the same values in `w:tblGrid/w:gridCol` and in every cell's `w:tcW`.

Example, 27 cm as 5 + 7 + 15 cm: 2835 + 3969 + 8504 = 15308. Subtract 1 from the
15 cm column → 2835 + 3969 + 8503 = 15307.

## Table XML

```xml
<w:tbl>
  <w:tblPr>
    <w:tblW w:w="15307" w:type="dxa"/>        <!-- 27 cm -->
    <w:jc w:val="center"/>                     <!-- centred -->
    <w:tblBorders>
      <w:top    w:val="single" w:sz="8" w:color="383938"/>  <!-- outer 1 pt Accent 6 -->
      <w:left   w:val="single" w:sz="8" w:color="383938"/>
      <w:bottom w:val="single" w:sz="8" w:color="383938"/>
      <w:right  w:val="single" w:sz="8" w:color="383938"/>
      <w:insideH w:val="single" w:sz="4" w:color="969896"/> <!-- inner 0.5 pt Accent 1 -->
      <w:insideV w:val="single" w:sz="4" w:color="969896"/>
    </w:tblBorders>
    <w:tblLayout w:type="fixed"/>              <!-- AutoFit off -->
    <w:tblCellMar>                             <!-- house padding -->
      <w:top    w:w="57"  w:type="dxa"/>
      <w:left   w:w="113" w:type="dxa"/>
      <w:bottom w:w="57"  w:type="dxa"/>
      <w:right  w:w="113" w:type="dxa"/>
    </w:tblCellMar>
    <w:tblCaption w:val="Elements of design comparison"/>              <!-- alt text title -->
    <w:tblDescription w:val="Compares line, shape and colour by definition, example and effect."/>
  </w:tblPr>
  <w:tblGrid>
    <w:gridCol w:w="2835"/>
    <w:gridCol w:w="3969"/>
    <w:gridCol w:w="8503"/>
  </w:tblGrid>
  …rows…
</w:tbl>
```

Element order inside `w:tblPr` matters to Word: `tblW`, `jc`, `tblBorders`,
`tblLayout`, `tblCellMar`, `tblCaption`, `tblDescription` (other properties sit
in between if used). Wrong order can make Word report the file as corrupt.

### Rows

```xml
<w:trPr>
  <w:cantSplit/>                          <!-- never split a row across pages -->
  <w:trHeight w:val="1134" w:hRule="atLeast"/>  <!-- response space: minimum 2 cm -->
  <w:tblHeader/>                          <!-- header rows only -->
</w:trPr>
```

Keep a short table on one page by setting `<w:keepNext/>` on the paragraphs in
every row except the last. Set it on any title paragraph directly above the table as well.

### Cells

```xml
<!-- filled header cell with white separator borders -->
<w:tcPr>
  <w:tcW w:w="2835" w:type="dxa"/>
  <w:tcBorders>
    <w:bottom w:val="single" w:sz="24" w:color="FFFFFF"/>  <!-- 3 pt white separator -->
  </w:tcBorders>
  <w:shd w:val="clear" w:color="auto" w:fill="383938"/>
</w:tcPr>

<!-- vertical category column: first cell of the group -->
<w:tcPr>
  <w:tcW w:w="567" w:type="dxa"/>
  <w:vMerge w:val="restart"/>
  <w:shd w:val="clear" w:color="auto" w:fill="494A49"/>
  <w:tcMar>
    <w:left w:w="57" w:type="dxa"/><w:right w:w="57" w:type="dxa"/>
  </w:tcMar>
  <w:textDirection w:val="btLr"/>        <!-- reads bottom to top -->
  <w:vAlign w:val="center"/>
</w:tcPr>
<!-- following cells in the same group: <w:vMerge/> with the same tcW, and an empty paragraph -->

<!-- edge-to-edge image cell -->
<w:tcPr>
  <w:tcW w:w="5102" w:type="dxa"/>
  <w:tcMar>
    <w:top w:w="0" w:type="dxa"/><w:left w:w="0" w:type="dxa"/>
    <w:bottom w:w="0" w:type="dxa"/><w:right w:w="0" w:type="dxa"/>
  </w:tcMar>
</w:tcPr>
```

`w:tcPr` child order: `tcW`, `gridSpan`, `vMerge`, `tcBorders`, `shd`, `tcMar`,
`textDirection`, `vAlign`.

## Page geometry

```xml
<!-- Landscape, flat printout: 1 cm margins -->
<w:sectPr>
  <w:type w:val="nextPage"/>
  <w:pgSz w:w="16838" w:h="11906" w:orient="landscape"/>
  <w:pgMar w:top="567" w:right="567" w:bottom="567" w:left="567"
           w:header="709" w:footer="709" w:gutter="0"/>
</w:sectPr>

<!-- Landscape, saddle-stapled booklet: 1.2 cm margins -->
<w:pgMar w:top="680" w:right="680" w:bottom="680" w:left="680"
         w:header="709" w:footer="709" w:gutter="0"/>
```

In a landscape section `w:w` must be greater than `w:h`, **and** `w:orient` must
be `landscape`. Setting only one of them gives inconsistent results.

Portrait sections take their `w:pgSz` (`w:w="11906" w:h="16838"`, no
`w:orient`) and margins from the template: booklet 12 / 12 / 12 / 8 mm, flat
12 / 12 / 10 / 10 mm (top / bottom / left or inside / right or outside).

## Mixed-orientation documents

In OOXML, a section's `w:sectPr` goes **at the end of** that section, inside the
`w:pPr` of the section's last paragraph. The final section's `w:sectPr` is the
last child of `w:body`.

For a landscape table between portrait pages:

```
… portrait content …
<w:p><w:pPr><w:sectPr> PORTRAIT </w:sectPr></w:pPr></w:p>            ← ends portrait section
<w:p> table title, if any (keep with next) </w:p>
<w:tbl> … landscape table … </w:tbl>
<w:p><w:pPr> tiny carrier … <w:sectPr> LANDSCAPE, nextPage </w:sectPr></w:pPr></w:p>  ← ends landscape section
… portrait content continues …
<w:sectPr> PORTRAIT, nextPage (final section) </w:sectPr>
```

Each `w:sectPr` holds the settings of the section it **ends**. So the
`<w:type w:val="nextPage"/>` inside a section's own `sectPr` controls how that
section starts. Give both the landscape section and the portrait section after
it `nextPage`.

Checklist:

- **Clean start.** `nextPage` on both the landscape section and the following
  portrait section.
- **No blank pages.** Word requires a paragraph after a table, and here it also
  carries the section break. Make it tiny so it can't spill onto a new page:
  font size 1 pt (`<w:rPr><w:sz w:val="2"/></w:rPr>` in its `pPr`), spacing
  before/after 0, exact line spacing of 1 pt
  (`<w:spacing w:before="0" w:after="0" w:line="20" w:lineRule="exact"/>`).
  Don't add a page break next to a section break.
- **Headers and footers stay consistent.** Leave out `w:headerReference` and
  `w:footerReference` in the new sections, so they inherit from the previous
  section (linked to previous). If the template's header or footer uses a
  fixed-width table or tab stops set for portrait, check how it renders on the
  landscape page.
- **Continuous page numbering.** Don't set `w:pgNumType w:start` on the
  landscape section or on the portrait section after it.
- **Return to portrait.** The section after the landscape section has its own
  portrait `pgSz` and template margins.
- **Booklets.** Recount pages: the total must still be a multiple of 4.

## Office.js notes

Office.js takes points (`cm * 28.3465`, `mm * 2.8346`).

- `table.alignment = "Centered"` for information tables. Grid layout blocks stay
  `"Left"`, as the print design system says.
- Set every `cell.columnWidth` explicitly, then **re-read the widths after the
  content is in**. Word's AutoFit can change them.
- Header rows: `table.headerRowCount = 1`.
- Padding: `cell.setCellPadding("Left", pts)` and the same for the other sides.
- Minimum heights: `row.preferredHeight`. Office.js treats it as "at least".
- Section breaks: `paragraph.insertBreak("SectionNext", "After")`. Then set the
  new section's `pageSetup` page width and height to the landscape values and
  read them back.
- Where Office.js doesn't expose a property (for example `cantSplit`,
  `textDirection`, `tblCaption` / `tblDescription` or `vMerge`), build the table
  as OOXML and insert it with `range.insertOoxml(...)`.

## docx-js notes

For a landscape section, pass the portrait dimensions (`width: 11906,
height: 16838`) together with `orientation: PageOrientation.LANDSCAPE`. The
library swaps them. Check `word/document.xml` to confirm the resulting `w:pgSz`
matches the one above.

## Verify before delivering

1. Render to PDF (`soffice --headless --convert-to pdf file.docx`).
2. Check each page's size and orientation (`pdfinfo -f 1 -l 999 file.pdf`, or
   look at the rendered pages):
   - every landscape page is 842 × 595 pt, and the pages around it return to
     595 × 842 pt;
   - there are no blank pages;
   - page numbers run continuously;
   - headers and footers are present and render correctly on landscape pages.
3. Check each table:
   - the grid columns add up exactly to `w:tblW`;
   - no column is below its minimum width;
   - AutoFit is off (`tblLayout fixed`);
   - header rows are marked;
   - every row has `cantSplit`;
   - the table has alt text.
4. Booklets: the page count is a multiple of 4; no borders or text within 6 mm
   of the fold.
