---
name: campaign-staging
description: Use when qualified leads and approved copy need to go into a sending tool such as Smartlead or Instantly. Decides first whether a new campaign is warranted or the leads belong in an existing one, then configures, imports and verifies the campaign by reading it back, and stops before launch. A human launches.
---

# Campaign staging

Sending tools say "ok" to things they didn't do. An import can return success and attach no leads. A setting can save and then lock in the wrong state once the campaign leaves draft. A new campaign can be created for every batch until nobody can compare anything. Staging means the campaign is configured and every part of it has been read back and checked. Launching is a separate decision that belongs to a human.

## When

- Leads are already sourced and qualified (see `lead-qualification`) and copy is approved.
- If the leads still need sourcing, do that first.
- Never with copy no human has approved.

## Steps

1. **Decide: new campaign or existing one?** A new campaign is warranted only for:
   - a deliberate test of one variable (see `outreach-experiments`);
   - deliverability isolation (new domains or inboxes);
   - a segment or offer that has no campaign yet.

   Not warranted: the batch was sourced later; a copy fix (apply it going forward); more leads for the same segment, offer and copy. "Batch" or "wave" is a tracking label, never a campaign name. If unsure, ask. Never default to a new campaign.
2. **Clean the list right before import** (see `pre-send-list-check`). Approved copy does not mean approved data.
3. **Check overlap.** Compare the batch with every active and draft campaign and with everyone who has already replied. Report each campaign checked and its count. A person who has replied is never a cold first-email lead again.
4. **Set lock-at-creation settings while still draft.** In many tools, plain text, open tracking and click tracking lock once the campaign leaves draft. Set them at creation and read them back.
5. **Load the sequence from your one source.** Each step holds its approved text, copied by script, never retyped.
6. **Threading.** Follow-ups usually stay in the same thread only when their subject is blank. Confirm your tool's behavior with a test send.
7. **Custom fields may be lead-level, not campaign-level.** Writing a field for one campaign can change the same lead in another. Check membership in other campaigns before reusing a lead with different copy.
8. **Attach inboxes and a schedule.** Read back which inboxes, how many, the time zone, days, hours and gap between sends.
9. **Connect reply handling.** Creating a campaign may not subscribe it to your reply webhook or automation (for example in n8n). List the subscriptions and confirm this campaign is on it.
10. **Verify content, not just settings.** Read back and quote step one's subject and body with fields filled for one real lead, and confirm every follow-up step is present. A settings table alone is not a pass.
11. **Read back lead count** after any add. A success response is not proof.
12. **Stop.** Report the campaign as staged with the checks above, and ask a human to launch.

## Rules for live campaigns

- Never resend a first email to fix a settings mistake.
- Never move a lead mid-sequence to a new campaign.
- Later steps of a live campaign may be edited only if no lead has received them yet: pause, edit, resume, read back.

## Valid and Invalid

- Valid: "Added 14 leads to the existing campaign for this segment. Read back: 14 new, 0 already in other campaigns. Plain text on, tracking off, 4 steps, follow-up subjects blank, webhook listed. Staged; ready for your launch."
- Invalid: "Created a new campaign for this week's batch. API returned ok. Launched." (no reason for a new campaign, no read-back, and launched without a human)
- Invalid: "Staged" with only a settings screenshot and no step-one body checked.
