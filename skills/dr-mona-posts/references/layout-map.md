# The invariants — furniture, type, material

What every post has in common. **This is not a layout.** The arrangement is designed per
post — see `references/composition.md`.

Canvas is **1080 × 1080**. Portrait 1080 × 1350 and reel 1080 × 1920 are allowed; the
furniture below does not change with the canvas, only the space between it does.

---

## 1. The furniture — four fixed elements

```
┌────────────────────────────────────────────────────────────┐
│ ① masthead — top, left or centred                          │
│                                                            │
│                                                            │
│              ← everything in here is designed →            │
│                     (composition.md)                       │
│                                                            │
│                                                            │
│ ② handle bottom-LEFT           ③ swipe arrow bottom-RIGHT   │
└────────────────────────────────────────────────────────────┘
```

| # | Element | Placement | Spec |
|---|---|---|---|
| ① | Masthead | top, `padding-top:24px`. **Left-aligned by default**; centred is allowed, and is the usual choice on a closing card. | logo mark 54px + `DR. MONA ALI` 22px / subtitle 11.5px, in `--cream` |
| ② | Handle | **absolute** `left:var(--pad-edge); bottom:26px`. Never anywhere else, on any slide. | `@dr.monaalisardar`, 20px Poppins 600, `rgba(cream,.92)` |
| ③ | Swipe arrow | **absolute** `right:var(--pad-edge); bottom:32px`. Carousel slides `1 … N-1` only. | a bare 200px arrow, `rgba(cream,.92)` |

`--pad-edge` is **46px** on square and portrait, **78px** on a reel cover.

② and ③ are absolute, so they have left the flow — **keep the bottom 66px of the stage
clear** or whatever you compose will collide with them.

### Never, on any slide
- Pagination dots.
- A "SWIPE NEXT" label — the arrow alone carries it.
- A `DM` monogram — the real logo mark replaces it.
- The handle anywhere other than bottom-left.

### The swipe arrow
```html
<div class="swipe-cue" aria-label="Swipe for the next slide">
  <svg viewBox="0 0 200 16" fill="none">
    <path d="M2 8H176" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>
    <path d="M174 1.4 198 8 174 14.6Z" fill="currentColor"/>
  </svg>
</div>
```

---

## 2. Hierarchy — the one rule about arrangement

**The occasion outranks the slogan.** The topic or awareness day is the largest thing on
the slide; a mantra is support. Getting this backwards has been rejected before.

That is a rule about *rank*, not about position or form. The topic can be centred, ranged
left, split across a photograph or set as one oversized word — as long as it is
unmistakably the thing the eye hits first.

---

## 3. Typography — four voices, always the same four

| Role | Face | Typical size | Notes |
|---|---|---|---|
| Display | Playfair Display 900 | 88px caps on a square; up to 300px for a hero figure | pair roman with italic — that pairing *is* the styling; no colour change, no outline |
| Secondary | Playfair Display 900 | 54–66px | roman + italic mix on one line |
| Script accent | **Caveat 700** | ≈1.35 × the serif beside it | one accent word or one closing line per slide — never more |
| Everything else | Poppins 400–700 | below | eyebrows, lede, card copy, handle, CTA |

```
eyebrow 17px / 6px tracking   ·  lede 25px / 1.5
card heading 27px / 3.4px tracking   ·  card body 20px / 1.45
handle 20px   ·  masthead wordmark 22px   ·  masthead subtitle 11.5px
```

**These are starting points, not a fixed scale.** Scale them to the composition — a hero
figure wants 260px, a quote plate wants 110px, a stacked-row list wants its headings at
32px. What must hold is the *ratio*: roughly 3.5× / 1.6× / 1× between display, secondary
and body. Two elements within 15% of each other's size read as a mistake.

**Larger is almost always the right call.** This has been asked for four separate times.
When something does not fit, buy the space from spacing and layout — never from font size.

**Playfair italic is noticeably wider than the roman** at the same size, so a long italic
line is what overruns the canvas first. Check the render, not the source.

**The Caveat underline squiggle** (under an accent word) needs `bottom:-9px` on the SVG and
`line-height:1.12` on its span, or it reads as a strikethrough.

Load all three from Google Fonts — headless Chrome fetches them at render time:

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700;1,900&family=Poppins:wght@400;500;600;700&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
```

---

## 4. Glass — the one panel material

Whatever form a panel takes — a card, a strip, a circle, a full-width plate — it uses this
recipe. **Never mix a glass panel with an opaque one on the same slide.**

```css
.glass{
  background:var(--panel);
  -webkit-backdrop-filter:blur(22px) saturate(1.28);
          backdrop-filter:blur(22px) saturate(1.28);
  border:1.5px solid rgba(255,255,255,.55);
  border-radius:24px;
  box-shadow:0 16px 36px rgba(48,36,62,.16),
             inset 0 1px 0 rgba(255,255,255,.80),
             inset 0 0 0 1px rgba(75,58,97,.09);
}
```

- The **gradient** is what sells it as glass. A flat `rgba()` fill at 84% reads as "full
  white background" and has been rejected.
- The border is a **light edge**, not a coloured hairline.
- Put real background linework **behind** the panels — seeing it through the glass is the
  proof of the material.
- Glass is a **pale version of the ground**. Anything sitting on it must be dark enough to
  survive that: `--ink` / `--ink-soft` for type, `--accent` for marks.
- A slide with no panels at all is a legitimate composition — often the strongest one.

**Illustration disc:** 96px circle, `background:rgba(ground-deep,.30)`,
`border:1.5px solid rgba(accent,.34)`, holding a **48-viewBox** hand-drawn line
illustration at 51px, stroke 1.9. Draw at 48, not 24 — a 24-viewBox UI icon looks thin at
this size.

---

## 5. The field — depth under everything

Every canvas carries three quiet layers beneath the content:

1. **A wash** — a light radial from above, a darker one bleeding off the bottom. This is
   what stops the flat ground looking like a colour swatch.
2. **Drawn linework** — an inline `<svg class="art" viewBox="0 0 1080 1080">` in
   `--ground-deep` and `--accent`. **What that linework is, is a design decision.** Long
   curves, concentric arcs, a dot field, rings, botanical fronds, a faint grid, rays, soft
   blobs. Vary it per post — this is where a slide gets its character.
3. **Grain** — a fractal-noise tile at ~26% opacity. It is what stops the gradients
   banding. Keep it.

Style SVG through CSS classes (`.curves{ stroke:var(--ground-deep) }`) — a
`stroke="var(--accent)"` *attribute* does not resolve.

---

## 6. Colour, on which surface

| Sits on | Use |
|---|---|
| the ground | `--ink` headlines (`--cream` on a dark ground); `--cream` for light type; `--accent` for icons, rules, keylines, script accents |
| glass | `--ink` headings, `--ink-soft` body, `--accent` marks |

**Type is never set in the accent hue on the ground.** The accent is for marks, not words —
the one exception being a Caveat accent word, which is a mark as much as a word.
