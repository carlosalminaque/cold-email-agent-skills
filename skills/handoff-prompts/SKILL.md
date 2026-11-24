---
name: handoff-prompts
description: "Use whenever drafting a prompt another agent or session will run, or a reply to a report pasted from one. Covers the two-line header outside the block, one block per destination, never replacing a prompt already pasted (send a steering note instead), start conditions inside the block, scope by outcome and rule rather than method or count, and a final check on the actual text before it ships."
---

# Handoff prompts

Needs: none

When a human relays work between agents by pasting, every prompt is a paste, a wait and a chance for confusion. Most confusion comes from the shape of the prompt, not its content: which window it goes into, whether it replaces something already running, when exactly to paste it. These rules make a prompt unambiguous on first read and complete enough that the next report is not just a question back.

## When

- The human asks for a prompt, or pastes a report and asks "what do I reply".
- An agent is about to hand work to another agent through the human.
- The human gives a vague ask: rewrite it into a fuller prompt (the real goal, widened scope, constraints, output shape), answer that prompt yourself, and show what the rewrite added. The rewrite asks for current, cited evidence wherever facts change, names the output shape (verdict first), and holds no verdict of its own. It is a rewrite of the ask, not an adversarial review loop.

## Steps

1. **Read the report as claims.** Check what can be checked (live state, a hash, a doc): verify technical claims against docs or a live test, recompute any hash, and read the current to-do before older audits, fixing a stale project doc found in the same turn. Confirm the report states its goal, done criteria, validation evidence and touched files; name what is missing and ask for it inside the next prompt. Lead with any finding that means a live system is doing something wrong, wherever it sat in the report. In prose, call the source "the other session" unless the human named the tool. A claim that no safe path exists gets checked against what already worked elsewhere; often only the method tried failed.

2. **Decide what is yours to decide.** Only business, pricing, wording and irreversible choices go to the human, each with a recommendation. Do not copy your own tool limits into a prompt for an agent that does not share them. If the same owner controls both sides of a problem, fix the system rather than working around its interface, and lead with that option.

3. **Scope by outcome.**
   - Say what must be true at the end, not the clicks to get there.
   - Cover a whole area and end at a real gate or a finished deliverable, never at "report back what you find".
   - Give the rule that defines the set, not a count. "Every lead that is qualified and has an address" beats "the 88 leads".
   - Authorize precisely in kind and broadly in coverage: the whole class of action across the area, with what is out of scope named. Batch authorizations up front, label independent tracks, keep corrections to one line, and write fallbacks rather than stops.
   - Authorize the fix, not just the look. Live is not a reason for read-only; irreversible is.
   - For "fix everything", pull every open item mechanically, sort them into buckets that add up, and state the sum.

4. **Put start conditions inside the block.** "Start only when the file X reads DONE" is something the recipient can check. "Wait until I tell you" is not. Any condition in the prompt is checked against the recipient's own records, never the human's memory.

5. **Format.**
   - One fenced code block per destination per time. Holds and corrections go into that block, never a second add-on block.
   - Two lines directly above it, outside it: `Prompt N of M: paste into <where, when>` and `About: <one plain line>`. The destination never goes inside the block.
   - The first line inside is a topic named by the outcome ("CAMPAIGN PAUSE"), never an agent's name.
   - A prompt to a different system opens with one line on why that system should do the work.
   - The block's first instruction is to write a small started note with the time and the session's title, so a later check can tell a prompt that ran from one whose status is unknown. A status check looks for that note before claiming a prompt was not yet pasted; no file means unknown, never "not yet pasted".
   - "When" uses words that cannot mean two things: "paste now", "paste now into the session already running X, while it works", "paste once its report ends with X: DONE".
   - A hold that keeps a session away from a shared check must still let it run that check, without editing it, when a release depends on it.
   - Briefly state any discrepancy or missing report field before the block, so the human knows why the text says what it says.
   - The prompt is the last thing in the reply, so it is never lost between tool calls. Say "drafted", never "sent".

6. **Never replace a prompt already pasted.** Assume it was pasted as soon as it was given. A change goes as a short steering note to the same running session, saying only what changes. First check whether the run already did the thing; if so, the note says how to undo it, or no note is sent.

7. **Final check against the actual text.** Every block has its two header lines, numbered right. No "stop", "propose" or "await" without a named real gate. Every open item and every defect raised in the conversation is in the prompt or named elsewhere. The recipient is told to test its own work, and to review it adversarially, before reporting. No mid-task step needs the human when an automatic check exists; any step only the human can do is batched into one ask at the start.

## Valid and Invalid

- Valid:

  Prompt 1 of 1: paste now into the session already running BACKUP REPAIR (steering, while it works)
  About: skip the archive folder, it is handled elsewhere.

  followed by a three-line block that says only that.
- Invalid: a full new prompt headed "replaces both blocks from earlier" after the human already pasted them.
- Invalid: a prompt in one message and a second block "paste after the first one" (after it starts, or after it ends?).
- Valid: "Build the import file from every lead that is qualified, drafted and not a duplicate. Report the count and one line per exclusion naming the rule it failed."
- Invalid: "Re-check duplicates for the import file (88)."

## Before and after

- Before: add-on blocks, "replacement" prompts for runs already in flight, and headers that said "after" without saying after what.
- After: one block per destination, steering notes for running sessions, and a header that answers where and when in two lines.
