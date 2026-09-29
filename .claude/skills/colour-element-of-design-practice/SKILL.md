---
name: colour-element-of-design-practice
description: >
  Helps apply COLOUR as an element of design in a real project, whether the user's
  own or a student's brand, poster, product, garment, video, interface or space.
  It chooses and tests colour variables one at a time, checks production and
  reproduction limits, tests brand decisions across touchpoints, and writes up the
  final decision with evidence, alternatives and trade-offs. Use it whenever
  someone is designing something and asks how to handle colour, what to change or
  how to justify it, even if they only mention "colour scheme", "brand colours",
  "my colours clash" or "colour grading".
---

# Colour: applying it in a design

This skill handles **applying it in a design** for colour as an element of design. Everything known about colour (definition, variables, types, relationships with the other elements and the principles, fields, production, misconceptions and worked examples) is in `references/element-knowledge.md`. The shared method is in `references/design-method.md`. Read the sections the workflow points to.

Related skills: `colour-element-of-design-teaching`, `colour-element-of-design-feedback`, `colour-element-of-design-analysis`; `colour-element-of-design` for general questions about colour; the `*-principle-of-design` skills for principles.

**Hand off to specialist skills when they fit and are available:**
- building a palette from a brief → `colour-palette-builder`
- writing a colour-psychology or brand rationale → `colour-psychology-rationale`
- WCAG contrast ratios and palette audits → `colour-contrast-audit`
- identifying and critiquing a colour scheme → `colour-harmony-analyser`
- HEX/RGB/CMYK conversions → `colour-codes-and-conversion`
- the physics and biology of colour → `colour-science-explainer`
- colour-theory lesson activities and videos → `colour-theory-teaching-activities`

Apply the language rules in `references/design-method.md` §14: Australian English, describe before interpreting, conditional language for emotional or cultural associations, and name the criterion whenever something "works".

## Workflow

1. **Clarify the brief.** Get the audience, purpose, every output or touchpoint, the production methods and any fixed constraints (brand rules, budget, equipment).
2. **Name the design question** before changing anything, e.g. "which weight keeps the mark readable at 16 px and in embroidery?". Don't vary things at random (method §7).
3. **Pick one variable** from the table below and propose three clearly different options. Hold the rest constant.
4. **Test in real conditions:** real size, real medium, real viewing distance or device. Check the production table below.
5. **If it's a brand,** extend the surviving options to at least three touchpoints and record what breaks away from the logo (method §8).
6. **Decide and record** the result as a rule (e.g. minimum sizes, permitted variants) and as a sophisticated justification: evidence → alternative rejected → trade-off accepted (method §4).

## Variables

| Variable | Range | Typical effect | Watch for |
|---|---|---|---|
| **Hue** | the colour wheel | differentiates and categorises | Meaning is contextual and cultural |
| **Saturation** | muted ↔ vivid | intensity, prominence | Vivid isn't automatically more accessible |
| **Value** | light ↔ dark | hierarchy, contrast | Test separately from hue |
| **Tint / shade / tone** | added white, black or grey | extends palette relationships | Terms vary; define them when teaching |
| **Temperature** | warmer ↔ cooler | relative colour interaction | Temperature is relative, not absolute |
| **Proportion / dominance** | how much of each colour | hierarchy, overall reading | A small accent can dominate |
| **Contrast** | of value, hue, saturation, complement | separation, emphasis | Check accessibility |
| **Interaction** | simultaneous contrast, surrounding colour | changes perceived colour | Judge colours in place, not as swatches |
| **Medium / lighting** | screen, ink, dye, material, light source | changes appearance and gamut | Proof and colour-manage |

## Production and reproduction

| Process | Colour risks |
|---|---|
| Screen (RGB) | Appearance varies with device, brightness, gamut and calibration |
| CMYK print | Some RGB colours are out of gamut; proof with the printer's profile |
| Spot / Pantone | Controlled matching, but stock and coating still change the result |
| Textile dye / print | Fibre chemistry, process and batch change the result |
| Embroidery / vinyl | Thread and film ranges limit exact matching |

## Colour across fields

- **Branding:** a brand colour system is more than one signature hue: primary, secondary, supporting and semantic colours; accessible pairings; logo colour versions; background rules; digital and print specs (RGB/HEX, CMYK, Pantone); material and finish references; and proportion across touchpoints.
- **Graphic and communication design:** colour organises hierarchy, grouping, navigation and data. Ask what information becomes easier or harder to find.
- **Photography, film and animation:** lighting, white balance, production design and grading create colour. Keep palette continuity across frames and displays; don't let colour changes carry essential meaning alone.
- **UI / UX:** semantic colour for status (error, success, warning) must be paired with text, icon or shape. Test contrast, light and dark modes, colour-vision differences, hover/focus/disabled states and charts.
- **Textiles and fashion:** colour depends on fibre, yarn, dye class, print method, surface and light; it shifts between materials and batches. Pattern scale changes colour proportion.
- **Product and industrial design:** material colour, coatings, gloss and texture change perceived colour. Colour can signal controls, hazards or status, subject to standards.
- **Interiors and architecture:** daylight, artificial light, reflectance and adjacency change colour; large areas look different from swatches.
- **Technical communication:** colour can code categories in diagrams and maps but must not be the only identifier; plan for greyscale printing.
