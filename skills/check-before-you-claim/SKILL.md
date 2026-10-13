---
name: check-before-you-claim
description: "Use before stating anything as fact that a source exists to settle - how an API or library behaves, what a governing rule file says, whether a change is live, what a system did. Read the actual current source, try a second path when the first is inconclusive, and label anything still unchecked as unchecked. Covers API folklore, stale memory of internal rules, guesses reported as findings, and \"done\" claimed from a written intention."
---

# Verify before claiming

Needs: none

An agent's confidence is not evidence. Four versions of the same failure show up again and again:

1. **API folklore.** Code written from memory of how an API "usually" works, against a version where a parameter was renamed or a default changed.
2. **Stale internal rules.** A judgment made from what a rule file "probably says", without opening it. Provisional criteria get applied as settled ones, and caveats get dropped.
3. **A guess reported as a finding.** "That's probably an auth error" goes into a report as fact. The real cause was an argument-parsing failure.
4. **Done because it was written down.** A plan or note says "from now on X", so the agent reports X as in effect. The file that would need to change was never touched.

## The test

If a source exists whose job is to settle this exact question (the official docs for the installed version, a live read of the system, the governing rule file), check it before stating the answer. Especially when the answer feels obvious.

Skip it for trivial, self-contained edits where nothing version-sensitive or rule-governed is at stake.

## What to check, in order

External:

1. Local and live evidence: the lockfile's installed version, existing usage in the codebase, an actual call against the resource.
2. Official documentation for that exact version. A specific instance's own spec or admin docs beat generic public docs when they disagree.
3. Community material only as a supplement.

Internal:

1. The governing file itself, read in full, including dated corrections (they override earlier passages).
2. The documents it cites for its reasoning.
3. The confidence level travels with the rule. If the source says "provisional", the recommendation built on it says so too.

## The loop

1. A failed check is a branch, not a stop. If the docs don't settle it, run a live test. If the live test is ambiguous, look for a more authoritative source.
2. If more than one path fails to settle it, say exactly that: "I could not confirm X. I checked Y and Z; neither settled it."
3. Don't stop at the first plausible explanation.

## Settings are not results

A configuration says what was asked for. The record of what happened says what happened. When you report a time, a count or a state:

- read it from the log, the sent records, the rows themselves;
- when both the setting and the record can be read, read both and compare. A difference is a fault and goes at the top of the report;
- when only the setting can be read, say "set to", never "runs at" or "is".

## A green status is not a success

A 2xx response, a "completed" execution or a switched-on job is a claim about the mechanism, not the outcome. Read back what the step produced: the row, the cell, the file, the count.

## Valid and Invalid

- Valid: "The schedule field says 11:00 to 17:00, but the send log shows Monday's emails went at 08:02. That is a fault."
- Invalid: "Sending opens at 11:00" read from the settings page.
- Valid: "The insert returned 201. Read back: 84 rows present, last one matches the input."
- Invalid: "The insert returned 201, so all 84 rows landed."
- Valid: "I wrote the new rule into the prompt file and re-read it: line 42 now says X."
- Invalid: "Done, the prompt now does X" because a planning note says it should.

## Before and after

- Before: an agent reported a campaign "sends at 11 AM" for two days, from the schedule field. The emails were going out at 8 AM.
- After: every time reported comes from the sent records, and the setting is compared against them.
