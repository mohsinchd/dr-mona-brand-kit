#!/usr/bin/env python3
"""
Derive the Dr. Mona palette from one ground colour.

    python3 derive_colors.py "#B8A9C9"
    python3 derive_colors.py sage
    python3 derive_colors.py --list

Prints a paste-ready :root block plus a contrast report. Standard library only.
"""
import colorsys
import sys

PRESETS = {
    "sage":     ("#799D84", "the core brand green — the default when no colour is named"),
    "cream":    ("#F0EAE1", "the brand's light field; pairs with sage accents"),
    "lavender": ("#B8A9C9", "used for the 2026-08-27 suicide-prevention carousel"),
    "plum":     ("#B8A9C9", "alias of lavender"),
    "clay":     ("#C9A695", "warm — recovery / hope topics"),
    "sky":      ("#A9BFCF", "cool — sleep / calm topics"),
    "night":    ("#2F3A44", "dark ground — headlines flip to cream"),
}

CREAM, INK, INK_SOFT = "#FDFCF5", "#2A2530", "#514A5C"


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"not a hex colour: {h!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#" + "".join(f"{max(0, min(255, round(c))):02X}" for c in rgb)


def to_hls(hexstr):
    r, g, b = (c / 255 for c in hex_to_rgb(hexstr))
    return colorsys.rgb_to_hls(r, g, b)          # (hue, lightness, saturation)


def from_hls(h, l, s):
    return rgb_to_hex(c * 255 for c in colorsys.hls_to_rgb(h, max(0.0, min(1.0, l)),
                                                           max(0.0, min(1.0, s))))


def relative_luminance(hexstr):
    def chan(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (chan(c) for c in hex_to_rgb(hexstr))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = relative_luminance(a), relative_luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def blend(fg, bg, alpha):
    """fg painted over bg at `alpha` — approximates a glass panel over the ground."""
    f, b = hex_to_rgb(fg), hex_to_rgb(bg)
    return rgb_to_hex(f[i] * alpha + b[i] * (1 - alpha) for i in range(3))


def derive(ground):
    h, l, s = to_hls(ground)
    dark = l < 0.42
    ground_deep = from_hls(h, l * 0.85, s)
    # --accent always sits at ~.25 lightness: it has to hold 4.5:1 against a GLASS panel,
    # and the panel is light whatever the ground is.
    accent = from_hls(h, 0.25, max(0.18, min(s, 0.32)))
    # on a dark ground, anything drawn directly ON the ground needs a lifted tone instead
    accent_soft = from_hls(h, 0.72, min(s, 0.28)) if dark else None
    duo_lo = from_hls(h, 0.20, min(0.45, max(s, 0.22)))
    duo_hi = from_hls(h, 0.88, min(0.28, max(s * 0.6, 0.10)))
    return dict(ground=ground.upper(), ground_deep=ground_deep, accent=accent,
                accent_soft=accent_soft, duo_lo=duo_lo, duo_hi=duo_hi,
                dark=dark, hue=h, light=l, sat=s)


def panel_css(dark):
    stops = (0.72, 0.46, 0.60) if dark else (0.60, 0.32, 0.46)
    return ("linear-gradient(152deg, rgba(253,252,245,%.2f) 0%%,\n"
            "                        rgba(253,252,245,%.2f) 54%%,\n"
            "                        rgba(253,252,245,%.2f) 100%%)" % stops)


def report(p):
    # the title-block headline sits directly on the GROUND
    headline_on_ground = CREAM if p["dark"] else INK
    # card headings and body copy sit on GLASS — always ink, whatever the ground
    glass = blend(CREAM, p["ground"], 0.72 if p["dark"] else 0.46)
    on_ground_accent = p["accent_soft"] or p["accent"]

    print(f"\n/* ground {p['ground']}  ·  "
          f"hue {p['hue']*360:.0f}°  lightness {p['light']:.2f}  sat {p['sat']:.2f}  ·  "
          f"{'DARK ground' if p['dark'] else 'light ground'} */")
    print(":root{")
    print(f"  --ground:      {p['ground']};   /* supplied by the user */")
    print(f"  --ground-deep: {p['ground_deep']};   /* lightness x0.85 — background linework */")
    print(f"  --accent:      {p['accent']};   /* icons, rules, keylines, script accents */")
    if p["accent_soft"]:
        print(f"  --accent-soft: {p['accent_soft']};   /* dark ground only — accent marks sitting ON the ground */")
    print(f"  --cream:       {CREAM};")
    print(f"  --ink:         {INK};")
    print(f"  --ink-soft:    {INK_SOFT};")
    print(f"  --panel: {panel_css(p['dark'])};")
    print("  --pad-edge: 46px;")
    print("}")
    print(f"/* reel-cover duotone:  --duo-lo {p['duo_lo']}   --duo-hi {p['duo_hi']} */")

    print("\ncontrast check")
    rows = [
        (f"headline {headline_on_ground} on ground", contrast(headline_on_ground, p['ground']), 4.5),
        (f"card heading {INK} on glass", contrast(INK, glass), 4.5),
        (f"card body {INK_SOFT} on glass", contrast(INK_SOFT, glass), 4.5),
        (f"accent {p['accent']} on glass", contrast(p['accent'], glass), 4.5),
        (f"accent {on_ground_accent} on ground", contrast(on_ground_accent, p['ground']), 3.0),
        (f"handle/masthead {CREAM} on ground", contrast(CREAM, p['ground']), 2.0),
    ]
    for label, ratio, need in rows:
        mark = "ok  " if ratio >= need else "LOW "
        print(f"  {mark} {label:40s} {ratio:5.2f}:1  (needs {need})")
    print("  note: cream masthead/handle on a mid-tone ground sits around 2-3:1 by design —")
    print("        that is the brand look, not a defect. Anything else marked LOW is.")

    if p["dark"]:
        print("\nDARK GROUND — apply the dark-ground rules in references/colour.md:")
        print("  - the title-block headline flips --ink -> --cream (it sits on the ground)")
        print("  - card headings and body copy stay --ink / --ink-soft (they sit on glass)")
        print("  - the panel stops above are already lifted")
        print("  - use --accent-soft for eyebrows, rules and linework drawn on the ground")
    print("\nRemember: the accent is for icons, rules, keylines and script accents only.")
    print("Type on the ground is --cream; headlines are --ink. Never type in the accent.\n")


def main(argv):
    if len(argv) != 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    arg = argv[1]
    if arg == "--list":
        print("\npresets\n")
        for name, (hexv, note) in PRESETS.items():
            print(f"  {name:9s} {hexv}   {note}")
        print()
        return 0
    if arg.lower() in PRESETS:
        ground = PRESETS[arg.lower()][0]
        print(f"\npreset '{arg.lower()}' — {PRESETS[arg.lower()][1]}")
    else:
        ground = arg
    try:
        report(derive(rgb_to_hex(hex_to_rgb(ground))))
    except ValueError as e:
        print(f"error: {e}\nGive a hex like '#799D84', or a preset name "
              f"({', '.join(PRESETS)}).")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
