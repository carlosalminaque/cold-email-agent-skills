---
name: approved-reply-send
description: "Use when a real prospect reply is waiting for a human to approve the answer, or when the human says yes to a proposed reply. Flags the waiting reply in its own short message so it cannot be missed, checks the draft body and especially the closing line, sends within minutes of the yes using the exact approved text, and reads the sent copy back from the mailbox before reporting."
---

# Approved reply send

Needs: browser control

A warm reply goes cold fast. The usual way it gets lost is not a bad draft but a buried one: the waiting reply sits at the bottom of a long status report and nobody sees it for a day. The second way is a closing line that asks the prospect something they just answered, or pushes a call they never asked for. The third is "sent" reported from a button click, when the email never left. This skill handles all three.

## When

- A real prospect reply needs a human's yes.
- The human says "send it" or approves a proposed reply.

## Part 1: flag it

1. Confirm it is real: open the thread. A test, a bounce or an auto-responder is not a waiting reply.
   - Also search the sending mailbox's Sent folder for the prospect. A reply sent by hand outside the sending tool leaves the thread looking unanswered. Never flag a reply that already went out.
   - A message that asks nothing and only restates what is settled (for example, confirming a time already booked) is not waiting. Leave it answered and draft nothing.
2. Do the research first. Read the prospect's home, services, about and case-study pages, plus pricing if it is published, and your own knowledge base. Check anything the reply links to (for a calendar link, what it opens and the soonest slot).
3. Send the flag as its own message, before any other work, in this shape and nothing else:

```
REPLY WAITING ON YOU: <name>, <company>
They wrote (<time>): "<their words>"
Waiting: <how long>
Read: <each page and source by name; name any page not read and why>
Reviewed: <how many review rounds, and that the last found nothing>

Proposed reply:
<the exact text>

New in this reply: <any fact, term or promise not already on record, or "nothing new">
Say yes and I send it.
```

Nothing after "Say yes". The one exception: a fact that changes whether they should say yes goes in one line just above it.

## Part 2: check the draft

The body:

- Answer in the prospect's own terms. If their message corrects an assumption ("actually..."), use their version everywhere.
- Lead with the direct answer, then apply it to their case. Answer every question asked.
- No greeting or sign-off inside a live thread. Nothing the thread already said.
- Every fact comes from your knowledge base, the thread or their site. Anything else goes on the "New in this reply" line, because sending it makes it a commitment.
- Write down in one line what they are really asking and what they will worry about next, then answer that, not only the literal words. Put that note on its own "Read:" line in the flag; a reply without it is unfinished.
- Every cost the reply mentions carries its current number and the volume it assumes, never "at cost" alone. A figure from earlier in the thread wins only if it named its volume; otherwise re-read the live calculator or price list.
- If they quote a price benchmark, work out your total cost per outcome (fees plus tools, divided by outcomes) at a realistic volume and put it on one line above the ask when it does not beat theirs. Never say yes to "can you match or beat X" unless it does.
- Open every link before including it and check that its prices and terms do not contradict the thread. If they conflict, leave the link out. Never write "we agreed" unless they said yes in words.
- Review loop on every reply before the human sees it: a clean-context reviewer checks the exact text against the thread, the facts and the prospect's site. Fix what it finds, then use a new reviewer on the fixed text. Repeat until a round finds nothing; never stop at one round.

The closing line. Read the thread as the prospect, then the last line:

1. It fits where they are. It never asks for setup work before they have chosen you.
2. It never proposes a call. If they ask for one, a link on its own is not the answer: name two specific times, say how long the call is, and give one way to confirm (for example, reply with the time that suits). Each time is open on the live calendar, inside the hours the person taking the call has set, far enough after the send for them to prepare (your minimum lead time, for example two hours), and written in the prospect's time zone and yours. If no time is left today, offer the next business day and say so. If they named a time that is open and inside those hours, accept it in one line; if it is outside, offer the nearest two inside and say why. A booking link may follow only as the way to pick a different time, after you have opened it and checked it.
3. It never asks back what they just said, and never repeats an offer or question from your own last message that they skipped. Read your last sent reply first; drop a skipped offer or act on it. Test: could they answer "I just told you that"?
4. It asks or offers something real. "Does that help?" is empty.

Best closes, in order: offer one concrete next thing as a yes or no; check the answer to their question; ask one new, easy question.

## Part 3: send and read back

1. After the yes, send first. Answer anything else in the message after. If the reply offered times, recheck each against now plus the minimum lead time and the live calendar just before sending; if one lapsed, propose new times and get a new yes.
2. Send the exact approved text. If one word must change, show it and get a new yes.
3. "Sending in progress" is not proof. Reload the thread and read the sent copy and its time.
4. Check whether the prospect already answered.
5. Report in two lines as its own message: who, time sent, route, any answer since. Then the notes.
6. If the send went around the normal path, fix the record so it does not show as pending.
7. If a send times out or errors while the draft still shows pending, nothing is proven: read the sent thread first and never fire a second send blind. If one send route refuses a held or edited draft, use the other.
8. A correction to one draft is a rule for every draft. In the same turn record it wherever replies are written (the knowledge base rules, this skill, your messaging notes), not only in the automation prompt. The same applies when you find your own mistake.

## Valid and Invalid

- Valid closing: "Want me to pull a short sample of the companies I'd contact for you, so you can judge the list yourself?"
- Invalid closing: "Worth a 15-minute call to go through it?" when they never asked for a call.
- Valid answer to "when are you free?": "Tomorrow at 11 AM or 2 PM Eastern (8 AM or 11 AM in your time zone) works, for 15 minutes. Reply with the one that suits you and I'll send the invite."
- Invalid answer to the same: "Happy to. Grab any time that works for you here: [link]".
- Valid report: "Sent to the prospect at 10:42 through the inbox. Read back from the thread. No answer yet."
- Invalid report: "Clicked Send, done."
- Invalid flag: the right shape, followed by three paragraphs of research notes.
