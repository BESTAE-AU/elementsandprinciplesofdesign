#!/usr/bin/env python3
"""Build one standalone skill per Principle of Design.

Each skill is written to skills/<name>-principle-of-design/SKILL.md and is assembled from the
shared content in principles-of-design/references/, so edits made there flow through when this
script is re-run:

    python3 tools/build_principle_skills.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "principles-of-design" / "references"
OUT = ROOT / "skills"

# name -> trigger phrases added to the description (what people say when they need this Principle)
PRINCIPLES = {
    "unity": "a design feeling coherent or fragmented, visual consistency, brand systems holding together, or things that 'don't belong together'",
    "harmony": "whether colours, typefaces, materials or components go together, visual compatibility, mood coherence, or something that 'clashes'",
    "balance": "visual weight, symmetry, asymmetry, radial or dynamic balance, a layout feeling lopsided, heavy or unstable",
    "alignment": "grids, edges, centring, baselines, optical alignment, text or elements 'not lining up', or deliberate misalignment",
    "proximity": "spacing between elements, grouping related content, whitespace, labels and fields, or layouts that feel crowded or disconnected",
    "proportion": "size relationships between parts, proportion vs scale, ratios, the golden ratio, silhouette divisions, or ergonomics and human scale",
    "hierarchy": "levels of importance, reading order, type hierarchy, what the viewer sees first, calls to action, or 'everything competes'",
    "emphasis": "focal points, making something stand out, dominance, isolation, calls to action, or a design with no clear focus",
    "contrast": "differences in value, colour, scale, type, texture or motion, legibility and luminance contrast, or a design that feels flat",
    "repetition": "recurring shapes, colours, type, components or motion, consistency, brand recognition, or monotony",
    "pattern": "repeat designs, motifs, textile prints, tessellations, surface pattern, façade modules, or organised recurrence",
    "rhythm": "visual or temporal cadence, interval and spacing, editing and animation timing, pacing, or flow in a layout",
    "movement": "how the eye travels, implied or actual motion, directional cues, scan paths, camera movement, animation, or reduced-motion",
    "tension": "instability, edge pressure, near-collision, cropping, opposition, drama, urgency, or deliberate disruption",
    "variety": "introducing difference, avoiding monotony, controlled variation within a brand or UI system, or designs that feel chaotic",
}


def title(name):
    return name.capitalize()


def mentions(text, name):
    return re.search(rf"\b{name}\b", text, re.IGNORECASE) is not None


def principle_body(name):
    lines = (REF / "principles" / f"{name}.md").read_text().split("\n")[1:]  # drop '# Name'
    out = []
    for ln in lines:
        if ln.startswith("#"):
            ln = "#" + ln
        out.append(ln)
    return "\n".join(out).strip()


def distinctions(name):
    rows = [ln for ln in (REF / "relationships.md").read_text().split("\n")
            if ln.startswith("| ") and " vs " in ln and mentions(ln.split("|")[1], name)]
    if not rows:
        return ""
    return "| Relationship | Distinction |\n|---|---|\n" + "\n".join(rows)


def bullets(text):
    """Yield top-level bullet items, joining wrapped continuation lines."""
    item = None
    for ln in text.split("\n"):
        if ln.startswith("- "):
            if item:
                yield item
            item = ln[2:].strip()
        elif item and ln.startswith("  ") and ln.strip():
            item += " " + ln.strip()
        else:
            if item:
                yield item
            item = None
    if item:
        yield item


def causal(name):
    text = (REF / "causal-reasoning.md").read_text()
    items = [b for b in bullets(text) if "→" in b or "↔" in b or b.startswith("**")]
    return "\n".join(f"- {b}" for b in items if mentions(b, name))


def section_after(path, heading, level):
    """Text under a heading of the given level, up to the next heading of that level or higher."""
    lines = path.read_text().split("\n")
    out, grab = [], False
    for ln in lines:
        m = re.match(r"^(#+) (.*)", ln)
        if m and grab and len(m.group(1)) <= level:
            break
        if grab:
            out.append(ln)
        if m and len(m.group(1)) == level and m.group(2).strip().lower() == heading.lower():
            grab = True
    return "\n".join(out).strip()


def experiment(name):
    return section_after(REF / "experimentation.md", title(name), 3)


def exemplar(name):
    path = REF / "analysis-justification-feedback.md"
    if name == "contrast":
        parts = [f"**{lvl}:** " + section_after(path, lvl, 3).lstrip("> ").split("\n")[0]
                 for lvl in ("Weak", "Developing", "Strong", "Sophisticated")]
        return "\n\n".join(parts)
    return section_after(path, f"{title(name)} example", 4)


def failure_degrees(name):
    return section_after(REF / "teaching-resources.md", title(name), 4)


def build(name, triggers):
    t = title(name)
    desc = (
        f"Design-reasoning skill for {t}, one of the 15 Principles of Design. Use it to teach, "
        f"explain, analyse, critique, generate, justify, evaluate or refine {t.lower()} in graphic "
        f"design, branding, multimedia, UI/UX, textiles, product, spatial design and architecture. "
        f"Use whenever someone asks what {t.lower()} is, how to create or fix it, or wants feedback, "
        f"a justification, a lesson or questions about it, including talk of {triggers}."
    )
    assert len(desc) <= 1024, (name, len(desc))

    sections = [f"""---
name: {name}-principle-of-design
description: >
  {desc}
---

# {t} — Principle of Design

Treat {t} as a **relational, organisational concept**: it describes how Elements of Design are
organised and perceived in relation to each other, not a physical object in the design. Explain
*how* specific Element variables create {t.lower()}, what effect that has, and whether the effect
suits the audience, purpose and context. Write in **Australian English**.

## How to reason about {t}

**Elements of Design** (the variables manipulated): line, direction, shape, form, space, size and
scale, time and duration, value, colour, texture, typography, layout and composition. Name the
specific variable (e.g. "type weight", "interval between modules"), not just the category.

**Causal model:** Elements manipulated → primary Principle → secondary Principle(s) → perceptual
effect → communication / functional outcome → suitability for audience, purpose and context.

- Identify whether {t.lower()} is the **primary** Principle (most directly created by the decision)
  or a **secondary** effect of another Principle.
- Treat causal links as conditional, not automatic, and don't force a chain the evidence doesn't
  support. Separate cause from correlation.
- Use hedged, mechanism-based language ("tends to", "may be perceived as", "can direct attention"):
  perception varies with culture, reading direction, medium, device, viewing distance and
  accessibility needs.
- Surface trade-offs (possible advantage ↔ possible disadvantage) and treat failure as a matter of
  degree: absent, weak, inconsistent, excessive, inappropriate or deliberately disrupted.
- Recognise deliberate rule-breaking: ask what effect the decision creates and whether it suits the
  purpose, not whether a rule was followed.
- Keep accessibility and production conditions (print, screen, responsive, textile repeat,
  manufacturing, frame rate) in view throughout.

## Knowledge: {t}

{principle_body(name)}"""]

    d = distinctions(name)
    if d:
        sections.append(f"## Distinguishing {t} from related concepts\n\n{d}")

    c = causal(name)
    if c:
        sections.append(
            f"## Causal chains and interactions involving {t}\n\n"
            f"Use these as possible relationships to test against the evidence in the design, "
            f"not as universal laws.\n\n{c}")

    f = failure_degrees(name)
    if f:
        sections.append(f"## Degrees of {t.lower()}\n\n{f}")

    e = exemplar(name)
    if e:
        sections.append(
            f"## Weak → sophisticated responses\n\nHelp learners move beyond naming the "
            f"Principle.\n\n{e}")
    else:
        sections.append(
            f"## Weak → sophisticated responses\n\nWhen scaffolding, generate a progression for "
            f"{t.lower()}: **weak** (names the Principle), **developing** (describes a visible "
            f"feature), **strong** (links specific Element variables to the Principle), "
            f"**sophisticated** (explains the causal chain to a communication or functional "
            f"outcome for the audience and context).")

    x = experiment(name)
    sections.append(f"""## Working protocols

### Analysing
Identify where {t.lower()} is evident → describe the Elements and relationships creating it →
explain the perceptual/functional effect → analyse how decisions combine and whether {t.lower()}
is primary or secondary → connect to communication, purpose, audience and context → evaluate
against explicit criteria → propose a refinement.

### Critiquing / feedback
State the intended outcome, the observable evidence, the Elements manipulated, the effect on
{t.lower()} and on communication or function, a trade-off where relevant, then a **specific**
change and the effect it should produce, and how to test it. Avoid vague advice like "improve the
{t.lower()}".

### Justifying a design decision
Design decision → Elements manipulated → primary Principle → secondary Principle(s) where relevant
→ perceptual/functional effect → communication outcome → purpose → audience/context →
suitability. For sophisticated work add evidence/research, an alternative considered, the trade-off
and an evaluation.

### Generating a concept or brief
Specify the intended outcome, how {t.lower()} will be created (which Elements and relationships),
related Principles, accessibility requirements, implementation constraints, system rules,
acceptable variation, trade-offs and testing criteria.

### Refining
Problem observed → evidence → variable changed → expected effect on {t.lower()} → expected
communication/function effect → test (at the intended size, medium or device). Change one
significant variable at a time where practical.

### Experimenting
{x if x else f"Create controlled variations that change how strongly {t.lower()} is expressed."}
Record: variable changed | variation | effect on {t.lower()} | secondary Principle | communication
effect | suitability | refinement.

### Teaching
Move learners through knowledge → recognition → description → explanation → analysis →
experimentation → application → justification → evaluation → refinement. Use non-leading
questions ("What effect does the level of {t.lower()} have?", not "How does the strong
{t.lower()} make it exciting?").

## Language

Prefer: establishes, contributes to, reinforces, disrupts, differentiates, groups, separates,
directs, emphasises, balances, creates cohesion, guides attention, may be perceived as, is
appropriate because. Avoid unsupported verdicts ("looks good", "is professional", "is boring",
"always works") unless criteria and context support them.

## Quality check

- {t} treated as a relationship, with the specific Element variables named.
- {t} distinguished from closely related Principles.
- Causal links evidence-based; primary vs secondary Principle identified where useful.
- Links made to communication, function, audience, purpose and context.
- Trade-offs, accessibility and implementation considered; deliberate disruption recognised.
- Feedback and refinements specific and testable; evaluation criteria explicit.
- Australian English throughout.

For the full cross-Principle framework (all 15 Principles, discipline-specific detail, Factors
Affecting Design, teaching resources), use the `principles-of-design` skill if it is installed.""")

    target = OUT / f"{name}-principle-of-design"
    target.mkdir(parents=True, exist_ok=True)
    (target / "SKILL.md").write_text("\n\n".join(sections).rstrip() + "\n")
    return target


if __name__ == "__main__":
    for n, trig in PRINCIPLES.items():
        p = build(n, trig)
        print(p.relative_to(ROOT), len((p / "SKILL.md").read_text().splitlines()), "lines")
