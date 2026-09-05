---
name: keep-organised
description: Keep the SIH26085 repository tidy and predictable — enforce the agreed folder layout, naming, and the rule that every artefact has one home. Use at the end of every work session, whenever a new kind of file is about to be created, whenever files are being written to the repository root, and when Bitty says "tidy up", "where does this go", or "this is getting messy".
---

# Keep It Organised (SIH26085)

Six people, two weeks, and a build that will be handed between sessions. Anything
that lives in a place nobody expects is effectively lost. One home per artefact,
and the layout below is the agreement.

## The layout

```
sih-work/                   <- the project root
  README.md                 how to install and run, for a teammate
  PROJECT_BRIEF.md          settled facts — rarely changes
  STATUS.md                 current state, rewritten every session
  CLAUDE_CODE_KICKOFF.md    the original brief given to Claude Code
  .env                      secrets — NEVER committed
  .gitignore
  data/
    raw/                    downloaded exactly as received, never edited
    interim/                clipped, reprojected, cleaned — reproducible
    processed/              model-ready inputs
    ground_truth/           the 2015 Chennai flood points and depths
  src/
    drainage/               KML to graph to SWMM model
    rainfall/               nowcast pipeline
    surface/                terrain and runoff
    routing/                flood-aware routing
    api/                    FastAPI service
  web/                      the MapLibre dashboard
  notebooks/                exploration only — never the source of truth
  outputs/
    figures/                charts and maps, dated
    runs/                   model run outputs, one folder per run
  tests/                    mirrors src/
  scripts/                  one-job utilities, including post_update.py
  research/                 vetted repos and data notes, dated
  handoffs/                 end-of-session documents, dated
  deck/                     presentation drafts and exported PDFs
  docs/                     reference documents (the red-team review)
```

## The rules

1. **Nothing new in the repository root** except the files listed above. If
   something has no home, propose one before writing it.
2. **Raw data is immutable.** Anything downloaded lands in `data/raw/` and is
   never edited in place. Every derived file must be reproducible by a script in
   `src/` or `scripts/` — if it cannot be regenerated, it is not trustworthy.
3. **Dates in filenames** for anything that will have a successor:
   `handoffs/SIH26085_HANDOFF_2026-09-08.md`, `outputs/figures/2026-09-08_nowcast_skill.png`.
   No `final`, no `final_v2`, no `new`.
4. **Tests mirror source.** `src/drainage/graph.py` is tested by
   `tests/drainage/test_graph.py`. A module with no matching test file is not done.
5. **One README per top-level code folder** if what it does is not obvious from
   the name — three lines is enough.
6. **Large data is git-ignored,** and the script that fetches it is committed
   instead. Never commit a 27 MB KML.
7. **Secrets never touch a tracked file.** Webhook URLs and API keys live in
   `.env` — that exact name, no prefix — which is git-ignored from the first
   commit. `.env.example` is committed with empty values as the template. The
   `.gitignore` uses both `.env` and `*.env` so a differently-named secrets file
   cannot slip through.
8. **`STATUS.md` is updated in the same session as the work,** not later. If the
   repository and `STATUS.md` disagree, that is a bug to fix immediately.

## At the end of every session

Run a quick tidy pass: list anything sitting in the root or in the wrong folder,
move it, note the move in `STATUS.md`, and confirm `.env` is still ignored
(`git check-ignore -v .env`). Report what you moved in one line — never move
files silently.
