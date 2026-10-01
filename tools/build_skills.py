#!/usr/bin/env python3
"""Build the Elements and Principles of Design skills from src/.

Edit these (the sources):
  src/elements/<element>.md      full knowledge for each element (12)
  src/principles/<name>/SKILL.md the principle skills Britt built in Claude (15), kept as written
  src/principle-examples/<p>.md  extra examples and teaching material added to each principle
  src/jobs/<job>.md              workflow templates for teaching, feedback, analysis and practice
  src/method/<part>.md           the shared method, split into six small files
  src/overview/                  the overview skill and its guides
  src/subjects/<name>/           subject skills (Multimedia, Textiles, D&T, Visual Arts), copied as is
  src/updated-skills/<name>/     Britt's existing teaching skills with merged reference files, copied as is

Generated (don't edit; rerun this script):
  .claude/skills/<name>/         one folder per skill, each with a lean SKILL.md and references/
  dist/                          .skill packages and all-skills-bundle.zip (with --package)

Every skill keeps its SKILL.md short and moves detail into references/ files that
Claude opens only when a task needs them, so everyday use stays cheap.

Usage:
  python3 tools/build_skills.py            # rebuild .claude/skills/
  python3 tools/build_skills.py --package  # rebuild and package into dist/
"""
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
SKILLS = ROOT / ".claude" / "skills"
DIST = ROOT / "dist"
JOBS = ["teaching", "feedback", "analysis", "practice"]
SUBJECTS, UPDATED = [], []

LANGUAGE_LINE = (
    "Follow `references/method/checks-and-language.md` for language: Australian English, "
    "describe before interpreting, conditional language for emotional or cultural associations, "
    "and name the criterion whenever something \"works\"."
)


# --------------------------------------------------------------------------- parsing helpers

def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("missing frontmatter")
    return m.group(1), m.group(2)


def sections(body):
    """Return (preamble, {heading: full section text}) in source order."""
    parts = re.split(r"\n(?=## )", body)
    pre, secs = parts[0], {}
    for p in parts[1:]:
        heading = p.split("\n", 1)[0][3:].strip()
        secs[heading] = p.rstrip() + "\n"
    return pre, secs


def find(secs, *needles, required=True):
    for h, s in secs.items():
        if all(n in h.lower() for n in needles):
            return s
    if required:
        raise KeyError(needles)
    return ""


def handoff_paragraphs(pre):
    """Preamble paragraphs that hand off to other skills."""
    keep = []
    for para in re.split(r"\n\s*\n", pre):
        low = para.lower()
        if "`" in para and ("skill" in low or "hand off" in low) and "design-method" not in para:
            keep.append(para.strip())
    return keep


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n")


def copy_method(skill_dir):
    for f in sorted((SRC / "method").glob("*.md")):
        write(skill_dir / "references" / "method" / f.name, f.read_text())


def pick_table(rows):
    out = ["| The request is… | Read |", "|---|---|"]
    out += [f"| {a} | {b} |" for a, b in rows]
    return "\n".join(out)


# --------------------------------------------------------------------------- elements

def build_element(src):
    slug = src.stem
    fm, body = split_frontmatter(src.read_text())
    title = re.search(r"^# (.+?) — element of design", body, re.M).group(1)
    e = title.lower()
    pre, secs = sections(body)
    d = SKILLS / f"{slug}-element-of-design"

    handoffs = handoff_paragraphs(pre)
    table = pick_table([
        ("A lesson, worksheet, Canvas page or activity", "`references/teaching.md`"),
        ("Feedback or marking on student work", "`references/feedback.md`"),
        ("Analysis, annotations or model answers", "`references/analysis.md`"),
        (f"Applying {e} in a design", "`references/practice.md`"),
        ("Types, links to other elements and principles, fields, production, misconceptions",
         "`references/knowledge.md`"),
        ("Whole-design feedback, justification writing, Factors Affecting Design",
         "the `elements-and-principles-of-design` skill"),
    ])
    skill = (
        f"---\n{fm}\n---\n\n# {title} — element of design\n\n"
        f"This skill covers {e} as an element of design. The essentials are below. Open **only** the "
        f"reference file the task needs; each one says which other files to consult.\n\n"
        + ("\n\n".join(handoffs) + "\n\n" if handoffs else "")
        + "## Pick the job\n\n" + table + "\n\n" + LANGUAGE_LINE + "\n\n"
        + find(secs, "what ") + "\n" + find(secs, "variables")
    )
    write(d / "SKILL.md", skill)

    knowledge = [find(secs, "types"), find(secs, "with the other elements"), find(secs, "principles"),
                 find(secs, "across fields"), find(secs, "production"), find(secs, "misconceptions")]
    write(d / "references" / "knowledge.md",
          f"# {title}: knowledge\n\nThe definition and variables are in `../SKILL.md`.\n\n" + "\n".join(knowledge))

    extra = {
        "teaching": [find(secs, "activity ideas")],
        "feedback": [find(secs, "feedback patterns"), find(secs, "justification examples")],
        "analysis": [find(secs, "worked analysis")],
        "practice": [],
    }
    for job in JOBS:
        tpl = (SRC / "jobs" / f"{job}.md").read_text().format(Title=title, element=e)
        write(d / "references" / f"{job}.md", tpl + "\n" + "\n".join(extra[job]))
    copy_method(d)
    return secs, title


# --------------------------------------------------------------------------- principles

def contributions(element_secs):
    """{principle: [(element title, text)]} from each element's principles section."""
    out = {}
    for title, secs in element_secs:
        for line in find(secs, "principles").splitlines():
            m = re.match(r"- \*\*(.+?):\*\* (.+)", line)
            if not m:
                continue
            for name in re.split(r",\s*|\s+and\s+", m.group(1).lower()):
                out.setdefault(name.strip(), []).append((title, m.group(2).strip()))
    return out


def build_principle(src, contrib):
    """Britt's Claude-built principle skill is the base and is kept as written.

    The extra material from src/principle-examples/ (worked analysis, justification
    examples, feedback patterns, activities, element contributions) goes into
    references/examples.md, with one pointer section added to SKILL.md.
    """
    name = src.parent.name
    p = name.removesuffix("-principle-of-design")
    base = src.read_text()
    ex = SRC / "principle-examples" / f"{p}.md"
    _, body = split_frontmatter(ex.read_text())
    title = re.search(r"^# (.+?) — principle of design", body, re.M).group(1)
    _, secs = sections(body)
    d = SKILLS / name

    pointer = (
        "## More on demand\n\n"
        f"`references/examples.md` has extra material on {p}: types and levers, a worked analysis, "
        "justification examples, feedback patterns to look for in student work, activity ideas, and what "
        "each element of design contributes. Open it only when the task needs it. For marks or a rubric, "
        "use `marking-rubric-builder`; with no rubric supplied, build criteria from the protocols above.\n\n"
    )
    marker = "For the full cross-Principle framework"
    base = base.replace(marker, pointer + marker, 1) if marker in base else base.rstrip() + "\n\n" + pointer
    write(d / "SKILL.md", base)

    items = contrib.get(p, [])
    contrib_sec = (
        "## What each element contributes\n\n"
        + ("\n".join(f"- **{t}:** {x}" for t, x in items) if items else "- (No element lists this principle yet.)")
        + "\n\nFor depth on an element, use its `<element>-element-of-design` skill.\n"
    )
    parts = [find(secs, "types"), find(secs, "levers"), find(secs, "misconceptions"),
             find(secs, "worked analysis"), find(secs, "justification"),
             find(secs, "feedback patterns"), find(secs, "activity ideas"), contrib_sec]
    write(d / "references" / "examples.md", f"# {title}: examples and teaching material\n\n" + "\n".join(parts))


# --------------------------------------------------------------------------- overview

def build_overview():
    d = SKILLS / "elements-and-principles-of-design"
    write(d / "SKILL.md", (SRC / "overview" / "SKILL.md").read_text())
    for f in sorted((SRC / "overview" / "references").glob("*.md")):
        write(d / "references" / f.name, f.read_text().lstrip())
    copy_method(d)


# --------------------------------------------------------------------------- whole-folder skills

def build_folders(kind):
    """Copy each src/<kind>/<name>/ folder (SKILL.md plus references/) as a skill."""
    names = []
    for d in sorted((SRC / kind).glob("*/SKILL.md")):
        d = d.parent
        for f in sorted(d.rglob("*")):
            if f.is_file():
                write(SKILLS / d.name / f.relative_to(d), f.read_text())
        names.append(d.name)
    return names


# --------------------------------------------------------------------------- checks and packaging

def check():
    problems, total_desc = [], 0
    for d in sorted(SKILLS.iterdir()):
        f = d / "SKILL.md"
        if not f.exists():
            continue
        fm, body = split_frontmatter(f.read_text())
        import yaml  # Claude.ai parses frontmatter as YAML, so check it the same way
        try:
            meta = yaml.safe_load(fm)
        except Exception as err:
            problems.append(f"{d.name}: invalid YAML frontmatter ({str(err).splitlines()[0]})")
            continue
        name, desc = str(meta.get("name", "")), " ".join(str(meta.get("description", "")).split())
        total_desc += len(desc)
        if name != d.name:
            problems.append(f"{d.name}: name '{name}' doesn't match folder")
        if len(desc) > 1024:
            problems.append(f"{d.name}: description {len(desc)} chars (max 1024)")
        if "<" in desc or ">" in desc:
            problems.append(f"{d.name}: description has angle brackets")
        for ref in re.findall(r"`(references/[^`]+\.md)`", body):
            if not (d / ref).exists():
                problems.append(f"{d.name}: missing {ref}")
    return problems, total_desc


def package():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    names = []
    for d in sorted(SKILLS.iterdir()):
        if not (d / "SKILL.md").exists():
            continue
        with zipfile.ZipFile(DIST / f"{d.name}.skill", "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(d.rglob("*")):
                if f.is_file():
                    z.write(f, f"{d.name}/{f.relative_to(d)}")
        names.append(d.name)

    def group(n):
        if n in SUBJECTS:
            return "4-subjects"
        if n in UPDATED:
            return "5-updated-teaching-skills"
        if n.endswith("-element-of-design"):
            return "2-elements"
        if n.endswith("-principle-of-design"):
            return "3-principles"
        return "1-start-here"
    with zipfile.ZipFile(DIST / "all-skills-bundle.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for n in names:
            z.write(DIST / f"{n}.skill", f"{group(n)}/{n}.skill")
    return len(names)


def main():
    if SKILLS.exists():
        shutil.rmtree(SKILLS)
    element_secs = [build_element(f) for f in sorted((SRC / "elements").glob("*.md"))]
    element_secs = [(t, s) for s, t in element_secs]
    contrib = contributions(element_secs)
    principles = sorted((SRC / "principles").glob("*/SKILL.md"))
    for f in principles:
        build_principle(f, contrib)
    build_overview()
    SUBJECTS.extend(build_folders("subjects"))
    UPDATED.extend(build_folders("updated-skills"))
    problems, total_desc = check()
    print(f"built: {len(element_secs)} elements, {len(principles)} principles, 1 overview, "
          f"{len(SUBJECTS)} subjects, {len(UPDATED)} updated teaching skills")
    print(f"always-on descriptions: {total_desc} characters (about {total_desc // 4} tokens)")
    for p in problems:
        print("PROBLEM:", p)
    if "--package" in sys.argv:
        if problems:
            sys.exit("not packaging: fix problems first")
        print(f"packaged: {package()} skills into dist/")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
