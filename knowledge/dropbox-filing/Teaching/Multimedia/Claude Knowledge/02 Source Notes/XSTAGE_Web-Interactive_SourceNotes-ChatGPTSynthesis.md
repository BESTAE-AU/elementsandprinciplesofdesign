# UI/UX and digital design

> Source: ChatGPT knowledge collection (topic 21), imported and trimmed on 1 October 2026. Per-element boilerplate is removed because the element-of-design skills cover it. Treat as reference notes: check claims against current syllabus, policy and manufacturer documentation before use.

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
