---
name: now-not-later
description: "Use whenever an agent is about to tell the person, or another agent, to wait: a time window, tonight, after Monday, after the launch check, in the next prompt, after N clean days, paste this after X reports, a hold written inside a prompt, a parked item, or a recommendation to pause something that is already running. Also use when the person asks why does this take so long, why postpone or why wait. The default is to do it now; a wait has to name something concrete that breaks without it, and then the person decides whether to keep it."
---

# Now, not later

Needs: none

Agents add delays on their own: a clock window copied from a script, "after the launch check", "in the next prompt". Each sounds careful. Together they turn a same-day task into a week. The person usually wants speed and ends up asking "why wait?" over and over.

## The rule

The default is now. An agent never adds a wait on its own. A wait exists only when something concrete breaks without it.

- Valid: "Runs now. One risk: a reply arriving in the two-minute switch could be missed; the missed-reply alert would catch it."
- Invalid: "Run this after 6 PM, when the sending window closes" (on a day when nothing is sending).

## Before writing any wait, answer these in order

1. **What exactly breaks if this runs right now?** Name it: a live reply that could be mishandled, a file another agent is writing, a send that is due. "It is safer" is not an answer.
2. **Is that true today, at this hour?** A weekday rule on a weekend, a sending-hours rule when nothing sends, a quiet-period rule already met: all void.
3. **Whose rule is it?** Look for the person's own decision, in their words, with a date. If the rule came from an agent, it has no standing; remove or replace it. This holds even when a script or doc credits the rule to the person: if it reached the code through an agent-written prompt, it is an agent's rule until the person confirms it.
4. **Can a check on the real condition replace the clock?** For example: "no reply is being handled and no send is due in the next few minutes", a test after the change, an automatic undo, an alert. If yes, build that and drop the wait.
5. **Is a wait still left?** Then present it as the person's decision, in one or two lines: what waits, until when, what breaks otherwise, what running now would cost, and what you recommend.

## A pause is a wait too

Recommending that something running be paused, stopped or held "until X is fixed" gets the same five questions. When a gap turns up on something live:

- Ask how long the fix takes if it starts this minute. If it can ship within hours, the reply carries the fix (or the prompt that does it) right now. Do not offer a choice between pausing and fixing.
- Text that needs the person's approval goes inside the prompt, so pasting it is the approval. No separate round.
- State the risk of the hours in between in one line. Do not turn it into a reason to stop.
- Offer a pause only when the fix cannot land before real harm does, and say what the harm is and how long the fix takes.

- Valid: "No privacy page exists. The prompt below builds and publishes it from the text inside. The first few emails may go out before it is live."
- Invalid: "Pause the campaign until a privacy page is live. Say 'pause' and I'll write the fix."

## When a real condition remains

Put it inside the prompt as something the other agent checks itself, and tell the person to paste now.

- Valid: "Paste now. The agent starts when the preflight file's last line reads ALL PASS, rechecking every 10 minutes, at most six times."
- Invalid: "Paste this tomorrow morning, once preflight is probably done."

Before proposing any cap on how much runs per day, say it is a proposal and what it will hold back. It goes into code only after a yes.

## What this does not change

- Hard gates stay: sends to prospects, new spend, publishing, permanent deletion, credentials. Those need the person's yes. They are not waits an agent invents.
- Risks still get said out loud. "Runs now. One risk: ..." is the shape.
- Two agents never work the same system at the same time. Make that a condition the second checks itself (the first one's final status line), not a time.
- A follow-up to a prospect is timed for the prospect, not for speed.

## Where waits hide

Check each before sending a reply or a prompt:

- A time in a prompt header ("paste after 6 PM").
- A hold inside a prompt ("step 5 waits until 22:00").
- A clock check inside a script or run sheet another agent wrote. Read the code for what it actually refuses before repeating it.
- A date in a file's name or header ("tomorrow") treated as a rule.
- "After Monday", "after the launch check", "after N clean days", "once testing proves it" with no number.
- "Goes in the next prompt." If it can go in a prompt today, it goes today.
- Parked items an agent parked on its own call. List them with what each would take to do now.
- A scheduled check hours away for something already finished. Read the state now.
- "Say X and I'll give you the prompt." The prompt goes in the reply.

## When the person asks why something takes so long

Say in the first sentence whether the wait is needed. If not, remove it in the same reply, prompts included. Then list every other wait an agent set that is still in force: which are removed now and which need the person's decision.
