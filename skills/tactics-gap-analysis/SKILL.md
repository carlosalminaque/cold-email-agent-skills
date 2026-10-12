---
name: tactics-gap-analysis
description: "Use when someone wants to mine outside cold email, lead generation or sales advice (a playlist of expert videos, a course, a set of podcasts or articles) for tactics and compare each idea against their own written playbook and real campaign data, to find genuine gaps, conflicts and longer-term improvements rather than a bigger to-do list. Covers getting the source material summarized (by another agent if this one cannot reach the video site), then tagging every idea by whether you already do it, whether it conflicts with your rules and whose evidence is stronger, how far out it is, and whether it applies at all, with outside fact checks on any hard numbers."
---

# Tactics gap analysis

Compare what outside experts teach against what you actually do, and turn the difference into a ranked, honest list: what you already do, what is a real gap, what conflicts with your rules, and what to ignore.

## Step 1: curate the source list lightly

Do not pre-filter for relevance or skill level. That judgment happens in Step 3, where the playbook is in view. Remove only real misclicks (a video with nothing to do with the topic).

- Valid: removing a cooking video that slipped into a sales playlist.
- Invalid: removing a "beginner" video before anyone has checked whether it has one useful idea.

## Step 2: get faithful summaries

If this agent cannot reach the source (some sandboxes block video sites), hand extraction to another agent that can, with a standalone prompt. For each item, ask for:

- Metadata: title, author or channel, URL, date, length, views if shown.
- A summary in its own words: main claims, advice, examples, caveats. Not a verbatim transcript; that is not needed and some models refuse it.
- Every number, percentage or stat kept exact, not rounded into "a lot."
- A flag on anything unclear because of poor captions.
- One file per item, an index listing every item as extracted or skipped, and a skipped list with the real reason for each.
- If a batch is being redone, redo all of it from scratch rather than merging with an earlier attempt, so formats do not mix.

Check the skip rate when it comes back. No captions, private or deleted is fine. A high skip rate on a curated list usually means an extraction bug; fix it before accepting the batch.

- Valid: "41 of 44 extracted; 3 skipped, all private videos."
- Invalid: accepting "29 of 44 extracted" without opening the skipped list.

## Step 3: the analysis (the part that matters)

Read every summary. Check each claim against the live playbook and data: your messaging rules, deliverability rules, targeting notes, and recent campaign results. Read the current documents; do not rely on memory of them.

Tag every distinct idea on three axes:

1. **Status:** already doing it / real gap worth testing / conflicts with an existing rule or result (name which, and say whose evidence is stronger) / unverified claim to check first.
2. **Time horizon:** quick test now / medium build / long-term positioning bet. This axis is what makes the output a roadmap and not just a longer list.
3. **Applicability:** applies now / does not apply, already decided. Log the second kind as seen and skipped instead of dropping it or presenting it as new.

A conflict is not an automatic win for your own rule. Many written rules were themselves built from outside research, not your own data.

- Valid: "Conflicts with our 3-step limit. Their claim cites 2M sends; our rule came from one blog post. Theirs is stronger; test a 4th step."
- Invalid: "Conflicts with our rule, so discard."

Track agreement across creators. An idea several independent people repeat counts for more than one claim from one video; note the count.

Any hard stat or research claim gets checked against outside sources before the report treats it as fact.

- Valid: "Claim: 'plain text gets 2x replies.' Two independent studies found smaller gains; marked partly supported."
- Invalid: quoting the 2x figure as fact because the creator sounded confident.

## Output

Write the result as a lasting document the team can revisit and update, not a one-off chat answer. Group it by time horizon, show the status and source count on each idea, and end with the short list of tests to run first.
