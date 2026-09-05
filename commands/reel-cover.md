---
description: Build a 1080x1920 Dr. Mona reel cover and export the PNG
argument-hint: "<topic / hook> [ground: sage|#HEX] [photo: path/to/image.jpg] [extra notes]"
---

Build a **reel cover** (1080 × 1920) for @dr.monaalisardar using the `dr-mona-posts` skill.

Load the skill now and follow it. Read `references/composition.md` and
`references/reel-cover.md` before writing any HTML.

**The user's request:**

$ARGUMENTS

**How to read that request**

- Parse into `topic`, `ground`, and any photograph, hook wording or notes the user gave.
- **The ground colour is required.** Ask if it is missing.
- If the user supplied a photograph, copy it into the reel's own `assets/` folder as
  `cover.jpg` and retune only `.photo img { width / top }` to frame the subject. The
  duotone grades it to the ground automatically — do not recolour the image by hand.
- If no photograph was given, say so and offer either to ship the cover as a pure type
  composition on the field, or to take a photo path from the user.
- **One hue plus white. No third colour anywhere.**
- Everything important must sit between y = 300 and y = 1600 — Instagram crops the cover
  to 4:5 in the profile grid and puts the caption near the bottom.
- On suicide, self-harm or addiction topics apply the safe-messaging rules in
  `references/copy-voice.md`: nothing depicting distress, nothing implying a method.


**Design it — do not fill in a template**

This is the step that matters. The skill ships a frame and a set of invariants, not a
layout. Before writing any HTML:

- Read `references/composition.md`.
- **Look at the last two posts** in `reels/` — open the PNGs. The new post must
  differ from them on **at least four** of the eight variation axes.
- If the user attached a **reference image**, read `references/reference-images.md` and
  work from its structure. Take the composition; leave their colours, fonts, marks and
  wording. Say what you took and what you replaced before you spend a render on it.
- **Write the composition down in four lines before you code it** — anchor, focal point,
  support, field, air.
- Then build it into `templates/frame-reel.html`. `examples/` shows finished slides:
  read them for craft, never copy their layout. A centred title over three glass cards is
  one archetype of fourteen — using it because it is first is the defect this step exists
  to prevent.

A cover is read at **thumbnail size** first — the hook has to survive being 200px wide.
That argues for fewer elements, larger type and higher contrast than a square post.

**Then**

1. `python3 scripts/derive_colors.py <ground>` — take `--duo-lo` / `--duo-hi` from it too.
2. Build from `templates/frame-reel.html` into `reels/YYYY-MM-DD/reel-NN-topic/`.
3. Render with `python3 scripts/render.py cover.html --height 1920`, **open the PNG and
   look at it**, and check the type sits inside the safe band.
4. Shrink it to thumbnail size and check the hook still reads.
5. **Critique and revise.** Answer the five questions in `references/composition.md` §7,
   fix the weakest thing, and re-render. **At least one revision pass, always** — the
   first render is a draft, not a deliverable.
6. Report the output paths, the composition you chose, and anything you assumed.

