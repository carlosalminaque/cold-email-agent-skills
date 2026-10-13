---
name: live-state-check
description: "Use whenever a task needs the current state of a live web tool (a CRM, a workflow tool like n8n, a sending platform, a hosting panel) before stating it or changing it. Reads the state in the real tool through a signed-in browser or its API, checks which account is signed in, handles frozen tabs, never types credentials, stops at a safety block instead of cycling workarounds, and reports results rather than settings, with the time read."
---

# Live state check

Needs: browser control

What a system did yesterday, or what a summary says it does, is not what it does now. Several people and agents touch the same tools, and settings drift. A common failure: an agent reports "the workflow is active" from a note, when it was switched off a week ago. Another: the agent reads a permission error as real when the browser was signed into the wrong account. Read the live tool, say which account and when, and report results rather than settings.

## When

- Before stating any live fact: what is switched on, what was sent, what a record holds.
- Before editing anything in a live tool.
- When a prior session's summary is the only source for a claim.

## Steps

1. **Use the right route.** Signed-in web tools usually block plain HTTP fetches from a sandbox. Read them through a signed-in browser, or the tool's own API called from inside that browser tab. Do not retry fetch variations after a block.

2. **Check every browser you have.** Separate browser tools often have separate logins. If one shows no signed-in state, try the other before reporting a blocker.

3. **Check the account.** Browsers can be signed into the wrong account (a personal one instead of the work one). Confirm the signed-in identity before trusting a permission error, and say which account each check used.

4. **Read text, not pixels.** Prefer page text or a small script over screenshots. A failed screenshot does not mean a dead page. Check the page with a text read first. With many heavy tabs open, close down to one and reload.

5. **Drive stubborn controls carefully.** If a click does not register on a custom control, set the value through the page's own events and read it back after every step.

6. **Settings are not results.** Read what happened (the log, the sent items, the rows), not only what was configured. When both can be read, compare them. A difference is a fault and goes first in the report.

7. **A green status is not an outcome.** A 2xx response, a completed run or an active switch describes the mechanism. Read back the row, the cell or the count it should have produced.

8. **Switched on is not in scope.** Before fixing something that is running, check whether a decision retired it. A retired component found running gets switched off and recorded, not fixed.

9. **Report a snapshot.** State what was read, where, when, and under which account.

## Hard lines

- On a login screen, even autofilled: never click Log in and never type a credential. Ask the human to sign in, then continue.
- Never ask for a password and never accept one in chat. Never repeat an API key.
- Never click "create API key" yourself.
- If a safety layer blocks a live edit, stop at the first block. Do not try other tools or methods. Say what was blocked and hand over the exact change for someone with the right access.

## Shared change budgets

Some tools cap saved versions or deploys for the whole project. Read the live version list right before a change, name each version with workstream, date and purpose, and batch changes. Deleting versions is permanent and needs explicit approval.

## Valid and Invalid

- Valid: "Read at 14:05 in the work account: workflow active, last run 13:58, 12 rows written."
- Invalid: "The workflow is running fine" from yesterday's handoff note.
- Valid: "Permission error, but the browser was signed into a personal account. Switched, re-read: access works."
- Invalid: "I don't have access" after one browser, one account, one try.
