# STATUS — SIH26085 Urban Flood Nowcasting

_Last updated: 2026-09-05 · Idea submission deadline: 20 September 2026 (15 days)_

## What works today
- Project scaffold is in place: folder structure, `.gitignore`, `.env` / `.env.example`,
  `README.md`, and eight project skills under `.claude/skills/`.
- `scripts/fetch_data.py` is written and parses. It resolves the three Chennai
  datasets through the OpenCity CKAN API and saves them into `data/`.
  **Not yet run** — see Blocked.
- `data/README.md` records what each dataset is, what it lacks, and the unit
  convention (rainfall mm, model depth m, ground-truth depth **inches**).

## In progress
- Nothing. Milestone 0 (Python environment, dependencies, first commit) is next,
  then Milestone 1 (the ward drain network).

## Blocked
- **Discord webhook URL** — waiting on the server owner. Paste it into `.env` as
  `DISCORD_WEBHOOK_URL=` when it arrives. Nothing else depends on it.
- **Data download must run on Christo's machine.** Both the cloud sandbox and the
  device shell are behind an egress proxy that refuses `data.opencity.in` (HTTP 403
  on CONNECT). The script is correct; it just needs a normal internet connection.
  First real command of Milestone 1:
  `python scripts/fetch_data.py` then `python scripts/fetch_data.py --download`.

## Next three things
1. **Milestone 0** — create the virtual environment, install dependencies, `git init`,
   confirm `git check-ignore -v .env` before the first commit.
2. **Milestone 1** — download the data, clip the drains to one ward, build the
   node/edge network, produce a picture of it.
3. **Milestone 2** — build a SWMM model from that network and make a manhole
   surcharge for a known storm.

## Decisions made (do not relitigate)
- Pilot city is **Chennai**, because it has open drain geometry *and* open flood
  ground truth. Mumbai has neither in machine-readable form.
- We never claim "no such system exists in India" — MoES already runs iFLOWS-Mumbai
  and CFLOWS-Chennai, and IIT Delhi runs Barapullah. Our gap is 0–3 h at road-segment
  scale from open data.
- No invented numbers anywhere. Unmeasured performance is a target and says so.

## Notes
Read `PROJECT_BRIEF.md` before changing anything. File placement rules are in
`.claude/skills/keep-organised/SKILL.md`. The full reasoning is in
`docs/SIH26085_RedTeam_Review.html`.
