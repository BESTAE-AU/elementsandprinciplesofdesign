# BESTAE colour audit

*Run 29 Sept 2026 with the colour-theory skills in this repo (`colour-contrast-audit`, `colour-harmony-analyser`, `colour-palette-builder`).*

## Sources checked

| Source | What it holds | Status |
|---|---|---|
| **BESTAE design system** artifact (`tokens.json`, `README.md`) | H/S/T families × 10, `surface`, `ink`, `on-dark`, `link`, `focus`, plus pairing rules | **Source of truth.** Hex values match the 2026 pptx exactly |
| `Bestae Template.pptx` (Google Drive, Feb 2026) | Same 30 hex values as CSS classes | Matches |
| Canva **Bestae Presentation – Brand Template** and 5 Canva brand kits | h9 twilight + t9 periwinkle + white | Matches the "knowledge-domain template" rule |
| `Bestae Branding and Word Template.docx` (Dropbox, June 2025) | Domain → primary/tint/shade table | **Out of date:** every hex differs slightly and some names don't match (see §5) |
| **Bestae Site Map** artifact | Its own subject colour set (e.g. `#1b6fa8`, `#c0462b`) | **Not on-brand:** doesn't use BESTAE tokens (see §6) |

## 1. What already works

- **The system shape is right.** The 10 hues span the whole wheel (`harmony` reports *free / mixed*). That's expected for a **colour-coding system**, not a palette to use all at once. Each H/S/T set is a ready-made **monochromatic** palette (accent, deep, tint), which the source videos call the safest harmony.
- **The Canva knowledge template follows 60-30-10** almost exactly: white or `t9-periwinkle` about 60%, `h9-twilight` panels and headings about 30%, `s9`/`t9` chips as the accent. Pairs: `h9` on `t9` **5.61:1**, white on `h9` **8.12:1**, `s9` on `t9` **11.52:1**. All pass.
- **`ink` on every T tint passes** (11.4–14.5:1), and every S shade except `s4` passes white text (10.9–16.7:1).
- The brand book already says *never use colour alone for meaning*. Keep that rule; §4 shows why it matters.

## 2. Fix: five H fills are marked "pair with `on-dark`" but white text fails

| H fill | White text | `ink` text | Fix |
|---|---|---|---|
| h2-tomato `#FF585D` | 3.09 ✗ | **5.36** ✓ | Use `ink` |
| h3-royal-orange `#F19C49` | 2.19 ✗ | **7.56** ✓ | Use `ink` |
| h6-seagreen `#00B2A2` | 2.66 ✗ | **6.21** ✓ | Use `ink` |
| h10-valentine-pink `#E56DB1` | 2.94 ✗ | **5.64** ✓ | Use `ink` |
| h7-bondi-blue `#008EAA` | 3.85 ✗ | 4.29 ✗ | Sits in the mid-tone **danger zone**. Use it for large text or shapes only (≥3:1), or adopt a slightly deeper `#007F98` (4.6:1 with white) |
| h4-corn, h5-lime | 1.25 / 1.39 ✗ | 13.18 / 11.92 ✓ | Already correct in the brand book |
| h1-jazzberry, h8-denim, h9-twilight | **7.00 / 6.33 / 8.12** ✓ | ✗ | White is correct |

**Simpler rule to put in the brand book:** *White text only on h1, h8, h9 and on every S shade except s4. `ink` text on every other H fill.*

## 3. Fix: `s4-mustard` isn't a shade

`#CFB500` gets 2.05:1 with white and 1.79:1 on its own tint `t4`, so it can't do the S job of "dark text, headers, strong contrast". Every other S shade is 10.9–16.7:1.
**Proposed:** make `s4` a true dark olive, **`#4B4200`** (10.1:1 on white, 8.86:1 on `t4`, 8.05:1 on `h4`), and keep `#CFB500` only as a decorative mid-tone (e.g. a rule line). *This changes a brand colour, so it's your call.*

## 4. Watch: links, chips and colour-vision

- **`link` (h8-denim) on `t9-periwinkle` = 4.38:1.** That fails, and it's on the *default* knowledge-template background. On t9, links should be `s9-dark-indigo` (11.5:1) and underlined. Denim passes on every other tint (4.78–5.55).
- **H on its own T** (e.g. a coloured icon or heading on a domain panel) fails for 6 of 10 sets: h2 2.35, h3 1.72, h4 1.10, h5 1.20, h6 2.20, h10 2.29. **Rule: on a T panel, text and icons use the matching S (or `ink`). H is for fills and large shapes.**
- **Red/green look-alikes:** h2-tomato (Critical Thinking) and h6-seagreen (Responsibility) have almost the same lightness (0.29 vs 0.34 relative luminance), and tomato vs pink vs seagreen sit within 0.05 of each other. People with the common red–green colour-vision types won't tell those domains apart by colour. **Always print the domain name or icon with the colour**, especially on greyscale printouts.

## 5. Update the 2025 Word template

The Word template's domain table predates the design system. The hex values are near-identical (1.01–1.08:1 difference, so you can't see it) but not the same, which breaks exact matching in Canva and Illustrator. Some names are also wrong:

| Domain | Word 2025 | Design system 2026 |
|---|---|---|
| Critical Thinking | `#FE5F55` | h2 `#FF585D` |
| Creative Thinking | `#F29E4C` | h3 `#F19C49` |
| Communication | `#EFEA5A` | h4 `#F3EA5D` |
| Self-Management ("Teal" in Word) | `#B9E769` | h5-lime `#C5E86C` |
| Responsible Design → Responsibility & Stewardship ("Green" in Word) | `#0DB39E` | h6-seagreen `#00B2A2` |
| Practical Skills | `#2C699A` | h8 `#326295` |
| Knowledge & Understanding | `#54478C` | h9 `#514689` |
| Independent Learning | `#E866B0` | h10 `#E56DB1` |
| (unassigned) | `#AA1155` | h1 `#AC145A` |

The Word tint and shade columns also differ from the T and S tokens (e.g. Word shade `#E2A712` vs `s4 #CFB500`).

## 6. Bring the Site Map artifact on-brand

The site map colours each subject with its own palette (`#1b6fa8`, `#c0462b`, `#a3346b`…) and uses Bricolage Grotesque and Atkinson Hyperlegible rather than Lato. If subjects need colours, map them onto BESTAE H/S/T sets rather than a new palette. Remember that the brand reserves colour for **domains and activity type**, so a second, subject-based colour code would compete with it. The simplest fix: subject names in `ink`, one accent (`h8` Make / `h9` Think), and domain colours only where the content is domain-tagged.

## 7. Usage rules (60-30-10 for BESTAE resources)

| Resource | 60% | 30% | 10% |
|---|---|---|---|
| Single-domain deck or page | `surface` / that domain's T | that domain's H (fills) + S (headings) | `ink` text; one CTA or highlight |
| Knowledge template (default) | `surface` / `t9` | `h9` | `s9` chips; links in `s9` on t9 |
| Multi-domain resource | `surface` | each domain's **T** as its panel background, **S** for its header | H only as small markers (tabs, icons with labels) |
| Greyscale print | Colour carries no meaning: label domains by name and icon, per the greyscale print system | | |

## Swatch files (`swatches/`)

All 32 tokens with their token names:
- `bestae.ase`: Illustrator, Photoshop, InDesign (*Swatches › Open Swatch Library › Other Library*)
- `bestae.css`: Figma, web
- `bestae-canva-paste-list.txt`: Canva brand kit
- `bestae.gpl`: GIMP, Inkscape, Krita
- `bestae.json`

These are the **current** values. If you adopt the §2/§3 fixes, re-export with `shared/colour_tools.py export`.
