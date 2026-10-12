---
name: pre-send-list-check
description: Use right before a lead list is uploaded to a sending tool. Checks the exact final list for verification status, whether each email's domain belongs to the company on the record, duplicates, catch-all and unknown results, junk in personalization fields, and anyone who opted out or is on a do-not-contact list. Data hygiene only; it does not re-score whether a lead is a good fit.
---

# Pre-send list check

A company can be a perfect fit and still have a dead address, a duplicate row, or an address that verifies fine but belongs to a different company. Qualification and hygiene are different jobs; this is hygiene.

## When

Right before the upload, after the copy is approved. Run it on the real final file, not an earlier draft: rows change between sourcing and sending.

## Steps

1. **Freeze the batch.** Take the exact file about to be uploaded. Record its row count and a hash.

2. **Verify every address** with an email verification service. Check your credit balance first so a large batch doesn't stop halfway silently.
   - Valid: continue to step 3.
   - Invalid: block, with the reason.
   - Catch-all or unknown: flag, don't block. Report the share of the batch, so the risk is visible.

   If the verification service is down, say so. Never send unverified without an explicit decision.

3. **Match the domain to the company.** Verification proves a mailbox exists, not that it belongs to the company on the record. For every surviving row, the email's domain must be the company's own domain, or a domain confirmed (on the company's own site) to belong to the same company. Otherwise block the row. A real case: an address verified as deliverable belonged to a completely unrelated business.

4. **Duplicates.** One row per email. Flag several contacts at the same domain and decide on purpose whether to send to more than one.

5. **Suppression.** Remove anyone who unsubscribed, asked to stop, bounced before or is on a do-not-contact list, across every past campaign and inbox. Remove your own and your team's addresses and test addresses.

6. **Personalization fields.** Every field the template fills must be present and clean. Flag only junk, never "fix" it with a rule: empty, a domain or URL, the words "logo" or "client", a `|` or ` - ` separator, more than five words, a legal suffix alone. Junk goes back to sourcing.

7. **Report and gate.**

   ```
   LIST CHECK <file> <rows in> -> <rows clear>
   Blocked: <n invalid> invalid, <n> domain mismatch, <n> suppressed, <n> duplicate
   Flagged: <n> catch-all/unknown (<share>%), <n> personalization junk
   Hash: <hash of the cleared file>
   ```

   The upload uses only the cleared file, and its hash must match the report.

## Valid and Invalid

- Valid: "120 in, 104 clear. Blocked: 6 invalid, 2 domain mismatch, 5 suppressed, 3 duplicate. Flagged: 11 catch-all (11%). Uploaded file hash matches."
- Invalid: "Ran verification, all good" with no domain match and no suppression pass.

## Before and after

- Before: a list passed verification and an address belonging to an unrelated company was about to be sent a message about someone else's business.
- After: every row's domain is matched to its company before upload, and mismatches are blocked.
