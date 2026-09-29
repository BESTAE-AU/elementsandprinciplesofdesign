#!/usr/bin/env python3
"""Typography maths helpers for the typography skills (standard library only).

Commands:
  convert <value><unit>          One size in pt, px, rem, pica, mm and inches.
                                 Units: pt, px, rem, em, pica (pc), mm, in.
  scale   --base N --ratio R     A modular type scale (body up to display),
                                 with suggested leading and tracking per step.
                                 R is a number or a name: minor-second,
                                 major-second, minor-third, major-third,
                                 perfect-fourth, augmented-fourth,
                                 perfect-fifth, golden.
  leading <size>                 Leading range (120-150%) for one text size,
                                 plus where on that range the size should sit.
  measure --width W --size S     Approximate characters per line for a column,
                                 and the width range that gives 45-75 chars.
                                 Width in mm (print, size in pt) or px (screen,
                                 size in px): add --screen for px.
  contrast <fg> <bg>             WCAG 2.x contrast ratio for a text colour on a
                                 background, with body/large-text verdicts.

Add --json to any command for machine-readable output.

Unit facts used (CSS / PostScript definitions):
  1 in = 72 pt = 96 px = 6 pica = 25.4 mm, so 1 px = 0.75 pt and 16 px = 12 pt.
  1 rem = the root font size (browser default 16 px).
"""
import argparse
import json
import re
import sys

PT_PER = {"pt": 1.0, "px": 0.75, "pica": 12.0, "pc": 12.0, "in": 72.0,
          "mm": 72 / 25.4}
RATIOS = {
    "minor-second": 1.067, "major-second": 1.125, "minor-third": 1.2,
    "major-third": 1.25, "perfect-fourth": 1.333, "augmented-fourth": 1.414,
    "perfect-fifth": 1.5, "golden": 1.618,
}
STEP_NAMES = ["Body", "H6 / large body", "H5", "H4", "H3", "H2", "H1",
              "Display", "Display 2", "Display 3"]
# Average lowercase character width as a fraction of the font size. About 0.5
# for typical text faces; narrow faces sit nearer 0.45 and wide ones 0.55.
AVG_CHAR_EM = 0.5


def out(data, as_json, lines):
    if as_json:
        print(json.dumps(data, indent=2))
    else:
        print("\n".join(lines))


def parse_size(text, root=16.0):
    m = re.fullmatch(r"\s*([0-9]*\.?[0-9]+)\s*([a-zA-Z]+)\s*", text)
    if not m:
        sys.exit(f"Could not read size '{text}'. Use e.g. 12pt, 16px, 1.5rem, 90mm.")
    value, unit = float(m.group(1)), m.group(2).lower()
    if unit in ("rem", "em"):
        return value * root * 0.75
    if unit not in PT_PER:
        sys.exit(f"Unknown unit '{unit}'. Use pt, px, rem, em, pica, mm or in.")
    return value * PT_PER[unit]


def cmd_convert(a):
    pt = parse_size(a.value, a.root)
    data = {"pt": round(pt, 3), "px": round(pt / 0.75, 3),
            "rem": round(pt / 0.75 / a.root, 4), "pica": round(pt / 12, 3),
            "mm": round(pt * 25.4 / 72, 3), "in": round(pt / 72, 4)}
    lines = [f"{a.value} =",
             f"  {data['pt']} pt   {data['px']} px   {data['rem']} rem (root {a.root:g} px)",
             f"  {data['pica']} pica   {data['mm']} mm   {data['in']} in"]
    out(data, a.json, lines)


def leading_factor(size_px):
    """Inverse relationship: small text needs looser leading, display text tighter."""
    if size_px <= 14:
        return 1.5
    if size_px <= 20:
        return 1.45
    if size_px <= 28:
        return 1.3
    if size_px <= 40:
        return 1.2
    if size_px <= 60:
        return 1.1
    return 1.0


def tracking_em(size_px):
    """Suggested letter-spacing in em: loosen tiny text, tighten big headings."""
    if size_px < 12:
        return 0.02
    if size_px <= 20:
        return 0.0
    if size_px <= 40:
        return -0.01
    return -0.02


def cmd_scale(a):
    ratio = RATIOS.get(a.ratio.lower()) if not re.fullmatch(r"[0-9.]+", a.ratio) else float(a.ratio)
    if not ratio:
        sys.exit(f"Unknown ratio '{a.ratio}'. Use a number or one of: {', '.join(RATIOS)}")
    unit = a.unit
    to_px = 1.0 if unit == "px" else 1 / 0.75
    rows = []
    for i in range(a.steps):
        size = a.base * ratio ** i
        px = size * to_px
        lf = leading_factor(px)
        rows.append({"step": i, "name": STEP_NAMES[i] if i < len(STEP_NAMES) else f"Step {i}",
                     "size": round(size, 1), "unit": unit,
                     "rem": round(px / a.root, 3),
                     "leading": round(size * lf, 1), "leading_pct": int(lf * 100),
                     "tracking_em": tracking_em(px),
                     "tracking_indesign": int(tracking_em(px) * 1000)})
    if a.small:
        size = a.base / ratio
        px = size * to_px
        rows.insert(0, {"step": -1, "name": "Caption / label", "size": round(size, 1),
                        "unit": unit, "rem": round(px / a.root, 3),
                        "leading": round(size * leading_factor(px), 1),
                        "leading_pct": int(leading_factor(px) * 100),
                        "tracking_em": tracking_em(px),
                        "tracking_indesign": int(tracking_em(px) * 1000)})
    lines = [f"Type scale: base {a.base:g}{unit}, ratio {ratio:g}",
             f"{'Role':<16}{'Size':>8}{'rem':>8}{'Leading':>10}{'%':>6}{'Track em':>10}{'InDesign':>10}"]
    for r in reversed(rows):
        lines.append(f"{r['name']:<16}{r['size']:>6}{unit:<2}{r['rem']:>8}{r['leading']:>8}{unit:<2}"
                     f"{r['leading_pct']:>6}{r['tracking_em']:>10}{r['tracking_indesign']:>10}")
    lines.append("Round sizes to whole or half points/pixels for the final spec. "
                 "InDesign tracking is in 1/1000 em.")
    out({"base": a.base, "ratio": ratio, "unit": unit, "steps": rows}, a.json, lines)


def cmd_leading(a):
    pt = parse_size(a.size, a.root)
    px = pt / 0.75
    lf = leading_factor(px)
    unit = "px" if a.size.strip().lower().endswith("px") else "pt"
    size = px if unit == "px" else pt
    data = {"size": round(size, 2), "unit": unit, "min_120": round(size * 1.2, 1),
            "max_150": round(size * 1.5, 1), "suggested": round(size * lf, 1),
            "suggested_pct": int(lf * 100)}
    lines = [f"Leading for {a.size}: 120-150% = {data['min_120']}-{data['max_150']} {unit}",
             f"Suggested for this size: {data['suggested']} {unit} ({data['suggested_pct']}%). "
             "Bigger text wants tighter leading; small body text wants the loose end.",
             "Nudge looser for long lines, large x-height faces or light-on-dark text."]
    out(data, a.json, lines)


def cmd_measure(a):
    if a.screen:
        char_w = a.size * AVG_CHAR_EM          # px
        chars = a.width / char_w
        lo, hi = 45 * char_w, 75 * char_w
        unit = "px"
    else:
        char_w = a.size * AVG_CHAR_EM * 25.4 / 72  # pt -> mm
        chars = a.width / char_w
        lo, hi = 45 * char_w, 75 * char_w
        unit = "mm"
    verdict = ("too short: choppy, lots of hyphens" if chars < 45 else
               "too long: the eye loses the next line" if chars > 75 else "comfortable")
    data = {"chars_per_line": round(chars), "verdict": verdict,
            "width_for_45": round(lo, 1), "width_for_66": round(66 * char_w, 1),
            "width_for_75": round(hi, 1), "unit": unit}
    lines = [f"About {data['chars_per_line']} characters per line ({verdict}).",
             f"For 45-75 characters use {data['width_for_45']}-{data['width_for_75']} {unit} "
             f"(about 66 chars at {data['width_for_66']} {unit}).",
             "Estimate assumes an average text face. Check by counting a real line; "
             "CSS can cap it with max-width: 66ch."]
    out(data, a.json, lines)


def parse_colour(text):
    t = text.strip()
    m = re.fullmatch(r"#?([0-9a-fA-F]{6})", t)
    if m:
        h = m.group(1)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.fullmatch(r"#?([0-9a-fA-F]{3})", t)
    if m:
        return tuple(int(c * 2, 16) for c in m.group(1))
    nums = re.findall(r"\d+", t)
    if len(nums) == 3:
        return tuple(int(n) for n in nums)
    sys.exit(f"Could not read colour '{text}'. Use #RRGGBB or r,g,b.")


def luminance(rgb):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def cmd_contrast(a):
    l1, l2 = luminance(parse_colour(a.fg)), luminance(parse_colour(a.bg))
    ratio = (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)
    data = {"ratio": round(ratio, 2),
            "body_AA_4.5": ratio >= 4.5, "body_AAA_7": ratio >= 7,
            "large_AA_3": ratio >= 3, "large_AAA_4.5": ratio >= 4.5}
    yes = lambda b: "pass" if b else "FAIL"
    lines = [f"{a.fg} on {a.bg}: {ratio:.2f}:1",
             f"  Body text   AA 4.5:1 {yes(data['body_AA_4.5'])}   AAA 7:1 {yes(data['body_AAA_7'])}",
             f"  Large text  AA 3:1 {yes(data['large_AA_3'])}   AAA 4.5:1 {yes(data['large_AAA_4.5'])}",
             "  Large = at least 18 pt (24 px) regular or 14 pt (about 18.7 px) bold."]
    out(data, a.json, lines)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--json", action="store_true")
    p.add_argument("--root", type=float, default=16.0, help="root font size in px for rem (default 16)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("convert"); s.add_argument("value"); s.set_defaults(f=cmd_convert)
    s = sub.add_parser("scale")
    s.add_argument("--base", type=float, default=16)
    s.add_argument("--ratio", default="major-third")
    s.add_argument("--steps", type=int, default=6)
    s.add_argument("--unit", choices=["px", "pt"], default="px")
    s.add_argument("--small", action="store_true", help="add one caption/label step below body")
    s.set_defaults(f=cmd_scale)
    s = sub.add_parser("leading"); s.add_argument("size"); s.set_defaults(f=cmd_leading)
    s = sub.add_parser("measure")
    s.add_argument("--width", type=float, required=True)
    s.add_argument("--size", type=float, required=True)
    s.add_argument("--screen", action="store_true")
    s.set_defaults(f=cmd_measure)
    s = sub.add_parser("contrast"); s.add_argument("fg"); s.add_argument("bg"); s.set_defaults(f=cmd_contrast)

    # Allow --json / --root after the subcommand too.
    argv = sys.argv[1:]
    glob = [x for x in argv if x == "--json"]
    rest = [x for x in argv if x != "--json"]
    a = p.parse_args(glob + rest)
    a.f(a)


if __name__ == "__main__":
    main()
