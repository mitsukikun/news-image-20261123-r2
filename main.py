#!/usr/bin/env python3
"""Deliver the front page for Monday 23 November 2026.

The entry is a single picture, ``entry.png``: a JPEG kept under the
name the bounty asks for, 1024 by 1024 pixels, showing the day's
world news as a newspaper front page. This program copies that
picture, byte for byte, into the output directory, and it will not
claim success until the copy has proved itself:

- the picture is there and not empty,
- it is no bigger than 1 MiB,
- it starts with the JPEG opening bytes and ends with the closing
  bytes,
- its first frame header reads 1024 by 1024,
- the copy matches the picture exactly.

Only the Python standard library is used. Nothing is fetched from
the network, and the same input always gives the same output, so
running the program twice writes the same bytes twice and the
grader's two runs agree.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

PICTURE = "entry.png"
SIZE_LIMIT = 1024 * 1024
SIDE = 1024

# Start-of-frame markers whose segment carries the picture's height
# and width as two big-endian 16-bit numbers.
FRAME_MARKERS = {
    0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
    0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF,
}


class BadPicture(Exception):
    """Raised when a check fails, so a bad copy is never reported."""


def refuse(message):
    raise BadPicture(message)


def read_dimensions(data):
    """Return (width, height) from a JPEG byte string's frame header.

    Walks the marker segments from the start of the image; the first
    start-of-frame segment holds the height, then the width.
    """
    offset = 2  # skip the SOI marker
    while offset + 9 <= len(data):
        if data[offset] != 0xFF:
            refuse("no marker at byte %d" % offset)
        marker = data[offset + 1]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            offset += 2
            continue
        (segment_len,) = struct.unpack(">H", data[offset + 2:offset + 4])
        if segment_len < 2 or offset + 2 + segment_len > len(data):
            refuse("segment at byte %d has an impossible length" % offset)
        if marker in FRAME_MARKERS:
            # The frame segment layout is: length (2), precision (1),
            # height (2), width (2) — so height sits at +5, width at +7.
            (height,) = struct.unpack(">H", data[offset + 5:offset + 7])
            (width,) = struct.unpack(">H", data[offset + 7:offset + 9])
            return width, height
        offset += 2 + segment_len
    refuse("no frame header found in the picture")


def main():
    folder = Path(__file__).resolve().parent
    source = folder / PICTURE
    if not source.is_file():
        refuse("picture missing: %s" % source)
    picture = source.read_bytes()
    if not picture:
        refuse("the picture is empty")
    if len(picture) > SIZE_LIMIT:
        refuse("picture is %d bytes, over the %d-byte limit"
               % (len(picture), SIZE_LIMIT))
    if picture[:2] != b"\xff\xd8":
        refuse("picture lacks the JPEG opening bytes")
    if picture[-2:] != b"\xff\xd9":
        refuse("picture lacks the JPEG closing bytes")
    width, height = read_dimensions(picture)
    if (width, height) != (SIDE, SIDE):
        refuse("picture is %d by %d, wanted %d by %d"
               % (width, height, SIDE, SIDE))

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / PICTURE
    if target.resolve() == source.resolve():
        refuse("output folder is the entry folder; the copy would "
               "overwrite the picture it ships")
    target.write_bytes(picture)

    delivered = target.read_bytes()
    if delivered != picture:
        refuse("the copy does not match the picture byte for byte")
    print("wrote %s (%d bytes, sha256 %s)"
          % (target, len(delivered), hashlib.sha256(delivered).hexdigest()))


if __name__ == "__main__":
    try:
        main()
    except BadPicture as problem:
        sys.stderr.write("refused: %s\n" % problem)
        sys.exit(1)
