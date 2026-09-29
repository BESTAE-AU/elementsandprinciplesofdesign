#!/usr/bin/env python3
"""Texture helpers for the texture-element-of-design skill (standard library only).

Commands:
  text-over <text-hex> <tone-hex> [<tone-hex> ...]
                                 Worst-case WCAG 2.x contrast for text sitting
                                 on a texture. Give the lightest and darkest
                                 tones behind the words (more tones are fine).
                                 If it fails, finds the lowest-opacity scrim
                                 (solid overlay under the text) that passes.
                                 Options: --target 4.5 (body; use 3 for large
                                 text), --scrim <hex> (default: tries black and
                                 white and reports the lower opacity).
  swatches [--blank] [--out FILE]
                                 A4 greyscale SVG worksheet of mark-making
                                 textures: each labelled example beside an
                                 empty practice box. --blank leaves both
                                 boxes empty (labels only). Default output:
                                 texture-swatches.svg.

Add --json to text-over for machine-readable output.

Contrast maths follows WCAG 2.x relative luminance. Scrim blending is simple
alpha compositing in sRGB, which is how design tools blend a normal layer at
reduced opacity.
"""
import argparse
import json
import math
import random
import re
import sys

# ---------------------------------------------------------------- contrast


def parse_hex(value):
    v = value.strip().lstrip("#")
    if re.fullmatch(r"[0-9a-fA-F]{3}", v):
        v = "".join(c * 2 for c in v)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", v):
        raise argparse.ArgumentTypeError(f"not a hex colour: {value}")
    return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))


def to_hex(rgb):
    return "#" + "".join(f"{round(c):02X}" for c in rgb)


def luminance(rgb):
    def chan(c):
        c = c / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (chan(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def blend(top, bottom, alpha):
    return tuple(alpha * t + (1 - alpha) * b for t, b in zip(top, bottom))


def min_scrim(text, tones, scrim, target):
    """Lowest scrim opacity (0-1) at which every tone passes, or None."""
    def ok(alpha):
        return all(contrast(text, blend(scrim, t, alpha)) >= target
                   for t in tones)
    if not ok(1.0):
        return None
    lo, hi = 0.0, 1.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if ok(mid):
            hi = mid
        else:
            lo = mid
    # Round up to the next whole percent so the stated value really passes.
    return math.ceil(hi * 100) / 100


def cmd_text_over(args):
    text = args.text
    tones = args.tones
    results = [{"tone": to_hex(t), "ratio": round(contrast(text, t), 2),
                "passes": contrast(text, t) >= args.target} for t in tones]
    worst = min(results, key=lambda r: r["ratio"])
    data = {"text": to_hex(text), "target": args.target, "tones": results,
            "worst": worst, "passes": worst["passes"]}

    lines = [f"Text {to_hex(text)} on texture, target {args.target}:1", ""]
    for r in results:
        mark = "pass" if r["passes"] else "FAIL"
        lines.append(f"  {r['tone']}  {r['ratio']:>5.2f}:1  {mark}")
    lines.append("")
    lines.append(f"Worst case: {worst['ratio']:.2f}:1 on {worst['tone']} "
                 f"-> {'PASSES' if worst['passes'] else 'FAILS'}")

    if not worst["passes"]:
        if args.scrim is not None:
            scrim = args.scrim
            alpha = min_scrim(text, tones, scrim, args.target)
        else:
            # Try black and white; keep whichever passes at the lower opacity.
            options = [(min_scrim(text, tones, s, args.target), s)
                       for s in ((0, 0, 0), (255, 255, 255))]
            passing = [o for o in options if o[0] is not None]
            alpha, scrim = min(passing) if passing else options[0]
        data["scrim"] = {"colour": to_hex(scrim),
                         "opacity": alpha if alpha is not None else None}
        lines.append("")
        if alpha is None:
            lines.append(f"No {to_hex(scrim)} scrim can reach {args.target}:1 "
                         f"with this text colour. Change the text colour or "
                         f"put the text on a solid panel.")
        else:
            after = [to_hex(blend(scrim, t, alpha)) for t in tones]
            data["scrim"]["tones_after"] = after
            lines.append(f"Fix: a {to_hex(scrim)} scrim at "
                         f"{round(alpha * 100)}% opacity behind the text makes "
                         f"every tone pass.")
            lines.append("  Tones after scrim: " + ", ".join(after))
        lines.append("Other fixes: lower the texture's contrast or opacity, "
                     "blur it behind the text, move the text to a smoother "
                     "area, or use a heavier/larger text size (3:1 target).")

    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print("\n".join(lines))
    return 0 if worst["passes"] else 1


# ---------------------------------------------------------------- swatches

BOX = 36.0          # swatch box size, mm
INK = "#1A1A1A"
GUIDE = "#8C8C8C"


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def line(x1, y1, x2, y2, w=0.3):
    return (f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" '
            f'stroke="{INK}" stroke-width="{w}" stroke-linecap="round"/>')


def hatching(x, y, rng):
    return [line(x + i, y, x + i, y + BOX) for i in range(2, int(BOX), 2)]


def cross_hatching(x, y, rng):
    out = []
    for i in range(-int(BOX), int(BOX) * 2, 3):
        out.append(line(x + i, y + BOX, x + i + BOX, y))
        out.append(line(x + i, y, x + i + BOX, y + BOX))
    return out


def contour_hatching(x, y, rng):
    # Lines bending around an imagined cylinder.
    out = []
    for i in range(1, 14):
        yy = y + i * BOX / 14
        pts = []
        for s in range(0, 21):
            xx = x + s * BOX / 20
            bulge = math.sin(math.pi * s / 20) * 4
            pts.append(f"{f(xx)},{f(yy + bulge)}")
        out.append(f'<polyline points="{" ".join(pts)}" fill="none" '
                   f'stroke="{INK}" stroke-width="0.3"/>')
    return out


def stippling(x, y, rng):
    out = []
    # Denser toward the lower left: a stippled value gradient.
    for _ in range(900):
        px, py = rng.random(), rng.random()
        if rng.random() < (1 - px) * py * 1.3 + 0.08:
            out.append(f'<circle cx="{f(x + px * BOX)}" cy="{f(y + py * BOX)}" '
                       f'r="0.28" fill="{INK}"/>')
    return out


def scribble(x, y, rng):
    # Loose overlapping loops travelling back and forth across the box.
    pts = []
    rows = 7
    for r in range(rows):
        yy = y + (r + 0.5) * BOX / rows
        forward = r % 2 == 0
        for s in range(0, 121):
            t = s / 120
            tx = t if forward else 1 - t
            ang = t * 2 * math.pi * 9
            rad = 2.2 + rng.uniform(-0.4, 0.4)
            px = x + 2 + tx * (BOX - 4) + rad * math.cos(ang)
            py = yy + rad * math.sin(ang) + rng.uniform(-0.3, 0.3)
            pts.append(f"{f(px)},{f(py)}")
    return [f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" '
            f'stroke-width="0.25" stroke-linejoin="round"/>']


def halftone(x, y, rng):
    out = []
    step = 2.5
    n = int(BOX / step)
    for i in range(n):
        for j in range(n):
            tone = (i + j) / (2 * (n - 1))          # light top-left, dark bottom-right
            r = 0.15 + tone * step * 0.62
            out.append(f'<circle cx="{f(x + (i + 0.5) * step)}" '
                       f'cy="{f(y + (j + 0.5) * step)}" r="{f(r)}" fill="{INK}"/>')
    return out


def wood_grain(x, y, rng):
    out = []
    knot_x, knot_y = x + BOX * 0.62, y + BOX * 0.45
    for i in range(16):
        base = x + (i + 0.5) * BOX / 16
        pts = []
        for s in range(0, 41):
            yy = y + s * BOX / 40
            dx = base - knot_x
            dy = yy - knot_y
            d = math.hypot(dx, dy) + 1
            push = 14 / d * (1 if dx >= 0 else -1)
            wobble = math.sin(s * 0.5 + i) * 0.35
            pts.append(f"{f(base + push + wobble)},{f(yy)}")
        out.append(f'<polyline points="{" ".join(pts)}" fill="none" '
                   f'stroke="{INK}" stroke-width="0.3"/>')
    out.append(f'<ellipse cx="{f(knot_x)}" cy="{f(knot_y)}" rx="1.6" ry="2.6" '
               f'fill="none" stroke="{INK}" stroke-width="0.4"/>')
    return out


def brick(x, y, rng):
    out = []
    h, w = 5.0, 10.0
    rows = int(BOX / h)
    for r in range(rows + 1):
        out.append(line(x, y + r * h, x + BOX, y + r * h, 0.35))
    for r in range(rows):
        offset = 0 if r % 2 == 0 else w / 2
        xx = x + offset
        while xx < x + BOX:
            if xx > x:
                out.append(line(xx, y + r * h, xx, y + (r + 1) * h, 0.35))
            xx += w
        # A few texture flecks per row.
        for _ in range(6):
            fx, fy = x + rng.random() * BOX, y + r * h + 1 + rng.random() * (h - 2)
            out.append(f'<circle cx="{f(fx)}" cy="{f(fy)}" r="0.25" fill="{INK}"/>')
    return out


def basket_weave(x, y, rng):
    out = []
    cell = 8.0
    n = int(BOX / cell)
    for i in range(n):
        for j in range(n):
            cx, cy = x + i * cell, y + j * cell
            for k in range(1, 4):
                t = k * cell / 4
                if (i + j) % 2 == 0:
                    out.append(line(cx + t, cy + 0.6, cx + t, cy + cell - 0.6))
                else:
                    out.append(line(cx + 0.6, cy + t, cx + cell - 0.6, cy + t))
    return out


def scales(x, y, rng):
    out = []
    r = 3.0
    for row in range(int(BOX / r) + 2):
        offset = 0 if row % 2 == 0 else r
        for col in range(-1, int(BOX / (2 * r)) + 2):
            cx = x + col * 2 * r + offset
            cy = y + row * r
            out.append(f'<path d="M {f(cx - r)} {f(cy)} A {f(r)} {f(r)} 0 0 0 '
                       f'{f(cx + r)} {f(cy)}" fill="none" stroke="{INK}" '
                       f'stroke-width="0.3"/>')
    return out


TECHNIQUES = [
    ("Hatching", "timber, hair, engraved shading", hatching),
    ("Cross-hatching", "shadow, mesh, woven cloth", cross_hatching),
    ("Contour hatching", "rounded forms, pipes, fruit", contour_hatching),
    ("Stippling", "sand, stone, skin, soft shading", stippling),
    ("Scribble", "foliage, fur, wool, energy", scribble),
    ("Halftone dots", "print, pop art, retro comics", halftone),
    ("Wood grain", "timber, bark, natural fibre", wood_grain),
    ("Brick and mortar", "walls, paving, urban", brick),
    ("Basket weave", "woven textiles, cane, hessian", basket_weave),
    ("Scales", "fish, reptiles, roof tiles", scales),
]


def cmd_swatches(args):
    W, H = 210.0, 297.0
    margin = 15.0
    col_w = (W - 2 * margin - 10) / 2
    title_h = 22.0
    row_h = (H - 2 * margin - title_h) / 5
    rng = random.Random(7)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{f(W)}mm" '
        f'height="{f(H)}mm" viewBox="0 0 {f(W)} {f(H)}" '
        f'font-family="Lato, Arial, Helvetica, sans-serif">',
        f'<rect width="{f(W)}" height="{f(H)}" fill="#FFFFFF"/>',
        f'<text x="{f(margin)}" y="{f(margin + 7)}" font-size="7" '
        f'font-weight="700" fill="{INK}">TEXTURE: MARK-MAKING SAMPLER</text>',
        f'<text x="{f(margin)}" y="{f(margin + 14)}" font-size="3.6" '
        f'fill="{INK}">'
        + ("Create each visual texture in the boxes. Write a real surface "
           "it could represent under each one."
           if args.blank else
           "Copy each visual texture into the practice box. Then name another "
           "surface it could represent.")
        + '</text>',
        f'<text x="{f(W - margin)}" y="{f(margin + 7)}" font-size="3.6" '
        f'text-anchor="end" fill="{INK}">Name: ____________________</text>',
    ]

    for idx, (name, uses, fn) in enumerate(TECHNIQUES):
        col, row = idx % 2, idx // 2
        cx = margin + col * (col_w + 10)
        cy = margin + title_h + row * row_h
        parts.append(f'<text x="{f(cx)}" y="{f(cy + 4)}" font-size="4" '
                     f'font-weight="700" fill="{INK}">{idx + 1}. '
                     f'{name.upper()}</text>')
        bx1, by = cx, cy + 6.5
        bx2 = cx + col_w - BOX
        clip = f"c{idx}"
        parts.append(f'<clipPath id="{clip}"><rect x="{f(bx1)}" y="{f(by)}" '
                     f'width="{f(BOX)}" height="{f(BOX)}"/></clipPath>')
        if not args.blank:
            parts.append(f'<g clip-path="url(#{clip})">')
            parts.extend(fn(bx1, by, rng))
            parts.append('</g>')
        for bx in (bx1, bx2):
            parts.append(f'<rect x="{f(bx)}" y="{f(by)}" width="{f(BOX)}" '
                         f'height="{f(BOX)}" fill="none" stroke="{INK}" '
                         f'stroke-width="0.4"/>')
        cap_y = by + BOX + 3.6
        left_cap = ("Surface: ________________" if args.blank
                    else "e.g. " + uses)
        parts.append(f'<text x="{f(bx1)}" y="{f(cap_y)}" font-size="2.8" '
                     f'fill="{GUIDE}">{left_cap}</text>')
        parts.append(f'<text x="{f(bx2)}" y="{f(cap_y)}" font-size="2.8" '
                     f'fill="{GUIDE}">'
                     f'{"Try it:" if args.blank else "Your version"} '
                     f'________________</text>')

    parts.append('</svg>')
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(parts) + "\n")
    print(f"Wrote {args.out} (A4 portrait, greyscale, "
          f"{len(TECHNIQUES)} techniques{', blank' if args.blank else ''}).")
    return 0


# ---------------------------------------------------------------- main


def main(argv=None):
    p = argparse.ArgumentParser(description="Texture helpers.")
    sub = p.add_subparsers(dest="cmd", required=True)

    t = sub.add_parser("text-over", help="worst-case contrast of text on a texture")
    t.add_argument("text", type=parse_hex)
    t.add_argument("tones", type=parse_hex, nargs="+")
    t.add_argument("--target", type=float, default=4.5)
    t.add_argument("--scrim", type=parse_hex, default=None)
    t.add_argument("--json", action="store_true")
    t.set_defaults(func=cmd_text_over)

    s = sub.add_parser("swatches", help="A4 mark-making worksheet (SVG)")
    s.add_argument("--blank", action="store_true")
    s.add_argument("--out", default="texture-swatches.svg")
    s.set_defaults(func=cmd_swatches)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
