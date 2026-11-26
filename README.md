# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/lucaslml0/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/lucaslml0/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

## What this is

Sum up 26 November's world news in one image: a newspaper front page for
Thursday 26 November 2026. The lead story is the US unveiling new tariffs on
14 trading partners; below it, six more of the day's biggest stories — oil
jumping after the Houthis claimed a strike on Saudi Arabia's Ras Tanura
refinery, the AI rout that sent the Nasdaq down nearly 4%, leaked Russian
statistics putting the war dead near 500,000, an Israeli strike killing a
second Hamas security chief in a day, 31 killed in a fuel tanker fire on a
Cairo highway, and all hostages freed in the Cartagena supermarket siege —
plus an in-brief strip with South Korea's rate hike and the Bank of Japan
signalling faster hikes.

The image is drawn from scratch by `draw_entry.py` (Python + Pillow, no
fetched images) and copied to the output by `main.ts`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png` (1024×1024 PNG, under 1 MiB). To regenerate the
image from the drawing script instead:

```sh
python3 draw_entry.py
```

## Files

- `entry.png` — the front page image
- `draw_entry.py` — the script that draws `entry.png`
- `main.ts` — entrypoint: copies `entry.png` to `$MAKEFUN_OUTPUT_DIR`

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=w8dfntsk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
