---
name: confirm-before-build
description: "Use before starting any nontrivial build, automation or integration task, especially anything that spans systems (agent-to-agent relays, workflow tools, CRM changes) or where done could mean more than one visibly different thing. Forces a short requirements pass before touching any tool: restate the end state in terms of what the person will actually see or do when it works, check whether something that already does this exists, and ask a targeted question with concrete options when the mechanism or visible behavior has more than one plausible reading. Skip it for small, unambiguous asks."
---

# Confirm before build

Needs: none

## Why this exists

A common and expensive failure: the person describes an experience in their own words, the agent picks a plausible technical reading, builds it, tests it, and declares it working. Every technical test passes. The person keeps saying they do not see the result. Only much later does it surface that the thing built and the thing asked for were different, sometimes when something that already did the job existed the whole time.

This skill catches that gap before building, not after.

## When to use

- Any integration or relay across systems.
- Any request where "it works" could look different depending on an unstated assumption: visible or background, real time or on request, automatic or with a human approval step.
- Any request that echoes something built before.
- Any build the person describes in plain experiential words rather than exact technical terms. "I want you and the other agent to talk back and forth" describes an experience, not a spec.

Skip it for small, clear asks: a one-line script, a well-scoped fix, a request that repeats an already-confirmed spec.

## Steps

1. **Restate the end state in terms of what the person will see or do,** not the internal mechanism.
   Valid: "You'll see my message typed into the other agent's open window, and its reply will appear there too." Invalid: "I'll build a relay channel between us."
   The second commits to nothing visible and leaves room for a background version that feels done to the builder but is not what was asked.

2. **Check what already exists before building new.** Search installed skills, memory, project docs and existing workflows for something that already does this or nearly does. If something does most of it, say so and ask whether to reuse or extend it.
   Valid: "There's already a skill that types into that window; extending it covers this." Invalid: Building a parallel version without looking.

3. **When there is more than one plausible reading, ask; do not guess and build.** Spell the options out concretely so the person can rule one out in one click.
   Valid: "Do you mean (a) I write to a file the other agent checks every few minutes and you read the log, or (b) you watch it happen live in its open window?" Invalid: "How should the relay work?"

4. **If the person corrects the reading mid-build, stop and re-confirm the new end state** before continuing. Do not patch the old approach and assume the correction was absorbed. A correction means step 1 was wrong or skipped.
   Valid: "Got it. Restating: replies should appear in your open window, not a log. Is that right?" Invalid: Tweaking the background version and testing it again.

5. **Watch for the warning sign:** tests keep passing but the person keeps saying it does not work for them. That is not a bug to keep debugging. It means the built thing and the requested thing differ. Go back to step 1.
   Valid: "Every test passes but you still don't see it, so I may have built the wrong thing. Let me restate." Invalid: Running a fourth technical check.

## What this is not

- Not a license to interrogate. Small asks skip it entirely.
- Not vague "what do you want?" questions. Restate a concrete guess first, and only ask when that guess has a real fork.
- Not a replacement for making implementation decisions yourself once the end state is confirmed. This settles the spec; the details after that are yours to decide.
