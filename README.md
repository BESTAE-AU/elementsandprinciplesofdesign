# Elements and Principles of Design

A suite of 83 Claude skills for teaching, analysing, applying and giving feedback on the **Elements and Principles of Design** in NSW TAS and design subjects (Multimedia, Graphics Technology, Visual Design, Textiles, D&T). It draws on NSW TAS design decision-making, multimedia analysis, Visual Arts, inclusive education, assessment, and professional design practice.

## What's in the suite

| Group | Count | Skills | Use for |
|---|---|---|---|
| Start here | 1 | `elements-and-principles-of-design` | Requests spanning several elements or principles; finding the right skill |
| Element skills | 12 | `<element>-element-of-design` | General knowledge of one element |
| Element job skills | 48 | `<element>-element-of-design-teaching` / `-feedback` / `-analysis` / `-practice` | One element, one job: lessons and worksheets, feedback and marking, analysis and model answers, applying it in a design |
| Principle skills | 15 | `<principle>-principle-of-design` | Balance, contrast, emphasis, hierarchy, movement, rhythm, repetition, pattern, proportion, unity, harmony, variety, alignment, proximity, tension |
| Method skills | 7 | `design-analysis-progression`, `design-justification-writing`, `factors-affecting-design`, `design-feedback-and-marking`, `design-experimentation`, `brand-system-testing`, `characteristics-features-properties-attributes` | Processes that work for any element or principle |

**Elements:** line, direction, shape, form, space, size and scale, time and duration, value, colour, texture, typography, layout and composition.

Every skill includes `references/design-method.md`, the shared method. It covers the analysis progression, justification levels, Factors Affecting Design, experimentation, teaching resources (kept tight for single lessons), differentiation, feedback and marking (using `marking-rubric-builder` when no rubric is supplied) and language rules. Colour, value, typography and layout skills hand specialist jobs to the matching specialist skills (palettes, contrast ratios, font pairing, type scales, InDesign grids) when those are installed.

## Installing

- **Claude.ai:** download [`dist/all-skills-bundle.zip`](dist/all-skills-bundle.zip) (grouped into folders) or individual files from [`dist/`](dist/), then save each `.skill` file under *Settings → Capabilities → Skills*. If you don't want all 83, start with `0-start-here`, the element skills and the method skills, then add job and principle skills for the areas you teach most.
- **Claude Code:** skills in `.claude/skills/` load automatically in this repository. Copy skill folders into another project's `.claude/skills/` or into `~/.claude/skills/` to use them elsewhere.

## Editing and rebuilding

Edit the hand-written sources:

- `shared/design-method.md` (the shared method)
- `.claude/skills/<element>-element-of-design/SKILL.md` (element knowledge)
- `.claude/skills/<principle>-principle-of-design/SKILL.md` (outside the generated block)
- the method skills and `elements-and-principles-of-design`

Then rebuild:

```sh
python3 tools/build_skills.py --package
```

This regenerates the 48 job skills from the element skills. It also:

- refreshes each principle's "What each element contributes" section and the overview's skill index
- copies the shared method into every skill
- checks names and description lengths
- rebuilds `dist/`

Don't edit the job skills or `references/` files directly; they're overwritten on rebuild.
