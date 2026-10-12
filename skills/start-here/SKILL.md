---
name: start-here
description: Use at the start of any cold email or agent-operations task when it is not obvious which skill in this collection applies, or when someone asks what these skills do or where to begin. Routes the task to the right skill in four tracks (cold email work, testing, when things go wrong, running AI agents) and names the order to run them in for a new campaign.
---

# Start here

This collection has 33 skills in four tracks. Each skill does one job and points to the others where they meet. This file only routes; it holds no rules of its own.

## Which skill

| The task | Skill |
|---|---|
| Deciding what campaign to run | campaign-angles, then market-size-check |
| Finding and qualifying companies and people | lead-qualification |
| Writing or fixing the emails | cold-email-first-touch for the rules, copy-refinement for the method |
| Before a list goes into the sending tool | pre-send-list-check |
| Before the first send on a domain | deliverability-audit |
| Loading a campaign into the sending tool | campaign-staging (stops before launch) |
| Replies arrive | reply-handling, approved-reply-send |
| A campaign has been live a week | campaign-weekly-review |
| Testing a change on purpose | outreach-experiments |
| Proving an automation works | round-trip-test, reply-test-battery, stress-test-and-manual |
| Reading a live tool before saying anything about it | live-state-check, check-before-you-claim |
| Screenshots for a deck or manual | demo-screenshots |
| Something is stuck or broken | troubleshooting-order, then unstick-yourself |
| An API key stopped working | split-secret-drift |
| A long session, or picking one back up | checkpoint-handoff, context-recovery |
| The human corrected the agent | permanent-fix, fix-the-generator |
| Handing work to another agent | handoff-prompts, route-blocked-work, fewer-round-trips |
| Long build with many small decisions | keep-going |
| A fact, price or rule changed | single-source-of-truth |
| Reporting status | disclose-gaps |
| Writing or editing a skill | skill-lint |
| Someone dislikes how something looks | visual-concepts |

## New campaign, in order

1. campaign-angles and market-size-check: pick the shape.
2. lead-qualification: build the list.
3. cold-email-first-touch with copy-refinement: write and test the copy on rendered emails.
4. pre-send-list-check and deliverability-audit: both are launch gates with a written result.
5. campaign-staging: load it, read it back, stop before launch. A human launches.
6. reply-handling and approved-reply-send once replies come in; campaign-weekly-review each week.

## Ground rules every skill shares

- The facts that are yours (who you target, your prices, your approved texts) live in one source you own. Skills point to it and never restate it.
- Sends, spend, publishing, deletion and credentials always need a human's yes.
- A green status is a claim. Read back what the step produced.

Valid: "New campaign: ran campaign-angles, then lead-qualification on the chosen angle." Invalid: loading leads into the sending tool before pre-send-list-check and deliverability-audit have a written result.
