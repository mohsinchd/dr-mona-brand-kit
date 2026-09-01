# Building a carousel

Read `layout-map.md` first — the element map is identical on every slide.

## How many slides

> A single square holds: **a title block, ONE content row, and a closing line.**

The CTA does **not** fit alongside that. A post that needs a title, a mantra, a lede, a
content row, a closing line *and* a CTA is a **two-slide carousel**. Do not compress it
onto one canvas — this was learned the hard way ("too much bloated").

**Default: 2 slides.** Go longer only when the content has genuinely separate beats — one
idea per slide, each with its own title block and its own row. Never pad to reach a count.

| Slide | Role | Composition | Arrow |
|---|---|---|---|
| 1 | Message | **left**-anchored masthead, centred title block, content row, closing line | yes |
| 2 … N-1 | Further beats | same as slide 1, new title block and row | yes |
| N | CTA | **centre**-anchored throughout — `cta-slide.md` | no |

Flipping the anchor (left on the message slides, centred on the last) is deliberate: it
makes the final slide read as a closing card rather than a repeat.

## What stays identical across the slides

- The ground and every derived token.
- The masthead — same mark, same size, same position.
- The handle, bottom-left, unmoved.
- The type scale and the glass recipe.

## What changes between slides

- The background linework: different curves, a different flourish, the glow moved.
- The title block wording and its topic glyph.
- The content row.

That is the whole variation budget. Moving elements between slides breaks the set.

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

Start from `templates/slide-content.html` for the message slides and
`templates/slide-cta.html` for the last one. Render every slide and look at all of them —
a carousel is judged as a set.
