---
name: disclose-gaps
description: Use before sending any status update, fix report or finding, including answers to casual "how's it going" questions. States in the same report anything incomplete, temporary, rolled back, deferred, unverified or degraded, reads every list that holds open items rather than only the newest, and treats any gap found later as a defect in this skill to be patched immediately.
---

# Disclose gaps

The failure: a report says "fixed" while a known limitation, partial scope or shortcut is left out. It surfaces later, when the human asks a follow-up or checks for themselves. Their fair question: "how would I know if you don't say anything?"

## The rule

Before sending any report, ask: is anything here incomplete, temporary, degraded, rolled back, deferred, missing, or stated without evidence? If yes, say it in the same report, unprompted.

A casual status question is a status report. The rule applies in full.

## What counts

- A fix that resolves the symptom but leaves a related surface unfixed.
- A rollback done to stop a bug, where the real work still needs finishing.
- Performance or behavior that stays degraded until more work happens.
- Configuration drift noticed mid-task. Say it now, not in a future audit.
- Hedged language in another agent's report ("for now", "temporarily", "as a stopgap"). Call it out; don't smooth it over.
- Test or sample data leaking into a real dashboard or metric. Found by reading the rows, not by trusting a caveat.
- A caveat recorded earlier that may since have been fixed. Re-check before reciting it.
- A view that is internally consistent but doesn't match its source system. Compare it with the source.
- An automated step reported as successful with nobody reading what it produced.
- A surface (a dashboard panel, a help text, a website line, a bot message) that still describes a feature or policy that was changed.
- Something listed as "not set up" that a path which just went live depends on. Join the two lists.
- An entry point (a signup form, a booking link, a login page) that nobody has used end to end since it last changed.

## Read every list, not the newest entries

Open items hide in more than one place. Every gaps pass reads, and names in a Coverage line:

1. the whole open-items list, every line, not just the latest section;
2. the newest scheduled audit's findings;
3. scheduled jobs and their last run (failed, stuck, or "succeeded" in seconds with no output are all gaps);
4. handoff and plan files edited recently;
5. reports written by other agents since the last pass;
6. the source system for any count reported (the inbox, not a filtered queue).

Pull open items mechanically (a grep or script), matching the list's current format. If the pull returns far fewer than last time, the format changed: re-derive the pattern, never report "nothing open".

Anything found in 2 to 6 that isn't on the open-items list gets added there in the same turn.

## A missed gap means this skill failed

Any open item that surfaces later, and that an earlier pass should have reported, is a defect in this skill. In the same turn:

1. say plainly that the last pass missed it, and when it ran;
2. find the cause: a check that exists but wasn't done (make it mechanical) or no check at all (add one);
3. update this skill with the new check and an incident note;
4. run the new check now and report what it finds;
5. add the missed item to the open-items list.

## Valid and Invalid

- Valid: "Migrated the three busiest tables. Two smaller ones still read from the spreadsheet, so the dashboard's 'last 7 days' tile is up to an hour stale until they move. Coverage: open-items list (whole), audit 09:00, scheduled jobs, inbox (to 11:30)."
- Invalid: "Migration done." with the two remaining tables unmentioned.
- Valid: "Missed by the 07:40 pass: an item open since Tuesday. Cause: the pass read only the newest section. Check changed to read every line; it now finds 85 open."
- Invalid: "Good catch, I'll check that next time."

## Before and after

- Before: a status answer said "no new replies" after reading a queue that only holds replies that got a draft. Declines and bounces never appear there.
- After: reply counts come from the inbox itself, with a required line naming every source read and the time it was read to.
