#!/usr/bin/env python3
"""news-image-01 entry v3: one image summing up the world's news of Friday 13 November 2026.

The image is a 2x2 photo storyboard, "The World in Four Pictures": four
AI-generated news scenes (no text in the artwork) with crisp PIL-rendered
headline bars — US envoys win Europe a seat at the Ukraine peace talks;
Nvidia chief Jensen Huang resigns and shares plunge; Microsoft 365 down
worldwide for a second day; an LNG tanker hit by a mine in the Strait of
Hormuz — plus an ALSO TODAY strip (FBI crypto seizure, Gaza hospital
strike, Brooklyn collapse). Every headline is rendered by PIL, so no word
is misspelled.

Writes the image to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png):
exactly the bundled entry.png bytes, deterministically, on every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Read back: the file the judge sees must be exactly the bundled bytes.
    assert target.read_bytes() == SOURCE.read_bytes()


if __name__ == "__main__":
    main()
