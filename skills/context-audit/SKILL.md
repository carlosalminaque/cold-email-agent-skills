---
name: context-audit
description: "Use when asked to audit an agent's working context for drift: its installed skills, persistent memory, project docs and instruction fields. Triggers include audit my setup, check for stale context, what has drifted, or a scheduled health check after a burst of new skills or parallel sessions. Read-only by default. Finds contradictions, broken references, retired skills that still trigger, stale open items, files restating facts owned elsewhere, and files that do not say whether they are current or historical. Scores four dimensions so drift can be tracked run over run, ranks findings by leverage, names an owner for each, and copies unresolved high findings into the running to-do list so they are actually seen."
---

# Context audit

Needs: local shell

A read-only audit of everything an agent loads as context. Over time, skills, memory and project docs drift apart: a skill still tells sessions to do something the person banned, a pointer names a file that no longer exists, an old checkpoint quietly passes for current. This audit finds that drift before a session acts on it.

Read-only means: produce findings, propose fixes, apply nothing without a yes per finding. The one exception is copying findings onto the to-do list (see below), which is a note, not a fix.

## Surfaces to inspect

**1. Installed skills.** List the skills folder and read each SKILL.md.
- Skills that contradict the person's stated preferences. Highest value: an active instruction to do something banned.
- References to skills or files that do not exist.
- Superseded skills that do not say so in their own description, so they still trigger.
- Contradictions inside one skill: two passages pointing opposite ways on the same case.
- Missing or empty descriptions, which make a skill trigger unreliably.

**2. Persistent memory.** List it, then read the suspects.
- Large old files duplicating a project doc: two sources of truth.
- Facts contradicted by newer docs or preferences.
- Files a cleanup pass claims to have handled but did not.

**3. Project docs and instruction fields.**
- To-do entries contradicted by live state: stale counts, old version IDs, items already done.
- Superseded checkpoints not marked as such.
- The same fact stated differently in two docs.
- The project's own description and instruction fields. These load first in every session, and often only the person can edit them. Check them against the docs every run; when they disagree, give the exact replacement wording and name the person as the owner.

Valid: "Skill X says to use the browser chime; preferences list it as rejected. A session following X would rebuild it." Invalid: "Some skills may be out of date."

## Restatement check

Flag any file that restates a fact owned elsewhere instead of pointing at it. A copied price or rule is a contradiction waiting to happen once the original changes. Instruction files should route ("prices: see the knowledge base"), not restate. Name the canonical owner for each hit.

Valid: "The setup skill states the price as 1,500; the knowledge base owns pricing and now says 2,000. Replace with a pointer." Invalid: Leaving the copy because it currently matches.

## Classification check

Every file should make clear which of three classes it is:

- **Durable knowledge.** True regardless of the current moment: a standing preference, a skill's method, a fact with one owner.
- **Project state.** True for now and expected to change: build status, an open decision.
- **Historical record.** A point-in-time account: a checkpoint, a session log. Once its facts live somewhere durable, it should be marked superseded.

Flag files whose class has to be guessed, and historical files whose facts were absorbed elsewhere but that are not marked superseded. Those are the ones that sit for weeks passing as current.

Valid: A checkpoint titled "Superseded, read the master to-do instead." Invalid: An unmarked three-week-old checkpoint that a new session reads as today's status.

## Lint, if a checker exists

If the setup ships a skill linter, run it on all installed skills every run, report counts by flag type and the change since the last run. If no skill files are on disk this run, say so in the first lines of the report and do not score capabilities as clean.

## Scoring

Score four dimensions, 25 points each, 100 total, and always show the breakdown:

- **Context.** Are facts current and single-sourced? Includes the classification check.
- **Connections.** Do references and pointers resolve?
- **Capabilities.** Do skills contradict each other, the preferences or themselves?
- **Cadence.** Is superseded material being retired, or only piling up?

Rank findings by leverage: how bad the wrong action would be, times how likely a session is to hit it. Record each run's score so the next run can state the change. A fix that does not move a score either was not real or was not the bottleneck.

## Findings must land where sessions look

An audit report in a dated file that nothing reads changes nothing. A correct high-severity finding can sit unread for days while sessions keep acting on the stale fact. So, every run:

- **Copy each unresolved high finding onto the running to-do list** that sessions read at start. One line: what is wrong, what a session would do wrong because of it, who can fix it, date first raised.
- **Remove the line** once a later run confirms it resolved.
- **Escalate on age.** A high finding open for more than three runs leads the report, with how long it has been open and what it has cost or risks.
- **Name an owner on every finding.** Some only the person can fix (fields only they can edit), some need a session with different access, some any session can fix. A finding with no owner is one nobody picks up.

Valid: To-do line "Project description still names a retired channel as live; sessions treat it as in scope; owner: the person; raised 3 runs ago." Invalid: The same finding only in a dated audit file.

## Output

Lead with the score, the breakdown, and any high finding open past three runs. Then each finding: what contradicts what, file and line evidence for both sides, what a session would do wrong, the owner, and the proposed fix. Then the top three fixes with concrete next steps. Stop there. If findings suggest building something new, propose it separately rather than building inside the audit.

## Cadence

On demand, and worth proposing after a burst of skill creation or parallel sessions. Do not schedule a recurring run without the person approving the interval.
