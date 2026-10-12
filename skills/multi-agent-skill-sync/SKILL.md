---
name: multi-agent-skill-sync
description: "Use whenever two or more AI agents (for example Claude and Codex, or several sessions with separate memory) work the same system and each keeps its own copy of skills, rules or notes. Fires the moment an agent edits a shared skill or rule file, and the moment it confirms, corrects or discovers a fact the other agent needs to act correctly (a root cause, a corrected live-state fact, a platform quirk, a reversed assumption, a new standing decision). Checks whether the content belongs in one shared source instead of per-agent copies, brings the other agent's copy to the same state in the same turn, and says out loud whether that happened."
---

# Multi-agent skill sync

## The failure this fixes

When two agents work one system, each with its own skill files and notes, the copies drift. One agent learns a sourcing rule the other never gets. One finds a root cause and fixes only its own notes, so the other keeps acting on the stale version. The mistake is treating "update my copy" as the whole job when the real job is "update the shared rule".

Two cases trigger this skill:

1. **An edit to a shared skill or rule file.**
2. **A finding that is not a skill edit at all** but would make the other agent's next action wrong: a root cause, a corrected fact about live state, a platform limit, a reversed assumption, a new standing decision.

It does not fire for routine progress, in-flight checkpoints, or notes scoped only to one agent's own execution.

## Step 1: one source first

Before writing new content into a local copy, ask whether it is volatile: a number, a threshold, a research-cited rule, a scoring framework, anything likely to be revised. Stable process (how to run steps, formatting) can live in each copy.

- If it is volatile and a shared source document exists, write it there and leave only a pointer in each local copy.
- If it is volatile and no shared source exists, do not extract one mid-edit for an unrelated task, but tell the person this skill is collecting content that will drift, so they can decide when to split it out.
- Valid: a new score cutoff goes into the shared scoring doc; both agents' skills point to it.
- Invalid: the new cutoff is pasted into one agent's skill and the other agent keeps the old one.

## Step 2: ask the parity question

"If the other agent ran a task right now without knowing this, would it act on wrong information?" If yes, it must cross over.

- Valid: "Root cause was the cache, not the lock. The other agent's notes still blame the lock, so update them."
- Invalid: fix your own notes and move on because the other agent "will figure it out".

## Step 3: put it where the other agent will read it

- A behavioral rule goes in the other agent's skill or instruction file.
- A live-state fact goes in the other agent's own running log or notes, if no skill file is the natural home.
- Keep each side's format. One side may keep an append-only log and the other a curated doc. The fact must be present and correct on both sides; byte-identical copies are not the goal.

## Step 4: push it directly

- If you can write to the other agent's files (shared folder, device bridge, repository), write the change there yourself and read it back.
- Only if no direct path exists, draft a complete copy-ready handoff for the person to paste. Paste the full text of any shared doc it relies on; a path the other agent cannot open blocks it. Say plainly that the copies are out of sync until it is pasted.
- If it is unclear whether a file has a counterpart on the other side, say so and ask. Do not assume either way.
- Valid: "Wrote the rule into the other agent's skill folder and read it back."
- Invalid: "This should be synced to the other agent at some point."

## Step 5: say it out loud

When reporting the edit or finding, state whether the other agent's copy was updated too. The person should never have to ask "did you also update the other one?"

## How to tell a skill is shared

Default to shared for anything that touches the common system, unless it only governs one agent's local conventions. Strong signs:

- The file says so.
- It governs a live system both agents write to.
- It references, or is referenced by, a skill already known to be shared.

## Closing check

Before ending a turn that changed a shared rule or produced a cross-system finding, answer: does the other agent now have it? If not, push it now. A deferred sync is a sync that does not happen.
