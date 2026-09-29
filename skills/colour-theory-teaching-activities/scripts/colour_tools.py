#!/usr/bin/env python3
"""Colour maths helpers for the colour-theory skills (standard library only).

Commands:
  convert  <colour>            RGB / HEX / HSB / CMYK for one colour, with the
                               hand-worked base-16 steps for the hex code.
  contrast <colour> <colour>   WCAG contrast ratio for one pair.
  audit    <colour> ...        Contrast matrix for a whole palette, the 3x3
                               luminosity x saturation cell of each colour, and
                               a balance verdict (light + dark, danger zone).
  harmony  <colour> ...        Hue angles on the RYB artist's wheel and the
                               closest named harmony.
  ratio    <colour>=<pct> ...  60-30-10 style ratio bar as text (1000 px bar).
  export   <Name>=<colour> ... --format ase|css|json|gpl|canva --out FILE
                               Swatch file for other tools: .ase loads into
                               Illustrator/Photoshop/InDesign/Express, css for
                               Figma/web, gpl for GIMP/Inkscape/Krita, canva is
                               a plain list for pasting into a Canva brand kit.

A <colour> is '#B834E0', 'B834E0', 'rgb(184,52,224)' or '184,52,224'.
Add --json to any command for machine-readable output.
"""
import argparse
import colorsys
import json
import re
import sys

HEX_DIGITS = "0123456789ABCDEF"


# ---------------------------------------------------------------- parsing
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
    if len(nums) == 3 and all(0 <= int(n) <= 255 for n in nums):
        return tuple(int(n) for n in nums)
    raise ValueError(f"Can't read colour {text!r}: use #RRGGBB or rgb(r,g,b)")


def to_hex(rgb):
    return "#" + "".join(f"{v:02X}" for v in rgb)


# ---------------------------------------------------------------- conversions
def hex_working(rgb):
    """The by-hand method from the Colour Palette Studio video (llA)."""
    lines = []
    for name, v in zip(("Red", "Green", "Blue"), rgb):
        q = v / 16
        first = int(q)
        rem = q - first
        second = round(rem * 16)
        lines.append(
            f"{name} {v}: {v} / 16 = {q:g} -> first digit {first} = "
            f"{HEX_DIGITS[first]}; remainder {rem:g} x 16 = {second} = "
            f"{HEX_DIGITS[second]}  => {HEX_DIGITS[first]}{HEX_DIGITS[second]}"
        )
    return lines


def to_hsb(rgb):
    h, s, v = colorsys.rgb_to_hsv(*(c / 255 for c in rgb))
    return round(h * 360), round(s * 100), round(v * 100)


def to_hsl(rgb):
    h, l, s = colorsys.rgb_to_hls(*(c / 255 for c in rgb))
    return round(h * 360), round(s * 100), round(l * 100)


def to_cmyk(rgb):
    """Naive device-independent CMYK. Real print values come from the ICC
    profile in Illustrator/InDesign, so treat this as an approximation."""
    r, g, b = (c / 255 for c in rgb)
    k = 1 - max(r, g, b)
    if k >= 1:
        return 0, 0, 0, 100
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)
    return tuple(round(x * 100) for x in (c, m, y, k))


# ---------------------------------------------------------------- contrast
def relative_luminance(rgb):
    def lin(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(a, b):
    la, lb = sorted((relative_luminance(a), relative_luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def wcag_label(ratio):
    if ratio >= 7:
        return "AAA text"
    if ratio >= 4.5:
        return "AA text"
    if ratio >= 3:
        return "large text / UI only"
    return "fail"


# ---------------------------------------------------------------- 3x3 grid
def grid_cell(rgb):
    """Place a colour in the Colour Palette Studio 3x3 spectrum grid (oDn):
    luminosity light/medium/dark x saturation muted/midtone/bright.
    Luminosity uses WCAG relative luminance so 'light' and 'dark' line up
    with what actually produces accessible pairs."""
    y = relative_luminance(rgb)
    lum = "light" if y >= 0.45 else "dark" if y <= 0.08 else "medium"
    _, s, v = to_hsb(rgb)
    chroma = s * v / 100  # 0-100, how far from grey
    sat = "bright" if chroma >= 55 else "muted" if chroma < 25 else "midtone"
    danger = lum == "medium" and sat == "midtone"
    return lum, sat, danger


# ---------------------------------------------------------------- harmony
# Map HSB hue (RGB wheel) to the traditional RYB artist's wheel so that
# complements match what students are taught (red/green, blue/orange,
# yellow/purple). Piecewise-linear through the key hues.
_RGB_TO_RYB = [(0, 0), (30, 60), (60, 120), (120, 180), (240, 240),
               (300, 300), (360, 360)]


def ryb_hue(rgb_hue):
    for (x0, y0), (x1, y1) in zip(_RGB_TO_RYB, _RGB_TO_RYB[1:]):
        if x0 <= rgb_hue <= x1:
            return y0 + (rgb_hue - x0) * (y1 - y0) / (x1 - x0)
    return rgb_hue


RYB_NAMES = ["red", "red-orange", "orange", "yellow-orange", "yellow",
             "yellow-green", "green", "blue-green", "blue", "blue-violet",
             "violet", "red-violet"]


def ryb_name(angle):
    return RYB_NAMES[int(((angle + 15) % 360) // 30)]


def ang_dist(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def classify_harmony(rgbs):
    chromatic = []
    neutrals = []
    for c in rgbs:
        h, s, v = to_hsb(c)
        (neutrals if s * v / 100 < 12 else chromatic).append(c)
    angles = sorted({round(ryb_hue(to_hsb(c)[0])) for c in chromatic})
    note = f"{len(neutrals)} neutral(s) ignored" if neutrals else ""
    if not angles:
        return "neutral / achromatic", angles, note
    # cluster hues within 20 degrees into one "family"
    fams = []
    for a in angles:
        if fams and ang_dist(a, fams[-1][-1]) <= 20:
            fams[-1].append(a)
        else:
            fams.append([a])
    if len(fams) > 1 and ang_dist(fams[0][0], fams[-1][-1]) <= 20:
        fams[0] = fams.pop() + fams[0]
    centres = sorted(f[len(f) // 2] for f in fams)
    n = len(centres)
    span = max((ang_dist(a, b) for a in centres for b in centres), default=0)
    tol = 25

    def near(x, target):
        return abs(x - target) <= tol

    if n == 1:
        name = "one colour + neutrals (e.g. one colour + black and white)" if neutrals else "monochromatic"
    elif n == 2:
        d = ang_dist(*centres)
        name = ("complementary" if near(d, 180) else "near-complementary" if d >= 130
                else "analogous" if d <= 60 else "two-colour (no classic harmony)")
    else:
        gaps = sorted(ang_dist(centres[i], centres[(i + 1) % n]) for i in range(n))
        full = sorted((centres[(i + 1) % n] - centres[i]) % 360 for i in range(n))
        if span <= 120:
            name = "analogous"
        elif n == 3 and all(near(g, 120) for g in full):
            name = "triadic"
        elif n == 3 and any(near(ang_dist(a, b), 150) and near(ang_dist(a, c), 150)
                            for a, b, c in _rotations(centres)):
            name = "split-complementary"
        elif n == 4 and all(near(g, 90) for g in full):
            name = "square"
        elif n == 4 and _two_pairs(centres, tol):
            name = "tetradic (rectangle)"
        else:
            name = "free / mixed (no single classic harmony)"
    return name, centres, note


def _rotations(c):
    return [(c[i], c[(i + 1) % 3], c[(i + 2) % 3]) for i in range(3)]


def _two_pairs(c, tol):
    a, b, x, y = c
    for p in ((a, b, x, y), (a, x, b, y), (a, y, b, x)):
        if abs(ang_dist(p[0], p[1]) - 180) <= tol and abs(ang_dist(p[2], p[3]) - 180) <= tol:
            return True
    return False


# ---------------------------------------------------------------- commands
def cmd_convert(args):
    rgb = parse_colour(args.colours[0])
    out = {
        "hex": to_hex(rgb),
        "rgb": f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})",
        "hsb": "hsb({}°, {}%, {}%)".format(*to_hsb(rgb)),
        "hsl": "hsl({}°, {}%, {}%)".format(*to_hsl(rgb)),
        "cmyk_approx": "cmyk({}%, {}%, {}%, {}%)".format(*to_cmyk(rgb)),
        "hex_working": hex_working(rgb),
        "ryb_wheel": ryb_name(ryb_hue(to_hsb(rgb)[0])),
        "grid_cell": "{} {}".format(*grid_cell(rgb)[:2]),
    }
    if args.json:
        return out
    print(f"HEX   {out['hex']}\nRGB   {out['rgb']}\nHSB   {out['hsb']}\n"
          f"HSL   {out['hsl']}\nCMYK  {out['cmyk_approx']}  (approximate - "
          f"confirm with the printer's profile)\nWheel {out['ryb_wheel']}   "
          f"3x3 grid: {out['grid_cell']}\n\nHex by hand:")
    for line in out["hex_working"]:
        print("  " + line)


def cmd_contrast(args):
    a, b = (parse_colour(c) for c in args.colours[:2])
    r = contrast_ratio(a, b)
    out = {"a": to_hex(a), "b": to_hex(b), "ratio": round(r, 2), "wcag": wcag_label(r)}
    if args.json:
        return out
    print(f"{out['a']} vs {out['b']}: {out['ratio']}:1  ({out['wcag']}; "
          f"body text needs 4.5:1)")


def cmd_audit(args):
    cols = [parse_colour(c) for c in args.colours]
    hexes = [to_hex(c) for c in cols]
    cells = [grid_cell(c) for c in cols]
    pairs = []
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            r = contrast_ratio(cols[i], cols[j])
            pairs.append({"a": hexes[i], "b": hexes[j], "ratio": round(r, 2),
                          "wcag": wcag_label(r)})
    pairs.sort(key=lambda p: -p["ratio"])
    has_light = any(c[0] == "light" for c in cells)
    has_dark = any(c[0] == "dark" for c in cells)
    passing = [p for p in pairs if p["ratio"] >= 4.5]
    issues = []
    if len(cols) < 2:
        issues.append("A palette needs at least two colours.")
    if not has_light:
        issues.append("No light colour: add or lighten one toward the light-muted corner.")
    if not has_dark:
        issues.append("No dark colour: add or darken one toward the dark corner.")
    in_danger = [hexes[i] for i, c in enumerate(cells) if c[2]]
    if in_danger:
        issues.append("In the danger zone (medium/midtone): " + ", ".join(in_danger))
    if not passing:
        issues.append("No pair reaches 4.5:1, so there is no accessible text pairing.")
    out = {
        "colours": [{"hex": h, "cell": f"{c[0]} {c[1]}", "danger_zone": c[2]}
                    for h, c in zip(hexes, cells)],
        "pairs": pairs,
        "compliant_pairs": len(passing),
        "balanced": not issues,
        "issues": issues,
    }
    if args.json:
        return out
    print("Colour     3x3 cell")
    for c in out["colours"]:
        print(f"  {c['hex']}  {c['cell']}{'  <- danger zone' if c['danger_zone'] else ''}")
    print("\nPairs (best first)")
    for p in pairs:
        mark = "PASS" if p["ratio"] >= 4.5 else "    "
        print(f"  {mark} {p['a']} / {p['b']}  {p['ratio']:>5}:1  {p['wcag']}")
    print(f"\n{len(passing)} of {len(pairs)} pairs reach 4.5:1.")
    print("Balanced." if not issues else "Issues:\n  - " + "\n  - ".join(issues))


def cmd_harmony(args):
    cols = [parse_colour(c) for c in args.colours]
    name, centres, note = classify_harmony(cols)
    def describe(c):
        h, s_, v = to_hsb(c)
        if s_ * v / 100 < 12:
            return {"hex": to_hex(c), "ryb_angle": None, "name": "neutral", "temperature": "-"}
        a = ryb_hue(h)
        return {"hex": to_hex(c), "ryb_angle": round(a), "name": ryb_name(a), "temperature": _temp(a)}

    out = {
        "harmony": name,
        "hue_families": [{"ryb_angle": a, "name": ryb_name(a)} for a in centres],
        "note": note,
        "per_colour": [describe(c) for c in cols],
    }
    if args.json:
        return out
    for c in out["per_colour"]:
        ang = "  -" if c["ryb_angle"] is None else f"{c['ryb_angle']:>3}"
        print(f"  {c['hex']}  {ang}°  {c['name']:<14} {c['temperature']}")
    print(f"\nClosest harmony: {name}" + (f"  ({note})" if note else ""))


def _temp(angle):
    # RYB wheel: red 0, orange 60, yellow 120, green 180, blue 240, violet 300
    return "warm" if angle < 140 or angle >= 330 else "cool"


def cmd_ratio(args):
    items = []
    for tok in args.colours:
        col, _, pct = tok.partition("=")
        items.append((to_hex(parse_colour(col)), float(pct or 0)))
    total = sum(p for _, p in items) or 1
    out = [{"hex": h, "percent": round(p / total * 100, 1),
            "px_of_1000": round(p / total * 1000)} for h, p in items]
    if args.json:
        return out
    for o in out:
        bar = "#" * max(1, round(o["percent"] / 2))
        print(f"  {o['hex']}  {o['percent']:>5}%  {o['px_of_1000']:>4}px  {bar}")


def _named(tokens):
    out = []
    for i, tok in enumerate(tokens, 1):
        name, sep, col = tok.rpartition("=")
        if not sep:
            name, col = f"Colour {i}", tok
        out.append((name.strip() or f"Colour {i}", parse_colour(col)))
    return out


def _ase(named, title):
    import struct

    def utf16(t):
        return t.encode("utf-16-be") + b"\x00\x00"

    blocks = []
    def block(kind, body):
        blocks.append(struct.pack(">HI", kind, len(body)) + body)
    t = utf16(title)
    block(0xC001, struct.pack(">H", len(t) // 2) + t)  # group start
    for name, rgb in named:
        n = utf16(name)
        body = (struct.pack(">H", len(n) // 2) + n + b"RGB "
                + struct.pack(">fff", *(c / 255 for c in rgb)) + struct.pack(">H", 2))  # 2 = normal
        block(0x0001, body)
    block(0xC002, b"")  # group end
    return b"ASEF" + struct.pack(">HHI", 1, 0, len(blocks)) + b"".join(blocks)


def _slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "colour"


def cmd_export(args):
    named = _named(args.colours)
    title = args.title
    fmt = args.format
    if fmt == "ase":
        data = _ase(named, title)
    elif fmt == "css":
        data = ":root {\n" + "".join(
            f"  --{_slug(n)}: {to_hex(c)};  /* rgb({c[0]}, {c[1]}, {c[2]}) */\n" for n, c in named) + "}\n"
    elif fmt == "gpl":
        data = f"GIMP Palette\nName: {title}\nColumns: {len(named)}\n#\n" + "".join(
            f"{c[0]:3d} {c[1]:3d} {c[2]:3d}\t{n}\n" for n, c in named)
    elif fmt == "canva":
        data = "".join(f"{to_hex(c)}  {n}\n" for n, c in named)
    else:  # json
        data = json.dumps({"name": title, "colours": [
            {"name": n, "hex": to_hex(c), "rgb": list(c), "hsb": list(to_hsb(c)),
             "cmyk_approx": list(to_cmyk(c))} for n, c in named]}, indent=2) + "\n"
    if args.out:
        mode = "wb" if isinstance(data, bytes) else "w"
        with open(args.out, mode) as f:
            f.write(data)
        msg = f"Wrote {len(named)} colours to {args.out} ({fmt})"
        return {"file": args.out, "format": fmt, "count": len(named)} if args.json else print(msg)
    if isinstance(data, bytes):
        sys.exit("ASE is binary: pass --out palette.ase")
    print(data, end="")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("command", choices=["convert", "contrast", "audit", "harmony", "ratio", "export"])
    p.add_argument("colours", nargs="+")
    p.add_argument("--json", action="store_true")
    p.add_argument("--format", default="json", choices=["ase", "css", "json", "gpl", "canva"])
    p.add_argument("--out", help="file to write (export only)")
    p.add_argument("--title", default="Palette", help="palette name (export only)")
    args = p.parse_args(argv)
    fn = globals()["cmd_" + args.command]
    try:
        res = fn(args)
    except ValueError as e:
        sys.exit(str(e))
    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
