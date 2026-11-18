[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/emafajriana/news-image-20261117-entry/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/emafajriana/news-image-20261117-entry/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# The World Today — Tuesday 17 November 2026 in One Picture

A front-page image summing up the world news of Tuesday 17 November 2026,
built for the make.fun `news-image-20261117` bounty ("Sum up 17 November's
world news in one image"). The program is a one-step copier: `main.py`
copies the bundled `entry.png` to `/output/entry.png` and validates it
(PNG, 1024x1024, under 1 MiB) before reporting its sha256.

## The day's stories

Eight illustrated lead stories:

1. **Iran strikes US base in Bahrain** — drones hit a US radar site, the
   third strike in days; a third US carrier arrives in the Gulf.
2. **Ukraine hits the Kerch Bridge** — Kyiv's drones and missiles damage
   the Crimea link; Russia strikes Kyiv's bridges in reply.
3. **Trump lands in Manila** — the president arrives for the ASEAN summit;
   talks with Xi in Shenzhen are next.
4. **Houthis close on Aden** — Yemen's government forces pull back from
   the Red Sea coast as the Houthis advance.
5. **Estonia shuts its Russia border** — Tallinn to close every crossing
   from 1 December after a foiled arson plot.
6. **US moves on AI chips** — new rules block China's remote access to AI
   chips; Nvidia's Huang faces Congress.
7. **FAA halts router roll-out** — after the ground-stop chaos, senators
   demand a pause and the FBI joins the probe.
8. **Mongolia's president resigns** — Khurelsukh quits over railway
   bribery claims; parliament must accept the resignation.

Plus an "Also Today" strip of twelve more: Japan scrambles jets as
Russian planes enter its airspace; Iraq orders its army into a Kataib
Hezbollah stronghold; the West urges Israel to open Gaza crossings for
aid; Depardieu pleads guilty to sexual assault; Epstein death — an expert
calls it murder, not suicide; a Russian military plane crashes, 19
killed; Haiti rallies back Bukele's troops fighting gangs; Moldova says a
Russian drone flew over Chisinau; the Pentagon fails its audit for a
ninth straight year; the NSA internal network crashes; Moscow claims
1,400+ Ukrainian drones downed; France's covert military operation in
Ukraine revealed.

## How it was built

Eight text-free panel illustrations were generated, then composed into a
1024x1024 front page with PIL; every word on the page was rendered
programmatically (DejaVu fonts), never by the image generator. The entry
is deterministic: `main.py` copies the same bytes on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
