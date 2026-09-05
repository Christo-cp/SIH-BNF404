---
name: flood-gate
description: Run the mandatory verification gate for the SIH26085 flood nowcasting project before calling anything done. Use EVERY time a module, script or fix is built — and whenever Bitty says "verify it", "run the gate", "is it done?", "ready to test?", or asks to move to the next milestone. This gate is a hard project rule, not optional.
---

# Verification Gate (SIH26085)

Hard rule: nothing is "done" until all four steps below have literally happened,
in order. This project's failure mode is not a crash — it is a pipeline that runs
cleanly and produces numbers that are quietly meaningless. A green test suite
proves the code did what you told it to; it does not prove the water is going
anywhere real.

## The four steps — in order, no skipping

**1. Tests written and shown.** Every module gets tests, and they must assert
behaviour, not existence. For this project that means at minimum: geometry lands
in the expected coordinate system, a clip returns a non-empty result, units are
what the function claims, and a storm that should flood a node actually floods it.

**2. Tests run, all passing, output shown.** Run the whole suite, not just the new
file, and paste the real output:
```
python -m pytest tests/ -q
```
Name any pre-existing failure as pre-existing. New failures block the gate.

**3. The physical sanity check — this is the step that matters here.** Before
claiming a result, prove it is not nonsense:
- Water flows downhill. Show that outfalls sit at or near the lowest elevations.
- Depths are plausible. A street reading 2 metres deep from 40 mm of rain is a
  bug, not a finding. State the rainfall and the resulting depth together.
- Rain volume roughly balances. Rainfall on the catchment should be in the same
  order of magnitude as runoff plus storage plus outflow.
- Nothing is silently empty. Report row counts after every clip, join and merge.
- Every estimated attribute is still flagged as estimated in the output.
If any of these cannot be checked yet, say so plainly rather than skipping it.

**4. Live test with Bitty, then explicit sign-off.** Give exact commands to type,
the folder to be in, what he should see on screen if it worked, and what failure
looks like. Wait for his report. Then ask, in spirit:
> "Are you happy with <module / Milestone N>? Shall I move to <next>?"
Only an explicit yes opens the gate. Silence, "probably fine", or your own
confidence do not.

## Honesty checks that are part of the gate

- No invented numbers anywhere — no accuracy, no cost, no probability. An
  unmeasured number is a target and must be labelled as one.
- Demo mode says demo mode. Replayed rainfall says replayed.
- If a result depends on an estimated pipe diameter, the sentence reporting it
  says so.

## If anything fails

Fix it before asking for sign-off, never ask early. Two failed fixes on the same
bug means the diagnosis is wrong — stop and use the flood-bug-triage skill rather
than guessing a third time.
