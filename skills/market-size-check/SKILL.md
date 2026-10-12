---
name: market-size-check
description: Use when asked whether a target market is big enough and worth enough for cold outreach, or for cohort numbers on qualification yield, reply rate or meeting rate by company size or funding. Reads live records, applies three economic-fit gates per company, keeps cohorts separate, and refuses to recommend a change from a thin sample.
---

# Market size and economic fit check

A market can look promising on a list and still fail: too few reachable buyers, deals too small to pay for outreach, or a buying path outreach can't touch. And a cohort table can mislead when it reuses last month's counts, blends small and large companies into one rate, or shows "0%" for a cohort with no sends. This check reads live data, judges each company on the same three gates, and says plainly when a number means nothing yet.

## When

- Before committing to a new market or segment.
- When someone asks for qualification yield, reply rate or meeting rate by cohort.
- Alongside sourcing, never instead of it (see `lead-qualification`).

## Steps

1. **Read live records.** Never reuse an earlier count or result as current. Exclude rows marked example, test, setup, dry run or failed send.
2. **Read your one source** for the thresholds: the size bands, the deal size that covers your cost, and your qualification rules. Don't invent them here.
3. **Three gates per company.** Mark each `Likely`, `Unverified` or `Poor`, with a source for each:
   1. **Deal size.** Public pricing or a sales-led path reaches the deal size your one source sets. Poor when visible pricing is far below it with no way up.
   2. **Trackable buying path.** Outreach can create something you can count: a demo, a call, a qualified trial. Poor for purely anonymous, low-value self-serve.
   3. **Reachable market.** The buyer is identifiable and there is a repeatable public way to find more like them. Poor only with real proof the market is too narrow.

   All three likely: proceed. Any poor: out. Any unverified and none poor: not yet decided.
4. **Cohorts.** Split by size band and by funding (funded versus self-funded), as your one source defines them. A range that crosses a band boundary stays out until an exact count is verified. Unclear funding stays out of that cohort and is logged as a missing fact. Never collapse cohorts into one blended rate.
5. **Rates per cohort.**
   - Qualification yield = qualified / all assessed in the cohort (rejected and undecided stay in the denominator).
   - Reply rate = real replies / real sends.
   - Positive-reply rate = interested plus meeting request / real sends, using categories already assigned.
   - Meeting rate = booked meetings / real sends.

   Count an outcome only when company, lead or campaign links it to a company defensibly.
6. **Empty is not zero.** No sends: "N/A (0 sends)". No records: "N/A".
7. **Thin-sample warning.** Every rate is descriptive until there are enough sends to tell a pattern from one or two rows. Never recommend a threshold or campaign change from a tiny sample.
8. **Record it.** A dated snapshot: sources read, time, method, all cohort rows, excluded rows and why, and every borderline call with the choice made.

## Valid and Invalid

- Valid: "Funded, small band: 12 assessed, 5 qualified (42%), 60 sends, 1 positive (1.7%). Thin sample, descriptive only."
- Invalid: "Overall reply rate 3% across all companies." (cohorts blended)
- Invalid: "Self-funded, large band: 0% meeting rate." (it had 0 sends; write N/A)
- Invalid: "Raise the size floor, the small band isn't working." (on 20 sends)

## Output

The cohort table first, then evidence gaps, the thin-sample warning, what was changed and not changed, and where the snapshot lives.
