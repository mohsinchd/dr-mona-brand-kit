# Gotchas that have actually bitten

Check this list before reporting anything done.

| Symptom | Cause | Fix |
|---|---|---|
| A row of content bleeds past the canvas edge | a `display:flex` row nested in a `flex-direction:column` parent has `min-width:auto` | `width:100%; min-width:0` on the row, **and** trim the content |
| Chrome silently clips ~40px off every edge | the canvas overflowed a window sized exactly to it, because `body` had preview padding | use the shipped templates (padding is behind a `min-width:1200px` media query) or render with `--legacy-crop` |
| Fonts come out as fallbacks | Google Fonts hadn't arrived | `--virtual-time-budget=10000`; the render script already passes it |
| Script underline looks like a strikethrough | the SVG sits at the glyph baseline | `bottom:-9px` on the SVG, `line-height:1.12` on the span |
| Title rule touching the headline | Playfair italic descenders | `margin-top:26px` minimum on `.rules` |
| Closing line running into the swipe arrow | the absolute handle/arrow left the flow | stage `padding-bottom:66px` |
| A divider vanishes on one side of a card | the card's diagonal sheen washes out a flat hairline | gradient rule with faded ends at ~46% cream |
| Type looks washed after a panel change | lower panel opacity lightened the ground beneath it | re-check contrast on **everything** sitting on that panel |
| Glass reads as a plain white box | a flat `rgba()` fill instead of the gradient | use the `--panel` gradient, and put linework behind it |
| Cut-out outline squared off under the feet | dilating a mask at its own bbox size | `np.pad(mask, M)` with `M >` the largest dilation, **before** dilating |
| Logo subtitle turns to mush | the full lockup was scaled below ~250px wide | use the icon-only mark and typeset the wordmark in Poppins beside it |
| The post "feels bloated" | a title, mantra, lede, row, closing line *and* CTA on one canvas | split into a two-slide carousel — never compress |
| A tall stack ends up almost touching the handle | `margin-top:auto` let the stack grow until it hit the stage's `padding-bottom:66px` — which is minimum *clearance*, not a comfortable gap | a full-width panel reads as a hard edge: give the stack `margin-bottom:16-24px` on top of the padding, or drop a row |
| The composition is balanced but forgettable | it was filled, not designed — the slack landed wherever `auto` put it | go back to `composition.md`: name the focal point, then place everything relative to it |
| The title's italic line runs to the canvas edge | Playfair italic is noticeably wider than the roman at the same size | drop line two to 78px, or shorten the words — the italic line is what overruns first, so measure that one |
| Cards are too tall / text overflows a card | card copy longer than ~14 words | cut the copy; do not shrink the type |
