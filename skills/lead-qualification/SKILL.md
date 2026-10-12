---
name: lead-qualification
description: Use when sourcing or qualifying B2B companies for cold outreach, or running a long sourcing run. Works in bounded waves with a checkpoint after each, runs cheap checks first (dedupe, address, fit), records evidence per lead, gates on a verified person-specific address, and checks country rules before import. Who is in scope is your own ideal customer profile, read live from your one source.
---

# Lead qualification

Padding a list to a round number fills it with companies that never fit. Long runs that die halfway lose everything that wasn't written down. A shared inbox that "qualified" wastes a whole sequence on nobody. This is the method for building a short list of real, verifiable prospects. The criteria, meaning your ideal customer profile, size bands, countries and exclusions, are yours and live in your one source. This skill never restates them.

## When

- Sourcing new companies or people for outreach.
- Rechecking companies held as "not yet decided".
- Any run long enough to stop partway.

## Steps

1. **Read your criteria live** from your one source at the start of every run. If the read fails or looks stale, stop. Do not gate on a remembered value or your own judgment.
2. **Work in waves of about 8 to 10 candidates.** After each wave, re-read your records, report counts (qualified, rejected, pending), and write a checkpoint a fresh run could resume from. If a run stops, report the last checkpoint. Never claim to still be working.
3. **Gates in order, cheapest first:**
   0. **Dedupe.** Check your records and every campaign in your sending tool, by domain and by person. Already present: stop, report where, spend nothing.
   1. **Person-specific address.** Find and verify the reader's own mailbox. A shared inbox (info@, hello@) disqualifies at sourcing. Use your lookup tools in a fixed order and record which one found each address.
   2. **Basic fit.** Country, size, business type, per your one source.
   3. **Proof the business is real.** Customers, case studies, funding or other traction your criteria require. Search news before rejecting on this.
   4. **Core offer.** Exclude competitors only on literal quotes from their own pages, never on one keyword.
   5. **Economic fit**: the deal size your one source sets.
   6. **Buyer.** A named person whose published title matches your buyer role. Never infer duties from a title.
   7. **Signals.** Record dated triggers and their source. A missing signal lowers priority. It never disqualifies on its own.
4. **Evidence per lead.** Every gate fact carries its source and the date checked. A fact from one secondary source is "unverified, single source" and cannot decide a verdict. Close calls get a human spot-check before a final verdict.
5. **Verdicts.** `Qualified`, `Rejected` (with reason), `Not yet decided` (with what is missing, the source to check, and a recheck date). Write each row as it is evaluated, not at the end.
6. **Enrich only qualified rows,** and never invent a missing field. A tool that is down means a blank field and a flag.
7. **Country compliance before import.** Each country has its own cold email rules (for example CASL in Canada, PECR in the UK, the Spam Act in Australia). Record whatever evidence your rules require per lead, such as where the address was published. Every send carries sender identity and a working opt-out.
8. **Hand over.** Qualified rows go to `campaign-angles` or `campaign-staging`. Sourcing never authorizes sending.

## Valid and Invalid

- Valid: "Wave 3: 9 checked. 2 already in a campaign (skipped, no spend), 3 rejected (shared inbox only), 1 rejected (no client proof, news searched), 3 qualified with verified named addresses, sources dated. Checkpoint written."
- Invalid: "Found 50 qualified leads." (no sources, no addresses verified, no checkpoint)
- Invalid: "Rejected: their site mentions outbound." (one keyword, no quote)
- Invalid: qualifying a company on info@ and planning to "find the person later".
