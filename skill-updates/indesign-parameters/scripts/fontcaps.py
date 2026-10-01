#!/usr/bin/env python3
"""Read cap-height ratios from font files and add the font to references/fonts.json.

The heading sizes in grid.py depend on each weight's cap ratio (cap height / point size).
This reads it from the font's OS/2 table (capHeight / unitsPerEm) with no extra libraries.

Usage:
  python3 fontcaps.py FILE [FILE ...] [--save]      # local .ttf/.otf files (one per weight)
  python3 fontcaps.py --find "Family Name" [--save] # search this Mac's font folders
  python3 fontcaps.py --google "Family Name" [--save]  # download from github.com/google/fonts
  python3 fontcaps.py --list                        # fonts already in fonts.json
"""
import glob
import json
import os
import struct
import sys
import tempfile
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REGISTRY = os.path.join(HERE, "..", "references", "fonts.json")
FONT_DIRS = [
    "~/Library/Fonts", "/Library/Fonts", "/System/Library/Fonts",
    "~/Library/Application Support/Adobe/CoreSync/plugins/livetype",  # Adobe Fonts (activated)
    "C:/Windows/Fonts", "~/.fonts", "/usr/share/fonts",
]


def read_font(path):
    """Return a list of upright/italic weight entries in the file (TTF, OTF, TTC, variable)."""
    d = open(path, "rb").read()
    if d[:4] == b"ttcf":
        count = struct.unpack(">I", d[8:12])[0]
        offsets = struct.unpack(f">{count}I", d[12:12 + 4 * count])
    elif d[:4] in (b"\x00\x01\x00\x00", b"OTTO", b"true"):
        offsets = (0,)
    else:
        return []
    out = []
    for base in offsets:
        out += read_sfnt(d, base, os.path.basename(path))
    return out


def read_sfnt(d, base, name):
    n = struct.unpack(">H", d[base + 4:base + 6])[0]
    tables = {}
    for i in range(n):
        tag, _, off, length = struct.unpack(">4sIII", d[base + 12 + 16 * i:base + 28 + 16 * i])
        tables[tag] = (off, length)
    if b"OS/2" not in tables or b"head" not in tables:
        return []
    upm = struct.unpack(">H", d[tables[b"head"][0] + 18:tables[b"head"][0] + 20])[0]
    o = tables[b"OS/2"][0]
    version, _, weight, width = struct.unpack(">HhHH", d[o:o + 8])
    italic = bool(struct.unpack(">H", d[o + 62:o + 64])[0] & 1)
    cap = struct.unpack(">h", d[o + 88:o + 90])[0] if version >= 2 else 0
    if cap <= 0:
        cap = h_height(d, tables)  # older fonts: measure the capital H outline instead
    names = read_names(d, tables.get(b"name"))
    family = names.get(16) or names.get(1, "?")
    ratio = round(cap / upm, 4) if cap > 0 else None
    style = names.get(17) or names.get(2, "?")
    italic = italic or any(w in style.lower() for w in ("italic", "oblique"))
    entry = {"file": name, "family": family, "style": style, "weight": weight, "italic": italic,
             "normal_width": width == 5, "cap": ratio, "variable": False}
    if b"fvar" not in tables:
        return [entry]
    # Variable font: one entry per named instance, weight from its wght coordinate.
    # Cap height is the default instance's (per-instance variation in MVAR is not read).
    f = tables[b"fvar"][0]
    axes_off, _, axis_count, axis_size, inst_count, inst_size = struct.unpack(">HHHHHH", d[f + 4:f + 16])
    tags = [d[f + axes_off + i * axis_size:f + axes_off + i * axis_size + 4] for i in range(axis_count)]
    inst_base = f + axes_off + axis_count * axis_size
    out = []
    for i in range(inst_count):
        p = inst_base + i * inst_size
        sub = struct.unpack(">H", d[p:p + 2])[0]
        coords = struct.unpack(f">{axis_count}i", d[p + 4:p + 4 + 4 * axis_count])
        w = round(coords[tags.index(b"wght")] / 65536) if b"wght" in tags else weight
        style = names.get(sub, f"Instance {i + 1}")
        out.append(dict(entry, style=style, weight=w, variable=True,
                        italic=italic or "italic" in style.lower()))
    return out or [dict(entry, variable=True)]


def h_height(d, tables):
    """Top of the capital H in font units, from cmap + glyf (TrueType outlines only)."""
    if b"cmap" not in tables or b"glyf" not in tables or b"loca" not in tables:
        return 0
    c = tables[b"cmap"][0]
    gid = None
    for i in range(struct.unpack(">H", d[c + 2:c + 4])[0]):
        off = struct.unpack(">I", d[c + 8 + 8 * i:c + 12 + 8 * i])[0]
        gid = cmap_lookup(d, c + off, 0x48)
        if gid:
            break
    if not gid:
        return 0
    long_loca = struct.unpack(">h", d[tables[b"head"][0] + 50:tables[b"head"][0] + 52])[0]
    l = tables[b"loca"][0]
    off = struct.unpack(">I", d[l + 4 * gid:l + 4 * gid + 4])[0] if long_loca else 2 * struct.unpack(">H", d[l + 2 * gid:l + 2 * gid + 2])[0]
    g = tables[b"glyf"][0] + off
    return struct.unpack(">h", d[g + 8:g + 10])[0]


def cmap_lookup(d, t, code):
    """Glyph id for a character code in one cmap subtable (formats 0, 4, 6, 12)."""
    u16 = lambda o: struct.unpack(">H", d[o:o + 2])[0]
    fmt = u16(t)
    if fmt == 0:
        return d[t + 6 + code] if code < 256 else 0
    if fmt == 6:
        first, count = u16(t + 6), u16(t + 8)
        return u16(t + 10 + 2 * (code - first)) if first <= code < first + count else 0
    if fmt == 12:
        for k in range(struct.unpack(">I", d[t + 12:t + 16])[0]):
            start, end, g = struct.unpack(">III", d[t + 16 + 12 * k:t + 28 + 12 * k])
            if start <= code <= end:
                return g + code - start
        return 0
    if fmt == 4:
        segx2 = u16(t + 6)
        ends, starts = t + 14, t + 16 + segx2
        deltas, ranges = starts + segx2, starts + 2 * segx2
        for k in range(segx2 // 2):
            if u16(starts + 2 * k) <= code <= u16(ends + 2 * k):
                delta = struct.unpack(">h", d[deltas + 2 * k:deltas + 2 * k + 2])[0]
                ro = u16(ranges + 2 * k)
                if ro == 0:
                    return (code + delta) & 0xFFFF
                g = u16(ranges + 2 * k + ro + 2 * (code - u16(starts + 2 * k)))
                return (g + delta) & 0xFFFF if g else 0
    return 0


def read_names(d, entry):
    if not entry:
        return {}
    off = entry[0]
    _, count, str_off = struct.unpack(">HHH", d[off:off + 6])
    names = {}
    for i in range(count):
        pid, eid, lid, nid, length, noff = struct.unpack(">6H", d[off + 6 + 12 * i:off + 18 + 12 * i])
        raw = d[off + str_off + noff:off + str_off + noff + length]
        if pid == 3 and lid == 0x409:
            names.setdefault(nid, raw.decode("utf-16-be", "ignore"))
        elif pid == 1 and lid == 0:
            names.setdefault(nid, raw.decode("mac_roman", "ignore"))
    return names


def find_local(family):
    key = family.lower().replace(" ", "")
    hits = []
    for d in FONT_DIRS:
        for path in glob.glob(os.path.join(os.path.expanduser(d), "**", "*"), recursive=True):
            if not os.path.isfile(path) or os.path.getsize(path) < 1000:
                continue
            if path.lower().endswith((".ttf", ".otf", ".ttc")) or "livetype" in path:
                try:
                    fonts = read_font(path)
                except Exception:
                    continue
                if any(f["family"].lower().replace(" ", "") == key for f in fonts):
                    hits.append(path)
    return hits


def fetch_google(family):
    slug = family.lower().replace(" ", "")
    out = tempfile.mkdtemp(prefix="fontcaps-")
    for licence in ("ofl", "apache", "ufl"):
        url = f"https://api.github.com/repos/google/fonts/contents/{licence}/{slug}"
        try:
            listing = json.load(urllib.request.urlopen(url))
        except Exception:
            continue
        paths = []
        for item in listing:
            if item["name"].endswith(".ttf"):
                p = os.path.join(out, item["name"])
                urllib.request.urlretrieve(item["download_url"], p)
                paths.append(p)
        if paths:
            return paths
    return []


def summarise(fonts):
    fonts = [f for f in fonts if f and f["cap"] and not f["italic"] and f.get("normal_width", True)]
    if not fonts:
        return None
    family = fonts[0]["family"]
    weights = {f["style"]: {"cap": f["cap"], "weight": f["weight"]} for f in sorted(fonts, key=lambda f: f["weight"])}
    heavy = [s for s, w in weights.items() if w["weight"] >= 700]
    light = [s for s, w in weights.items() if w["weight"] <= 300]
    entry = {
        "weights": weights,
        # Headings: heaviest weight (Black > ExtraBold > Bold). Subheading: the light weight
        # closest to 300 (Light, else ExtraLight, else Thin).
        "heavy": max(heavy, key=lambda s: weights[s]["weight"]) if heavy else None,
        "light": max(light, key=lambda s: weights[s]["weight"]) if light else None,
        "variable": any(f["variable"] for f in fonts),
    }
    return family, entry


def load():
    return json.load(open(REGISTRY)) if os.path.exists(REGISTRY) else {"default": "Lato", "fonts": {}}


def main(argv):
    if not argv or argv[0] == "--list":
        reg = load()
        for name, e in reg["fonts"].items():
            mark = " (default)" if name == reg["default"] else ""
            print(f"{name}{mark}: headings {e['heavy']}, subheading {e['light']}, weights "
                  + ", ".join(f"{s} {w['cap']}" for s, w in e["weights"].items()))
        return
    if argv[0] == "--find":
        paths = find_local(argv[1])
    elif argv[0] == "--google":
        paths = fetch_google(argv[1])
    else:
        paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print("No font files found. Try --google, pass the files directly, or measure a 100 pt H in InDesign.")
        sys.exit(1)
    key = None if argv[0] not in ("--find", "--google") else argv[1].lower().replace(" ", "")
    fonts = [f for p in paths for f in read_font(p)
             if key is None or f["family"].lower().replace(" ", "") == key]
    result = summarise(fonts)
    if not result:
        print("Found files but no readable upright weights with a cap height.")
        sys.exit(1)
    family, entry = result
    print(f"{family}: headings {entry['heavy'] or 'NO BOLD/BLACK WEIGHT'}, "
          f"subheading {entry['light'] or 'NO LIGHT/THIN WEIGHT'}")
    for style, w in entry["weights"].items():
        print(f"  {style:<14} weight {w['weight']:<4} cap ratio {w['cap']}")
    if entry["variable"]:
        print("  Variable font: cap ratio is the default instance's. Check headings with the 100 pt H test.")
    if "--save" in argv:
        reg = load()
        reg["fonts"][family] = entry
        json.dump(reg, open(REGISTRY, "w"), indent=2, ensure_ascii=False)
        print(f"Saved {family} to references/fonts.json")


if __name__ == "__main__":
    main(sys.argv[1:])
