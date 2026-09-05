# Data

`raw/` and `ground_truth/` are **immutable**. Download them with
`python scripts/fetch_data.py --download` and never edit them in place. Anything
derived from them belongs in `interim/` (clipped, reprojected, cleaned) or
`processed/` (model-ready), and must be reproducible by a script in `src/`.

| Folder | Contents | Source |
|---|---|---|
| `raw/swd/` | Greater Chennai Corporation stormwater drain maps — citywide KML of drain alignments plus per-ward PDFs. Real geometry; **no pipe diameters, invert levels or slopes**, so those are estimated downstream and must stay flagged as estimated. | OpenCity, GCC, public domain |
| `raw/wards/` | GCC ward and zone boundaries (KML). Used to clip everything to one ward. | OpenCity, GCC, public domain |
| `ground_truth/` | Chennai flooding data — 2015 flood points, inundation points with depth **in inches**, and flood hazard zones for 5/10/25/50/100/200-year return periods. This is what the model is scored against. | OpenCity, GCC, public domain |
| `raw/dem/` | CartoDEM 30 m (NRSC) or SRTM 30 m for the ward. 10 m CartoDEM is chargeable and clearance-gated — we do not use it and do not claim its resolution. | NRSC / USGS |
| `raw/rainfall/` | GPM IMERG near-real-time grids (NASA Earthdata login required, free). IMD station rainfall via the public API where useful. | NASA / IMD |

Nothing in here is committed to git — `.gitignore` excludes it. The fetch script is
committed instead, so anyone can reproduce the folder from scratch.

**Units, written down once:** rainfall in millimetres, model depths in metres,
the ground-truth inundation depths in **inches**. Convert at the edge, and name the
unit in every variable that carries one.
