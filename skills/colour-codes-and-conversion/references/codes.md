# Colour codes: reference (source: llA, The Colour Palette Studio; Co75, Flux Academy; 9jm, Jack Watson)

## RGB
- Each channel (red, green, blue) runs 0–255, which is **256 levels** (0% to 100% intensity). It suits screens because pixels are made of R, G and B sub-pixels.
- Format: `rgb(R, G, B)`. Pure red is `rgb(255, 0, 0)` and pure blue is `rgb(0, 0, 255)`.
- Darker versions of a colour have **lower numbers across the board**. A colour with no black in it has at least one channel near 255.

## HEX (hexadecimal, base 16)
- `#RRGGBB`: two digits each for red, green and blue. It's **just another way of writing RGB**. At 7 characters it's much shorter than the ~17 characters of `rgb(...)`, so it's used in CSS and JavaScript.
- Why base 16? 256 = 16 × 16, so each channel fits exactly in two base-16 digits.
- Digits: 0–9, then A = 10, B = 11, C = 12, D = 13, E = 14, F = 15. **A hex code can never contain G–Z.**
- Shorthand: `#FA0` means `#FFAA00`.

### RGB → HEX by hand (per channel)
1. Divide the value by 16.
2. The whole-number part is the **first digit** (convert 10–15 to A–F).
3. Multiply the remainder (the decimal part) by 16. That's the **second digit**.

Worked example, `rgb(184, 52, 224)`:
- Red 184 ÷ 16 = 11.5. 11 = **B**, and 0.5 × 16 = **8**, giving **B8**.
- Green 52 ÷ 16 = 3.25. **3**, and 0.25 × 16 = **4**, giving **34**.
- Blue 224 ÷ 16 = 14. 14 = **E**, and 0 × 16 = **0**, giving **E0**.
- Result: **#B834E0**, a bright purple leaning blue.

### HEX → RGB by hand
Each pair = (first digit × 16) + second digit. `B8` = 11 × 16 + 8 = 184.

## HSB / HSL
Hue (0–360° around the wheel), Saturation (grey to vivid), Brightness (HSB) or Lightness (HSL). This is how designers refine a colour in Illustrator or Figma: lowering saturation adds grey, lowering brightness adds black (a shade), and in HSL raising lightness adds white (a tint). (Co75)

## CMYK
- Cyan, magenta, yellow and key (black), each written as a percentage. The four channels match the four printing plates.
- Format: `cmyk(59%, 0%, 24%, 31%)`. A higher K means darker.
- Converting from screen colour depends on the colour profile and paper, so any formula is approximate.

## Pantone
- An industry-standard colour-matching system for reproducing colour exactly across printers and factories.
- The same ink looks different on **coated vs uncoated** stock, so Pantone swatches specify the substrate (e.g. "C" vs "U").
- Essential for packaging, merchandise and brand guidelines. A brand identity deck should show HEX, RGB and CMYK for each colour, plus a Pantone slide if there's packaging. (9jm)
