# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/mitsukikun/news-image-20261123-r2/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/mitsukikun/news-image-20261123-r2/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One picture summing up the world's news of Monday 23 November 2026 — a
front page for the day, built as a single image.

## The six stories on the front page

1. **Gulf war: Hormuz tanker attacks at their peak, Bahrain industrial site hit** — the lead story, with the Strait of Hormuz tanker attacks reaching their worst point and an industrial site in Bahrain struck.
2. **Russian ship still burning off Finland** — a Russian vessel continues to burn off the Finnish coast.
3. **14 missing after a drone hits Kyiv flats** — a drone strike on residential flats in Kyiv leaves 14 people missing.
4. **COP31 draft omits fossil fuels** — the COP31 draft text leaves fossil fuels out.
5. **7 dead, 50 missing in an Indonesia factory fire** — a factory fire in Indonesia kills 7 and leaves 50 missing.
6. **Lisbon marches over the cost of living** — crowds march in Lisbon against the rising cost of living.

Footer strip: **Myanmar rejects the ASEAN decision**; **the UN chief race is deadlocked**.

## Files

- `entry.png` — the front-page image (JPEG, 1024x1024, 323,076 bytes)
- `main.py` — copies `entry.png` to the output folder and self-checks it (JPEG markers, 1024x1024 frame header, ≤ 1 MiB, byte-identical to the shipped picture)
- `LICENSE` — MIT

## How to run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Without `MAKEFUN_OUTPUT_DIR` the image is written to `/output/entry.png`.
The program prints the bytes written and the sha256 of the copy, and
refuses to report success unless every self-check passes.

Deterministic: the same shipped picture is delivered on every run —
no network access, no randomness, no modification of the image.
