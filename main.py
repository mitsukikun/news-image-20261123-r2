#!/usr/bin/env python3
"""news-image-20261123 — write the front page of Monday 23 November 2026.

The picture itself is shipped in this repository as ``entry.png`` (a JPEG
despite the name, which the competition allows). This program's only job is
to deliver that exact picture to the output folder and prove, before it
reports success, that the delivered copy is the genuine article:

  * it exists and is not empty,
  * it is no bigger than 1 MiB,
  * it opens with the JPEG start marker (FF D8) and closes with the JPEG
    end marker (FF D9),
  * the dimensions read from its JPEG frame header are 1024 by 1024, and
  * it is byte-for-byte identical to the picture shipped in this repo.

Nothing is downloaded, generated or modified: the same input bytes always
produce the same output bytes, so running the program twice writes the
same file twice.

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
    (without MAKEFUN_OUTPUT_DIR the output folder is /output)
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

# --- limits from the competition rules ------------------------------------
MAX_BYTES = 1 * 1024 * 1024          # 1 MiB
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
JPEG_START = b"\xff\xd8"            # SOI marker
JPEG_END = b"\xff\xd9"              # EOI marker

SOURCE_NAME = "entry.png"           # the picture shipped beside this file
OUTPUT_NAME = "entry.png"           # the name the judge expects in /output


def fail(message: str) -> "SystemExit":
    """Abort with a clear reason; a failed copy must never look like a win."""
    return SystemExit(f"error: {message}")


def read_frame_dimensions(data: bytes) -> tuple[int, int]:
    """Return (width, height) from the first JPEG frame (SOF) segment.

    Walks the JPEG marker stream starting after the SOI marker. Standalone
    markers (SOI, EOI, RSTn, TEM) carry no length field; every other segment
    does, so the walk skips each segment by its declared length until it
    reaches a Start-Of-Frame marker, whose payload stores the height then
    the width as two big-endian 16-bit values.
    """
    if data[:2] != JPEG_START:
        raise ValueError("not a JPEG: missing SOI marker (FF D8)")

    pos = 2
    while pos + 1 < len(data):
        if data[pos] != 0xFF:
            raise ValueError(f"bad marker byte 0x{data[pos]:02x} at offset {pos}")
        marker = data[pos + 1]
        pos += 2

        # Markers with no payload: restart markers, SOI/EOI/TEM.
        # Skipping them is safe: they are always exactly two bytes.
        if marker == 0xD8 or marker == 0xD9 or marker == 0x01 or 0xD0 <= marker <= 0xD7:
            continue

        if pos + 2 > len(data):
            raise ValueError("truncated segment length")
        length = int.from_bytes(data[pos:pos + 2], "big")
        if length < 2 or pos + length > len(data):
            raise ValueError("segment length runs past the end of the file")

        # SOF0 (baseline) and SOF2 (progressive) both carry the dimensions.
        if marker in (0xC0, 0xC2):
            payload = data[pos + 2:pos + length]
            if len(payload) < 5:
                raise ValueError("frame segment too short for dimensions")
            height = int.from_bytes(payload[1:3], "big")
            width = int.from_bytes(payload[3:5], "big")
            return width, height

        pos += length

    raise ValueError("no JPEG frame (SOF) segment found")


def verify_copy(source: bytes, copy: bytes) -> tuple[int, int]:
    """Check the delivered copy against every rule; return (width, height)."""
    if not copy:
        raise ValueError("output is empty")
    if len(copy) > MAX_BYTES:
        raise ValueError(f"output is {len(copy)} bytes, over the 1 MiB limit")
    if not copy.startswith(JPEG_START):
        raise ValueError("output does not start with the JPEG SOI marker FF D8")
    if not copy.endswith(JPEG_END):
        raise ValueError("output does not end with the JPEG EOI marker FF D9")
    width, height = read_frame_dimensions(copy)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            f"frame is {width}x{height}, expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )
    if copy != source:
        raise ValueError("output differs from the shipped picture")
    return width, height


def main() -> int:
    here = Path(__file__).resolve().parent
    source_path = here / SOURCE_NAME
    if not source_path.is_file():
        raise fail(f"shipped picture not found: {source_path}")

    source = source_path.read_bytes()

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / OUTPUT_NAME
    output_path.write_bytes(source)

    copy = output_path.read_bytes()
    try:
        width, height = verify_copy(source, copy)
    except ValueError as exc:
        output_path.unlink(missing_ok=True)
        raise fail(str(exc))

    digest = hashlib.sha256(copy).hexdigest()
    print(f"wrote {output_path} ({len(copy)} bytes, {width}x{height} JPEG)")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
