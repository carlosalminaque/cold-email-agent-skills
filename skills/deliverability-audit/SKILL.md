---
name: deliverability-audit
description: Use before a sending domain's first real cold email, weekly while campaigns run, and whenever replies drop, bounces rise, mail lands in spam or a blocklist is suspected. Checks SPF, DKIM and DMARC by DNS lookup, mailbox provider reputation tools, compliance basics (opt-out and postal address), bounce and complaint rates from send records, and gives a first-response order for a live incident.
---

# Deliverability audit

New sending domains have no reputation to fall back on. A broken record or a bounce spike in the first week can do lasting damage. The most common failure is not a missing check, it is a checklist that existed and was never run before launch.

**Hard gate:** the full audit runs and its result is reported before any domain's first real send. If a launch is imminent and the audit hasn't run, say so and get an explicit go or no-go. "It's on the checklist" does not count as run.

## 1. DNS authentication

For each sending domain:

```bash
dig TXT example.com +short                         # SPF: "v=spf1 ..."
dig TXT <selector>._domainkey.example.com +short   # DKIM: selector from your sending tool's setup page
dig TXT _dmarc.example.com +short                  # DMARC: "v=DMARC1; p=..."
```

Flag:

- SPF, DKIM or DMARC missing.
- More than one SPF record on a domain, or an SPF record needing more than 10 DNS lookups. Both make SPF fail at the receiver, silently.
- DKIM or SPF not aligned with the From domain.
- A DMARC policy of `quarantine` or `reject` on a brand-new domain. It can be right (many inbox vendors ship it as their baseline), but confirm alignment is clean first. `p=none` is safer while reputation builds, and is incompatible with BIMI, which needs an enforced policy. Surface that trade-off; don't pick silently.

Write down any deliberate exception (a vendor's standard DMARC policy, say) next to the check, with the source, so the next audit doesn't re-flag it.

## 2. Mailbox provider tools

- Register each sending domain with Google Postmaster Tools, and Microsoft SNDS for sending IPs if you control them. Low volumes may show no data; that is expected, not a pass.
- Check the domains and IPs against the major public blocklists.

## 3. Compliance basics

- Every email carries a working opt-out and a valid physical postal address (required for commercial email under CAN-SPAM in the US; similar rules elsewhere).
- Opt-outs are honored across every campaign and inbox at once, not per campaign.
- Check the current requirements of the large mailbox providers for your volume (Google and Yahoo publish sender guidelines covering authentication, unsubscribe handling and spam-complaint thresholds). Read the live page; the thresholds change.

## 4. Rates, from the send records

Read from what was sent, never from a dashboard summary alone:

- bounce rate per inbox and per domain, and per list source;
- spam complaints where the provider reports them;
- reply rate per inbox: one inbox far below the others usually means that inbox is landing in spam.

Set your own thresholds before launch and write them in the source, for example: pause an inbox above a set bounce rate, pause a list source above a set bounce rate.

## 5. Rendering and format

- Send a test to Gmail, Outlook and a phone. Check plain-text rendering, line breaks and that placeholders filled.
- No images, tracking pixels or link shorteners in a first cold email unless you have tested their effect on placement.

## Incident response, in order

1. **Stop the bleeding.** Pause the affected inbox or campaign. Don't keep sending to measure.
2. **Find the scope.** One inbox, one domain, one list source, or everything? Compare rates across them.
3. **Check what changed** in the last week: DNS, a new list, new copy, a volume increase, a new tracking setting.
4. **Bounce spike:** check the list source first (see `pre-send-list-check`); suppress the bounced addresses everywhere.
5. **Spam placement:** test-send from the affected inbox, check authentication headers in the received message, check blocklists.
6. **Resume slowly,** at lower volume, and watch the same numbers for several days.

## Valid and Invalid

- Valid: "Audit run Monday before launch: SPF/DKIM/DMARC pass and aligned on all four domains; DMARC quarantine with pct tuning is the vendor's baseline (source linked); postal address and opt-out present; test sends land in the inbox in Gmail and Outlook."
- Invalid: "Domains look fine" from the sending tool's green warmup badge.

## Before and after

- Before: a launch went out with none of the checklist run. A later audit found the postal address missing and plain-text rendering broken, both of which the checklist named.
- After: the audit is a launch gate with a written result, not a document someone may read.
