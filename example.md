---
marp: true
theme: chiaroscuro
paginate: true
math: mathjax
---

<!-- _class: cover -->
<!-- _paginate: false -->

![bg opacity:.4 saturate:0](assets/placeholder.jpg)

# Chiaroscuro

A Marp theme in light and shadow
One slide per layout

---

<!-- _class: agenda -->

# **Contents**

1. Fourteen layouts, one slide each
2. Modifiers, named as they come up
3. Nothing here you have to write CSS for

---

<!-- _class: question -->

# What is this<br>**subject** about?

---

<!-- _class: poster -->

# Titles go **here**

---

# Default

The document page: a brief line before each exhibit.

A long equation gets the whole measure to itself:

$$
X[k] = \sum_{n=0}^{N-1} x[n]\, e^{-j 2\pi k n / N}
     = \sum_{n=0}^{N-1} x[n] \cos\!\left(\frac{2\pi k n}{N}\right)
     - j \sum_{n=0}^{N-1} x[n] \sin\!\left(\frac{2\pi k n}{N}\right),
\qquad k = 0, \ldots, N-1
$$

A long table drops to `xsmall` — here also `centered`:

<div class="xsmall centered">

| Layout | The photograph | Credit |
| --- | --- | --- |
| `half` · `side` | `![bg right]`, or `![bg left]` to mirror | top right |
| `board` | a full-bleed band across the top | top right |
| `image` | covering the slide, cropped to fit | top right |

</div>

---

<!-- _class: indent justify -->

# Indent

`indent` is the everyday slide with the body hung off the title: a quarter of the measure is given away and the three quarters left close against the right margin. It is what the everyday slide used to do by default — and this one is also set with `justify`, which is why these paragraphs come out flush on both edges.

One block of an *ordinary* slide takes `<div class="indent">` instead — the block form of the same indent; the two are for different slides, not for nesting. `no-rule` drops the red bar and `centered` centres everything, here as anywhere; a **word** can be picked out of a sentence, with a [test link](https://github.com/mressl-itba/chiaroscuro).

---

<!-- _class: columns-2 -->

# Columns

###### Modifier

`columns-2` … `columns-6` set the body of an everyday slide in columns, with the title spanning them; `columns-1` is the way back when a deck-wide `class:` said otherwise. The same modifier counts text columns on `comparison`, photographs on `trio` and photo panels on `board` — one name, one variable, four things to count.

The sixth heading level is the eyebrow above: caps, letter-spaced, in the secondary ink. It is the only place the theme uses capitals other than a cover title. The listing below — set in the theme's own palette, not highlight.js defaults — is wrapped in `<div class="break">`, which opens the next column where the browser would have balanced:

<div class="xsmall break">

```cpp
// --fs-code reaches a fence
// a class cannot.
int median(std::vector<int>& v) {
    auto m = v.begin() + v.size() / 2;
    std::nth_element(v.begin(), m, v.end());
    return *m;
}
```

</div>

---

<!-- _class: columns-2 -->

# The content **series**

###### Helpers

`--red` is the theme's own — the rule under this title, the dash in front of a list row, the bars of `agenda` — and `.accent-1` is that same red under a second name. The four beside it are yours, a ramp running from it to blue:

<div class="xxlarge centered">

<span class="accent-1">**1**</span> <span class="accent-2">**2**</span> <span class="accent-3">**3**</span> <span class="accent-4">**4**</span> <span class="accent-5">**5**</span>

</div>

No rule in the theme reads one of them, so nothing on any other slide moves if you replace all five. They colour text; for a shape — a bar, a cell, a path of an inline SVG — read `var(--accent-3)` straight.

---

<!-- _class: columns-2 -->

# The **scale**

###### Helpers

Twelve sizes in two families, on the 4 px grid. The six of `content` are for sentences, and each fits on a page:

<div class="centered">

<span class="xsmall">24</span> <span class="small">28</span> <span class="medium">32</span> <span class="large">48</span> <span class="xlarge">64</span> <span class="xxlarge">80</span>

</div>

The six of `symbol` — 128 · 192 · 256 · 384 · 512 · 768 — are for a glyph or a numeral, never a sentence, and are too large to stand here.

<div class="break">

Line weights have a scale of their own, and an inline SVG reads it straight, `stroke-width="var(--sw-medium)"`:

<div class="centered">

<svg viewBox="0 0 730 178" width="730" height="178">
  <g stroke="currentColor">
    <line x1="0" y1="14" x2="260" y2="14" stroke-width="var(--sw-xxsmall)" />
    <line x1="0" y1="44" x2="260" y2="44" stroke-width="var(--sw-xsmall)" />
    <line x1="0" y1="74" x2="260" y2="74" stroke-width="var(--sw-small)" />
    <line x1="0" y1="104" x2="260" y2="104" stroke-width="var(--sw-medium)" />
    <line x1="0" y1="134" x2="260" y2="134" stroke-width="var(--sw-large)" />
    <line x1="0" y1="164" x2="260" y2="164" stroke-width="var(--sw-xlarge)" />
  </g>
  <g font-size="var(--fs-content-xsmall)" dominant-baseline="middle" text-anchor="start">
    <text x="290" y="14">--sw-xxsmall · 1 — a hairline</text>
    <text x="290" y="44">--sw-xsmall · 2 — rules and guides</text>
    <text x="290" y="74">--sw-small · 3</text>
    <text x="290" y="104">--sw-medium · 4 — axes and curves</text>
    <text x="290" y="134">--sw-large · 6 — the emphasis line</text>
    <text x="290" y="164">--sw-xlarge · 8</text>
  </g>
</svg>

</div>

</div>

---

<!-- _class: half -->
<!-- _footer: placeholder text -->

# Half

Title and body on the left half, the right half free for a photo. Write `![bg right]` with no percentage: the split is forced to 50/50, and a different percentage only narrows the text box without moving the photo.

![bg right](assets/placeholder.jpg)

---

<!-- _class: half -->

# Half, **free field**

For something other than a photo, wrap it in `<div class="right">`. The field carries no type style of its own; compose it with `symbol`, `red` or `pale` when you want one.

<div class="right">

```cpp
// A free field: it takes a code
// block, a list, a table, an
// inline SVG — whatever you put
// in the div.
int main() {
    return 0;
}
```

</div>

---

<!-- _class: half -->

# Half, **few glyphs**

The same field at the top of the scale. `symbol` is the display step, 384 px, and the name is the instruction: a few glyphs or a number, never a sentence. `pale` takes it down to a tint of the page.

Together they turn the subject of the slide into the illustration of it — something to look at while the body is read, rather than one more thing to read.

<div class="right symbol pale">

O(n)

</div>

---

<!-- _class: half -->
<!-- _footer: placeholder text -->

# Half, **mirrored**

###### Modifier

Nothing to switch on: write `![bg left]` and the layout follows the photo. The title and its rule move to the outer edge, the body keeps its ranging and hugs the same one. For a field rather than a photo, say it yourself with `<div class="left">`.

Where a side is a real choice and no photo implies it, that is what `mirror` is for: it flips `split`, `comparison`, `board` and the everyday slide.

![bg left](assets/placeholder.jpg)

---

<!-- _class: side -->
<!-- _footer: placeholder text -->

# Side

Same idea as `half`, with the whole block dropped to the middle of the page. Bullets come out as dashes:

- first point
- second point
- third point

![bg right](assets/placeholder.jpg)

---

<!-- _class: board wide large -->

# Board

## One free field, with the title of `comparison` under it and an `h2` beside it. The table keeps its own width — `wide` would stretch it to the field's.

| Edge | Borrowed from |
| --- | --- |
| left and right | the left margin of `half`, and its mirror |
| top and bottom | the band a full-bleed photograph fills |

---

<!-- _class: board -->
<!-- _footer: placeholder text -->

# Board, **photo**

## A raster image is a photograph: a full-bleed band, cropped to fit. `columns-2` … `columns-4` share it edge to edge, with no gutter.

![](assets/placeholder.jpg)

---

<!-- _class: image -->
<!-- _footer: placeholder text -->

# Image

![](assets/placeholder.jpg)

---

<!-- _class: duo -->

# Duo

## Two photos, a rule and a caption each. The line beside the title is an `h2`, and it lands in the bottom strip whatever order you write it in.

#### Something in **light**

![](assets/placeholder.jpg)

#### Something in **shadow**

![](assets/placeholder.jpg)

---

<!-- _class: trio -->

# Trio

## Three photos in a row, written the same way as `duo`. With `columns-2` the photos widen and their rules follow.

#### First

![](assets/placeholder.jpg)

#### Second

![](assets/placeholder.jpg)

#### Third

![](assets/placeholder.jpg)

---

<!-- _class: comparison -->

# Comparison

## An `h2` lands beside the title, in the same strip `duo` and `trio` use.

### Light

**Columns** hang from a full-bleed line, with a dot each. Two of them by default — write one h3 per column, then its text and its list.

- `code` in a list
- comes out underlined

### Shadow

The h1 goes last and lands at the **bottom left**, with its rule bleeding off that edge — the same corner as every other title in the theme.

- a point
- another one

---

<!-- _class: comparison columns-4 mirror -->

# Four columns

### One

`columns-3` … `columns-6` for more than two.

- a point
- another one

### Two

The gutter stays at 70.5 px throughout.

- fixed
- gutter

### Three

Only the column width is recomputed.

- width
- scales

### Four

Past four, prefer bare lists to prose. This slide is `mirror`ed, so the title is on the right.

- terse
- items

---

<!-- _class: dark columns-2 -->

# Dark

`dark` turns any layout black. It has no rules of its own: the page, the ink, the code panel, the rules of a table and the slide number are all one set of variables, redefined once.

```cpp
// Recoloured by the palette, not by a
// second theme; strings and numbers too.
std::vector<int> v{3, 1, 2};
std::sort(v.begin(), v.end());
```

| Reads | From |
| --- | --- |
| the panel | `--pre-bg` |
| the table rule | `--gray-rule` |

---

<!-- _class: split -->

<div class="left">

# Light

What the deck says out loud.

</div>

<div class="right">

# Shadow

What it leaves for the room to fill in.

</div>

---

<!-- _class: poster dark -->

# chiaroscuro
