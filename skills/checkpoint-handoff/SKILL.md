---
name: checkpoint-handoff
description: Use during long, tool-heavy agent sessions (workflow builds, integrations, browser work, multi-step coding), unasked, every handful of real steps and at each milestone, and whenever the human steps away or asks what is left. Writes a self-contained checkpoint file a fresh session can resume from, and keeps one shared open-items list, so no item lives only in one chat.
---

# Checkpoint and handoff

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

2. **Keep one open-items list.** One file, open items only, one line each: what, who acts next, date raised. Closing an item means deleting the line and adding one line to a done log with the proof. No other doc keeps its own checklist; their open items go into this list.

3. **Stamp live-state claims.** Each line that states how a live system behaves carries "checked on date, how" or "unchecked". Re-check an unchecked claim before repeating it.

4. **Update the list in the same turn** that a checkpoint opens or closes an item. Edit an existing line rather than adding a near-copy.

5. **Write some facts immediately,** not at the next checkpoint: a changed standing rule, a retired component, a capability moving between agents, a new platform limit, a shared schema change. Ask: would another session acting right now make a wrong call without this? If yes, write it now.

6. **Before answering "what's left",** read the whole open-items list and any newer handoff files, reconcile with live state, and fix stale lines.

7. **Keep working.** A checkpoint is a safety net, not a pause.

Durable facts that outlive one build (account URLs, which tools are in play, naming rules) belong in long-term memory or project docs. The checkpoint holds this build's moving state and points to those.

## Valid and Invalid

- Valid: "Confirmed done: webhook receives test events (read the receiver log). Decided, not built: retry on failure. Check first: the paid plan was already upgraded; do not upgrade again."
- Invalid: "Most of the integration is done, just finish the rest." No buckets, nothing to check first.
- Valid: "What's left: 7 open items from the list, 2 marked unchecked and re-checked just now."
- Invalid: answering "what's left" with the two items this chat happens to remember.
- Invalid: a handoff doc with its own checkbox list that never reaches the shared list.

## Before and after

- Before: a session answered "what's left" with two items. An older checkpoint held several more that were forgotten after the chat got long.
- After: one open-items list, read in full before every "what's left" answer.
