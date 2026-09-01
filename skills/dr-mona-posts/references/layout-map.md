# The element map — fixed for every post and every slide

Canvas is **1080 × 1080**. Portrait 1080 × 1350 is allowed; only the middle stretches.
Reel covers are 1080 × 1920 and have their own map (`reel-cover.md`).

```
┌────────────────────────────────────────────────────────────┐
│ ①  masthead: logo mark + wordmark        top-left, y=24    │
│                                                            │
│ ②  title block                              centred        │
│      topic glyph                                           │
│      ─── EYEBROW ───   (17px, 6px tracking, --accent)      │
│      LINE ONE          (Playfair 900 caps, 88px)           │
│      LINE TWO          (Playfair 900 caps ITALIC, 88px)    │
│      ▔▔▔▔▔▔▔▔▔▔  3px rule, 340px + 170px hairline          │
│                                                            │
│ ③  supporting line / mantra                 centred        │
│ ④  lede paragraph              centred, max-width 820px    │
│                                                            │
│ ⑤  ONE content row  (three glass cards)   margin-top:auto  │
│                                                            │
│ ⑥  closing line     (Caveat, centred, leaf glyph each side)│
│                                                            │
│ ⑦ handle bottom-LEFT          ⑧ swipe arrow bottom-RIGHT   │
└────────────────────────────────────────────────────────────┘
```

| # | Element | Exact placement | Notes |
|---|---|---|---|
| ① | Masthead | flow, `padding-top:24px`, left-aligned | mark 54px tall + `DR. MONA ALI` 22px / subtitle 11.5px |
| ② | Title block | flow, centred, `margin-top:26px` | see below |
| ③ | Mantra | flow, centred, `margin-top:22px` | supporting size — never rivals ② |
| ④ | Lede | flow, centred, `margin:20px auto 0`, `max-width:820px` | 25px / 1.5 |
| ⑤ | Content row | flow, `margin-top:auto` | pins the row low and absorbs slack |
| ⑥ | Closing line | flow, centred, `margin-top:24px` | last flowed element |
| ⑦ | Handle | **absolute** `left:var(--pad-edge); bottom:26px` | 20px Poppins 600 cream — bottom-left on **every** slide |
| ⑧ | Swipe arrow | **absolute** `right:var(--pad-edge); bottom:32px` | carousel slides `1 … N-1` only |

⑦ and ⑧ are absolute, so they leave the flow — **the stage needs `padding-bottom:66px`**
or the closing line collides with them.

```css
.stage{ position:absolute; inset:0; z-index:5;
        display:flex; flex-direction:column;
        padding:24px var(--pad-edge) 66px; }
```

③ and ④ are optional. Use one or the other on a dense slide, both only when the row is
light. Dropping both is fine — the title block plus the row is a complete composition.

### Never on any slide
- Pagination dots.
- A "SWIPE NEXT" label — the arrow alone carries it.
- A `DM` monogram — the real logo mark replaces it.
- The handle anywhere other than bottom-left.

---

## The title block — the occasion outranks the slogan

The occasion or topic is the **largest thing on the slide**. A slogan or mantra is
support. Getting this backwards has been rejected before.

```html
<div class="day">
  <svg class="ribbon">…</svg>                            <!-- topic glyph, 40px -->
  <div class="eyebrow"><i></i><span>Awareness</span><i></i></div>
  <h1><span class="a">World Suicide</span>
      <span class="b">Prevention Day</span></h1>          <!-- .b is italic -->
  <div class="rules"><i></i><i></i></div>
</div>
```

- Both lines **Playfair Display 900 caps at 88px**, `line-height:.96`.
- **Line two is italic.** The roman/italic pair *is* the styling — no colour change, no
  outline, no second hue.
- Eyebrow rules fade outward: `linear-gradient(90deg, transparent, rgba(accent,.55))`,
  mirrored on the right.
- Rules beneath: 340px × 3px at 72% opacity, then 170px × 1.6px at 42%, 5px apart.
- **`margin-top:26px` on `.rules` is a minimum** — less and the rule collides with
  Playfair italic descenders.
- A very long title may drop to 78px, or split across three lines with the last italic.
  Below 72px, shorten the words instead — the size is the point.
- **Line two is the one that overruns.** Playfair italic is noticeably wider than the
  roman at the same size, so a line-two of about 16 characters or more will reach the
  edge at 88px. Check the render, not the source.

---

## Typography — four voices, always the same four

| Role | Face | Size | Notes |
|---|---|---|---|
| Display heading | Playfair Display 900 | 88px caps | line two italic |
| Secondary heading | Playfair Display 900 | 54–66px | roman + italic mix on one line |
| Script accent | **Caveat 700** | 1.35 × the serif it sits beside | one accent word or one closing line — never more |
| Everything else | Poppins 400–700 | below | eyebrows, lede, card copy, handle, CTA |

```
eyebrow 17px / 6px tracking   ·  lede 25px / 1.5
card heading 27px / 3.4px tracking   ·  card body 20px / 1.45
handle 20px   ·  masthead wordmark 22px   ·  masthead subtitle 11.5px
```

**The Caveat underline squiggle** (under an accent word) needs `bottom:-9px` on the SVG
and `line-height:1.12` on its span, or it reads as a strikethrough.

Load all three from Google Fonts — headless Chrome fetches them at render time:

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700;1,900&family=Poppins:wght@400;500;600;700&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
```

---

## Glass panels

Every card and every panel uses one recipe. **Never mix a glass panel with an opaque one
on the same slide.**

```css
.card, .cta{
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

**Illustration disc inside a card:** 96px circle, `background:rgba(ground-deep,.30)`,
`border:1.5px solid rgba(accent,.34)`, holding a **48-viewBox** hand-drawn line
illustration at 51px, stroke 1.9. Draw at 48, not 24 — 24-viewBox UI icons look thin here.

---

## Background linework

Every canvas carries three quiet layers under the content, in this order:

1. `.canvas::before` — two radial washes: a light one top-centre, a dark one bleeding off
   the bottom. This is what gives the flat ground its depth.
2. `.art` — an inline `<svg viewBox="0 0 1080 1080">` holding the drawn linework: soft
   radial glow ellipses, two or three long horizontal curves in `--ground-deep`, a
   scatter of `--accent` dots at ~46% opacity, and a leaf/frond flourish in the bottom
   corners.
3. `.canvas::after` — a fractal-noise grain tile at ~26% opacity. It is what stops the
   gradients from banding.

Vary the linework per topic — different curves, a different flourish, a different glow
placement. That is where a post gets its own character; the element map does not move.
