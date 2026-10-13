---
name: handoff-contract
description: "Use when reporting delegated build work or any completed implementation handoff, whether the work was done by a coding agent, a sub-agent, a script or an outside automation. Requires five parts in every report: the goal, done criteria set before building, concrete validation evidence, every touched file and system, and what was not verified. Marks hypotheses as hypotheses."
---

# Handoff contract for delegated build work

Needs: none

Use this for every report on delegated build work: work done by a coding agent, another AI session, a sub-agent, a script or an outside automation.

## The five parts

1. **Goal.** What the task was supposed to achieve, in one line.
2. **Done criteria.** What would prove it worked. Set these before building; do not reconstruct them afterward.
3. **Validation evidence.** The artifact behind each claim: a run ID, an HTTP status and response body, a diff, a re-fetched object, a test result, a screenshot. "I verified it" is not evidence.
4. **Touched files and systems.** Everything actually changed, including incidental changes.
5. **Not verified.** Every untested claim, inference or limit. If evidence was not captured and cannot be recovered, say so instead of reconstructing what probably happened. An explanation of why something must be true stays a hypothesis until tested.

## Evidence discipline

- Capture evidence while doing the work, not only at the end.
- Keep the status code and body of failed and successful API calls that matter.
- Re-fetch the resulting object or live state when the claim is about persistence, publishing, activation or sync.
- Tell source documentation apart from runtime proof.
- Never present a hypothesis as an established cause.

## Example

Valid: "Goal: nightly export writes the lead file. Done: file dated today with 412 rows. Evidence: run 8812 exit 0, file listing, row count 412. Touched: export script, schedule. Not verified: behavior when the source API is down."

Invalid: "All done, I tested it and it works."

Related: [route-blocked-work](../route-blocked-work/SKILL.md) covers blocker reports; this skill covers completion reports.
