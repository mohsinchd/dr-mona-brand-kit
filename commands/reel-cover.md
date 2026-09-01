---
description: Build a 1080x1920 Dr. Mona reel cover and export the PNG
argument-hint: "<topic / hook> [ground: sage|#HEX] [photo: path/to/image.jpg] [extra notes]"
---

Build a **reel cover** (1080 × 1920) for @dr.monaalisardar using the `dr-mona-posts` skill.

Load the skill now and follow it. Read `references/reel-cover.md` before writing any HTML.

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

**Then**

1. `python3 scripts/derive_colors.py <ground>` — take `--duo-lo` / `--duo-hi` from it too.
2. Copy `templates/reel-cover.html` into `reels/YYYY-MM-DD/reel-NN-topic/`.
3. Render with `python3 scripts/render.py cover.html --height 1920`, **open the PNG and
   look at it**, and check the type sits inside the safe band.
4. Report the output path and anything you assumed.
