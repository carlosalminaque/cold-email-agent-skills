---
name: reply-handling
description: "Use when building, testing or operating an AI system that sorts and drafts responses to cold email replies, and when a real prospect reply is waiting for a human's approval. Covers reply categories and which may auto-send, check-and-redraft instead of editing model output, testing against a fixed case set, finding disagreeing instructions when results flip, and flagging a waiting reply so it gets answered fast."
---

# Reply handling

Needs: none

Replies are where a cold email program is won or lost, and where an AI drafter can do the most damage. The design goal: fast answers to the easy replies, nothing risky sent without a human, and a human who can approve in seconds.

## Categories

Sort every reply before drafting. A working set:

| Category | Default |
|---|---|
| Out of office | No reply; reschedule the next step after the return date |
| Unsubscribe / stop / remove me | No reply; suppress everywhere at once |
| Bounce or delivery failure | No reply; mark the address bad |
| Auto-response from a company system | No reply |
| Not interested | Optional short close; never a counter-pitch |
| Information request answered by published facts | Can auto-send once tested |
| Interested / wants a meeting | Human approves |
| Price negotiation, commission, contract terms | Human approves, always |
| Hostile | Human, always |
| Anything the rules don't cover | Human, with the reason |

Decide which categories may auto-send in one place, and have every surface that describes it (dashboards, help text) render from that same setting.

## The rules live in one source

The drafter, the grader and any code check all read the same rule file (see `single-source-of-truth`). When a test failure shows a rule problem, change the source first, then rerun. Never patch the drafting prompt so one case passes.

## Never edit the model's text afterwards

Don't fix a draft with regex, string replacement or appended lines. It produces broken sentences. Use check-and-redraft instead:

1. a deterministic check flags a rule break (a price where none is allowed, a missing sign-off, a banned phrase);
2. the draft is redrafted once, with the specific problem stated;
3. a second failure holds the reply for the human, with the reason.

The check never edits text.

## Testing

- Keep a fixed set of made-up replies covering every category plus multi-turn threads. Run every candidate change against it before shipping.
- It tests rule compliance, not persuasion. A perfect score says nothing about whether replies win meetings. The business signal is real replies and meetings.
- Hard gates, must be zero: wrong auto-sends and missed unsubscribes. For auto-send categories also zero: invented policy, wrong facts.
- For held replies (a human edits them anyway), ship if the candidate is no worse than the live version on the same cases.
- **If a case passes in one run and fails the next, stop patching.** The cause is almost always two instructions disagreeing: rules vs prompt, drafter vs grader, grader vs code check. Find the pair and resolve it in the source.
- Hold a run lock. Two runs over the same cases double the cost.

## A reply waiting on a human

The moment a real reply needs approval, send it as its own message, never inside a status report:

```
REPLY WAITING ON YOU: <Name>, <Company>
They wrote (<time>): "<their words>"
Waiting: <how long>

Proposed reply:
<exact text>

New in this reply: <any fact or promise not already in the source, or "nothing new">
Say yes and I send it.
```

- Nothing after "Say yes and I send it." Research, call notes and explanations wait until after the send.
- Confirm it is real first (open the thread). A bounce or auto-responder is not a waiting reply.
- Do the research before the message: read their site and answer in their terms; if they name a second company, read that one too.
- If they corrected an assumption in their last reply, the new draft must not repeat it.
- Practice the send path ahead of time. After a yes, sending should take seconds, then read the sent message back.

## Valid and Invalid

- Valid: a deterministic check finds a price in a reply to "what's this?", the draft is redrafted once without it, passes, and sends.
- Invalid: code strips the price sentence out of the draft, leaving "Commission would be I take half...".
- Valid: a message that starts "REPLY WAITING ON YOU" and holds only the reply.
- Invalid: the same reply as the second paragraph of a status update.

## Before and after

- Before: an interested reply sat for four hours because it was buried at the top of a routine report.
- After: waiting replies arrive as their own fixed-shape message, and the approved send takes under a minute.
