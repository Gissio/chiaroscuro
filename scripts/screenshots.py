#!/usr/bin/env python3
"""Regenerate the README screenshots from example.md.

Renders the example deck with marp-cli, then composes the images in
assets/screenshots/: the full-size hero, the reduced series shot, and
the rows of three thumbnails on a grey ground.

Requires marp-cli on the PATH and Pillow (pip install Pillow).
Run from anywhere: paths are resolved relative to this file.
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "screenshots"

# Slide numbers refer to example.md, 1-based, in deck order.
SLIDES = {
    "cover": 1,
    "agenda": 2,
    "question": 3,
    "poster": 4,
    "default": 5,
    "indent": 6,
    "columns": 7,
    "series": 8,
    "scale": 9,
    "half": 10,
    "half-field": 11,
    "half-glyphs": 12,
    "half-mirrored": 13,
    "side": 14,
    "board": 15,
    "board-photo": 16,
    "image": 17,
    "duo": 18,
    "trio": 19,
    "comparison": 20,
    "comparison-mirror": 21,
    "dark": 22,
    "split": 23,
    "poster-dark": 24,
}

# name -> (slide, width): rendered alone, scaled to the given width.
SINGLES = {
    "hero": ("cover", 1920),
    "series": ("series", 1440),
    "scale": ("scale", 1440),
}

# name -> three slides, left to right, matching the README captions.
ROWS = {
    "layouts-row-1": ["agenda", "poster", "question"],
    "layouts-row-2": ["default", "indent", "half"],
    "layouts-row-3": ["side", "duo", "trio"],
    "layouts-row-4": ["board", "board-photo", "image"],
    "layouts-row-5": ["split", "comparison", "poster-dark"],
    "modifiers-row-1": ["dark", "columns", "comparison-mirror"],
    "modifiers-row-2": ["half-mirrored", "half-field", "half-glyphs"],
}

TILE = (640, 360)  # one thumbnail in a row
PAD = 8            # grey border around a row
GAP = 8            # grey gutter between thumbnails
BG = (217, 217, 217)
QUALITY = 90


def render_deck(tmp: Path) -> dict[str, Path]:
    marp = shutil.which("marp")
    if marp is None:
        sys.exit("marp-cli not found on the PATH")
    subprocess.run(
        [marp, "example.md", "--images", "png", "--image-scale", "1",
         "-o", str(tmp / "slide.png")],
        cwd=ROOT, check=True,
    )
    rendered = sorted(tmp.glob("slide.*.png"))
    if len(rendered) != max(SLIDES.values()):
        sys.exit(f"SLIDES maps {max(SLIDES.values())} slides, marp produced "
                 f"{len(rendered)} — the map is stale")
    return {name: rendered[n - 1] for name, n in SLIDES.items()}


def save(img: Image.Image, name: str) -> None:
    path = OUT / f"{name}.jpg"
    img.save(path, quality=QUALITY, optimize=True)
    print(f"{path.relative_to(ROOT)}  {img.width}x{img.height}")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        slides = render_deck(Path(tmpdir))

        for name, (slide, width) in SINGLES.items():
            img = Image.open(slides[slide])
            height = round(width * img.height / img.width)
            save(img.resize((width, height), Image.LANCZOS), name)

        for name, keys in ROWS.items():
            canvas = Image.new(
                "RGB",
                (len(keys) * TILE[0] + (len(keys) - 1) * GAP + 2 * PAD,
                 TILE[1] + 2 * PAD),
                BG,
            )
            for i, key in enumerate(keys):
                tile = Image.open(slides[key]).resize(TILE, Image.LANCZOS)
                canvas.paste(tile, (PAD + i * (TILE[0] + GAP), PAD))
            save(canvas, name)


if __name__ == "__main__":
    main()
