---
name: unstick-yourself
description: Use when about to stop early, about to say a capability is not available, about to ask the human to redo work the agent could do, or about to blame an outage on something untestable such as propagation lag or the vendor's side. Records the exact symptom, lists several causes tied to what recently changed, tests them cheapest first, and resumes the original task as soon as the blocker is gone.
---

# Unstick yourself

An agent that hits a wall tends to stop with an explanation that sounds final but was never tested: "this tool is not available", "probably a transient blip", "must be on the provider's side". Each of these hands the work back to the human while real, cheap checks were still left. A blocker is only real once it has been proven. Until then it is a list of hypotheses to work through.

## When

- About to tell the human "I can't do this" after one failed attempt.
- About to ask the human to repeat a step the agent has tools to do.
- An outage is still unexplained and the next idea is "wait and see".
- The human pushes back: "try again", "why", "what did we change?".

## Steps

1. **Restate the goal and the last confirmed checkpoint.** Recovery starts from the last state you checked yourself, not from scratch and not from a guess.

2. **Record the symptom exactly.** The verbatim error, the tool or route used, the exact target (file, record, session, device), the state at the time, and when it happened relative to other changes. If a cause was already claimed, mark it as a claim.

3. **List several causes, then test the cheapest first.** Read-only checks before anything that changes state. For a live incident, start from the list of what changed recently: deploys, permission edits, moved files, config changes, new versions. Test each one for a link to the symptom.

4. **Check before calling a capability absent.** Is the tool registered right now? Was the session or connection initialized? Is there a setting that unlocks it? Is the permission real or stale? Is the session on the target you think? Has the object changed since you last looked? Absent means these were checked, not that one call failed.

5. **Treat outside causes as hypotheses.** "The vendor is down" is fine once tested (status page, a second account, a plain request). Untested, it is a guess, and the internal list is not done.

6. **Resume at once.** When the blocker clears, carry on with the original task. Do not stop to report a fixed blocker as if it were open, and do not ask again for approval that was already given.

7. **Stop only for one of these:**
   - a step only the human may do (a password, a 2FA code, a consent click);
   - a permission that was checked and is really missing;
   - a capability that is truly unavailable after step 4;
   - continuing would need clearly wider approval than the task already has.

8. **Report what is confirmed and what is not,** and why each open item is still open.

## Valid and Invalid

- Valid: "Two causes ruled out: sharing settings (file opens fine) and a code exception (no failed runs logged). Next, from what changed this week: the deployment was re-archived on Tuesday. Checking which version the URL serves."
- Invalid: "Both checks came back clean, so it is probably propagation on the provider's side. Let's wait." Untested, and the change list was never used.
- Valid: "The browser tool errored once. Re-listed tabs, opened a fresh tab, the read worked. Continuing the import."
- Invalid: "Browser automation isn't available in this session. Can you copy the table for me?"
- Valid, when asked "why": a new pass through steps 2 to 4 with a new hypothesis.
- Invalid, when asked "why": the same explanation reworded.

## Before and after

- Before: an outage sat for a day on "wait and see" after two hypotheses failed. The human had to ask what had changed.
- After: the recent-change list is the first source of hypotheses, and "wait and see" is not a step.
