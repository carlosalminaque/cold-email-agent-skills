---
name: keep-going
description: "Use when the human says keep going, just make the call, don't stop for questions, or wants progress over check-ins on a long build or automation task. At each design fork, pick the option you would have recommended, log it, and continue. At the first natural stopping point, present every logged decision as multiple choice with your pick marked so the human can override. Sends, spend, publishing, deletion and credentials still need a yes first."
---

# Keep going, decide, report the decisions afterwards

Needs: none

An agent that stops at every design fork turns a two-hour task into a day of waiting. An agent that decides silently leaves the human unable to see or reverse what was chosen. This skill does both halves: never block on a design question, and never let a decision go unrecorded. The human reviews all the forks at once, at a moment that suits them, and can override any of them.

## When

- The human says "keep going", "just make the call", "don't stop for questions", or similar.
- A long build or automation task where forward progress matters more than check-ins.
- Not for anything irreversible or gated (see below).

## Steps

1. **At a real fork, pick what you would have recommended** if you had asked. Reason it as carefully as a live question. Prefer the existing pattern and the smallest reversible choice.
2. **Log it** in the task's notes or checkpoint: the question, the options, your pick, and why.
3. **Keep going** immediately.
4. **At the first real stopping point,** present every logged decision as a multiple-choice question with your pick marked "(Recommended)". Add what was validated and what risk remains. Flag any work built on a decision the human might override.

## Still ask before, not after

Sending on the human's behalf, spend, publishing, permanent deletion, credentials and irreversible submits need an explicit yes first. Keep-going mode never loosens these.

## Rules while working

- **A standing default is not a question.** If a saved preference already picks an option, take it and say so.
- **A checkable fact is never a fork.** If a doc, a test or a live read can settle it, check it instead of deciding it.
- **Validate step by step** and compare the result with the original request before reporting.
- **Spend the free options before stopping:** retry a glitch, try another interface, vary the technique, search for the exact error. "I don't know the fix yet" is a starting point, not a stop.
- **Before stopping, look for more work** on the task list that needs no new permission, and pull it.
- **Fix the system you own.** If you control both sides, fix the cause instead of automating around it.
- **Route, don't dump.** When this agent can't do a step, hand it to another agent with a one-line reason, not to the human.

## Valid and Invalid

- Valid, at the end of the run:

  1. Where should failed rows go? (a) a separate errors sheet (Recommended: keeps the main sheet clean) (b) a status column (c) drop them.
  2. Retry count for the webhook? (a) 3 (Recommended: matches the other jobs) (b) 5.

- Invalid: stopping mid-build to ask "should failed rows go to a separate sheet?"
- Invalid: choosing silently and never mentioning it.
- Invalid: decisions surfaced as a paragraph of prose the human has to parse.
- Invalid: "deciding" which API parameter name is right instead of reading the docs.
- Invalid: publishing a page under keep-going mode because "the human wanted no questions".

## Failure modes

Picking arbitrarily to move fast. Losing a decision. Surfacing decisions late or as prose. Treating a fact as a fork. Asking when a default exists. Stopping after one attempt. Stopping while work is left.

## Before and after

- Before: a build paused six times for design questions, each one waiting hours for an answer the agent could have guessed right.
- After: the build ran end to end, and the human changed one of six recommended picks in a single reply.
