#!/usr/bin/env python3
"""Entry for make.fun news-image-20261117: copy the bundled front page to /output/entry.png.

The image (entry.png, beside this file) sums up the world news of Tuesday
17 November 2026: a front page with eight illustrated lead stories and an
"Also Today" strip of twelve more. This program only copies those bytes;
it never draws, downloads, or changes anything, so both grader runs write
the same file.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIM = 1024


def png_dimensions(path):
    """Return (width, height) of a PNG by reading its IHDR chunk."""
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file (bad signature)")
    if header[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk where expected")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")

    size = os.path.getsize(src)
    if size > MAX_BYTES:
        raise ValueError(
            f"entry.png is {size} bytes, over the {MAX_BYTES} byte limit"
        )
    width, height = png_dimensions(src)
    if width > MAX_DIM or height > MAX_DIM:
        raise ValueError(
            f"entry.png is {width}x{height}, over the {MAX_DIM}x{MAX_DIM} limit"
        )

    shutil.copyfile(src, dst)

    # Confirm the copy is byte-identical to the source before reporting it.
    with open(src, "rb") as f:
        src_digest = hashlib.sha256(f.read()).hexdigest()
    with open(dst, "rb") as f:
        dst_digest = hashlib.sha256(f.read()).hexdigest()
    if src_digest != dst_digest:
        raise ValueError("copied entry.png does not match the source bytes")
    print(f"Wrote {dst}: PNG {width}x{height}, {size} bytes, sha256 {dst_digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
