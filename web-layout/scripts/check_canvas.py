#!/usr/bin/env python3
"""Check that every inline style in an HTML file survives the Canvas LMS sanitiser.

Allowlist copied from instructure/canvas-lms
gems/canvas_sanitize/lib/canvas_sanitize/canvas_sanitize.rb (master, checked 2026-09-29).
Also flags <style>, <script> and house classes, which Canvas drops, and warns on CSS functions:
var() never works (custom properties are not allowed); calc()/clamp() are untested in Canvas.

  check_canvas.py FILE.html
"""
import re
import sys
from html.parser import HTMLParser

BASE = """align-content align-items align-self background border border-radius clear clip color
column-gap cursor direction display flex flex-basis flex-direction flex-flow flex-grow flex-shrink
flex-wrap float font gap grid height justify-content justify-items justify-self left line-height
list-style margin max-height max-width min-height min-width order overflow overflow-x overflow-y
padding position place-content place-items place-self right row-gap text-align table-layout
text-decoration text-indent top user-select vertical-align visibility white-space width z-index
zoom""".split()
ALLOWED = set(BASE)
ALLOWED |= {f"grid-{i}" for i in "area auto-columns auto-flow auto-rows column gap row template".split()}
ALLOWED |= {f"grid-template-{i}" for i in "areas columns rows".split()}
ALLOWED |= {f"grid-column-{i}" for i in "end gap start".split()}
ALLOWED |= {f"grid-row-{i}" for i in "end gap start".split()}
ALLOWED |= {f"background-{i}" for i in "attachment color image position repeat".split()}
ALLOWED |= {"background-position-x", "background-position-y"}
ALLOWED |= {f"border-{i}" for i in "bottom collapse color left right spacing style top width".split()}
ALLOWED |= {f"border-{s}-{p}" for s in "bottom left right top".split() for p in "color style width".split()}
ALLOWED |= {f"font-{i}" for i in "family size stretch style variant width".split()}
ALLOWED |= {f"list-style-{i}" for i in "image position type".split()}
ALLOWED |= {f"margin-{i}" for i in "bottom left right top offset".split()}
ALLOWED |= {f"padding-{i}" for i in "bottom left right top".split()}


class Checker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.problems = []
        self.warnings = []

    def handle_starttag(self, tag, attrs):
        line = self.getpos()[0]
        if tag in ("style", "script", "link"):
            self.problems.append(f"line {line}: <{tag}> is stripped by Canvas")
        for name, value in attrs:
            if name == "class" and value and "hw-" in value:
                self.problems.append(f"line {line}: class '{value}' has no effect in Canvas")
            if name != "style" or not value:
                continue
            for decl in filter(None, (d.strip() for d in value.split(";"))):
                prop, _, val = decl.partition(":")
                prop = prop.strip().lower()
                if prop not in ALLOWED:
                    self.problems.append(f"line {line}: '{prop}' is not allowed")
                if re.search(r"\bvar\(", val):
                    self.problems.append(f"line {line}: var() cannot work in Canvas")
                elif re.search(r"\b(calc|clamp|min|max)\(", val):
                    self.warnings.append(f"line {line}: '{val.strip()}' is untested in Canvas")


def main(path):
    c = Checker()
    c.feed(open(path, encoding="utf-8").read())
    for p in c.problems:
        print(p)
    for w in c.warnings:
        print("warning:", w)
    print(f"{len(c.problems)} problem(s) in {path}")
    return 1 if c.problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
