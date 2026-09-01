# Dr. Mona — Instagram brand kit

A Claude Code plugin that builds publish-ready Instagram artwork for
**@dr.monaalisardar** — Dr. Mona Ali, psychiatrist, psychiatric & drug rehabilitation
clinic. Static posts, carousels and reel covers, as plain HTML/CSS rendered to PNG with
headless Chrome. No frameworks, no paid tools, no design software.

It carries the whole system: the layout spec, the colour contract, the brand
non-negotiables, the client's own assets, and the scripts that derive and export
everything. Hand someone this folder and they can produce on-brand work on day one.

---

## What you get

**Slash commands**

| Command | What it does |
|---|---|
| `/dr-mona:carousel` | a carousel — message slides plus the CTA slide |
| `/dr-mona:post` | a single static post, square or portrait |
| `/dr-mona:reel-cover` | a 1080 × 1920 reel cover |
| `/dr-mona:recolour` | re-ground an existing post to a new colour and re-export |
| `/dr-mona:export` | re-render slide HTML to PNG at 2× |
| `/dr-mona:brand-check` | audit finished slides against the non-negotiables |
| `/dr-mona:setup` | scaffold a new working folder |

Claude Code accepts the short form — `/carousel` — when no other plugin claims that name.

**A skill** — `dr-mona-posts`. It loads on its own whenever someone asks for a post, a
carousel, a slide or a reel cover, so the commands are a shortcut, not a requirement.

**The assets** — the client's logo, her CTA artwork, 22 line icons, 9 decorative shapes,
her photographs. Originals are never modified; every script writes new sibling files.

**Four scripts** — palette derivation with a contrast check, the PNG exporter, and two
asset re-tinters.

---

## Install

### The people you are handing this to

Push this folder to a git repo, then have them run, inside Claude Code:

```
/plugin marketplace add <your-github-user>/dr-mona-brand-kit
```

```
/plugin install dr-mona@dr-mona-brand
```

That is the whole install. The commands, the skill and the assets all come with it, and
`/plugin update dr-mona` picks up whatever you push later — everyone stays on one spec.

If they have the folder on disk rather than in a repo, the same two commands work with a
path instead of a repo name:

```
/plugin marketplace add /full/path/to/dr-mona-brand-kit
```

### Without a plugin

The skill alone also works as a plain folder. Copy it to either location and restart
Claude Code:

```bash
cp -R skills/dr-mona-posts ~/.claude/skills/          # available in every project
```

```bash
cp -R skills/dr-mona-posts .claude/skills/            # this project only
```

The skill still triggers on its own; only the `/dr-mona:*` commands are missing, and you
can copy `commands/` to `~/.claude/commands/` to get them as `/carousel`, `/post` and so on.

### Requirements

- **Google Chrome** (or Chromium, or Edge) — the renderer finds it on macOS, Windows and
  Linux, or you point the `CHROME` environment variable at it.
- **Python 3** — bundled on macOS and Linux; on Windows install it from python.org.
- Pillow and NumPy, but **only** for the two asset re-tinters:
  `python3 -m pip install pillow numpy`. Building and exporting posts needs neither.

---

## Using it in a new project

```bash
mkdir my-dr-mona-work && cd my-dr-mona-work
claude
```

Then:

```
/dr-mona:setup
```

That copies the assets in and creates `ready-posts/` and `reels/`. After that:

```
/dr-mona:carousel World Mental Health Day, ground: sage
```

```
/dr-mona:post signs of burnout, ground: #C9A695, portrait
```

```
/dr-mona:reel-cover anxiety is treatable, ground: sage, photo: ~/Downloads/bench.jpg
```

You do not have to use a command. "Make me a carousel about sleep hygiene on a sky
ground" reaches the same skill.

---

## The one variable

**The background colour — "the ground" — is the only thing that changes per post, and
you supply it.** Everything else is fixed: where each element sits, its size, its
spacing, the type system. Two supporting tones are derived from your colour; the rest of
the palette never varies.

```bash
python3 skills/dr-mona-posts/scripts/derive_colors.py "#B8A9C9"
python3 skills/dr-mona-posts/scripts/derive_colors.py sage
python3 skills/dr-mona-posts/scripts/derive_colors.py --list
```

Presets: `sage` (the core brand green) · `cream` · `lavender` · `clay` · `sky` · `night`.

If you do not name a colour, Claude will ask rather than guess.

## Everything else you can steer

Say it in plain words after the topic and it is folded in as an addition to the spec, not
a replacement for it:

- **an asset** — "use the photo at `~/Downloads/hands.jpg`", "put her portrait in the CTA"
- **the copy** — give your own headline or card text, or let Claude write and improve it
- **the shape** — "three slides", "portrait", "two wide cards instead of three"
- **the emphasis** — "lead with the statistic", "keep it gentle", "no script font"

If something you ask for collides with a brand non-negotiable, Claude says which rule and
offers the nearest on-brand alternative rather than quietly breaking either.

---

## What is fixed, and why

These have each been enforced in a client review. The skill will not trade them away.

- The handle `@dr.monaalisardar` sits **bottom-left on every slide**, and never moves.
- The swipe cue is a **bare 200px arrow**, bottom-right, on slides 1…N-1 only. No
  pagination dots, no "SWIPE NEXT", no monogram.
- **The occasion outranks the slogan** — the topic is the largest thing on the slide.
- **One content row per canvas.** A title, a row, a closing line *and* a CTA is a
  two-slide carousel, not a denser square. "Too much bloated" was the verdict last time.
- **The client's own CTA artwork** is used, never a typeset substitute, and `cta.png` is
  never overwritten.
- **Real contact data always** — `MON-SAT | 6:00 – 9:00 PM`, `0315-7090609`,
  `MBBS, MD, MRCPsych(UK)`. Placeholders in a brief are ignored in favour of these.
- **Glass panels, never opaque**, and never both on one slide.
- **Sage + cream + ink is the core brand.** Another ground is fine when you name it; it
  stays a ground, never a text colour.
- **Larger type is almost always right.** When something does not fit, the space comes
  out of spacing and layout — never out of font sizes.
- **Nothing the client supplied is ever deleted or overwritten.** Derived files are
  written alongside.

---

## Output

```
ready-posts/YYYY-MM-DD/post-NN-topic/
  slide-01.html  slide-02.html
  output/slide-01.png  slide-02.png     2160 × 2160

reels/YYYY-MM-DD/reel-NN-topic/
  cover.html  assets/cover.jpg
  output/cover.png                      2160 × 3840
```

Exported at 2× device scale — Instagram re-compresses uploads, so a crisp 2× source stays
sharp. Every slide file opens directly in a browser for preview; the preview padding sits
behind a media query, so a headless window sized to the canvas screenshots it exactly.

```bash
python3 skills/dr-mona-posts/scripts/render.py ready-posts/2026-09-01/post-01-topic/*.html
```

---

## Editing the system itself

| File | What lives there |
|---|---|
| `skills/dr-mona-posts/SKILL.md` | the intake contract, the colour contract, the non-negotiables |
| `skills/dr-mona-posts/references/` | the layout map, per-format recipes, colour, assets, voice, gotchas |
| `skills/dr-mona-posts/templates/` | the four slide skeletons — every fixed value is already in them |
| `skills/dr-mona-posts/scripts/` | palette derivation, the renderer, the two re-tinters |
| `skills/dr-mona-posts/assets/` | the client's logo, CTA artwork, icons, graphics, photos |

Change a rule in one place, push, and everyone gets it on `/plugin update dr-mona`.

**A rule that came out of a real review belongs in `SKILL.md` or a reference file — not in
a one-off instruction to Claude.** That is the difference between a system and a habit.
