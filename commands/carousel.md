---
description: Build a Dr. Mona Instagram carousel (message slides + CTA slide) and export the PNGs
argument-hint: "<topic> [ground: sage|#HEX] [slides: N] [any extra notes or assets]"
---

Build a **carousel** for @dr.monaalisardar using the `dr-mona-posts` skill.

Load the skill now and follow it. Read `references/composition.md`,
`references/carousel.md` and `references/layout-map.md` before writing any HTML, and
`references/cta-slide.md` before the last slide.

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

Within one carousel the slides are a **set**: hold the ground, masthead, type scale and
alignment system across the message slides, and vary the background artwork and the
content arrangement. The closing card should read differently — that is what makes it land
as a close rather than a repeat.

**Then**

1. Run `python3 scripts/derive_colors.py <ground>` and paste the `:root` block it prints.
2. Build each slide from `templates/frame-square.html` into
   `ready-posts/YYYY-MM-DD/post-NN-topic/`; delete the `.swipe-cue` block on the last one.
3. Write the copy yourself — improve on the brief, follow `references/copy-voice.md`, and
   apply the safe-messaging rules if the topic touches suicide, self-harm or addiction.
4. Render every slide with `scripts/render.py` and **open each PNG and look at it** —
   together, since a carousel is judged as a set.
5. **Critique and revise.** Answer the five questions in `references/composition.md` §7,
   fix the weakest thing, and re-render. **At least one revision pass, always** — the
   first render is a draft, not a deliverable.
6. Report the output paths, the composition you chose, and anything you assumed.

