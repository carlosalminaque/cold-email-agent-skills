---
name: start-here
description: Use at the start of any cold email or agent-operations task when it is not obvious which skill in this collection applies, or when someone asks what these skills do or where to begin. Routes the task to the right skill in four tracks (cold email work, testing, when things go wrong, running AI agents) and names the order to run them in for a new campaign.
---

# Start here

This collection has 61 skills in five tracks. Each skill does one job and points to the others where they meet. This file only routes; it holds no rules of its own.

## Which skill

| The task | Skill |
|---|---|
| Deciding what campaign to run | campaign-angles |
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
| Last checks before launch | campaign-prelaunch |
| Reporting on a batch of prospects | prospect-report |
| Someone sent tactics from a course or video | tactics-gap-analysis |
| Answering an RFP, job post or details request | reply-to-written-request |
| Another agent says it finished | review-executor-work |
| Rules or memory feel stale or contradictory | context-audit |
| A plan is about to be marked final | second-opinion |
| About to tell someone to wait | now-not-later |
| Before a nontrivial build | confirm-before-build |
| Choosing between ways to do something | least-manual-option, straight-answer |
| A pile of messy material and a vague ask | synthesize-messy-input |
| Prompting a coding agent | coding-agent-prompts |
| Several agents share one system | multi-agent-skill-sync |
| A tool that overwrites a whole document | full-replace-write-safety |
| A list of concerns to work through | one-decision-at-a-time |
| Deciding what to automate | what-to-automate-next |
| Long browser automation | browser-automation-setup, browser-payload-transfer |
| Working on n8n | n8n-platform-notes |
| A plan or change to show visually | visual-plan-and-recap, comparison-diagrams, mockups, preview |
| Matching a reference image | match-a-reference-image |
| Instructions for a person to follow | step-by-step-guide |
| Spreadsheets and Word files | spreadsheet-cell-rules, docx-table-page-breaks |
| A recorded voice sounds off | voice-recording-check |

## New campaign, in order

1. campaign-angles: pick the shape.
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
