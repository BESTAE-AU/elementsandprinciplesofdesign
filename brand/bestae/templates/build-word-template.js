// Builds "BESTAE Word Template.docx" from the BESTAE design system tokens
// (29 Sept 2026 palette). Run: node build-word-template.js
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  ShadingType, BorderStyle, AlignmentType, HeadingLevel, LevelFormat, Header,
  Footer, PageNumber, TabStopType, PageBreak, TableLayoutType,
} = require("docx");

// ---- tokens (hex without #) ------------------------------------------------
const C = {
  ink: "041E42", white: "FFFFFF", muted: "5B6470", line: "C9CDD6",
  h: { 1: "AC145A", 2: "FF585D", 3: "F19C49", 4: "F3EA5D", 5: "C5E86C", 6: "00B2A2", 7: "007F98", 8: "326295", 9: "514689", 10: "E56DB1" },
  s: { 1: "651C32", 2: "551C25", 3: "4F2C1D", 4: "8A6400", 5: "1C4220", 6: "024638", 7: "003540", 8: "041E42", 9: "201547", 10: "621244" },
  t: { 1: "EEDAEA", 2: "F5DADF", 3: "FFDFB4", 4: "F7F4A2", 5: "EFF4A4", 6: "D7EFE7", 7: "DCEBEC", 8: "D5EBEE", 9: "DCD3E7", 10: "F2DEE9" },
};
// White text only on these H fills; every other H fill takes ink.
const WHITE_ON_H = new Set([1, 7, 8, 9]);
const onH = (n) => (WHITE_ON_H.has(n) ? C.white : C.ink);

const DOMAINS = [
  { n: 2, name: "Critical Thinking", h: "Tomato", verbs: "analyse, evaluate, compare, justify" },
  { n: 3, name: "Creative Thinking, Problem Solving & Innovation", h: "Royal orange", verbs: "generate ideas, prototype, refine" },
  { n: 4, name: "Communication", h: "Corn", verbs: "explain, document, present" },
  { n: 5, name: "Self-Management & Organisation", h: "Lime", verbs: "plan, sequence, follow procedure" },
  { n: 6, name: "Responsibility & Stewardship", h: "Seagreen", verbs: "safety, sustainability, ethics" },
  { n: 8, name: "Practical Skills & Technical Application", h: "Denim", verbs: "make, operate, apply techniques" },
  { n: 9, name: "Knowledge & Conceptual Understanding", h: "Twilight", verbs: "define, describe, explain concepts" },
  { n: 10, name: "Independent Learning & Collaboration", h: "Valentine pink", verbs: "goal-setting, reflection, feedback" },
];

// ---- page: A4 portrait, greyscale-print-grid margins (mm -> DXA) ----------
const mm = (v) => Math.round(v * 56.6929);
const PAGE_W = mm(210);
const MARGIN = { top: mm(12), bottom: mm(12), left: mm(10), right: mm(10) };
const CONTENT_W = PAGE_W - MARGIN.left - MARGIN.right; // ~10772 DXA (190 mm)

const FONT = "Lato";
const border = (color = C.line, size = 4) => ({ style: BorderStyle.SINGLE, size, color });
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const allBorders = (b) => ({ top: b, bottom: b, left: b, right: b });
const shade = (fill) => ({ type: ShadingType.CLEAR, color: "auto", fill });

function run(text, o = {}) {
  return new TextRun({ text, font: o.font || FONT, bold: o.bold, italics: o.italics, color: o.color, size: o.size });
}
function para(text, o = {}) {
  const runs = Array.isArray(text) ? text : [run(text, o)];
  return new Paragraph({ style: o.style, heading: o.heading, alignment: o.align, spacing: o.spacing, children: runs, keepNext: o.keepNext });
}
function cell(children, o = {}) {
  return new TableCell({
    width: { size: o.w, type: WidthType.DXA },
    shading: o.fill ? shade(o.fill) : undefined,
    borders: o.borders || allBorders(border()),
    margins: { top: 90, bottom: 90, left: 140, right: 140 },
    columnSpan: o.span,
    verticalAlign: o.vAlign,
    children: (Array.isArray(children) ? children : [children]).map((c) => (typeof c === "string" ? para(c, { style: o.pStyle || "TableText", color: o.color }) : c)),
  });
}
function table(widths, rows) {
  return new Table({ width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED, rows });
}
function headerRow(labels, widths, fill = C.h[9], color = C.white) {
  return new TableRow({
    tableHeader: true,
    children: labels.map((l, i) => cell(para(l, { style: "TableHeading", color }), { w: widths[i], fill })),
  });
}
const spacer = (after = 120) => new Paragraph({ spacing: { after }, children: [] });

// A callout panel: tint background, S-coloured label (never the H colour on its tint).
function callout(label, body, n) {
  return table([CONTENT_W], [
    new TableRow({ children: [cell([
      para(label.toUpperCase(), { style: "PanelLabel", color: C.s[n] }),
      ...(Array.isArray(body) ? body : [body]).map((b) => para(b, { style: "PanelText" })),
    ], { w: CONTENT_W, fill: C.t[n], borders: { top: noBorder, bottom: noBorder, right: noBorder, left: border(C.h[n], 24) } })] }),
  ]);
}

// ---- content --------------------------------------------------------------
const children = [];

// Cover block
children.push(
  para("BESTAE", { style: "Title" }),
  para("Resource title goes here", { style: "Subtitle" }),
  para([run("Course  ", { bold: true, color: C.s[9] }), run("Course name · Stage · Year"), run("     Focus area  ", { bold: true, color: C.s[9] }), run("Topic or unit")], { style: "Meta" }),
  para([run("Outcome  ", { bold: true, color: C.s[9] }), run("Syllabus outcome code and description")], { style: "Meta" }),
  new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: C.h[9], space: 6 } }, spacing: { after: 240 }, children: [] }),
);

// Heading hierarchy
children.push(
  para("Heading 1: section title", { heading: HeadingLevel.HEADING_1 }),
  para("Body text is Lato at 10.5 pt in ink (#041E42). Keep paragraphs short and chunk content under clear headings. Introduce technical terms, explain them, model them, then expect students to use them independently. Write in Australian English.", { style: "Normal" }),
  para("Heading 2: sub-section", { heading: HeadingLevel.HEADING_2 }),
  para("Heading 3: minor heading", { heading: HeadingLevel.HEADING_3 }),
  new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [run("Bulleted list item")] }),
  new Paragraph({ numbering: { reference: "bullets", level: 1 }, children: [run("Second-level bullet")] }),
  new Paragraph({ numbering: { reference: "steps", level: 0 }, children: [run("Numbered step for a procedure")] }),
  new Paragraph({ numbering: { reference: "steps", level: 0 }, children: [run("Next numbered step")] }),
  para("“Quote style: Lato italic, twilight rule on the left. Use for quotations and source extracts.”", { style: "Quote" }),
  para([run("Key term: ", { bold: true, color: C.s[9] }), run("Strong emphasis uses bold dark indigo; never colour alone for meaning.")], { style: "Normal" }),
  spacer(),
);

// Callout panels
children.push(para("Panels", { heading: HeadingLevel.HEADING_2 }));
children.push(
  callout("Key idea", "Summarise the core concept in one sentence.", 9), spacer(),
  callout("Teacher note", "Differentiation tips, scaffolding ideas or timing guidance.", 8), spacer(),
  callout("Activity", ["Task instruction goes here.", "Step or question placeholder."], 5), spacer(),
  callout("Safety (WHS)", "Equipment, setup and safety checkpoint for practical work.", 6), spacer(),
  callout("Extension", "Challenge task for students ready to go further.", 10), spacer(),
);

// Lesson planning table (headings carried over from the 2025 template)
children.push(para("Lesson planning table", { heading: HeadingLevel.HEADING_2 }));
{
  const w = [1500, 2100, 2100, 1900, 1586, 1586];
  children.push(table(w, [
    headerRow(["Weeks / Lesson", "Syllabus content", "Activities", "Resources", "Extension", "Adjustments"], w),
    ...[0, 1].map(() => new TableRow({ children: w.map((cw, i) => cell(i === 0 ? "Wk 1 · L1" : "", { w: cw })) })),
  ]), spacer(200));
}

// Question formats
children.push(para("Question formats", { heading: HeadingLevel.HEADING_2 }));
children.push(
  para([run("1.  ", { bold: true }), run("Multiple-choice question stem goes here."), new TextRun({ text: "\t/1", font: FONT, bold: true, color: C.s[9] })], { style: "Question" }),
  ...["A", "B", "C", "D"].map((l) => para([run(`${l}   `, { bold: true, color: C.s[9] }), run("Option text")], { style: "Option" })),
  spacer(),
  para([run("2.  ", { bold: true }), run("Extended-response question stem goes here."), new TextRun({ text: "\t/2", font: FONT, bold: true, color: C.s[9] })], { style: "Question" }),
  ...[0, 1, 2, 3].map(() => new Paragraph({ style: "WritingLine", children: [] })),
  spacer(),
);
{
  const w = [8772, 2000];
  children.push(table(w, [
    headerRow(["Criteria", "Marks"], w),
    new TableRow({ children: [cell("Outlines how … with relevant detail", { w: w[0] }), cell(para("2", { style: "TableText", align: AlignmentType.CENTER }), { w: w[1] })] }),
    new TableRow({ children: [cell("Provides some relevant information", { w: w[0] }), cell(para("1", { style: "TableText", align: AlignmentType.CENTER }), { w: w[1] })] }),
  ]), spacer(200));
}

// A–E marking criteria (school wording)
children.push(para("Marking criteria (A–E)", { heading: HeadingLevel.HEADING_2 }));
{
  const w = [1400, 9372];
  const grades = [["A", "Extensive"], ["B", "Thorough"], ["C", "Sound"], ["D", "Basic"], ["E", "Elementary"]];
  children.push(table(w, [
    headerRow(["Grade", "Criteria: describe the observable quality of the work"], w),
    ...grades.map(([g, word]) => new TableRow({ children: [
      cell([para([run(g, { bold: true, color: C.s[9], size: 24 })], { style: "TableText" }), para(word, { style: "TableText", color: C.ink })], { w: w[0], fill: C.t[9] }),
      cell("", { w: w[1] }),
    ] })),
  ]), spacer(200));
}

// Domain colour key
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(para("Domain colour key", { heading: HeadingLevel.HEADING_1 }));
children.push(para("Each domain has a strong colour (H) for fills and bars, a tint (T) for panel backgrounds, and a shade (S) for headings and text on the tint. Always print the domain name with its colour: several domains look alike to colour-blind students and on greyscale printouts.", { style: "Normal" }));
{
  const w = [3772, 2400, 2300, 2300];
  children.push(table(w, [
    headerRow(["Domain", "Strong (H) — text colour", "Tint (T)", "Shade (S)"], w, C.s[8]),
    ...DOMAINS.map((d) => new TableRow({ children: [
      cell([para(d.name, { style: "TableText", bold: true, color: C.s[d.n] }), para(d.verbs, { style: "TableSmall" })], { w: w[0], fill: C.t[d.n] }),
      cell(para(`${d.h}  #${C.h[d.n]}  ·  ${onH(d.n) === C.white ? "white" : "ink"} text`, { style: "TableText", color: onH(d.n), bold: true }), { w: w[1], fill: C.h[d.n] }),
      cell(para(`#${C.t[d.n]}`, { style: "TableText" }), { w: w[2], fill: C.t[d.n] }),
      cell(para(`#${C.s[d.n]}`, { style: "TableText", color: C.white, bold: true }), { w: w[3], fill: C.s[d.n] }),
    ] })),
  ]), spacer(160));
}
children.push(
  para("Colour rules", { heading: HeadingLevel.HEADING_3 }),
  new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [run("White text only on jazzberry, bondi blue, denim, twilight and every shade (S). All other strong colours take ink text.")] }),
  new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [run("On a tint, use ink or the matching shade for text and icons, never the matching strong colour.")] }),
  new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [run("Links are denim and underlined; on the periwinkle tint use dark indigo (#201547).")] }),
  new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [run("Knowledge-domain resources default to twilight with a periwinkle tint; don't bring in the full palette unless the content spans several domains.")] }),
);

// ---- styles -----------------------------------------------------------------
const pt = (v) => v * 2; // half-points
const styles = {
  default: { document: { run: { font: FONT, size: pt(10.5), color: C.ink }, paragraph: { spacing: { after: 120, line: 288 } } } },
  paragraphStyles: [
    { id: "Title", name: "Title", basedOn: "Normal", next: "Subtitle", run: { font: "Lato Black", bold: true, size: pt(40), color: C.h[9] }, paragraph: { spacing: { after: 40 } } },
    { id: "Subtitle", name: "Subtitle", basedOn: "Normal", next: "Normal", run: { font: "Lato Light", size: pt(20), color: C.ink }, paragraph: { spacing: { after: 200 } } },
    { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, bold: true, size: pt(18), color: C.h[9] }, paragraph: { spacing: { before: 280, after: 120 }, keepNext: true, outlineLevel: 0 } },
    { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, bold: true, size: pt(14), color: C.ink }, paragraph: { spacing: { before: 240, after: 100 }, keepNext: true, outlineLevel: 1 } },
    { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, bold: true, size: pt(11.5), color: C.s[9] }, paragraph: { spacing: { before: 200, after: 80 }, keepNext: true, outlineLevel: 2 } },
    { id: "Heading4", name: "Heading 4", basedOn: "Normal", next: "Normal", run: { font: FONT, bold: true, size: pt(10.5), color: C.ink }, paragraph: { spacing: { before: 160, after: 60 }, keepNext: true, outlineLevel: 3 } },
    { id: "Heading5", name: "Heading 5", basedOn: "Normal", next: "Normal", run: { font: FONT, bold: true, italics: true, size: pt(10.5), color: C.s[9] }, paragraph: { spacing: { before: 120, after: 60 }, keepNext: true, outlineLevel: 4 } },
    { id: "Heading6", name: "Heading 6", basedOn: "Normal", next: "Normal", run: { font: FONT, italics: true, size: pt(10.5), color: C.ink }, paragraph: { spacing: { before: 120, after: 60 }, keepNext: true, outlineLevel: 5 } },
    { id: "Quote", name: "Quote", basedOn: "Normal", run: { font: "Lato Light", italics: true, size: pt(11), color: C.ink }, paragraph: { indent: { left: 283 }, border: { left: { style: BorderStyle.SINGLE, size: 18, color: C.h[9], space: 8 } }, spacing: { before: 120, after: 160 } } },
    { id: "Meta", name: "Meta", basedOn: "Normal", run: { size: pt(9.5), color: C.ink }, paragraph: { spacing: { after: 40 } } },
    { id: "TableHeading", name: "Table Heading", basedOn: "Normal", run: { bold: true, size: pt(9.5) }, paragraph: { spacing: { after: 0 } } },
    { id: "TableText", name: "Table Text", basedOn: "Normal", run: { size: pt(9.5) }, paragraph: { spacing: { after: 0, line: 264 } } },
    { id: "TableSmall", name: "Table Small", basedOn: "Normal", run: { size: pt(8.5), color: C.ink }, paragraph: { spacing: { after: 0 } } },
    { id: "PanelLabel", name: "Panel Label", basedOn: "Normal", run: { bold: true, size: pt(8.5), characterSpacing: 20 }, paragraph: { spacing: { after: 40 } } },
    { id: "PanelText", name: "Panel Text", basedOn: "Normal", run: { size: pt(10) }, paragraph: { spacing: { after: 40 } } },
    { id: "Question", name: "Question", basedOn: "Normal", run: { size: pt(10.5) }, paragraph: { tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }], spacing: { before: 120, after: 80 } } },
    { id: "Option", name: "Option", basedOn: "Normal", paragraph: { indent: { left: 397 }, spacing: { after: 40 } } },
    { id: "WritingLine", name: "Writing Line", basedOn: "Normal", paragraph: { spacing: { before: 0, after: 0, line: 480 }, border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: C.line, space: 1 } } } },
    { id: "Footer", name: "Footer", basedOn: "Normal", run: { size: pt(8), color: C.muted }, paragraph: { spacing: { after: 0 } } },
  ],
  characterStyles: [
    { id: "Hyperlink", name: "Hyperlink", run: { color: C.h[8], underline: {} } },
    { id: "KeyTerm", name: "Key Term", run: { bold: true, color: C.s[9] } },
  ],
};

const numbering = {
  config: [
    { reference: "bullets", levels: [
      { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } }, run: { color: C.h[9] } } },
      { level: 1, format: LevelFormat.BULLET, text: "–", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 240 } }, run: { color: C.h[9] } } },
    ] },
    { reference: "steps", levels: [
      { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 300 } }, run: { bold: true, color: C.s[9] } } },
    ] },
  ],
};

const doc = new Document({
  creator: "BESTAE",
  title: "BESTAE Word Template",
  description: "BESTAE resource template: Lato, BESTAE colour tokens (29 Sept 2026 palette), A4 print-grid margins.",
  styles,
  numbering,
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: mm(297) }, margin: { ...MARGIN, header: mm(6), footer: mm(6) } } },
    headers: { default: new Header({ children: [new Paragraph({ style: "Footer", tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }], children: [run("BESTAE", { bold: true, color: C.h[9], size: pt(8) }), new TextRun({ text: "\tCourse · Topic", font: FONT, size: pt(8), color: C.muted })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ style: "Footer", tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }], children: [run("Name: ______________________", { size: pt(8), color: C.muted }), new TextRun({ children: ["\tPage ", PageNumber.CURRENT, " of ", PageNumber.TOTAL_PAGES], font: FONT, size: pt(8), color: C.muted })] })] }) },
    children,
  }],
});

const out = path.join(__dirname, "BESTAE Word Template.docx");
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(out, buf); console.log("wrote", out); });
