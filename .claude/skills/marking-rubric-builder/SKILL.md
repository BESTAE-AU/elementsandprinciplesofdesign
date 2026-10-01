---
name: "marking-rubric-builder"
description: "Writes NESA-aligned marking rubrics matching the school's A-E common grade scale: builds an HSC-style matrix first, then translates it into the vertical marking-criteria format used in assessment tasks. Use for any request to write, build, draft or revise a marking rubric or marking criteria."
---

# Marking Rubric Builder

Builds marking rubrics for Stage 4-6 (Years 7-12) tasks at Marist Catholic College North Shore that speak the school's actual grading language and NESA's marking vocabulary, in the two-stage workflow the teacher thinks in: a matrix rubric first (the HSC practical-subject format), then a translation of that matrix into the vertical marking-criteria format used in her actual assessment task documents.

Do not skip straight to the vertical format. The matrix is the reasoning tool — it is where grade consistency across criteria gets checked — and the vertical version is a re-presentation of the same content, not a separately-invented one.

## Step 0 — Gather inputs before writing anything

Ask (or infer from supplied task material) whatever is missing from this list. Don't guess silently on the items that change the rubric's substance:

- **The task itself**: what students actually produce/do (practical piece, folio, written response, presentation, etc.) and its syllabus outcomes.
- **Stage/course**: Stage 4-5 (Years 7-10) is governed by the NESA Common Grade Scale + Stage 4/5 Performance Descriptors below — this is the school's confirmed reporting framework for those years. Stage 6 (HSC) courses have their own NESA performance-band descriptors per course/component — if the task is Stage 6, ask whether the teacher has the course-specific performance descriptors to hand, or default to adapting the common grade scale's structure and language (extensive/thorough/sound/basic/elementary) since that is the house style, flagging that official HSC band descriptors should be swapped in if she has them.
- **Total marks** for the task and how they're distributed across criteria (equal weighting is a reasonable default if not specified — state the assumption). Any convenient raw total works (10, 20, 50) — the school reports learning tasks to families as a percentage out of 100 regardless (an "Assessment Mark" column on the report), so the raw total just needs to divide cleanly into sensible mark bands; only build the rubric directly out of /100 if she asks for that specifically.
- **Number of criteria/rows**: usually 3-6, each mapping to one or more outcomes. If she's supplied a task description, propose a criteria breakdown and confirm it covers the outcomes rather than inventing an unrelated structure. Keep to **one outcome per criterion where possible** — if two outcomes are both genuinely and substantially applicable to the same piece of evidence, split that into two criteria rather than double-tagging one row. The deliberate exception is when two outcomes are two lenses on the exact same evaluative act (e.g. evaluating a product's own qualities and evaluating that product's wider impact) — a teacher may choose to combine those into one row and tag both codes; treat this as an explicit override to flag back, not a default.
- **Formative or summative**: summative tasks need the full mark-bearing rubric; formative tasks may only need 3-4 tiers of feedback-oriented descriptors plus the written feedback lines (what was done well / what to improve / how to improve) — don't force full HSC matrix machinery onto a quick formative check unless asked.
- **Adjustments/differentiation**: if the task has a scaffolded or adjusted version for a student with disability, that version's rubric must still offer a genuine pathway to every grade band (A-E) — NESA guidance is explicit that adjustments must not cap a student's access to the full range of grades. Build the extension/scaffold variants alongside the standard rubric, not as a separate lower-ceiling version.
- **School adjustment layer**: when need profiles are named, apply `diverse-learning-adjustments` (reads the Diverse Learning project's `claude/school-adjustment-bank.md`) and add a short marking note on how to mark alternative response formats (oral, annotated sketch, photo portfolio, voice-to-text, scribed) against the same criteria. Need profiles only, never student names.
- **Newman / gifted layer**: for Newman classes apply `newman-gifted-differentiation` — A-band descriptors reward off-level work (originality, synthesis, justification, evaluation, transfer; SOLO relational/extended abstract) within the same rubric, not a separate Newman rubric; add a moderation note.

## Reference: the school's common grade scale (use this wording as the base)

Confirmed against the school's own "Guide to Year 7-10 Student Reports" and a real example report: Learning Outcomes, Learning Tasks and Grade Distribution are reported using the NESA Common Grade Scale and Stage 4/5 Performance Descriptors below. Every custom criterion descriptor should read as a task-specific instance of the relevant grade's paragraph — same strands, same register, same verbs — not generic AI rubric language.

Note on provenance: this exact wording is technically NESA's *Common Grade Scale for Preliminary courses* (designed for Year 11), which the school has adopted for its Years 7-10 reporting — it's richer than the plainer, generic NESA Years 1-10 Common Grade Scale wording (which just says e.g. "extensive knowledge and understanding of the content and can readily apply this knowledge", with no mention of contexts, creative/critical thinking or communication). Always use the version below, not the plainer generic one, even if a NESA search turns up the other wording.

> **A** — The student demonstrates extensive knowledge of content and understanding of course concepts, and applies highly developed skills and processes in a wide variety of contexts. In addition, the student demonstrates creative and critical thinking skills using perceptive analysis and evaluation. The student effectively communicates complex ideas and information.
>
> **B** — The student demonstrates thorough knowledge of content and understanding of course concepts, and applies well-developed skills and processes in a variety of contexts. In addition, the student demonstrates creative and critical thinking skills using analysis and evaluation. The student clearly communicates complex ideas and information.
>
> **C** — The student demonstrates sound knowledge of content and understanding of course concepts, and applies skills and processes in a range of familiar contexts. In addition, the student demonstrates skills in selecting and integrating information and communicates relevant ideas in an appropriate manner.
>
> **D** — The student demonstrates a basic knowledge of content and understanding of course concepts, and applies skills and processes in some familiar contexts. In addition, the student demonstrates skills in selecting and using information and communicates ideas in a descriptive manner.
>
> **E** — The student demonstrates an elementary knowledge of content and understanding of course concepts, and applies some skills and processes with guidance. In addition, the student demonstrates elementary skills in recounting information and communicating ideas.

Use this exact grade-word ladder — **extensive / thorough / sound / basic / elementary** — not softened synonyms ("limited", "developing", etc.), so rubrics read consistently with reports and other school documents. On the report itself, each Learning Outcome is tagged with just the single grade word (e.g. "Extensive") — keep that word consistent with whatever band the rubric ultimately places the student in.

Remember that a semester/report grade is a **holistic on-balance professional judgement** across multiple pieces of evidence, not a straight average of task marks — a rubric produced here informs that judgement for one task, it doesn't determine the overall subject grade by itself.

### The four strands embedded in that scale

Every grade paragraph above is built from the same four strands, tiered A→E. When writing a custom criterion, pick whichever strand(s) the criterion actually assesses and tier it the same way:

1. **Knowledge & understanding of content/concepts** — extensive → thorough → sound → basic → elementary knowledge.
2. **Skills & processes applied in context** — wide variety of contexts (highly developed) → variety of contexts (well-developed) → range of familiar contexts → some familiar contexts (basic) → with guidance (elementary).
3. **Creative & critical thinking** — perceptive analysis and evaluation → analysis and evaluation → selecting and integrating information → selecting and using information → recounting information.
4. **Communication** — effectively communicates complex ideas → clearly communicates complex ideas → communicates relevant ideas appropriately → communicates ideas descriptively → communicates ideas (elementary, guided).

### Bloom's verb ladder (use to push descriptors up the thinking ladder, per the teacher's standing instruction)

| Grade | Bloom's level | Typical verbs to build into the descriptor |
|---|---|---|
| A | Evaluate / Create | evaluate, justify, critically analyse, synthesise, design, appraise, formulate |
| B | Analyse / Evaluate | analyse, compare, differentiate, examine, assess, critique |
| C | Apply | apply, demonstrate, implement, select and integrate, solve, use |
| D | Understand | describe, explain, outline, summarise, classify, select and use |
| E | Remember (guided) | identify, recall, list, label, recount, define |

### Alternative verb ladder — List → Outline → Describe → thorough → extensive (for descriptive/justification-style criteria)

The Bloom's ladder above is the default because most criteria genuinely escalate in cognitive complexity from E to A (recalling vs. evaluating are different mental operations). But some criteria — a Statement of Intent, a justification of selected materials/tools/processes, a Design Brief — aren't really asking students to think at a different cognitive level per band; they're asking students to cover the same content more fully and with more depth as the grade rises. For these, a single-verb-family ladder that scales by *completeness and depth* rather than by *switching verbs across cognitive levels* often reads more naturally and avoids descriptors that feel like a forced fit to Bloom's:

| Grade | Verb pattern | Example |
|---|---|---|
| A / Extensive | "Provides an extensive description/justification of..." (or: extensively describes/justifies) | Provides an extensive justification of the selected materials, tools, equipment, techniques and processes, with clear reasoning for their appropriateness. |
| B / Thorough | "Provides a thorough description/justification of..." (thoroughly describes/justifies) | Provides a thorough justification of the selected materials, tools, equipment, techniques and processes, with clear reasoning for most choices. |
| C / Sound | "Describes / justifies..." | Describes the selection of materials, tools, equipment, techniques and processes, with some justification of choices. |
| D / Basic | "Outlines..." | Outlines the selection of materials, tools, equipment, techniques and/or processes, with limited or superficial justification. |
| E / Elementary | "Lists..." | Lists materials, tools, equipment, techniques and/or processes, with guidance, providing little or no justification. |

When to reach for this instead of Bloom's: the criterion is fundamentally about how fully/completely a student covers required content in a written planning or justification document, not about escalating skill or thinking. When to stick with Bloom's: the criterion assesses genuine escalation in cognitive operation (evaluating vs. applying vs. recalling) — most practical/production and evaluation criteria. Both ladders are valid tools; pick whichever one actually describes what changes between bands for that specific criterion, and don't mix the two verb families within a single criterion's five bands.

## Reference: General capabilities (use these exact names when tagging — don't invent others)

Fixed list — only the capabilities actually relevant to the task/subject get tagged, not all seven:

| Capability | What it covers |
|---|---|
| Critical and creative thinking | Applying critical/creative thinking skills specific to the subject's outcomes and content |
| Literacy | Developing and applying knowledge/skills to communicate and comprehend effectively |
| Numeracy | Understanding and applying mathematical knowledge and skills across contexts |
| Digital literacy | Using digital tools and technologies to solve problems and work collaboratively |
| Ethical understanding | Understanding ethical/moral concepts; managing context, conflict and uncertainty |
| Intercultural understanding | Understanding the dynamic, variable nature of culture and cultural diversity |
| Personal and social capability | Understanding self and others; managing relationships, life, work and learning |

On reports, capabilities are rated on their own 5-point scale — **Well below / Below / At / Above / Well above expected standard** — which is separate from the A-E academic grade above. Don't blend the two scales: a rubric's mark-earning criteria use the A-E ladder; a capability tag just names which capability(s) the criterion draws on.

## Reference: Commitment to Learning / Commitment to Self & Others (separate axis from the A-E grade)

Rated on a 4-point Level of Achievement scale — not marks, and not this rubric-builder's main output, but relevant if a task's reporting also feeds these:

| Level | Description |
|---|---|
| Always | Evidence indicates application to meet this outcome consistently |
| Usually | Evidence indicates regular application to meet this outcome |
| Sometimes | Evidence indicates some application to meet this outcome, but not on a consistent basis |
| Rarely | Evidence indicates that further assistance and/or encouragement is needed to meet this outcome |

**Commitment to Learning** dispositions (confirmed via example report — use these exact five, don't invent others):
- Confident in working with information and ideas – their own and those of others
- Demonstrates initiative and responsibility toward their own learning
- Reflective as a learner, developing their ability to learn
- Responsive to and respectful of the learning of others
- Innovative and equipped for new and future challenges

**Commitment to Self and Others** (CASEL-model social/emotional learning outcomes) uses the same 4-point scale; specific items not yet supplied — ask if a task needs to reference one.

Only bring this scale into a rubric if asked — the default rubric output is the academic A-E matrix/vertical criteria above. Note: a criterion built around ongoing work practices, engagement, preparedness or time management (as opposed to a piece of evidence a student hands in) sits at the boundary between the academic A-E scale and this Commitment to Learning axis — flag this explicitly to the teacher when such a criterion comes up, since she may want it marked here instead of (or as well as) on the task's A-E rubric.

## Step 1 — Build the matrix rubric (HSC practical-subject format)

Structure: rows = criteria (each tagged with its outcome(s)), columns = grades A-E, cells = mark range + task-specific descriptor built from the strand(s) that criterion assesses, worded through the Bloom's verb (or the alternative List→Outline→Describe ladder above, where that fits better) for that grade.

Mark bands per criterion (proportional split of that criterion's total marks — adjust rounding so bands are whole numbers and never overlap; double-check adjacent bands don't share a boundary number, e.g. "7-8" then "8-10" is an overlap error):

| Grade | % of criterion's marks | 
|---|---|
| A | ~90-100% |
| B | ~70-89% |
| C | ~50-69% |
| D | ~30-49% |
| E | ~10-29% |
| (below E) | 0-9%, or 0 for non-attempt |

Worked example — criterion "Applies design thinking to develop textile design solutions" (outcome TE5-3, 10 marks):

| Grade | Marks | Descriptor |
|---|---|---|
| A | 9-10 | Perceptively evaluates and synthesises design options, applying highly developed design-thinking skills across a wide variety of contexts to justify the final design direction |
| B | 7-8 | Analyses and compares design options, applying well-developed design-thinking skills across a variety of contexts to support the design direction |
| C | 5-6 | Applies design-thinking skills in a range of familiar contexts, selecting and integrating design options into an appropriate direction |
| D | 3-4 | Applies design-thinking skills in some familiar contexts, describing design options in a basic direction |
| E | 1-2 | Recounts design options with guidance, demonstrating elementary application of design-thinking skills |

Repeat for each criterion. Check across the finished matrix that: the mark bands sum correctly to the task total; language escalates consistently strand-by-strand across every row (an A shouldn't accidentally read easier than a B in another row); and no descriptor introduces content the task didn't actually ask for.

## Step 2 — Translate the matrix into the vertical marking-criteria format

This is the format that goes into her actual assessment task documents — modelled on the real NESA/HSC criteria-table pattern (e.g. the Design and Technology Major Design Project exam criteria: a criteria list against total marks). Each matrix row becomes its own vertical block: a small table with **Marks** in one column and **Criteria** in the other, mark ranges listed top-to-bottom from highest to lowest, using the same descriptor text as the matrix (don't re-draft it — this is a reformat, not a rewrite).

Worked example (continuing from above):

**Applies design thinking to develop textile design solutions (TE5-3)**

| Marks | Criteria |
|---|---|
| 9-10 | Perceptively evaluates and synthesises design options, applying highly developed design-thinking skills across a wide variety of contexts to justify the final design direction |
| 7-8 | Analyses and compares design options, applying well-developed design-thinking skills across a variety of contexts to support the design direction |
| 5-6 | Applies design-thinking skills in a range of familiar contexts, selecting and integrating design options into an appropriate direction |
| 3-4 | Applies design-thinking skills in some familiar contexts, describing design options in a basic direction |
| 1-2 | Recounts design options with guidance, demonstrating elementary application of design-thinking skills |

Stack one such block per criterion, in task order. If the task groups several small criteria under one heading (common for shorter tasks), merge their descriptors into one combined line per band rather than producing a wall of tiny tables.

## Step 3 — Tag for reporting traceability

Under (or beside) each criterion block, add a compact tag line the teacher can lift into her outcomes/general-capabilities tracking spreadsheet, using only the canonical outcome codes, capability names and (if relevant) Commitment to Learning items from the reference tables above, e.g.:

`Outcomes: TE5-3, TE5-8 | General capabilities: Critical and creative thinking | Commitment to learning: Demonstrates initiative and responsibility toward their own learning (only if the task also reports this)`

Don't invent outcome codes, capability names, or disposition wording — use the ones supplied with the task or the fixed lists above. When a criterion genuinely doesn't map to any outcome (e.g. a pure work-practices/completion row), say so explicitly rather than forcing a code onto it, and flag it against the Commitment to Learning note above.

## Step 4 — Formative tasks (lighter-weight variant)

For formative checks, skip the full 0-100% matrix machinery unless asked. Produce 3-4 tiers (e.g. Extensive/Thorough–Sound–Basic/Elementary, collapsing adjacent bands) per criterion, and close with three short written-feedback lines per student-facing copy: what was done well, what to improve, and how to improve it — matching her standing feedback requirement.

## Stage 6 / HSC tasks

If the task is genuinely Stage 6 (Year 11-12), don't default to the Stage 4-5 wording above without checking first — use the actual NESA course performance bands where they're known (Design and Technology, Industrial Technology, Textiles and Design, Software Engineering, Graphics Technology and others have official Board 1-6 performance-band descriptions; the teacher may have them on hand from the project's reference material, or ask her to paste/search for the course-specific ones if not). Note the HSC scale is Bands 1-6, not letters A-E — don't relabel bands as letters.

## Output & formatting

- Deliver as a Word document (.docx) unless the teacher asks otherwise — these get printed and pasted into assessment task booklets.
- Keep tables clean and print-ready; if this is going into a booklet/workbooklet being built with the print design system, mention that the greyscale-print-design-system skill should be applied at that layout stage rather than duplicating its formatting rules here.
- Always show the matrix version first (even briefly) before presenting the vertical version, so the teacher can sanity-check grade consistency before it's locked into task-document format.
- When work spans several messages of iteration (very common — this teacher typically refines wording criterion-by-criterion in chat before committing to a document), keep a running mental tally of: mark bands assigned per criterion, outcome codes used/reused/missing from the task's full outcome list, and any specific vocabulary substitutions requested (e.g. "remove X term", "use this verb ladder instead") so later criteria stay consistent with earlier decisions without the teacher having to repeat instructions.

## Before delivering — quick check

- Grade language matches the school scale exactly (extensive/thorough/sound/basic/elementary — not synonyms) for Stage 4-5, or the correct course's Band 1-6 language for Stage 6.
- Descriptors are task-specific, not the generic whole-of-course paragraph copy-pasted per row.
- Verbs step up correctly from E to A within every criterion, using either the Bloom's ladder or the List→Outline→Describe→thorough→extensive alternative — and consistently one or the other within a single criterion's five bands, not a mix.
- Mark bands per criterion sum to the stated task total, and adjacent bands don't overlap at a shared boundary number.
- Outcomes, general capabilities, and (if used) Commitment to Learning items are tagged using only the school's canonical names, not invented — and any criterion without a clean outcome fit is flagged rather than force-tagged.
- Any adjusted/scaffolded variant still reaches every grade band — it isn't capped.
- Vertical version's wording matches the matrix version's wording (reformatted, not rewritten).

## Reference file

- `references/descriptor-quality-and-feedback.md` — writing and auditing descriptors, avoiding overlap, borderline decisions, feedback banks, and analytic, holistic, single-point, university (HD to F), reflective, argument and ethical-reasoning rubrics. Read when auditing a rubric, writing a feedback bank, or working outside the school A–E scale.
