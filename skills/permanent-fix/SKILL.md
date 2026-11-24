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

2. **Fix each item, strongest first.** Before adding anything, ask what to remove: a duplicate rule, a rule a check already enforces, a copy that drifted from its source. A deletion or merge counts as a fix.

   a. **Make it impossible.** Can a check, test, hook, lint rule or guard stop it happening again? Build it and run it once to show it catches the case. If another agent or person owns that code, write the exact prompt or ticket for them.

   b. **Otherwise, a rule, but only if it earned one.** Earned means the same problem appears earlier (in memory, the issue tracker, an earlier retro) or a test proves the current guidance wrong. Also name one other fault from the last month that the new rule would have prevented: one instance is a log line, two is a pattern. Then add or merge one rule of two or three lines, with one Valid and one Invalid example, into the file that owns the topic. Keep rules short and free of narrative.
   c. **Otherwise, log only.** A one-off with no recurrence risk is a valid outcome: `Permanent fix: none, logged: one-off because <reason>`. So is `deleted <rule>` or `merged into <file>`.

3. **Search before adding.** Grep the skills, agent instructions and memory for the same lesson. If a similar rule exists, sharpen it or merge into it. Never add a second copy. Rules hold operations, not incident stories.

4. **Log every item.** Append one line per item to a dated retro file: what happened | fixed where (check, rule, or log) | permanent or stopgap.

5. **Name stopgaps honestly.** A rule, a note to one session or a one-time cleanup is a stopgap. Only something built (a check that runs, a guard a script enforces) is permanent.

6. **A workaround is unfinished** until it has a check or an owning rule.

   Three tests before calling a fix done:
   - Name the cause, not the instance.
   - Would it still change what happens if the agent made the same mistake again, or does it only work if a note gets read? Only the first is structural.
   - Run any new check against the current state at once and report what it finds.

   Where a lesson goes: when two homes are plausible, use the one read before the mistake, not the one that explains it afterward. Memory holds facts and decisions, never steps; steps go in a skill or an enforced check. Record the reason with every decision, since the reason survives cases nobody foresaw. If a skill already covers the missed case, make its existing check harder to skip instead of adding a duplicate line. Skip one-offs and choices that expire, but a correction to one draft is a rule when the same mistake could happen in the next.

7. **Track corrections as records.** Each correction opens a tracked record in the same turn, in whatever tracker you use. A record moves through accepted, built (an independent test passes), proved, closed. A different job accepts the record than the one that builds the fix, and an independent test run proves it, so the builder never judges its own work. For a repeat mistake, the proof is a check that re-runs the original failing case: it fails before the fix and passes after. An explanation closes nothing, and the retro does not finish while a record it opened has no artifact attached. When the same class of mistake comes back, mark it as a repeat: the fix must then go to the underlying cause (the habit, tool or design that keeps producing it), not another rule on the symptom.

8. **Files you cannot edit.** If a skill or file belongs to someone else or is read-only here, write the proposed change into a dated updates file for its owner rather than dropping it.

9. **Never widen permissions.** A retro does not grant the agent new rights. Sends, spend, publishing, credentials and deletion stay with the human.

10. **Don't stall the work for the retro.** Write the note, say the one line, and keep going, unless the fix touches something that needs the human's yes. Any promise of changed behavior says where it is saved and who it binds; never a bare "from now on".

## Reporting a correction

Every reply that reports any problem, not only a correction, includes the first line below, placed before the closing RETRO DONE line. A reply to a correction adds the second:

```
Permanent fix: <what removes the cause>, <built <what> | queued <item> | not possible, because <reason>>
Fixed in: <place> (done, binds <who>), <place> (not needed, <why>), <place> (not done, <what it takes>)
```

"Fixed in" lists every place that acts on the rule, meaning every agent, script or file that could repeat the mistake, not just the one file that owns it. Places that needed no change are listed too, with the reason. Next to each place that was changed, say who it binds.

## Valid and Invalid

- Valid: "Restated an AI-generated summary of the user's work history as fact (correction). Same shape appears twice in earlier retros. Rule merged into check-before-you-claim: an AI summary of someone's history is a claim, check or ask before restating it. Logged."
- Invalid: "Lesson learned: be more careful with summaries." No fix, no owner, no log line.
- Invalid: adding a fourth near-identical rule to a skill that already has three.

## Finish

The RETRO DONE line is the last line of the reply, after any Permanent fix and Fixed in lines. End with exactly one line:

`RETRO DONE: <n> items, <k> fixes, <m> rules, <r> removed, <j> logged.`

`<r>` counts what the retro took away: rules deleted or merged, checks or jobs dropped. A retro should not leave the system bigger than it found it. When fixes plus rules exceed removals, append `; net add because <reason>`.

Say above it which items are permanent and which remain stopgaps.

- Valid: `RETRO DONE: 5 items, 2 fixes, 2 rules, 1 removed, 5 logged; net add because both rules cover a new tool with no existing home.`
- Invalid: `RETRO DONE: 5 items, 2 fixes, 2 rules, 5 logged.` (nothing counted as removed, no reason for the growth)

## Before and after

- Before: the same "release script exited 0 but did nothing" fault was found four times, each time patched by hand.
- After: the retro turned it into an outcome check that reads the released file and fails the run when it doesn't match. The fault class stopped recurring.
