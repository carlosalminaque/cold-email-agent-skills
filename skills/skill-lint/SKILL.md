---
name: skill-lint
description: Use before writing, editing or delivering any SKILL.md, and before shipping a batch of skill edits. Runs check_skill.py on each skill (description length and angle brackets, name format), which blocks delivery on failure, then runs lint_skills.py on the whole skills folder to flag oversized files, copied facts, duplicated rules, history piled into the body, broken reference pointers and names of retired skills.
---

# Skill lint

Skills rot in predictable ways. A description grows past the platform limit, or quotes a template with angle brackets that the loader reads as a tag, and the skill silently fails to save. Over months, the same rule gets pasted into three skills and drifts, a price or setting gets copied in and goes stale, incident stories pile up in the body until the rules are hard to find, and pointers to merged skills stop working. Two scripts catch all of this mechanically, so nobody has to remember to look.

## When

- Before writing or delivering any SKILL.md, new or edited.
- Before shipping a batch of skill edits.
- On a regular schedule over the whole skills folder.

## Steps

1. **Check each skill before delivery.** This one blocks.

   `python3 scripts/check_skill.py path/to/skill-folder` (also takes a SKILL.md or a zipped .skill file)

   It checks: frontmatter exists; `name` is lowercase letters, digits and hyphens, at most 64 characters, without reserved words; `description` is present, at most 1024 characters, and has no angle brackets. Deliver only on PASS.

2. **On a length failure, trim the description, not the meaning.** Cut in this order: dated changelog fragments, long lists of trigger phrases (keep two or three), clauses that explain why rather than when. If scope-defining text must go, move it into the body under a Scope heading and leave a short pointer.

3. **Lint the whole folder.** This one reports; it does not block.

   `python3 scripts/lint_skills.py path/to/skills [--max-kb 15] [--facts facts.txt] [--retired retired.txt] [--strict]`

   - **SIZE:** SKILL.md over the limit with no `references/` folder. Keep rules as short lines; move reasoning and stories to `references/`.
   - **FACT:** a line matches a pattern from your facts file. Point to the fact's one source instead of copying it.
   - **DUP:** the same rule line in two or more skills. Keep it in one, point to it from the other.
   - **HISTORY:** five or more dated incident markers in the body. Move the stories out.
   - **REF:** a pointer to a reference file that is missing, or that lives in another skill without naming it.
   - **RETIRED:** a skill names one listed in your retired file. Update the pointer to the new owner.

4. **Supply your own lists.** Both files are optional and plain text.
   - `facts.txt`: one regex per line, optionally a tab and a label. Use it for prices, DNS values, limits, anything that must live in exactly one place.
   - `retired.txt`: one `old-name=new-name` per line. Add a line every time you merge or remove a skill.

5. **Fix flags in batches.** Report the count, fix the worst first. Use `--strict` in CI to fail the build on any flag.

## Valid and Invalid

- Valid: description says "ends with a count line"; the exact template with its placeholders lives in the body.
- Invalid: a description that quotes `DONE: <n> items`. Under the length limit, still refused.
- Valid: `retired.txt` gains `old-review=weekly-review` in the same commit that merges the two skills.
- Invalid: the price copied into four skills "so the agent sees it", then changed in one.
- Valid: lint shows 3 DUP flags; one rule is kept in its owner skill and the other two skills point to it.

## Before and after

- Before: a skill failed to save twice in one week, once on length and once on a bracket, and each time the human found it.
- After: the check runs before every delivery and the folder lint runs on a schedule; neither failure reached the human again.
