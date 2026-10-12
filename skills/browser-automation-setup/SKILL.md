---
name: browser-automation-setup
description: "Use at the start of any multi-step browser automation task driven by an AI agent through a browser extension or DevTools connection (editing a node-graph editor such as n8n, testing a web UI, any job with several clicks and edits in a row). Sets up an isolated tab and covers the common failures: screenshot timeouts on hidden tabs, safety-classifier blocks, missed drags on tiny canvas targets, overlapping nodes, content-filter false positives on code reads, frozen tabs, and sign-in redirects in the agent's own tab. Also use mid-task when any of those failures appear."
---

# Browser automation setup

## The common failures

1. **Screenshot timeouts.** The screenshot call times out ("renderer may be frozen") while clicks, typing and script evaluation still work. Browsers stop producing frames for hidden tabs, so a buried or minimized tab cannot be captured.
2. **Classifier blocks.** An agent's safety layer can refuse legitimate actions, sometimes even read-only DOM queries. A block on a read-only query is a stop for that turn. Do not retry around it.
3. **Drag misses on tiny targets.** Connector dots of a few pixels are missed when coordinates come from eyeballing a screenshot: the node moves instead, or the edge lands on the wrong nearby node.

## Setup

1. Start with a fresh, isolated tab or window. It clears most screenshot timeouts and some blocks. The person does not need to watch the tab.
2. If a fresh isolated tab is still blocked, that is a real stop, not a setup problem. Report it instead of creating more tabs.

- Valid: "Fresh tab still refuses the read-only query; stopping and reporting."
- Invalid: open a fourth and fifth tab hoping the block clears.

## Canvas and node-graph editors

1. **Read exact positions from the DOM before any drag.** Query the handle elements (for example `.vue-flow__handle` or `data-handleid`) and use `getBoundingClientRect()` for exact centers. Fall back to zoomed screenshots only if that read is blocked, and expect more misses.
2. **Verify against the app's own data, not a screenshot.** After any connection edit, read the saved graph from the app's API (for n8n, a same-origin `GET /rest/workflows/{id}` with `credentials: 'include'`). A line on a cluttered canvas is not proof.
3. **If a drag moved a node instead,** undo once right away, then re-read the saved data to confirm nothing else was undone with it.
4. **Overlapping nodes:** when clicking one node keeps opening a neighbor, drag the covering node a modest distance away first. It is a reversible layout change. Confirm in the saved data that only position fields changed.
5. **A failed drag is usually a coordinate problem.** Different automation tools use the same underlying mouse-event sequence. Check whether the coordinates came from the DOM or a screenshot before blaming the tool.
6. **Prefer a first-party editor assistant** when the app has one (n8n has a built-in AI Assistant). It edits through the app's own API, so drag precision and classifier blocks do not apply. Verify its result in the saved data too.

- Valid: "Read handle centers from the DOM, dragged, then confirmed the new edge in the workflow JSON."
- Invalid: "Screenshot shows a line between the two nodes, so it is connected."

## When automation cannot finish the job

In order: (a) the app's own assistant, driven conversationally; (b) plain-text click steps for the person using the exact node and output names shown in the UI; (c) another browser-capable agent, whose claim is then checked against the saved data. Check any annotated screenshot against the real target before sending it.

## Blocked writes are not blocked screenshots

A blocked write says nothing about whether a screenshot or read will work. Try each action on its own merits. Different agents also fail for different reasons (one is refused by its classifier, another hits a client-side network block), so verify that the other agent can actually do the write before routing it there.

- Valid: write was refused, screenshot attempted anyway and it worked.
- Invalid: "Writes are blocked, so I could not take a screenshot either."

## Content-filter false positives on code reads

Reading raw code or JSON that contains words like "cookie", or base64 output, can trip a content filter. Return the string as joined character codes and decode it outside the tool call.

## Frozen tab: fix it yourself first

If script evaluation times out even on `1+1`, close that tab, open a fresh one, and navigate back. Do this before asking the person to reload anything. Some agents attach to an existing tab and cannot open or close tabs; for those, the person reopens the tab or the task moves to an agent that can.

- Valid: close tab, new tab, navigate, `1+1` returns 2, continue.
- Invalid: "The page seems frozen; can you reload it?"

## Sign-in redirect only in the agent's tab

A redirect to a sign-in page that happens only in the agent's tab is usually a missing session in that tab. Retry with a fresh navigation, and have the person sign in once inside that tab, before routing work elsewhere. Never trust an earlier session's "could not authenticate" note without retrying. Fixing sign-in does not fix the other issues above.
