# Agent skills for running cold email with AI

Ten skills for AI agents (Claude, Codex and others that read `SKILL.md` files) that run a B2B cold email operation: four on the cold email work itself, six on keeping a multi-agent setup honest.

Every skill here exists because its opposite went wrong in real operation. Each one carries a Valid and an Invalid example and a short before and after.

## Install

Copy any folder from `skills/` into your agent's skills directory, for example `~/.claude/skills/` for Claude Code, or upload it as a custom skill in the Claude app. Each folder is self-contained.

## Cold email

| Skill | What it does | Before | After |
|---|---|---|---|
| [cold-email-first-touch](skills/cold-email-first-touch/SKILL.md) | First email and follow-up rules, how to change copy, launch check against approved texts | A per-lead AI sentence about the reader read as AI-written | Only checkable fields filled in; launch blocked unless every live step matches an approved text |
| [reply-handling](skills/reply-handling/SKILL.md) | Reply categories, check-and-redraft, testing, flagging a waiting reply | An interested reply sat four hours inside a status report | Waiting replies arrive as their own message; the approved send takes under a minute |
| [deliverability-audit](skills/deliverability-audit/SKILL.md) | SPF, DKIM, DMARC, provider tools, compliance, rates, incident order | A launch went out with the checklist never run | The audit is a launch gate with a written result |
| [pre-send-list-check](skills/pre-send-list-check/SKILL.md) | Verification, domain-to-company match, suppression, field junk | A verified address belonged to an unrelated company | Every row's domain is matched to its company before upload |

## Running agents without drift

| Skill | What it does | Before | After |
|---|---|---|---|
| [single-source-of-truth](skills/single-source-of-truth/SKILL.md) | Every fact in one source, pointers everywhere else, a sweep for retired wording | A prompt held an old price in its own words | Prices read from one file; the publish fails if the old number appears |
| [check-before-you-claim](skills/check-before-you-claim/SKILL.md) | Read the source before stating a fact; settings are not results | "Sends at 11 AM" from a settings field, for two days, while mail went at 8 | Times come from the sent records, compared with the setting |
| [permanent-fix](skills/permanent-fix/SKILL.md) | Turn every mistake into a check, a rule or a log line | The same silent release failure, patched by hand four times | An outcome check fails the run |
| [fewer-round-trips](skills/fewer-round-trips/SKILL.md) | Prompts that don't spawn more prompts | Seven prompts in eighty minutes, the human as courier | One prompt per agent; builder and releaser loop on their own |
| [disclose-gaps](skills/disclose-gaps/SKILL.md) | Reports state what is incomplete, unprompted | "No new replies" from a queue that hides declines and bounces | Counts come from the inbox, with every source named |
| [fix-the-generator](skills/fix-the-generator/SKILL.md) | Sweep for the pattern, fix what generates faults | One bug class flagged five times in one page | The first flag triggers a sweep of everything the edit touched |

## Before you contribute or fork

`scripts/scrub-check.py` blocks private data: email addresses, file paths, long IDs, key-like strings, phone numbers, and any term in a local `.scrub-blocklist.txt` (gitignored, so your list of real names never ships). Run it before every commit:

```bash
python3 scripts/scrub-check.py
```

## License

MIT
