# Word Implementation Reference

These are the OOXML values used to build the table system in a .docx. Word stores
lengths in **twips** (dxa): 1 cm = 1440 / 2.54 ≈ **566.93 twips**.

## Conversion table

| Measurement | Twips |
|---|---:|
| 0.5 cm | 283 |
| 1 cm | 567 |
| 18 cm (portrait alternative) | 10205 |
| 19 cm (portrait preferred) | 10772 |
| 26 cm (landscape alternative) | 14740 |
| 27 cm (landscape preferred) | 15307 |
| 27.7 cm (landscape usable width) | 15704 |
| 21 cm (A4 short edge) | 11906 |
| 29.7 cm (A4 long edge) | 16838 |

Formula: `twips = round(cm * 1440 / 2.54)`.

## Column widths must sum exactly

Rounding each column separately can leave the columns 1–2 twips off the table
width. To avoid this:

1. Convert each column's cm width to twips and round.
2. Add or subtract the difference on the **widest** column so the columns add up
   exactly to the table's twip width.
3. Use the same values in `w:tblGrid/w:gridCol` and in every cell's `w:tcW`.

Example, 27 cm as 5 + 7 + 15 cm: 2835 + 3969 + 8504 = 15308. Subtract 1 from the
15 cm column → 2835 + 3969 + 8503 = 15307.

## Table properties

```xml
<w:tblPr>
  <w:tblW w:w="15307" w:type="dxa"/>   <!-- 27 cm -->
  <w:jc w:val="center"/>                <!-- centred table alignment -->
  <w:tblLayout w:type="fixed"/>         <!-- stop Word auto-resizing columns -->
</w:tblPr>
<w:tblGrid>
  <w:gridCol w:w="2835"/>
  <w:gridCol w:w="3969"/>
  <w:gridCol w:w="8503"/>
</w:tblGrid>
```

Each row:

```xml
<w:trPr>
  <w:cantSplit/>        <!-- never split an individual row across pages -->
  <w:tblHeader/>        <!-- header rows only: repeat on each page of a long table -->
</w:trPr>
```

To keep a short table on one page, set `keepNext` on the paragraphs in every row
except the last.

## Landscape section geometry (§60)

```xml
<w:sectPr>
  <w:pgSz w:w="16838" w:h="11906" w:orient="landscape"/>
  <w:pgMar w:top="567" w:bottom="567" w:left="567" w:right="567"
           w:header="567" w:footer="567" w:gutter="0"/>
</w:sectPr>
```

In a landscape section, `w:w` must be greater than `w:h` **and** `w:orient` must
be `landscape`. Setting only one of these gives inconsistent results. Keep the
`w:header` and `w:footer` distances the same as the template's portrait sections.

With **docx-js**, pass the portrait dimensions (`width: 11906, height: 16838`)
together with `orientation: PageOrientation.LANDSCAPE`. The library swaps them.
Check the generated `word/document.xml` to confirm the `w:pgSz` above.

## Mixed-orientation documents (§66)

In OOXML, a section's `w:sectPr` goes **at the end of** that section: inside the
`w:pPr` of the section's last paragraph. The final section's `w:sectPr` is the
last child of `w:body`.

For a landscape table between portrait pages:

```
… portrait content …
<w:p> <w:pPr> <w:sectPr> PORTRAIT, type=nextPage </w:sectPr> </w:pPr> </w:p>   ← ends portrait section
[Heading 4 table heading]
<w:tbl> … landscape table … </w:tbl>
<w:p> <w:pPr> <w:sectPr> LANDSCAPE, type=nextPage </w:sectPr> </w:pPr> </w:p>  ← ends landscape section
… portrait content continues …
<w:sectPr> PORTRAIT (final) </w:sectPr>
```

Checklist:

- **Clean start.** Use `<w:type w:val="nextPage"/>` so the landscape section
  starts on a new page.
- **No blank pages.** Word requires a paragraph after a table. Use that paragraph
  as the section-break carrier and make it tiny: font size 1 pt (`w:sz w:val="2"`),
  spacing before/after 0, line spacing exact 1 pt. Don't add a separate page
  break before or after a section break.
- **Headers and footers stay consistent.** Leave out `w:headerReference` and
  `w:footerReference` in the new sections so they inherit from the previous
  section (linked to previous). If the template's header/footer uses a fixed-width
  table or tab stops set for portrait, check how it renders on the landscape page.
- **Continuous page numbering.** Don't set `w:pgNumType w:start` on the landscape
  section or on the portrait section that follows it.
- **Return to portrait.** The section after the landscape section must have its
  own portrait `w:pgSz` (`w:w="11906" w:h="16838"`, no `w:orient`) and portrait
  margins copied from the template.
- **Table stays centred.** Keep `w:jc="center"` on the table. The 27/26 cm width
  leaves 0.35/0.85 cm spare on each side of the 27.7 cm usable width.

## Verify before delivering

- Render to PDF (e.g. `soffice --headless --convert-to pdf`). Check each landscape
  page's orientation, that the table is centred, that no page is blank, that page
  numbers run continuously, and that headers and footers look right.
- Check that the grid column widths add up exactly to `w:tblW`.
