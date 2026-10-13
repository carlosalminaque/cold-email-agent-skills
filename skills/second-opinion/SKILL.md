---
name: second-opinion
description: "Use right before a plan, spec or build handoff prompt is marked final, to get an independent, adversarial critique from a clean context rather than a self-review by the session that wrote it. Use before implementing a nontrivial spec, before handing a build prompt to another agent, or whenever the person asks for a second opinion, a gut check, or did we miss anything before we lock this. Runs on a plan before code exists; it is not a code review of a finished diff. Skip it for small, low-stakes changes."
---

# Second opinion

Needs: none

A session that wrote a plan cannot fully review it: whatever assumptions produced the plan are still in its context when it reads it back. This skill runs the critique from a clean context instead.

## When to run it

- A plan, spec or handoff prompt is about to be marked final and passed to implementation.
- The person asks for a second opinion, a gut check, or "did we miss anything".
- Skip it for small, low-stakes changes like a copy tweak or a single field rename.

A self-review step inside your own planning process is still useful, but it shares the plan's blind spots. For anything high-stakes, run this in addition, not instead.

## Steps

1. **Get a clean read.** Start a reviewer (a subagent or a fresh session) with no exposure to the conversation or research that produced the plan. Give it only: the plan itself, the stated goal, and any hard constraints already decided (access limits, must-nots, budget, scope). Do not give it the back-and-forth. If it can see the reasoning, it inherits the blind spots.
   Valid: Reviewer gets the spec, the goal in two lines, and the three hard limits. Invalid: Reviewer gets the full chat history "for context".

2. **Ask it to find weaknesses, not to praise.** Require this report structure:
   - **SHOWSTOPPERS.** Something that will not work as written, a real security or data problem, or a contradiction with a hard constraint.
   - **GAPS.** Edge cases not handled; decisions that read as settled but are not pinned down.
   - **INCONSISTENCIES.** Contradictions or shifting terms between sections.
   - **UNDERSPECIFIED.** Anything vague enough that two builders would build it two ways.
   - **SUGGESTIONS.** Simpler approaches worth considering. Lowest priority; must not crowd out real findings.
   - **STRENGTHS.** Briefly, what is solid, so the plan is not rewritten over a few gaps.

   Require specifics: each finding names the exact section and says concretely what breaks or stays ambiguous.
   Valid: "Section 4 doesn't say what happens to a draft in progress if its category changes mid-edit." Invalid: "This might cause issues."

3. **For high-stakes plans, run two reviewers in parallel.** Anything touching money, an irreversible action, or several systems at once. Note where they agree and where they differ; agreement between independent reviews is a stronger signal than either alone.
   Valid: "Both reviewers flagged the missing retry limit; only one flagged naming." Invalid: Merging both lists without saying which findings overlap.

4. **Synthesize before presenting.** Separate must-fix gaps from minor suggestions. If a finding is already covered elsewhere in the plan (a false positive from the reviewer's missing context), say so and drop it.
   Valid: "Reviewer flagged missing auth; it's covered in section 2, dropped." Invalid: Passing all 14 raw findings along unfiltered.

5. **Present the findings, then ask** which real gaps need the person's decision and which are obvious fixes. Do not silently patch the plan and re-ship it without showing what changed.
   Valid: "Three real gaps: two I can fix as obvious, one needs your call on whether failed sends retry. Changes shown below." Invalid: "Reviewed and updated the plan; it's ready."

## After it runs

Once every flagged gap is fixed or explicitly waived, the plan ships. This skill is a checkpoint between "the plan looks done" and "the plan actually ships"; it does not replace the plan's own review steps.
