---
description: Audit finished Dr. Mona slides against the brand non-negotiables before publishing
argument-hint: "[path to post folder — defaults to the most recent]"
---

Audit finished artwork against the brand rules, using the `dr-mona-posts` skill.

**The user's request:**

$ARGUMENTS

**Do this**

1. Load the `dr-mona-posts` skill. Find the slides (default: the most recent folder under
   `ready-posts/`, and say which one you picked).
2. **Render them if the PNGs are missing or older than the HTML**, then open every PNG and
   look at it. This audit is on the rendered image, not on the source.
3. Check each slide against the skill's non-negotiables and `references/gotchas.md`:
   - handle `@dr.monaalisardar` bottom-left, identical position on every slide
   - bare 200px swipe arrow bottom-right on slides 1…N-1 only; none on the last slide or
     a static post; no dots, no "SWIPE NEXT", no DM monogram
   - the occasion is the largest thing on the slide, not the slogan
   - exactly one content row per canvas
   - glass panels only, never mixed with opaque ones
   - no type set in the accent hue on the ground
   - real contact data — `MON-SAT | 6:00 – 9:00 PM`, `0315-7090609`, `MBBS, MD, MRCPsych(UK)`
   - the client's own CTA artwork, not a typeset substitute
   - one hue: the logo mark and CTA strip tinted to this post's accent, not left plum on a
     non-plum ground
   - fonts actually loaded; nothing clipped at an edge; nothing colliding
   - on a suicide, self-harm or addiction topic, the safe-messaging rules in
     `references/copy-voice.md`
4. Report a short pass/fail list. For each failure, name the slide, the rule, and the fix.
   Do not change any file unless the user asks — this is an audit.
