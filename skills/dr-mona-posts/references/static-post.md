# Building a single static post

Read `layout-map.md` first. A static post uses the same element map with two removals.

**Title block → one content row → closing line.** No CTA, no swipe arrow.

| Element | Static post |
|---|---|
| Masthead ① | yes, top-left |
| Title block ② | yes — the largest thing on the canvas |
| Mantra ③ / lede ④ | optional; one of them, or neither |
| Content row ⑤ | exactly one |
| Closing line ⑥ | yes |
| Handle ⑦ | yes, bottom-left |
| Swipe arrow ⑧ | **no** |
| CTA artwork | **no** — it does not fit; that is a carousel |

Because there is no arrow, the stage's `padding-bottom:66px` still applies: the handle is
absolute and would otherwise collide with the closing line.

## Size

`1080 × 1080` by default. `1080 × 1350` portrait is allowed when the row needs more air —
only the middle of the map stretches; the masthead, handle and edge padding are unchanged.

## Content row options

Three glass cards is the default and the safest. Two variants that hold on one canvas:

- **Two wide cards** — for a contrast pair (myth / fact, before / after). Same glass
  recipe, `grid-template-columns:repeat(2,1fr)`, copy can run to ~24 words.
- **One wide card** — for a single statistic or a pull quote. The illustration disc grows
  to 128px and sits left of the text rather than above it.

Anything that needs four or more cards is a carousel.

## Files

```
ready-posts/YYYY-MM-DD/post-NN-topic/
  slide-01.html
  output/slide-01.png     2160 × 2160
```

Start from `templates/static-square.html`.
