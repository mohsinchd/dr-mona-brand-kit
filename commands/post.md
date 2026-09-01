---
description: Build a single Dr. Mona Instagram post (static square or portrait) and export the PNG
argument-hint: "<topic> [ground: sage|#HEX] [portrait] [any extra notes or assets]"
---

Build a **single static post** for @dr.monaalisardar using the `dr-mona-posts` skill.

Load the skill now and follow it. Read `references/static-post.md` and
`references/layout-map.md` before writing any HTML.

**The user's request:**

$ARGUMENTS

**How to read that request**

- Parse it into the skill's intake contract — `topic`, `ground`, `size`, plus any
  headline, card copy, assets or notes.
- **The ground colour is required.** Ask for it if the user did not name one.
- Extra instructions from the user are **additions** to the spec. Fold them in; if one
  collides with a non-negotiable, say so and offer the nearest on-brand alternative.
- A static post is **title block → ONE content row → closing line. No CTA, no swipe
  arrow.** If the brief needs a CTA as well, tell the user it is a two-slide carousel and
  build that instead of compressing it — a dense square has been rejected before.
- `portrait` in the request means 1080×1350; render with `--height 1350`.

**Then**

1. `python3 scripts/derive_colors.py <ground>` and paste the `:root` block.
2. Copy `templates/static-square.html` into `ready-posts/YYYY-MM-DD/post-NN-topic/`.
3. Write the copy yourself, following `references/copy-voice.md`.
4. Render with `scripts/render.py`, **open the PNG and look at it**, then check against
   the non-negotiables and `references/gotchas.md`.
5. Report the output path and anything you assumed.
