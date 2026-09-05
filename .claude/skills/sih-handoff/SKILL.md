---
name: sih-handoff
description: Write the end-of-session handoff document for the SIH26085 flood nowcasting project, so the next session and the rest of the team can cold-start from it. Use whenever Bitty says "write the handoff", "wrap up", "end of session", "save where we are", or when a work session is winding down.
---

# Handoff Writer (SIH26085)

The next session — and four teammates who were not in this one — start from this
document. Audit the real state first; never write state from memory.

## Process

1. **Audit reality before writing anything.**
   - `python -m pytest tests/ -q --tb=no` — record the true counts, name each
     failure and whether it is new or pre-existing.
   - `git log --oneline` since the last handoff, and `git status` for anything
     uncommitted.
   - Confirm the pipeline still runs end to end, or say exactly where it stops.

2. **Write the session delta, in four buckets:**
   - **Working and seen by Bitty** — only things he has live-tested and signed
     off. Tests passing is not sign-off.
   - **Built but not yet live-tested** — and exactly what the next live test must
     show, phrased as something visible on screen.
   - **Open questions** — what is known, what evidence exists, what the next step
     is, and any "do not guess before checking X" warnings.
   - **Backlog** — carry forward every unresolved item from the previous handoff.
     A dropped item is silent data loss; if something was deliberately closed,
     say so rather than deleting it.

3. **List the files touched**, one line each: what changed and why.

4. **Add a plain-language paragraph for the team.** Three or four sentences a
   non-programmer teammate can read in the Discord channel without asking a
   follow-up question.

5. **Save** to `handoffs/SIH26085_HANDOFF_<YYYY-MM-DD>.md`, stating which handoff
   it supersedes. Never delete old handoffs. Update `STATUS.md` in the same pass
   so the two never disagree.

6. **Offer the Discord post.** Suggest running
   `python scripts/post_update.py --from-status`, but do not post anything
   without Bitty saying so.

## Content rules

- Days remaining to 20 September 2026 in the header.
- No invented numbers. Unmeasured performance is a target, labelled as one.
- Keep the tone direct and specific: warn future-you about traps, and admit
  uncertainty out loud rather than sounding finished.
