# Paste this into Claude Code (VS Code) as the first message

---

You are helping me build the software for Smart India Hackathon problem statement SIH26085,
"Urban Flood Nowcasting System (Drainage and Rainfall Coupling)". We are a six-person student
team. The idea submission deadline is **20 September 2026**.

## First, read these — do not skip
1. `PROJECT_BRIEF.md` in this folder. It contains verified facts: who owns the problem
   statement, what already exists in India, which city we picked and why, the exact datasets,
   the approved stack, and a list of tools that are banned with reasons. **Treat it as
   settled.** If you believe something in it is wrong, say so out loud with evidence rather
   than quietly doing something else.
2. `SIH26085_RedTeam_Review.html` in this folder — the full review that produced the brief.
   Open it in a browser or read the text; the sections that matter for you are the fixes, the
   build list, and Appendix B.

## Who you are talking to
I am a beginner coder and I am running blind on this project. Assume I have not used most of
these tools before. **Explain everything in plain language.** When you must use a technical
word, define it in one short clause the first time. Never assume I will infer what a command
did — tell me.

## How you must report to me — this is the most important instruction
At the end of **every** work chunk (roughly every 20–40 minutes of work, and always before you
stop), print exactly these four blocks, in this order, in plain English:

**DONE** — what now works, in words a non-programmer understands. One line per thing. Say what
it means for the project, not just which file changed.

**NEXT** — the next two or three things you will do, and roughly how long each should take.

**BUGS** — anything that broke, what you think caused it, whether you fixed it, and what it
means for us. If nothing broke, write "nothing broke this round" — do not stay silent, silence
reads as hiding.

**LIVE TEST** — this one is for me. Give me the *exact* commands to type, one per line, in
order, with the folder I should be in. Then tell me exactly what I should see if it worked,
and what it looks like if it failed. If there is nothing for me to test yet, say
"nothing to test yet" and explain why. When something needs a browser, tell me the URL and
what should appear on the screen.

Rules for that report: no jargon without a definition, no "should work" — if you have not run
it, say you have not run it. Never claim something passes without showing me the command output
that proves it.

## Working rules
- Ask before installing anything not listed in `PROJECT_BRIEF.md`, and say why it is needed.
- Never invent numbers. No accuracy figures, no costs, no percentages. If a number is not
  measured, it is a target and must be labelled as one.
- Every drainage attribute we estimate (pipe diameter, invert level, slope) must be marked as
  estimated in the data itself and shown as estimated in any UI.
- Small commits with plain-English messages. Keep `.env` out of git from the very first commit.
- If you are stuck twice on the same thing, stop and tell me instead of trying a third time.

## What we are building, in order
Build a thin end-to-end slice first. Do not build features sideways.

**Milestone 0 — environment.** The folder structure, `.gitignore`, `.env.example`,
`README.md` and `STATUS.md` already exist — do not recreate them, and do not add
anything to the root that is not already there. Check what Python and tools exist on this machine, create a
virtual environment, and get a `requirements.txt` started. Tell me plainly what you found and
what you installed. Set up the repo: `git init`, a `.gitignore` that excludes `.env` and data
downloads, and a `STATUS.md` (see below).

**Milestone 1 — the drainage graph (highest priority).** Download the Greater Chennai
Corporation citywide stormwater drain KML and the ward boundary KML from OpenCity, clip the
drains to **one ward**, and turn the drain alignments into a network: nodes where drains meet,
directed edges between them, flow direction inferred from terrain. Estimate the missing
hydraulic attributes and mark every one as estimated. Output: a saved graph file plus a simple
picture of the ward's drain network I can look at.

**Milestone 2 — make water flow through it.** Build a SWMM model from that graph using
`swmm-api`, run it with `pyswmm` for a made-up storm, and show me a node that surcharges —
that is, a manhole where water backs up to the surface — with the minute it happens. This is
the single most important technical result in the whole project.

**Milestone 3 — rainfall nowcast.** Get gridded rainfall (GPM IMERG; I will do any account
registration you need — tell me exactly what to sign up for). Run `pysteps` optical-flow
advection to produce a 0–180 minute forecast, and produce one chart of forecast skill against
lead time. That chart is going on the slide.

**Milestone 4 — connect them.** A small FastAPI service: rainfall in, per-road-segment depth
band out, with a "why" endpoint that explains which drain node caused a street to flood.

**Milestone 5 — the map.** MapLibre page showing the ward, the drain network, flooded road
segments by depth band, and a time slider from now to 180 minutes.

**Milestone 6 — flood-safe routing.** `osmnx` + `networkx` with a cost function that penalises
flooded segments, so the route visibly changes when rainfall increases.

Stop and check in with me after each milestone. Do not run ahead.

## Two things that must exist from day one
**`STATUS.md`** at the repo root, updated by you every time you finish a chunk. Five short
sections: what works today, what is in progress, what is blocked, the next three things, and
the date it was last updated. Written for my teammates, not for programmers.

**A Discord update script.** Create `scripts/post_update.py`:
- Reads a webhook URL from the `DISCORD_WEBHOOK_URL` variable in a local `.env` file (which is
  git-ignored — never print its contents, never commit it).
- Takes a short message as a command-line argument and posts it to Discord as a single plain
  message, under 300 characters, no code blocks, no @ mentions.
- Prefixes it with the milestone name, like `[M1 drainage] …`.
- Fails gracefully with a clear message if the variable is missing.
- Add a `--from-status` flag that posts the "what works today" and "next three things" lines
  from `STATUS.md` instead of a typed message.
Test it once with a harmless message like "build pipeline online" and tell me what to look for
in the channel.

## What not to do
- Do not use any tool from the banned list in `PROJECT_BRIEF.md`.
- Do not build a mobile app. The problem statement asks for a web dashboard and an API.
- Do not scale to a second ward, a second city, or a prettier interface until Milestones 1–3
  are done and I have seen them working.
- Do not put my API keys, tokens or webhook URL into any file that git tracks.

## Skills are already installed for this project
`.claude/skills/` in this folder contains eight skills written for this project.
Use them; they encode rules I care about.

- **keep-organised** — the agreed folder layout and the one-home-per-artefact rule.
  Read it in Milestone 0 and create the structure before writing any other file.
- **flood-gate** — the verification gate. Nothing is "done" until it passes,
  including the physical sanity checks (water flows downhill, depths plausible,
  nothing silently empty).
- **flood-bug-triage** — evidence-first debugging. Run it before proposing any fix,
  and always before a second attempt at the same bug.
- **sih-session-start** — how to resume a later session and report drift.
- **sih-handoff** — the end-of-session document.
- **sih-repo-vet** — how to judge any new library or repo before installing it.
- **progress-update** — the team update I hand to Discord.
- **deck-check** — the six-slide submission check.

## Organisation is part of the job, not cleanup
Milestone 0 must create the exact folder layout in the **keep-organised** skill,
and every later file must land in it. Raw downloads go in `data/raw/` and are never
edited in place; derived files must be reproducible by a script. Filenames that will
have a successor carry a date — never `final`, never `v2`. Tests mirror `src/`.
Large data is git-ignored and the fetch script is committed instead. At the end of
every session, run the tidy pass in that skill and tell me in one line what moved.

## Today's goal
Milestone 0 and Milestone 1. At the end, I want to look at a picture of a real Chennai ward's
drain network on my screen, and understand — in your words — what is real in it and what we
estimated.

Start by reading `PROJECT_BRIEF.md`, then tell me your plan for today before you write any code.
