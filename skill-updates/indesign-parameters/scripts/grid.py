#!/usr/bin/env python3
"""Whole-number 12 x 12 grid presets for InDesign Parameters (mm for print, px for digital).

Usage:
  python3 grid.py                      # list all sizes and presets
  python3 grid.py A4P A                # full spec for one preset
  python3 grid.py A3L C --cols 8 --rows 3   # size of a frame spanning 8 cols x 3 rows
  python3 grid.py A3P C --cols 6 --booklet   # booklet width (some A3 booklets use a narrower column)
  python3 grid.py PRES C --cols 4 --rows 6    # digital sizes work the same way (px)
  python3 grid.py A4L A --half 3.5          # distance from top margin to row line 3.5 (half rows)
  python3 grid.py --styles A4P A [--booklet] # object style widths and X positions
  python3 grid.py --type A4P A [--font "Avenir Next"] [--heavy Bold] [--light Thin]   # heading sizes (default font Lato)
  python3 grid.py --body A4P A [--font NAME]   # Body, Body Condensed, Body Small leading and lines per row
  python3 grid.py --contrast-hex "#FFFFFF" "#326295"   # WCAG contrast for screen/domain colours
  python3 grid.py --domains [slug]              # text colour + ratio for every domain colour
  python3 grid.py --library                 # full object style list (regenerates references/object-styles.md)
  python3 grid.py --markdown SIZE      # regenerate references/<size>.md tables
"""
import sys

# size: (name, width, height)
SIZES = {
    "A4P": ("A4 portrait", 210, 297),
    "A4L": ("A4 landscape", 297, 210),
    "A3P": ("A3 portrait", 297, 420),
    "A3L": ("A3 landscape", 420, 297),
}

# (col, col gutter, row, row gutter, sheet L, sheet R,
#  booklet inside, booklet outside, booklet col, top, bottom)
# booklet col differs from col only where the sheet margins are too small for binding.
PRESETS = {
    "A4P": {
        "A": (14, 2, 20, 3, 10, 10, 12, 8, 14, 12, 12),
        "B": (13, 3, 20, 3, 10, 11, 12, 9, 13, 12, 12),
        "C": (12, 4, 19, 4, 11, 11, 13, 9, 12, 12, 13),
        "D": (10, 6, 17, 6, 12, 12, 14, 10, 10, 13, 14),
    },
    "A4L": {
        "A": (21, 2, 13, 3, 11, 12, 13, 10, 21, 10, 11),
        "B": (20, 3, 13, 3, 12, 12, 14, 10, 20, 10, 11),
        "C": (19, 4, 12, 4, 12, 13, 14, 11, 19, 11, 11),
        "D": (17, 6, 10, 6, 13, 14, 15, 12, 17, 12, 12),
    },
    "A3P": {
        "A": (21, 2, 30, 4, 11, 12, 13, 10, 21, 8, 8),
        "B": (20, 3, 28, 6, 12, 12, 14, 10, 20, 9, 9),
        "C": (17, 7, 27, 7, 8, 8, 16, 12, 16, 9, 10),
        "D": (16, 8, 26, 8, 8, 9, 17, 12, 15, 10, 10),
    },
    "A3L": {
        "A": (30, 4, 21, 2, 8, 8, 16, 12, 29, 11, 12),
        "B": (28, 6, 20, 3, 9, 9, 17, 13, 27, 12, 12),
        "C": (27, 7, 17, 7, 9, 10, 18, 13, 26, 8, 8),
        "D": (26, 8, 16, 8, 10, 10, 12, 8, 26, 8, 9),
    },
}
# Digital (pixels). Margins equal on all sides, gutters equal both ways.
# size: (name, width, height); preset: (col, col gutter, row, row gutter, left, right, top, bottom)
DIGITAL_SIZES = {
    "PRES": ("Presentation 1920 × 1080 (16:9)", 1920, 1080),
}
DIGITAL = {
    "PRES": {
        "A": (135, 10, 65, 10, 95, 95, 95, 95),
        "B": (125, 20, 55, 20, 100, 100, 100, 100),
        "C": (115, 30, 45, 30, 105, 105, 105, 105),
        "D": (105, 40, 35, 40, 110, 110, 110, 110),
    },
}

NAMES = {"A": "Standard", "B": "Even 3", "C": "Medium", "D": "Open"}
N = 12


def span(module, gutter, n):
    return n * module + (n - 1) * gutter


def check(size, key):
    _, W, H = SIZES[size]
    c, cg, r, rg, l, rt, i, o, bc, t, b = PRESETS[size][key]
    assert l + span(c, cg, N) + rt == W, (size, key, "sheet width")
    assert i + span(bc, cg, N) + o == W, (size, key, "booklet width")
    assert i >= 12 and o >= 8, (size, key, "booklet margins too small for binding")
    assert t + span(r, rg, N) + b == H, (size, key, "height")
    assert i > o, (size, key, "booklet inside must exceed outside")


def half_row(row, gutter, step=1):
    """Half module and half-row offset, or None if half rows aren't whole (or whole 5 px)."""
    half = row - gutter
    if half <= 0 or half % (2 * step):
        return None
    return half // 2, half // 2 + gutter


def half_label(v, step=1):
    h = half_row(v[2], v[3], step)
    return f"{h[0]} (line at +{h[1]})" if h else "full rows only"


def check_digital(size, key):
    _, W, H = DIGITAL_SIZES[size]
    c, cg, r, rg, l, rt, t, b = DIGITAL[size][key]
    assert l + span(c, cg, N) + rt == W, (size, key, "width")
    assert t + span(r, rg, N) + b == H, (size, key, "height")
    assert all(v % 5 == 0 for v in DIGITAL[size][key]), (size, key, "digital values must be multiples of 5 px")


def markdown_digital(size):
    name, W, H = DIGITAL_SIZES[size]
    p = DIGITAL[size]
    keys = list(p)
    out = [f"# {name}: grid presets (px)", ""]
    rows = [
        ("Column width", lambda v: v[0]), ("Column gutter", lambda v: v[1]),
        ("Row height", lambda v: v[2]), ("Row gutter", lambda v: v[3]),
        ("Half row: module (line)", lambda v: half_label(v, 5)),
        ("Margins (all sides)", lambda v: v[4]),
        ("Live area (W × H)", lambda v: f"{span(v[0], v[1], N)} × {span(v[2], v[3], N)}"),
        ("Width check", lambda v: f"{v[4]}+{N*v[0]}+{(N-1)*v[1]}+{v[5]} = {W}"),
        ("Height check", lambda v: f"{v[6]}+{N*v[2]}+{(N-1)*v[3]}+{v[7]} = {H}"),
    ]
    out.append("| | " + " | ".join(f"**{k}: {NAMES[k]}**" for k in keys) + " |")
    out.append("|---" * (len(keys) + 1) + "|")
    for label, f in rows:
        out.append(f"| {label} | " + " | ".join(str(f(p[k])) for k in keys) + " |")
    for title, i in [("Widths (px) by number of columns spanned", 0), ("Heights (px) by number of rows spanned", 2)]:
        out += ["", f"## {title}", ""]
        out.append("| Span | " + " | ".join(str(n) for n in range(1, N + 1)) + " |")
        out.append("|---" * (N + 1) + "|")
        for k in keys:
            out.append(f"| {k} | " + " | ".join(str(span(p[k][i], p[k][i + 1], n)) for n in range(1, N + 1)) + " |")
    out += ["", "## Common slide divisions (frame width, px)", ""]
    out.append("| Layout | Grid cols each | " + " | ".join(keys) + " |")
    out.append("|---" * (len(keys) + 2) + "|")
    for label, n in [("Full width", 12), ("2 across", 6), ("3 across", 4), ("4 across", 3), ("6 across", 2)]:
        out.append(f"| {label} | {n} | " + " | ".join(str(span(p[k][0], p[k][1], n)) for k in keys) + " |")
    return "\n".join(out) + "\n"


def markdown(size):
    name, W, H = SIZES[size]
    p = PRESETS[size]
    keys = list(p)
    out = [f"# {name} ({W} × {H} mm): grid presets", ""]
    rows = [
        ("Column width", lambda v: v[0]), ("Column gutter", lambda v: v[1]),
        ("Row height", lambda v: v[2]), ("Row gutter", lambda v: v[3]),
        ("Half row: module (line)", lambda v: half_label(v)),
        ("Single sheet: left / right", lambda v: f"{v[4]} / {v[5]}"),
        ("Booklet: inside / outside", lambda v: f"{v[6]} / {v[7]}"),
        ("Booklet column width", lambda v: v[8] if v[8] == v[0] else f"**{v[8]}** (differs)"),
        ("Top / bottom", lambda v: f"{v[9]} / {v[10]}"),
        ("Live area (W × H)", lambda v: f"{span(v[0], v[1], N)} × {span(v[2], v[3], N)}"),
        ("Width check", lambda v: f"{v[4]}+{N*v[0]}+{(N-1)*v[1]}+{v[5]} = {W}"),
        ("Booklet width check", lambda v: f"{v[6]}+{N*v[8]}+{(N-1)*v[1]}+{v[7]} = {W}"),
        ("Height check", lambda v: f"{v[9]}+{N*v[2]}+{(N-1)*v[3]}+{v[10]} = {H}"),
    ]
    out.append("| | " + " | ".join(f"**{k}: {NAMES[k]}**" for k in keys) + " |")
    out.append("|---" * (len(keys) + 1) + "|")
    for label, f in rows:
        out.append(f"| {label} | " + " | ".join(str(f(p[k])) for k in keys) + " |")
    out += ["", "## Widths (mm) by number of columns spanned (single sheet)", ""]
    out.append("| Span | " + " | ".join(str(n) for n in range(1, N + 1)) + " |")
    out.append("|---" * (N + 1) + "|")
    for k in keys:
        out.append(f"| {k} | " + " | ".join(str(span(p[k][0], p[k][1], n)) for n in range(1, N + 1)) + " |")
    out += ["", "## Heights (mm) by number of rows spanned", ""]
    out.append("| Span | " + " | ".join(str(n) for n in range(1, N + 1)) + " |")
    out.append("|---" * (N + 1) + "|")
    for k in keys:
        out.append(f"| {k} | " + " | ".join(str(span(p[k][2], p[k][3], n)) for n in range(1, N + 1)) + " |")
    out += ["", "## Common page divisions (frame width, mm)", ""]
    out.append("| Layout | Grid cols each | " + " | ".join(keys) + " |")
    out.append("|---" * (len(keys) + 2) + "|")
    for label, n in [("Full width", 12), ("2 across", 6), ("3 across", 4), ("4 across", 3), ("6 across", 2), ("12 across", 1)]:
        out.append(f"| {label} | {n} | " + " | ".join(str(span(p[k][0], p[k][1], n)) for k in keys) + " |")
    return "\n".join(out) + "\n"


# Object style library: every span (1-12 columns) at every start column = 78 styles.
# Each goes in the coarsest division it lines up with (2, 3, 4, 6 Columns); anything
# that only lines up with single columns goes in 12 Columns, sub-foldered by fraction.
FOLDER_ORDER = [2, 3, 4, 6, 12]


def fraction(n):
    from fractions import Fraction
    f = Fraction(n, 12)
    return "Full Width" if f == 1 else f"{f.numerator}/{f.denominator}"


def position(first, n):
    last = first + n - 1
    if first == 1:
        return "Left"
    if last == 12:
        return "Right"
    if first - 1 == 12 - last:
        return "Centre"
    return f"Col {first}" if n == 1 else f"Cols {first}–{last}"


def style_library():
    lib = [("", "Full Width", 1, 12)]
    rows = []
    for n in range(1, 12):
        for first in range(1, 14 - n):
            for d in FOLDER_ORDER:
                unit = 12 // d
                if (first - 1) % unit == 0 and n % unit == 0:
                    folder = f"{d} Columns"
                    if d == 12:
                        folder += f" › {fraction(n)}"
                    rows.append((FOLDER_ORDER.index(d), n, first, folder,
                                 f"{fraction(n)} Page – {position(first, n)}"))
                    break
    rows.sort()
    lib += [(folder, name, first, n) for _, n, first, folder, name in rows]
    return lib


STYLE_LIBRARY = style_library()


def library_markdown():
    out = ["# Object style library: 12-column grid", "",
           f"{len(STYLE_LIBRARY)} position styles, all Based On `Text – Grid`. Column ranges are the same "
           "for every size and preset. Get widths and X offsets with `python3 scripts/grid.py --styles SIZE PRESET`.", "",
           "| Folder | Style | Columns | Span |", "|---|---|---|---|"]
    for folder, name, first, n in STYLE_LIBRARY:
        cols = str(first) if n == 1 else f"{first}–{first + n - 1}"
        out.append(f"| {folder or '(top level)'} | {name} | {cols} | {n} |")
    return "\n".join(out) + "\n"


def styles(size, key, booklet=False):
    table = DIGITAL if size in DIGITAL else PRESETS
    unit = "px" if size in DIGITAL else "mm"
    v = table[size][key]
    c, cg = v[0], v[1]
    if booklet and table is PRESETS:
        c = v[8]
    out = [f"Object styles for {size} {key}{' booklet' if booklet else ''} (based on 'Text – Grid'; "
           f"X measured from the page margin, left reference point)", "",
           "| Folder | Style | Columns | Width | X from margin |", "|---|---|---|---|---|"]
    for folder, name, first, n in STYLE_LIBRARY:
        cols = str(first) if n == 1 else f"{first}–{first + n - 1}"
        out.append(f"| {folder or '(top level)'} | {name} | {cols} | {span(c, cg, n)} {unit} | {(first - 1) * (c + cg)} {unit} |")
    return "\n".join(out)


# Heading paragraph styles: (name, lines, rows). Visible gap between lines = row gutter,
# so cap height = (rows x row + (rows - 1) x gutter - (lines - 1) x gutter) / lines.
TYPE_STYLES = [
    ("Title", 1, 1),
    ("Subheading", 2, 1),
    ("Heading 1", 3, 2),
    ("Heading 2", 2, 1),
    ("Heading 3", 3, 1),
    ("Heading 4", 4, 1),
    ("Heading 5", 5, 1),
]
MM_TO_PT = 72 / 25.4

# Fonts and their per-weight cap ratios live in references/fonts.json (default: Lato).
# Add a font with scripts/fontcaps.py --save.
import json
import os
FONTS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "fonts.json")))


def font_entry(font=None):
    name = font or FONTS["default"]
    for known, entry in FONTS["fonts"].items():
        if known.lower().replace(" ", "") == name.lower().replace(" ", ""):
            return known, entry
    sys.exit(f"{name} isn't in references/fonts.json yet. Add it first: "
             f"python3 scripts/fontcaps.py --find \"{name}\" --save  (or --google, or pass the font files)")
MIN_CAP = {"mm": 1.4, "px": 10}  # below this a heading is too small to read (about 6 pt / 14 px type)


def type_scale(size, key, font=None, heavy=None, light=None):
    table = DIGITAL if size in DIGITAL else PRESETS
    unit = "px" if size in DIGITAL else "mm"
    v = table[size][key]
    r, g = v[2], v[3]
    family, entry = font_entry(font)
    heavy, light = heavy or entry["heavy"], light or entry["light"]
    for w in (heavy, light):
        if w not in entry["weights"]:
            sys.exit(f"{family} has no '{w}' weight. Available: {', '.join(entry['weights'])}")
    out = [f"Heading styles for {size} {key} (row {r}, gutter {g} {unit}), all caps, {family} {heavy} / Subheading {family} {light}", "",
           f"| Style | Font | Lines in rows | Cap height ({unit}) | Font size | Leading | Stays on grid | Status |", "|---|---|---|---|---|---|---|---|"]
    for name, lines, rows in TYPE_STYLES:
        weight = light if name == "Subheading" else heavy
        cap_ratio = entry["weights"][weight]["cap"]
        cap = (span(r, g, rows) - (lines - 1) * g) / lines
        # Leading = cap + gutter = rows x (row + gutter) / lines, the same lock-to-rows rule as
        # body text. Rounded to 1 decimal; on print the rounding error is checked the same way
        # as body text (drift <= MAX_DRIFT_MM), measured over the heading's own lines.
        exact_lead = (cap + g) * (MM_TO_PT if unit == "mm" else 1)
        size_v = round(cap / cap_ratio * (MM_TO_PT if unit == "mm" else 1), 1)
        lead_v = round(exact_lead, 1)
        tu = "pt" if unit == "mm" else "px"
        err = abs(lead_v - exact_lead)
        if unit == "mm":
            block = err * (lines - 1) / MM_TO_PT
            max_lines = MAX_DRIFT_MM * MM_TO_PT / err if err > 1e-9 else float("inf")
            rows_ok = max_lines * rows / lines
            stays = "any length" if rows_ok >= 12 else f"{int(rows_ok)} rows ({int(max_lines)} lines)"
            lead_ok = block <= MAX_DRIFT_MM
        else:
            stays = "any length" if err < 1e-9 else "not exact"
            lead_ok = err < 1e-9
        if cap <= 0:
            status = "impossible (gutter too big for row)"
        elif cap < MIN_CAP[unit]:
            status = "too small to read"
        elif not lead_ok:
            status = "leading isn't whole/1 decimal"
        else:
            status = "ok"
        if cap <= 0:
            out.append(f"| {name} | {family} {weight} | {lines} in {rows} | {cap:.3f} | – | – | – | {status} |")
        else:
            out.append(f"| {name} | {family} {weight} | {lines} in {rows} | {cap:.3f} | {size_v:g} {tu} | {lead_v:g} {tu} | {stays} | {status} |")
    return "\n".join(out)


# Body text styles (print). Leading locks to the grid: n lines per k rows (k = 1, else 2),
# so leading = k x (row + gutter) / n. n is chosen for leading closest to the target ratio
# within the style's comfortable range.
# (name, size pt, target leading ratio, allowed range, tracking)
BODY_STYLES = [
    ("Body", 12, 1.35, (1.20, 1.50), 0),
    ("Body Condensed", 12, 1.15, (1.05, 1.25), -10),
    ("Body Small", 10, 1.35, (1.20, 1.50), 0),
]
# Slides (px; InDesign treats 1 px = 1 pt in pixel documents). Nothing under 16 px.
BODY_STYLES_DIGITAL = [
    ("Body", 18, 1.35, (1.20, 1.50), 0),
    ("Body Condensed", 18, 1.15, (1.05, 1.25), -10),
    ("Body Small", 16, 1.35, (1.20, 1.50), 0),
]


MAX_DRIFT_MM = 0.25   # print: allowed drift from rounding leading, over a full page of text
ROW_PENALTY = 0.03    # prefer fitting lines into fewer rows


def body_fit(pitch, pt, target, rng, digital=False, page_rows=12):
    """Best (n lines, k rows, leading, drift mm) with leading a whole number or 1 decimal.

    Slides (px): leading must be exactly whole or 1 decimal.
    Print (pt): leading is rounded to 1 decimal; allowed only if the rounding drifts less than
    MAX_DRIFT_MM from the rows over a full page (12 rows) of text.
    Scored by closeness to the target ratio, with a small penalty per extra row in the cycle.
    """
    best = None
    for k in (1, 2, 3, 4):
        for n in range(1, 100):
            exact = k * pitch / n
            if not rng[0] <= exact / pt <= rng[1]:
                continue
            lead = round(exact, 1)
            if digital:
                if abs(lead - exact) > 1e-9:
                    continue
                drift = 0.0
            else:
                drift = abs(lead - exact) * (page_rows * n / k) / MM_TO_PT
                if drift > MAX_DRIFT_MM:
                    continue
            score = abs(lead / pt - target) + ROW_PENALTY * (k - 1)
            if best is None or score < best[0]:
                best = (score, n, k, lead, drift)
    return best[1:] if best else None


def body_text(size, key, font=None):
    digital = size in DIGITAL
    v = (DIGITAL if digital else PRESETS)[size][key]
    unit = "px" if digital else "mm"
    pitch = v[2] + v[3]
    pitch_type = pitch if digital else pitch * MM_TO_PT   # in px or pt
    tu = "px" if digital else "pt"
    family, entry = font_entry(font)
    out = [f"Body text for {size} {key} in {family} Regular (row {v[2]} + gutter {v[3]} = {pitch} {unit}"
           + ("" if digital else f" = {pitch_type:.3f} pt") + " per row)", "",
           "| Style | Size | Tracking | Lines | Leading | Of size |", "|---|---|---|---|---|---|"]
    for name, pt, target, rng, track in (BODY_STYLES_DIGITAL if digital else BODY_STYLES):
        fit = body_fit(pitch_type, pt, target, rng, digital)
        if not fit:
            out.append(f"| {name} | {pt} {tu} | {track} | – | no whole/1-decimal fit | – |")
            continue
        n, k, lead, drift = fit
        rows = "1 row" if k == 1 else f"{k} rows"
        extra = "" if digital else f" (drift {drift:.2f} mm/page)"
        out.append(f"| {name} | {pt:g} {tu} | {track} | {n} per {rows} | {lead:g} {tu}{extra} | {lead / pt:.0%} |")
    return "\n".join(out)


# ---------------------------------------------------------------- full style sheet
LEAD = {"print": (16, 1.30, (1.20, 1.45)), "digital": (24, 1.30, (1.20, 1.45))}
PULL_QUOTE = {"print": (24, 1.25, (1.15, 1.40)), "digital": (36, 1.25, (1.15, 1.40))}
LEAD_ROWS = 4          # lead paragraphs and quotes are short: drift checked over 4 rows
ANSWER_AIM_MM = 10     # answer lines: spacing closest to 10 mm, within 8-12 mm
INDENT = {"print": {"bullet": 5, "numbered": 7}, "digital": {"bullet": 20, "numbered": 30}}


def answer_lines(pitch_mm):
    best = None
    for n in range(1, 8):
        gap = pitch_mm / n
        exact = gap * MM_TO_PT
        lead = round(exact, 1)
        drift = abs(lead - exact) * 12 * n / MM_TO_PT
        if 8 <= gap <= 12 and drift <= MAX_DRIFT_MM:
            if best is None or abs(gap - ANSWER_AIM_MM) < abs(best[1] - ANSWER_AIM_MM):
                best = (n, gap, lead)
    return best


def style_sheet(size, key, font=None):
    digital = size in DIGITAL
    v = (DIGITAL if digital else PRESETS)[size][key]
    c, cg, r, rg = v[0], v[1], v[2], v[3]
    pitch = r + rg
    ptype = pitch if digital else pitch * MM_TO_PT
    tu, du = ("px", "px") if digital else ("pt", "mm")
    family, entry = font_entry(font)
    heavy, light = entry["heavy"], entry["light"]
    bold = "Bold" if "Bold" in entry["weights"] else heavy
    bodies = {name: (pt, track, body_fit(ptype, pt, t, rng, digital))
              for name, pt, t, rng, track in (BODY_STYLES_DIGITAL if digital else BODY_STYLES)}

    def bl(name):
        pt, track, fit = bodies[name]
        return f"{pt:g} / {fit[2]:g} {tu}" if fit else f"{pt:g} {tu} / no fit"

    ind = INDENT["digital" if digital else "print"]
    col_x = lambda n: n * (c + cg)          # X of column n + 1, from the margin
    lp, la, lr = LEAD["digital" if digital else "print"]
    lead_fit = body_fit(ptype, lp, la, lr, digital, LEAD_ROWS)
    lead_s = (f"{lp} / {lead_fit[2]:g} {tu} ({lead_fit[0]} per {lead_fit[1]} row{'s' if lead_fit[1] > 1 else ''})"
              if lead_fit else "no fit")
    # Pull quote is sentence case, so it's sized like body text (not by cap height like the
    # all-caps headings): descenders need real space between lines.
    qp, qa, qr = PULL_QUOTE["digital" if digital else "print"]
    q_fit = body_fit(ptype, qp, qa, qr, digital, LEAD_ROWS)
    pq_s = (f"{qp} / {q_fit[2]:g} {tu} ({q_fit[0]} per {q_fit[1]} row{'s' if q_fit[1] > 1 else ''})"
            if q_fit else "no fit")
    small = bl("Body Small")
    li = lambda name, based, fit, left, first, marker: (
        f"| {name} | {based} | {bl(fit)} | {left} {du} | −{first} {du} | {left} {du} | {marker} |")
    out = [f"# Paragraph and character styles: {size} {key} ({family})", "",
           "Values follow SKILL.md section 7. Sizes and leading are whole or 1 decimal and lock to the rows.", "",
           "## Headings", "", type_scale(size, key, font), "",
           "## Body", "", body_text(size, key, font), "",
           "## Lists", "",
           "Space Between Paragraphs Using Same Style 0; Space After one line (the style's leading).", "",
           "| Style | Based on | Size / leading | Left indent | First line | Tab | Marker |",
           "|---|---|---|---|---|---|---|",
           li("Bullet", "Body", "Body", ind["bullet"], ind["bullet"], "•"),
           li("Bullet Level 2", "Bullet", "Body", 2 * ind["bullet"], ind["bullet"], "– (en dash)"),
           li("Numbered", "Body", "Body", ind["numbered"], ind["numbered"], "1. 2. 3."),
           li("Numbered Level 2", "Numbered", "Body", 2 * ind["numbered"], ind["numbered"], "a. b. c."),
           li("Bullet Condensed", "Body Condensed", "Body Condensed", ind["bullet"], ind["bullet"], "•"),
           li("Numbered Condensed", "Body Condensed", "Body Condensed", ind["numbered"], ind["numbered"], "1. 2. 3."),
           li("Checklist", "Bullet", "Body", ind["numbered"], ind["numbered"], "□ (U+25A1)"),
           li("Step", "Numbered", "Body", col_x(1), col_x(1), f"\"Step 1\" in {family} {bold}"),
           li("Definition", "Body", "Body", col_x(2), col_x(2), f"term in {family} {bold}, then tab"),
           "", "## Supporting", "",
           "| Style | Font | Size / leading | Case / tracking |", "|---|---|---|---|",
           f"| Lead | {family} {light} | {lead_s} | Sentence case |",
           f"| Caption | {family} {light} | {small} | Sentence case |",
           f"| Label | {family} {heavy} | {small} | ALL CAPS, tracking +100 |",
           f"| Pull Quote | {family} {light} Italic | {pq_s} | Sentence case |",
           f"| Block Quote | {family} Italic | {bl('Body')}, left indent {col_x(1)} {du} | Sentence case |",
           f"| Footnote | {family} Regular | {small} | Sentence case |"]
    if not digital:
        ans = answer_lines(pitch)
        ans_s = f"{ans[2]:g} pt leading = {ans[1]:.4g} mm apart, {ans[0]} per row" if ans else "no fit"
        out += ["", "## Worksheet", "",
                "| Style | Settings |", "|---|---|",
                "| Learning Intention / Success Criteria | Label style; the list below uses Checklist |",
                f"| Question | Numbered, {family} {bold}, {bl('Body')}, right indent tab for marks, Keep with Next |",
                f"| Question Part | Numbered Level 2, {family} Regular, {bl('Body')}, (a) (b) (c), right indent tab for marks |",
                f"| Instruction | Body, {family} Italic, {bl('Body')} |",
                f"| Answer Line | empty paragraph, Paragraph Rule Below 0.5 pt solid black, offset 0, column width; {ans_s} |",
                "", "## Page (parent pages, in the bottom margin)", "",
                "| Style | Settings |", "|---|---|",
                f"| Page Number | {family} {bold}, {small}, outside edge of the live area |",
                f"| Running Footer | {family} Regular, {small}, inside/left edge of the live area |"]
    body_pt = bodies["Body"][0]
    out += ["", "## Character styles", "",
            "| Style | Settings |", "|---|---|",
            f"| Bold | {family} {bold} |",
            f"| Italic | {family} Italic |",
            f"| Key Term | {family} {bold}, K 100, on a K 20 highlight: Underline On, weight {body_pt + 1:g} {tu}, "
            f"offset −{round(body_pt * 0.3, 1):g} {tu}, colour K 20 (for {body_pt:g} {tu} text) |",
            "| Link | Underline 0.5 pt, offset 1.5 pt, K 100 |",
            f"| Marks | {family} Regular, {bodies['Body Small'][0]:g} {tu} |",
            f"| Step Label | {family} {bold} (used by the Step numbering) |"]
    # Colour: panels and tables (colour.md). Insets = one gutter: column gutter left/right,
    # row gutter top/bottom.
    out += ["", "## Panels (object styles, folder: Panels)", "",
            f"Frame = exact column span x whole rows, fill as below, Inset Spacing {cg} {du} left/right, "
            f"{rg} {du} top/bottom, Auto-Size off. Text inside uses the highest-contrast colour.", "",
            "| Object style | Fill | Text |", "|---|---|---|",
            "| Accent – K 100 | [Black] (small items only) | Reversed styles (white) |",
            "| Panel – K 90 | K 90 | Reversed styles (white) |",
            "| Panel – K 80 | K 80 | Reversed styles (white) |",
            "| Panel – K 70 | K 70 | Reversed styles (white) |",
            "| Panel – K 20 | K 20 | Normal styles (K 100; secondary K 80) |",
            "| Panel – K 10 (default light panel) | K 10 | Normal styles (K 100; secondary K 80) |",
            "", "## Tables", "",
            "| Style | Settings |", "|---|---|",
            f"| Table Header (paragraph) | {family} {bold}, {bl('Body Condensed')}, ALL CAPS, tracking +25, [Paper] (white) |",
            f"| Table Body (paragraph) | Body Condensed: {bl('Body Condensed')}, tracking −10, K 100 |",
            f"| Table Header (cell) | Fill K 90; inset {cg} {du} left/right, {rg} {du} top/bottom |",
            f"| Table Body (cell) | No fill; same insets; bottom stroke 0.5 pt K 50 |",
            "| Table Body Banded (cell) | Fill K 10 (alternate rows, optional); same insets and stroke |",
            "| Table (table style) | Header rows use Table Header; body rows alternate Table Body / Banded; "
            "columns = exact column spans; row height At Least |"]
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- contrast (greyscale K)
DOT_GAIN = 0.15   # typical mid-tone dot gain; contrast is checked with and without it


def _luminance(k):
    g = 1 - k
    return g / 12.92 if g <= 0.04045 else ((g + 0.055) / 1.055) ** 2.4


def contrast(text_k, bg_k):
    """Worst-case WCAG contrast ratio for K tints (0-100), with and without dot gain."""
    def ratio(a, b):
        la, lb = _luminance(a), _luminance(b)
        return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)
    gain = lambda t: min(1.0, t + DOT_GAIN * 4 * t * (1 - t))
    a, b = text_k / 100, bg_k / 100
    return min(ratio(a, b), ratio(gain(a), gain(b)))


# Domain colours (shared house tokens, references/house-tokens.md section 6): slug -> (domain, H, S, T)
DOMAINS = {
    "critical-thinking": ("Critical Thinking", ("2H TOMATO", "#FF585D"), ("2S ESPRESSO", "#551C25"), ("2T SOFT BLUSH", "#F5DADF")),
    "creative-thinking-problem-solving-and-innovation": ("Creative Thinking, Problem Solving and Innovation",
        ("3H ROYAL ORANGE", "#F19C49"), ("3S DARK LEATHER", "#4F2C1D"), ("3T APRICOT", "#FFDFB4")),
    "communication": ("Communication", ("4H CORN", "#F3EA5D"), ("4S DARK GOLD", "#8A6400"), ("4T BUTTERMILK", "#F7F4A2")),
    "self-management-and-organisation": ("Self-Management and Organisation",
        ("5H LIME", "#C5E86C"), ("5S ZUCCHINI", "#1C4220"), ("5T LIME CREAM", "#E8F6C4")),
    "responsibility-and-stewardship": ("Responsibility and Stewardship",
        ("6H SEAGREEN", "#00B2A2"), ("6S SHERWOOD", "#024638"), ("6T SWANS DOWN", "#D7EFE7")),
    "practical-skills-and-technical-application": ("Practical Skills and Technical Application",
        ("8H DENIM", "#326295"), ("8S NIGHT", "#041E42"), ("8T CRUSHED ICE", "#D2DCE8")),
    "knowledge-and-conceptual-understanding": ("Knowledge and Conceptual Understanding",
        ("9H TWILIGHT", "#514689"), ("9S DARK INDIGO", "#201547"), ("9T PERIWINKLE", "#DCD3E7")),
    "independent-learning-and-collaboration": ("Independent Learning and Collaboration",
        ("10H VALENTINE PINK", "#E56DB1"), ("10S PLUM", "#621244"), ("10T POWDER PINK", "#F7D0E6")),
}


def _hex_luminance(h):
    h = h.lstrip("#")
    rgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (f(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_hex(fg, bg):
    la, lb = _hex_luminance(fg), _hex_luminance(bg)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def best_text(bg):
    """Highest-contrast text colour (black or white) for a background, with its ratio and verdict."""
    w, k = contrast_hex("#FFFFFF", bg), contrast_hex("#000000", bg)
    colour, ratio = ("white", w) if w > k else ("black", k)
    verdict = ("all text" if ratio >= 7 else "large text and graphics only" if ratio >= 4.5
               else "graphics only (3:1)" if ratio >= 3 else "no text")
    return colour, ratio, verdict


def domain_report(slug=None):
    out = ["| Domain | Swatch | Hex | Text | Ratio | Allowed |", "|---|---|---|---|---|---|"]
    for key, (name, *swatches) in DOMAINS.items():
        if slug and key != slug:
            continue
        for sw_name, hx in swatches:
            colour, ratio, verdict = best_text(hx)
            out.append(f"| {name} | {sw_name} | {hx} | {colour} | {ratio:.1f}:1 | {verdict} |")
    return "\n".join(out)


def contrast_report(text_k, bg_k):
    c = contrast(text_k, bg_k)
    verdict = ("AAA 7:1: OK for all text" if c >= 7 else
               "AA 4.5:1: secondary/small text floor only; large text OK" if c >= 4.5 else
               "3:1: large text (18 pt+, or 14 pt+ bold) and meaningful graphics only" if c >= 3 else
               "FAIL: no text or meaningful graphics")
    return f"K {text_k} on K {bg_k}: {c:.1f}:1 (worst case with print dot gain). {verdict}"


def main(argv):
    for s in PRESETS:
        for k in PRESETS[s]:
            check(s, k)
    for s in DIGITAL:
        for k in DIGITAL[s]:
            check_digital(s, k)
    if not argv:
        for s, (name, W, H) in DIGITAL_SIZES.items():
            for k, v in DIGITAL[s].items():
                print(f"{s} {k} {NAMES[k]:<8} {name}  col {v[0]}/{v[1]}  row {v[2]}/{v[3]}  margins {v[4]} px  half rows: {half_label(v, 5)}")
        for s, (name, W, H) in SIZES.items():
            for k, v in PRESETS[s].items():
                print(f"{s} {k} {NAMES[k]:<8} {name:<13} col {v[0]}/{v[1]}  row {v[2]}/{v[3]}  "
                      f"sheet L/R {v[4]}/{v[5]}  booklet {v[6]}/{v[7]} col {v[8]}  T/B {v[9]}/{v[10]}  half rows: {half_label(v)}")
        return
    if argv[0] == "--contrast-hex":
        c = contrast_hex(argv[1], argv[2])
        verdict = ("AAA 7:1: OK for all text" if c >= 7 else "AA 4.5:1: large/secondary text only" if c >= 4.5
                   else "3:1: graphics only" if c >= 3 else "FAIL")
        print(f"{argv[1]} on {argv[2]}: {c:.1f}:1 (WCAG, screen colours). {verdict}")
        return
    if argv[0] == "--domains":
        print(domain_report(argv[1] if len(argv) > 1 else None))
        return
    if argv[0] == "--contrast":
        print(contrast_report(int(argv[1]), int(argv[2])))
        return
    if argv[0] == "--sheet":
        opt = lambda f: argv[argv.index(f) + 1] if f in argv else None
        print(style_sheet(argv[1].upper(), argv[2].upper(), opt("--font")), end="")
        return
    if argv[0] == "--body":
        opt = lambda f: argv[argv.index(f) + 1] if f in argv else None
        print(body_text(argv[1].upper(), argv[2].upper(), opt("--font")))
        return
    if argv[0] == "--type":
        opt = lambda f: argv[argv.index(f) + 1] if f in argv else None
        print(type_scale(argv[1].upper(), argv[2].upper(), opt("--font"), opt("--heavy"), opt("--light")))
        return
    if argv[0] == "--library":
        print(library_markdown(), end="")
        return
    if argv[0] == "--styles":
        print(styles(argv[1].upper(), argv[2].upper(), "--booklet" in argv))
        return
    if argv[0] == "--markdown":
        size = argv[1].upper()
        print(markdown_digital(size) if size in DIGITAL else markdown(size), end="")
        return
    size, key = argv[0].upper(), argv[1].upper()
    table = DIGITAL if size in DIGITAL else PRESETS
    unit = "px" if size in DIGITAL else "mm"
    c, cg, r, rg, *rest = table[size][key]
    if "--half" in argv:
        n = float(argv[argv.index("--half") + 1])
        top = rest[-2]
        whole = int(n)
        if n != whole and not half_row(r, rg, 5 if table is DIGITAL else 1):
            print(f"{size} {key} has no whole-number half rows: use full rows only")
            return
        y = (whole - 1) * (r + rg) + (half_row(r, rg, 5 if table is DIGITAL else 1)[1] if n != whole else 0)
        print(f"row line {n}: {y} {unit} below the top margin, {y + top} {unit} from the top of the page")
        return
    if "--booklet" in argv:
        c = rest[4]
    if "--cols" in argv or "--rows" in argv:
        nc = int(argv[argv.index("--cols") + 1]) if "--cols" in argv else None
        nr = int(argv[argv.index("--rows") + 1]) if "--rows" in argv else None
        if nc: print(f"width  {nc} cols = {span(c, cg, nc)} {unit}")
        if nr: print(f"height {nr} rows = {span(r, rg, nr)} {unit}")
        return
    print(markdown_digital(size) if size in DIGITAL else markdown(size))


if __name__ == "__main__":
    main(sys.argv[1:])
