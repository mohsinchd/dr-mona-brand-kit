# The CTA slide

The CTA is a **full page**, not an enlarged strip. It is centre-anchored throughout,
which is what makes it read as a closing card rather than a repeat of the message slide.

```
centred glass circle (138px) holding the logo mark in --accent, 86px
   ↳ concentric "welcome rings" behind it: r=122 solid, r=168 dashed, r=216 faint
DR. MONA ALI   (30px, 3px tracking, cream)
subtitle       (13px, 2.6px tracking, uppercase)
─── EYEBROW ───
Headline line 1   (Playfair 900, 66px, --ink)
Headline line 2   (Caveat 700, 100px, --accent, squiggle underline)
lede              (24px, max-width 790px)
leaf ornament     (margin-top:auto — splits the slack either side)
▸ the client's CTA artwork on a glass card
handle bottom-left
```

No swipe arrow on the last slide.

## The logo mark inside the glass circle

The shipped `logo-plum-mark.png` belongs on a **plum or lavender ground only**. On any
other ground it is a second hue, which the brand does not allow. For every other ground:

```bash
python3 scripts/tint_logo.py "<your --accent hex>"
```

It writes a new `logo-<hex>-mark.png` beside the originals and touches nothing else.
Point the template's `<img src>` at it.

## The CTA artwork is a supplied asset — use it, do not typeset one

`assets/cta/cta.png` is the client's own 1080×297 RGBA strip: hours, "Book your
appointment now:", the WhatsApp pill, her photo, name and credentials.

- Use the derived **`assets/cta/cta-plum-trimmed.png`** (trimmed to ink +12px, then 2×
  upscaled — 1820 × 440, **aspect 4.136**). The sage variant is `cta-trimmed.png`.
- **Re-tint it to the post's `--accent`, not to the ground.** The glass panel is a pale
  version of the ground, so a ground-tinted strip washes out on it — on a sage ground the
  sage strip's "DR. MONA" goes nearly invisible. The dark accent holds.
  `python3 scripts/retint_cta.py "<accent hex>"`
- **Budget ~250px of canvas height** for it at full content width.
- It must sit on a **glass panel** — its black text needs a light ground.
- **It does not contain the handle** — place the handle separately, bottom-left.
- **Never overwrite `cta.png`.** Re-tinting writes a new sibling file —
  `python3 scripts/retint_cta.py <hex>`.

## Real contact data — always these

```
MON-SAT | 6:00 – 9:00 PM   ·   0315-7090609   ·   MBBS, MD, MRCPsych(UK)
@dr.monaalisardar
```

Briefs that supply placeholders (`dr-mona.com`, `1-800-…`) are ignored in favour of these.

Start from `templates/slide-cta.html`.
