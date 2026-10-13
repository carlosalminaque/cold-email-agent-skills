---
name: fewer-round-trips
description: "Use when coordinating work across agents or sessions (a builder, a reviewer, a releaser) and whenever a human says \"no back and forth\", \"why didn't you just\", or \"prompt\" after a reply that should already have contained one. Every reply to a report ends with the next prompt ready, prompts cover everything left rather than the last finding, the executor tests its own work, and the agent never becomes the courier between two other agents."
---

# No back and forth

Needs: none

For a solo operator, every round trip costs two pastes, a wait and a context switch, and produces nothing they didn't already have. Most round trips come from a handful of habits in how prompts are written. This skill names them and replaces each one.

## Rules

1. **Every reply to a report ends with the next prompt ready.** Never "when it finishes I'll draft the next step." The only reasons not to include it: the next step is gated on a decision that is really the human's (then give the recommendation and the prompt for it), or there is no next step.

2. **A failure the agent finds itself is a report too.** If you find a failed release in a log, the same reply carries the diagnosis and the fix prompt. "I haven't diagnosed it yet" is not a reason to defer: read the script that failed and the file it checked first.

3. **Paste now is the default.** Before telling the human to hold a prompt until another run ends, work out when that run can end and which steps actually depend on it. Put holds inside the prompt on those steps only ("hold step 5 until after 09:40"), and put the urgent step first.

4. **Write from what is left, not from the last report.** Before drafting, read the open-items list and the plan the work belongs to. The prompt covers every item this executor can do, in order. A prompt scoped to "the findings I just read" spawns the next prompt.

5. **One prompt per executor per pass.** If the same executor needs a second prompt within half a day, the first was scoped too small. Say so and fold everything left into one.

6. **Check the mechanism before ordering a switch.** Before a prompt says "flip", "release" or "enable", confirm the script has that step, the caller reads that flag, and the secret it needs exists. If you can't check, the check is step one of the prompt and building what is missing is the fallback.

7. **The executor attacks its own check.** When a prompt asks for a guard or filter, it tells the executor to test it with fresh cases in rounds until a full fresh batch passes clean, and to report the misses per round. Your own test afterwards is a spot check. If it finds a miss, change the method, don't send the misses back as a list.

8. **Mechanical review lives in a script.** Every check a reviewer would make by hand goes into a ready-check the executor must pass before it may say READY. Enforce it in the loop, not in the prompt.

9. **The builder and the releaser close their own loop.** The builder reads the releaser's result file, diagnoses failures, rebuilds and writes the next run sheet, for a set number of rounds. The releaser has one fixed prompt. You are not the courier between them.

10. **Decisions travel as files.** When the human answers a gated question, write their words and the time into a decision file the executor reads. A yes never costs them a paste.

11. **Don't re-ask what the record answers.** Before asking for a decision, search memory and past decision files for the human's own words. If they decide it, apply them and quote them.

12. **Count the pastes.** Before sending, count how many pastes the plan needs from the human until the outcome, and say the number.

## When it happens anyway: diagnose, don't apologize

Name which habit caused the round trip and quote the offending line from your last output. If a rule against it already existed and was broken, say so: a rule that didn't hold needs a different mechanism, not a repeat.

## Valid and Invalid

- Valid: "Two pastes from here to release: one for the builder (everything left on the plan, with a hold at 08:00), one fixed release prompt. The builder reruns failed parts itself."
- Invalid: "When the report ends, I'll turn that into the next prompt."
- Valid: "Attack your own filter with fresh batches of 20 until a batch of 30 has no miss, at most 5 rounds. Write READY only when ready-check exits 0."
- Invalid: "I found these eleven sentences get past the filter, add them."

## Before and after

- Before: seven prompts in eighty minutes, each correct for the report just read, making the human the courier between two agents.
- After: one prompt per executor, written from the open-items list, with the release rule inside it. Failures loop between builder and releaser without the human.
