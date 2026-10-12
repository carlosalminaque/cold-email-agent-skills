---
name: copy-refinement
description: Use before drafting, reviewing or fixing any outbound copy (cold email steps, reply drafts, deck or website lines, example emails) and whenever someone reacts to a rendered line with "that doesn't make sense" or "why does it say that". Finds the root cause before patching, shows rendered examples before rules, reads every draft as the recipient, stops after two patch-induced failures, freezes fixed elements, and ships every rule with a Valid and an Invalid example.
---

# Copy refinement

Most bad copy is not a wording problem. It is a mechanism asking one line to do a job it cannot do from its inputs, then patched rule by rule until the rules contradict each other. In one rebuild, a per-lead AI sentence about the reader passed every written rule (sourced, checked, read aloud) and still read as AI-written to the one prospect who answered. The rules tested whether a line was true. None tested whether it was worth reading. This skill is the method that makes copy rules, tests them on real sentences, and keeps them small. The domain rules themselves (your wording, your bans, your approved texts) live in your one source, not here.

## When

- Before any outbound copy is drafted, reviewed or changed.
- When a human reacts to a rendered line.
- When the same kind of fix has been made twice.
- When a wording has gone to a couple of hundred people with almost no positive replies. That is evidence against the structure, not only the list.

## Steps

1. **Root cause first.** If errors grow with the number of rules, the mechanism is wrong. Fix what is fixed versus generated before touching a rule, and say so out loud.
2. **Check outside evidence.** Search how working operators do it before choosing an approach, and again on the exact failing question after the same fix fails twice. Cite what you found.
3. **Generate only what can be checked.** A filled-in field states only what a named source shows. Inference and consequence go in fixed text written once per segment, true of that whole segment by construction.
4. **Show rendered examples, not rules.** Every proposal is a full email, greeting to sign-off, with a plausible company name and no placeholder for the part under discussion. The human approves sentences, never abstract rules.
5. **Recipient-reaction gate.** Read the draft as the recipient and write their one-line reaction next to it. Kill it if the reaction is "that's exactly what I'm doing", "those two sentences don't go together", "why are you telling me this" or "I already know this about myself". For each sentence, answer: what does this tell them that they don't already know?
6. **Clarity over concision.** Write it as said aloud. No dropped verbs, noun stacks or three ideas in one clause. Use a whole-message range checked by script (word count, longest sentence), not a word cap on one field.
7. **One flag, one sweep.** Name the pattern behind a flagged line and fix every instance on every surface (emails, site, deck) in the same pass.
8. **Every rule ships with a Valid and an Invalid example,** the invalid one quoted from the line that caused it, plus one line of reasoning.
9. **Patch-on-patch stop.** Two patch-induced failures in a row means stop. Ask "can this line ever be true from these inputs?" before a third patch.
10. **Keep the live rule set small.** When a rule replaces another, carry over its still-correct details, then delete the old one from the file the drafter reads. History goes in a changelog.
11. **Fix once, then freeze.** The ask, the offer line, the structure and segment names are chosen once and copied by script, never retyped or re-varied per draft. Changes happen in the source, not in a draft.
12. **Find the copied source before blaming the copier.** When a drafter gets it wrong, check what it read. Often it is your own file.
13. **Honesty gate.** "What I see at most X" needs real research. "Who I talk to" or "our clients" needs real conversations. Until then the line is false.
14. **Naming the goal is not a promise.** Cut a line as an outcome promise only if it states a number, a rate, a date for a result, or a guarantee.
15. **Don't argue with a critic the reader never met.** After a correction, the next draft tends to defend itself ("this does not repeat your website back to you"). A reader who never saw the old version reads that as noise.
16. **Report reversals,** not just survivors, so dead ends aren't proposed again.

## Valid and Invalid

- Valid: "Writing because you're hiring your first salesperson. Cold email can be running, with replies coming in, before they start." Reaction: "Fair, that's timely."
- Invalid: "Noticed your About page names you as founder of Acme. That matches what I see at most agencies like yours." Reaction: "You sent my own bio back to me."
- Valid: "So meetings show up on your calendar." (names the goal)
- Invalid: "Ten meetings a month, guaranteed." (a number and a guarantee)
- Valid rule change: one rule replaced in place, old one deleted, its correct details carried over.
- Invalid: a third patch on a line that has failed twice from patches.

## Output

Root cause (if any), outside evidence, rendered examples with recipient reactions, new or changed rules with Valid, Invalid and reasoning, sweep results, what was reversed, and which file in your one source changed.

Related: `cold-email-first-touch`, `fix-the-generator`, `single-source-of-truth`.
