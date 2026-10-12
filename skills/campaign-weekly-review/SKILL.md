---
name: campaign-weekly-review
description: Use once a cold email campaign has been sending for at least a few days, roughly once a week per live campaign, or when someone asks how a campaign is doing. Runs a deliverability check, a reply-category review with a positive-reply rate, and a short retro, then writes one dated note, so drift is caught before it is loud.
---

# Campaign weekly review

Without a recurring check, problems surface only when someone happens to ask or something breaks loudly: a domain on a blocklist for days, a reply category creeping up, an angle quietly dead. A short weekly pass catches drift early. Daily is too often: small campaigns produce noise day to day, and reading noise leads to bad changes.

## When

- A campaign has been sending for at least a few days.
- About once a week per live campaign.
- When someone asks "how's the campaign doing?"
- Not before launch, and not in the first day or two. A thin read is worse than none.

## Steps

1. **Deliverability.** Run your deliverability audit (see `deliverability-audit`) on the campaign's actual sending domains and inboxes: authentication records, inbox health in the sending tool, blocklists, and a placement test if you have one. Run it even when nothing seems wrong. That is the point of a recurring check.
2. **Replies by category.** Pull counts since the last review from the system that actually holds replies (the sending tool's inbox, not a summary view). Use your own categories, for example: interested, meeting request, information request, not interested, wrong person, out of office, unsubscribe, bounce.
3. **Rates.** Report:
   - reply rate = real replies / real sends;
   - positive-reply rate = (interested + meeting request) / real sends;
   - the change since last week, if there was a last week.

   Use the categories already assigned. Don't re-judge replies here. With zero sends, write "N/A (0 sends)", not "0%". Flag any rate built on too few sends (see `outreach-experiments`).
4. **Short retro.** Three plain questions:
   - Did anything surprising happen (bounce spike, spam placement, an angle much stronger or weaker)?
   - Is there a gotcha worth logging where your team keeps them?
   - Is there a decision for a human (pause an angle, try the next one from `campaign-angles`, change volume)?
5. **Write it down.** One dated note in your running to-do or log: what was checked, what changed, actions taken or recommended. A quiet week gets one line, "checked, nothing new", which beats silence.

## Valid and Invalid

- Valid: "Week of review: domains clean, no blocklist hits. 210 sends, 9 replies (4.3%), 2 positive (1.0%), up from 0.6%. Sample still small. One out-of-office spike, no action. Logged."
- Invalid: "Looks fine, replies are coming in." (no sources, no rates, no note)
- Invalid: "Positive rate fell from 2% to 0% this week, pausing the angle." (on 30 sends, a one-reply swing)
- Invalid: skipping deliverability because the reply numbers looked normal.

## Output

The deliverability result, the category table, the two rates with sample size, retro answers, and the line written to your log.
