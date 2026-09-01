---
description: Build a Dr. Mona Instagram carousel (message slides + CTA slide) and export the PNGs
argument-hint: "<topic> [ground: sage|#HEX] [slides: N] [any extra notes or assets]"
---

Build a **carousel** for @dr.monaalisardar using the `dr-mona-posts` skill.

Load the skill now and follow it. Read `references/carousel.md` and
`references/layout-map.md` before writing any HTML, and `references/cta-slide.md`
before the last slide.

**The user's request:**

$ARGUMENTS

**How to read that request**

- Everything above is the brief. Parse it into the skill's intake contract — `topic`,
  `ground`, `slides`, plus any headline, card copy, assets or notes the user gave.
- **The ground colour is required.** If the user named a colour or a preset, use it. If
  they did not, **ask for it before building** — do not guess, and do not default to sage
  without saying so.
- Anything extra the user wrote — a mood, a must-include line, a supplied image, a
  deadline detail — is an **addition** to the spec, not a replacement for it. Honour it.
  If it collides with a non-negotiable, say which one and offer the nearest on-brand
  alternative rather than silently overriding either.
- **Default to 2 slides**: one message slide + the CTA slide. Go longer only if the
  content has genuinely separate beats. Never pad to reach a slide count.

**Then**

1. Run `python3 scripts/derive_colors.py <ground>` and paste the `:root` block it prints.
2. Copy `templates/slide-content.html` for each message slide and `templates/slide-cta.html`
   for the last one, into `ready-posts/YYYY-MM-DD/post-NN-topic/`.
3. Write the copy yourself — improve on the brief, follow `references/copy-voice.md`, and
   apply the safe-messaging rules if the topic touches suicide, self-harm or addiction.
4. Render every slide with `scripts/render.py`, **open each PNG and look at it**, then
   check the result against the non-negotiables and `references/gotchas.md`.
5. Report the output paths and anything you assumed.
