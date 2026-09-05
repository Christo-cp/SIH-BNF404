---
name: progress-update
description: Produce a progress report for the SIH26085 project — a short team-facing update ready to post in Discord, and a franker private version for Bitty. Use whenever Bitty says "progress report", "what's the status", "update for the team", "what do I tell them", or before a team meeting.
---

# Progress Report (SIH26085)

Bitty is the only person with the full picture, and that is the problem this
solves. Produce two versions every time. Never post anything yourself — hand him
the text and let him send it.

## Gather the facts first, from the repo, not from memory

- `STATUS.md` — the claimed state.
- `git log --oneline --since="7 days ago"` — what actually changed.
- `python -m pytest tests/ -q --tb=no` — the real test count.
- The newest file in `handoffs/`, if any.
- Days remaining until 20 September 2026.

If the repository contradicts `STATUS.md`, the repository wins, and say so.

## Version 1 — for the team (Discord)

Under about 120 words. Plain language, no library names unless a teammate has to
act on one. Four short lines:

- **Working now:** what someone could open or run today.
- **Being built:** the one or two things in flight.
- **Blocked / need help:** name the person if a specific teammate is needed.
- **Next check-in:** when the next update lands.

No jargon, no percentages of completion, no invented numbers. Say
"drain network for one ward is built from the real GCC map", not "M1 complete".

## Version 2 — for Bitty only

Blunter, and it must include what the team version leaves out:

- What has slipped and by how long.
- What is at risk of not making 20 September, and what would have to be dropped.
- Anything currently held together with an assumption or an estimated value.
- Which teammate is blocked or has gone quiet, if the commit history shows it.
- One recommendation for the single most useful thing to do next.

## Then

Offer the Discord command rather than running it:
`python scripts/post_update.py "<the team version>"`
Ask before sending. Never post without an explicit yes.
