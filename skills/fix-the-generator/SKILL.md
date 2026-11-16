---
name: fix-the-generator
description: "Use when a specific flaw is pointed out (a wrong word, a bug, a bad line, a broken assumption) and the fix is about to be a single-spot patch, and before proposing the first solution that comes to mind. Name the general pattern, sweep the whole surface for other instances and fix them in one pass, and when new kinds of fault keep arriving, find what in how the system is built keeps producing them."
---

# Think past the symptom

Needs: none

A flagged problem is usually one instance of a pattern. Fixing only the flagged instance leaves the rest live, to be found one at a time by whoever has to keep flagging them.

## The mechanic

When a flaw is pointed out:

1. **Fix the flagged instance** right away.
2. **Name the pattern.** "The actual issue is X; this line was one place X showed up."
3. **Sweep the surface.** Reread the whole section or file for the same failure, grep the codebase for the same anti-pattern, check whether the same assumption is built in elsewhere. Scope it to what one pass can reach.
4. **Fix everything the sweep finds,** in the same turn.
5. **Reread the new wording cold.** Does it say something, or does it restate its own heading or trigger ("we respond when someone replies")? A rewrite that fixes the flag but adds nothing is not done.
6. **Say what you checked.** "Reread the whole section for subject-less sentences; found two more, fixed both." If you found none, say that and move on. A clean sweep is not a reason to redesign unrelated things, and it does not replace verifying the facts.

## Sweeping a whole set

When the job is to act on some members of a set (files, rules, records, pages):

- **List the set mechanically from its source** (a directory listing, a grep, an API list) and record the count. A pick made from memory misses items.
- **Give every member a status** from a fixed list, for example done, to add, covered by another item, alias, excluded. Every exclusion needs a stated reason; "not relevant" is not one.
- **Keep the classified list beside the work,** with a small script that fails on members the source has but the list lacks, and on list entries the source no longer has. Run it on a schedule so it stays true. Report counts: total, then per status.

## One source per fact

When a rule, number, text or decision changes:

1. Find the single place that owns it. If none exists, name one.
2. Change only that place. Every other copy becomes a one-line pointer to it.
3. Retire the old wording in the same change: add its distinctive phrase (whole sentences, not a bare word that is still valid elsewhere) to a retired-wording list (create one if absent), then sweep skills, docs, notes and public pages for the old version and require zero live hits.
4. Hand-written pages and outputs (website, slide deck, video script) are not sources. Edit them to match the source and include them in the sweep.

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
5. **Subtract first.** The answer to "too many rules" is never another rule. Ask what can be removed before adding anything.
6. **Get a second read before building.** Send the diagnosis and the proposed fixes to a fresh reviewer with a neutral brief and no conversation history. Ask: is this a generator or only a class; what is left untouched; what one high-leverage change is missing; which proposed change should be cut. Apply what survives, and say where you disagree and why.
7. **Split the output honestly.** Say which fixes are class fixes, build what can be built now, queue the rest as one job per owner or agent, and list what stays unfixed because nothing has been built for it.

## A mechanical sub-check for copy edits

When an edit removes or replaces the subject of a sentence, reread every sentence that used to point at it. Each must still name who or what does the verb. A sentence opening on a bare verb ("Engages only on replies...") is the tell.

## Valid and Invalid

- Valid: "Class fix: 98 wrapper scripts now pass failures on. Generator: nothing checks results from outside; the same change adds an outcome suite."
- Invalid: a fourth class fix called "the permanent fix" while new kinds of fault keep arriving.
- Valid: "Fixed 'what is it?' in line 3, and the two other sentences that lost their subject in the same edit."
- Invalid: fixing line 3 and waiting for the next flag.
- Valid: "Price changed in the one owning file; four other docs now point to it; old figure searched across all docs and the site, zero hits."
- Invalid: editing the price on the landing page and the deck by hand and calling the source updated.

## Before and after

- Before: the same dangling-pronoun bug was flagged five times in one page of copy, each time fixed in the one line pointed at.
- After: the first flag triggers a sweep of every sentence the edit touched.
