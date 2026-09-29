#!/usr/bin/env python3
"""Whole-number 12-column web grid solver (house design system, web layout).

Every value is a multiple of STEP (5 px). The grid is built from the margins
inwards:  width = 2*margin + 12*module + 11*gutter.
Rows are ratio modules: row = module * ratio, and must also be a whole 5 px step.

Usage:
  grid.py WIDTH [--ratio 1:1] [--margin-min 0] [--margin-max 80]
          [--gutter 10,20] [--module-min 10]
"""
import argparse
from fractions import Fraction

STEP = 5
COLS = 12


def parse_ratio(text):
    w, h = text.split(":")
    return Fraction(int(h), int(w))  # row height as a fraction of module width


def solve(width, ratio=Fraction(1), margin_min=0, margin_max=None,
          gutters=None, module_min=STEP):
    """Return every (margin, module, gutter, row) whose sum equals width exactly."""
    if margin_max is None:
        margin_max = width // 4
    results = []
    for gutter in gutters or range(STEP, width // COLS, STEP):
        for margin in range(margin_min, margin_max + 1, STEP):
            live = width - 2 * margin
            rest = live - (COLS - 1) * gutter
            if rest <= 0 or rest % COLS:
                continue
            module = rest // COLS
            if module < module_min or module % STEP:
                continue
            row = module * ratio
            if row.denominator != 1 or row % STEP:
                continue
            results.append(dict(width=width, margin=margin, module=module,
                                gutter=gutter, row=int(row), live=live,
                                pitch=module + gutter, vpitch=int(row) + gutter))
    return results


def proof(g):
    return (f"{g['margin']} + {COLS} × {g['module']} + {COLS - 1} × {g['gutter']}"
            f" + {g['margin']} = {g['width']}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("width", type=int)
    p.add_argument("--ratio", default="1:1", help="module w:h, e.g. 1:1, 4:3, 3:2")
    p.add_argument("--margin-min", type=int, default=0)
    p.add_argument("--margin-max", type=int)
    p.add_argument("--gutter", help="comma list of gutters to allow, e.g. 10,20")
    p.add_argument("--module-min", type=int, default=STEP)
    a = p.parse_args()
    gutters = [int(x) for x in a.gutter.split(",")] if a.gutter else None
    rows = solve(a.width, parse_ratio(a.ratio), a.margin_min, a.margin_max,
                 gutters, a.module_min)
    if not rows:
        print(f"No whole-number grid for {a.width} px at ratio {a.ratio}.")
        return 1
    print(f"{'margin':>6} {'module':>6} {'gutter':>6} {'row':>5} {'pitch':>5}  proof")
    for g in rows:
        print(f"{g['margin']:>6} {g['module']:>6} {g['gutter']:>6} {g['row']:>5}"
              f" {g['pitch']:>5}  {proof(g)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
