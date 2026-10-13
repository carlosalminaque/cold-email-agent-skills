---
name: what-to-automate-next
description: "Use when the person asks what to automate next, what is worth building, or wants a periodic review of repeated manual work during an active build phase. Also use instead of building a new skill or agent on reflex whenever a gap appears. A deliberately restrained method: find repeated manual work, ask whether the work should exist at all before automating it, choose the lowest autonomy level that solves it with a stated condition for raising it, pick the simplest build that meets the need, and ship exactly one thing tied to one measurable outcome."
---

# What to automate next

Needs: none

The point of this skill is restraint. Its default answers are: stop doing that entirely, lowest autonomy, no AI if a script works, and ship one thing.

Run it when there is real evidence of repeated manual work: after an audit, during an active build phase, or when the person names a recurring annoyance. Not on a schedule for its own sake.

## Phase 1: find the candidate

Ask these and wait for real answers rather than guessing from context:

1. What did you repeat three or more times this week?
2. What felt manual, boring or copy-paste?
3. What could a smart intern handle?
4. What would break if ten times the current volume arrived tomorrow?
5. What would unlock that volume?

Output one to three ranked candidates, each with a one-line reason it is high leverage. Pick exactly one with the person and drop the rest. They are not a backlog; they come back next run if they still matter.

- Valid: "Top pick: the weekly report copy-paste, done 4 times this week, about 40 minutes each."
- Invalid: a list of nine ideas filed as a roadmap

## Phase 2: scope it

**Eliminate first, always.** Before automating anything, ask whether the work should exist at all. A deleted step beats an automated step every time. Only if it truly must happen, continue. Then ask whether it should be automated or handed to another agent or tool.

- Valid: "Nobody reads this weekly report. Stop producing it."
- Invalid: building a scheduled job for a report nobody reads

**Process map.** State all five before building: trigger, data sources, transformations, decision points, destination. If any is unclear, it is not ready to build.

**Autonomy level.** Start at the lowest that solves the problem:

- L0: manual, no AI
- L1: AI suggests, the person decides each step
- L2: AI drafts, the person reviews and edits
- L3: AI runs, the person checks periodically
- L4: fully autonomous

This is a starting point with a direction, not a ceiling. Starting low is about earning confidence, not a preference for supervision. Every level you set comes with the evidence that would justify raising it and roughly when to re-check. A level with no exit condition is a permanent manual process with a temporary label.

- Valid: "L2 for now. Raise to L3 after 30 drafts sent with no edits needed; re-check in two weeks."
- Invalid: "L2." (no exit condition)

Label which kind of gate you are setting:

- A **validation gate** is temporary. It exists because the system is unproven and comes off when testing shows it works.
- A **standing safety gate** is permanent, whatever the track record, because a wrong action cannot be undone: real sends to real people, publishing, spending money, handling credentials.

Mixing them up either strands a working system at manual forever or quietly removes a gate that should never come off.

**Tie it to one measurable outcome:** more qualified leads or sales, higher conversion, or less of the person's time. If it maps to none of these, do not build it.

## Phase 3: build the simplest thing

In increasing complexity. Start at the top and move down only when the simpler option truly cannot do the job:

1. A saved prompt or template the person runs by hand
2. A deterministic script, no AI in the loop
3. A skill with one AI call inside
4. A multi-step agent, last resort and rarely justified

- Valid: a small script that wraps an API call the same way every time. It cannot make things up and is easy to debug.
- Invalid: a "management agent" for the same job, with more moving parts and different results each run

Plan before building anything structural, and summarize what changed after.

## Hard rules

- One run, one artifact. Not "and while we're at it."
- The eliminate question is always asked first and answered honestly.
- Default to the lowest autonomy and the simplest build that works.
- Read-only on everything except the artifact being shipped and the record of what was decided.
- If the honest answer is "nothing here is worth building this round," say so and end the run. That is a successful outcome.
