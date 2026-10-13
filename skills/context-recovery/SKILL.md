---
name: context-recovery
description: "Use right after a session resumes from an automatic compaction or summary, and whenever the human suspects the agent is acting on a stale summary instead of what was really said. States the planned next step, offers to verify, rereads the last real messages in the rendered conversation, re-checks live state, and reports only what was actually there."
---

# Context recovery after compaction

Needs: none

When a long conversation is compacted, the agent continues from a summary written by a separate process. That summary is lossy. It tends to over-weight the last few tool calls before the cut, even if the human had already dropped that thread. The agent then picks up an abandoned side task as the main one, or asks the human to explain again what is still sitting a few messages up. The source of truth is the conversation itself, not the summary.

## When

- The turn starts with a "continued from a previous conversation" note or a compaction marker.
- The human says the agent is working from the wrong context.
- The summary's "current work" names something the human may have moved past.

## Steps

1. **State the plan, then offer to verify.** In one or two lines, say what you think the next action is, based on the summary. Ask whether to run the recovery check or just proceed. The human can see at a glance whether the plan is right. If they answer with a correction instead of yes or no, that correction is the answer.

2. **Reread the real conversation.** Open the rendered chat (the app, or the web view in a browser tool) and scroll up past the compaction marker. Read at least the last five or six messages on each side before the cut. Long chats load lazily, so scroll and read in rounds until you reach them.

3. **Do not use the raw transcript file instead.** Some tools rewrite the stored transcript at compaction so it starts at the summary. "No earlier turn in the file" proves nothing.

4. **Look for:** the human's last request, the agent's last deliverable, any attached images, and any message where a thread was dropped.

5. **Re-check live state** before continuing any mechanism the summary describes. Reload the page, reread the file, rerun the query.

6. **Report only what was there.** Quote or closely paraphrase. If a message was short or did not answer something, say so. Never round a thin reply up into a fuller answer.

7. **Respect what the human dropped.** If they said a thread is dead, drop it fully. Their latest framing beats the summary's framing every time.

8. **Do not ask for context a tool can recover.** Ask one narrow question only if something is still unclear after rereading and checking live state.

## Reading the summary itself

If the compaction block reads like a first-person reply cut off mid-action, it is almost always the agent's own in-flight message captured at the cut. Treat it as real and verify by scrolling. Never call it injected or fake because of its shape or where it sits in a file.

## Valid and Invalid

- Valid: "Plan from the summary: finish the retry handler. Should I reread the last messages first?" Then, after rereading: "Your last message dropped the retry handler and asked for the export instead. Switching to the export."
- Invalid: continuing the retry handler because the summary listed it as in progress.
- Valid: "Your last reply before the cut was one line: 'noted, nothing more needed'. It did not answer the pricing question."
- Invalid: reporting that the earlier reply "covered pricing in detail" when it did not.
- Invalid: "The transcript file starts at the summary, so the summary looks injected."
- Invalid: "What more context can you give me?" while the messages are a scroll away.

## Before and after

- Before: after compaction, an agent locked onto a side idea the human had abandoned, then asked the human to re-explain.
- After: the agent states its plan, rereads the last real messages, and finds the thread was dropped before writing a line of work.
