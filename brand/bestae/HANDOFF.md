# BESTAE palette rollout: remaining steps (for Cowork)

This is a handoff from the Claude Code cloud session on 29 Sept 2026. The palette decisions are final:

| Token | Old | New |
|---|---|---|
| `s4` Communication shade | `s4-mustard` `#CFB500` | **`s4-dark-gold` `#8A6400`** (keeps the yellow base) |
| `h7-bondi-blue` | `#008EAA` | **`#007F98`** |

Text-on-fill rules:
- White text only on h1, h7, h8, h9 and every S shade. Ink `#041E42` text on every other H fill.
- On a tint, use ink or the matching S colour for text, never the matching H colour.
- Links on `t9-periwinkle` use `#201547`, underlined.
- Always show the domain name with its colour.

## Already done
- [x] BESTAE design system artifact (v7): tokens and brand book updated. https://claude.ai/artifact/9M7CWe736AqQGqWXudNdT6
- [x] Bestae Site Map artifact recoloured to BESTAE tokens (v9).
- [x] Dropbox note added: `/Teaching/Reddam House/Documents/Documents/Planning/Branding/BESTAE palette update 2026-09-29.md`
- [x] Swatch files re-exported: `brand/bestae/swatches/` (`.ase`, `.css`, `.gpl`, `.json`, Canva paste list)
- [x] Corrected copies made: `brand/bestae/updated-files/`
- [x] New Word template built: `brand/bestae/templates/BESTAE Word Template.docx` (build script alongside)

## To do on the desktop
1. **Check the new Word template** in Word: layout, Lato installed, panels and tables. It passed validation but was never rendered. Adjust `templates/build-word-template.js` if needed.
2. **Google Drive:** replace these files with the `updated-files/` versions, keeping the same names and folder:
   - `Bestae Template.pptx`
   - `Bestae Word Style Kit3.docx`
3. **Word style kit clean-up (optional):** the style kit still has many colours that are close to BESTAE values but not exact (e.g. `FF4556`, `00B6A2`, `1C6399`, `003641`, `F5EA37`, `F763B4`, `FF9730`, `BCEA55`, `32D7D4`). Map each to its BESTAE token.
4. **Dropbox:** update the table in `Bestae Branding and Word Template.docx` (2025) to match the note next to it, or replace the file with the new Word template.
5. **Canva:** in each brand kit (Bestae, Bestae Print Documents, BESTAE PRESENTATIONS, Magazine/Booklets, Colour Theory), change `CFB500` to `8A6400` and `008EAA` to `007F98`. Check any Canva designs that used the old mustard or bondi blue.
6. **Adobe:** load `swatches/bestae.ase` into the Illustrator, InDesign and Photoshop Swatches panels.
7. **Claude Projects:** check the Multimedia project (and any other) for knowledge files that hold BESTAE colours, and update them.
8. [x] **Claude skills:** the seven colour skills are installed (confirmed 29 Sept 2026).

## MCCNS (added later the same day)
- [x] MCCNS colour usage guide: `brand/mccns/colour-usage-guide.md`. Swatches are in `brand/mccns/swatches/`. No brand components were changed.
- [x] MCCNS design system in Claude: https://claude.ai/artifact/G6i4tRCPKbEKhM5PwcBNF5. A copy of its files is in `brand/mccns/design-system/`.
- [ ] Ask the MCCNS marketing office to confirm that Light Blue is `#909DB2`. The guideline's RGB, CMYK and swatch all say so, but its printed HEX `#D9DDE2` looks like a misprint.
- [ ] Get the official `.eps` logo suite, Mary's Monogram and the spear files from the school, and add them to the design system's Logos group.
- [ ] Canva: add a MCCNS brand kit from `brand/mccns/swatches/mccns-canva-paste-list.txt`, if there isn't one yet.

## MBE Creative Studio and Greyscale Workbooklet (added later the same day)
- [x] MBE design system updated (v7): colour usage rules and corrected token notes. No colours were changed. https://claude.ai/artifact/2ptfHF8cDnoeLt3RDdtzWi
- [x] Greyscale Workbooklet design system created: https://claude.ai/artifact/AHsqwt586J6rMJDpkqSdL8
- [x] MCCNS type sizes converted from pt to px. The design system format drops pt sizes.
- [x] Updated greyscale skill installed (confirmed).
- [ ] Greyscale: in `Greyscale Workbooklet.dotm`, change the Hyperlink style colour from #898A89 to **#5E5E5E** (decided and applied in the design system and skill).
- [x] MBE: small pink CTAs use the new `accent-bloom-deep` #e3008c with white text; inputs use `border-strong` #a48061.

## Cross-system audit fixes (applied the same day)
- [x] BESTAE tints: `t5` #E8F6C4, `t8` #D2DCE8, `t10` #F7D0E6. Design system v8, swatches, Word template, PowerPoint copy and site map are all updated, and a Dropbox note is added.
- [ ] Canva brand kits: also change `EFF4A4` to `E8F6C4`, `D5EBEE` to `D2DCE8` and `F2DEE9` to `F7D0E6` (as well as the earlier two changes).
- [ ] Adobe: reload `brand/bestae/swatches/bestae.ase` (re-exported with the new tints).
- [x] Greyscale skill re-uploaded with the new link colour and coding set (confirmed).
- [ ] MBE: add `#e3008c` and `#a48061` to any MBE Canva brand kit or website stylesheet.

## Skills that still carried the old palette (found after install)
- [ ] Replace these four skills with the updated zips in `skill-updates/`: `workbooklet-style-system`, `indesign-parameters`, `word-tables` and `canvas-course-builder`. Each has the Dark Gold shade (white text, headers only), the new Bondi Blue (white text), the three new tints and the Greyscale link #5E5E5E. The `indesign-parameters` contrast script (`grid.py --domains`) confirms every value.

## Colour theory knowledge file (1 Oct 2026)
- [x] Built `knowledge/colour-theory-knowledge.md`: all colour theory plus the current four brand palettes.
- [ ] Add it to the knowledge of each relevant Claude Project (Multimedia, and any Graphics, Textiles or Visual Arts projects).
- [ ] Archive the copy `knowledge/XSTAGE_DesignFactors_Guide-ColourTheory.md` into Dropbox `Teaching/Multimedia/Claude Knowledge/01 Terms and Frameworks/`. The Dropbox connector can't upload files from the cloud session, so Cowork should copy it.
