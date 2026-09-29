#!/usr/bin/env python3
"""Build the Elements and Principles of Design skill suite.

Hand-written sources (edit these):
  shared/design-method.md                              shared method, copied into every skill
  .claude/skills/<element>-element-of-design/SKILL.md  element knowledge (12)
  .claude/skills/<principle>-principle-of-design/      principles (15); auto block filled in
  .claude/skills/<method skill>/SKILL.md               cross-element method skills (7)
  .claude/skills/elements-and-principles-of-design/    overview skill; auto block filled in

Generated (don't edit by hand; rerun this script instead):
  .claude/skills/<element>-element-of-design-{teaching,feedback,analysis,practice}/  (48)
  references/design-method.md in every skill
  references/element-knowledge.md in every job skill
  the auto blocks in the principle and overview skills
  dist/<skill>.skill packages (with --package)

Usage:
  python3 tools/build_skills.py            # regenerate skills
  python3 tools/build_skills.py --package  # regenerate and package into dist/
"""
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".claude" / "skills"
SHARED_METHOD = ROOT / "shared" / "design-method.md"
DIST = ROOT / "dist"

JOBS = ["teaching", "feedback", "analysis", "practice"]

# Short, element-specific trigger phrases used in the generated job descriptions.
KEYWORDS = {
    "line": '"leading lines", "stroke weight", "outlines" or "the lines in my logo"',
    "direction": '"eye flow", "reading path", "where does the eye go" or "screen direction"',
    "shape": '"negative space", "silhouette", "icon style" or "rounded corners"',
    "form": '"3D", "volume", "shading to look 3D", "drape" or "the shape of the product"',
    "space": '"white space", "cluttered", "breathing room", "padding" or "clear space"',
    "size-and-scale": '"make it bigger", "minimum logo size", "favicon" or "scale drawing"',
    "time-and-duration": '"pacing", "too fast", "how long should the title stay up" or "easing"',
    "value": '"tone", "shading", "contrast", "greyscale test" or "it looks flat"',
    "colour": '"colour scheme", "brand colours", "my colours clash" or "colour grading"',
    "texture": '"surface finish", "grain overlay", "tactile", "embossing" or "fabric feel"',
    "typography": '"fonts", "hierarchy of text", "kerning", "legibility" or "captions"',
    "layout-and-composition": '"it looks messy", "grid", "balance", "hierarchy" or "rule of thirds"',
}

JOB_TITLES = {
    "teaching": "teaching resources",
    "feedback": "feedback and marking",
    "analysis": "analysis and model answers",
    "practice": "applying it in a design",
}


def job_description(slug, e):
    kw = KEYWORDS[slug]
    return {
        "teaching": (
            f"Plans and writes teaching resources on {e.upper()} as an element of design for NSW TAS "
            f"and design subjects (Multimedia, Graphics Technology, Visual Design, Textiles, D&T): "
            f"single lessons, printable worksheets, Canvas pages, starters, experiments, homework, "
            f"support/core/extension differentiation and answer keys. Sequences learning from "
            f"recognition to analysis, a controlled one-variable experiment and justification, and "
            f"keeps single-lesson resources tight. Use it whenever someone asks for a lesson, "
            f"worksheet, activity or Canvas page on {e}, even if they only mention {kw}. For a full "
            f"workbooklet use content-booklet-builder; for rubrics use marking-rubric-builder."
        ),
        "feedback": (
            f"Gives feedback on, and marks, how a student has used {e.upper()} as an element of design "
            f"in folio justifications, annotations, posters, logos, products, garments, videos or "
            f"screens. Quotes the student, names the {e} variable involved, challenges universal "
            f"claims and preference used as a reason, checks reproduction and accessibility, and "
            f"gives one or two concrete next steps. Marks against the supplied rubric, or uses "
            f"marking-rubric-builder to create criteria when none is given. Use it whenever a "
            f"teacher shares student work or a justification and wants feedback, a mark or 'what "
            f"gets them to the top band' on {e}, even if they only mention {kw}."
        ),
        "analysis": (
            f"Writes analyses, annotations and model answers about {e.upper()} as an element of "
            f"design: identify, describe, explain, analyse and evaluate how {e} is used in a poster, "
            f"photo, film, logo, product, garment, interface or space, and levelled exemplars "
            f"(developing, sound, high-range) with notes on what lifts each to the next level. Use "
            f"it whenever someone wants a model answer, exemplar, sample response, HSC-style short "
            f"answer, annotation or analysis of {e} in a specific design, even if they only mention "
            f"{kw}."
        ),
        "practice": (
            f"Helps apply {e.upper()} as an element of design in a real project, whether the "
            f"user's own or a student's brand, poster, product, garment, video, interface or space. "
            f"It chooses and tests {e} variables one at a time, checks production and reproduction "
            f"limits, tests brand decisions across touchpoints, and writes up the final decision "
            f"with evidence, alternatives and trade-offs. Use it whenever someone is designing "
            f"something and asks how to handle {e}, what to change or how to justify it, even if "
            f"they only mention {kw}."
        ),
    }


# --------------------------------------------------------------------------- helpers

def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("missing frontmatter")
    return m.group(1), m.group(2)


def folded(desc):
    """Render a description as a YAML folded block wrapped at ~80 columns."""
    words, lines, cur = desc.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > 80:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    lines.append(cur)
    return ">\n" + "\n".join("  " + l for l in lines)


def sections(body):
    """Return (preamble, {heading: full section text}) preserving order."""
    parts = re.split(r"\n(?=## )", body)
    pre, secs = parts[0], {}
    for p in parts[1:]:
        heading = p.split("\n", 1)[0][3:].strip()
        secs[heading] = p.rstrip() + "\n"
    return pre, secs


def find(secs, *needles):
    for h, s in secs.items():
        hl = h.lower()
        if all(n in hl for n in needles):
            return s
    raise KeyError(needles)


def related_paragraphs(pre):
    """Paragraphs in an element preamble that hand off to specialist skills."""
    keep = []
    for para in re.split(r"\n\s*\n", pre):
        if "`" in para and "skill" in para.lower() and "design-method" not in para:
            keep.append(para.strip())
    return keep


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


# --------------------------------------------------------------------------- element job skills

def element_skills():
    return sorted(p for p in SKILLS.glob("*-element-of-design") if p.is_dir())


def build_job_skills():
    count = 0
    for edir in element_skills():
        slug = edir.name[: -len("-element-of-design")]
        text = (edir / "SKILL.md").read_text()
        _, body = split_frontmatter(text)
        title = re.search(r"^# (.+?) — element of design", body, re.M).group(1)
        e = title.lower()
        pre, secs = sections(body)
        knowledge_secs = [s for h, s in secs.items() if not h.lower().startswith("pick the job")]
        knowledge = (
            f"# {title}: element knowledge\n\n"
            f"Generated from `{edir.name}/SKILL.md` by `tools/build_skills.py`. Edit the element "
            f"skill, not this file.\n\n" + "\n".join(knowledge_secs)
        )
        handoffs = related_paragraphs(pre)
        descs = job_description(slug, e)
        for job in JOBS:
            name = f"{edir.name}-{job}"
            jdir = SKILLS / name
            if jdir.exists():
                shutil.rmtree(jdir)
            write(jdir / "references" / "element-knowledge.md", knowledge)
            siblings = ", ".join(f"`{edir.name}-{j}`" for j in JOBS if j != job)
            head = (
                f"---\nname: {name}\ndescription: {folded(descs[job])}\n---\n\n"
                f"# {title}: {JOB_TITLES[job]}\n\n"
                f"This skill handles **{JOB_TITLES[job]}** for {e} as an element of design. "
                f"Everything known about {e} (definition, variables, types, relationships with the "
                f"other elements and the principles, fields, production, misconceptions and worked "
                f"examples) is in `references/element-knowledge.md`. The shared method is in "
                f"`references/design-method.md`. Read the sections the workflow points to.\n\n"
                f"Related skills: {siblings}; `{edir.name}` for general questions about {e}; the "
                f"`*-principle-of-design` skills for principles.\n"
            )
            if handoffs:
                head += "\n" + "\n\n".join(handoffs) + "\n"
            head += (
                "\nApply the language rules in `references/design-method.md` §14: Australian "
                "English, describe before interpreting, conditional language for emotional or "
                "cultural associations, and name the criterion whenever something \"works\".\n\n"
            )
            write(jdir / "SKILL.md", head + JOB_BODIES[job](e, secs))
            count += 1
    return count


def teaching_body(e, secs):
    return f"""## Workflow

1. **Pin down the context.** Stage or year, subject, lesson length, print or Canvas, and any students on learning support plans. If something isn't given, pick a sensible default and state it at the top.
2. **Sequence the learning** (method §10): knowledge → recognition → description → analysis → controlled experiment → application → justification → evaluation. Don't jump from a definition to "design your own".
3. **Keep it tight.** A single lesson should fit its time with no padding. Use one short modelled example and one stimulus to analyse, adding a non-example only when the comparison is the point. Cut anything a student won't write on or a teacher won't use. The answer key can be more generous than the student pages.
4. **Choose the experiment.** Pick one variable from the Variables table in `element-knowledge.md`, make three clearly different versions and hold everything else constant (method §7). Test at real size or in the real medium.
5. **Build in the misconceptions** below as quick checks, such as true/false items, example vs non-example, or "what's wrong with this statement?".
6. **Differentiate** with support, core and extension (method §11): word bank, sentence starters and partly completed tables for support; competing constraints for extension. Keep the concept accurate at every level.
7. **Write the answer key** with model answers at two levels, following the justification ladder in `element-knowledge.md`.
8. **Check** against method §15. Hand off full workbooklets to `content-booklet-builder`, hands-on technique to `practical-skill-builder`, rubrics to `marking-rubric-builder` and print layout to `workbooklet-style-system`, when those skills are available.

{find(secs, "types")}
{find(secs, "misconceptions")}
{find(secs, "activity ideas")}"""


def feedback_body(e, secs):
    return f"""## Workflow

1. **Read the work against its brief.** Note the audience, purpose and every touchpoint or output named, such as cups, embroidery, a phone screen or signage. Reproduction problems usually hide there.
2. **Start from what the student actually did.** Quote their words or point to the part of the design, and name the {e} variable involved (see Variables in `element-knowledge.md`).
3. **Check for the patterns below** and for the misconceptions in `element-knowledge.md`.
4. **Check production and accessibility.** Use the Production and reproduction table in `element-knowledge.md` and method §13.
5. **Place the reasoning on the justification ladder** (weak → developing → strong → sophisticated; method §4). Say what link in the chain is missing.
6. **If marking:** use the rubric supplied. If none is supplied, use `marking-rubric-builder` (if available) to generate NESA-aligned criteria first, then mark against them and say they were generated. Without that skill, give feedback without a grade (method §12).
7. **Write it up:**
   - **What's working:** specific, not generic praise.
   - **What's holding it back:** 2–4 points, each quoting the student.
   - **Next steps:** one or two, phrased as a test or a design decision, in priority order.
   - **Model structure** (optional): a fill-in-the-blanks version of a top-level justification, with a note not to copy the numbers.
   - **Teacher notes:** current level, the gap to the top, and a conferencing question.

Keep the tone warm, honest and specific.

{find(secs, "feedback patterns")}
{find(secs, "justification examples")}
{find(secs, "misconceptions")}"""


def analysis_body(e, secs):
    return f"""## Workflow

1. **Fix the artefact.** If the user gives an image or description, work from it. If you're inventing one (for an exemplar), describe it briefly first so students can picture it, with the specific {e} characteristics the answers will cite.
2. **Work through the progression** (method §2): identify → describe → explain → analyse (connect to communication, purpose, audience) → evaluate against a named criterion, including a limitation or trade-off.
3. **For levelled exemplars** (e.g. developing / sound / high-range), make each level add a link in the reasoning chain, not just more words. Respect any word limits. Under each, add a short note on what lifts it to the next level.
4. **Analyse relationships.** Use the relationships with other elements and principles below to go beyond the element on its own.
5. **Language:** conditional wording for emotional or cultural readings, observation before interpretation, and no "it works" without a criterion.

{find(secs, "worked analysis")}
{find(secs, "justification examples")}
{find(secs, "with the other elements")}
{find(secs, "principles")}"""


def practice_body(e, secs):
    return f"""## Workflow

1. **Clarify the brief.** Get the audience, purpose, every output or touchpoint, the production methods and any fixed constraints (brand rules, budget, equipment).
2. **Name the design question** before changing anything, e.g. "which weight keeps the mark readable at 16 px and in embroidery?". Don't vary things at random (method §7).
3. **Pick one variable** from the table below and propose three clearly different options. Hold the rest constant.
4. **Test in real conditions:** real size, real medium, real viewing distance or device. Check the production table below.
5. **If it's a brand,** extend the surviving options to at least three touchpoints and record what breaks away from the logo (method §8).
6. **Decide and record** the result as a rule (e.g. minimum sizes, permitted variants) and as a sophisticated justification: evidence → alternative rejected → trade-off accepted (method §4).

{find(secs, "variables")}
{find(secs, "production")}
{find(secs, "across fields")}"""


JOB_BODIES = {
    "teaching": teaching_body,
    "feedback": feedback_body,
    "analysis": analysis_body,
    "practice": practice_body,
}


# --------------------------------------------------------------------------- auto blocks

def replace_block(path, marker, content):
    text = path.read_text()
    pat = re.compile(rf"(<!-- BEGIN: {marker} -->\n).*?(<!-- END: {marker} -->)", re.S)
    if not pat.search(text):
        raise ValueError(f"{path} has no {marker} block")
    path.write_text(pat.sub(lambda m: m.group(1) + content + m.group(2), text))


def principle_contributions():
    """{principle: [(element title, text)]} parsed from each element's principles section."""
    out = {}
    for edir in element_skills():
        _, body = split_frontmatter((edir / "SKILL.md").read_text())
        title = re.search(r"^# (.+?) — element of design", body, re.M).group(1)
        _, secs = sections(body)
        for line in find(secs, "principles").splitlines():
            m = re.match(r"- \*\*(.+?):\*\* (.+)", line)
            if not m:
                continue
            for name in re.split(r",\s*|\s+and\s+", m.group(1).lower()):
                out.setdefault(name.strip(), []).append((title, m.group(2).strip()))
    return out


def fill_principles():
    contrib = principle_contributions()
    n = 0
    for pdir in sorted(SKILLS.glob("*-principle-of-design")):
        p = pdir.name[: -len("-principle-of-design")].replace("-", " ")
        items = contrib.get(p, [])
        body = (
            "Generated from the element skills by `tools/build_skills.py`. For more on any "
            "element, use its `<element>-element-of-design` skill.\n\n"
        )
        body += "\n".join(f"- **{t}:** {txt}" for t, txt in items) if items else "- (No element skill lists this principle yet.)"
        replace_block(pdir / "SKILL.md", "element-contributions", body + "\n")
        n += 1
    return n


def fill_overview():
    path = SKILLS / "elements-and-principles-of-design" / "SKILL.md"
    if not path.exists():
        return
    rows = {"Element skills": [], "Element job skills": [], "Principle skills": [], "Method skills": []}
    for d in sorted(SKILLS.iterdir()):
        if not (d / "SKILL.md").exists() or d.name == "elements-and-principles-of-design":
            continue
        if d.name.endswith("-element-of-design"):
            rows["Element skills"].append(d.name)
        elif "-element-of-design-" in d.name:
            continue  # summarised per element below
        elif d.name.endswith("-principle-of-design"):
            rows["Principle skills"].append(d.name)
        else:
            rows["Method skills"].append(d.name)
    out = "Generated by `tools/build_skills.py`.\n\n"
    out += "**Element skills** (general knowledge), each with four job skills: `<element>-element-of-design-teaching`, `-feedback`, `-analysis` and `-practice`:\n\n"
    out += "\n".join(f"- `{n}`" for n in rows["Element skills"]) + "\n\n"
    out += "**Principle skills:**\n\n" + "\n".join(f"- `{n}`" for n in rows["Principle skills"]) + "\n\n"
    out += "**Method skills** (work for any element or principle):\n\n" + "\n".join(f"- `{n}`" for n in rows["Method skills"]) + "\n"
    replace_block(path, "skill-index", out)


# --------------------------------------------------------------------------- method copy, checks, packaging

def copy_method():
    n = 0
    for d in SKILLS.iterdir():
        if (d / "SKILL.md").exists():
            write(d / "references" / "design-method.md", SHARED_METHOD.read_text())
            n += 1
    return n


def check():
    problems = []
    for d in sorted(SKILLS.iterdir()):
        f = d / "SKILL.md"
        if not f.exists():
            continue
        fm, _ = split_frontmatter(f.read_text())
        name = re.search(r"^name:\s*(\S+)", fm, re.M).group(1)
        desc = " ".join(fm.split("description:", 1)[1].replace(">", "", 1).split())
        if name != d.name:
            problems.append(f"{d.name}: name '{name}' doesn't match folder")
        if len(desc) > 1024:
            problems.append(f"{d.name}: description {len(desc)} chars (max 1024)")
        if "<" in desc:
            problems.append(f"{d.name}: description contains '<'")
    return problems


def package():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    n = 0
    for d in sorted(SKILLS.iterdir()):
        if not (d / "SKILL.md").exists():
            continue
        with zipfile.ZipFile(DIST / f"{d.name}.skill", "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(d.rglob("*")):
                if f.is_file():
                    z.write(f, f"{d.name}/{f.relative_to(d)}")
        n += 1
    # One bundle of every .skill file, grouped by kind, for easy download.
    def kind(name):
        if name.endswith("-element-of-design"):
            return "1-element-skills"
        if "-element-of-design-" in name:
            return "2-element-job-skills/" + name.split("-element-of-design-")[0]
        if name.endswith("-principle-of-design"):
            return "3-principle-skills"
        if name == "elements-and-principles-of-design":
            return "0-start-here"
        return "4-method-skills"
    with zipfile.ZipFile(DIST / "all-skills-bundle.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(DIST.glob("*.skill")):
            z.write(f, f"{kind(f.stem)}/{f.name}")
    return n


def main():
    jobs = build_job_skills()
    principles = fill_principles()
    fill_overview()
    copied = copy_method()
    problems = check()
    print(f"job skills: {jobs}, principles filled: {principles}, method copied into: {copied}")
    for p in problems:
        print("PROBLEM:", p)
    if "--package" in sys.argv:
        if problems:
            sys.exit("not packaging: fix problems first")
        print(f"packaged: {package()} skills into dist/")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
