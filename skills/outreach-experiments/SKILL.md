---
name: outreach-experiments
description: "Use when planning, running or reading a cold outreach test between segments, personas, angles or offers. Writes the plan before launch: arms that really differ, exact control and variant, a size worked out from the real reply rate, a fixed measurement window and one primary metric. Says up front when an arm cannot reach its size, and refuses small-copy tests that low volume cannot read."
---

# Outreach experiments

Needs: none

Reading a result well cannot fix a test designed badly. Two things changed at once, no fixed read date, twenty sends per arm, and an early peek reported as a finding: that test answers nothing, and it looks like it answered something. A small operation can still isolate one difference, work out what size its reply rate demands, fix a window, and decide before launch what counts.

## When

- Before launching any test between two versions of anything.
- When someone wants to "see which works better".
- When reading a result, to check the plan was followed.

## Steps

1. **Hypothesis in one sentence.** "If we change X, we expect metric Y to go up or down, because Z."
2. **One difference, and a real one.** Use this ladder: market (the list filter), segment (a split of that market that sees the world differently), persona (who there owns the problem), angle (the argument made to them). Write each arm as one line: "angle X to persona Y in segment Z of market M". Two arms with the same segment, persona and angle are one arm.
3. **Hold the rest still.** Same list rules, send window, cadence, inboxes and follow-ups. Two changes means two experiments, run in separate campaigns or separate time windows.
4. **Work out the size from your real reply rate.** A fixed floor of 20 to 30 sends per arm is wrong: at a reply rate of a few percent, 30 sends produce less than one reply, so there is nothing to read. Two-proportion math at 95% confidence and 80% power, from a 2.5% any-reply baseline:

   | Variant's true reply rate | Sends needed per arm |
   |---|---|
   | 1.5x baseline | about 3,000 |
   | 2x | about 900 |
   | 3x | about 300 |
   | 4x | about 160 |

   Rerun the math from your own baseline. Keep arms a similar size, never 20 against 200.
5. **Test big differences at low volume.** A subject line, one sentence or spintax is a small-copy test, and low volume cannot read it. Don't run those as experiments: pick the version your messaging rules prefer and move on. Test a different segment, persona or angle per arm, where a 3x gap is plausible, at about 200 contacts per arm, and read it by the buckets in step 10 instead of claiming significance.
6. **Check volume before you start.** Estimate how many qualified leads each arm can actually get, and say up front if one cannot reach its size. Often the right call is to drop the test and answer a more basic question first (does this market reply at all?).
7. **Fixed window.** Pick the read date before launch. A reasonable default is about three weeks after each arm's last send, so slow readers and out-of-office returns land.
8. **One primary metric.** Usually positive-reply rate or meeting rate. Others are context only.
9. **Write the plan down** before launch: hypothesis, arms, target size per arm, window, primary metric. A few lines in your running log is enough.
10. **Read only at the read date, into three buckets.** Clearly works: worth doing at this pace, so scale it. Clearly does not: no positives, or negatives showing they understood and said no, so drop it and keep the lesson. Messy middle: one or two positives, so a human decides whether to scale or test something else. Give each arm three lines: what you expected, what happened, what that means for the market. An early look is not a result, and an arm that missed its planned volume never yields a percentage.
11. **Log the outcome** next to where the decision to test was recorded: size reached, window, result, and the confidence caveat. A test dropped before launch gets logged too, with why, so nobody re-proposes it without a new reason.
12. **Keep passive tags.** If a segment test is dropped for lack of volume, keep tagging the segment on every lead, so an informal read stays possible later.

## Valid and Invalid

- Valid plan: "If we write to founder-led shops about X instead of the generic angle, positive-reply rate goes up, because Z. Arm A: angle X to founders in the founder-led segment. Arm B: generic angle to the same persona and segment. Same list rules, same inboxes, same follow-ups. 200 contacts per arm. Read three weeks after the last send. Primary: positive-reply rate."
- Invalid: "New subject line and new segment this week, let's see if replies improve." (two changes, no size, no window)
- Invalid: "Subject line A against B, 30 sends each." (small-copy test, under one reply expected per arm)
- Invalid: "Variant is winning, 2 replies to 0 after 15 sends each." (below its size, read early)
- Valid drop: "Only 4 qualified leads found for the variant segment after two sourcing passes. The arm needs about 200. Dropped the test, kept the segment tag on every lead. Logged."
