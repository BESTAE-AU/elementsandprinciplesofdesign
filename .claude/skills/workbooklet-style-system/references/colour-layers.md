# Colour Layers

Colour is a layer on top of the shared type system. A document uses **either** the
Greyscale layer **or** the Bestae layer. Every colour decision is made through a
**role token**, so moving a document between layers is a token swap, not a
redesign.

Heading and body text is always **black**, or **white on a Dark or Darkest
fill**, in both layers. Colour never goes on heading text.

## Role tokens

| Token | Role | Greyscale | Bestae (domain colour *n*) | Word theme slot |
|---|---|---|---|---|
| **Paper** | Page and white cells | `#FFFFFF` | `#FFFFFF` | `lt1` (Background 1) |
| **Text** | All text | `#000000` | `#000000` | `dk1` (Text 1) |
| **Light** | Label cells (Heading 9), default table header row (Heading 4), Possible Answers | `#E3E4E3` | Tint *n*T | `lt2` (Background 2) |
| **Pale** | Group and sub-header rows (Heading 5), MARKING CRITERIA header | `#CACBCA` | Tint *n*T | `accent1` |
| **Accent** | Colour bars, rules, small banners, icons. Never behind body text | `#767776` | Main *n*H | `accent4` |
| **Dark** | Dark header rows, vertical category column, Example Response, table borders | `#4C4D4C` | Shadow *n*S | `accent6` |
| **Darkest** | Full-width banners (Heading 1 White) | `#343433` | Shadow *n*S | `dk2` (Text 2) |
| **Muted** | Captions, subtle references | `#5E5E5E` | `#5E5E5E` | — (fixed) |

The Greyscale values are the existing **Greyscale for Printing** Word theme.
Booklets already built with it won't change.

## Text contrast rule

Text must reach at least **4.5 : 1** contrast with its fill (WCAG AA). Large
headings (Heading 4 and above) need at least **3 : 1**. This decides whether text
on a fill is black or white.

### Greyscale

| Fill | Text | Contrast |
|---|---|---|
| Light `#E3E4E3`, Pale `#CACBCA` | Black | 16.5 / 12.9 |
| Accent `#767776` | Avoid text; if it's unavoidable, use white Heading 4 or larger | 4.5 / 4.7 |
| Dark `#4C4D4C`, Darkest `#343433`, `#626362` | White | 8.8+ / 6.0 |

### Bestae palette

| # | Domain of learning | Main (H) | Text on H | Shadow (S) | Text on S | Tint (T) | Text on T |
|---|---|---|---|---|---|---|---|
| 1 | *Brand / default* | Jazzberry `#AC145A` | **White** (7.0) | Mulberry `#651C32` | White | Piggy Pink `#EEDAEA` | Black |
| 2 | Critical Thinking | Tomato `#FF585D` | Black (6.8) | Espresso `#551C25` | White | Soft Blush `#F5DADF` | Black |
| 3 | Creative Thinking, Problem Solving and Innovation | Royal Orange `#F19C49` | Black (9.6) | Dark Leather `#4F2C1D` | White | Apricot `#FFDFB4` | Black |
| 4 | Communication | Corn `#F3EA5D` | Black (16.7) | Mustard `#CFB500` | **Black** (10.3) ⚠ | Buttermilk `#F7F4A2` | Black |
| 5 | Self-Management and Organisation | Lime `#C5E86C` | Black (15.1) | Zucchini `#1C4220` | White | Lime Cream `#EFF4A4` | Black |
| 6 | Responsibility and Stewardship | Seagreen `#00B2A2` | Black (7.9) | Sherwood `#024638` | White | Swans Down `#D7EFE7` | Black |
| 7 | *(unassigned)* | Bondi Blue `#008EAA` | Black (5.4) | Cyprus `#003540` | White | Mystic `#DCEBEC` | Black |
| 8 | Practical Skills and Technical Application | Denim `#326295` | **White** (6.3) | Night `#041E42` | White | Crushed Ice `#D5EBEE` | Black |
| 9 | Knowledge and Conceptual Understanding | Twilight `#514689` | **White** (8.1) | Dark Indigo `#201547` | White | Periwinkle `#DCD3E7` | Black |
| 10 | Independent Learning and Collaboration | Valentine Pink `#E56DB1` | Black (7.2) | Plum `#621244` | White | Powder Pink `#F2DEE9` | Black |

⚠ **Mustard (4S) is not dark.** It's the one Shadow that needs black text. For
domain 4, use Dark = Mustard with black text, and Darkest = `#343433` (the
Greyscale Darkest). Or set white banners on the Shadow of another domain.

Main colours are mid-tones. Five of them need **black** text and three need
**white**. That's why Main is the Accent role (bars and rules) rather than a
fill for text.

### Choosing the Bestae domain colour

- A document or unit about one domain of learning uses that domain's H/S/T set
  throughout.
- A document without a single domain uses **1 (Jazzberry)**, the brand default.
- One set per document. Don't mix domain colours on a page, except in a key or
  legend that explains them.

## How switching layers works in Word

Word can recolour a whole document by changing its **theme colours**, but only
where fills and borders reference a **theme slot** rather than a fixed hex value.
So:

1. **Every fill and border uses a theme colour.** In Word's colour picker,
   choose a colour from the "Theme Colours" rows (for example "Accent 6", "Background
   2"), not "More colours…". In the XML this is `w:themeFill="accent6"` or
   `w:themeColor="accent6"`, not only `w:fill="4C4D4C"`.
2. **Each layer is a theme colour set** with the slots in the role table above:
   - `Greyscale for Printing` (existing);
   - `Bestae – 1 Jazzberry` … `Bestae – 10 Valentine Pink`, one per domain, with
     `dk1` = `#000000`, `lt1` = `#FFFFFF`, `lt2` = *n*T, `accent1` = *n*T,
     `accent4` = *n*H, `accent6` = *n*S, `dk2` = *n*S. Fill the remaining accents
     with the same set: `accent2` = *n*T, `accent3` = *n*H, `accent5` = *n*S.
3. **To switch:** Design → Colours → pick the other set. Fills, banners and
   borders recolour; type doesn't move.
4. **After switching**, check the text contrast rule. Domains 1, 8 and 9 need
   white text on Accent (Main), and domain 4 needs black text on Dark (Mustard).

The current Bestae theme puts brand colours in the `dk1` and `lt1` slots, which
makes "Text 1" Jazzberry and "Background 1" Tomato. That breaks any text or fill
set to the theme defaults. The new Bestae theme sets must keep `dk1` black and
`lt1` white.

## Printing

- **Greyscale** documents print on mono or colour printers identically. They're
  designed for photocopying.
- **Bestae** documents printed in mono lose colour meaning: Tints become very
  light grey, and Mains become mid-greys of different darkness. Never rely on
  colour alone. Labels must name the domain or category in words (see the
  `word-tables` accessibility rules).
- Large fills of Dark or Darkest use a lot of toner. Keep them to banners and
  header rows.
