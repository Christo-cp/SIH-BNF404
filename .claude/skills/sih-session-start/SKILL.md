---
name: sih-session-start
description: Resume work on the SIH26085 flood nowcasting project at the start of a session — read the brief and status, re-ground against the actual repository, report drift, count days to the deadline, and confirm direction before building anything. Use whenever Bitty says "resume", "continue the flood project", "pick up where we left off", or opens the project without context. Run this BEFORE writing any code.
---

# Session Start (SIH26085)

Documents go stale within days. Read them, then verify them against the code
before trusting a single line. Starting from a stale status file wastes sessions.

## Steps

1. **Read the ground truth, in this order:** `PROJECT_BRIEF.md` (settled facts —
   owner ministry, prior art, chosen city, approved and banned tools, honesty
   rules), then `STATUS.md` (where the build actually stands), then the most
   recent file in `handoffs/` if one exists.

2. **Verify the status against reality.** Do not skip this:
   - Run the suite: `python -m pytest tests/ -q --tb=no` and compare the counts
     with what STATUS.md claims.
   - Confirm the files and functions STATUS.md names actually exist — a few
     greps, not a full audit.
   - Check the data directory: are the downloaded datasets still present, and are
     they the size you would expect?
   - Look for half-finished work the status file does not mention
     (`git status`, `git log --oneline -10`).

3. **Report drift in plain language.** "Status says X, reality says Y" for every
   mismatch, or "status verified, no drift". Include the test count and any known
   failures by name.

4. **State the clock.** Days remaining until the idea submission deadline of
   20 September 2026, and one sentence on whether the deck or the code is the
   binding constraint this week. If the deck is behind, say so — the deck is what
   is scored first.

5. **Confirm direction before building.** Present the next three items from
   STATUS.md and ask which to start. Do not assume the top item is still what
   Bitty wants today.

## Standing rules from minute one

- One module at a time. Tests first. The flood-gate skill applies to everything.
- Two failed fixes on one bug means stop and run flood-bug-triage.
- Never use anything on the banned list in `PROJECT_BRIEF.md`, and never claim
  "no such system exists in India".
- Explain in plain language. Bitty is a beginner coder running this blind.
