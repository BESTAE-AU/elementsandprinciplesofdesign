# Colour audit: all four design systems

*29 Sept 2026. Covers the live tokens of BESTAE (v7), Greyscale Workbooklet (v2), MBE Creative Studio (v7) and MCCNS (v3).*

*Two tests:*
- *Readability: WCAG contrast. Body text needs 4.5:1; large text and UI marks need 3:1.*
- *Distinguishability: CIE ΔE colour difference. Under 5 is barely visible and under 10 is easy to confuse.*

> **Status: all recommendations applied (29 Sept 2026).**
> - **BESTAE (v8):** `t5` is now `#E8F6C4`, `t8` is now `#D2DCE8`, and `t10` is now **`#F7D0E6`**. That is pink at 32%, not the 35% `#F6CCE4` proposed below, because denim links on `#F6CCE4` were only 4.42:1. On `#F7D0E6` they are 4.56:1, and it is ΔE 10.0 from `t2`.
> - **Greyscale (v3):** `link` is now `#5E5E5E`, and the coding set is named.
> - **MBE (v8):** `accent-bloom-deep` `#e3008c` and `border-strong` `#a48061` added.
> - **MCCNS:** no change.
>
> The same values are carried into the swatches, the Word template, the PowerPoint copy, the site map, the greyscale skill copy and a Dropbox note.

## Summary

| System | State | Recommended changes |
|---|---|---|
| BESTAE | Text rules are now all passing | **Two domain tint pairs look identical**: re-tint `t5` and `t10` (optionally `t8`) |
| Greyscale | Rules added; two values are weak | Change the Link grey. Formalise a 4-step coding set |
| MBE Creative Studio | Rules added; two gaps have no token | Add a deep-pink token for small CTAs and a visible border token |
| MCCNS | Can't change (school brand) | None. Just the guideline's HEX misprint for the school to fix |

## BESTAE

**1. Recommended: domain tints that can't be told apart.** Panels are coloured by domain, so their tints must look different.

| Pair | ΔE now | Problem |
|---|---|---|
| `t4` Communication `#F7F4A2` vs `t5` Self-Management `#EFF4A4` | **3.4** | Effectively the same pale yellow |
| `t2` Critical Thinking `#F5DADF` vs `t10` Independent Learning `#F2DEE9` | **4.2** | Effectively the same pale pink |
| `t6` Responsibility `#D7EFE7` vs `t8` Practical Skills `#D5EBEE` | 5.9 | Very close pale aqua |

Proposed tints (each is its domain's H colour mixed with white, so they read as that domain):

| Token | Now | Proposed | Nearest other tint (ΔE) | `ink` / own S on it |
|---|---|---|---|---|
| `t5-lime-cream` | `#EFF4A4` | **`#E8F6C4`** (lime 40%) | t4: 17.5 | 14.5 / 10.0 |
| `t10-powder-pink` | `#F2DEE9` | **`#F6CCE4`** (pink 35%) | t1: 9.5 (unassigned), t2: 11.6 | 11.6 / 8.7 |
| `t8-crushed-ice` *(optional)* | `#D5EBEE` | **`#D2DCE8`** (denim 22%) | t7: 7.7 (unassigned), t9: 8.1 | 11.9 / 11.9 |

**2. Keep as is (labelled rule already covers it):**
- Tomato, valentine pink and seagreen print as the same mid-grey (luminance 0.29–0.34).
- Twilight and denim print as similar dark greys.
- The brand book's "always label the domain" rule is the right fix. No colour change can make eight hues distinct in greyscale.

**3. Keep, but watch:** `s4-dark-gold` on `t4` is 4.7:1. That passes, but only just, so use it bold for headers and keep body text in `ink`.

**4. Keep, positive:** BESTAE `ink` `#041E42` and MCC Navy `#001D3E` are ΔE 2.5 apart, i.e. visually the same navy. BESTAE content therefore sits comfortably inside MCCNS-framed documents.

**5. Keep the rule:** `h1-jazzberry` vs MCC Cerise is ΔE 9.4, easy to confuse, so keep jazzberry out of MCCNS work, as the brand books already say.

## Greyscale Workbooklet

1. **Recommended: change `link` from `#898A89` to `#5E5E5E`** (the existing `muted` grey). That takes it from 3.5:1 to 6.5:1 on paper. Or keep links in `ink`, underlined. This also means changing the Hyperlink style in `Greyscale Workbooklet.dotm`.
2. **Recommended: name a coding set.** Make Pale, Accent 2, Accent 4 and Accent 6 the only shades used to tell categories apart. They are 2.2, 1.95 and 1.65:1 apart, versus 1.24–1.3:1 for neighbours. Accents 1, 3 and 5 stay available for decoration.
3. **Keep, as a rule:** Accent 3 takes no text, because it's 4.67:1 with black and 4.50:1 with white, right on the edge. Don't change the value; it's still useful as a fill.
4. **Keep, as a rule:** captions on Pale use Ink, because Muted is 4.0:1 there.

## MBE Creative Studio

1. **Recommended: add `accent-bloom-deep` `#E3008C`** for small pink CTAs with white text (4.52:1). The logo pink `#ff3eb5` stays exactly as it is for the logo and large moments. Today's alternative is green text on pink at bold 19px+, which reads well but limits button sizes.
2. **Recommended: add `border-strong` `#A48061`** for inputs and focus rings (3.0:1 on cream, 3.6:1 on white). It's a warmer, on-brand alternative to using `ink-muted` for borders. Keep `border` for decorative dividers.
3. **Keep, note:** cream and white cards are only 1.2:1 apart (ΔE 8.7), so cards on cream need a `border` or a shadow to read as cards.
4. **Keep:** pink and peach are very different hues (ΔE 81) but similar in lightness. They're fine together, but don't use them as the only difference between two states.

## MCCNS

No changes recommended. It's the school's brand, and the usage rules already handle every failing pair.
- **For the school:** the guideline prints Light Blue's HEX as `#D9DDE2`, but its RGB, CMYK and swatch are `#909DB2`. The PDF should be corrected.
- Cerise is a mid-tone (the "danger zone" on the 3×3 grid), but it passes with white text (7.1:1), so it's fine.
