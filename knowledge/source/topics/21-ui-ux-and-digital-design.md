# UI/UX and Digital Design

## Purpose and provenance

A reference knowledge base for Claude, covering concepts, relationships, application and teaching. This is not an installable skill.

General subject knowledge synthesised for this collection; relevant plugin instructions and verified primary-source links are identified in the collection references.

## UI, UX and interaction

User interface design concerns visible and operable controls and information. User experience concerns the broader experience of achieving a purpose across context, interaction and service. An attractive screen can still create poor usability.

**User need → task → information architecture → flow → wireframe → prototype → usability evidence → refinement.**

## Interface concepts

| Concept | Meaning |
|---|---|
| Information architecture | Organisation, labels and relationships of content |
| Affordance | Possible action offered by an object/system |
| Signifier | Perceivable cue indicating action or state |
| Discoverability | Ease of recognising what is available |
| Feedback | Indication of action results or system status |
| State | Condition such as idle, selected, loading, success or error |
| Progressive disclosure | Presenting complexity as needed |
| Component system | Reusable controls with defined variants and behaviour |
| Responsive design | Adaptation to viewport, content and user conditions |

Navigation should reflect users' tasks and language. Group related controls, use meaningful labels, provide clear status and make errors recoverable. Forms need visible labels, helpful validation and an understandable path to completion.

## Accessibility and interaction

Consider keyboard use, logical focus order, visible focus, semantic structure, accessible names, screen-reader feedback, reflow, zoom, contrast and reduced motion. Do not use colour alone to indicate error or selection.

W3C SC 1.4.3 specifies text contrast thresholds with defined exceptions; [SC 2.5.8](https://www.w3.org/WAI/WCAG22/quickref/) specifies minimum pointer target size or qualifying spacing/exceptions. A simple “all targets must be 44 px” claim confuses criteria and levels. Larger targets may remain a useful practical choice.

Web conformance cannot be established from a screenshot alone. Test implementation and representative user tasks.

## Usability testing

Give realistic tasks without explaining the interface solution. Observe completion, errors, hesitation, routes and comments. Avoid treating a small sample as representative statistical proof. A/B testing needs a defined measure and appropriate sample; two students preferring a colour is not a robust experiment.

## Dashboards and data

Define decisions the dashboard should support. Use accurate labels, units, dates and status. Distinguish missing data from zero and estimates from measured values. Priority controls should reflect meaningful categories rather than arbitrary colours.

Ethical UX avoids deceptive consent, hidden costs, coerced actions and deliberately difficult cancellation. Optimising clicks is not automatically beneficial to users.

## Teaching and application

Students can prototype a school-equipment selection interface or portfolio dashboard. Support with paper wireframes and a small component bank; extend through responsive states, task-based tests and competing user needs.

Justification framework: **control/layout decision → observable interaction effect → user task → evidence → suitability**. Assess reasoning and task success rather than decorative sophistication. Reusable components support consistency but must remain suitable for the content and access needs.


## Detailed element-specific applications from the existing knowledge base

The following material is extracted from the existing Elements of Design master. Original instructional phrasing and contextual claims are retained as inherited source material, not newly verified evidence. It provides deeper applications alongside the synthesis above.

### Colour

#### Digital / UI / UX

Use semantic colour for status, but combine with text, icon or shape. Test contrast, dark/light modes, colour vision differences, hover/focus/disabled states and data visualisations.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

### Direction

#### Digital / UI / UX

Direction governs arrows, chevrons, carousels, scroll cues, progress steps, swipe affordances, disclosure icons and spatial navigation. Do not assume left-to-right equals forward. Localisation, platform conventions and bidirectional scripts can change expectations.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

### Form

#### Digital / UI / UX

Most UI form is simulated rather than physical. Depth cues, shadows and elevation can imply layering or affordance, but excessive pseudo-3D treatment can reduce clarity. Physical interfaces require actual form and ergonomics.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

### Layout And Composition

#### Digital / UI / UX

Responsive layouts must reflow, reorder and resize while preserving logical reading order, accessibility and component relationships. A desktop grid should not simply be squeezed into mobile.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

### Line

#### Digital / UI / UX

Use line for dividers, borders, focus indicators, icon strokes, charts, connectors and progress paths. Prefer spacing and grouping over excessive rules. Focus indicators must remain visible; subtle hairlines may fail at zoom or on low-contrast displays.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

### Shape

#### Digital / UI / UX

Buttons, cards, chips, input fields, badges and icons depend on shape. Shape must support affordance and state differentiation without becoming the sole signal. Touch targets are about interactive area, not merely visible shape.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

### Size And Scale

#### Digital / UI / UX

Text size, icon size, touch targets and component scale affect accessibility and usability. Visual size and interactive hit area are separate. Responsive systems should maintain hierarchy rather than simply shrinking everything.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

### Space

#### Digital / UI / UX

Spacing systems, padding, touch-target separation, responsive gutters and content density directly affect usability. More space is not automatically better; excessive separation can weaken grouping and require more scrolling.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

### Texture

#### Digital / UI / UX

Visual texture should not reduce text readability or suggest false affordances. Physical interfaces may use texture for grip, orientation or control differentiation. Sensory sensitivity should be considered.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

### Time And Duration

#### Digital / UI / UX

Response time, feedback delay, loading states, microinteraction duration, progressive disclosure and timeouts affect usability. Users should be able to pause, stop or extend time where necessary; avoid auto-advancing essential content without control.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

### Typography

#### Digital / UI / UX

Responsive type scales, labels, forms, navigation and error states need readable sizes, line lengths and hierarchy. Font loading, fallback, localisation and user zoom must be anticipated.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

### Value

#### Digital / UI / UX

Value contrast is central to text, icons, focus states and component separation. Avoid relying on faint dividers. Test light/dark themes and disabled states without making essential content illegible.

Claude should consider usability, readability, discoverability, information hierarchy, responsive behaviour, cognitive load, touch/pointing interaction, localisation and assistive technologies.

## Connections

Use the [collection index](00-INDEX.md) to locate related topics. The shared reasoning frameworks and source notes are in [READ-ME-FIRST.md](READ-ME-FIRST.md). Specific curriculum codes, machine settings, platform limits and software commands require their identified current source before use.
