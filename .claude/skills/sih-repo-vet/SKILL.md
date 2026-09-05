---
name: sih-repo-vet
description: Deep-review GitHub repositories, libraries or datasets someone proposes for the SIH26085 flood nowcasting project, against this project's fixed constraints, and record the verdict. Use whenever Bitty or a teammate shares repo links and asks "can we use this?", "review these", "is this useful?", or pastes a list of tools — even without the word review.
---

# Repo Vetting (SIH26085)

The project has already been burned once by a repository recommended on the
strength of its name. Never judge from the README alone, and never from memory.

## Step 1 — Verify live, never from memory

Open the actual GitHub page for every repository. Record the exact owner/repo,
licence, stars, last commit year, whether it is pip-installable, and how heavy the
dependency chain is. Then look at the file tree and read the code that does the
thing being claimed. If you cannot load the page, say so — do not report it as
verified. If sources disagree, say so.

## Step 2 — Judge against this project's fixed constraints

Argue every verdict against these explicitly:

- **Free and open data only.** Nothing paid, nothing behind a ticketed portal, no
  trial keys. If it needs a purchase, it is out even as an "optional extra".
- **Runs on a student Windows laptop.** No CUDA, no compiled Fortran or C++ build
  steps, no multi-service Docker stack. If installing it is a project, it is out.
- **Licence must permit reuse and be stated.** No licence means no permission.
  Flag GPL/AGPL so a deliberate decision gets made rather than an accidental one.
- **The banned list in `PROJECT_BRIEF.md` is binding** — GNN drainage surrogates
  on stale TensorFlow, deep-learning nowcasters without usable weights, ANUGA and
  BG_Flood, OSRM, and FloodSense. If a new candidate is one of these wearing a
  different name, say so.
- **The clock.** Idea deadline 20 September 2026; the finale build is 36 hours. A
  tool needing a week of integration is future scope, not a dependency.
- **The maintainer is a beginner coder.** Infrastructure he cannot keep running is
  a cost, not a feature.
- **It must survive a judge's question.** If we cannot explain what it does at a
  whiteboard, we do not ship it.

## Step 3 — Write it down

Save to `research/vetted_<YYYY-MM-DD>_<short-topic>.md`, one block per repo:

```markdown
## <owner>/<repo>
Stars, licence, last activity — verified live on <date>. One line: what it is.

Plain language: what would this actually do for us, and what does it overlap
with that we already have or already planned?

**Verdict:** Adopt | Install and test first | Inspiration only | Reference only |
Skip — with the one-sentence reason.
```

End with a bottom line if there are three or more. Tier large batches into adopt,
maybe, and ruled-out-after-checking — "ruled out" is different from "not looked at"
and the difference must be visible.

## Step 4 — Route the outcome

Real actions ("install pysteps", "test the KML parser") go into `STATUS.md`, not
only into the research file — an action item that lives only in a research file is
lost. Tell Bitty the verdicts in one or two plain sentences per repo; he should not
have to open the file to know what you concluded. Check `research/` first: if a
repo was already vetted, say so and record that you checked.
