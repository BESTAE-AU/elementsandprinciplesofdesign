---
name: "diverse-learning-adjustments"
description: "Adds student-needs adjustments to any teaching work: adapts resources into tiers, adjusts assessments and exam provisions, builds class adjustment plans, and gives quick strategies for a need, using the school's own adjustment bank."
---

# Diverse Learning Adjustments (hub skill)

For Britt, a NSW secondary TAS/Visual Arts teacher (Textiles, D&T, Timber, Multimedia, Graphics, Visual Arts; Stages 4–6) at Marist Catholic College North Shore (Sydney Catholic Schools). This is the **single entry point for student needs**: differentiation, accommodations, adjustments, exam provisions and class plans. NCCD levels, evidence and program compliance belong to the companion skill `nccd-adjustments-evidence`. Gifted, Newman class, extension-by-design, compacting, underachievement and 2E strength-side planning belong to `newman-gifted-differentiation`.

## How it fits with Britt's other skills
- `content-booklet-builder`, `practical-skill-builder`, `assessment-task-designer` and `marking-rubric-builder` own the **instructional design**. Their generic differentiation sections stay as they are.
- This skill adds the **school-specific adjustment layer** on top. When one of those skills is building something and Britt names need profiles or a class ("my Year 8 textiles class has 4 ADHD, 1 VI…"), run this skill as well and add its output as a section of that resource.
- Layout and print: `workbooklet-style-system` / `greyscale-print-design-system`. Word output: `docx`; `word-tables` for tables.

## Sources (Diverse Learning project; read with the Projects tool)
1. `claude/school-adjustment-bank.md` — **the college's own adjustment wording and exam provisions, by need. Use it first and match its language.**
2. `claude/school-need-profiles.md` — school fact sheets (ADHD, APD, ASD, MH, ODD, SPD, SLD), the Levels of Adjustment Breakdown, and the PPSD Functional Impact Checklist.
3. `claude/nesa-adjustment-examples.md` — NESA adjustment areas (making/constructing, communication, reading, writing, group work, etc.) and the Omar Technology Mandatory case study.
4. `claude/hpge-differentiation-adjustments.md` — the 9 HPGE adjustments for extension, gifted and 2E students.
5. `claude/newman-gifted-program.md` — the school's Newman Selective Gifted Program process (pre-assessment, compacting, flexible grouping, Elegant Design assessment, underachievement, 2E).
If the project isn't reachable, use the fallback library at the end.

## Non-negotiables
- **Need profiles, never names.** Describe students by need ("P1: ADHD + anxiety, exit pass"). No names, diagnoses or health details on anything student-facing. Label versions neutrally (A/B/C or colours).
- **Same outcome, different access.** Adjust how students access and show learning, not what is assessed. Flag anything that changes the outcome (different stage, Life Skills) for the Diverse Learning team rather than deciding it.
- **Never cap grades.** Every adjusted task or rubric keeps a genuine pathway to A–E.
- Handle privately: some students don't know their diagnosis; some profiles flag sensitive topics, past bullying or embarrassment about needing help. Keep support subtle.
- Australian spelling. Web-search any external resource before recommending it, and only include strong, current sources.

## Pick the mode from the request (ask once, only for what's missing)

### Mode A — Adapt a resource (worksheet, lesson, booklet page, slides)
Inputs: the resource (read all of it), year and subject, outcomes, need profiles, output format (default .docx).
Output:
1. **Three tiers** with the same layout and page count:
   - **Supported:** chunked, numbered single-step instructions; worked example; sentence starters; word bank with visuals; cloze, matching or labelled-diagram options; fewer items covering the same outcome; "done looks like" checklist; uncluttered layout.
   - **Core:** the original tidied up, with success criteria visible.
   - **Extension:** deeper, not more. Use the HPGE adjustments (complexity, challenge, choice, abstraction, authenticity). For a Newman class or a full gifted plan, hand off to `newman-gifted-differentiation`.
2. **Adjustments table:** *Profile | Adjustment (school wording) | How it applies to this resource | Lesson moment*.
3. **Practical/workshop layer** (almost always needed): photo step cards and SOPs at each station; demonstration over explanation; pre-cut or pre-marked materials, jigs, pre-threaded machines; reduced-choice kits; ear protection or headphones and a quiet bench; warning before machines start; buddy near machinery and heat/light cautions for epilepsy or diabetes profiles; the teacher operates a tool at the student's direction when manipulation isn't the outcome.
4. **Teacher notes:** which profile gets which version, check-in points, and a one-line NCCD evidence note.

### Mode B — Assessment adjustments (task, exam, test)
Inputs: the task, outcomes, rubric, need profiles and approved provisions, Stage 6 or not.
Output:
1. **Provisions checklist** (teacher-facing): *Profile | process (small group, rest breaks 5/30, extra time 2.5 or 5/30, reader, scribe, enlarged print, headphones, diabetic provisions) | activity (rephrased, simplified, chunked, visual prompts, glossary) | response format (point form, scaffolded, annotated sketches, oral or recorded, photo portfolio, demonstration) | who organises | done ✓*.
2. **Adjusted task sheet(s)** with the same marks and outcomes: a plain-language task statement, a staged planner with dated checkpoints and tick boxes, a submission checklist and scaffolds.
3. **Marking note:** how to mark alternative formats against the same criteria, using the school's A–E wording (extensive / thorough / sound / basic / elementary). Pass rubric work to `marking-rubric-builder`.
4. Stage 6: flag that HSC disability provisions are a separate NESA application.

### Mode C — Class / unit adjustment plan (one A4 desk reference)
Inputs: class, unit, term, need profiles.
Output: a header (class, unit, outcomes) → a table (*Profile | Key functional impact | Classroom | Practical/workshop | Assessment provisions*) → **whole-class QDTP moves** that cover most profiles (routine lesson start, visual step cards, a fortnight task sheet with tick boxes, instructions both written and spoken, success criteria up, seating plan) → **unit pinch-points** (machine demos, extended writing, group critique, noisy workshop) with the planned adjustment for each → check-in schedule and teacher-only reminders (time-out cards, medical plans). Hand NCCD level suggestions to `nccd-adjustments-evidence`.

### Mode D — Quick strategies
For a question like "how do I support an ASD + APD student in a sewing lesson?": 5–8 concrete moves in the school's wording, translated to the actual lesson, plus one thing to avoid.

## Design rules (Britt's style)
- Printed, visually designed worksheets that students handwrite on; minimal screen time.
- Sans-serif, 12pt minimum (14pt for supported), 1.5 spacing, left-aligned, white space, one idea per box.
- OpenDyslexic option for dyslexia; VI at the specified font and size (e.g. 26pt Verdana, A4); OCD profiles get no mixed fonts and minimal bold or underlining.
- Images sit beside the text they explain; icons for read / watch / make / write.

## Fallback library (only if the project is unavailable)
- **ADHD:** 5–10 minute chunks, instructions one at a time, check in after instructions, visual reminders, timers, movement, "stop, think, do", reduced written load.
- **ASD:** predictable routine, pre-warn changes, literal steps, specific choices, processing time, sensory supports, demonstrate don't explain, monitor groupings.
- **SLD reading:** Read & Write or audio, highlight key words, pre-teach vocabulary and give glossaries, never read aloud cold.
- **SLD writing / dysgraphia / DCD:** scaffolds, sentence starters, voice-to-text, no board copying, don't mark spelling or handwriting.
- **Dyscalculia:** worked solutions, calculator, uncluttered sheets, talk through the steps.
- **APD/DLD/speech:** written and visual versions of verbal instructions, slower talk, short sentences, wait time.
- **Hearing:** front seat, face the student, digital copies.
- **VI:** specified font, high contrast, slides in advance, blinds.
- **Anxiety/MH:** preview tasks, choice, no cold-calling, exit pass, affirm effort.
- **ODD:** must/should/could do, avoid power struggles, neutral private redirection.
- **Gifted/2E:** HPGE adjustments; scaffold the weakness; challenge in the strength (see `newman-gifted-differentiation`).
- **Medical:** teacher-only notes.

## Reference file

- `references/barriers-and-constructs.md` — identifying the construct before adjusting, a barrier → response → preserve table, equity checks for TAS tasks, practical-class access, and review questions. Use when the project sources don't cover a situation.
