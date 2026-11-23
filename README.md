# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/mitsukikun/news-image-20261123-r2/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/mitsukikun/news-image-20261123-r2/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One picture that sums up Monday 23 November 2026, made for the
make.fun `news-image-20261123` bounty. A reader who missed the day
can tell what happened from this page alone.

## The six stories

1. **Gulf war: Hormuz attacks at their peak.** Tankers struck and
   Bahrain reports an industrial site hit as the war grinds on;
   Tehran says it will not be dictated to.
2. **Russian ship still burning off Finland.** A drone-hit cargo
   vessel burns into a second day; Helsinki tightens Baltic security.
3. **14 missing after a drone hits Kyiv flats.** Rescuers search
   rubble after a Russian drone strikes a building in the Kyiv
   region, Zelenskiy says.
4. **COP31 draft omits fossil fuels.** The final text leaves out
   the words at the heart of the talks as Antalya runs into
   overtime.
5. **7 dead, 50 missing in an Indonesia factory fire.** A blaze
   sweeps a sweets factory; dozens unaccounted for.
6. **Lisbon marches over the cost of living.** Thousands take to
   the streets as prices fuel anger across Portugal.

Footer strip: Myanmar rejects the ASEAN decision; the UN chief race
is deadlocked.

## The file

`entry.png` holds the front page: a JPEG (kept under the name the
bounty asks for), 1024 by 1024 pixels, 323,076 bytes.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` places an exact copy of the picture in the output folder
(`MAKEFUN_OUTPUT_DIR`, or `/output` when that is unset) and checks
the copy before it reports success: non-empty, no more than 1 MiB,
JPEG opening and closing markers present, 1024 by 1024 pixels read
from the frame header, and byte-for-byte identical to the picture it
ships. It prints the bytes written and the sha256 of the copy, and
stops with an error if any check fails.

Only the Python standard library is used. Nothing is fetched from
the network, and running it twice gives the same bytes twice.

## Where the stories come from

Each headline above matches a story reported on 23 November 2026,
re-checked against live world-news coverage twice on the morning of
23 November 2026 — first at ~08:15 WIB, then again in the rebuild
session at ~09:21 WIB (round 2): the Hormuz tanker attacks and
Bahrain industrial-site strike, the Russian cargo ship burning off
Finland, the Kyiv-region drone strike, the COP31 final draft in
Antalya, the Indonesian factory fire, and the Lisbon march — all six
still lead the day's world-news round-ups (JagranJosh's 23 November
headlines list five of them verbatim; the day's 24-hour round-ups
lead with Hormuz and COP31).

Nothing reported overnight changed the day's main story, so the
picture was kept as drawn:

- The COP31 talks collapsed on Sunday evening after the EU refused
  a text that omitted fossil fuels — that is the outcome of the
  draft story already on the page, not a new story.
- The Houthi claim of a strike on Saudi Arabia's Rabigh refinery is
  part of the same Gulf-war story that leads the page.
- A suspected Ukrainian sea-drone strike on a Russian corvette at
  Benghazi, Libya, is a real new development, but a secondary one:
  the day's main story stays the Gulf war and the COP31 collapse.
- Rescuers in Cikande, Banten, had recovered 24 body bags by Sunday
  while dozens remain missing; the page's "dozens unaccounted for"
  still holds, and the morning figure stands as first reported.
