---
description: Build a single Dr. Mona Instagram post (static square or portrait) and export the PNG
argument-hint: "<topic> [ground: sage|#HEX] [portrait] [any extra notes or assets]"
---

Build a **single static post** for @dr.monaalisardar using the `dr-mona-posts` skill.

Load the skill now and follow it. Read `references/composition.md`,
`references/static-post.md` and `references/layout-map.md` before writing any HTML.

**The user's request:**

$ARGUMENTS

**How to read that request**

- Parse it into the skill's intake contract — `topic`, `ground`, `size`, plus any
  headline, card copy, assets or notes.
- **The ground colour is required.** Ask for it if the user did not name one.
- Extra instructions from the user are **additions** to the spec. Fold them in; if one
  collides with a non-negotiable, say so and offer the nearest on-brand alternative.
- A static post carries **one idea and no CTA, and has no swipe arrow.** How that idea is
  arranged is yours to design. If the brief needs a CTA as well, tell the user it is a
  two-slide carousel and build that instead of compressing it — a dense square has been
  rejected before.
- Because it has nowhere to continue to, a static post usually wants a **more restrained**
  composition than a carousel slide, not a busier one.
- `portrait` in the request means 1080×1350; render with `--height 1350`.


**Design it — do not fill in a template**

This is the step that matters. The skill ships a frame and a set of invariants, not a
layout. Before writing any HTML:

- Read `references/composition.md`.
- **Look at the last two posts** in `ready-posts/` — open the PNGs. The new post must
  differ from them on **at least four** of the eight variation axes.
- If the user attached a **reference image**, read `references/reference-images.md` and
  work from its structure. Take the composition; leave their colours, fonts, marks and
  wording. Say what you took and what you replaced before you spend a render on it.
- **Write the composition down in four lines before you code it** — anchor, focal point,
  support, field, air.
- Then build it into `templates/frame-square.html`. `examples/` shows finished slides:
  read them for craft, never copy their layout. A centred title over three glass cards is
  one archetype of fourteen — using it because it is first is the defect this step exists
  to prevent.

**Then**

1. `python3 scripts/derive_colors.py <ground>` and paste the `:root` block.
2. Build from `templates/frame-square.html` into `ready-posts/YYYY-MM-DD/post-NN-topic/`,
   deleting the `.swipe-cue` block.
3. Write the copy yourself, following `references/copy-voice.md`.
4. Render with `scripts/render.py` and **open the PNG and look at it**, then check against
   the non-negotiables and `references/gotchas.md`.
5. **Critique and revise.** Answer the five questions in `references/composition.md` §7,
   fix the weakest thing, and re-render. **At least one revision pass, always** — the
   first render is a draft, not a deliverable.
6. Report the output paths, the composition you chose, and anything you assumed.

