BESTAE — Brittany Elizabeth Staniforth, Teaching And Education — is a learning-design system, not just a visual brand: curriculum, pedagogy, accessibility, explicit teaching, assessment and visual communication work together in every resource BESTAE produces (workbooklets, worksheets, presentations, rubrics, Canva templates, curriculum planning documents). Judge every resource both as a designed object and as a piece of teaching.

Always write in Australian English (colour, organise, analyse, behaviour) across every resource this system produces.

## Content fundamentals

Write like a teacher who also runs a studio: clear, explicit, professional, never padded with generic education jargon or marketing-speak. Student-facing copy is encouraging, direct and age-appropriate; introduce technical terms rather than avoiding them (introduce → explain → model → expect independent use). Teacher-facing copy is concise, practical and pedagogically justified where it needs to be.

Split content into two families by what it asks the reader to do, and colour it accordingly: **Make** (workshops, templates, tutorials, hands-on/practical content) carries `h8-denim`; **Think** (courses, planning tools, consulting, conceptual content) carries `h9-twilight`. Don't force genuinely mixed content into one bucket.

Where the school's A–E grade scale applies, use its wording exactly and don't mix it with other performance language: **A** Extensive, **B** Thorough, **C** Sound, **D** Basic, **E** Elementary.

## Visual foundations — colour

BESTAE's palette is three ten-colour families — **H** (prominent, high-impact accents), **S** (deep/supporting tones — dark text, strong contrast, headers), **T** (light backgrounds and tints) — `h1-jazzberry` … `h10-valentine-pink`, `s1-mulberry` … `s10-plum`, `t1-piggy-pink` … `t10-powder-pink`. Colour communicates structure, not decoration: use it for domain/subject identification, section differentiation, activity type, worked examples, warnings or extension — never as the *only* signal for meaning. Eight of the ten H/S/T sets (2–6 and 8–10) double as this system's content-domain colours (Critical Thinking, Creative Thinking, Communication, Self-Management, Responsibility & Stewardship, Practical Skills, Knowledge & Conceptual Understanding, Independent Learning) — the same colour-by-domain logic Brittany already uses in her MCCNS/Canvas teaching materials, carried over and given retail names here; `h1`/`s1`/`t1` and `h7`/`s7`/`t7` are BESTAE-only additions not currently used at school.

Default usage: `surface` (white) is the base ground and the only choice for editable, image or placeholder areas where a tint would cost readability. `ink` (aliases `s8-night`) carries default body text and headings on `surface` or any T tint. `link` (aliases `h8-denim`) and `focus` (aliases `s8-night`) are fixed — don't substitute another accent for either.

Text on fills follows one rule, checked against WCAG 4.5:1:

- **White (`on-dark`) text:** `h1-jazzberry`, `h7-bondi-blue`, `h8-denim`, `h9-twilight`, and every S colour.
- **`ink` text:** every other H fill — `h2-tomato`, `h3-royal-orange`, `h4-corn`, `h5-lime`, `h6-seagreen`, `h10-valentine-pink`. White on these fails (1.3–3.1:1).
- **On a T tint:** text and icons use `ink` or the matching S colour, never the matching H colour (1.1–2.4:1 for sets 2–6 and 10). H colours are for fills, bars and large shapes.
- **Links on `t9-periwinkle`** use `link-on-t9` (`s9-dark-indigo`), underlined — denim is only 4.4:1 there.

Because several domain colours share a lightness (tomato, seagreen and valentine pink sit within a narrow band, and tomato vs seagreen is the classic red–green confusion), always show the domain **name or icon** with its colour; this matters most on greyscale print.

*Palette change, 29 Sept 2026:* `s4` is now `s4-dark-gold` `#8A6400`, a dark gold that keeps the Communication set's yellow base (was `s4-mustard` `#CFB500`, too light to act as a shade), and `h7-bondi-blue` is now `#007F98` (was `#008EAA`, which failed with both white and ink). Later the same day three domain tints were re-tinted so no two domain panels look alike: `t5-lime-cream` `#E8F6C4` (was `#EFF4A4`, indistinguishable from buttermilk), `t8-crushed-ice` `#D2DCE8` (was `#D5EBEE`), `t10-powder-pink` `#F7D0E6` (was `#F2DEE9`, indistinguishable from soft blush). Swatch files for Adobe, Canva, Figma and GIMP live in the BESTAE-AU/elementsandprinciplesofdesign repo under `brand/bestae/swatches/`.

For knowledge-domain presentation templates specifically, default to `h9-twilight` as the primary colour and `t9-periwinkle` as its soft background — don't introduce the full palette into a knowledge-domain template unless the content genuinely spans multiple domains.

## Visual foundations — typography

Lato is the only typeface across every BESTAE output — presentations, print, Canva templates. Don't substitute another face. Roles, from the `Presentation` type group: `title` (Lato Black, deck/document titles and the cover name), `subtitle` (Lato Light, under a title), `heading` (Lato Bold, same size as `subtitle` — bold is what makes it read as a heading rather than a subtitle), `subheading` (Lato Light), `section-header` (Lato Bold, card/section headers within a page), `body` (Lato Light, default copy), `quote` (Lato Light, same size as `body`, set in italics), `caption` (Lato Light, small print). Keep this hierarchy consistent slide by slide and page by page — don't change weights or sizes arbitrarily.

## Visual foundations — grid and layout

Presentations (Canva, 16:9 decks) use the `grid` token family: a **1920×1080px** canvas, `grid-margin` (100px) on every side, a 12-column / 12-row grid built from `grid-col-unit` (125px) and `grid-row-unit` (55px) with a `grid-gutter` (20px) between cells — giving an 1720×880px usable area. Use the `grid-col-span-*` / `grid-row-span-*` tokens for exact widths/heights (e.g. a 4-column-wide, 2-row-tall card is `grid-col-span-4` × `grid-row-span-2` = 560×130px), and derive a component's x/y position from `grid-margin + (start column − 1) × (grid-col-unit + grid-gutter)` and the row equivalent. When building a reusable Canva template rather than a finished lesson, populate it with placeholder labels (Heading, Body, Image, Diagram, Callout, Teacher Note, Activity Panel), not lesson content.

Print resources (workbooklets, worksheets, A4 documents) use Brittany's existing Greyscale Workbooklet print grid unchanged — a 12×12 modular grid in millimetres, A4 portrait with 12/12/10/10mm margins (or 12/12/12/8mm for a saddle-stitch booklet), 2mm column and 3mm row gutters. Treat that system, not the presentation grid above, as the source of truth for anything going to print.

Round with `radius-md` for cards, buttons and images; step up to `radius-lg` for feature panels and hero blocks; `radius-full` is reserved for pills and the BESTAE monogram badge. Stack and pad with the `space-*` scale rather than arbitrary values.

## Pedagogical design rules (apply to every resource, not only visuals)

A resource is not finished because it looks right — check it against these before calling it done:

- **Explicit teaching.** For unfamiliar concepts or practical skills, support an I do (model) → We do (guided practice) → You do (independent application) progression — apply the principle, don't mechanically label every resource with those three headings.
- **Scaffolding fades, it doesn't replace thinking.** Guiding questions, worked/partial examples, word banks, sentence starters and checklists should reduce *extraneous* load, never the intellectual challenge itself; withdraw scaffolds over time rather than leaving them in permanently.
- **Cognitive load.** Chunk content, use consistent terminology and visual patterns, and signal structure explicitly. Avoid dense text walls, decoration that doesn't aid comprehension, and requiring students to infer hidden task requirements.
- **Accessibility is non-negotiable, not an add-on.** Every instructional image needs alt text describing its instructional purpose; essential video needs captions or a transcript; a graph whose interpretation isn't the point of the task needs an accessible data table or description; never rely on colour alone to carry meaning.
- **Practical/workshop content teaches WHS by default** alongside what-to-do and how-to-know-it's-correct — equipment, setup, safety, sequence, checkpoints, common mistakes, quality expectations.
- **Assessment measures quality, not completion.** Rubric criteria must be observable and distinct; avoid unsupported descriptors ("good", "excellent") unless the descriptor itself defines what that quality means. Feedback names what was demonstrated, what needs improvement, and what to do next — specific feedforward, not "add more detail".
- **Never invent** curriculum outcomes, content points, assessment rules, BESTAE programmes, claims, prices or effectiveness data. Flag what's missing rather than filling the gap.

## Iconography

No icon set has been supplied yet. Where an icon is genuinely needed, use a simple, single-weight line icon (no filled icons, no emoji as decoration) in `ink` or the relevant H/S colour — flag it as a placeholder until a proper set exists.

## Assets

No logo or wordmark has been supplied. Until one exists, set "BESTAE" in plain `title` type (see the cover) rather than approximating a mark.
