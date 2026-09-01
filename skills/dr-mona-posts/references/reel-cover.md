# Building a reel cover

**1080 × 1920.** A different composition from the square posts — one alignment system
(left), one photograph, type living in the air above it.

## The crop that governs everything

Instagram crops the cover to **4:5 in the profile grid** and overlays the caption near the
bottom. So:

> **Everything important sits between y = 300 and y = 1600.**

The masthead can sit above it; the contact block and handle sit below it and are expected
to be partly hidden in the grid.

## Map

| Element | Placement |
|---|---|
| Masthead — mark 72px + wordmark 27px | `left:var(--pad-edge); top:104px` |
| Type block | `left:var(--pad-edge); top:340px; width:928px` |
| Headline line 1 | Playfair 900 caps, **118px**, `line-height:1.0` |
| Headline line 2 | Playfair 900 **italic, not caps**, **157px**, `line-height:.96` |
| Rules | 326px × 3px, then 168px × 1.6px, 6px apart, `margin-top:46px` |
| Lede | 42px / 1.38, width 706px, `margin-top:38px` |
| Contact block | `left:var(--pad-edge); bottom:198px` — hours 34px, "Book your appointment now:" 26px, WhatsApp pill 76px tall |
| Handle | `left:var(--pad-edge); bottom:96px`, 26px |

`--pad-edge` is **78px** on a reel cover, not 46px.

The reel cover is the one place the contact details are typeset rather than using the CTA
artwork — the strip's 4.136 aspect does not work in a 9:16 column. Use the exact strings
from `cta-slide.md`.

## The photograph

Full-bleed from `top:900px` down, feathered into the ground with a mask gradient so it
emerges from the field rather than sitting in a box.

```css
.photo{ position:absolute; left:0; right:0; top:900px; bottom:0; z-index:2; }
.photo .frame{ position:absolute; inset:0; overflow:hidden; isolation:isolate;
  -webkit-mask-image:linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,.16) 5%,
      rgba(0,0,0,.58) 12%, rgba(0,0,0,.90) 19%, #000 25%);
          mask-image:linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,.16) 5%,
      rgba(0,0,0,.58) 12%, rgba(0,0,0,.90) 19%, #000 25%); }
.photo img{ position:absolute; left:50%; transform:translateX(-50%);
            width:1240px; top:-392px; display:block;
            filter:grayscale(1) brightness(1.03) contrast(1.08); }
```

### Duotone — grade any photo to the ground

Two blend layers over a desaturated image, plus ~16% of the untreated frame back through
so it still reads as a photograph:

```css
.photo .lo{ position:absolute; inset:0; background:#26402F; mix-blend-mode:lighten; }   /* shadows → deep ground */
.photo .hi{ position:absolute; inset:0; background:#DAE7DE; mix-blend-mode:multiply; }  /* highlights → pale ground */
.photo .raw{ position:absolute; inset:0; overflow:hidden; opacity:.16; }
.photo .raw img{ filter:none; }
```

`.lo` is the ground at ~lightness .20, `.hi` at ~lightness .88 — `derive_colors.py` prints
both as `--duo-lo` / `--duo-hi`. Then a radial vignette and a vertical wash weight the
bottom so the type and the contact block stay legible over it.

**Drop-in replacement:** the photo path is the only thing that changes. Any image saved to
the reel's own `assets/` folder is graded to the palette by this CSS on render — no code
change.

## Restraint

- **One hue plus white.** No third colour anywhere on a reel cover.
- A white panel behind a single word is the campaign's signature device — **it appears
  exactly once per cover**, on the one word that carries the whole idea.
- Nothing in the imagery depicts distress or implies a method (`copy-voice.md`).
- Faces framed away from camera when the image is generated rather than licensed.

## Files

```
reels/YYYY-MM-DD/reel-NN-topic/
  cover.html
  assets/           the photograph
  output/cover.png  2160 × 3840
```

```bash
python3 scripts/render.py cover.html --height 1920
```

Start from `templates/reel-cover.html`.
