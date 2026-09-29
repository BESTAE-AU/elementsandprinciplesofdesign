# MBE Creative Studio

MBE Creative Studio is Britt's freelance creative business — a shopping platform for prints, photography and artwork, combined with a portfolio and general freelancing offering. This is the brand's first foundation: real logo assets, a working colour palette, and the tokens to build from. Typography and components come next.

## The mood: biophilic

The brand's visual direction is grounded in a biophilic mood — macro nature photography, backlit leaves, growth rings, radiating veins, warm earthy neutrals and deep grounded greens. It should feel calm, organic and considered rather than loud. Against that quiet base, the brand's signature pink is a deliberate "bloom" — one bright, living moment against everything else being restrained, the way a single flower reads against a field of green.

## Logo

The real vector logo lives in this system's assets (Logos group), never approximated:

- **Pink Logo** — the full lockup: the hand-lettered "mbe" script mark with "creative studio" set beneath it in a lighter italic script.
- **Favicon** — the "mbe" mark on its own, for small/square placements (favicons, social avatars, app icons).

Both are drawn in `accent-bloom` (`#ff3eb5`) exactly — this is where that hex code comes from, and the reason it's treated as the brand's one non-negotiable accent colour. Always place the logo on `surface-100`, `surface-000` or `surface-900` (cream, white or deep green); it hasn't been tested on the warm peach and may lose contrast there.

## Colour

Six source colours, expanded into usable tokens. Full values and usage notes are in `tokens.json`; the roles:

- **Cream (`#f3e9e2`) and deep green (`#13342c`)** do the daily work — background and text/dark-sections. This pairing carries the biophilic mood on its own and reaches 11.3:1 contrast, so it's safe for body copy at any size.
- **White (`#ffffff`)** is the elevated surface — cards, product photography backdrops — one step lighter than the linen background.
- **Pink (`#ff3eb5`)** is the bloom accent: one CTA, a badge, a hover state. Not a background, not a large shape, not the default button colour. If everything on a page is pink, it's stopped being a bloom.
- **Peach (`#ffa06a`)** is the secondary accent — tags, highlights, illustration fills — and reads as the warm, natural counterpart to the pink. It only works with dark text on top (see Accessibility below).
- **Black (`#000000`)** stays a utility colour for print production; the UI never needs pure black since deep green already reads as a strong near-black.

### Colour usage rules

**Proportion.** About 60% `surface-100` / `surface-000`, 30% deep green (`ink`, `surface-900`, `brand-primary`), under 10% `accent-warm`, and `accent-bloom` at about 5% — a single bloom per view. The palette works as a cool, grounded neutral base with a near-complementary warm accent pair: the pink reads as a bloom precisely because everything around it is green and linen.

**Text on each ground (WCAG, body text needs 4.5:1):**

| Ground | Use for text | Never |
|---|---|---|
| `surface-100` cream | `ink` 11.3 · `ink-muted` 7.3 | `accent-bloom` 2.7 · `accent-warm` 1.7 |
| `surface-000` white | `ink` 13.5 · `ink-muted` 8.7 | `accent-bloom` 3.2 · `accent-warm` 2.0 |
| `surface-900` deep green | `ink-inverse` 11.3 · white 13.5 | `ink-muted` 1.6 |
| `accent-warm` peach | `accent-warm-ink` 6.7 | `ink-muted` 4.3 · white 2.0 · cream 1.7 |
| `accent-bloom` pink | `accent-bloom-ink` 4.25 **or** white 3.18 — **large/bold only** (24px+, or bold 19px+) | any small text |

- **Bloom buttons:** label in `accent-bloom-ink`, bold, 19px or larger. If a CTA needs smaller text, use a `brand-primary` button instead and let the pink carry a badge or hover state.
- **Borders:** `border` is decorative only (1.25:1 on cream). Inputs, focus rings and anything interactive use `ink-muted` (7.3:1).
- **Pink and peach** are 1.6:1 apart. Never use them side by side as the only difference between two things.
- **Logo:** WCAG exempts logos from contrast rules, but the pink mark is only 2.7:1 on cream. At small sizes (favicon, social avatar, footer) place it on `surface-000` or `surface-900` (4.25:1).
- **Print:** `utility-black` and `utility-white` are for production files. The bright pink and peach are outside the CMYK gamut, so soft-proof them and specify spot colours if exact matching matters.

## Spacing and radius

A simple 4–48px spacing scale and four radius steps, generous rather than sharp — soft, rounded corners suit the organic, biophilic direction better than square-edged UI. See `tokens.json` for the full scale.

## Typography

Two families, doing two different jobs.

**Gill Sans Nova** is body and UI text — a humanist sans with an extensive weight range, which is why it works for everything from captions to display headings without borrowing a second family. It isn't in the Adobe Fonts or Google Fonts catalogues Claude can search from here, so this system's own previews fall back to your system's Gill Sans / Calibri where Gill Sans Nova itself isn't installed — the token still declares the real name first, so anywhere the actual font is available (your Adobe apps, a site with the font files or a Monotype/Adobe web licence linked) picks it up correctly. To serve it properly on a future website, you'll need either the licensed webfont files self-hosted, or a Monotype/Adobe Fonts web project for it — worth checking what your Creative Cloud plan already includes.

**Santorini** is the accent script — the real typeface behind the "mbe" logotype, now carried into the system as its own family (the actual font file is bundled in, so it renders correctly everywhere this system is opened). Use it the way the logo uses it: sparingly, large, and short — a hero word on a landing page, a pull-quote, a handwritten-feel annotation beside a product. It's not for body copy, long headings, or anything a customer needs to read quickly; connected script letterforms get harder to read fast as the string gets longer, which is exactly why the logo itself keeps the large flourish to the short "mbe" and sets "creative studio" smaller, in a lighter companion script, underneath it.

Gill Sans Nova and Santorini pair well because they don't compete: one is plain and geometric, the other loose and expressive, so the script stays the one flourish in the system rather than one of several.

## What's next

- **Imagery direction.** Macro, backlit, botanical — leaf veins, growth rings, lotus and ginkgo leaves against sky or warm neutral backdrops. Concentric/radiating line patterns (like the growth-ring motif on this system's cover) are a natural recurring graphic device across the brand.
- **Components.** Buttons, cards and product tiles once typography is settled.
