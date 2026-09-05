# Working from a reference the user gives you

The user may attach a screenshot of a post they like, point at a file, or paste a link.
That reference is a **structural brief**, not a thing to copy.

---

## The rule

> **Take the composition. Leave the content.**

What you take: the arrangement, the grid, the alignment system, the hierarchy ratios, the
density, the shape language, where the eye is led, what is doing the work.

What you never take: their colours, their fonts, their logo or wordmark, their photographs
or illustrations, their icon set, their wording. Those get replaced by ours — the ground
the user named, Playfair / Caveat / Poppins, Dr. Mona's mark, the assets in `assets/`, and
copy you write yourself.

The result should read as a Dr. Mona post that happens to be built on the same
architecture — not as someone else's post recoloured. If the reference is so distinctive
that its structure alone identifies the brand it came from (a signature device, a
recognisable mark, a proprietary layout), say so and build the nearest thing that stands
on its own.

---

## How to read one

**Look at the image properly first** — open it, don't skim the filename. Then write out
what you found, in the conversation, before designing:

| Read this | Ask |
|---|---|
| **Grid** | how many columns? where do the edges align? is there a margin they hold? |
| **Alignment** | centred, ranged left, split, diagonal? one system or two? |
| **Hierarchy** | how many size levels? roughly what ratio between them? |
| **Focal point** | what does the eye hit first, and what makes it win — size, contrast, isolation, position? |
| **Density** | how much of the canvas is empty? where is the air? |
| **Shape language** | rounded or square? panels or bare? hairlines or solid blocks? |
| **Ornament** | what decoration exists, and what job is each piece doing? |
| **Weight** | top-heavy, centred, bottom-weighted? |
| **The move** | what is the one idea that makes this design work? |

That last row is the important one. Most references have a single structural idea — an
oversized numeral bleeding off the edge, a headline broken across a photograph, a stack of
rules that gets denser downward. Name it, then rebuild *that* with our material.

---

## Then

1. Say what you took and what you replaced, in a sentence or two, so the user can correct
   you before you spend a render on it.
2. Map it onto our invariants. The handle still goes bottom-left, the arrow bottom-right,
   the masthead at the top — even if the reference puts them elsewhere. **The reference
   never overrides a non-negotiable.** If it collides, name the collision and adapt: a
   reference with its handle top-right becomes our handle bottom-left, and you keep the
   *balance* it was providing by other means.
3. Translate the type. Their display face becomes Playfair Display at whatever size holds
   the same proportion of the canvas — match the *ratio*, not the point size, since their
   canvas may be a different shape.
4. Translate the colour. Their palette becomes ours: the field is `--ground`, their
   accents become `--accent`, their light panels become our glass. If their design depends
   on three hues, collapse it to ours and say what you lost.
5. Build, render, look, and compare against the reference side by side. Ask whether you got
   the *structure* or only the vibe.

---

## When the reference is one of our own posts

Different job. If the user points at a previous Dr. Mona post and says "like this one",
they want a **family resemblance**, not a variation — so match it closely: same
archetype, same alignment, same density, same ornament vocabulary. The variation rule in
`composition.md` is suspended for that post; say so explicitly, since it is normally a
defect to repeat a layout.

Watch for the third possibility: "here is the last one, make the next one" usually means
*a set that belongs together but is not identical*. Ask which they mean if it is unclear —
the two answers produce very different work.

---

## Several references at once

Do not average them. Pick the strongest structural idea from each and say which came from
where. Two composition ideas per slide is a maximum; three fight.
