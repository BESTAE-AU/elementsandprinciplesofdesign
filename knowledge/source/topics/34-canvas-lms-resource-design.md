# Canvas/LMS Resource Design

## Purpose and provenance

A reference knowledge base for Claude, covering concepts, relationships, application and teaching. This is not an installable skill.

Canvas Instructure Formatter instructions, Multimedia Teaching Assistant content architecture and current Instructure documentation. No Canvas page was edited or published in producing this collection.

## Canvas and LMS resource design

An LMS page should make learning, navigation, resources and next actions clear. Structure modules around a coherent sequence and use consistent naming. The page title supplies the main heading; content should have a logical subsequent heading structure.

## Established Canvas Formatter preferences

The Canvas Instructure Formatter plugin prioritises teacher-editable, stable HTML: inline styles, simple tables, centred layouts usually at 90% width, collapsed borders and balanced columns. It avoids external CSS, style blocks, JavaScript, complex div layouts and decorative cards by default. Maintain the Canvas default font.

Visible headings are written in uppercase in the source text. Use h2, h3 and h4 according to hierarchy, with separate editable heading and content cells when practical. H2 uses a domain highlight, H3 its shade, H4 its tint; body cells use white. Bold paragraph subheadings can use the matching shade.

These are the user's formatting preferences, not general HTML best practice or an accessibility guarantee. Layout tables should not be mistaken for data tables. Preserve logical reading order and minimise unnecessary nesting. Data tables need proper header semantics and meaningful captions; presentation-only layouts need appropriate semantics compatible with the platform.

## Domains and branding

Use the exact domain palette in topic 38. The plugin maps critical thinking to 2, creativity/problem-solving/innovation to 3, communication to 4, self-management to 5, responsibility/stewardship to 6, practical skills to 8, knowledge to 9 and independent learning/collaboration to 10. Do not use groups 1 or 7 as domains unless requested.

MCCNS branding is used only when requested: navy #001D3E, light blue #D9DDE2, yellow #FFCB05 and cerise #A6214D. Do not substitute this for BESTAE silently.

## Media and access

Use meaningful image alternatives, descriptive links and titled embeds. The plugin prefers images at 100% width with 12 px rounded corners and video iframes at 100% width. Image rounding is visual treatment, not an access feature.

Provide captions and suitable text access; an automated transcript should be checked. Avoid wide layouts that force horizontal scrolling on a small device. Colour coding needs visible labels. Verify contrast against the actual foreground/background pair.

The [Canvas HTML allowlist](https://community.instructure.com/en/kb/articles/387066-canvas-html-editor-allowlist) determines supported markup. The [Accessibility Checker guidance](https://community.instructure.com/en/kb/articles/664351-how-do-i-use-the-accessibility-checker-in-canvas) identifies checks and limitations. A passing automated check is not proof of full accessibility.

## Content and editing workflow

**Learning goal → concise explanation → model/media → guided task → project application → check for understanding → next step.**

Keep source content separate from rendered HTML. Verify links, embedded permissions, mobile display, heading order, table editability and student view. Avoid unpublished resources in a student-facing navigation chain.

The plugin's HTML-only output rule applies when producing Canvas-ready pages; this knowledge base intentionally records the underlying requirements as Markdown.

## Connections

Use the [collection index](00-INDEX.md) to locate related topics. The shared reasoning frameworks and source notes are in [READ-ME-FIRST.md](READ-ME-FIRST.md). Specific curriculum codes, machine settings, platform limits and software commands require their identified current source before use.
