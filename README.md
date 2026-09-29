# elementsandprinciplesofdesign

Claude skills for teaching the elements and principles of design in NSW Stage 4–6 design subjects.

## Typography skills (`skills/`)

Built from the "Typography" YouTube playlist (Canva, DesignSpo, Envato Tuts+, The Color Palette Studio). They follow the same pattern as the colour-theory skills.

| Skill | What it does |
|---|---|
| `typography-fundamentals-explainer` | Explains terms, anatomy, units, classifications and history at the learner's level, and corrects the videos' factual slips |
| `typeface-selection-rationale` | Chooses and pairs fonts for a brief (heading = extrovert, body = introvert) and writes the justification |
| `type-system-builder` | Builds a type scale and style spec (sizes, leading, tracking, line length, grid) for InDesign, Word, Canva or CSS |
| `typography-critique-audit` | Critiques the typography of a design or student work, with prioritised fixes and marking feedback |
| `typography-teaching-activities` | Lessons, a 6-lesson sequence, 12 activities and a timestamped video map |

`scripts/type_tools.py` (standard library Python) handles unit conversion, type scales, leading, line length and WCAG contrast. It is copied into each skill that uses it so every skill works on its own.

Installable packages are in `dist/` (`.skill` files).
