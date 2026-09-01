# The ground, and everything derived from it

**The user supplies the ground. If they didn't, ask — do not guess.**

## Derivation

```bash
python3 scripts/derive_colors.py "#B8A9C9"     # any hex
python3 scripts/derive_colors.py sage          # a preset
python3 scripts/derive_colors.py --list        # every preset
```

The script prints a paste-ready `:root` block plus a contrast report. What it does:

| Token | Rule | Why |
|---|---|---|
| `--ground-deep` | same hue, lightness × 0.85 | background linework must read *on* the ground without becoming a second colour |
| `--accent` | same hue, lightness ≈ .25, saturation ≈ .25 | needs 4.5:1 against a **glass panel** — and the panel is light whatever the ground is, so this stays dark on every ground |
| `--accent-soft` | same hue, lightness ≈ .72 | **dark grounds only** — for eyebrows, rules and linework drawn directly on the ground, where the dark accent would disappear |
| `--duo-lo` / `--duo-hi` | lightness .20 / .88 | the two blend layers that grade a photo to the ground (`reel-cover.md`) |

Fixed regardless of ground: `--cream #FDFCF5`, `--ink #2A2530`, `--ink-soft #514A5C`,
the `--panel` gradient, `--pad-edge 46px`.

## Presets

| Name | Ground | Note |
|---|---|---|
| `sage` | `#799D84` | **the core brand green** — the default answer when the user has no preference |
| `cream` | `#F0EAE1` | the brand's light field; pairs with sage accents |
| `lavender` | `#B8A9C9` | used for the 2026-08-27 suicide-prevention carousel |
| `clay` | `#C9A695` | warm, for recovery / hope topics |
| `sky` | `#A9BFCF` | cool, for sleep / calm topics |
| `night` | `#2F3A44` | dark ground — read the dark-ground rules below |

## Rules that survive any ground

- **Never set type in the accent hue on the ground itself.** Headlines are `--ink`;
  anything sitting directly on the ground in light type is `--cream`. The accent is for
  icons, hairlines, rules, keylines and script accent words only.
- **Know which surface a thing sits on.** The title-block headline sits on the *ground*;
  card headings and body copy sit on *glass*. That distinction is what the dark-ground
  rules turn on.
- If the ground is **dark** (`derive_colors.py` flags it):
  - the title-block headline flips `--ink` → `--cream` — it is on the ground;
  - card headings and body copy **stay** `--ink` / `--ink-soft` — they are on glass, and
    the glass is still light;
  - lighten `--panel` (the script raises each stop ~.14 for you);
  - use `--accent-soft` for anything drawn on the ground, `--accent` for anything on glass.
  Everything else is unchanged.
- The cream masthead and handle sit at roughly **2–3:1** on a mid-tone ground. That is the
  brand look, not a defect — the script's report says so. Anything else it marks LOW is real.
- **Check contrast after any ground change.** Lowering panel opacity lightens whatever
  sits on it — re-check *everything* on that panel, not just the thing you changed.
- One ground per post. Slides in a carousel share it; the linework and composition are
  what change between them, not the colour.

## Which hue is allowed

**Sage `#799D84` + cream `#F0EAE1` + ink is the core brand.** Gold, lavender and
terracotta accents were each proposed and rejected in review. A different ground is fine
**only when the user names it for that post** — and even then it stays a ground, never a
text colour, and never a second hue alongside the first.

If a user asks for "something fresh" without naming a colour, offer two or three presets
and let them pick. Rolling a random hue is how the rejected posts happened.
