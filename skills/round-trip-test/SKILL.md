---
name: round-trip-test
description: Use when someone needs proof that an email automation works end to end, not just that its code looks right. Sends a real message through the real path to a test inbox you own, gets a real reply back, and records every stage as it happens, including the write-back to the system of record. Use after synthetic tests pass and before trusting a reply or send automation with real prospects.
---

# Round-trip test

A mock proves the logic. It does not prove the live system. Webhooks get pointed at the wrong URL, a credential expires, a timer never fires, a record never gets marked as sent. These faults only show up when a real message travels the real path. A common failure: the email leaves the inbox, the run ends in an error, and the record still says "pending". The next approval then sends the same reply twice. A round-trip test catches that before a prospect does.

## When

- Someone asks "does it actually work?" or "let's test it for real".
- After a synthetic test pass, before real prospects depend on the automation.
- After any change to the send, reply or write-back path.

## Steps

1. **Use test infrastructure you already own.** A test campaign and a test inbox you control, wired to the same webhook, the same classifier, the same draft queue and the same send step as production. Do not build a parallel copy: a copy can pass while production fails.

2. **Re-check the test setup live.** Confirm the test campaign still exists, the test address is still yours, and it still routes through the production path. Setups drift between sessions.

3. **Confirm the safety switches.** Read the live state of anything that can send on its own (auto-send timers, allowed categories). If the test reply will trigger a real automatic send, say so before it happens.

4. **Decide what this run proves.** One draft can test one path. Pick it first: let the timer run and send, or step in and confirm it backs off. You cannot test both on one draft.

5. **Send a real message, then a real reply.** A human or another agent writes the reply from the test inbox through the real mail channel. Never a hand-made webhook POST. Word the reply so it lands in the category you want to test.

6. **Record every stage as it happens:**
   - the trigger firing (execution log);
   - the classification result;
   - the draft record being created;
   - any notification;
   - the send, if one happens.

7. **Check the write-back as its own stage.** After every send, check three things together:
   - the received email in the test inbox;
   - the record marked sent, with a sent time;
   - the notification that says it was sent.

   Any mismatch fails the test. First neutralize the record so nothing can send it again. Then read the execution log for the cause. Then turn off automatic sending for the affected path until a clean re-run proves the fix.

8. **Write it up.** Stage by stage, with evidence for each. What passed, what failed (exact error text), and what is still untested.

## Safety

- Both ends must be yours. Confirm the recipient address and the campaign before every send.
- Never point the test at a real prospect or a campaign with live leads, even briefly.

## Valid and Invalid

- Valid: "Real reply sent from the test inbox at 10:14. Classified as Interested. Draft created. Timer sent it at 10:34. Test inbox received it. Record shows sent at 10:34. Notification posted. Pass."
- Invalid: "POSTed a sample payload to the webhook and got 200. The automation works."
- Valid: "Email arrived, but the record still says pending and the run ended in an error. Fail. Record archived so it cannot be sent again. Automatic sending off for this category until a re-run passes."
- Invalid: "Email arrived, so it passed. The record anomaly is a minor note."
