#!/usr/bin/env python3
"""
Re-tint the client's CTA artwork from its sage green to a new ground hue.

    python3 retint_cta.py "#4B3A61"                 -> assets/cta/cta-4b3a61.png
                                                       + assets/cta/cta-4b3a61-trimmed.png
    python3 retint_cta.py sage --name mypost        -> a named sibling file
    python3 retint_cta.py "#4B3A61" --src path/to/cta.png --out-dir path/

ALWAYS writes new sibling files. The client's original cta.png is never touched.

Needs Pillow and NumPy:  python3 -m pip install pillow numpy

Why it works: the strip uses a single sage tone (~RGB 120,155,130) throughout, so one hue
remap catches all of it. The mask is feathered in HSV — hard thresholds leave jagged
fringes on antialiased type — and the saturation floor is what protects her photograph
(skin is orange-hued, the white sari is desaturated).
"""
import argparse
import colorsys
import os
import sys

try:
    import numpy as np
    from PIL import Image
except ImportError:
    sys.exit("retint_cta.py needs Pillow and NumPy:\n"
             "  python3 -m pip install pillow numpy")

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SRC = os.path.join(HERE, "..", "assets", "cta", "cta.png")

PRESETS = {"sage": "#799D84", "lavender": "#B8A9C9", "plum": "#4B3A61",
           "clay": "#C9A695", "sky": "#A9BFCF", "night": "#2F3A44"}


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"not a hex colour: {h!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def smoothstep(x, lo, hi):
    t = np.clip((x - lo) / (hi - lo), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def rgb_to_hsv_arr(rgb):
    """rgb float 0..1, shape (...,3) -> h,s,v each (...,) with h in degrees."""
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    mx, mn = rgb.max(-1), rgb.min(-1)
    d = mx - mn
    h = np.zeros_like(mx)
    nz = d > 1e-9
    idx = nz & (mx == r)
    h[idx] = ((g - b)[idx] / d[idx]) % 6
    idx = nz & (mx == g)
    h[idx] = ((b - r)[idx] / d[idx]) + 2
    idx = nz & (mx == b)
    h[idx] = ((r - g)[idx] / d[idx]) + 4
    h = h * 60.0
    s = np.where(mx > 1e-9, d / np.maximum(mx, 1e-9), 0.0)
    return h, s, mx


def hsv_to_rgb_arr(h, s, v):
    h = np.mod(h, 360.0) / 60.0
    i = np.floor(h).astype(int)
    f = h - i
    p, q, t = v * (1 - s), v * (1 - s * f), v * (1 - s * (1 - f))
    i = i % 6
    out = np.zeros(h.shape + (3,), dtype=np.float64)
    for k, (rr, gg, bb) in enumerate([(v, t, p), (q, v, p), (p, v, t),
                                      (p, q, v), (t, p, v), (v, p, q)]):
        m = i == k
        out[m, 0], out[m, 1], out[m, 2] = rr[m], gg[m], bb[m]
    return out


def retint(src, target_hex):
    tr, tg, tb = (c / 255 for c in hex_to_rgb(target_hex))
    target_h = colorsys.rgb_to_hsv(tr, tg, tb)[0] * 360.0

    im = Image.open(src).convert("RGBA")
    a = np.asarray(im).astype(np.float64) / 255.0
    rgb, alpha = a[..., :3], a[..., 3]
    h, s, v = rgb_to_hsv_arr(rgb)

    # feathered selection of the sage range, with a saturation floor that spares her photo
    mask = (smoothstep(h, 72, 92)
            * (1 - smoothstep(h, 158, 182))
            * smoothstep(s, 0.07, 0.15))

    # hold the value: purple reads perceptually darker at equal HSV value, and darkening
    # it once cost the black phone number its contrast
    new = hsv_to_rgb_arr(np.full_like(h, target_h),
                         np.minimum(s * 1.42, 0.46),
                         v * 0.86 + 0.14 * v)          # ~= hold v
    m = mask[..., None]
    out = rgb * (1 - m) + new * m
    return Image.fromarray(
        (np.dstack([out, alpha]) * 255).round().clip(0, 255).astype(np.uint8), "RGBA")


def trim(im, pad=12, upscale=2):
    """Trim to the ink plus `pad`, then upscale — matches cta-*-trimmed.png (aspect 4.136)."""
    a = np.asarray(im)
    ink = a[..., 3] > 8
    rows, cols = np.where(ink.any(1))[0], np.where(ink.any(0))[0]
    if not len(rows) or not len(cols):
        return im
    t, b = max(0, rows[0] - pad), min(a.shape[0], rows[-1] + 1 + pad)
    l, r = max(0, cols[0] - pad), min(a.shape[1], cols[-1] + 1 + pad)
    cut = im.crop((l, t, r, b))
    return cut.resize((cut.width * upscale, cut.height * upscale), Image.LANCZOS)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("colour", help="target hex, or a preset: " + ", ".join(PRESETS))
    ap.add_argument("--src", default=DEFAULT_SRC, help="source CTA strip (never modified)")
    ap.add_argument("--out-dir", default=None, help="where to write (default: beside --src)")
    ap.add_argument("--name", default=None, help="slug for the new files (default: the hex)")
    args = ap.parse_args()

    target = PRESETS.get(args.colour.lower(), args.colour)
    try:
        hex_to_rgb(target)
    except ValueError as e:
        sys.exit(f"error: {e}")

    src = os.path.abspath(args.src)
    if not os.path.exists(src):
        sys.exit(f"source not found: {src}")
    out_dir = os.path.abspath(args.out_dir or os.path.dirname(src))
    os.makedirs(out_dir, exist_ok=True)
    slug = args.name or target.lstrip("#").lower()

    full = os.path.join(out_dir, f"cta-{slug}.png")
    trimmed = os.path.join(out_dir, f"cta-{slug}-trimmed.png")
    for p in (full, trimmed):
        if os.path.abspath(p) == src:
            sys.exit("refusing to overwrite the source. Pass a different --name.")

    im = retint(src, target)
    im.save(full)
    tm = trim(im)
    tm.save(trimmed)

    print(f"source (untouched): {src}")
    print(f"  wrote {full}      {im.width} x {im.height}")
    print(f"  wrote {trimmed}   {tm.width} x {tm.height}  "
          f"(aspect {tm.width / tm.height:.3f})")
    print("Place the trimmed file on a glass panel — its black type needs a light ground.")


if __name__ == "__main__":
    main()
