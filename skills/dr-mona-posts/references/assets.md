# Assets

Everything ships inside this skill under `assets/`. Reference a file with a relative path
from the slide (`../../../` from `ready-posts/YYYY-MM-DD/post-NN-topic/` when the skill's
assets folder has been copied to the project root), or copy the files you need into the
post's own folder. Copying is safer for handover — the folder stays portable.

## Inventory

| Asset | File | Size | Use |
|---|---|---|---|
| Logo mark, cream | `logo/logo-cream-mark.png` | 209×243 | masthead on a coloured ground |
| Logo mark, plum | `logo/logo-plum-mark.png` | 209×243 | CTA glass circle — **plum/lavender grounds only** |
| Logo mark, any hue | `scripts/tint_logo.py "<accent>"` | 209×243 | CTA glass circle on every other ground |
| Full lockup | `logo/logo-cream.png`, `logo-plum.png`, `logo-transparent.png` | 712×361 | never below ~250px wide |
| Original logo | `logo/1.jpg` | 864×534 | **client-supplied — never modify** |
| CTA strip, original | `cta/cta.png` | 1080×297 | **client-supplied — never modify or overwrite** |
| CTA strip, plum | `cta/cta-plum-trimmed.png` | 1820×440, aspect 4.136 | the one to place on a CTA slide |
| CTA strip, sage | `cta/cta-trimmed.png` | 1820×440 | sage-ground posts |
| Portrait medallion | `photos/dr-mona-avatar.png` | 640×640 | small medallion only |
| Portrait cut-outs | `photos/dr-mona-*-cutout.png` | various | **never as the centrepiece** |
| Source portraits | `dr-mona.png`, `photos/image*.jpeg` | various | **client-supplied — never modify** |
| Line icons | `icons/*.svg` | 24 viewBox | 22 icons, `currentColor` |
| Decorative shapes | `graphics/*.svg` | — | 9 blobs, waves, arcs, dot grids |

Icons: `brain · heart · hand-heart · leaf · lotus · sun · moon · cloud · sparkle · shield ·
chat · phone · whatsapp · clock · calendar · check-circle · quote · pill · star ·
arrow-right · meditation · ribbon`

Graphics: `blob-1 · blob-2 · wave · arc · dot-grid · leaf-branch · sparkle-cluster · rays ·
half-ring`

**Inline the SVG** into the slide rather than linking it — SVG-as-CSS-mask is blocked on
`file://`, and inlining lets `currentColor` pick up the accent.

**The card illustration discs are drawn at a 48 viewBox, stroke 1.9** — the 24-viewBox
icons above are for small chips and ornaments. A 24-viewBox icon scaled to 51px looks
thin. Draw a new 48-viewBox illustration per card when the shipped icons don't fit.

## When the user supplies an extra asset

1. Put it in the **post's own** `assets/` folder, not the skill's.
2. Reference it relatively from the slide file.
3. **Grade it to the ground.** A raw full-colour photo on a tinted field breaks the
   palette — apply the duotone in `reel-cover.md` (it works on square posts too).
4. Never modify the original in place.

## Deriving new files — the traps

**Logo off its white ground:** alpha = `clip((255 - rgb.min(axis=2)) * k)` — the **min**
channel, not luminance, or the light sage mark comes out ghosted. `k≈1.6` keeps the
two-tone; `k≈2.8` gives a solid mono. To split the mark from the wordmark, find the first
row with ink at `x < 170` and cut ~18px above it.

**Never scale the full lockup below ~250px wide** — the subtitle turns to mush. Use the
icon-only mark and typeset the wordmark in Poppins beside it.

**Tinting the logo mark:** `python3 scripts/tint_logo.py "#344B3B"` replaces the colour
of `logo-cream-mark.png` while keeping its alpha, and writes a new sibling file. Tint it
to the post's `--accent` — the shipped plum mark is only correct on a plum ground.

**Re-tinting the CTA artwork:** `python3 scripts/retint_cta.py "#4B3A61"` writes a new
sibling file and leaves the original alone. **Tint it to `--accent`, not to `--ground`** —
the glass panel is a pale version of the ground, so a ground-tinted strip washes out on it. It works because the strip uses a single sage
tone ~RGB(120,155,130) throughout, so one hue remap catches all of it:

1. Select in HSV with a **feathered** mask —
   `smoothstep(hue,72,92) · (1-smoothstep(hue,158,182)) · smoothstep(sat,0.07,0.15)`.
   Hard thresholds leave jagged fringes on antialiased type. The saturation floor is what
   protects her photo (skin is orange-hued, the white sari is desaturated).
2. Rebuild as `HSV(target_hue, sat×1.42 capped .46, val×0.86)`, then lerp original→new by
   the mask weight.
3. **Hold or raise the value** when moving green→purple. Purple reads perceptually darker
   at equal HSV value; darkening it cost the black phone number its contrast.
4. Write a **new file**. The client's original stays untouched.

**Cut-out with the brand keyline:** `rembg` with `isnet-general-use`, clean the mask
(`binary_closing`/`opening`, then `binary_erosion` ×3 to kill white fringe), then dilate
for the ring — cream inner ~7px + accent outer ~4px.

> **`np.pad(mask, M)` with `M >` the largest dilation count, BEFORE dilating.**
> `binary_dilation` does not grow the array, so the ring gets clipped flat wherever the
> subject touches its own bbox.

## Free sources when new imagery is needed

Photography: **Unsplash** and **Pexels** (free commercial, no attribution). Illustrations:
**unDraw** (MIT). Fonts: **Google Fonts**. Download locally into the post's `assets/` —
never hotlink in a file that will be rendered later.

Search terms that fit the account: `therapy session`, `hands holding`, `journaling`,
`calm`, `recovery`, `support group`, `sunrise`, `conversation`.
