---
name: checkpoint-handoff
description: "Use during long, tool-heavy agent sessions (workflow builds, integrations, browser work, multi-step coding), unasked, every handful of real steps and at each milestone, and whenever the human steps away or asks what is left. Writes a self-contained checkpoint file a fresh session can resume from, and keeps one shared open-items list, so no item lives only in one chat."
---

# Checkpoint and handoff

Needs: none

Long agent sessions can slow down, hang, or get compacted with no warning and no clean way to export the history. When that happens, whatever existed only in the chat is gone. A fresh session then either asks the human to explain everything again, or acts on guesses and redoes work: a second paid upgrade, an overwritten config, a migration run twice. Checkpoints written as a habit, like commits, mean there is always a recent save point. One shared open-items list means "what's left" has one answer, not one per session.

## When

- A milestone was just confirmed working.
- About to start a new open-ended sub-task.
- Every five to eight real tool steps in a long session, even with nothing dramatic done.
- The human says they are stepping away, switching chats, or asks "what's left".
- Several sessions or agents share the same live systems.

Do not ask before writing one. It is cheap and does not stop the work.

## Steps

1. **Write a checkpoint file,** not a chat message. It must survive the session. Sections:
   - **Goal** in one line.
   - **Check first:** things the next session must verify before acting (does this account or app already exist, is this change already live).
   - **Status** in four separate buckets: confirmed done (with how it was checked), decided but not built, proposed but not approved, open.
   - **Settled decisions** with one line of why each, so nobody reopens them.
   - **Order:** steps that must not run out of order.
   - **Blockers,** including ones only the human can clear.
   - **Pointers** to specs, mockups and files, instead of retelling them.
   - **Questions** for the human, each answerable in one line.
   - **Next actions:** a flat checklist, each line tagged with who acts.

2. **Keep one open-items list.** One file, open items only, one line each: what, who acts next, date raised. Closing an item means deleting the line and adding one line to a done log with the proof. Never tick a box and leave the line standing. No other doc keeps its own checklist; their open items go into this list.

3. **Stamp live-state claims.** Each line that states how a live system behaves carries "checked on date, how" or "unchecked". Re-check an unchecked claim before repeating it.

4. **Update the list in the same turn** that a checkpoint opens or closes an item. Edit an existing line rather than adding a near-copy.

5. **Write some facts immediately,** not at the next checkpoint: a changed standing rule, a retired component, a capability moving between agents, a new platform limit, a shared schema change. Ask: would another session acting right now make a wrong call without this? If yes, write it now.

6. **Write down unfinished work as unfinished.** Partly done or blocked work gets a line saying "not done, blocked on X". A bug found but not fixed gets written down too. Silence reads as "nothing happened here", and the next session will repeat or skip the work.

7. **Record decisions where they belong.** A decision goes into the one file that owns its topic. If no file owns the topic yet, add an entry for it to your index of owners first. Do not park decisions in a new decisions file, a handoff note, or memory alone, because each of those becomes a second, drifting copy. The checkpoint's settled-decisions list names each decision with a pointer to its owning file.

8. **Before answering "what's left",** read the whole open-items list and any newer handoff files, reconcile with live state, and fix stale lines.

9. **Keep working.** A checkpoint is a safety net, not a pause.

Durable facts that outlive one build (account URLs, which tools are in play, naming rules) belong in long-term memory or project docs. The checkpoint holds this build's moving state and points to them instead of re-explaining them. Save such facts to your agent's persistent memory (or a notes file if it has none) as you find them on a multi-session project, but never put fast-changing build progress into memory: it goes stale and gets trusted.

## Working in shared systems

- Before editing a shared system or file, look for a note that another session is active there. If the note is ambiguous or the situation unclear, ask the human and hold off, even for a small change.
- Read the target right before writing, and use its version marker or token if it has one, so a stale write cannot overwrite a concurrent edit.
- A retired component that is still running (an active automation, a logged-in account, an endpoint still accepting traffic) is not proof it is in scope. Check the standing decisions. If it should be gone, switch it off and record that, rather than repairing it.

## Resuming a dead or stuck session

- Do not assume how far it got. A checkpoint can predate real work, and the session may have done more or less than it claimed.
- Read its visible history if you can reach it. Where the history and the checkpoint disagree, say so and let the human break the tie.
- Ask for the real-world state (what is actually live, what the human saw) before resuming any step that changes something.

## Handing over to a new session

- Read live state first, and stamp the handoff doc with the time of that last real read. Never present older reads as current.
- Give the human exactly one short paste prompt. It points at the doc and tells the new session to re-read live state before trusting any line.
- Cancel the old session's scheduled check-ins, so two coordinators never act at once.

## Packaging an earlier answer as a file

When asked to turn a previous answer into a document, use the content as already stated. No new research, no new claims, no re-deriving. Produce one self-contained file and do not restate its content in the reply.

## Valid and Invalid

- Valid: "Confirmed done: webhook receives test events (read the receiver log). Decided, not built: retry on failure. Check first: the paid plan was already upgraded; do not upgrade again."
- Invalid: "Most of the integration is done, just finish the rest." No buckets, nothing to check first.
- Valid: "What's left: 7 open items from the list, 2 marked unchecked and re-checked just now."
- Invalid: answering "what's left" with the two items this chat happens to remember.
- Invalid: a handoff doc with its own checkbox list that never reaches the shared list.
- Valid: "Export job: not done, blocked on the missing API key. Found but not fixed: the date filter drops the last day."
- Invalid: leaving the export job out of the checkpoint because nothing finished.

## Before and after

- Before: a session answered "what's left" with two items. An older checkpoint held several more that were forgotten after the chat got long.
- After: one open-items list, read in full before every "what's left" answer.
