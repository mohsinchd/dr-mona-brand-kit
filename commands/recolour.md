---
description: Re-ground an existing Dr. Mona post to a new background colour and re-export
argument-hint: "<path to post folder or slide> to <colour: sage|#HEX>"
---

Re-ground an existing post to a new background colour, using the `dr-mona-posts` skill.

**The user's request:**

$ARGUMENTS

**Do this**

1. Load the `dr-mona-posts` skill and read `references/colour.md`.
2. Find the slide files the user means. If the path is ambiguous, list what you found and
   ask which one — do not guess and overwrite the wrong post.
3. Run `python3 scripts/derive_colors.py <new colour>` and replace **only** the
   `--ground` / `--ground-deep` / `--accent` lines (and `--panel` if the script's dark-ground
   variant applies). Nothing else in the file changes — the layout is fixed.
4. Re-derive the tinted assets for the new ground, to the post's **`--accent`**, not to the
   ground itself:
   - `python3 scripts/tint_logo.py "<accent>"` for the CTA slide's logo mark
   - `python3 scripts/retint_cta.py "<accent>"` for the CTA artwork
   Both write **new sibling files**. Never overwrite `cta.png` or any original.
5. Read the script's contrast report and apply the dark-ground rules if it flags one.
6. Re-render every affected slide, **open each PNG and look at it**, and confirm nothing
   washed out — a colour change moves the contrast of everything sitting on glass.
7. Report which files changed and which new asset files were written.
