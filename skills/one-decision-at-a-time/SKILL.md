---
name: one-decision-at-a-time
description: "Use when the person hands over a batch of concerns, review findings, feedback or things to fix about a system and wants to work through them together, with phrases like go through these one by one, ask me as you go, let's fix these, or think this through with me. Runs a structured session: a visible to-do list, one item at a time with a real recommendation and a question, live state checked instead of guessed, and every decision written back to the skills, docs and notes it changes before the session counts as finished."
---

# One decision at a time

The person has a list of concerns about a live system and wants to settle them together, not have the agent silently rewrite everything. The shape: one item at a time, a real recommendation up front, the person's call on the tradeoff, then the changes made and written back to wherever they need to last.

## Why one at a time

Bundling every question into one message is faster to write but worse to answer. The person skims past tradeoffs or answers out of context. Going item by item keeps each recommendation fresh when it is weighed, and earlier decisions can shape how later ones are framed.

- Valid: ask about item 1, get the answer, then ask about item 2
- Invalid: one message with seven questions and seven option lists

## The flow

1. **Make the to-do list first.** One task per concern, in a task list the person can see, before asking anything. It is the tracker and the checkpoint if the session runs long or is interrupted.

2. **Take items one at a time.** For each:
   - Mark it in progress.
   - Form an actual recommendation. You have read the system; lead with your view. State the tradeoff honestly: what the recommended option costs and what the alternative costs.
   - Ask with a structured question tool if one exists, recommended option first and labeled "(Recommended)", plus one to three real alternatives. Keep it to this one item even if two concerns feel related.
   - When answered, mark it complete and restate the decision in one line. Do not reopen an answered item.

   - Valid: "Recommend gating the costly check behind the cheap filters, because most records fail the cheap ones. Option 1 (Recommended) ..."
   - Invalid: "What would you like to do about the costly check?"

3. **If a decision depends on live state, check it.** "Does the code already do X?" gets answered by looking at the code, the system or its docs, not by asking the person to remember or by trusting what an earlier session said. Live state drifts.

   - Valid: "Checked the workflow: the retry is already there, so this item is only about the alert."
   - Invalid: "A previous summary says retries exist, so let's skip that."

4. **After every item is decided, write the decisions back.** This step is easy to skip and must not be.
   - Update every skill whose behavior a decision changed.
   - Update project docs when a decision is a standing rule, not a one-off code change.
   - Save anything durable and relevant to later sessions in the person's notes or memory.
   - If a skill file cannot be edited in place, produce the updated file and hand it over to be saved. Never skip the update because the mechanism is awkward.
   - Say exactly what changed where, one line each.

   - Valid: "Updated: the qualification skill (step order), the infrastructure doc (retry rule), saved the approval decision to notes."
   - Invalid: "Done, I've updated things."

5. **Keep the to-do list current throughout.** It is the running summary if the person steps away and comes back.

## What a recommendation means

A specific, actionable option with its reasoning attached, not a neutral menu. The person can override it; the value is having a real starting point to react to, which is faster than building the option space from scratch.

## Failure modes

- All questions in one message.
- Options with no recommended one, or the recommendation buried mid-list.
- Trusting an earlier account of live state when a decision hinges on it.
- Finishing the questions and stopping. The write-back is part of the task.
- A vague write-back report instead of naming each change and its place.
