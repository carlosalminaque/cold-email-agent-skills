---
name: fix-the-generator
description: Use when a specific flaw is pointed out (a wrong word, a bug, a bad line, a broken assumption) and the fix is about to be a single-spot patch, and before proposing the first solution that comes to mind. Name the general pattern, sweep the whole surface for other instances and fix them in one pass, and when new kinds of fault keep arriving, find what in how the system is built keeps producing them.
---

# Think past the symptom

A flagged problem is usually one instance of a pattern. Fixing only the flagged instance leaves the rest live, to be found one at a time by whoever has to keep flagging them.

## The mechanic

When a flaw is pointed out:

1. **Fix the flagged instance** right away.
2. **Name the pattern.** "The actual issue is X; this line was one place X showed up."
3. **Sweep the surface.** Reread the whole section or file for the same failure, grep the codebase for the same anti-pattern, check whether the same assumption is built in elsewhere. Scope it to what one pass can reach.
4. **Fix everything the sweep finds,** in the same turn.
5. **Reread the new wording cold.** Does it say something, or does it restate its own heading or trigger ("we respond when someone replies")? A rewrite that fixes the flag but adds nothing is not done.
6. **Say what you checked.** "Reread the whole section for subject-less sentences; found two more, fixed both." If you found none, say that.

## Three levels of fix

Say which level each fix is at:

- **Instance:** this line, this record, this script.
- **Class:** every place the same mistake can occur.
- **Generator:** what about how the system is built or run keeps producing mistakes of different kinds.

The test of a fix's level: would it have prevented a fault of a kind not seen yet? If not, it is a class fix at best.

## When new kinds of fault keep arriving

Class fixes with clean sweeps can still leave a stream of new faults. That means a generator is at work.

1. Count the distinct kinds of fault in the last few days, from the issue list, not from memory. Three or more means a generator.
2. Write one sentence per generator. It names how the system is built or run, never a single fault. Examples: "steps are believed on their own report", "there are hundreds of one-off ways to write to the live system", "too much changes at once", "checks read settings instead of results".
3. The same change that fixes the latest fault carries a section for each generator, ahead of feature work.
4. A generator fix is something built: an outside check of outcomes, one shared write path, a limit a script enforces. A rule in a file is a stopgap and is called one.

## A mechanical sub-check for copy edits

When an edit removes or replaces the subject of a sentence, reread every sentence that used to point at it. Each must still name who or what does the verb. A sentence opening on a bare verb ("Engages only on replies...") is the tell.

## Valid and Invalid

- Valid: "Class fix: 98 wrapper scripts now pass failures on. Generator: nothing checks results from outside; the same change adds an outcome suite."
- Invalid: a fourth class fix called "the permanent fix" while new kinds of fault keep arriving.
- Valid: "Fixed 'what is it?' in line 3, and the two other sentences that lost their subject in the same edit."
- Invalid: fixing line 3 and waiting for the next flag.

## Before and after

- Before: the same dangling-pronoun bug was flagged five times in one page of copy, each time fixed in the one line pointed at.
- After: the first flag triggers a sweep of every sentence the edit touched.
