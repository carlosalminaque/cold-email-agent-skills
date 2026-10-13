---
name: permanent-fix
description: "Use right after a human corrects the agent, at the end of every long session, and when asked for a retro or a permanent fix. Lists every mistake, refusal, workaround and correction from the session and turns each into the strongest fix available - first a check or script that makes the mistake impossible, then one short rule merged into the file that owns the lesson, otherwise a log line. Searches before adding so rules are merged, never duplicated. Ends with a count line."
---

# Permanent fix (session retro)

Needs: none

Every mistake should happen once. "Lesson learned, I'll be more careful" is not a fix: the next session starts with no memory of being careful. A fix is something that changes what the next session sees or what the system allows.

## When

- Right after a correction ("that's wrong", "why did it do that", a fact that contradicts what the agent said).
- At the end of every long session, without being asked.
- When asked for a retro or a permanent fix.

## Steps

1. **List.** One line per real item from the session:
   - every agent mistake;
   - every refusal or blocked tool;
   - every workaround;
   - every slow or round-trip pattern;
   - every claim made without a check;
   - every correction from the human.

   No hypothetical lessons.

2. **Fix each item, strongest first.**

   a. **Make it impossible.** Can a check, test, hook, lint rule or guard stop it happening again? Build it and run it once to show it catches the case. If another agent or person owns that code, write the exact prompt or ticket for them.

   b. **Otherwise, a rule, but only if it earned one.** Earned means the same problem appears earlier (in memory, the issue tracker, an earlier retro) or a test proves the current guidance wrong. Then add or merge one rule of two or three lines, with one Valid and one Invalid example, into the file that owns the topic.

   c. **Otherwise, log only.**

3. **Search before adding.** Grep the skills, agent instructions and memory for the same lesson. If a similar rule exists, sharpen it or merge into it. Never add a second copy. Rules hold operations, not incident stories.

4. **Log every item.** Append one line per item to a dated retro file: what happened | fixed where (check, rule, or log) | permanent or stopgap.

5. **Name stopgaps honestly.** A rule, a note to one session or a one-time cleanup is a stopgap. Only something built (a check that runs, a guard a script enforces) is permanent.

6. **A workaround is unfinished** until it has a check or an owning rule.

7. **Never widen permissions.** A retro does not grant the agent new rights. Sends, spend, publishing, credentials and deletion stay with the human.

## Reporting a correction

Every reply to a correction ends with two lines:

```
Permanent fix: <what removes the cause>, <built | in the prompt below | not possible, because ...>
Fixed in: <the one file that now owns it>
```

## Valid and Invalid

- Valid: "Restated an AI-generated summary of the user's work history as fact (correction). Same shape appears twice in earlier retros. Rule merged into check-before-you-claim: an AI summary of someone's history is a claim, check or ask before restating it. Logged."
- Invalid: "Lesson learned: be more careful with summaries." No fix, no owner, no log line.
- Invalid: adding a fourth near-identical rule to a skill that already has three.

## Finish

End with exactly one line:

`RETRO DONE: <n> items, <k> fixes, <m> rules, <j> logged.`

Say above it which items are permanent and which remain stopgaps.

## Before and after

- Before: the same "release script exited 0 but did nothing" fault was found four times, each time patched by hand.
- After: the retro turned it into an outcome check that reads the released file and fails the run when it doesn't match. The fault class stopped recurring.
