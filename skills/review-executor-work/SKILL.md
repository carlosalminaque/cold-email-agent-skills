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
5. **Name the stop.** For any session that stopped, say which kind of stop it is: waiting at a real decision point (answer its question) or stalled with nothing left to wait for (restart or route it).
6. **Write it back.** Move closed items to the done log and keep open ones on the running to-do list, if the person keeps one.
7. **Do what you can close yourself, then reply.** A check ends with action, not a list. Any next step within your own reach is done in this turn, and the reply never lists an item you could have closed.
8. **Reply** with what finished, what failed, what is still unproven, and the next instruction for each track that has one. Include the open queue count, the pending question count, and each instruction you queued with its receipt or the reason it is still waiting. Say how many steps the person has to take. Run the reply checks below before sending.

## Scope: the whole check, whichever agent was named

A check covers every executor and active session, the work queue and any pending questions, even when the person names only one agent. The named one goes first in the reply; it never shrinks the check.

- **Machine health first.** If a host that runs agents is unhealthy (offline, on a network setting it should not have, doing no work), that goes at the very top, read fresh. If there is none, say so with the time you checked. A health file that has gone stale is itself a problem.
- **Every recent agent chat.** Read the last message from the person and the last reply in each agent chat active recently, not only the ones that keep a status file. Report them in a table (chat, last reply time, what it says, whether the person is needed). A status file or handoff note is not the chat's final word.
- **Work left behind is open work.** A task a finished agent left in the queue for another agent is reviewed with everything else, even when the person asked about a different agent.
- **Pending decisions.** Read every open question for the person each time. Put each at the top of the reply with the question, your recommendation and the exact words that answer it. When the person answers one in the session, write the answer into its question record (status, their words, the time) and queue the follow-up work in the same turn. A pending question must not sit unread behind a report about the queue.
- **The queue.** Read the whole work queue, not a folder listing. If your scheduler records why it skipped an item, count waiting items by that reason. An item waiting on a start condition is the runner's job, not the person's. When an executor is out of usage or quota, its waiting items are listed as waiting on quota, never as failures. When items are waiting but none can start, say that a usage limit is the constraint, not free capacity.
- **A gaps table to finish.** Every open item across all executors, read live this turn, gets one row ending in exactly one next move: a queued job, a handoff to another agent, or an action only the person can do. Add a coverage line naming what you read and what you skipped, and why.

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

## Finished media is checked where it is going

A video, image or cover that is headed for a public destination (a social account, a video channel, the website) is not sent to the person for review. Check instead that the live post or page carries the newest file and the right thumbnail. Send a file to the person only when they have to listen to it, sign it, upload it themselves or decide from it.

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
- Before asking about something they may already have told another agent, read that agent's latest message from them and its reply. An item already answered is not asked again.
- Only two things belong under "needs you": a decision that is gated (one the person said always needs their yes, such as sends, spend or deletion) and has no approval yet, and a step only the person can physically do. Test each candidate in order: is it gated, is it already approved, can an agent read or do it. Anything that is not gated, you decide yourself and log.

Valid: "Last read 8:14 PM Sunday: the payment had failed. Has it been fixed since? I can't see that console." Invalid: "The card is still failing. Please fix it."

## Count fixes before queuing another

Before queuing a fix, check whether the same part of the system already got a fix queued today. If so, stop and look for the generator of the problem (the script, template or rule that keeps producing it) and queue that fix first. Say the count in the reply.

## Hand the next instruction over through a file

If you have a work queue, and the next instruction is for another agent you can reach, put it in that agent's queue as a file and read its receipt. Give the person a prompt to paste only for a target the queue cannot reach. Never set a queued item to received or done by hand; only the runner that processes it sets that status. After queuing, read the scheduler's next pass (its skip log and its claims) to confirm the item was picked up. An item skipped as invalid or ineligible never starts on its own: fix it and queue it again. After writing a file through a sync or commit tool, read its size back from the destination, so you know the new version landed and not an older copy.

## Second opinion before a plan ships

The session that wrote a plan shares its blind spots, so reviewing it in the same session does not catch them. Before a non-trivial plan or build handoff is final, get a critique from a clean context. Skip this for small, low-stakes changes. Give the reviewer only the plan, the goal and the hard constraints already decided; leave out the discussion that produced the plan. Tell it to look for weaknesses, not to praise, and to report under fixed headings: showstoppers, gaps, inconsistencies, underspecified, suggestions, strengths. Each finding names the exact section and says concretely what breaks or stays unclear; "might cause issues" is not a finding.

For a high-stakes plan (money, an action that cannot be undone, several systems at once), run two independent reviews in parallel; where they agree is the stronger signal. Sort the findings before showing them: must fix before handoff, then minor. A finding the plan already covers elsewhere (a false alarm from missing context) is named as such and dropped. Show the sorted findings and ask which need the person's decision and which are obvious fixes. Never patch the plan quietly and ship it again without showing what changed.

Valid: "Two clean reviews; both flag the missing rollback step, one flags a naming nit. Rollback added (diff below); the nit is yours to call." Invalid: "Reviewed it myself, looks good, shipping."

## What not to do

- Don't ask the person to paste the report or say which file it is in, unless every read path has failed and you have said so.
- Don't answer from a report already in the chat. The executor has moved on since.
- Don't stop at "it says done".
