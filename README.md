# Dr. Mona — Instagram brand kit

A Claude Code plugin that builds publish-ready Instagram artwork for
**@dr.monaalisardar** — Dr. Mona Ali, psychiatrist, psychiatric & drug rehabilitation
clinic. Static posts, carousels and reel covers, as plain HTML/CSS rendered to PNG with
headless Chrome. No frameworks, no paid tools, no design software.

You describe the post in a sentence. Claude designs the layout, writes the copy, builds
it, renders it, critiques its own work, revises, and hands you a 2160 × 2160 PNG.

**The layout is designed fresh every time — this is not a template filler.** The brand
furniture is fixed (handle bottom-left, arrow bottom-right, masthead, palette, fonts,
glass panels); everything else is a new design decision per post.

---

## Contents

- [Install](#install) · [Updating](#updating)
- [Your first post](#your-first-post)
- [**Example prompts**](#example-prompts) ← start here
- [What you can steer](#what-you-can-steer)
- [Working from a design reference](#working-from-a-design-reference)
- [Why every post looks different](#why-every-post-looks-different)
- [What is fixed, and why](#what-is-fixed-and-why)
- [Output](#output) · [Editing the system](#editing-the-system-itself)

---

## Install

Inside Claude Code, run these two, once:

```
/plugin marketplace add mohsinchd/dr-mona-brand-kit
```

```
/plugin install dr-mona@dr-mona-brand
```

That is the whole install — the commands, the skill and all the brand assets come with it.

### Updating

```
/plugin update dr-mona
```

Run it whenever you hear the kit has changed. Everyone on the team stays on one spec, so a
rule fixed once is fixed for all of you. Check what you are on with `/plugin` → **dr-mona**.

### Requirements

- **Google Chrome** (or Chromium, or Edge) — the renderer finds it on macOS, Windows and
  Linux, or you point the `CHROME` environment variable at it.
- **Python 3** — bundled on macOS and Linux; on Windows install it from python.org.
- Pillow and NumPy, but **only** for the two asset re-tinters:
  `python3 -m pip install pillow numpy`. Building and exporting posts needs neither.

### Without the plugin

The skill alone works as a plain folder — copy it and restart Claude Code:

```bash
cp -R skills/dr-mona-posts ~/.claude/skills/
```

It still triggers on its own; only the `/dr-mona:*` commands are missing. Copy `commands/`
to `~/.claude/commands/` to get those too. You lose one-command updates this way.

---

## Your first post

```bash
mkdir dr-mona-work && cd dr-mona-work
claude
```

```
/dr-mona:setup
```

That copies the assets in and creates `ready-posts/` and `reels/`. Then:

```
/dr-mona:carousel World Mental Health Day, ground: sage
```

Two or three minutes later you have `ready-posts/2026-09-05/post-01-.../output/*.png`,
ready to upload.

---

## Example prompts

Copy any of these and change the words. **The only thing you must supply is the ground
colour** — leave it out and Claude asks rather than guessing.

Colour can be a preset — `sage` `cream` `lavender` `clay` `sky` `night` — or any hex.

### Carousels

The default is two slides: one message slide, one closing CTA card.

```
/dr-mona:carousel World Mental Health Day, ground: sage
```

```
/dr-mona:carousel three myths about antidepressants, ground: lavender
```

```
/dr-mona:carousel what to say when someone tells you they are struggling, ground: clay
```

```
/dr-mona:carousel the difference between sadness and depression, ground: sky,
3 slides — one for sadness, one for depression, then the CTA
```

```
/dr-mona:carousel how families can support someone in recovery, ground: #C9A695.
Warm and practical, not clinical. Lead with what NOT to say.
```

```
/dr-mona:carousel World Suicide Prevention Day, ground: lavender.
Safe messaging matters here — keep it hopeful, and tell me if you need a helpline number.
```

### Single posts

One idea, no CTA, no swipe arrow.

```
/dr-mona:post the quiet signs of burnout, ground: clay
```

```
/dr-mona:post 1 in 4 of us will live through a mental illness in any given year,
ground: clay. Make the number huge.
```

```
/dr-mona:post you cannot pour from an empty cup — a quote card, ground: sage.
Type only, no cards.
```

```
/dr-mona:post four things that actually fix sleep, ground: sky, portrait
```

```
/dr-mona:post panic attacks are not dangerous, even though they feel it, ground: sky.
Keep it calm and very sparse.
```

### Reel covers

```
/dr-mona:reel-cover anxiety is treatable, ground: sage
```

```
/dr-mona:reel-cover why nobody talks about postpartum depression, ground: lavender,
photo: ~/Downloads/window-light.jpg
```

```
/dr-mona:reel-cover addiction is a medical condition, not a character flaw, ground: clay.
Big, blunt hook — it has to read at thumbnail size.
```

### With a design reference

Attach or point at an image and it is used as a **structural brief** — the composition is
taken, the colours and fonts are not. See
[Working from a design reference](#working-from-a-design-reference).

```
/dr-mona:carousel binge eating disorder, ground: clay — build it like the layout in
this screenshot
```

```
/dr-mona:post signs of ADHD in adult women, ground: sky.
Use the grid from ~/Downloads/inspo.png but our palette and fonts.
```

```
/dr-mona:post stigma, ground: sage — same family as
ready-posts/2026-09-05/post-01-one-in-four, it is going out as a pair
```

### With your own assets or copy

```
/dr-mona:post therapy is not just for crises, ground: sage.
Use the photo at ~/Downloads/two-chairs.jpg.
```

```
/dr-mona:carousel our new evening clinic hours, ground: cream.
Headline: "Now open six evenings a week". Put her portrait in the CTA.
```

```
/dr-mona:post ground: lavender. Use exactly this copy —
ASK: Ask directly and calmly. Naming it does not plant the idea.
LISTEN: Listen without fixing, judging or rushing toward advice.
STAY: Check in tomorrow, and the day after.
```

### Steering the design

Leave these out and Claude designs it. Say them and they are honoured.

```
/dr-mona:post medication myths, ground: sage. Left-aligned, no cards, lots of air.
```

```
/dr-mona:carousel the recovery timeline, ground: clay.
Lay it out as numbered steps along a line, not as cards.
```

```
/dr-mona:post seasonal affective disorder, ground: sky.
Split the canvas — type on the left, one big panel on the right.
```

```
/dr-mona:carousel World Mental Health Day, ground: sage.
Nothing like the last three posts — surprise me.
```

### Fixing and iterating

```
/dr-mona:recolour ready-posts/2026-09-05/post-01-burnout to sage
```

```
/dr-mona:export ready-posts/2026-09-05/post-02-sleep
```

```
/dr-mona:brand-check
```

```
Slide 2 is too busy — drop the lede and make the headline bigger, then re-render.
```

```
The cards are too similar to last week's post. Redesign slide 1 with a different
archetype and keep the copy.
```

### Without a slash command

The skill loads on its own — plain English reaches it too.

```
Make me a carousel about sleep hygiene on a sky ground.
```

```
I need a post for World Mental Health Day. Sage. Something quiet and confident.
```

---

## What you can steer

Say it in plain words after the topic. Anything you add is an **addition** to the brand
spec, not a replacement for it.

| You can say | Example |
|---|---|
| **the colour** *(required)* | `ground: sage` · `ground: #C9A695` |
| **the format** | `portrait` · `3 slides` · `square` |
| **an asset** | `use the photo at ~/Downloads/hands.jpg` · `put her portrait in the CTA` |
| **the copy** | give your own headline or card text, or let Claude write it |
| **the layout** | `left-aligned` · `lead with a huge number` · `no cards this time` |
| **the emphasis** | `lead with the statistic` · `keep it gentle` · `no script font` |
| **the mood** | `warm and practical` · `stark` · `very sparse` |
| **a reference** | attach an image, or name one of your own past posts |

**Copy is in scope.** Give a rough brief and Claude writes and improves the words. Give
exact copy and it is used as written.

If something you ask for collides with a brand non-negotiable, Claude names the rule and
offers the nearest on-brand alternative rather than quietly breaking either.

---

## Working from a design reference

Attach a screenshot of a post you like, or point at a file:

```
/dr-mona:carousel binge eating, ground: clay, like the layout in this image
```

It takes the **composition** — the grid, the alignment, the hierarchy ratios, the density,
and the one structural idea that makes the design work — and rebuilds it in Dr. Mona's
palette, fonts and furniture. It tells you what it took and what it replaced before
spending a render on it.

It does **not** take their colours, fonts, logos, photographs or wording. Those are
replaced by ours. And the invariants still win: a reference with its handle top-right
becomes our handle bottom-left, with the balance it was providing rebuilt another way.

Point it at one of **your own** past posts instead and it does the opposite — matches
closely for a family resemblance, and tells you it is suspending the variation rule.

---

## Why every post looks different

The kit ships a **frame and a set of invariants — not a layout.**
`references/composition.md` carries a catalogue of fourteen composition archetypes —
centred plate, editorial left, split canvas, hero figure, stacked rows, pair, quote plate,
orbit, steps, photo-led, type poster, keyline plate, offset row, corner weight — eight
variation axes, and one hard rule:

> **A new post must differ from the previous post of the same format on at least four of
> the eight axes** (alignment · content form · title treatment · background artwork ·
> ornament · density · imagery · vertical weight).

Before designing, Claude opens the last two posts and chooses deliberately against them.
It writes the composition down in four lines before coding it, then renders, critiques the
result against five questions, and **revises at least once** — the first render is a
draft, never the deliverable.

Within one carousel this inverts: the slides are a set, so they hold together, and only
the closing card changes register.

If you ever get two posts that look alike, run `/dr-mona:brand-check` — it audits
variation as well as the rules, and names which axes it checked.

---

## What is fixed, and why

These have each been enforced in a client review. The kit will not trade them away.

- The handle `@dr.monaalisardar` sits **bottom-left on every slide**, and never moves.
- The swipe cue is a **bare 200px arrow**, bottom-right, on slides 1…N-1 only. No
  pagination dots, no "SWIPE NEXT", no monogram.
- **The occasion outranks the slogan** — the topic is the largest thing on the slide.
- **One idea per canvas.** A title, its content, *and* a CTA is a two-slide carousel, not
  a denser square. "Too much bloated" was the verdict last time. This is a density rule —
  how that one idea is arranged is designed per post.
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
- On suicide, self-harm and addiction topics, **safe-messaging rules are requirements**,
  not taste: never imply a method, no imagery of visible anguish, "died by suicide" not
  "committed", statistics attributed, and a crisis resource before any clinic promotion.

### The colour contract

The ground is the one required input; the palette is derived from it.

```bash
python3 skills/dr-mona-posts/scripts/derive_colors.py "#B8A9C9"
python3 skills/dr-mona-posts/scripts/derive_colors.py sage
python3 skills/dr-mona-posts/scripts/derive_colors.py --list
```

It prints a paste-ready `:root` block and a contrast report. Presets: `sage` (the core
brand green) · `cream` · `lavender` · `clay` · `sky` · `night`.

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
python3 skills/dr-mona-posts/scripts/render.py ready-posts/2026-09-05/post-01-topic/*.html
```

---

## Editing the system itself

| File | What lives there |
|---|---|
| `skills/dr-mona-posts/SKILL.md` | the intake contract, the colour contract, the non-negotiables |
| `skills/dr-mona-posts/references/composition.md` | **the archetypes, the variation rule, the critique pass** |
| `skills/dr-mona-posts/references/reference-images.md` | how an attached design reference is used |
| `skills/dr-mona-posts/references/` | the invariants, per-format recipes, colour, assets, voice, gotchas |
| `skills/dr-mona-posts/templates/` | the two frames — invariant furniture plus a kit of primitives |
| `skills/dr-mona-posts/examples/` | four finished slides, for craft reference — never copied as layouts |
| `skills/dr-mona-posts/scripts/` | palette derivation, the renderer, the two re-tinters |
| `skills/dr-mona-posts/assets/` | the client's logo, CTA artwork, icons, graphics, photos |

Change a rule in one place, push, and everyone gets it on `/plugin update dr-mona`.

**A rule that came out of a real review belongs in `SKILL.md` or a reference file — not in
a one-off instruction to Claude.** That is the difference between a system and a habit.

---

## Changelog

**2.0 — the layout is designed, not filled in.** `templates/` became frames carrying only
the invariants plus a kit of primitives; the four finished templates moved to `examples/`.
Added `references/composition.md` (14 archetypes, 8 variation axes, the ≥4-axis rule, the
beauty criteria, a mandatory critique-and-revise pass) and
`references/reference-images.md` (work from an attached design reference).
`brand-check` now audits variation as well as the rules.

**1.0 —** the system packaged as a plugin: 7 slash commands, the `dr-mona-posts` skill,
the brand assets, and four scripts.
