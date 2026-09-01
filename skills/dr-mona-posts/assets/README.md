# Assets — vector icons, graphics & photo

Canva-style vector building blocks. All SVGs use `currentColor` (stroke or fill),
so the same file recolors to sage / cream / lavender by setting `color`.

```
assets/
├─ icons/        22 line icons (24×24, stroke=currentColor)
├─ graphics/      9 decorative shapes (blobs, waves, dots, sparkles…)
├─ doctor-mona.png   ← YOU add this (Dr. Mona's cut-out photo, ~square PNG)
├─ library.html   visual gallery of everything (open in a browser)
└─ README.md
```

## Icons (assets/icons)
`brain · heart · hand-heart · leaf · lotus · sun · moon · cloud · sparkle · shield ·
chat · phone · whatsapp · clock · calendar · check-circle · quote · pill · star ·
arrow-right · meditation · ribbon`

## Graphics (assets/graphics)
`blob-1 · blob-2 · wave · arc · dot-grid · leaf-branch · sparkle-cluster · rays · half-ring`

## Two ways to use them

**1. Inline SVG (recommended — works everywhere, recolors, no flags).**
Paste the file's SVG markup straight into the template and set `color` (for stroke
icons) or `fill` (for fill icons). This is how the shipped templates do it:
```html
<span class="icon-chip on-sage">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7">…</svg>
</span>
```

**2. CSS-mask utility (`.icon` / `.gfx`) — convenient, needs http or the render flag.**
```html
<span class="icon" style="--icon:url(../assets/icons/leaf.svg);
      font-size:52px; color:var(--color-sage)"></span>
```
SVG-as-mask is blocked on `file://` (null origin). It works when the page is served
over http (e.g. a local server) **or** when exported via `render.sh`, which passes
`--allow-file-access-from-files`. For zero-surprise viewing, prefer inline SVG.

## Dr. Mona's photo
Save her cut-out portrait (transparent or plain background, roughly square) as:
```
assets/doctor-mona.png
```
The CTA footer (`carousel-cta.html`) already points at it and shows a sage circle
until the file exists. Same file can be reused anywhere a portrait is needed.
