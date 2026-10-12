---
name: reply-test-battery
description: Use whenever an AI reply drafter for cold email is tested, fixed or shipped. Runs a fixed set of made-up prospect replies against a test copy, grades the drafts, and gates the release. Covers fixing the one rule source first, never editing model output in code, stopping when results flip, a pass bar split by what can reach a prospect unedited, a spend cap, and cheap iteration before one full paid run.
---

# Reply test battery

An AI reply drafter changes every time its prompt, rules or model changes. Without a fixed test set, each fix is checked against whatever reply happened to come in, and a fix for one case quietly breaks three others. A common failure: a team patches the drafter prompt to pass one case, the grader still holds the old rule, and the same cases flip between pass and fail on every run while the API bill grows. The battery is a fixed set of cases, one rule source, and a pass bar decided before the run.

## When

- Before any change to the drafter, its rules, its classifier or its model ships.
- When reading a battery report or deciding whether a candidate can ship.
- When drafting instructions for another agent to run the battery.

## What it is

- A fixed set of made-up replies: price, objections, out-of-office, unsubscribe, hostile, meeting requests, information requests, multi-turn threads.
- Each case runs through a test copy of the real drafter. A grader scores the draft against the written rules.
- It tests rule compliance, not persuasion. A perfect battery says nothing about meetings booked. Never report battery progress as messaging progress.

## Steps

1. **Fix the rule source first.** Reply rules live in one place. Write the change there, with a Valid and an Invalid example. The drafter, the grader and any code check read that source, never a paraphrased copy. Then test.

2. **No text surgery.** Never edit the model's output with string replacement, and never append fixed lines in code. Use check and redraft: a code check flags a rule break, the draft is redone once with the problem named, and a second failure is held for a human.

3. **Stop on a flip.** If a case passes in one run and fails in the next, stop patching. Two instructions disagree: rule source vs prompt, prompt vs grader, grader vs code check. Find the pair and fix it in the rule source.

4. **Split the pass bar.** Mark each case AUTO (could send without a human) or HELD (always goes to a human).
   - Must be zero on all cases: wrong automatic sends, missed unsubscribes.
   - Must be zero on AUTO cases: invented policy, wrong facts, unanswered questions.
   - HELD cases: the candidate must be no worse than the live version on the same cases.

5. **Iterate cheaply, gate once.** Between fixes, build the exact prompt the drafter would send and draft each case in a fresh agent context that has never seen the expected answers. Run a small regression set plus the last failures. Run the full set through the real workflow only as the release gate. That run catches code bugs the cheap run cannot.

6. **Cap the spend.** Every paid run states a money cap and a maximum run count. Use prompt caching on the large fixed blocks. One run at a time. Switch the test copies off afterwards and read back that they are off.

7. **Report.** A table against the bar, quoted drafts for every failure, a one-line cause for each (messaging or code), spend, and any case that flipped.

8. **Release.** Fresh read of the live version, publish, read back, record how to roll back. Then a real round trip through the test campaign. If it fails, check whether the live version has the same fault before blaming the candidate.

## Valid and Invalid

- Valid: "Price cases flipped twice. The grader still said never restate the price; the rule source now allows it when asked. Fixed the rule source, grader reads it, re-ran the regression set."
- Invalid: "Patched the drafter prompt so the price case passes."
- Valid: "Free iteration until the regression set passes, then one paid full run as the gate."
- Invalid: "Ran the full paid battery to see whether a one-word fix worked."
