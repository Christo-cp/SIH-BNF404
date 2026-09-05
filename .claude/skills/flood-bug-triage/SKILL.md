---
name: flood-bug-triage
description: Evidence-first debugging protocol for the SIH26085 flood nowcasting project. Use whenever a script breaks, a map comes out empty, a model produces impossible numbers, a test fails unexpectedly, or Bitty says "it's not working", "the map is blank", "the numbers look wrong" — BEFORE proposing any fix. Also use before attempting a second fix for the same bug.
---

# Bug Triage (SIH26085)

Geospatial and hydraulic bugs almost never announce themselves. The code runs, a
file is written, a map renders — and it is wrong. Never guess. Gather evidence
first, and never attempt a third blind fix.

## Protocol

**1. Capture the exact symptom.** What command was run, what appeared, what should
have appeared. If it happened on Bitty's machine, get the verbatim error line and
the last thing printed before it.

**2. Check the known shapes first.** In this project, in rough order of frequency:

- **Coordinate system mismatch.** The single most common GIS bug. Drain KML is in
  degrees (EPSG:4326); anything measuring length, area or slope must be in metres
  (a projected CRS such as EPSG:32644 for Chennai). Symptoms: distances of 0.0003,
  a clip that returns nothing, layers not overlapping. Always print the CRS of
  every layer before blaming the logic.
- **Silently empty result.** A clip, join or filter returned zero rows and the
  code carried on. Print row counts after every one of those operations.
- **Unit confusion.** Rainfall in mm, depths in metres, the Chennai ground truth
  in **inches**. Convert once, at the edge, and name the unit in the variable.
- **A model that runs but nothing floods.** Usually the rainfall never reached the
  network: no subcatchment attached to the node, an empty rain time series, or a
  timestep so long the peak is averaged away. Check inflow at the node first, not
  the hydraulics.
- **A model where everything floods.** Usually pipe capacity is wrong by orders of
  magnitude — an estimated diameter in millimetres treated as metres, or a slope
  of zero.
- **Time confusion.** Satellite and IMD timestamps are UTC; the demo is in IST.
  An apparently five-and-a-half-hour lag is this, not the model.
- **NaN spreading.** One missing elevation turns a whole column into NaN and the
  map goes blank. Count NaNs after every merge.
- **It worked yesterday.** Suspect a re-download that changed, a cached file, or a
  different ward extent — not the code.

**3. Gather evidence before hypothesising.** Print the shapes, the CRSs, the row
counts, the min/max of the suspect column, and the first three rows. Attach that
output to the diagnosis. Never reason from what the data "should" contain.

**4. Isolate and confirm.** Find the one line, value or file that flips with the
hypothesis. Only then propose the fix, stated as cause → fix → the test that
proves it.

**5. Fix, then add the regression test.** Every diagnosed bug gets a test that
would have caught it. Then the flood-gate skill applies.

**6. Two-strike rule.** Two failed fixes on the same bug means the diagnosis is
wrong. Stop, restart this protocol from step 1 as if the bug were new, and say so
plainly instead of sounding confident.

## Honesty rules

- Say "confirmed cause" or "most likely candidate" — never blur them.
- If the evidence needed does not exist yet, say exactly what Bitty must run and
  what its output will settle. Do not fix ahead of the evidence.
- Explain the bug in plain language: what broke, why it happened, what it means
  for the project. Bitty is a beginner coder and is running this blind.
