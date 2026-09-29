# Elements and Principles of Design

Claude skills for teaching, analysing, applying and giving feedback on the **Elements and Principles of Design** in NSW TAS and design subjects (Multimedia, Graphics Technology, Visual Design, Textiles, D&T).

## The skills (28)

| Group | Skills | Use for |
|---|---|---|
| Start here (1) | `elements-and-principles-of-design` | Anything spanning several elements or principles, plus the shared method: analysis, justification writing, Factors Affecting Design, whole-design feedback and marking, experimentation, brand-system testing, and characteristics/features/properties/attributes |
| Elements (12) | `<element>-element-of-design`: line, direction, shape, form, space, size-and-scale, time-and-duration, value, colour, texture, typography, layout-and-composition | Any task about one element: lessons, feedback and marking, analysis and model answers, applying it in a design |
| Principles (15) | `<principle>-principle-of-design`: balance, contrast, emphasis, hierarchy, movement, rhythm, repetition, pattern, proportion, unity, harmony, variety, alignment, proximity, tension | Any task about one principle |

## Built to stay light

- **Small always-on cost.** Claude reads every installed skill's description in every conversation. These 28 descriptions total about 2,200 tokens.
- **Load only what's needed.** Each `SKILL.md` holds just the essentials and a "Pick the job" table. Detail lives in `references/` files that Claude opens only when a task needs them:
  - element skills: `teaching.md`, `feedback.md`, `analysis.md`, `practice.md`, `knowledge.md`
  - principle skills: `examples.md`
  - every skill: `method/` (six small method files)

  A typical task loads the core plus one or two small files.
- **Built-in rules:** single-lesson resources stay tight. When no rubric is supplied, marking uses `marking-rubric-builder` to create criteria first. Colour, value, typography and layout skills hand specialist jobs (palettes, contrast ratios, font pairing, type scales, InDesign grids) to the matching skills when those are installed.

## Installing

- **Claude.ai:** download [`dist/all-skills-bundle.zip`](dist/all-skills-bundle.zip) (grouped into `1-start-here`, `2-elements` and `3-principles`) or single files from [`dist/`](dist/). Save each `.skill` file under *Settings → Capabilities → Skills*. You can install only the elements and principles you teach; the overview is useful with any selection.
- **Claude Code:** the skills in `.claude/skills/` load automatically in this repository.

## Editing and rebuilding

Edit only the sources in `src/`. Don't edit `.claude/skills/` or `dist/`; they are regenerated.

| Source | What it holds |
|---|---|
| `src/elements/<element>.md` | Full knowledge for each element |
| `src/principles/<principle>.md` | Full knowledge for each principle |
| `src/jobs/<job>.md` | Teaching, feedback, analysis and practice workflows, shared by all elements |
| `src/method/<part>.md` | The shared method, in six parts |
| `src/overview/` | The overview skill and its seven method guides |

Then rebuild:

```sh
python3 tools/build_skills.py --package
```

The build splits each source into a lean `SKILL.md` plus reference files, copies the method in, and generates each principle's "What each element contributes" list from the element sources. It also checks names, description lengths and file links, and rebuilds `dist/`.
