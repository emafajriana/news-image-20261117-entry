[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/emafajriana/news-image-20261117-entry/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/emafajriana/news-image-20261117-entry/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# Tuesday 17 November 2026: 40 stories, 6 continents, one front page and a map

A front-page image summing up the world news of Tuesday 17 November 2026,
built for the make.fun `news-image-20261117` bounty ("Sum up 17 November's
world news in one image"). The page follows the classic newspaper layout:
a date-only serif masthead on cream paper, three hero stories and twelve
more pictured stories, then a world map with numbered pins and a dense
index of all 40 stories. `main.py` rebuilds the page deterministically
from the bundled assets in `assets/` and writes `/output/entry.png`,
validating it (PNG, 1024x1024, under 1 MiB) and reporting its sha256; if
the drawing stack is unavailable it falls back to copying the bundled
`entry.png`, which is byte-identical to a built page.

## The day's stories

Fifteen pictured stories (numbered badges on the panels, matching pins on
the map):

1. **US and Iran trade fire across the Gulf** — US jets strike a missile
   site on Qeshm Island; Iranian drones hit a US radar site in Bahrain
   for the third time in five days.
2. **Ukraine knocks out a section of the Kerch Bridge** — a span of the
   Crimea link collapses into the strait.
3. **Trump lands in Manila** — the president arrives for the ASEAN
   summit as Quad leaders agree their first joint patrol exercise.
4. **Ebola in DR Congo passes 11,000 cases** — more than 5,400 dead in
   the outbreak.
5. **Cyclone Xavier batters the Cook Islands** — the storm reaches
   Category 5 over the northern group.
6. **Knesset elects Kahana as speaker** — an ally of Gadi Eisenkot takes
   the chair.
7. **Settler mob kills a woman, 72, near Jericho** — Britain sanctions
   settler groups in response.
8. **US, Mexico and Bolivia lose measles-free status** — PAHO strips
   the elimination status of all three.
9. **Nvidia posts record $115bn quarterly revenue** — and will not
   reinstate Huang, Congress is told.
10. **Pope Leo ends his South America tour in Peru** — defending the
    Amazon and Indigenous peoples.
11. **146,000 march in France** — public-sector pay protests across the
    country; unions claim far more.
12. **Estonia shuts its border with Russia** — every crossing to close
    from 1 December.
13. **Mongolia's president resigns** — Khurelsukh quits; parliament must
    accept the resignation.
14. **Deadly hailstorms sweep central Argentina** — severe storms batter
    the pampas.
15. **Vulcan failure costs 40 Amazon satellites** — ULA confirms the
    first stage underperformed.

Plus 25 more in the index (16-40): Houthis close in on Aden; US tightens
AI chip rules for China; FAA halts air-traffic router roll-out; Japan
jets scramble near Russian planes; Iraq army clashes with Kataib
Hezbollah; West urges Israel to open Gaza crossings; Depardieu found
guilty in Paris; Epstein expert floats murder claim; Russian plane crash
kills 19 in Siberia; Haiti backs Bukele troop offer; drone overflies
Chisinau; Pentagon fails audit for ninth year; NSA network crash blamed
on vendor; Moscow claims 1,400 drones downed; France ran covert op in
Ukraine; Trump "looking into" Iran dirty-bomb talk; COP31 draft sparks
fossil-fuel fight; Intel shareholders sue after 29% fall; China expands
tariff relief for Canada; five EU states plan Rwanda migrant hub; two
mass shootings kill 17 in South Africa; Nepal first for loss-and-damage
funds; EU clears UniCredit bid for Commerzbank; Burnham floats closer UK
ties to EU.

Every story was cross-checked in at least two independent roundups of
17 November 2026 before it earned its number.

## How it was built

Fifteen text-free flat editorial illustrations were generated (cream,
tan, ochre, deep red and slate, halftone texture), then composed into a
1024x1024 front page with PIL from the assets in `assets/`: every word on
the page was rendered programmatically (bundled DejaVu fonts), the flag
chips and number badges are drawn by code, and the world map is a
public-domain outline with code-drawn pins. The build is deterministic:
two runs of `main.py` produce byte-identical output, equal to the bundled
`entry.png`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
