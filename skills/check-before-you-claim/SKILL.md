---
name: check-before-you-claim
description: "Use before stating anything as fact that a source exists to settle - how an API or library behaves, what a governing rule file says, whether a change is live, what a system did. Read the actual current source, try a second path when the first is inconclusive, and label anything still unchecked as unchecked. Covers API folklore, stale memory of internal rules, guesses reported as findings, and \"done\" claimed from a written intention."
---

# Verify before claiming

Needs: none

An agent's confidence is not evidence. Four versions of the same failure show up again and again:

1. **API folklore.** Code written from memory of how an API "usually" works, against a version where a parameter was renamed or a default changed.
2. **Stale internal rules.** A judgment made from what a rule file "probably says", without opening it. Provisional criteria get applied as settled ones, and caveats get dropped.
3. **A guess reported as a finding.** "That's probably an auth error" goes into a report as fact. The real cause was an argument-parsing failure.
4. **Done because it was written down.** A plan or note says "from now on X", so the agent reports X as in effect. The file that would need to change was never touched.

## The test

If a source exists whose job is to settle this exact question (the official docs for the installed version, a live read of the system, the governing rule file), check it before stating the answer. Especially when the answer feels obvious.

Skip it for trivial, self-contained edits where nothing version-sensitive or rule-governed is at stake.

## What to check, in order

External:

1. Local and live evidence: the lockfile's installed version, existing usage in the codebase, an actual call against the resource.
2. Official documentation for that exact version. A specific instance's own spec or admin docs beat generic public docs when they disagree.
3. Community material only as a supplement.

Internal:

1. The governing file itself, read in full, including dated corrections (they override earlier passages).
2. The documents it cites for its reasoning.
3. The confidence level travels with the rule. If the source says "provisional", the recommendation built on it says so too.

## The loop

1. A failed check is a branch, not a stop. If the docs don't settle it, run a live test. If the live test is ambiguous, look for a more authoritative source.
2. If more than one path fails to settle it, say exactly that: "I could not confirm X. I checked Y and Z; neither settled it."
3. Don't stop at the first plausible explanation.

## Settings are not results

A configuration says what was asked for. The record of what happened says what happened. When you report a time, a count or a state:

- read it from the log, the sent records, the rows themselves;
- when both the setting and the record can be read, read both and compare. A difference is a fault and goes at the top of the report;
- when only the setting can be read, say "set to", never "runs at" or "is".

## A green status is not a success

A 2xx response, a "completed" execution or a switched-on job is a claim about the mechanism, not the outcome. Read back what the step produced: the row, the cell, the file, the count.

## Text about a run is not the run

A chat-bot line, a log summary, a dashboard label or an AI-written profile is text one step wrote about something else. It can be wrong while the thing itself was right. Open the run or the record, say which one you read, and add no detail the line does not state. If you cannot open it, quote the line and mark the conclusion unconfirmed.

## Claims that need the same proof

- **Absence.** "It doesn't exist" or "that isn't possible" needs the same check as "it does".
- **Weak signals.** A field clearing or a spinner stopping does not prove a post landed or a save worked. Prefer a re-fetch or a visible result in the destination.
- **Identity.** Match a resource by its immutable ID or canonical URL, read back, before attributing an owner, history or behavior to it. A similar title, container or timestamp is not an identity check.
- **Readers of a thing.** "Which systems read X" is answered by opening each reader's own configuration, not by inferring from what the serving API offers.
- **Earlier findings.** A caveat or a "fixed and verified" line from a previous pass is a claim. Re-derive it before repeating it.
- **Saved state.** A stored phase such as blocked, needs-user or ready is a note, not live proof. Reconcile it with the latest transcripts and current instructions before preserving or reporting it.
- **Remembered response shapes.** Before calling a write and reread mismatched, inspect the live response and the handler's current contract. A shape recalled from earlier is not evidence of a failure.
- **Login walls.** A sign-in form seen right after navigation may vanish once the app restores its session. Let that finish and re-read the same tab before reporting a logout.
- **One checkable answer.** Do not apply "pick a reasonable option and move on" to a question with a single verifiable truth. Verify the factual part, then use judgment only on a true design fork.

## Testing a repair

- Run the code that actually ships: the real normalizer, the real category definitions, realistic aliases and casing. A friendlier test stand-in can pass while the deployed path fails.
- For an end-to-end proof, freeze the systems under test and record version and state baselines first. If someone else changes one mid-proof, mark the evidence mixed and rerun from a fresh baseline.

## Before any report

Check four things: the goal, what "done" means, concrete validation evidence for each claim, and the exact files and systems touched. If one is missing, say so instead of letting the report imply it is complete.

Tag each non-trivial claim: `[VERIFIED: <what was checked>]` or `[UNCONFIRMED: <what was tried and why it did not settle it>]`. Tag conclusions, not routine narration. Readers can then scan straight to the unconfirmed lines.

Say everything still open in the same report: unfinished, degraded, rolled back, deferred, unverified or broken. Nobody should learn of a gap by asking a follow-up. Each open line ends with its next action and who owns it; a report with an open line that lacks one is unfinished.

## Disclosing gaps: the checks behind an honest "nothing else is open"

1. **Enumerate mechanically.** Pull every open line from the whole to-do list, not the newest section, plus audit documents, scheduled runs, handoffs and queues sorted by age. A sudden drop in count means a format changed, not that nothing is open.
2. **Count from the source.** Event and reply counts come from the originating system, its alerts and any derived queue together, never the downstream queue alone. Name each source read and when.
3. **Join missing things to their consumer.** For anything listed as missing, unset or undeployed, check whether a live path depends on it. If so it is a present defect, not a chore.
4. **Use every entry point like a visitor.** Load each public page and app in a real browser, read the console, parse-check inline scripts, call each form endpoint with a labelled test submission (never a real one), open outside links, and repeat after any upload or repoint.
5. **Look inside the app.** Read caveats printed in the UI and the freshness footer, and read the actual rows, spotting test or synthetic data in production views. Reconcile the system of record against its external source row by row, and load the live authenticated page, since a grep of page source is not a data check.
6. **Surfaces against decisions.** Compare every dashboard, bot message, page, deck, help article and script that describes behavior with current decisions. A removed feature still shown, or two surfaces that disagree, is a gap. The lasting fix is generating them from one config.
7. **Public copy.** Each promise on a public page names the record showing it exists, and thresholds in copy match the form logic. Check wording rules by script over the rendered DOM (options, placeholders, titles, alt text, meta), never by eye.
8. **Enforced rules trace to a decision.** Every gate, cap or wait that scripts enforce should trace to a dated decision by its owner. Report any that does not, with what it blocks.
9. **Alerts and blocklists.** Read every alert type and the reason inside each bounce. Check sending domains against blocklists only after proving the resolver answers honestly; a list whose test fails is unchecked, never clean.

Writing the gaps report:

- Only open items, each with its next action and owner. No closed, context or FYI lines.
- An item waiting on an outside event carries the in-house test that would settle it now, or the reason none exists.
- End with a coverage line naming every source checked and every one skipped, with the reason and real numbers per check.
- If a gap surfaces that an earlier pass should have reported, the check failed. In the same turn say which pass missed it, find the cause, make the check mechanical, patch this procedure and run it now.

## Valid and Invalid

- Valid: "The schedule field says 11:00 to 17:00, but the send log shows Monday's emails went at 08:02. That is a fault."
- Invalid: "Sending opens at 11:00" read from the settings page.
- Valid: "The insert returned 201. Read back: 84 rows present, last one matches the input."
- Invalid: "The insert returned 201, so all 84 rows landed."
- Valid: "I wrote the new rule into the prompt file and re-read it: line 42 now says X."
- Invalid: "Done, the prompt now does X" because a planning note says it should.
- Valid: "The alert says no retry. The run stored a pending retry for the 12th (row read), so the alert text is wrong."
- Invalid: "The alert says no retry, so nothing was rescheduled."

## Before and after

- Before: an agent reported a campaign "sends at 11 AM" for two days, from the schedule field. The emails were going out at 8 AM.
- After: every time reported comes from the sent records, and the setting is compared against them.
