# Platforms

Each platform sets its own content width. The house grid sits inside it, with our own margins,
never the theme's padding. Status: **verified** means checked against the platform's source or
settings; **unverified** means a starting point to test before relying on it.

## Canvas LMS (verified against source; test on a live course)

- **Width:** the content column is fluid. It shrinks as the course menu and sidebar open, and pages
  go full width above 1450 px. Wrap content in `max-width: 1200px`.
- **Allowed CSS:** only inline `style` attributes on the sanitiser allowlist
  (`gems/canvas_sanitize/.../canvas_sanitize.rb`).
  - **Allowed:** `display: grid`, `grid-template-columns`, `grid-column`, `gap`, `flex` / `flex-wrap`,
    `max-width`, `border`, `padding`, `margin`, `background`, and `font` (shorthand).
  - **Stripped:** `<style>`, classes' effects, media queries, `font-weight`, `text-transform`,
    `letter-spacing`, `aspect-ratio`, `box-sizing` and custom properties (so `var()` can't work).
  - **Untested:** whether `calc()` survives. Avoid it.
- **Layouts:**
  - **Wrapping cards** (recommended): `flex: 1 1 290px` with a `gap: 10px`. Cards are at least
    the 290 px mobile live area wide, so they stack on phones.
  - **Fixed 12-column grid:** `grid-template-columns: repeat(12, 1fr); gap: 10px`. The gutter is exact
    and the columns are fluid twelfths. It does not stack on phones, so it's for wide-only layouts.
  - **Tables:** the fallback for anything else.
- **Type:** 760 heading scale at every size, caps typed, weight via the `font` shorthand.
- **Check:** `python3 scripts/check_canvas.py page.html` must report 0 problems.
- **To confirm on a live course:**
  - whether Canvas's Lato Extended includes a Black (900) weight (if not, headings render Bold)
  - how grid and flex behave in the Canvas mobile app

## Shopify (verified: Dawn theme source)

- **Width:** Dawn's `page_width` setting runs 1000–1600 px in 100 px steps, default **1200**.
  `.page-width` padding is 1.5rem (24 px) on mobile and 5rem (80 px) from 750 px up.
- **Recommended:** keep page width at 1200. Put house sections in a Custom Liquid section (or theme
  CSS) using `.hw-container`, which sets its own width and margins, and remove Dawn's padding
  on that wrapper.
- **If Dawn's 80 px padding is kept,** the live area is 1040. The only whole grid is then
  12 × 50 + 11 × 40 = 1040, preset D with no choice.
- **Other page-width settings** are all multiples of 100, so each one has a whole grid. Solve it with
  `scripts/grid.py WIDTH`.
- Dawn's own grid spacing uses 4 px steps (default 8), so it isn't on the 5 px system.
  Don't mix Dawn grid blocks with house blocks in one section.

## WordPress (verified: Twenty Twenty-Five theme.json)

- **Theme defaults:** Twenty Twenty-Five has `contentSize` 645 px and `wideSize` 1340 px. These happen to be
  whole (12 × 40 + 11 × 15 = 645; 12 × 75 + 11 × 40 = 1340), but they don't match the house presets.
- **House setting:** in `theme.json` (or Site Editor → Styles → Layout), set `contentSize` to **760px** and
  `wideSize` to **1200px**, and set root padding to 0. Then add `house-web.css` and use
  `.hw-container` on a Group block (Additional CSS class) so the house margins apply.
  Needs testing in a block theme.
- **Spacing presets:** WordPress's spacing uses 10 / 20 / 30 px, then `clamp()` values from 50 up.
  Use the 10 / 20 / 30 steps and avoid the fluid ones.

## Plain HTML (verified by render)

- Link `assets/house-web.css` and `assets/snap.js`. Put `class="hw-page hw-a"` on `<body>`
  (swap `hw-a` for `hw-b`, `hw-c` or `hw-d`) and use `<main class="hw-container"><div class="hw-grid">…`.
- See `assets/sample.html`.

## Site builders (unverified)

- **Google Sites:** no custom CSS on the page itself. House layouts only work inside an
  **Embed → Embed code** block, which renders in an iframe. So use the full CSS inside the embed,
  and size the embed to a container step.
- **Squarespace:** set the site's maximum content width to 1200 in Site Styles if the template
  allows it. Custom CSS (paid plans) can add `house-web.css` rules.
- **Wix:** classic Wix has no custom CSS, so match the numbers by hand in the editor's grid.
  Wix Studio allows custom CSS and CSS grid, so use the tokens there.
- **Adobe Express / Canva web pages:** sized by canvas, not CSS. Set the page width to 1200 and
  place elements using the 1200 preset numbers (e.g. A: 65 margin, 80 module, 10 gutter).
