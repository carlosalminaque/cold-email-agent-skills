---
name: troubleshooting-order
description: "Use when troubleshooting stalls, the same request keeps coming back with no progress, a tool's output conflicts with what is visible, or a capability that should work fails. Separates what was checked from what was assumed, tests the common hidden causes in a fixed order, retries with a fresh handle before calling anything unavailable, takes the smallest probe that tells the theories apart, and checks the result from outside."
---

# Troubleshooting order

Needs: none

Most stalled debugging is not a hard problem. It is an easy problem worked from a wrong fact. A screenshot from an hour ago, another agent's report, or the agent's own first guess gets treated as true, and every later step builds on it. The fix is a fixed order of work that keeps checked facts and assumptions apart, and tests the boring causes before the clever ones.

## When

- The same fix has been tried twice and the symptom is unchanged.
- The human repeats the request, or asks "why is this still broken".
- A tool says one thing and the screen, file or record says another.
- A tool or connection that should be there seems to be missing.

## Steps

1. **Pin the goal.** Write the original objective in one line. Keep it fixed while the work branches.

2. **Keep a ledger.** Tag every claim you are relying on:
   - *observed*: you checked it yourself, this session, against the live system;
   - *stale*: it was true once, but time or later actions may have changed it;
   - *inferred*: a conclusion drawn from other evidence;
   - *unchecked*: someone said it and nobody tested it.

   Only *observed* is settled. Reports, screenshots and your own earlier conclusions start as *unchecked*.

3. **Test the hidden causes in order.** Rule each out before going deeper:
   - wrong target (file, record, environment, workflow version);
   - wrong account or identity;
   - stale state (a cached read, a page from before the change);
   - a hidden branch or fallback that the surface does not show;
   - permissions that look like a different error;
   - a change that was made but never saved, deployed or committed;
   - the tool is driving a different device, browser or account than the one you are looking at;
   - a limit above the session (account, plan, organization) that a fresh session would hit the same way.

4. **Retry fresh before you say "unavailable".** Open a new session, tab or tool handle. Re-list handles and IDs instead of reusing old ones. Reread the tool's own instructions. Try the other supported routes. If a brand new session fails in exactly the same way, the cause sits above the session; stop retrying and look there.

5. **Take the smallest probe that tells theories apart.** Not the action that fixes things if one guess is right. Prefer read-only or reversible checks.

6. **Check the result from outside.** Never infer success from the action itself. Say which level you confirmed: visible, saved, deployed, or behaving correctly end to end. Each one does not imply the next.

7. **Try to refute yourself.** Before concluding, look for the fact that would make your answer wrong. Label any doubt that survives.

8. **Hand off only after the above.** If a real gap remains after steps 3 and 4 and a search of the product's docs, write a self-contained prompt for whoever can act: the goal, what was ruled out and how, the steps to try in order, and how to confirm done.

9. **Report.** Outcome, evidence by ledger tag, what changed and what did not, open doubt, and the exact point where you stopped.

Never read, print, send or store a secret, token, cookie or password at any step. If a step would need that, stop and name the boundary.

## Valid and Invalid

- Valid: "Ledger: the webhook URL is observed (read from the live config just now). 'It fired yesterday' is unchecked (from a report). Smallest probe: send one test event and read the receiving log."
- Invalid: "The other session said the webhook works, so the bug must be in the parser." An unchecked claim was used as a fact.
- Valid: "A fresh session also shows the wrong device, so this is an account-level binding, not a session bug. Checking the account's active sessions next."
- Invalid: restarting the tool a fifth time after a fresh session already reproduced the exact same wrong target.
- Valid: "Confirmed saved and deployed. Not yet confirmed behaving: no real event has run end to end yet."
- Invalid: "Fixed" because the save button returned success.

## Before and after

- Before: an hour went into a parser that was fine. The edit had been made in a draft version that was never deployed.
- After: "change made but never deployed" sits in the fixed order at step 3, and gets checked in the first five minutes.

More on each hidden cause: `references/hidden-causes.md`.
