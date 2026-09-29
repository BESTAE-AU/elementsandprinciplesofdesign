# Applying colour work in connected tools (Adobe, Canva and others)

These skills produce **tool-neutral results**: named hex codes with roles, proportions, pairing rules and a rationale. This guide explains how to carry those results into whatever the person designs in. The same process works for any plugin or connector.

## Ground rules

1. **Discover, don't assume.** Connectors differ between accounts and change over time. Look for tools by keyword (e.g. search "canva brand", "adobe colour", "express", "wordpress theme") before promising anything. Use the tool names below as examples, not guarantees.
2. **Do the colour thinking first, then apply it.** Settle the palette, its roles and contrast checks with these skills *before* calling a design tool. Design tools execute; they don't replace the rules. Give the tool the same hex codes, roles and 60-30-10 proportions.
3. **Follow each connector's own rules.** Some servers require an initialisation or playbook call first (Adobe for creativity: `adobe_mandatory_init`, then `create_visual_design_express_skill` for any visual design). Read and obey the playbook it returns.
4. **Ask before anything outward-facing or hard to undo:** publishing a Canva brand template, overwriting a brand kit, changing a live WordPress theme, sharing files.
5. **Re-check after applying.** Export or preview the result and audit the real colours (`colour_tools.py audit`). A tool may have substituted or tinted them.
6. **No connector? Hand over files.** Use `colour_tools.py export` for `.ase`, `.css`, `.gpl`, `.json` or a Canva paste list, plus written steps for applying them by hand.

## Handover pack (produce this before any tool call)

```
Palette name, harmony
Role | Name | HEX | RGB | (CMYK / Pantone if print) | proportion | allowed on
Pairing rules: bg -> text / link / button (from audit, ratios shown)
Don'ts: e.g. accent never as body text, no pink on blue
Mood words (3-5) and fonts, if chosen
```

## Canva (connector)

- **Read the existing brand first:** `list-brand-kits`. If the brand has a kit, build around its colours rather than inventing new ones (treat it as a "client must-have colour" in `colour-palette-builder`).
- **New designs:** `generate-design` / `generate-design-structured` or `create-design`. Put the handover pack in the prompt: hex codes with roles, "60% #…, 30% #…, 10% accent #… for buttons only", and the text colour rules.
- **Existing designs:** `read-design`, then `edit-design` to recolour according to the rules. `get-design-dataset` / `autofill-design` for data-driven templates.
- **Brand templates:** `create-brand-template-draft`, then `publish-brand-template` only after the person confirms.
- **Colour review of a design:** `read-design` or `export-design` (PNG), then estimate the colours, then use `colour-harmony-analyser` and `colour-contrast-audit`, then `comment-on-design` with concrete fixes (hex, ratio, where).
- Canva brand kits can't be written through every connector. If there's no write tool, give the `--format canva` list for pasting into *Brand › Colours*.

## Adobe (Adobe for creativity connector: Express, Firefly, Photoshop-style image tools, fonts)

- **Start:** `adobe_mandatory_init`, then `create_visual_design_express_skill` for posters, slides, social posts and similar. Author the design with the palette as CSS custom properties (`colour_tools.py export --format css`), then use `export_html_to_express` after its readiness check.
- **Recolour images to the palette:** `image_apply_color_overlay`, `image_apply_monochromatic_tint` (monochromatic schemes, duotone-style), `image_adjust_hsl` / `image_adjust_single_color_saturation` (tone-matching photos to the palette's saturation), `change_background_color`, `image_adjust_color_temperature` (warm/cool mood).
- **Type to match the mood:** `font_recommend`, `suggest_type_palettes` / `get_type_palette`.
- **Mood boards:** `create_firefly_board`, `boards_add_items_to_board`. Add the swatch strip and ratio bar next to the imagery.
- **Illustrator / Photoshop / InDesign desktop** (no direct connector): give the `.ase` file. Load it via *Swatches panel › Open Swatch Library › Other Library* (Illustrator) or *Swatches › Import Swatches* (Photoshop). In Illustrator, *Edit › Edit Colors › Recolor Artwork* applies a palette globally, which is useful for brand decks (see `colour-psychology-rationale`).
- **Print:** state that CMYK values from the script are approximate and that the document profile or printer decides. Recommend Pantone for packaging.

## Other connectors that often exist

| Tool | Use it to |
|---|---|
| WordPress.com | Read `theme.presets` in the site editor context, then map palette roles to the theme's colour slots (background, foreground, primary, secondary, accent). Draft changes and preview before publishing. Run a contrast audit on the pairs the theme will actually use |
| Unsplash | Find imagery for the mood board that fits the palette's hue and temperature. Describe the colours in the search ("muted teal, warm beige, soft light") |
| Microsoft 365 / Google Drive / Dropbox | File the palette handover, `.ase` and style-guide doc where the person keeps resources. Follow any filing skill they have (e.g. a knowledge-sync or Dropbox resource skill) |
| Word / PowerPoint skills (docx, pptx) | Style guides, colour slides (HEX, RGB, CMYK, Pantone per swatch) and student handouts |
| Figma (if connected) or any CSS tool | Paste the `--format css` variables or create colour styles named by role |
| Shopify | Map the palette to theme settings (buttons get the accent) and check contrast on product pages |

## Teaching resources and greyscale printing

If a resource will be printed in greyscale (e.g. with a greyscale print design system), colour can't carry meaning on the page:
- Label every swatch with its **name and hex code**.
- Show harmonies as **wheel diagrams with labelled positions**, not colour alone.
- Use value (light/dark) tasks, which print well.
- Put the full-colour version in the digital copy, Canvas page or slide deck.
