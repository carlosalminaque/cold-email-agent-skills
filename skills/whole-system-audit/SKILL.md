---
name: whole-system-audit
description: "Use when an agent-run operation keeps breaking and the ask is to fix it fundamentally, harden it, or check every part against outside best practice. Read-only audit that tests whether breakage comes from too many moving parts, tallies past failures by component and by fix type, and ends in a keep/merge/delete plan with part counts before and after, a home for every scheduled job, and a reversible migration order. Not for one live incident or for drift in skills and memory."
---

# Whole-system audit

Needs: local shell, web access

When a small, agent-run operation feels like it is always breaking, the useful answer is rarely "patch each part". Chronic breakage usually comes from too many moving parts: several agents passing work to each other, homegrown plumbing, guards stacked on guards, production jobs on a personal machine. Every fix that adds a guard adds one more thing that can break.

This audit tests that hypothesis with evidence and outside sources, then ends in a plan that lowers the part count. If the evidence says the hypothesis is wrong, say so and follow the evidence.

Hand off narrower requests: one live failure goes to a troubleshooting method; contradictions in skills, memory or docs go to a context audit.

## Step 0: show the plan, get a yes

Before starting, send a short plan: the passes (inventory, failure tally, outside best practice, plan, second opinion), the scale (one session, one document), that it is read-only, and the one decision only the owner can make: is retiring major parts (an agent, a relay, a queue, a machine) on the table? If not, the audit can only rank patches. Say so.

## Step 1: open the document first

Create the report with one empty section each: Verdict, Inventory (a diagram of components and where each runs), Failure tally, Best-practice check, Keep / merge / delete, Migration order, Second opinion, Sources. Fill one section at a time as results arrive.

## Step 2: three read-only passes, in parallel

Run them as parallel sub-agents so raw files stay out of the main context. Give each the current live facts first.

1. **Inventory.** Every component: what it does, its layer (the path that earns or sends, data store, site, coordination, monitoring, backup), where it runs, who or what runs it, what it depends on, and the file that proves it. Include every scheduled job and its cadence. Tag each row VERIFIED or UNCONFIRMED.
2. **Failure tally.** Read the last 7 to 14 days of retros, incident notes and decision records. Classify each failure by component and by fix type: new guard or code, new rule, deletion, or log only. A high share of "new guard" is the signature of a complexity spiral. List separately every failure that touched a real customer, prospect or send; those carry most of the weight. Say where the hypothesis is wrong.
3. **Outside best practice.** Open real pages, not search snippets, and date them. Cover multi-agent versus single-agent reliability research, the official docs for each platform in the stack, and how to run agent jobs unattended in the cloud. For every mechanism you might propose, read its own limits and write them next to the proposal.

Never search a huge output folder recursively; list named folders instead.

## Step 3: the plan, in this order

- **Fence the critical path.** The path that touches customers or money runs in the cloud with no dependence on a laptop or an interactive agent session. Harden it with the platform's own tools (error handlers, retry with backoff, idempotent sends, a daily canary) before writing anything custom.
- **Keep, merge or delete each component.** Every coordination part must justify itself against the simplest setup that could work (for example one coordinator plus one executor). Show the part count before and after.
- **Give every scheduled job a home** (database cron, CI scheduler, workflow tool, or stays local because it needs a signed-in desktop), with the reason and the deciding limit.
- **Set a complexity budget.** A fix either deletes a part or adds a test. A new guard ships only if it replaces an existing one.
- **Order the migration** so each step is small, reversible and has a stated proof that it worked. The critical path goes first; new features go last.

Each recommendation names what it removes. A rule people must remember is a stopgap and is labelled one. Tag every claim VERIFIED (read in a file, a live system or a fetched page) or UNCONFIRMED, and list open gaps without being asked.

## Step 4: second opinion, then close

Give the draft plan to a fresh sub-agent with no context: what would it cut, what is missing, what is wrong? Revise, and record in the report what changed. Then copy every high item onto the running to-do list with an owner, write a decision record, send the verdict in a few lines, and ask only the decisions that belong to the owner.

## Valid and Invalid

Valid: "Failure tally, 14 days: 41 failures, 29 in coordination (queue, relay, session status), 3 on the send path. 22 of 41 fixes added a guard. Plan: retire the relay and the status board, move 6 scheduled jobs to the database's cron. Parts 23 to 14. Step 1, the send-path canary, proves itself by one green run a day for a week."

Invalid: "Audited all 23 components and wrote a hardening patch for each one." (No tally, no part count, no test of the too-many-parts hypothesis, and 23 new guards.)
