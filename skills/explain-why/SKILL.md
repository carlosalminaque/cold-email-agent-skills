---
name: explain-why
description: "Use when the person asks why the agent did, skipped or misread something: why, why didn't you, what made you, or a bare question mark after an action. Gives the direct causal explanation first from what actually happened, states any wrong assumption plainly, and does not pivot into a new plan or new actions unless asked."
---

# Explain why

Needs: none

A "why" question is a question, not a new command. Answer it first.

## Steps

1. **State the direct explanation in the first sentence,** from what actually happened in the session: what was read, assumed or skipped.
2. **If it was a mistake, say so plainly,** including the wrong assumption behind it.
3. **Only then,** if it applies and is allowed, say what was or will be done about it.
4. **If the question is unclear,** ask one clarifying question, not a list.

## Limits

- Do not run destructive, live or publishing actions in response to a "why" unless explicitly authorized in the same message.
- Do not claim certainty about states not observed in this session.
- Do not replace the explanation with a plan unless asked.
- For "what do you think" or "how about X", use [straight-answer](../straight-answer/SKILL.md) instead.

## Examples

Valid: "I skipped the second file because I assumed the first one was the only config. That was wrong; both are loaded."

Invalid: "Good question! Here is my plan for the next steps..."
