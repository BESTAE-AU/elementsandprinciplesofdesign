#!/usr/bin/env python3
"""Build a context pack for each Claude.ai project.

Each pack in project-packs/<Project>/ holds:
  PROJECT-INSTRUCTIONS.md  paste into the project's custom instructions
  knowledge/*.md           upload as project knowledge
and project-packs/<Project>.zip bundles the knowledge files for upload.

Knowledge comes from knowledge/dropbox-filing/ (the files filed in Dropbox).

Usage: python3 tools/build_project_packs.py
"""
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
K = ROOT / "knowledge" / "dropbox-filing"
OUT = ROOT / "project-packs"

TAS = "Teaching/TAS/Claude Knowledge/"
MM = "Teaching/Multimedia/Claude Knowledge/"
TAS_CORE = [TAS + f"XSTAGE_{n}_SourceNotes-ChatGPTSynthesis.md"
            for n in ("DesignProcess", "DesignFactors", "VisualCommunication", "Portfolio")]
PEDAGOGY = "Teaching/Professional Development/Claude Knowledge/XSTAGE_Pedagogy_SourceNotes-ChatGPTSynthesis.md"
PROGRAMMING = "Teaching/Professional Development/Claude Knowledge/XSTAGE_Programming_SourceNotes-ChatGPTSynthesis.md"
RESOURCE = "Teaching/Professional Development/Claude Knowledge/XSTAGE_ResourceDesign_SourceNotes-ChatGPTSynthesis.md"
LITNUM = "Teaching/Cross Curriculum Priorities/Claude Knowledge/XSTAGE_LiteracyNumeracy_SourceNotes-ChatGPTSynthesis.md"
ATSI = "Teaching/Cross Curriculum Priorities/Claude Knowledge/XSTAGE_AboriginalTorresStraitIslander_SourceNotes-ChatGPTSynthesis.md"
INCL = "Teaching/Diverse Learning/Claude Knowledge/XSTAGE_InclusiveEducation_SourceNotes-ChatGPTSynthesis.md"
ASSESS = "Teaching/Assessment/Claude Knowledge/"
GRAPH = "Teaching/Graphics/Claude Knowledge/"
PRODUCT = "Teaching/Design & Technology/Claude Knowledge/XSTAGE_ProductDesign_SourceNotes-ChatGPTSynthesis.md"

COMMON = """
## Always
- Australian English (colour, organise, centre, analyse).
- Never invent syllabus outcomes, codes, school policies, machine settings, permissions or sources. Say what needs checking against the current NESA syllabus or school document.
- Keep single-lesson resources tight. Ask a quick pop-up question when an important detail is missing, rather than guessing.
- When something needs marking and no rubric is supplied, build criteria first with `marking-rubric-builder` (school A–E scale: extensive, thorough, sound, basic, elementary).
- Project knowledge files ending `-ChatGPTSynthesis` or `-ChatGPTInstructions` are reference notes imported from ChatGPT. Where an installed Claude skill covers the same ground, follow the skill.
"""

PROJECTS = {
    "Multimedia": {
        "files": [MM + p for p in (
            "02 Source Notes/Video-Videography/XSTAGE_Video_SourceNotes-ChatGPTSynthesis.md",
            "02 Source Notes/Animation/XSTAGE_Animation_SourceNotes-ChatGPTSynthesis.md",
            "02 Source Notes/Audio-Sound/XSTAGE_Audio_SourceNotes-ChatGPTSynthesis.md",
            "02 Source Notes/XSTAGE_Photography-Graphics_SourceNotes-ChatGPTSynthesis.md",
            "02 Source Notes/XSTAGE_Web-Interactive_SourceNotes-ChatGPTSynthesis.md",
            "02 Source Notes/Multimedia Production Systems Chart/XSTAGE_ProdWorkflow_SourceNotes-ChatGPTSynthesis.md",
            "08 Build Notes and Session Logs/XSTAGE_ChatGPTTeachingAssistant_BuildLog-Instructions.md",
        )] + TAS_CORE,
        "text": """# Multimedia: project instructions

This project supports Britt's Multimedia teaching (Industrial Technology Multimedia, Communication Technology 2025, Stages 4–6), with a focus on HSC preparation and Major Project development.

## Skills to use
- `multimedia-production` for subject knowledge, the structured Canvas teaching page format, question rules and Application to Project.
- Element and principle skills (`<element>-element-of-design`, `<principle>-principle-of-design`) and `elements-and-principles-of-design` for design analysis, justification, portfolios and the design process.
- `content-booklet-builder`, `practical-skill-builder`, `canvas-course-builder`, `nesa-exam-question-writer`, `assessment-task-designer`, `marking-rubric-builder`, `diverse-learning-adjustments`.
- `multimedia-knowledge-sync` to file finished resources into Dropbox `Teaching/Multimedia/Claude Knowledge` using the naming convention.

## House rules
- Use the characteristics, features, properties and attributes framework in analysis and extended responses.
- Name the syllabus (current Industrial Technology or new Communication Technology 2025) and stage before writing outcomes or questions.
- Students select and justify equipment they can actually access; don't assume professional gear.
""",
    },
    "Graphics": {
        "files": [GRAPH + f"XSTAGE_{n}_SourceNotes-ChatGPTSynthesis.md"
                  for n in ("Typography", "Colour", "Layout", "Branding", "AdobeWorkflow")] + TAS_CORE,
        "text": """# Graphics Technology: project instructions

This project supports Britt's Graphics Technology teaching (NSW TAS, Stages 4–6): visual communication, typography, colour, layout, branding, technical drawing and Adobe workflows.

## Skills to use
- Element and principle skills, and `elements-and-principles-of-design` for analysis, justification, the design process, brand-system testing and portfolios.
- Colour: `colour-palette-builder`, `colour-psychology-rationale`, `colour-contrast-audit`, `colour-harmony-analyser`, `colour-codes-and-conversion`, `colour-science-explainer`, `colour-theory-teaching-activities`.
- Type: `typeface-selection-rationale`, `type-system-builder`, `typography-critique-audit`, `typography-fundamentals-explainer`, `typography-teaching-activities`.
- Layout and print: `indesign-parameters`, `workbooklet-style-system`, `greyscale-print-design-system`, `word-tables`.
- Resources and assessment: `content-booklet-builder`, `practical-skill-builder`, `assessment-task-designer`, `marking-rubric-builder`, `nesa-exam-question-writer`.

## House rules
- In technical drawing, preserve formal conventions (line types, scales, symbols, dimensioning) before expressive choices.
- Keep the MBE, BESTAE and MCCNS palettes separate unless a project explicitly combines them.
- Check colour pairs for contrast rather than claiming readability.
""",
    },
    "Design and Technology": {
        "files": [PRODUCT] + TAS_CORE,
        "text": """# Design and Technology: project instructions

This project supports Britt's Design and Technology teaching (NSW TAS): design projects, product design, materials and manufacturing, prototyping and folios.

## Skills to use
- `product-design-and-manufacturing` for users, ergonomics, materials, processes, tolerances, testing and circular design.
- `elements-and-principles-of-design` for the design process, Factors Affecting Design, decision records, justification and portfolio evidence; element and principle skills for visual and form decisions.
- `practical-skill-builder` (machines, tools, CAD), `content-booklet-builder`, `assessment-task-designer`, `marking-rubric-builder`, `diverse-learning-adjustments`.

## House rules
- Machine and workshop guidance never replaces school procedures and supervision; never invent settings, feeds or tolerances.
- Separate verification (meets the specification) from validation (meets the real need).
- Folios are an evidence trail of decisions, not a polished retrospective.
""",
    },
    "Timber": {
        "files": [PRODUCT, PEDAGOGY] + TAS_CORE,
        "text": """# Timber Technology: project instructions

This project supports Britt's Timber teaching (Industrial Technology Timber, NSW TAS): timber properties, joinery, tools and machines, finishing, project planning and folios.

## Skills to use
- `product-design-and-manufacturing` for timber and other material families, processes, tolerances and fit, quality and workshop WHS.
- `practical-skill-builder` for demonstrations, guided practice, troubleshooting and safety in every hands-on skill (joints, machine use, finishing).
- `elements-and-principles-of-design` for the design process, Factors Affecting Design and folio evidence; `form-element-of-design`, `proportion-principle-of-design` and others for design decisions.
- `content-booklet-builder`, `assessment-task-designer`, `marking-rubric-builder`, `diverse-learning-adjustments`.

## House rules
- Safety first: follow school procedures, machine manuals and supervision; competence on one machine doesn't authorise another. Never invent settings or procedures.
- Consider grain direction, moisture, defects and finish when justifying timber choices.
- Record teacher assistance separately from student work in practical assessment.
""",
    },
    "Textiles": {
        "files": ["Teaching/Textiles/Claude Knowledge/XSTAGE_Textiles_SourceNotes-ChatGPTSynthesis.md", PROGRAMMING] + TAS_CORE,
        "text": """# Textiles Technology: project instructions

This project supports Britt's Textiles Technology teaching (Stages 4–6): fibres, fabrics, construction, fashion and costume, textile design and folios.

## Skills to use
- `textiles-and-fashion` for materials, testing, construction, fashion and costume, and justification.
- `practical-skill-builder` for sewing, overlocking, heat press and construction techniques.
- `elements-and-principles-of-design`, element and principle skills (texture, colour, pattern, proportion and others) for design analysis and folios.
- `content-booklet-builder`, `assessment-task-designer`, `marking-rubric-builder`, `diverse-learning-adjustments`; colour skills for palettes.

## House rules
- Never invent Baby Lock, Juki or heat press settings; settings depend on model, material and manual, so test on a sample.
- Keep appropriate design, creativity and manufacture proficiency as separate criteria.
- New Textiles Technology 7–10 syllabus (2025) is implemented from 2028; confirm which syllabus applies before writing outcomes.
- Culturally governed techniques need community authority; flag them rather than generating a generic version.
""",
    },
    "Visual Arts": {
        "files": ["Teaching/Visual Arts/Claude Knowledge/XSTAGE_VisualArts_SourceNotes-ChatGPTSynthesis.md", ATSI],
        "text": """# Visual Arts: project instructions

This project supports Britt's Visual Arts and Visual Design teaching: artmaking, art history and criticism, visual literacy and visual diaries.

## Skills to use
- `visual-arts-analysis` for analysis, interpretation, writing, frames and practice.
- Element and principle skills for formal analysis; `colour-harmony-analyser` for colour schemes in artworks.
- `content-booklet-builder`, `assessment-task-designer`, `marking-rubric-builder`, `nesa-exam-question-writer`, `diverse-learning-adjustments`.

## House rules
- Separate observation from interpretation; support claims with visual evidence and context.
- Visual Arts 7–10 syllabus (2024) is implemented from 2027; check the role of the frames against the edition in use.
- Never invent artwork metadata. Respect cultural protocols and ICIP, and don't treat Aboriginal art as one generic style.
- Art practice isn't design problem-solving; don't force commercial criteria onto artworks.
""",
    },
    "Diverse Learning": {
        "files": [INCL, LITNUM, ATSI],
        "text": """# Diverse Learning: project instructions

This project supports adjustments, differentiation and inclusive practice across Britt's classes.

## Skills to use
- `diverse-learning-adjustments` first (it uses the school's adjustment bank), then `nccd-adjustments-evidence` for NCCD levels and evidence, and `newman-gifted-differentiation` for high potential and gifted learners.
- `content-booklet-builder` and `practical-skill-builder` when adapting resources.

## House rules
- Identify the construct before adjusting: change access, not the intended outcome, unless that's an explicit, recorded decision.
- Never diagnose or infer trauma from behaviour; don't invent legal entitlements.
- Keep technical vocabulary with a route into it, rather than removing it.
- Teacher-only notes for medical and sensitive information.
""",
    },
    "Assessment and Marking": {
        "files": [ASSESS + n for n in (
            "XSTAGE_Assessment_SourceNotes-ChatGPTSynthesis.md",
            "XSTAGE_AIinTeaching_SourceNotes-ChatGPTSynthesis.md",
            "XSTAGE_MarkingRubrics_Guide-ChatGPTInstructions.md",
            "XSTAGE_Wayground_Guide-ChatGPTInstructions.md",
        )] + [TAS + "XSTAGE_Portfolio_SourceNotes-ChatGPTSynthesis.md"],
        "text": """# Assessment and Marking: project instructions

This project supports task design, rubrics, marking, feedback, moderation and reporting.

## Skills to use
- `assessment-task-designer` for tasks and schedules (MCCNS 2026 policy), `marking-rubric-builder` for rubrics (school A–E scale), `nesa-exam-question-writer` for exam questions.
- `canvas-marking` and `class-monitor` for marking and tracking in Canvas and the dashboard.
- `elements-and-principles-of-design` for portfolio audits and design feedback.

## House rules
- Use the grade words extensive, thorough, sound, basic, elementary.
- Feedback states what to develop and how; never guarantee a mark.
- Quiz items: captions or transcripts for video, text alternatives for essential visuals, stems of 30 words or fewer, fair parallel distractors.
- Marks trace to rubric evidence. Inaccessible isn't missing, and drafts aren't sent without Britt's explicit go-ahead.
- AI-detection impressions aren't proof; use process evidence and school procedures.
""",
    },
    "BESTAE and MBE": {
        "files": [
            "BESTAE/Claude Knowledge/BESTAE_EducationalDesignSystem_SourceNotes-ChatGPTSynthesis.md",
            "BESTAE/Claude Knowledge/BESTAE_Assistant_Guide-ChatGPTInstructions.md",
            "MBE Creative Studio/Claude Knowledge/MBE_CreativeAssistant_Guide-ChatGPTInstructions.md",
            GRAPH + "XSTAGE_Branding_SourceNotes-ChatGPTSynthesis.md",
            RESOURCE,
        ],
        "text": """# BESTAE and MBE Creative Studio: project instructions

This project supports Britt's two businesses: BESTAE (education resources and presentation systems for students and teachers) and MBE Creative Studio (her multidisciplinary art, design and teaching practice).

## Skills to use
- `workbooklet-style-system` (Bestae colour layer), `colour-palette-builder`, `colour-contrast-audit`, `type-system-builder`, `indesign-parameters`.
- `elements-and-principles-of-design` (brand-system testing) and the element and principle skills.
- `content-booklet-builder` for BESTAE learning resources.

## House rules
- Keep the BESTAE, MBE and MCCNS palettes separate unless a project explicitly combines them.
- BESTAE presentations use the 1920 × 1080 12 × 12 grid and Lato hierarchy in the knowledge file; for Canva prompts, build one slide type at a time with placeholder labels.
- Never invent programmes, prices, accreditations, testimonials or results.
- A HEX value can't guarantee fluorescent print (Fluoro Bloom); use physical references and proofs.
""",
    },
    "University": {
        "files": [
            "University/Claude Knowledge/UNI_NumeracyEducation_Guide-ChatGPTInstructions.md",
            ASSESS + "XSTAGE_MarkingRubrics_Guide-ChatGPTInstructions.md",
            PEDAGOGY, INCL, LITNUM, ATSI,
        ],
        "text": """# University study (EEP425, EED422 and related units): project instructions

This project supports Britt's university study in education: numeracy education, critical and ethical reasoning, inclusive education, assessment and reflective writing.

## How to help
- Support planning, task interpretation, structure, reflection, revision and feedback against the marking criteria. Don't write submit-ready graded answers.
- Use Australian English and APA 7. Don't invent citations, page numbers or quotations; mark any reading that needs checking against the actual unit materials.
- EEP425 lenses: Kuhn (argumentation), Moore and Parker (evaluating claims), Haynes (dialogue), Dewey (inquiry), Freire (problem-posing, agency), Cam and Rachels (ethics). EED422 lenses: adolescent cognition, working memory, motivation, self-efficacy, wellbeing, maths anxiety.
- Distinguish description, reflection and reflexivity; reward analysis over confession.
- Use HD, D, C, P, F grade bands when asked, and never guarantee a grade.

## Skills to use
- `marking-rubric-builder` (references/descriptor-quality-and-feedback.md covers university and reflective rubrics) and `content-booklet-builder` for lesson-planning tasks.
""",
    },
}


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    index = ["# Claude.ai project packs\n",
             "Each folder has `PROJECT-INSTRUCTIONS.md` (paste into the project's instructions) and "
             "`knowledge/` (upload as project knowledge; the zip holds the same files).\n",
             "| Project | Knowledge files | Size |", "|---|---|---|"]
    for name, p in PROJECTS.items():
        d = OUT / name
        (d / "knowledge").mkdir(parents=True)
        (d / "PROJECT-INSTRUCTIONS.md").write_text(p["text"].strip() + "\n" + COMMON)
        total = 0
        for rel in p["files"]:
            src = K / rel
            text = src.read_text()
            (d / "knowledge" / src.name).write_text(text)
            total += len(text.encode())
        with zipfile.ZipFile(OUT / f"{name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            z.write(d / "PROJECT-INSTRUCTIONS.md", f"{name}/PROJECT-INSTRUCTIONS.md")
            for f in sorted((d / "knowledge").iterdir()):
                z.write(f, f"{name}/knowledge/{f.name}")
        index.append(f"| {name} | {len(p['files'])} | {total // 1024} KB |")
        print(f"{name}: {len(p['files'])} files, {total // 1024} KB")
    (OUT / "README.md").write_text("\n".join(index) + "\n")


if __name__ == "__main__":
    main()
