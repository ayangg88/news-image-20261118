#!/usr/bin/env python3
"""News-image entry: place the front-page image at the grader's output.

The image (entry.png, 1024x1024) is drawn at build time from Wednesday
18 November 2026's headlines and shipped in this repository; the program's
only job is to put an exact copy at /output/entry.png (or $MAKEFUN_OUTPUT_DIR
when set, which the kit uses for local runs).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(DST_DIR, exist_ok=True)
out_path = os.path.join(DST_DIR, "entry.png")
shutil.copyfile(SRC, out_path)

# Fail loudly if the copy is not a whole PNG, instead of handing the
# gate a broken file: the PNG signature is its first eight bytes.
with open(out_path, "rb") as fh:
    if fh.read(8) != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG")
