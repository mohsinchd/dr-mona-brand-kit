#!/usr/bin/env python3
"""
Write a logo mark in an arbitrary colour, from the alpha of an existing mark.

    python3 tint_logo.py "#344B3B"                 -> assets/logo/logo-344b3b-mark.png
    python3 tint_logo.py "#344B3B" --lockup        -> the full lockup instead of the mark
    python3 tint_logo.py "#344B3B" --name sage     -> logo-sage-mark.png

The shipped marks are cream and plum. The plum one only belongs on a plum/lavender
ground — on any other ground it reads as a second hue, which the brand does not allow.
Tint a mark to the post's --accent instead, and point the template at the new file.

ALWAYS writes a new file. The client's originals are never touched.
Needs Pillow:  python3 -m pip install pillow
"""
import argparse
import os
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("tint_logo.py needs Pillow:  python3 -m pip install pillow")

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO_DIR = os.path.join(HERE, "..", "assets", "logo")


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"not a hex colour: {h!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("colour", help="target hex, normally the post's --accent")
    ap.add_argument("--lockup", action="store_true",
                    help="tint the full lockup rather than the icon-only mark "
                         "(never place the lockup below ~250px wide)")
    ap.add_argument("--src", default=None, help="override the source PNG")
    ap.add_argument("--name", default=None, help="slug for the new file (default: the hex)")
    args = ap.parse_args()

    try:
        rgb = hex_to_rgb(args.colour)
    except ValueError as e:
        sys.exit(f"error: {e}")

    kind = "lockup" if args.lockup else "mark"
    src = args.src or os.path.join(
        LOGO_DIR, "logo-cream.png" if args.lockup else "logo-cream-mark.png")
    src = os.path.abspath(src)
    if not os.path.exists(src):
        sys.exit(f"source not found: {src}")

    slug = args.name or args.colour.lstrip("#").lower()
    out = os.path.abspath(os.path.join(
        os.path.dirname(src), f"logo-{slug}-{'lockup' if args.lockup else 'mark'}.png"))
    if out == src:
        sys.exit("refusing to overwrite the source. Pass a different --name.")

    im = Image.open(src).convert("RGBA")
    solid = Image.new("RGBA", im.size, rgb + (255,))
    solid.putalpha(im.getchannel("A"))      # keep the artwork's shape, replace its colour
    solid.save(out)

    print(f"source (untouched): {src}")
    print(f"  wrote {out}   {im.width} x {im.height}   {kind} in {args.colour.upper()}")
    print("Point the template's <img src> at this file.")


if __name__ == "__main__":
    main()
