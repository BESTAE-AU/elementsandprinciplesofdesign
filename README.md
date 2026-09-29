# elementsandprinciplesofdesign

Claude skills for reasoning about the Elements and Principles of Design.

## `principles-of-design/`

A design-reasoning, teaching, critique and justification framework for the 15 Principles of Design,
across graphic design, branding, multimedia, UI/UX, textiles, product, spatial design and
architecture. Written in Australian English.

```
principles-of-design/
├── SKILL.md                                   core reasoning model, protocols, routing
└── references/
    ├── principles/<principle>.md              one file per Principle (15)
    ├── causal-reasoning.md                    Principle chains, networks, dependencies, cause vs correlation
    ├── relationships.md                       Element ↔ Principle links, Principle distinctions
    ├── disciplines.md                         branding, multimedia, time-based, UI/UX, textiles, product, spatial
    ├── cross-cutting-considerations.md        CFPA, accessibility, production, sustainability, ethics, Factors Affecting Design, trade-offs, rule-breaking
    ├── analysis-justification-feedback.md     analysis, justification, exemplars, critique, evaluation, refinement
    ├── experimentation.md                     controlled experimentation
    └── teaching-resources.md                  questioning, vocabulary, misconceptions, resources, differentiation
```

`SKILL.md` stays short so it loads quickly when the skill triggers; Claude reads the reference
files only when a task needs that depth.

### Installing

Package with the skill-creator `package_skill.py` script (or zip the `principles-of-design/`
folder) and upload it via Claude settings → Capabilities → Skills, or copy the folder into
`~/.claude/skills/` for Claude Code.
