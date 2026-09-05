# Building a carousel

Read `composition.md` first — the layout is designed per post. `layout-map.md` has the
invariant furniture that is identical on every slide.

## How many slides

> A single square holds: **a title block, ONE content row, and a closing line.**

The CTA does **not** fit alongside that. A post that needs a title, a mantra, a lede, a
content row, a closing line *and* a CTA is a **two-slide carousel**. Do not compress it
onto one canvas — this was learned the hard way ("too much bloated").

**Default: 2 slides.** Go longer only when the content has genuinely separate beats — one
idea per slide, each with its own title block and its own row. Never pad to reach a count.

| Slide | Role | Arrow |
|---|---|---|
| 1 | Message — the topic, given full display treatment, and its content | yes |
| 2 … N-1 | Further beats — one idea each, its own title and its own content | yes |
| N | CTA — the closing card (`cta-slide.md`) | no |

**The closing card must read differently from the message slides.** Flipping the anchor —
message slides ranged left, the closing card centred — is the usual way and it works, but
any clear change of register does: a different density, a bare field where the others had
panels, a single centred column where the others were split.

## A carousel is a set — this is where the variation rule inverts

Between *posts*, differ boldly (`composition.md` §4). Between *slides of one carousel*,
hold together:

**Identical across the slides**
- the ground and every derived token
- the masthead — same mark, same size, same position
- the handle, bottom-left, unmoved
- the type scale and the panel material
- the alignment system: pick one and keep it across the message slides

**Changes between slides**
- the background linework — different curves, a different flourish, the glow moved
- the title wording and its topic glyph
- the content, and how that particular content is arranged within the chosen system

Moving the furniture between slides breaks the set. Changing the *architecture* between
slide 1 and slide 2 of the same carousel breaks it too — that reads as two posts.

## The swipe arrow

Slides `1 … N-1` only. A bare long arrow, no text.

```html
<div class="swipe-cue" aria-label="Swipe for the next slide">
  <svg viewBox="0 0 200 16" fill="none">
    <path d="M2 8H176" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>
    <path d="M174 1.4 198 8 174 14.6Z" fill="currentColor"/>
  </svg>
</div>
```
```css
.swipe-cue{ position:absolute; right:var(--pad-edge); bottom:32px; z-index:6;
            color:rgba(253,252,245,.92); line-height:0; }
.swipe-cue svg{ width:200px; height:16px; display:block; }
```

## Files

```
ready-posts/YYYY-MM-DD/post-NN-topic/
  slide-01.html
  slide-02.html
  output/
    slide-01.png      2160 × 2160
    slide-02.png
```

Start every slide from `templates/frame-square.html`; delete the `.swipe-cue` block on the
last one. `examples/carousel-message.html` and `examples/carousel-cta.html` show finished
slides — read them for craft, not to copy their layout.

Render every slide and **look at all of them together** — a carousel is judged as a set,
and a slide that is fine alone can still break the set.
