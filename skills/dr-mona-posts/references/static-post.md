# Building a single static post

Read `composition.md` and design the layout. `layout-map.md` has the invariants.

A static post is the same canvas as a carousel message slide, with two removals:

| | Static post |
|---|---|
| Masthead | yes |
| Topic, given full display treatment | yes — the largest thing on the canvas |
| One body of content | yes, in whatever form the composition calls for |
| Handle, bottom-left | yes |
| **Swipe arrow** | **no** — delete the block |
| **CTA artwork** | **no** — it does not fit; that is a carousel |

The stage still needs its bottom 66px clear: the handle is absolute and has left the flow.

Because a static post has nowhere to continue to, it carries more weight than a carousel
slide 1 — it has to be complete on its own. That usually argues for a **more restrained**
composition, not a busier one: one idea, set large, with real air around it.

## Size

`1080 × 1080` by default. `1080 × 1350` portrait is allowed when the row needs more air —
only the middle of the map stretches; the masthead, handle and edge padding are unchanged.

## How much content fits

One body of content, whatever its form — a row of three, a stack of four rows, a single
panel, a statistic, a quote with no panel at all. The archetypes are in `composition.md`.

The density limit is real even though the form is free: a title, a mantra, a lede, a
content row, a closing line *and* a CTA on one square was rejected as "too much bloated".
If the content will not sit comfortably, **split it into a carousel** — never compress it,
and never shrink the type to make it fit.

## Files

```
ready-posts/YYYY-MM-DD/post-NN-topic/
  slide-01.html
  output/slide-01.png     2160 × 2160
```

Start from `templates/frame-square.html` and delete the `.swipe-cue` block.
`examples/static-square.html` shows one finished treatment — read it for craft, not to
copy its layout.
