# Elements and Principles of Design, and teaching skills

Claude skills for teaching, analysing, applying and giving feedback on the **Elements and Principles of Design** in NSW TAS and design subjects (Multimedia, Graphics Technology, Visual Design, Textiles, D&T), plus subject skills and updates to Britt's existing teaching skills.

## The skills (37)

| Group | Skills | Use for |
|---|---|---|
| Start here (1) | `elements-and-principles-of-design` | Anything spanning several elements or principles, plus the design process, portfolios and evidence, visual communication, analysis, justification writing, Factors Affecting Design, whole-design feedback and marking, experimentation, brand-system testing, and characteristics/features/properties/attributes |
| Elements (12) | `<element>-element-of-design`: line, direction, shape, form, space, size-and-scale, time-and-duration, value, colour, texture, typography, layout-and-composition | Any task about one element |
| Principles (15) | `<principle>-principle-of-design`: balance, contrast, emphasis, hierarchy, movement, rhythm, repetition, pattern, proportion, unity, harmony, variety, alignment, proximity, tension | Any task about one principle. These are Britt's own Claude-built skills, kept as written, with an added `references/examples.md`. Proportion is new, in the same format. |
| Subjects (4) | `multimedia-production`, `textiles-and-fashion`, `product-design-and-manufacturing`, `visual-arts-analysis` | Subject knowledge and teaching patterns. Multimedia includes the structured Canvas teaching page format. |
| Updated teaching skills (5) | `assessment-task-designer`, `marking-rubric-builder`, `content-booklet-builder`, `practical-skill-builder`, `diverse-learning-adjustments` | Britt's existing skills, unchanged except for one or two new reference files and a pointer line each |

Not included because they're unchanged: `principles-of-design` and Britt's colour, typography, Canvas, workbooklet, table and other skills. Keep the installed versions.

## Built to stay light

- **Small always-on cost.** Claude reads every installed skill's description in every conversation. The new skills (elements, overview, subjects) add about 1,600 tokens; the principle and teaching skills replace ones already installed, so they add nothing.
- **Load only what's needed.** Each `SKILL.md` holds the essentials and a table of which reference file to open. Detail lives in `references/` files that Claude opens only when a task needs them.
- **Built-in rules:** single-lesson resources stay tight. When no rubric is supplied, marking uses `marking-rubric-builder` to create criteria first. Specialist jobs (palettes, contrast ratios, font pairing, type scales, InDesign grids, Canvas pages) hand off to the matching skills.

## Installing

- **Claude.ai:** download [`dist/all-skills-bundle.zip`](dist/all-skills-bundle.zip) (grouped into `1-start-here`, `2-elements`, `3-principles`, `4-subjects` and `5-updated-teaching-skills`) or single files from [`dist/`](dist/). Upload each `.skill` file under *Settings → Capabilities → Skills*. For a skill you already have (the principles and the five teaching skills), replace the old version.
- **Claude Code:** the skills in `.claude/skills/` load automatically in this repository.

## Editing and rebuilding

Edit only the sources in `src/`. Don't edit `.claude/skills/` or `dist/`; they are regenerated.

| Source | What it holds |
|---|---|
| `src/elements/<element>.md` | Full knowledge for each element |
| `src/principles/<name>/SKILL.md` | Britt's principle skills, kept as written |
| `src/principle-examples/<principle>.md` | Extra examples and teaching material added to each principle as `references/examples.md` |
| `src/jobs/<job>.md` | Teaching, feedback, analysis and practice workflows, shared by all elements |
| `src/method/<part>.md` | The shared method, in six parts |
| `src/overview/` | The overview skill and its guides |
| `src/subjects/<name>/` | The four subject skills, copied as is |
| `src/updated-skills/<name>/` | Britt's teaching skills with the new reference files, copied as is |

Then rebuild:

```sh
python3 tools/build_skills.py --package
```

The build checks that frontmatter parses as YAML, that names match folders, description lengths and that referenced files exist, then rebuilds `dist/`.

## Source material

`knowledge/source/` holds the ChatGPT collection this work was built from (40 topic files, the GPT instructions, index, read-me and source register). Its trimmed versions were filed into Dropbox subject folders; see `knowledge/DROPBOX-FILING.md`.
