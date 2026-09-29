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
8. **Claude skills:** upload the seven colour skill zips (`dist/*.zip`) at claude.ai › Settings › Capabilities › Skills.
