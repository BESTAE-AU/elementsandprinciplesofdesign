# Canvas, workbooklet and educational document design

> Source: ChatGPT knowledge collection (topic 34, 35, 37), imported and trimmed on 1 October 2026. Per-element boilerplate is removed because the element-of-design skills cover it. Treat as reference notes: check claims against current syllabus, policy and manufacturer documentation before use.

## Canvas/LMS Resource Design

### Canvas and LMS resource design

An LMS page should make learning, navigation, resources and next actions clear. Structure modules around a coherent sequence and use consistent naming. The page title supplies the main heading; content should have a logical subsequent heading structure.

### Established Canvas Formatter preferences

The Canvas Instructure Formatter plugin prioritises teacher-editable, stable HTML: inline styles, simple tables, centred layouts usually at 90% width, collapsed borders and balanced columns. It avoids external CSS, style blocks, JavaScript, complex div layouts and decorative cards by default. Maintain the Canvas default font.

Visible headings are written in uppercase in the source text. Use h2, h3 and h4 according to hierarchy, with separate editable heading and content cells when practical. H2 uses a domain highlight, H3 its shade, H4 its tint; body cells use white. Bold paragraph subheadings can use the matching shade.

These are the user's formatting preferences, not general HTML best practice or an accessibility guarantee. Layout tables should not be mistaken for data tables. Preserve logical reading order and minimise unnecessary nesting. Data tables need proper header semantics and meaningful captions; presentation-only layouts need appropriate semantics compatible with the platform.

### Domains and branding

Use the exact domain palette in topic 38. The plugin maps critical thinking to 2, creativity/problem-solving/innovation to 3, communication to 4, self-management to 5, responsibility/stewardship to 6, practical skills to 8, knowledge to 9 and independent learning/collaboration to 10. Do not use groups 1 or 7 as domains unless requested.

MCCNS branding is used only when requested: navy #001D3E, light blue #D9DDE2, yellow #FFCB05 and cerise #A6214D. Do not substitute this for BESTAE silently.

### Media and access

Use meaningful image alternatives, descriptive links and titled embeds. The plugin prefers images at 100% width with 12 px rounded corners and video iframes at 100% width. Image rounding is visual treatment, not an access feature.

Provide captions and suitable text access; an automated transcript should be checked. Avoid wide layouts that force horizontal scrolling on a small device. Colour coding needs visible labels. Verify contrast against the actual foreground/background pair.

The [Canvas HTML allowlist](https://community.instructure.com/en/kb/articles/387066-canvas-html-editor-allowlist) determines supported markup. The [Accessibility Checker guidance](https://community.instructure.com/en/kb/articles/664351-how-do-i-use-the-accessibility-checker-in-canvas) identifies checks and limitations. A passing automated check is not proof of full accessibility.

### Content and editing workflow

**Learning goal → concise explanation → model/media → guided task → project application → check for understanding → next step.**

Keep source content separate from rendered HTML. Verify links, embedded permissions, mobile display, heading order, table editability and student view. Avoid unpublished resources in a student-facing navigation chain.

The plugin's HTML-only output rule applies when producing Canvas-ready pages; this knowledge base intentionally records the underlying requirements as Markdown.

## Learning Resource and Workbooklet Design

### Learning resources and workbooklets

A resource should help students learn or make a decision, not merely occupy space. A workbooklet can organise modelling, guided practice, investigation, planning and evidence collection while leaving meaningful student choices.

**Learning/decision → required evidence → scaffold → response space → checking → application.**

### Core resource types

Worksheets focus a defined task. Student guides support independent reference. Teacher guides explain implementation and expected evidence. Exemplars reveal quality and reasoning. Checklists support monitoring. Decision matrices compare alternatives. Learning maps show relationships and sequence. Posters serve rapid reference at an appropriate viewing distance.

Select the format for the cognitive work. A comparison table suits alternatives; a sequence suits ordered actions; annotated images support visual reasoning. Avoid placing all content into tables when relationships become harder to read.

### Established user preferences

- Use tables wherever they improve comparison or provide useful response space.
- Leave sufficient blank space; writing lines are not required.
- Use clear headings rather than unnecessary first-person prompts such as “What I want”.
- Students should select and justify each piece of equipment, acknowledging what they can access.
- Organise camera equipment scaffolds under camera, support/mounting, lighting, movement, lens, power/storage, safety and audio.
- Keep directions concise while retaining the reasoning required.

These are project/resource preferences, not mandatory wording for every resource.

### Scaffold quality

A scaffold should expose reasoning: **selection → capability/property → effect → purpose → suitability → alternative/trade-off**. It becomes too restrictive if the final answer is already prescribed.

Support can include word banks, choices, partially completed examples, visual prompts and sentence stems. Fade support as learners become more capable. Extension should increase reasoning, complexity or transfer rather than only writing volume.

### Example equipment-selection table

| Equipment category | Available option | Intended use | Why appropriate | Limitation/alternative |
|---|---|---|---|---|
| Camera support | Student completes | Student completes | Student connects stability to shot purpose | Student completes |

Provide room for each equipment justification. Do not assume a professional rig is required when a simpler safe method satisfies the brief.

### Layout and access

Coordinate headings, explanatory text and response areas. Avoid splitting rows across pages where possible. Put instructions close to the relevant response. Use readable type, strong contrast, meaningful media descriptions and accessible digital fields if creating a fillable resource.

Blank space needs purpose: too little restricts evidence; too much can obscure task structure. Fit short tables on one page when practical, but do not shrink text excessively to force it.

### Review and assessment

Check that students know what to do, what evidence to supply, how much detail is expected and how the result supports their project. Pilot one section or inspect a sample response before duplicating a poor scaffold throughout a booklet.

Assess the learning demonstrated, not simply whether every box contains text. A concise evidence-based justification can be stronger than a long generic paragraph.

## Educational Presentation and Document Design

### Educational presentation and document design

Design should make ideas, instructions and relationships easy to perceive. A visually coherent resource supports learning when hierarchy, reading order, spacing and media are matched to purpose.

### Presentations

Use a clear title, one coherent focus per slide where practical, meaningful grouping and appropriate visual density. A presentation shown in a classroom has different constraints from a document read closely on a device. Test the actual viewing distance and projection conditions.

Avoid treating slides as pages of continuous prose. Coordinate spoken explanation and visuals; provide reference content separately when necessary. Essential labels and diagrams should remain understandable without tiny captions.

The BESTAE 1920 × 1080 grid and Lato typography are documented in topic 38. Exact template values are brand source requirements, but final readability still needs checking. Do not silently apply them to MCCNS or MBE resources.

### Documents and tables

Use consistent styles, margins, headings and spacing. Tables suit comparison and structured response, but excessively narrow columns or nested tables can hinder reading and access.

Established user table preferences include:

- High-contrast borders: light internal borders on dark fills, appropriately contrasting borders on lighter cells.
- With a cell border, images should be 0.5 mm smaller in total width and height than the cell, subject to actual layout and padding.
- Without borders, edge-to-edge images should use zero cell padding where supported.
- Prevent rows splitting across pages where practical.
- Keep short tables on one page when content can fit comfortably; permit long tables to continue.
- Landscape tables may be 26 or 27 cm wide according to the page setup.

The 0.5 mm image instruction does not mean 0.5 mm on each side. Check the final rendering because borders and editor behaviour can affect dimensions.

### Grids and geometry

For an N-column grid, available width is **page width − left margin − right margin**. Column width is **(available width − (N−1) × gutter) ÷ N**. A span covers columns plus internal gutters. Account for the last gutter correctly.

Grid alignment supplies consistency but may need optical correction for irregular shapes and type. It should organise content without forcing unreadable fits.

### Accessibility and media

Use meaningful heading structure, logical reading order, descriptive links, contrast, accessible tables and media alternatives. Colour alone should not carry required meaning. PDF export can lose structure; inspect tags, reading order and real output where required.

Avoid essential text embedded only inside an image. Check crop, distortion, resolution and permission for every asset. A design that looks clear on the author's screen may fail when printed or projected.

### Verification

Render final documents and inspect page breaks, row splits, clipping, whitespace, image fit and heading continuity. Inspect slide layout and speaker/reference material separately. Validate calculations and table totals before styling.

Teaching application: compare two layouts with the same content, then explain hierarchy and access differences. Assess communication effectiveness rather than decorative complexity.
