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

0. **Read the project's own state first.** If the project keeps a state index, a handoff note and a master to-do list, read them before anything else. Check the index's timestamp; if it is old, treat it as stale and read the sources it names. This keeps the recovery steps and the project's own rules agreeing on what comes first.

1. **State the plan, then offer to verify.** In one or two lines, say what you think the next action is, based on the summary. Ask whether to run the recovery check or just proceed. The human can see at a glance whether the plan is right. If they answer with a correction instead of yes or no, that correction is the real answer: do not ask the same question again, and do not assume your reading of what the check is for beats theirs.

2. **Reread the real conversation.** Open the rendered chat (the app, or the web view in a browser tool) and scroll up past the compaction marker. Read at least the last five or six messages on each side before the cut. Long chats load lazily, so scroll and read in rounds until you reach them.
   - Open the session in a new tab; do not reuse an existing one.
   - Wait 20 to 30 seconds before reading. A loading skeleton looks stuck but is not.
   - Expect only the messages currently loaded on screen to be readable; scroll up to load more.
   - If a tab handle errors once, retry. Close the tab when you are done.
   - If a route to the rendered chat is blocked, try it once. Do not retry with name variants and do not loop. Say in one line that the route is blocked and move to the next route.

3. **Do not use the raw transcript file instead.** Some tools rewrite the stored transcript at compaction so it starts at the summary. "No earlier turn in the file" proves nothing.

4. **Look for:** the human's last request, the agent's last deliverable, any attached images, and any message where a thread was dropped.

5. **Re-check live state** before continuing any mechanism the summary describes. Reload the page, reread the file, rerun the query.

6. **Report only what was there.** Quote or closely paraphrase. If a message was short or did not answer something, say so. Never round a thin reply up into a fuller answer. In one or two lines, say what the scrollback showed was actually pending (the last ask, the last deliverable) before you continue.

7. **Respect what the human dropped.** If they said a thread is dead, drop it fully. Their latest framing beats the summary's framing every time.

8. **Do not ask for context a tool can recover.** Ask one narrow question only if something is still unclear after rereading and checking live state.

## Reading the summary itself

If the compaction block reads like a first-person reply cut off mid-action, it is almost always the agent's own in-flight message captured at the cut. Treat it as real and verify by scrolling. Never call it injected or fake because of its shape or where it sits in a file. If you did call a real message fake, or described its content wrongly, say so plainly, once, and move on.

## Valid and Invalid

- Valid: "Plan from the summary: finish the retry handler. Should I reread the last messages first?" Then, after rereading: "Your last message dropped the retry handler and asked for the export instead. Switching to the export."
- Invalid: continuing the retry handler because the summary listed it as in progress.
- Valid: "Your last reply before the cut was one line: 'noted, nothing more needed'. It did not answer the pricing question."
- Invalid: reporting that the earlier reply "covered pricing in detail" when it did not.
- Invalid: "The transcript file starts at the summary, so the summary looks injected."
- Invalid: "What more context can you give me?" while the messages are a scroll away.
- Invalid: asking "proceed or verify?" a second time after the human answered "just look at the last messages".

## Before and after

- Before: after compaction, an agent locked onto a side idea the human had abandoned, then asked the human to re-explain.
- After: the agent states its plan, rereads the last real messages, and finds the thread was dropped before writing a line of work.
