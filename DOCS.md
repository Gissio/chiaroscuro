# chiaroscuro — documentation

The complete reference. For the visual tour of the layouts, see the
[README](README.md).

## Install

Copy `themes/chiaroscuro.css` anywhere in your project — a `themes/` folder is
the usual place — and register it. There are three separate channels, and they
do not know about each other, so set up the ones you actually use.

**marp-cli, via a config file.** Put a `.marprc.yml` next to where you run the
command:

```yaml
themeSet: ./themes
allowLocalFiles: true
```

`marp-cli` looks for `.marprc.yml` **only in the directory you run it from**,
never in parent directories, and `themeSet` resolves relative to the config
file, not to the current directory. If you run the command from more than one
place, keep a copy of the config in each, or pass `--config <path>` explicitly.

**marp-cli, without a config file.** Point at the theme directly:

```bash
marp deck.md --theme themes/chiaroscuro.css --pdf
```

**Marp for VS Code.** The extension does not read `.marprc.yml`. It reads the
`markdown.marp.themes` setting, so add this to `.vscode/settings.json`:

```json
{
  "markdown.marp.themes": ["./themes/chiaroscuro.css"]
}
```

If the extension warns *"The specified theme 'chiaroscuro' is not recognized"*,
that setting has not reached it — check you opened the folder as a workspace and
not the `.md` file on its own.

### When it silently does not load

`theme: chiaroscuro` does not fail loudly. If the theme is not registered, Marp
falls back to its `default` theme without a word. The tell is unmistakable once
you know it: **Segoe UI, `#224466` headings and a 960 × 540 canvas**. If you see
that, the theme never loaded — go back and register it.

## Quick start

```markdown
---
marp: true
theme: chiaroscuro
paginate: true
---

<!-- _class: cover -->
<!-- _paginate: false -->

![bg opacity:.4](photo.jpg)

# Title

Subtitle
Author

---

# An ordinary slide

The title starts at the left margin with its red rule bleeding off the edge,
and the body hangs to the right of it.
```

Pick a layout per slide with a Marp class directive, `<!-- _class: name -->`.
Modifiers go in the same directive, space separated: `<!-- _class: half dark -->`.

Render `example.md` to see all of it at once — from the repository root, where
`.marprc.yml` registers the theme and allows local files:

```bash
marp example.md --pdf -o example.pdf
```

Run it from anywhere else and you must say both things yourself:
`--theme themes/chiaroscuro.css --allow-local-files`. Forget the first and you
get the fallback described above.

## Layouts

| Class | What it is |
| --- | --- |
| *(none)* | The everyday slide: title with its rule, body indented past it. |
| `cover` | Full-bleed photo over black, title in caps, rule, credits. |
| `question` | A white band with the question, black below, a giant "?". |
| `half` | Title and body on the left half, the right half free for a photo. |
| `side` | Like `half`, with the whole block dropped to the middle of the page. |
| `duo` | Two photos with a rule and a caption each. |
| `trio` | Three photos in a row, each with its rule and caption. |
| `band` | A full-bleed band of image across the top. |
| `image` | One photo covering the slide, with an optional title. |
| `split` | Half black, half white, with a free field on each half. |
| `poster` | One large statement, centred and staying centred as it grows. |
| `comparison` | N columns hanging from a full-bleed line, a dot each. |
| `board` | One free field across the top, with the title of `comparison`. |
| `agenda` | Red title and a numbered list set against big grey numerals. |

A talk usually opens on `cover`, sets out its shape with `agenda`, and then
alternates: stretches of ordinary slides broken up by a `question` or a
full-bleed `image` whenever the argument turns. `poster` is for the one line you
want the room to remember; `comparison` for the moment you put the options side
by side.

### Writing each one

**`cover`** — the title is set in caps whatever you type. The photo is optional;
without one the slide is black. Choose the dimming to suit the photo.

```markdown
<!-- _class: cover -->
<!-- _footer: photo credit -->

![bg opacity:.4](photo.jpg)   <!-- a light photo: dim it -->
![bg](dark-photo.jpg)         <!-- already dark: leave it -->

# Title

Subtitle
Author
```

**`question`** — bold runs in the title come out red. Break the title with
`<br>` if you want two rows.

```markdown
<!-- _class: question -->

# What is a<br>**data structure**?
```

Two rows come out centred in the white band, and the title is anchored by its
bottom edge: a one-row question lands where the second row of a two-row one
would, as if the first row were blank. The "?" is centred in the black band,
both ways: on the right half of the slide, and — measured to its ink, not its
box — on the height of the band.

**`half`** and **`side`** — the same layout at two heights; `side` sits lower
down the page. The photo on the right goes in as a
Marp background. **Write `![bg right]` with no percentage**: the theme forces
the split to 50/50, and a different percentage only narrows the text box without
moving the photo.

```markdown
<!-- _class: half -->

![bg right](photo.jpg)

# Title

Body text.
```

The title is held to the left half, so a long one wraps instead of running over
the photo — and it is anchored by its bottom edge, so it **grows upwards**. A
one-line and a three-line title leave the red rule and the body underneath in
exactly the same place.

The right half does not have to be a photo. Wrap anything in a `div` with the
`right` class and it is stacked and centred in that half. The field is free: it
carries no type style and no inset of its own, so it takes a code block, a list,
a table or an inline SVG, and gets the full 960 px to do it in — a code panel
bleeds off the right edge of the slide, which is the intent, not an oversight. A
table is the one thing that keeps the width of its own contents, centred; wrap
it in `wide` when it should fill the field instead:

````markdown
<div class="right">

```cpp
int main() { return 0; }
```

</div>
````

Roughly sixty columns of code fit across it. For a single big glyph, compose the
field with the type helpers rather than reaching for CSS:

```markdown
<div class="right symbol pale">

∴

</div>
```

**`duo`**, **`trio`** and **`band`** share one footing: photos pinned across the
top, and a band across the bottom carrying the title on the left and the running
text on the right half. That band is the same strip on all three, and the text
hangs from a fixed line inside it, so the first row lands in the same place
whichever layout you are on and however long the text runs — three slides in a
row do not jitter. Four rows is the practical maximum; past that the text
reaches the bottom edge. Order matters — photo, caption, photo, caption, …, then
the running text, then the `h1`. Bold runs in a caption come out red.

```markdown
<!-- _class: duo -->

![](left.jpg)

#### Something in **light**

![](right.jpg)

#### Something in **shadow**

The running text, however many paragraphs it runs to.

# Title
```

`trio` takes three photos, or two to six with `columns-2` … `columns-6` — the
photographs and their rules are rescaled to match, though past four they are
smaller than their own captions. `band` takes one image, or up to four with
`columns-2` … `columns-4`, sharing the band edge to edge with no gutter; it has
no captions.

**`image`** — one photo covering the slide, centred, undistorted, cropped to
fit. Like `cover`, `half`, `side` and `band`, it takes a credit line in the top
right corner — see *Crediting a photograph* below. The photo is never veiled or dimmed: a title comes out bottom left carrying
its own soft shadow, which lifts it off a busy picture without touching the
picture itself.

```markdown
<!-- _class: image -->

![](photo.jpg)

# Optional title
```

**`split`** — half the slide black, half white, with a free field on each half.

```markdown
<!-- _class: split -->

<div class="left">

# Before

What it used to be.

</div>

<div class="right">

# After

What it is now.

</div>
```

The field is the same one `half`, `side` and `board` use — a half-slide column,
full height, contents stacked and centred — so each side takes a title, a
paragraph, a list, a code panel, a picture or an inline SVG, at whatever length
it needs.

Each half is its own colour scope, so everything inside comes out right without
your having to think about it: a code panel on the black half gets the dark
panel and the dark syntax colours, a table gets the light rule, an SVG is
inverted. `mirror` moves the black half to the right and the ink follows; the
fields do not move.

**`poster`** — a single large statement, centred on both axes, staying centred as
it grows to two or three rows. Add `dark` for the black version.

```markdown
<!-- _class: poster -->

# Everything in its **place**
```

The statement is a title, written `#` like every other title in the theme.
Anything else on the slide is ordinary content at the body size, so a poster can
carry a line under its statement, or a list, without the two competing:

```markdown
<!-- _class: poster -->

# Everything in its **place**

And the line underneath, at the size of any other line in the deck.

- or a list, whose rows range left while the block stays centred
```

**`comparison`** — one `h3` per column, then its text and list; the `h1` goes
last and lands at the bottom left, or bottom right with `mirror`. An `h2` lands
beside it, in the same bottom strip `duo`, `trio` and `band` use, so a subtitle
sits in the same place whichever of the four you are on — and here, where the
strip is placed and the columns are in flow, `##` is the only way to reach it.
The row of column headings starts on the same line as the title of an
ordinary slide, and the columns run between the same side margins as every
other layout — only the gutter between them is the template's own. Two columns
by default, `columns-3` … `columns-6` for more. Past four the columns get narrow — prefer bare lists over
prose. For plain running text in columns you do not need this layout at all: put
`columns-2` on an ordinary slide and the body runs in columns with the title
spanning them.

```markdown
<!-- _class: comparison columns-3 -->

### First

A line about it.

- a point
- another one

### Second

…

### Third

…

# Title
```

**`board`** — one free field across the top of the slide and the title of
`comparison` under it, at the bottom left. Nothing inside the field is placed
for you: whatever the slide carries is stacked and centred on both axes, so it
takes a table, a diagram, a code block, an inline SVG or one big glyph as
readily as a paragraph. It is the free field of `half` grown to the full width,
and it is centred in exactly the rectangle a full-bleed image fills on `band` —
so a diagram on one slide and a photograph on the next sit on one centre line.

```markdown
<!-- _class: board -->

| A | B |
| --- | --- |
| a | b |

An optional line about it.

# Title
```

Every edge of the field is borrowed rather than invented: the sides sit on the
left margin of `half` and its mirror on the right, and the top and bottom on the
band of photograph of `band`. Reach for it when what you want to show is one
thing, wide, and the running text is a caption to it. Here too a table keeps the
width of its own contents — add `wide` to the directive, or wrap the table in
`<div class="wide">`, when it should span the field.

**`agenda`** — an `h1` and an ordered list. The theme draws the grey numerals
and the red dashes.

## Modifiers

Combine with any layout, in the same directive:

| Modifier | Effect |
| --- | --- |
| `dark` | Inverts the slide to black: text, table rules, list markers, code, pagination, footer. |
| `mirror` | Puts the title, its rule and the body on the other side. |
| `centered` | Centres the content, red rule included. |
| `no-rule` | Drops the red rule under the title. |
| `no-indent` | Pulls the body back to the margin, out from behind the title. |
| `columns-2` … `columns-6` | How many of whatever the layout counts. |
| `debug` | Draws the box every element got, and lets overflow show. Not for a finished deck. |

### Which side things are on

Every layout hangs its title off the left, with the red rule bleeding off that
edge. There are no exceptions, which is the point: the rule is the loudest thing
on most slides, and a rule that changes sides from one slide to the next reads
as a mistake rather than as a decision.

To go the other way on a slide that wants it, there are two mechanisms, and
which one you use depends on whether anything else on the slide already implies
a side.

**A photograph implies one.** On `half` and `side`, write `![bg left]` instead of
`![bg right]` and the layout mirrors itself — title and rule to the outer edge,
the body ranged left in a box that hugs the same edge, the slide number back in
the corner the photo is no longer covering. There is no modifier to add, and
therefore no way for the picture and the type to end up on the same half.

```markdown
<!-- _class: half -->

![bg left](photo.jpg)

# Title

Body text.
```

The free field has no such mark, so there you say it: `<div class="left">` is
the mirror of `<div class="right">`, and it carries the title with it.

**Otherwise, `mirror`.** On the everyday slide it moves the title, the rule and
the indent all at once. On `comparison` and `board` it takes the title to the
bottom right, which is where the reading finishes on those two — the line across
the top, then the columns left to right — so it is the one they most often want.
On `split` it means something else again: the black half moves to the right, and
the columns do not move with it. The first thing you wrote stays the first thing
on the left, and only the ink and the paper trade places.

```markdown
<!-- _class: comparison mirror -->
```

`centered`, `poster` and `split`'s two titles are centred and have no side to be
on, so `mirror` leaves them alone.

`columns-N` is one modifier, not four: it says how many of something a slide
has, and each layout takes it to mean the thing it counts.

| On | It counts |
| --- | --- |
| *(the everyday slide)* | Text columns, with the title spanning them. |
| `comparison` | Text columns. Two by default. |
| `trio` | Photographs in the row. Three by default; past four they get small. |
| `band` | Panels sharing the strip, edge to edge, no gutter. One by default. |

### Text helpers

For inline runs, wrap them in a `span`; for a whole slide, put one in the class
directive. The sizes are steps of the theme's own scale, so asking for one by
hand never invents a size the deck does not already use:

| Helper | Size | For |
| --- | --- | --- |
| `.xsmall` | 24 | A listing or a table that will not fit at 28. |
| `.small` | 28 | Smaller than the body — what code blocks and tables are set in. |
| `.medium` | 32 | The body size — how you get back to it after reaching for another. |
| `.large` | 48 | A line that needs to carry further than the body. |
| `.xlarge` | 64 | Between the two — bigger than a line of the body, short of a title. |
| `.xxlarge` | 80 | A statement, a figure — the title size, off a title. |

Above those the **symbol family**, one helper per step, for a glyph or a number
rather than a sentence — the name is the instruction. All six carry the display
weight and a line box tight around the glyph:

| Helper | Size | For |
| --- | --- | --- |
| `.symbol-xxsmall` | 128 | A numeral standing beside text rather than behind it. |
| `.symbol-xsmall` | 192 | |
| `.symbol-small` | 256 | |
| `.symbol` | 384 | The default rung — what you get when you do not ask for one. |
| `.symbol-large` | 512 | |
| `.symbol-xlarge` | 768 | The size of the `?` on `question`. One glyph, and only one. |

Plus `.gray`, `.pale` and `.light` for tone and weight, and `.red` with the four
colours beside it — see *The content series* below.

The first four **carry into a code block and into a table**, which is the only
way to resize either: neither a fenced block nor a markdown table takes a class
of its own, so say it further up and it reaches down. `.xlarge` and `.xxlarge`
carry into a table but not into code — a short table set that large is a figure,
a listing at 64 or 80 is not something anyone wants — and the symbol six into
neither, at any size, being glyphs.

````markdown
<!-- _class: xsmall -->    the whole slide, code and tables included

<div class="xsmall">       just this listing, or just this table

```cpp
int main() { return 0; }
```

</div>
````

One more helper is width rather than size: **`.wide`** stretches a table to the
full measure of whatever holds it — the free field of `half` and `board`, or
the text column of the everyday slide. Everywhere, a table otherwise sits at
the width of its own contents. It reaches the table the same way the sizes do,
through a variable (`--table-width`), and takes the same two routes: the class
directive for every table on the slide, the `div` for one.

Both routes work for every helper — the class directive sizes the slide, the
`div` sizes one block. If you fork the theme and add a helper of your own, note
that each is declared **twice**, as `section.name` and as `.name`: Marpit scopes
a selector that does not start with `section` as a descendant of the slide, so
the bare form alone reaches a `div` inside the slide but never the slide itself,
and a class directive using it would silently do nothing at all.

### The scale behind them

Twelve steps in two families of six, on the 4 px grid. **`content`** is type
meant to be read; **`symbol`** is type meant to be looked at — a glyph, a
numeral, a formula of three characters, never a sentence at any of its six
sizes. Within a family each step is named for where it falls and nothing else,
which is why the variable says `--fs-content-large` rather than `--fs-subtitle`:
48 is also the size of a blockquote, of a row of `agenda` and of a column
heading on `comparison`, and a name with room for one job would have been wrong
about the other three.

| Family | Steps |
| --- | --- |
| `--fs-content-*` | `xsmall` 24 · `small` 28 · `medium` 32 · `large` 48 · `xlarge` 64 · `xxlarge` 80 |
| `--fs-symbol-*` | `xxsmall` 128 · `xsmall` 192 · `small` 256 · `medium` 384 · `large` 512 · `xlarge` 768 |

The symbol six are every multiple of 64 at 2, 3, 4, 6, 8 and 12 times, so the
ratio between neighbours alternates 3:2 and 4:3 and every second step is a
doubling — 128·256·512 and 192·384·768, two doubling series interleaved. If you
retune them, pick sizes that hold the alternation rather than sizes that look
round on their own.

Four of the steps the theme never spends on anything itself — **64**, **192**,
**256** and **512** — but each has a helper like every other, so a deck can ask
for any of the twelve. A step the theme does not use is not the same as a step
you cannot reach.

Every step has a helper, and all but one are named after the step they set. The
exception is `.symbol`, which sets `--fs-symbol-medium` (384) as the bare name of
its family — the rung you get when you do not ask for one.

### The content series

`--red` is the theme's own and it is spoken for: the rule under every title, the
bars of `agenda` and the red dash beside each of its rows, a bold word in a
heading. (The dash that marks an ordinary list row is a different thing — it is
set in the ink of the page, like the text it belongs to.)
The four colours beside it are yours. They are declared at the top of the file
as one series with the red at its head, and **no rule in the theme reads any of
them** — they are for what you put on a slide, never for what the theme draws
around it.

| Class | Colour |
| --- | --- |
| `.accent-1` | `#fa3a36` — the theme's red; `.red` is the same colour under the name it already had |
| `.accent-2` | `#f6006a` |
| `.accent-3` | `#af1cbc` |
| `.accent-4` | `#8047cd` |
| `.accent-5` | `#4f5fc0` |

It is a ramp rather than a set — red to blue through a pink and two purples, in
that order — so two neighbours are close and the two ends are far apart. Take
them from the ends when the difference has to carry to the back of the room, and
from anywhere when it does not.

The same two routes as the size helpers: a `span` for a run, a class directive
for the slide.

```markdown
Red, then <span class="accent-3">a purple</span>, then
<span class="accent-5">the blue</span>.
```

The classes set `color` and nothing else. For a shape rather than a word, read
the variable straight — a diagram is half of why the series exists, and a custom
property declared on `:root` reaches an inline style like any other inherited
value:

```html
<div style="background: var(--accent-4); height: 96px"></div>
<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="var(--accent-2)" /></svg>
```

That route needs `html: true` in your config. Marp's default allowlist keeps the
tag and **silently drops the `style` attribute** — a `<div style="…">` comes out
as a bare `<div></div>`, so a row of swatches renders as nothing at all and
nothing warns you. The classes above need no such setting.

```yaml
# .marprc.yml
html: true
```

Inside an inline `<svg>`, the page's ink is the default. SVG's own initial
fill is black — not the ink, which is what an unfilled `<text>` or shape
plainly means — so on the black layouts every label left unfilled simply
vanished, black on black. The theme hands `currentColor` to any `<svg>` that
does not declare a root `fill` of its own: leave labels and shapes unfilled
and they follow the ground, light or dark; write `stroke="currentColor"` for
outlines that should do the same; and anything that declares its own `fill` —
an accent, the red — stays exactly what it says. `stroke` gets no such
default on purpose: its initial value is `none`, and handing it a colour
would draw outlines the diagram never asked for.

Retune `--red` and the head of the ramp moves with it, which is the intent: the
first colour of the series *is* the theme's accent rather than a copy of it. And
`**bold**` in a heading stays red on a slide you have given an accent class — it
is a device of the theme's, not a follower of the local colour.

**What the five promise.** They are anchors, the same hex on a white slide and
on a black one, and the last three sit exactly where holding both grounds put
them: the ramp darkens as it runs, and each of them rides as dark as black
allows. Every one of the five keeps at least 3.7 : 1 against white *and* against
black (against white 3.7, 4.1, 5.7, 5.7 and 5.6 : 1; against black 5.7, 5.1,
3.7, 3.7 and 3.7 : 1), so any of them can set a word on either ground — the
black layouts included. What that does not buy is distance inside the family: to
red-green colour-blindness the purple, the violet and the blue are nearly one
colour. That is what taking from the ends is for — 1 against 5 stays far apart
to every eye.

### Diagrams in an `.svg` file

Everything above is for markup written *in* the slide. A diagram that lives in
its own file — `![](figure.svg)` — arrives as an `<img>`, and an image is a
separate document: no custom property and no `currentColor` crosses that
boundary, so a figure cannot read the palette the way an inline shape can.

The theme's contract for those files is: **draw once, in the light palette, on
a transparent background** — ink `#000000`, quiet rules `#cbcbcb`, the theme's
red `#fa3a36` or any of the ramp for an accent, and no background rectangle.
On a white slide the file renders as drawn. On the black layouts (`dark`,
`cover`, `question`, `image`) the theme inverts SVG images and turns the hues
back around, so the ink comes out white, the grays land where the dark palette
wants them, and an accent comes back as a lighter shade of itself rather than
its complement. You keep one file per figure and a slide can change ground
without touching it.

Two edges worth knowing. The inversion matches SVG only — a photograph or a
PNG on a dark slide is left alone, which also means a *raster* diagram will
not adapt; export diagrams as SVG. And in a PDF export the filter rasterises
the figure's own box (the rest of the page stays vectorial), so a hairline in
a figure on a black slide prints as pixels rather than strokes.

### Crediting a photograph

Five layouts carry a photograph big enough to want a credit on it, and all five
take one the same way — a Marp footer directive:

```markdown
<!-- _class: half -->
<!-- _footer: photo: someone -->
```

It lands in the **top right corner of the picture**, on all five and with no
exception — which is the point: the bottom right is the slide number's, the
bottom left is the title's on four layouts, and a credit that moves from one
corner to another between two slides reads as a mistake rather than as a
decision. On a mirrored `half` or `side` that corner is the photograph's inner
edge, so the credit stays on the picture rather than crossing to the paper.

It is small print, but it is small print on a photograph, so it is set heavier
than the body rather than lighter: the title weight, at the size code and tables
take, over a halo that holds it up against a bright picture as well as a dark
one. The ink is the tone the palette keeps for text that falls on a photograph.

The same directive without `_` (`<!-- footer: ... -->`, or `footer:` in the
front matter) puts a line on every slide from there on, in the same corner.

### Eyebrows and captions

Two small things the everyday slide can do:

```markdown
###### Where we are          <!-- an eyebrow: caps, spaced, in the grey -->

# The title

<figure>

![](photo.jpg)

<figcaption>What it shows.</figcaption>

</figure>
```

`h5` and `h6` are the two headings below the ones the layouts use: `h5` is a
run-in at body size, `h6` the eyebrow — the label above a title saying what part
of the talk this is, and the only place other than a cover title where the theme
sets capitals.

The eyebrow is placed rather than flowed, and that is the point of it: **it does
not move the title**. A slide with an eyebrow and a slide without put their
title, and the red rule under it, on exactly the same line — which matters,
because the rule is the one thing on the page an audience notices moving. It
sits centred in the space above the title and follows it across under `mirror`.

It goes above the title on **every layout**, not only the ones that keep the
title at the top. On the eight that put it lower — `half`, `side`, `duo`,
`trio`, `band`, `image`, `comparison` and `board` — it is placed against the
title itself rather than left at the top of the slide, where it would be in the
opposite corner from the thing it labels. Write it the same way everywhere.

One limit worth knowing: on the four whose title grows *upwards* from a fixed
bottom edge — `half`, `side`, `comparison`, `board` — the eyebrow is placed one
title-line above that edge, so **a two-line title on those four will reach its
eyebrow**. Their titles are short by design; if you need both, shorten the title.

### The line beside the title

Five layouts carry a sentence in the bottom strip, level with the title and
reading as its subtitle: `duo`, `trio`, `band`, `comparison` and `board`. It is
a second-level heading, and that is the whole convention — the title is `#` and
the line under it is `##`:

```markdown
<!-- _class: duo -->

![](one.jpg)

#### First

![](two.jpg)

#### Second

## The sentence that goes beside the title.

# Title
```

Where you write it in the file does not matter, on any of the five. It is a
**subtitle by position, not by type**: in the strip it takes the size, the
weight and the leading of running text, and its `**bold**` is the body's bold —
a weight, not the red a bold run takes inside a real title.

On `duo`, `trio` and `band` a plain paragraph still lands in the strip too,
which is what those layouts always did; `##` is the way to say it out loud, and
the only way to say it on `comparison` and `board`.

## Two weights

There are two on the page, and the theme never reaches for a third:

| Weight | Where |
| --- | --- |
| **800** | Headings, table headers, the numerals on `agenda`, `.symbol`, `**strong**` and links in body copy, and the header and footer. |
| **300** | Running text, everywhere, on every layout, at every size. |

Montserrat is a variable font, so both are real weights rather than the
browser's synthetic thickening, and 800 against 300 is a difference you can see
from the back of the room. `--fw-strong` is kept as a separate name from
`--fw-title` even though they land on the same number, so that retuning a bold
run in a sentence does not drag every heading with it.

A link is marked the same way — 800, in the ink of the page, with a rule under
it to tell it from a plain bold run. It used to come out red, which put it in
competition with the one thing the red is for and made every mention of a URL
the loudest thing on the slide.

Bold marks a word, never a block — the header and the footer are the one
exception, and they earn it: they are the only text on the page that regularly
lands on a photograph, and Montserrat Light at that size disappears into one.

A row of a list is a sentence like any other
and takes the running weight, however large it is set and whatever it stands
beside — the rows of `agenda` and the list rows of `comparison` are 300, the
same as a paragraph. What tells them apart from body copy is their size and
what is next to them, not their weight. Their marker is an en dash, the same
on every layout; an ordered list keeps its numbers.

## Red in a title

`**strong**` picks out a word in red in **any** heading, on any layout — cover
titles, column headings, the lot:

```markdown
# Everything in its **place**
```

It is a colour accent and nothing else: the word keeps the heading's own weight,
so it changes hue without also changing shape. On the black slides it comes out
red against white or black text alike.

In body copy `**strong**` stays what it always was — a weight change, not a
colour. That holds on `poster` too: its statement is a heading, so its bold is
red like any heading's, and the supporting text under it is body copy like any
other.

## Exporting

```bash
marp deck.md -o deck.html
marp deck.md --pdf -o deck.pdf
marp deck.md --pptx -o deck.pptx
marp deck.md --images png -o slide.png    # one image per slide
marp -s .                                 # live-reloading server
```

Add `--allow-local-files` whenever the deck references images on disk.

Two things worth knowing about exports:

- **Export to PDF, not PNG, when the colour of the text matters.** In the PDF
  the text stays vectorial and pure black. Rasterising to PNG, Chromium uses
  subpixel antialiasing and the thin strokes of Montserrat Light come out
  fringed with colour. That is the rasteriser, not the theme.
- **If `--pdf` or `--images` hangs, add `--browser edge`.** Marp drives a
  headless browser and picks Chrome by default; with Chrome already open on your
  profile the launch can stall for minutes with nothing to show for it.

## Canvas, type and licence

The canvas is a fixed **1920 × 1080 px**. Every measurement in the theme is in
pixels on that canvas, so the geometry is stable and predictable — if you fork
it and move a number, you know exactly what you are moving.

Body copy is 32 px, Light, on a 1.44 leading, and that is set once on `section`
rather than per layout: a paragraph reads the same wherever it lands. Fork it in
one place and the whole deck follows.

The same holds for everything else the theme decides. The palette, the type
scale, the spacing scale, the three weights, the red rule, the list marker and
the count of columns are all variables declared at the top of the file; a layout
that departs from one resets the variable on itself rather than restating the
property. If you are retuning the theme, the first two hundred lines are where
the decisions live — not the thousand below them.

The palette is in three groups, and it is worth knowing which is which if you
fork it. Three colours are **anchors** — black, white and the red — and mean the
same thing wherever they appear. The nine under them are **contextual**: the
page, the ink, the secondary ink, the table rule, the two code backgrounds and
the three code colours. Those nine are redefined exactly once, on the four
layouts that run their text on black — `dark`, `cover`, `question` and `image` —
and everything else in the file reads them without knowing which side it is on.
That is why `dark` has no rules of its own: change `--pre-bg` and a code panel
follows on both a white slide and a black one.

The five at the end are the **content series**, described above, and they are the
only colours in the file the theme itself never draws with. Nothing breaks if you
replace all five; nothing else in the deck moves.

Change `--red` and you have a different theme, in one line — and the head of the
series follows it, since `--accent-1` is that same red rather than a copy of it.

Maths comes out of one of two engines, and which one decides how much of it the
theme can reach. Marp picks **MathJax** unless the deck asks for the other with
`math: katex` in the front matter, and MathJax in its SVG mode writes glyph
outlines rather than text — a `<path>` takes no typeface, so no stylesheet can
change the face it is set in.

A displayed equation (`$$…$$`) gets more air above and below it than a paragraph
does, on either engine: it is a block the eye stops on, and at the paragraph gap
it read as one more line of the paragraph it had just interrupted. The theme
zeroes what each engine puts there and spaces the two identically, so a slide
looks the same whichever one built it.

`--font-math` is therefore a **KaTeX-only** knob. It ships as Times New Roman.
KaTeX names its own faces on every span it writes, so the theme has to reach the
spans to override them — which it does. Worth knowing before you change it:
KaTeX measures its own faces and writes the spacing into the markup in ems, so
any other family is set on metrics that are not its own, and a family missing the
mathematical operators — quantifiers, relations, arrows — will fall back glyph by
glyph and set one formula in two faces. Set it to `unset` to have KaTeX's own
faces back.

Montserrat is **embedded in the CSS as base64**, as a variable font of weight
100–900 in the `latin` and `latin-ext` subsets. Composing and exporting need
neither an internet connection nor installed fonts, and the HTML and PDF you
export are self-contained. That is most of the theme's ~300 kB. Code is set in
Consolas with system fallbacks; no monospaced font is embedded.

The theme is MIT licensed. Montserrat is under the SIL Open Font License 1.1.
`assets/placeholder.jpg` is filler for the example deck only — replace it with
your own before you publish anything.
