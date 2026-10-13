---
name: review-executor-work
description: "Use when another agent (a coding agent, a scheduled worker, a background run) says it finished or stopped, or when the person says check, go check, or it's done about that agent. Instead of asking the person to paste the agent's report, read its actual output files, handoff notes and logs where they live, verify the claims that matter against live state, compare any republished public file whole against the copy that was live before, diagnose failures in the same turn, and reply with what finished, what failed, what is unproven and the next instruction. Covers the common review mistakes: trusting a done marker, reporting a setting as a result, writing times the reader cannot read, and repeating an old request without re-reading its state."
---

# Review executor work

Needs: local shell

An executor (another agent doing the hands-on work) has finished or stopped. Your job is to go read what it did, check it, and come back with a review and the next instruction. The person should never have to paste the report to you if you can read it yourself.

## Steps

1. **Read the report where it lives.** The executor's handoff note, its log, its last message and the result files those name. Read the newest entries first. Use exact paths; broad globs over large output folders are slow and can time out.
2. **Check what matters against live state, not the report.** The live system, the chat channel it posts to, the files themselves. A script's own readback is still a claim until an independent read agrees.
3. **When something public was republished, compare the whole thing** with what was live before. See below.
4. **Diagnose any failure in the same turn.** Read the failing script and the file it checked before you reply.
5. **Write it back.** Move closed items to the done log and keep open ones on the running to-do list, if the person keeps one.
6. **Reply** with what finished, what failed, what is still unproven, and the next instruction for each track that has one. Say how many steps the person has to take. Run the reply checks below before sending.

## A done marker is a claim

"DONE" or a green status is what the executor says about itself. Treat it as a pointer to what to verify, never as the verification.

Valid: "Handoff says DONE; I read the output table and 48 of 50 rows landed. Two failed on a timeout." Invalid: "The executor reports DONE, so the import is complete."

## A republished file is checked whole

Executors often rebuild a page, deck or document to change one part, and silently revert other parts by building from an old local copy.

- Find the copy that was live before the change.
- Compare every page or section of the new live file with it, not just the part that was meant to change.
- List every difference. A difference outside the requested change is a defect, even when the requested change is correct.
- Check which source the new file was built from. It must be the version that was live, never an older draft.

Valid: "13 pages compared with the previous live copy; only page 11 differs, as requested." Invalid: "Pricing slide verified" with the other 12 pages unread.

## A setting is not a result

A configured value says what was asked for. The record of what happened says what actually happened. They can disagree for days without anyone noticing.

- A time, count or state you report comes from the record: sent times, execution history, the rows, the full list.
- When both the setting and the record can be read, read both and compare. A mismatch is a fault and goes at the top of the reply.
- When only the setting can be read, write "set to", never "sends at" or "is".
- A count comes from the list it counts, read in full, not from an earlier message about part of it.
- A countdown or "next run" timer is a forecast. Say something ran only after reading the record that it ran.

Valid: "The schedule says 11:00, but yesterday's sends went out at 8:02. That is a fault." Invalid: "Sending opens at 11:00" read from the settings page.

## A generic web fetch is not a live read

A cloud fetch can hit a cached copy, a different route or a bot block. Live facts come from the system itself, through a tool that is signed in or reads the real files. If none of those can be reached, say which sources were not read and stop there.

Valid: "The browser and file tools did not answer; the backend's state is unread." Invalid: "The backend returns 404, so it is probably deleted," from a generic fetch.

## "Cannot reach it" needs a failed call behind it

An empty tool search is not a read. Before saying a machine, folder or account cannot be reached, make the actual request for it, narrowly scoped, and retry once if the first answer is a transient "not ready". Only a real failed call justifies "not reachable". The person's device or location is never the reason by itself.

Valid: "Requested the review folder; granted; three new entries." Invalid: "I can't read those files from here" with no call made.

## Times are written in the reader's clock

Logs and executor-facing instructions can use UTC. Sentences the person reads use their own timezone with the day.

- Before sending, scan the prose outside code blocks for a digit followed by Z, and for "UTC". Convert them.

Valid: "The run stopped at 10:23 PM Eastern, Sunday." Invalid: "The run ended 02:23Z."

## Anything asked of the person is re-read first

A "needs you" line costs the person attention, so it gets the strictest check.

- Before repeating any request for them to act, re-read its state now, from a source that can see it.
- If no source can see it, write it as a question with the age of your last reading, never as a current fact or an instruction.
- The words "still", "remains" and "has not" need a read from this turn behind them.

Valid: "Last read 8:14 PM Sunday: the payment had failed. Has it been fixed since? I can't see that console." Invalid: "The card is still failing. Please fix it."

## What not to do

- Don't ask the person to paste the report or say which file it is in, unless every read path has failed and you have said so.
- Don't answer from a report already in the chat. The executor has moved on since.
- Don't stop at "it says done".
