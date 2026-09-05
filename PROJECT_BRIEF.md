# SIH26085 — Project Brief (locked facts)

Everything here was verified against primary sources on 4–5 September 2026.
Do not contradict this file. If something here turns out wrong, say so explicitly
and cite what you found — do not silently work around it.

## The problem statement
- **SIH26085 — Urban Flood Nowcasting System (Drainage and Rainfall Coupling)**
- Owner: **Ministry of Earth Sciences (MoES)**, department **NCMRWF** (India's numerical weather prediction centre)
- Category: Software · Theme: Disaster Management
- Idea submission deadline on the SIH portal: **20 September 2026**
- Required outputs: 0–3 hour street-level flood forecast, drainage network as a directed
  graph (nodes = manholes/inlets, edges = pipes/canals), hydraulic capacity + surcharge /
  backflow prediction, water depth estimates, a dynamic web GIS dashboard, and an API that
  navigation systems can call for flood-safe routes.

## Who we are pitching to, and the trap
MoES **already operates** two urban flood warning systems: **CFLOWS-Chennai** (NCCR, 2019)
and **iFLOWS-Mumbai** (2020, with MCGM — coupled 1D drainage + 2D hydrodynamic model on a
20 cm DEM with 120 rain gauges, ward-level depth 6–72 hours ahead). NCMRWF contributes
weather models to both. The closest technical prior art is **IIT Delhi's Jalsuraksha /
Barapullah** system — a live web-GIS with junction-level SWMM flooding depth — but it covers
one 376 km² basin in Delhi and the newest data on it is January 2025.

**Never claim "no such system exists in India."** Our position is:
> MoES already warns Mumbai and Chennai at ward scale, 6–72 hours ahead, using bespoke
> survey data that took years and cannot be repeated for every Indian city. We nowcast the
> next three hours at **road-segment** scale, from **open data**, in a ward that can be
> stood up anywhere in a day.

Two rival SIH26085 demos are already public. Both run on synthetic/inferred drainage and
"illustrative" metrics. Our differentiation is **real drain geometry + measured skill on a
real event**. That is the whole game.

## Pilot city: Chennai (settled)
Chennai has open drain geometry and open flood ground truth. Mumbai has neither in
machine-readable form. All datasets below are Greater Chennai Corporation via OpenCity,
public domain.

| Dataset | What it gives us |
|---|---|
| Chennai Stormwater Drain (SWD) Maps | Citywide KML of drain alignments + per-ward PDFs for 114 wards. **Real geometry. No diameters, inverts or slopes** — those must be estimated and labelled as estimated, everywhere, in code and UI. |
| Chennai Flooding Data | 9 KMLs: 2015 flood points, **inundation points with depth in inches**, and 5/10/25/50/100/200-year hazard zones. **This is our validation ground truth.** |
| GCC ward / zone boundaries | Ward KMLs (incl. 2022) to clip everything to one ward. |

Source pages:
- https://data.opencity.in/dataset/chennai-stormwater-drain-swd-maps
- https://data.opencity.in/dataset/chennai-flooding-data
- https://data.opencity.in/dataset/gcc-ward-information

## Rainfall
- **IMD public API** (api.imd.gov.in): district/station nowcast, AWS/ARG station rainfall,
  radar *image* products. The district nowcast is district-scale — **far too coarse to force
  a street-level model**. Use station data for magnitude, never as the forecast field.
- **Raw IMD Doppler radar volumes**: only via the paid, ticketed Data Supply Portal. Not a
  hackathon path.
- **NASA GPM IMERG near-real-time**: free with an Earthdata login, gridded, ~10 km. This is
  our dependable gridded rainfall input.
- Nowcasting method: **optical-flow / Lagrangian advection via pysteps** — the approach
  national met services actually run. No training required.

## Terrain
NRSC CartoDEM 30 m is free; 10 m is chargeable and clearance-gated. **Never claim resolution
gained by interpolating 30 m to 10 m.** We predict per **road segment** and per **drainage
node**, not per pixel, and we output depth *bands* (0–10 / 10–30 / 30–50 / >50 cm) with a
confidence class — never a centimetre point value.

## Approved stack (all licence-checked)
| Job | Tool | Licence |
|---|---|---|
| Drainage hydraulics | `pyswmm` (bundles the EPA SWMM engine) | BSD-2 |
| SWMM model read/write, geometry → network | `swmm-api` (MarkusPic/swmm_api) | MIT |
| Synthesise a network for a second city | `SWMManywhere` (ImperialCollegeLondon) | BSD-3 |
| Rainfall nowcast | `pysteps` | BSD-3 |
| Read Indian radar files (if we ever get them) | `radarx` / `PyScanCf`, `wradlib` | MIT |
| Surface water over terrain | `landlab` OverlandFlow; `pysheds` / `pyflwdir` for a cheap HAND proxy | MIT / GPL-3 |
| Geospatial | `geopandas`, `shapely`, `rasterio`, `pyproj`, `networkx` | permissive |
| Flood-aware routing | `osmnx` + `networkx` (callable edge weights) | MIT |
| API | `FastAPI` + `uvicorn` | MIT |
| Map | MapLibre GL + a deck.gl example layer | BSD/MIT |

## Banned — do not install, do not propose
- `GNN-UDS` and GNN drainage surrogates — pinned to a 2021-era TensorFlow stack. The *idea*
  may appear on a slide as future work; it is not a dependency.
- DGMR / SmaAt-UNet / NowcastNet — no usable weights, trained on non-Indian radar grids.
- ANUGA, BG_Flood — compiled / GPU-only, will eat the schedule.
- **OSRM** — precomputes its routing graph, so edge costs cannot change per request. That is
  exactly what a nowcast needs. Use osmnx + networkx.
- `roohiiiit/FloodSense` — reviewed and rejected. It is a Flutter phone app that thresholds a
  five-day rain total and draws an 80 km circle. Not a baseline, not a reference, not cited.

## Honesty rules that are part of the deliverable
1. No invented numbers, ever — no accuracy percentages, no rupee figures, no probabilities.
2. Every estimated drainage attribute is flagged as estimated, in the data and on screen.
3. Model performance is a **target** until measured on the 2015 Chennai ground truth.
4. Demo mode is labelled as demo mode. Replay is labelled as replay.

## Where the project lives
Project root: `C:\Users\chris\Claude\Projects\SIH\sih-work\`. All code, data, deck and documents live
under this root; nothing new goes in the parent `SIH` folder.

## Repository organisation
The folder layout, naming conventions and the "one home per artefact" rule live in
`.claude/skills/keep-organised/SKILL.md`. That file is the agreement — create the
structure before writing code, and keep to it. Raw data is immutable and lives in
`data/raw/`; every derived file must be reproducible by a script; dated filenames
for anything with a successor; secrets only in a git-ignored `.env`.
