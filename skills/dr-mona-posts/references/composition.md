# Composition — designing the slide

**Read this before you write any HTML.** The frame in `templates/` is a chassis, not a
layout. Designing the composition for *this* topic is your job, every time.

The failure mode this file exists to prevent: every post coming out as a centred title
over three glass cards. That layout is one option among many, and using it twice in a row
is a defect.

---

## 1. What is fixed, and what is yours

**Fixed — these survive to the final file, always:**

| | |
|---|---|
| Canvas | 1080 × 1080 (portrait 1080 × 1350 · reel 1080 × 1920) |
| Handle | `@dr.monaalisardar`, **bottom-left**, 20px Poppins 600 cream. Never moves, on any slide of any post. |
| Swipe arrow | bare 200px arrow, **bottom-right**, carousel slides `1 … N-1` only. No dots, no "SWIPE NEXT", no monogram. |
| Masthead | the logo mark + `DR. MONA ALI` + subtitle, at the top. Left or centred. |
| Palette | `--ground` from the user; `--ground-deep` and `--accent` derived; `--cream` `--ink` `--ink-soft` fixed |
| Fonts | Playfair Display · Caveat · Poppins. Nothing else. |
| Material | glass panels, never opaque, never both on one slide |
| Contact data | `MON-SAT \| 6:00 – 9:00 PM` · `0315-7090609` · `MBBS, MD, MRCPsych(UK)` |
| Grain + depth | the noise tile and a light/dark wash under the content |
| Export | the `@media (min-width:1200px)` preview guard |

**Yours — decide these fresh for every post:**

the arrangement · the grid · what the content row even *is* · where the eye lands first ·
the size relationships · which background artwork · the ornament · the density · the
balance of air · whether there are panels at all · the alignment system.

---

## 2. Design before you code

Before touching the frame, write down — in the conversation, in about four lines — the
composition you are going to build:

> *Anchor:* left, on a 3-column grid, everything ranged from x=46.
> *Focus:* the number "1 in 4" at 260px, top third.
> *Support:* one wide glass strip under it holding the explanation.
> *Field:* concentric arcs radiating from behind the number, off the right edge.
> *Air:* the bottom third is empty except the handle.

That paragraph is the design. The CSS is transcription. Skipping it is how you end up
back at the default layout without noticing.

---

## 3. The archetypes

A catalogue to choose from and combine — not a menu to work through in order. Each is a
genuinely different composition, not a restyle of the same one.

| # | Archetype | Shape | Fits |
|---|---|---|---|
| 1 | **Centred plate** | centred title, three glass cards, closing line | three parallel beats; awareness days |
| 2 | **Editorial left** | everything ranged left on a column grid, a vertical accent rule down the left, content stacked | explanatory posts; a strong quiet voice |
| 3 | **Split canvas** | 60/40 vertical split — type one side, one large glass panel or image well the other | contrast, before/after, "what it is / what it isn't" |
| 4 | **Hero figure** | one enormous number or word (Playfair 220–300px), a supporting line, one thin glass strip | a statistic; a single blunt fact |
| 5 | **Stacked rows** | 3–5 full-width glass rows, small disc left, heading + line right | a list that needs more words than a card holds |
| 6 | **Pair** | two large panels, side by side or stacked, contrasting headers | myth / fact · symptom / response |
| 7 | **Quote plate** | a giant Playfair or Caveat quote, small attribution, almost no ornament, no panels | a line worth sitting alone with |
| 8 | **Orbit** | a central glyph with 3–4 satellites and connecting hairlines | cycles, systems, "these feed each other" |
| 9 | **Steps** | a horizontal or diagonal connector with 3 nodes along it | a sequence, a process, what to do first |
| 10 | **Photo-led** | a duotoned photograph filling one third or half, type in the clear area | when a real image earns its place |
| 11 | **Type poster** | no panels at all — title, a rule, a paragraph set large and confident | the most restrained option; use it more often than feels natural |
| 12 | **Plate in a keyline** | an inset hairline border, everything living inside it | a formal, printed feel; anniversaries, statements |
| 13 | **Offset row** | three cards, staggered vertically by 20–40px | the centred plate, loosened |
| 14 | **Corner weight** | the mass in one corner, a long diagonal of empty ground opposite | a short hook with a lot of confidence |

Combining two is normal — *editorial left* + *stacked rows*, or *hero figure* + *photo-led*.
Inventing a fifteenth is welcome. What is not welcome is defaulting to #1.

---

## 4. The variation rule

> **A new post must differ from the previous post of the same format on at least four of
> the eight axes below.**

Before designing, look at the two most recent posts in `ready-posts/` (open the PNGs, not
just the HTML). Then choose deliberately against them.

| # | Axis | Range |
|---|---|---|
| 1 | Alignment | centred · left · split · asymmetric / diagonal |
| 2 | Content form | cards · stacked rows · single panel · no panel · orbit · steps · pair |
| 3 | Title treatment | roman + italic stack · one line with an italic word · a Caveat accent word · one oversized word · a rule between the lines |
| 4 | Background artwork | long curves · concentric arcs · dot field · rings · botanical fronds · faint grid · rays · soft blobs |
| 5 | Ornament | leaf glyphs · fading hairlines · corner keylines · a numeral series · none |
| 6 | Density | sparse (one idea, lots of air) · medium · full |
| 7 | Imagery | pure vector · a duotoned photograph · a single line illustration at scale |
| 8 | Vertical weight | top-heavy · centred · bottom-weighted |

Within one carousel the opposite applies: the slides are a **set**. Ground, masthead,
handle, type scale and panel material stay identical across them; what changes between
slides is the background artwork and the content arrangement. The CTA slide is the one
that should read differently — flipping the anchor (left on the message slides, centred
on the closing card) is the usual way, and it works.

---

## 5. What makes it beautiful

Beauty here is not decoration. Six things do the work:

**One focal point.** Decide what the eye hits first and make it unarguable. If two things
compete, the slide fails, however nice both are.

**A real size jump between levels.** Title, subhead, body should be roughly 3.5× / 1.6× /
1×. Two elements within 15% of each other's size read as a mistake. **Larger is almost
always the right call** — this client has asked for bigger type four separate times. When
something does not fit, take the space out of spacing and layout, never out of font size.

**Alignment you could draw.** Every edge should line up with another edge. Pick a grid —
3 columns of 316px with 22px gutters, or a 12-column of 78px — and put everything on it.
Nothing sits at a coincidental x.

**Unequal, generous whitespace.** Equal margins all round read as a form. Give one region
much more air than the others, and let the emptiness be deliberate rather than left over.
A slide with one idea and a lot of ground beats a slide with three and none.

**Ornament that earns its place.** Every rule, dot, frond and glyph should be doing one of:
separating, pointing, framing, or setting a mood. If it is only filling space, cut it.

**Optical balance, not mathematical.** A dark mass reads heavier than a light one of the
same area; a title feels top-heavy when it is mathematically centred. Trust the render.

### And the edges

Nothing important within 46px of any edge. Nothing accidentally *near* an edge either —
either commit to bleeding off it, or clear it properly. Playfair italic is noticeably
wider than the roman at the same size, so a long italic line is what overruns first.

---

## 6. Colour, applied

`references/colour.md` has the derivation. In composition terms:

- The ground is the field. `--ground-deep` is for linework *on* the ground.
- `--accent` is for icons, hairlines, rules, keylines and script accents — **never for
  body or headline type on the ground.**
- Headlines on the ground: `--ink` (or `--cream` on a dark ground). Anything on glass:
  `--ink` / `--ink-soft`.
- Glass is a *pale version of the ground*. Anything you place on it must be dark enough to
  survive that — this is why the CTA strip and logo mark get tinted to `--accent`, not the
  ground.
- One hue per post. The variation comes from arrangement, not from a second colour.

---

## 7. The critique pass — not optional

Render. **Open the PNG and look at it.** Then answer, honestly:

1. What does the eye hit first? Is that what should have been first?
2. What is the weakest element on this slide?
3. Where is the composition merely *filled* rather than *designed*?
4. Is any type smaller than it needs to be?
5. Would this be mistaken for the last post at thumbnail size?

Fix the weakest thing and re-render. **At least one revision pass, always** — the first
render is a draft, not a deliverable. Report done only after looking at the second one.
