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
- The human pushes back ("try again", "why", "that makes no sense"). Treat it as a trigger for a fresh pass through steps 2 to 5, never a restatement of the same explanation.

## Steps

1. **Pin the goal.** Write the original objective in one line. Keep it fixed while the work branches.

2. **Record the exact symptom.** Before diagnosing, write down:
   - the error text or odd value, word for word;
   - any cause someone already claimed (a tool, a report, your own first read), marked as a claim until verified;
   - the route or tool used and the exact target (which file, record, session, device);
   - the state at the time and when it happened relative to other events.

   "It didn't work" makes every later step guesswork.

3. **Keep a ledger.** Tag every claim you are relying on:
   - *observed*: you checked it yourself, this session, against the live system;
   - *stale*: it was true once, but time or later actions may have changed it;
   - *inferred*: a conclusion drawn from other evidence;
   - *unchecked*: someone said it and nobody tested it.

   Only *observed* is settled. Reports, screenshots and your own earlier conclusions start as *unchecked*.

4. **Test several causes, cheapest and safest first.** Do not commit to the first explanation. List a few plausible causes and test read-only checks before anything that changes state. Rule these out before going deeper:
   - wrong target (file, record, environment, workflow version);
   - wrong account or identity;
   - stale state (a cached read, a page from before the change);
   - a hidden branch or fallback that the surface does not show;
   - permissions that look like a different error;
   - a change that was made but never saved, deployed or committed;
   - the tool is driving a different device, browser or account than the one you are looking at;
   - a limit above the session (account, plan, organization) that a fresh session would hit the same way.

   For an unexplained incident in a live system, first list what changed recently (deployments, permission edits, migrations, config edits, moved files) and test each change as a hypothesis before reaching for an outside explanation.

5. **Verify before calling anything absent.** A capability is missing only after you have checked that the tool is registered right now, that the session or connection was actually initialized, that configuration and permissions allow it, and that the object it acts on is in the expected state. One failed attempt proves nothing.

6. **Retry fresh before you say "unavailable".** Open a new session, tab or tool handle. Re-list handles and IDs instead of reusing old ones. Reread the tool's own instructions. Try the other supported routes. If a brand new session fails in exactly the same way, the cause sits above the session; stop retrying and look there.

7. **Do not accept an untestable explanation as an answer.** "Propagation delay", "a transient blip" or "the third party is down" is a hypothesis until tested. After two theories are ruled out, generate the next one instead of pausing to wait and see.

8. **Take the smallest probe that tells theories apart.** Not the action that fixes things if one guess is right. Prefer read-only or reversible checks.

9. **Check the result from outside.** Never infer success from the action itself. Say which level you confirmed: visible, saved, deployed, or behaving correctly end to end. Each one does not imply the next.

10. **Try to refute yourself.** Before concluding, look for the fact that would make your answer wrong. Label any doubt that survives.

11. **Resume at once.** When a blocker is repaired, go straight back to the original task. Do not report a fixed blocker as still open, and do not wait for permission to continue work that was already authorized.

12. **Stop only for a real stop.** The valid stops are: an action only the human can take (entering a password, solving a CAPTCHA) or any step that would need a secret (see the boundary below), a permission verified missing under step 5, a required capability that is truly unavailable after real discovery, or a task that would now cross a materially wider authorization boundary. Anything else is a recoverable blocker: try another route.

13. **Hand off only after the above.** If a real gap remains after steps 4 to 6 and a search of the product's docs, write a self-contained prompt for whoever can act: the goal, what was ruled out and how, the steps to try in order, and how to confirm done.

14. **Report.** Outcome, evidence by ledger tag, what changed and what did not, open doubt, and the exact point where you stopped. If your setup keeps durable notes or skills, do not update them from a recovery unless asked; if asked, record the general pattern, not one-off identifiers.

Never read, print, send or store a secret, token, cookie or password at any step. If a step would need that, stop and name the boundary.

## Valid and Invalid

- Valid: "Ledger: the webhook URL is observed (read from the live config just now). 'It fired yesterday' is unchecked (from a report). Smallest probe: send one test event and read the receiving log."
- Invalid: "The other session said the webhook works, so the bug must be in the parser." An unchecked claim was used as a fact.
- Valid: "A fresh session also shows the wrong device, so this is an account-level binding, not a session bug. Checking the account's active sessions next."
- Invalid: restarting the tool a fifth time after a fresh session already reproduced the exact same wrong target.
- Valid: "Confirmed saved and deployed. Not yet confirmed behaving: no real event has run end to end yet."
- Invalid: "Fixed" because the save button returned success.
- Valid: "Two theories are ruled out. Third: a config edit from Tuesday. Reading the change history."
- Invalid: "Probably a brief delay on their side, let's wait and see." An untestable explanation was used to stop.

## Before and after

- Before: an hour went into a parser that was fine. The edit had been made in a draft version that was never deployed.
- After: "change made but never deployed" sits in the fixed order at step 4, and gets checked in the first five minutes.

More on each hidden cause: `references/hidden-causes.md`.
