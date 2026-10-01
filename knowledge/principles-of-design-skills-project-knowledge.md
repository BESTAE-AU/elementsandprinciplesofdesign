# Principles of Design Skills — Project Knowledge

Use this file as project knowledge in any Claude project where design is taught, analysed or
produced (e.g. Multimedia, Graphics Technology, Visual Design / Visual Arts, Textiles, Design &
Technology, Timber Technology). It records the Principles of Design skills I built, how they're
named and organised, and the reasoning approach Claude should use with them.

Last updated: 1 October 2026.

---

## 1. What exists

### The main skill: `principles-of-design`

This skill covers all 15 Principles of Design. It's a framework for reasoning, teaching, critique
and justification, not a glossary. Use it for questions that span several Principles: a full
critique, a design justification, a design brief, or a unit or lesson on the Elements and
Principles.

It's structured so it loads quickly:

- `SKILL.md`: the core reasoning model and working protocols, plus a guide to which reference
  file to read for what.
- `references/principles/<principle>.md`: full knowledge for each Principle.
- `references/causal-reasoning.md`: Principle chains, networks, dependencies, and cause vs
  correlation.
- `references/relationships.md`: how each Element links to Principles, and how similar
  Principles differ.
- `references/disciplines.md`: branding, graphic design, multimedia, time-based design, UI/UX,
  textiles, product and spatial design.
- `references/cross-cutting-considerations.md`: Characteristics, Features, Properties and
  Attributes; accessibility; production; sustainability; culture and ethics; Factors Affecting
  Design (with a definition of each); trade-offs; and intentional rule-breaking.
- `references/analysis-justification-feedback.md`: the frameworks for analysis, justification,
  critique, evaluation and refinement, plus weak → sophisticated exemplars.
- `references/experimentation.md`: controlled experimentation tables.
- `references/teaching-resources.md`: questioning, vocabulary, misconceptions, resource
  sequence, differentiation, and failure-mode degrees.

### 15 single-Principle skills

Each one works on its own. **Naming convention: the Principle comes first**, so the skills sort
and read by Principle:

| Skill name | Skill name | Skill name |
|---|---|---|
| `unity-principle-of-design` | `proportion-principle-of-design` | `pattern-principle-of-design` |
| `harmony-principle-of-design` | `hierarchy-principle-of-design` | `rhythm-principle-of-design` |
| `balance-principle-of-design` | `emphasis-principle-of-design` | `movement-principle-of-design` |
| `alignment-principle-of-design` | `contrast-principle-of-design` | `tension-principle-of-design` |
| `proximity-principle-of-design` | `repetition-principle-of-design` | `variety-principle-of-design` |

Each skill contains:

- the shared reasoning model
- the full knowledge for that Principle
- how it differs from related Principles
- the causal chains it's part of
- degrees of the Principle (from absent to deliberately disrupted)
- weak → sophisticated exemplars
- steps for analysing, critiquing, justifying, generating, refining, experimenting and teaching
- language rules and a quality check

**Which skill to use:** for a question about one Principle, use that Principle's skill (e.g. "is
this balanced?" → `balance-principle-of-design`). For anything involving several Principles or
the whole framework, use `principles-of-design`.

### Source files and where everything lives

- GitHub repo: `bestae-au/elementsandprinciplesofdesign`, on the branch
  `claude/practical-maxwell-uypz51`.
- `source/principles-of-design-knowledge-base.md` is the master knowledge base, used for
  building future skills and resources.
- `source/principles-of-design-original-skill-draft.md` is the original single-file draft.
- To change content, edit the files in `principles-of-design/references/`, then rebuild the 15
  single-Principle skills with `python3 tools/build_principle_skills.py`.

---

## 2. House conventions

- **Australian English** throughout (colour, organisation, emphasise, centre, judgement).
- **Skill naming:** `<principle>-principle-of-design`, with the Principle at the start of the name.
- **Elements of Design (12):** Line, Direction, Shape, Form, Space, Size and Scale, Time and
  Duration, Value, Colour, Texture, Typography, Layout and Composition.
- **Principles of Design (15):** Unity, Harmony, Balance, Alignment, Proximity, Proportion,
  Hierarchy, Emphasis, Contrast, Repetition, Pattern, Rhythm, Movement, Tension, Variety.
- Elements are the variables a designer manipulates. Principles are the **relationships** that
  result. A Principle is never a physical object in the design.

---

## 3. Core reasoning approach (summary)

**Reasoning model**

design intention → design choices → Elements manipulated → relationship between Elements →
Principle created → interaction with other Principles → perceptual effect →
communication/function → audience or user experience → suitability → trade-offs → evaluation →
refinement

**Causal model**

Elements manipulated → primary Principle → secondary Principle(s) → perceptual effect →
communication / functional outcome → suitability for audience, purpose and context

**Causal reasoning rule:** when several Principles are identified, explain them as
**Element → Principle → Principle → Effect → Outcome** rather than listing them. Treat links as
conditional, not automatic. Separate cause from correlation: repetition doesn't automatically
create rhythm, and contrast doesn't automatically create effective hierarchy. Don't force a chain
the evidence doesn't support.

**Example chains**

- Value + size + typography → Contrast → Emphasis → Hierarchy → faster recognition of the main
  message
- Space + alignment + proximity → Grouping → Hierarchy → easier information processing
- Shape + colour + typography repetition → Repetition → Rhythm + Unity → brand consistency
- Asymmetrical placement + opposing direction + scale difference → Tension → Movement + Emphasis
- Timing + duration + scale change + motion → Temporal contrast → Emphasis → Changing hierarchy

**Considerations to weave through every response:**

- Trade-offs, framed as possible advantage ↔ possible disadvantage.
- Failure as a matter of degree: absent, weak, inconsistent, excessive, inappropriate or
  deliberately disrupted.
- Intentional rule-breaking: judge the effect, not whether a rule was followed.
- Accessibility, embedded throughout rather than added at the end.
- Production and implementation conditions.
- Culture and ethics, treated as contextual rather than universal.
- Spatial vs temporal organisation.
- Factors Affecting Design, only where they're meaningful.

---

## 4. Working protocols (summary)

| Task | Sequence |
|---|---|
| Analyse | identify → describe → explain → analyse → apply → justify → evaluate → refine |
| Critique / feedback | intended outcome → evidence → Elements → Principle → effect → audience/purpose/context → trade-off → specific change → expected effect → test |
| Justify | decision → Elements → primary Principle → secondary Principle(s) → effect → communication → purpose → audience/context → suitability (advanced: + evidence, alternative, trade-off, evaluation) |
| Generate a brief | outcome, Principles, Elements, spatial/temporal relationships, hierarchy, accessibility, constraints, system rules, acceptable variation, trade-offs, testing criteria |
| Refine | problem → evidence → variable changed → expected Principle effect → expected communication effect → test |
| Teach / build resources | knowledge → recognition → description → explanation → analysis → experimentation → application → justification → evaluation → refinement |

**Language**

- Prefer: establishes, contributes to, reinforces, disrupts, differentiates, groups, directs,
  emphasises, may be perceived as, is appropriate because.
- Avoid unsupported verdicts such as "looks good", "is professional", "is boring" or "always
  works".

**Feedback must be specific and testable.** Say what to change, which Element to change, and
what effect the change should have.

---

## 5. How this fits my other skills

When I'm building resources, use the Principles skills for the **design-reasoning content**. Pair
them with my other skills for format and delivery:

- **Workbooklets and unit sequences:** `content-booklet-builder`, then
  `workbooklet-style-system` for layout.
- **Practical or making outcomes:** `practical-skill-builder`.
- **Assessment:** `assessment-task-designer`, `marking-rubric-builder`,
  `nesa-exam-question-writer`.
- **Canvas pages and modules:** `canvas-course-builder`.
- **Colour:** `colour-harmony-analyser`, `colour-palette-builder`, `colour-contrast-audit`.
- **Typography:** `type-system-builder`, `typography-critique-audit`.
- **Adjustments and differentiation:** `diverse-learning-adjustments`,
  `newman-gifted-differentiation`.

---

## 6. Status and next steps

- Done:
  - `principles-of-design` built and installed.
  - 15 single-Principle skills built and packaged as `.skill` files, ready to install.
  - Causal-reasoning reference and Factors Affecting Design definitions added.
- Not yet done: testing the skills against realistic prompts, such as critiquing a student
  poster, writing a folio justification, or planning a hierarchy lesson.
- Possible later: tune each skill's description so Claude picks the right skill more reliably,
  and build matching skills for the 12 Elements of Design.
