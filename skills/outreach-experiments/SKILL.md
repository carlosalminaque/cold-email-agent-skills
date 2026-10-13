---
name: outreach-experiments
description: "Use when planning, running or reading an A/B test or segment test on cold outreach (subject lines, angles, offers, segments, sending settings). Writes the plan before launch: one variable, exact control and variant, a sample floor, a fixed measurement window and one primary metric. Also checks up front whether the available volume can reach the floor at all."
---

# Outreach experiments

Needs: none

Reading a result well cannot fix a test designed badly. Two things changed at once, no fixed read date, twenty sends per arm, and an early peek reported as a finding: that test answers nothing, and it looks like it answered something. Small operations can't run formal power calculations, but they can isolate one variable, set a floor, fix a window, and decide before launch what counts.

## When

- Before launching any test between two versions of anything.
- When someone wants to "see which works better".
- When reading a result, to check the plan was followed.

## Steps

1. **Hypothesis in one sentence.** "If we change X, we expect metric Y to go up or down, because Z."
2. **One variable.** Control and variant differ in exactly one thing. Same list rules, send window, cadence, inboxes and follow-ups. Two changes means two experiments, run in separate campaigns or separate time windows.
3. **Sample floor.** Don't read either arm below roughly 20 to 30 real sends; a single reply swings the rate too much. Better: keep both arms at a similar size, never 20 against 200. If you need a smaller effect detected, you need far more volume, so say so.
4. **Check volume before you start.** Estimate how many qualified leads each arm can actually get. If it will land below the floor, say so now. Often the right call is to drop the test and answer a more basic question first (does this market reply at all?).
5. **Fixed window.** Pick the read date before launch. A reasonable default is about three weeks after each arm's last send, so slow readers and out-of-office returns land.
6. **One primary metric.** Usually positive-reply rate or meeting rate. Others are context only.
7. **Write the plan down** before launch: hypothesis, control, variant, target size per arm, window, primary metric. A few lines in your running log is enough.
8. **Read only at the read date.** Check in if you like, but an early look is never reported as a result. If the floor wasn't reached, the result is "inconclusive", not a percentage.
9. **Log the outcome** next to where the decision to test was recorded: sample reached, window, result, and the confidence caveat. A test dropped before launch gets logged too, with why, so nobody re-proposes it without a new reason.
10. **Keep passive tags.** If a segment test is dropped for lack of volume, keep tagging the segment on every lead, so an informal read stays possible later.

## Valid and Invalid

- Valid plan: "If the first email asks for two samples instead of a call, positive-reply rate goes up. Control: call ask. Variant: sample ask. Same list rules, same inboxes, same follow-ups. Target 100 sends per arm. Read three weeks after the last send. Primary: positive-reply rate."
- Invalid: "New subject line and new segment this week, let's see if replies improve." (two variables, no floor, no window)
- Invalid: "Variant is winning, 2 replies to 0 after 15 sends each." (below the floor, read early)
- Valid drop: "Only 4 qualified leads found for the variant segment after two sourcing passes. Floor is 20 or more. Dropped the test, kept the segment tag on every lead. Logged."
