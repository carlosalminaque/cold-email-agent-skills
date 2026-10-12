---
name: coding-agent-prompts
description: "Use whenever drafting a prompt that a coding agent (Codex, Claude Code, or any agent that runs commands and edits files) will execute, or setting up how a long agent run keeps going across turns. Covers scope given as checkable rules rather than counts, end-of-turn reports with honest markers, keep-going loops and how to prove one actually works, proof of real runs instead of syntax checks, stating every allowance and limit, keeping reloaded files small, gate order for builds that need review, and prompt titles that do not confuse the agent about who it is."
---

# Coding agent prompts

Coding agents follow prompts literally and stop when something required is missing. Each rule below closes a gap that made a real run stall, fake progress, or cut valid work.

## 1. Give the rule, never a count, as the scope

The agent reads any number in the prompt as a requirement. A count copied from an old note becomes a target it will cut valid items to hit, or stall trying to reconcile.

- Define the set by rules the agent can check. The count is whatever the rules produce.
- Ask for the final count plus one line per excluded item naming the rule it failed, written to a file.
- Never copy a count from a to-do or old report as current. Check it live, or label it "last seen N on date, not a target".
- Say what to do with unclear items (exclude and say why) so they are not a reason to stop.
- Valid: "The import file holds every lead that is approved, has an address and passes the duplicate check. Report the count and each exclusion with its rule."
- Invalid: "Re-check duplicates for the import file (88)."

## 2. End-of-turn report and honest markers

- Require a short report every turn: done of target, held count, current step, next step, then a marker.
- Give a marker for every honest outcome: DONE, CONTINUING, NOT RUNNING. With only one marker available the agent either stalls or prints a false one.
- Never tell the agent to stay silent. "Only reply when finished" produces turns that end with no report.
- Valid: "Done so far: 22 of 60. Next: wave 3. JOB CONTINUING"
- Invalid: "Don't send me progress updates."

## 3. Turns end; plan for it

A turn ends after a time limit or when the agent messages the person. No wording makes one turn run forever. For multi-turn work, the first prompt includes the keep-going setup (section 4). Never tell the agent to pause when low on context: agents that compact should keep going, with the handoff file as their memory, updated every wave.

- Valid: "Keep HANDOFF.md current after every wave."
- Invalid: "If you run low on room, checkpoint and pause."

## 4. Keep-going loops: registered is not running, running is not working

- Use one resume method per job (the app's scheduled task, or an OS scheduled task that starts a fresh run), never two on the same files. Name any older loop on the same files and have it disabled and read back.
- Save the complete instructions as `PROMPT.md` beside the handoff file. A fresh run never saw the chat.
- Only the wrapper script keeps two runs apart (a lock). Never tell a run to "exit if another run is working": it sees its own task and process and exits.
- OS tasks often default to "AC power only" with no wake. Set start on battery, do not stop on battery, start when available, wake to run, and read the settings back.
- Before calling a loop handled, wait one interval and read three things: the loop log (a run started), the run's last message (anything like "another run is active" or "no files touched" means nothing happened), and the job's files (changed after the run started). A run under two minutes usually did nothing.
- Valid: "Run at 05:55 edited the builder and wrote the scope file."
- Invalid: "The loop fired at 05:16, 05:25 and 05:40" read from the log alone.

## 5. Proof means a real run

A parse check or dry probe is not proof. Every prompt that changes a script requires a real run of each changed script in the target runtime and version, plus one labelled fixture write through the changed path, read back. The report says per script what ran and what it wrote.

- Valid: "Ran under the production shell version, wrote fixture row TEST_FIXTURE, read it back."
- Invalid: "Syntax and dry-route checks passed."

## 6. State every allowance and limit

The agent stops when an approval is missing. Name every paid service or tool it may use and the limit for each. List tools it does not have and the fallback, and keep known limits in one table it reads before starting.

## 7. Save context: scripts print verdicts, not data

Pulling raw records into the conversation fills context in one wave. Have local scripts print only verdicts (CLEAR, DUPLICATE), counts, ids and pass or fail, and keep per-item notes in files.

## 8. Titles and where to paste

Never put an agent's name in a prompt title; an agent that reads another agent's name may start building for that agent. Title by outcome and say outside the copy block where to paste it.

- Valid: title "IMPORT FILE REBUILD", with "paste into the build session" above the block.
- Invalid: title "CODEX AUTO-LOOP" pasted into a different agent.

## 9. Long builds with a reviewer

- Lock scope: "this job ONLY until its reviewer approval exists".
- Spell out gate order: build the whole package, live proofs before publishing steps, reviewer approval last and tied to the package's exact hash. A changed package needs a new approval.
- Say "building" only when a log line or job file changed in the last ten minutes.
- Keep reloaded files small (a prompt file under about 20 KB, a handoff under about 15 KB, history archived beside it). Shorten by cutting history, never by deleting spaces, and replace superseded rules in place.
- For exact copy, give approved wording and require a scripted whole-page diff against the live page listing every difference.
- If the agent's own approval layer refuses a write, do not have another agent make it. Ask for smaller readable edits, or report it.
- Approvals come only from the person. An agent never writes an approval into a file for another agent to find.
