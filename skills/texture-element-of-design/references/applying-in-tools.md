# Applying texture in tools (Adobe, Canva and others)

## Ground rules

1. **Discover, don't assume.** Connectors differ between accounts and change over time. Search for tools by keyword (e.g. "adobe grain", "canva edit", "unsplash") before promising anything. The tool names below are examples, not guarantees.
2. **Decide the texture first, then apply it.** Settle on the texture's purpose, type, strength, placement and what stays smooth *before* calling a design tool.
3. **Follow each connector's own rules.** Adobe for creativity needs `adobe_mandatory_init` first, and `create_visual_design_express_skill` for any visual design. Obey the playbook it returns.
4. **Work on copies.** Never overwrite the person's original image or design. Ask before publishing or sharing.
5. **Re-check after applying.** Preview at 100% and at the final size, and run `texture_tools.py text-over` for any text on the texture.

## Texture brief (write this before any tool call)

```
Purpose: (realism / mood / emphasis / brand story / tactile invitation)
Texture: (e.g. recycled kraft paper, fine film grain, halftone dots)
Actual or visual; simulated or invented
Where: (background only / inside heading / whole image) | Stays smooth: (text panel, logo)
Strength: (e.g. 20-40% opacity, Multiply) | Scale for output: (print A3 300 ppi / 1080 px social)
Text rule: worst-case contrast >= 4.5:1 body, 3:1 large
```

## Adobe (Adobe for creativity connector)

| Goal | Tool |
|---|---|
| Film grain on a photo or design | `image_add_grain` |
| Digital noise / grit | `image_add_noise` |
| Halftone (pop art, retro print) | `image_apply_halftone` |
| Glitch texture (Multimedia, tech, music) | `image_apply_glitch_effect` |
| Reduce texture behind text, or push background back (texture gradient) | `image_apply_gaussian_blur`, `image_apply_lens_blur` |
| Stronger or weaker surface detail | `image_adjust_brightness_and_contrast`, `image_adjust_highlights`, `image_adjust_dark_portions` |
| Turn a textured photo or rubbing into clean vector marks | `image_vectorize` |
| Isolate a textured object for a collage | `image_remove_background`, `image_select_subject` |
| Find texture images | `asset_search` (Adobe Stock) |
| Texture mood board | `create_firefly_board`, `boards_add_items_to_board` |
| Posters or social posts with texture | `create_visual_design_express_skill`, author HTML with a texture layer (CSS `background-blend-mode: multiply` or an overlay image at reduced opacity), then `export_html_to_express` after its readiness check |

## Photoshop / Photopea (desktop, no connector)

- **Overlay a texture:** place the texture above the artwork. Set the blend mode to *Multiply* (dark marks on light art), *Screen* (light dust or scratches on dark art) or *Overlay* / *Soft Light* (keeps colour). Lower the opacity to 20–60%. Desaturate the texture first (*Image › Adjustments › Desaturate*) so it doesn't shift your colours.
- **Texture only inside type or a shape:** texture layer above the type, then *Layer › Create Clipping Mask* (Alt/Option-click between layers).
- **Remove texture behind text:** add a layer mask to the texture and paint black with a soft brush where the text sits.
- **Grain:** *Filter › Noise › Add Noise* (Monochromatic, 2–6%) or *Filter › Camera Raw Filter › Effects › Grain*.
- **Wrap type onto a textured surface:** *Filter › Distort › Displace* with a greyscale copy of the texture saved as a PSD.
- **Seamless texture:** *Filter › Other › Offset* by half the width and height, then heal the visible seams.

## Illustrator and InDesign

- **Illustrator:** *Effect › Texture* (Photoshop effects in Illustrator's menu, raster); *Effect › Distort & Transform › Roughen* for rough edges; pattern swatches (*Object › Pattern › Make*) for invented textures; Image Trace for vectorising rubbings. Set document raster effects to 300 ppi for print (*Effect › Document Raster Effects Settings*).
- **InDesign:** place the texture image in a frame behind the text. Use *Object › Effects › Transparency* with Multiply and reduced opacity. Mark print finishes (spot UV, foil, emboss) on a separate spot-colour layer named for the finish, as printers expect.

## Canva (connector)

- `read-design` or `export-design` to review the current texture; `copy-design` then `edit-design` to change it on a copy.
- In the editor, search Elements for "paper texture", "grain" or "concrete". Put it behind the content, lower its *Transparency* and use *Adjust* to desaturate. Canva has no full blend modes, so transparency is the main control.
- `generate-design` prompts should include the texture brief (e.g. "subtle recycled kraft paper background at low opacity, smooth cream panel behind body text").
- `comment-on-design` with specific fixes after a critique.

## Other connectors

| Tool | Use it to |
|---|---|
| Unsplash | Find texture photos (`search_photos` with "macro texture", "kraft paper", "concrete wall", "linen close-up") and credit the photographer |
| Dropbox / Google Drive / Microsoft 365 | File texture libraries and worksheets where the teacher keeps resources; follow any filing skill they have |
| docx / pptx skills | Worksheets and slides. Embed the `swatches` SVG (converted to PNG if needed) |

## Physical and print texture

- **Print finishes:** see the table in `glossary.md`. Put each finish on its own spot-colour layer in the artwork, get a printed proof, and ask the printer for the minimum line weight for emboss and foil (fine detail fills in).
- **Paper stocks:** uncoated, felt, linen and recycled stocks add texture but make fine type and photos softer.
- **Classroom mock-ups:** stylus on a foam mat for blind emboss, PVA or clear varnish for "spot UV", textured card for stock.
- **Textiles:** texture comes from fibre, yarn (slub, bouclé), construction (weave, knit, pile), finishing (brushing, washing) and surface decoration. Present as annotated swatches: fibre, construction, handle adjectives, end use.
- **Timber:** sand through the grits along the grain; raise the grain with a damp cloth before the final sand; oil to show figure; wire-brush or scorch (yakisugi-style) for an actual texture feature. Follow workshop safety rules and PPE.

## Greyscale teaching resources

- Texture reproduces well in greyscale, so use it to separate areas and label diagrams where colour can't.
- Very fine or light textures (under about 10% grey) may vanish on a copier; increase density or line weight.
- Keep text on white or light smooth panels. Run `text-over` if text sits on any texture.
