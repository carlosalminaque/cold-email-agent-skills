---
name: agent-permission-guards
description: "Use when making a Claude Code agent ask for permission less, running headless workers (claude -p), setting up auto mode rules, or stopping agents from forging approvals or touching protected files. Explains which control enforces what, what each one does not cover, how to test a guard, and traps found in practice."
---

# Agent permission guards

Needs: Claude Code

Letting agents ask less without letting them approve themselves.

## Pick the control that actually enforces it

| Goal | Use | What it does not cover |
|---|---|---|
| Fewer prompts for routine tools | `permissions.allow` | In auto mode, broad rules such as `Bash(*)` or wildcarded interpreters are suspended; narrow rules still skip the classifier |
| A path agents must never change | `permissions.deny` or `--disallowedTools "Edit(path/**)"` on the runner | Covers the built-in file tools, file commands Claude Code recognizes in the shell (`sed`, `tee`, ...) and redirect targets. Does not cover a script that opens the file itself (`python -c`, `node -e`). Use `Edit(...)`: `Write(...)` path rules are accepted but never consulted |
| Every process, scripts included | The sandbox (OS-level) | Only what the sandbox is configured to restrict |
| Judging content (a forged approval, an unapproved request) | A PreToolUse hook that exits 2 to block | Only the tools its matcher names; it reads what is being written, nothing else does |
| Risky outside actions (deploys, pushes, external writes) | `autoMode` `allow` / `soft_deny` / `hard_deny` | Read only from `~/.claude/settings.json`, managed settings and `--settings`, never from the project's `.claude/settings*.json`. Calls already approved by an allow rule never reach it |

## Rules that held up

- Put worker guards on the runner (`--settings` with inline hooks, `--disallowedTools`), not in user settings. Otherwise they also block the people and agents who legitimately write those files.
- An approval must be something the agent cannot write itself: a person's chat message, or a file only a different, trusted writer can change. Block agents from editing approval files and approval fields, and remember a deny rule alone does not stop a script from writing them; pair it with a hook on the shell tool or the sandbox.
- Tools passed in `--allowedTools` are pre-approved, so auto mode rules never see those calls. Keep that list narrow.
- An agent may be refused when it edits its own settings file, as self-modification. Have the person or a different agent make that change.
- Keep `"$defaults"` in every `autoMode` list you set, or you replace the built-in rules instead of adding to them (for `soft_deny` that drops force-push and production-deploy blocks).
- In one test (Claude Code v2.1.303) auto mode did not review file writes inside the working directory. Do not count on the classifier to protect files in the project; use deny rules, hooks or the sandbox.

## Test before trusting

1. Back up the runner config, then change it.
2. Run a real worker against cases that must pass and cases that must be blocked. Record the block reason for each.
3. Include every write route in the blocked cases: the edit tool, a shell redirect, `sed -i`, and a script that opens the file itself.
4. Have an agent that has not seen the guard's code write attack cases in batches of 10. Fix and repeat until a batch has 0 misses. Also run harmless cases that must still pass.
5. If anything misses, roll back.

`claude auto-mode config` showing a rule only proves it loaded, not that it is enforced. `claude auto-mode critique` reviews wording, not behavior.

## Valid and Invalid

Valid: "Approval files are protected by `--disallowedTools \"Edit(approvals/**)\"` plus a PreToolUse hook on Bash that blocks any command naming `approvals/`. A batch of 10 unseen attack cases, including `python -c` writes, had 0 misses; 6 harmless cases passed."

Invalid: "Added `Write(approvals/**)` to the deny list and `claude auto-mode config` shows it, so agents can't forge approvals." (Write path rules are never consulted, scripts bypass deny rules, and showing in config proves loading, not enforcement.)
