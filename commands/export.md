---
description: Re-render Dr. Mona slide HTML to PNG at 2x
argument-hint: "[path to folder or html files] [portrait|reel]"
---

Re-export slides to PNG using the `dr-mona-posts` skill's renderer.

**The user's request:**

$ARGUMENTS

**Do this**

1. Work out which HTML files to render. With no path given, use the most recent folder
   under `ready-posts/` — say which one you picked.
2. Render:
   ```bash
   python3 scripts/render.py <files>                  # square, 2160 x 2160
   python3 scripts/render.py <files> --height 1350    # portrait, 2160 x 2700
   python3 scripts/render.py <files> --height 1920    # reel cover, 2160 x 3840
   ```
   A file written before this kit — one whose `body` has an unconditional
   `padding:40px` rather than the `@media (min-width:1200px)` guard — needs
   `--legacy-crop`, or Chrome silently clips ~40px off every edge. Check the file before
   rendering rather than after.
3. **Open every PNG and look at it.** Confirm the dimensions, that the fonts loaded
   (Playfair and Caveat, not a fallback serif), and that nothing is clipped at the edges.
4. Report the output paths and pixel sizes.
