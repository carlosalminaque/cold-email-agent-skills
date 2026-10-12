# Agent skills for running cold email with AI

33 skills for AI agents (Claude, Codex and any agent that reads `SKILL.md` files) that run a B2B cold email operation, in four tracks: the cold email work itself, testing, what to do when things go wrong, and running several AI agents without drift.

Most skills were written after something went wrong in real work. Each one carries Valid and Invalid examples. Not sure where to begin? Load **[start-here](skills/start-here/SKILL.md)**: it routes any task to the right skill.

**Status:** *proven* means the skill has run in daily operation for weeks and its rules came from repeated real failures. *Newer* means it is in use but has had less time to be tested by real cases.

## Install

All skills:

```bash
npx skills add carlosalminaque/cold-email-agent-skills
```

Or copy any folder from `skills/` into your agent's skills directory (for example `~/.claude/skills/` for Claude Code), or upload it as a custom skill in the Claude app. Each folder is self-contained.

## Cold email

| Skill | What it does | Status |
|---|---|---|
| [campaign-angles](skills/campaign-angles/SKILL.md) | 15 to 20 campaign concepts from broad to niche before committing to one | proven |
| [lead-qualification](skills/lead-qualification/SKILL.md) | Source and qualify in bounded waves, cheapest gates first, a source for every fact | proven |
| [cold-email-first-touch](skills/cold-email-first-touch/SKILL.md) | First email and follow-up rules; launch only if every live step matches an approved text | proven |
| [copy-refinement](skills/copy-refinement/SKILL.md) | The method for writing and fixing copy: rendered examples before rules, read as the recipient | proven |
| [pre-send-list-check](skills/pre-send-list-check/SKILL.md) | Verification, domain-to-company match, suppression, junk fields | proven |
| [deliverability-audit](skills/deliverability-audit/SKILL.md) | SPF, DKIM, DMARC, provider tools, compliance, rates, incident order | proven |
| [campaign-staging](skills/campaign-staging/SKILL.md) | Load a campaign into the sending tool, read it back, stop before launch | proven |
| [reply-handling](skills/reply-handling/SKILL.md) | Reply categories, check and redraft, what may send without a human | proven |
| [approved-reply-send](skills/approved-reply-send/SKILL.md) | Flag a waiting reply so it can't be missed; send the approved text and read it back | proven |
| [campaign-weekly-review](skills/campaign-weekly-review/SKILL.md) | Weekly deliverability, reply and retro pass per live campaign | newer |
| [outreach-experiments](skills/outreach-experiments/SKILL.md) | One variable, a sample floor, a read date fixed in advance | newer |

## Testing and research

| Skill | What it does | Status |
|---|---|---|
| [round-trip-test](skills/round-trip-test/SKILL.md) | Prove an automation end to end with a real message through the real path | proven |
| [reply-test-battery](skills/reply-test-battery/SKILL.md) | A fixed set of test replies run against an AI reply drafter before changes ship | proven |
| [stress-test-and-manual](skills/stress-test-and-manual/SKILL.md) | Click every state, misuse it on purpose, then write the manual | proven |
| [live-state-check](skills/live-state-check/SKILL.md) | Read the live tool before stating its state; settings are not results | proven |
| [demo-screenshots](skills/demo-screenshots/SKILL.md) | Clean happy-path screenshots for decks and manuals | newer |
| [campaign-prelaunch](skills/campaign-prelaunch/SKILL.md) | Every pre-launch gate in order, with a written result for each | newer |
| [prospect-report](skills/prospect-report/SKILL.md) | A verified, screenshot-backed report on a batch of prospects | newer |
| [tactics-gap-analysis](skills/tactics-gap-analysis/SKILL.md) | Compare outside cold email tactics with your own playbook, item by item | newer |
| [reply-to-written-request](skills/reply-to-written-request/SKILL.md) | Answer an RFP, job post or "send me details" email: every ask, in their order | newer |

## When things go wrong

| Skill | What it does | Status |
|---|---|---|
| [troubleshooting-order](skills/troubleshooting-order/SKILL.md) | Tag every claim, test hidden causes in order, smallest probe first | proven |
| [unstick-yourself](skills/unstick-yourself/SKILL.md) | Test concrete causes instead of stopping or saying "not possible" | proven |
| [check-before-you-claim](skills/check-before-you-claim/SKILL.md) | Read the source before stating a fact | proven |
| [fix-the-generator](skills/fix-the-generator/SKILL.md) | Sweep for the pattern, then fix what keeps generating faults | proven |
| [permanent-fix](skills/permanent-fix/SKILL.md) | Turn every mistake into a check, a rule or a log line | proven |
| [split-secret-drift](skills/split-secret-drift/SKILL.md) | Find and fix a secret stored in two places that drifted apart | proven |
| [checkpoint-handoff](skills/checkpoint-handoff/SKILL.md) | Checkpoints during long sessions; one open-items list | proven |
| [context-recovery](skills/context-recovery/SKILL.md) | Recover after compaction from what was really said, not the summary | proven |
| [review-executor-work](skills/review-executor-work/SKILL.md) | Check another agent's finished work against live state, not its report | newer |
| [context-audit](skills/context-audit/SKILL.md) | Audit an agent's rules, memory and skills for stale or conflicting context | newer |
| [second-opinion](skills/second-opinion/SKILL.md) | An independent critique of a plan before it is marked final | newer |
| [now-not-later](skills/now-not-later/SKILL.md) | Do it now unless a real dependency forces a wait | newer |
| [n8n-platform-notes](skills/n8n-platform-notes/SKILL.md) | n8n platform quirks worth knowing before you publish a workflow | newer |

## Running AI agents

| Skill | What it does | Status |
|---|---|---|
| [start-here](skills/start-here/SKILL.md) | Routes any task to the right skill | newer |
| [single-source-of-truth](skills/single-source-of-truth/SKILL.md) | Every fact in one source, pointers everywhere else | proven |
| [disclose-gaps](skills/disclose-gaps/SKILL.md) | Reports state what is unfinished, unprompted | proven |
| [fewer-round-trips](skills/fewer-round-trips/SKILL.md) | Prompts that don't spawn more prompts; agents close their own loops | proven |
| [handoff-prompts](skills/handoff-prompts/SKILL.md) | How to write a prompt another agent will run | proven |
| [route-blocked-work](skills/route-blocked-work/SKILL.md) | A blocked step goes to the next capable agent before it reaches a human | proven |
| [keep-going](skills/keep-going/SKILL.md) | Pick and log design decisions instead of stopping; ask at the end | proven |
| [skill-lint](skills/skill-lint/SKILL.md) | Scripts that check SKILL.md limits and lint a whole skills folder | newer |
| [visual-concepts](skills/visual-concepts/SKILL.md) | Four to six structurally different design concepts, checked at phone width | newer |
| [confirm-before-build](skills/confirm-before-build/SKILL.md) | State the end result in plain words and check what exists before building | newer |
| [least-manual-option](skills/least-manual-option/SKILL.md) | Pick the option that leaves the human the least to do | newer |
| [straight-answer](skills/straight-answer/SKILL.md) | A verdict or a pick first, then the reason, never a menu | newer |
| [synthesize-messy-input](skills/synthesize-messy-input/SKILL.md) | Turn a pile of uploads and links into the real question and a recommendation | newer |
| [coding-agent-prompts](skills/coding-agent-prompts/SKILL.md) | Prompts a coding agent runs: scope, markers, keep-going loops, real-run proof | newer |
| [multi-agent-skill-sync](skills/multi-agent-skill-sync/SKILL.md) | Keep rules in sync when several agents work one system | newer |
| [full-replace-write-safety](skills/full-replace-write-safety/SKILL.md) | Read, merge, write and read back when a tool replaces the whole document | newer |
| [one-decision-at-a-time](skills/one-decision-at-a-time/SKILL.md) | Work through a list of concerns one decision at a time | newer |
| [what-to-automate-next](skills/what-to-automate-next/SKILL.md) | Find the step most worth automating next | newer |
| [browser-automation-setup](skills/browser-automation-setup/SKILL.md) | Set up a browser agent so long click-throughs don't fail | newer |
| [browser-payload-transfer](skills/browser-payload-transfer/SKILL.md) | Get a large exact payload into a browser tab without retyping it | newer |

## Visuals and documents

| Skill | What it does | Status |
|---|---|---|
| [visual-plan-and-recap](skills/visual-plan-and-recap/SKILL.md) | A plan as a diagram before building; a visual recap after | newer |
| [comparison-diagrams](skills/comparison-diagrams/SKILL.md) | A shareable diagram for "why X worked and Y didn't" or X versus Y | newer |
| [mockups](skills/mockups/SKILL.md) | A recognizable mockup of a screen or page before it is built | newer |
| [preview](skills/preview/SKILL.md) | Show the current state of a page or deck as it renders | newer |
| [match-a-reference-image](skills/match-a-reference-image/SKILL.md) | Recreate icons and colors from a reference image exactly | newer |
| [step-by-step-guide](skills/step-by-step-guide/SKILL.md) | Plain, screenshot-backed steps a person can follow alone | newer |
| [spreadsheet-cell-rules](skills/spreadsheet-cell-rules/SKILL.md) | No blank cells, every value sourced, row heights that fit | newer |
| [docx-table-page-breaks](skills/docx-table-page-breaks/SKILL.md) | Word tables that break across pages cleanly | newer |
| [voice-recording-check](skills/voice-recording-check/SKILL.md) | Find why a recorded voice sounds off before building on it | newer |

## Before you contribute or fork

`scripts/scrub-check.py` blocks private data: email addresses, file paths, long IDs, key-like strings, phone numbers, and any term in a local `.scrub-blocklist.txt` (gitignored, so your list of real names never ships). Run it before every commit:

```bash
python3 scripts/scrub-check.py
python3 skills/skill-lint/scripts/lint_skills.py skills
```

## License

MIT. See [LICENSE](LICENSE).
