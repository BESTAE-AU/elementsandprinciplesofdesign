# Elements and Principles of Design: colour theory skills

Seven Claude skills distilled from two colour-theory YouTube playlists (20 videos, see `sources/`). They are written for teaching and designing in Graphics Technology, Multimedia, Visual Arts / Design, Textiles and D&T.

| Skill | Use it for |
|---|---|
| `colour-science-explainer` | Light, wavelength, rods and cones, RGB vs CMYK, pigment vs dye, metamerism, illusions, plus demos |
| `colour-codes-and-conversion` | RGB, HEX, HSB, CMYK and Pantone, with hand-worked hex maths and which code to use |
| `colour-palette-builder` | Brief to palette to tone match to 60-30-10 to usage rules to review; client must-have colours |
| `colour-contrast-audit` | WCAG contrast matrix, light/dark balance, danger zone, smallest fix |
| `colour-harmony-analyser` | Naming and critiquing the scheme in a poster, artwork, brand or set of hex codes |
| `colour-psychology-rationale` | Colour meanings, culture, brand case studies, written rationales, brand-deck colour slides |
| `colour-theory-teaching-activities` | Lesson sequence, activity bank, quick-recall questions, video map |

## Works with Adobe, Canva and other connectors

The skills produce tool-neutral results (named hex codes, roles, proportions, pairing rules and a rationale), then carry them into whatever is connected. See `shared/applying-in-tools.md` for the Canva (brand kits, generate/edit/comment on designs), Adobe for creativity (Express, Firefly boards, image recolouring, fonts), WordPress, Unsplash and Microsoft 365/Drive/Dropbox recipes.

The helper script also writes swatch files:

```bash
python3 shared/colour_tools.py export "Warm Ivory=#F5F0E6" "Deep Harbour=#1F3D5A" "Marigold=#F2A541" \
  --title "Harbour Cafe" --format ase --out harbour-cafe.ase   # Illustrator / Photoshop / InDesign
# formats: ase | css | canva | gpl | json
```

Other commands: `convert`, `contrast`, `audit`, `harmony` and `ratio`. They use only the Python standard library.

## Installing

- **claude.ai (web, desktop, mobile):** *Settings › Capabilities › Skills › Upload skill*, then upload each zip from `dist/`. They then work in normal chats and alongside your Canva/Adobe connectors.
- **Claude Code** (including cloud sessions on this repo): automatic. `.claude/skills` points to `skills/`.

## Editing

Edit `shared/` for the script and connector guide, and `skills/<name>/` for everything else. Then run `./scripts/build-skills.sh`, which copies the shared files into every skill and rebuilds `dist/*.zip`.
