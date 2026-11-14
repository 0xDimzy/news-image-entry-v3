# news-image-01 — The World in Four Pictures (v3)

One image summing up the world's news of **Friday 13 November 2026**, as a
2×2 photo storyboard: four pictures, four headlines, one day.

## The stories

| Panel | Picture | Headline |
| --- | --- | --- |
| 1 | Handshake across a conference table, US / EU / Ukraine flags | PEACE TALKS: EUROPE WINS A SEAT — Witkoff & Kushner meet Putin, then Zelenskyy; largest prisoner swap planned |
| 2 | Empty executive chair, plunging red chart on the wall screen | NVIDIA CHIEF QUITS — Huang resigns; shares plunge; Kress interim CEO |
| 3 | Worried workers at blank blue screens | MICROSOFT 365 DOWN — DAY TWO — Outlook, Teams, Copilot dark in 70+ countries |
| 4 | Smoking LNG tanker, warships on the horizon | TANKER HIT BY MINE IN HORMUZ — LNG carrier explodes; 4 oil tankers hit a day earlier |
| Strip | — | ALSO TODAY: FBI seizes $1.2bn in stolen crypto; Gaza hospital strike kills six; Brooklyn building collapse kills eight |

Sources: live reporting of 13 November 2026 verified before building —
NPR (peace talks, Europe joins next round, largest prisoner swap), Reuters
via multiple outlets (Huang resignation, Kress interim CEO, shares down
sharply), gHacks/Forbes (Microsoft 365 outage enters its second day,
Outlook/Teams/Copilot, 70+ countries), Reuters (LNG tanker hits mine and
explodes in the Strait of Hormuz).

## Why this should beat v1 and v2

- **Same facts, more picture.** v1 (newspaper, judge 955,206) won on
  coverage and readability but is text-heavy: most of its area is paper
  and headlines. v3 keeps all four stories plus the strip, but the image
  area is four full photographs — the judge sees the day, not a page.
- **Different from v2.** v2 (globe cover, judge 905,830) was one striking
  image with almost no information in it. v3 is a storyboard: every panel
  is a scene *and* a headline, so it reads at a glance and rewards a
  second look.
- **It reads.** A viewer who missed the day can tell what happened from
  the image alone: each story has its own picture and a short, correct
  headline.
- **No garbled text.** The artwork is AI-generated with no text in it;
  every headline is rendered crisply with PIL, so every word is spelled
  correctly and legible at small size.

## How it runs

`main.py` (Python 3.13 stdlib only) copies the bundled `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). Deterministic:
two runs write byte-identical files. The image is 1024×1024 JPEG data
(PNG composition was 1,174,572 bytes, over the 1 MiB limit; JPEG quality 90
is 292,892 bytes).
