---
name: cold-email-first-touch
description: Use when writing, reviewing or launching a B2B cold email sequence - the first email, its follow-ups, or any example email shown to someone. Keeps per-lead personalization to fields that can be checked, keeps the first email short with one low-friction ask and no price, tests changes on rendered emails rather than abstract rules, and checks before launch that every live step matches an approved text.
---

# Cold first email

These are working rules from running cold email for B2B services, not universal laws. Each one exists because the opposite went wrong. Put your own versions in one source (see `single-source-of-truth`) and let the drafter read them from there.

## The first email

1. **Fill in only what can be checked.** Per lead, fill fields a named source shows: the company name as written by the company, the market it sells to in its own words. Anything that needs inference ("you're probably struggling with...") goes in fixed text written once per segment and approved once, where it is true of the whole segment by construction.
2. **Never restate the reader's own page back to them.** "I saw you offer SEO and PPC" tells them nothing they don't know and reads as automated. Open on their situation instead.
3. **One ask, and make it cheap to say yes to.** For example: "Want two sample emails written for your market?" Not a call, not a calendar link.
4. **No price in the first email.** Price appears first in a follow-up. Mentioning cost before the reader cares about the offer gives them a reason to stop reading.
5. **Short.** A working limit: at most 80 words from greeting to sign-off, no sentence over 25 words. Read it aloud once; dropped verbs and noun-stacks show up immediately.
6. **Name the specific market,** never "agencies like yours" or "companies like you".
7. **Don't claim experience you don't have.** "What I see at most SEO agencies I talk to" is false until those conversations have happened.
8. **Naming the goal is not an outcome promise.** "So meetings show up on your calendar" describes the service. "10 meetings a month" promises a number. Only the second is banned.

## Follow-ups

- One first email, then a fixed small number of follow-ups (we use up to three), then stop for that person.
- Keep follow-ups in the same thread. In most sending tools that means a blank subject on follow-up steps; check your tool's behavior with a test send before launch.
- Follow-ups carry the price and the second way to say yes, not a repeat of email one.

## The personalized field is data, not copy

- Use the company name exactly as sourced. Never re-case it or "clean it up" with a rule: companies style their own names on purpose (all lowercase, all caps, run-together words), and a rule that fixes one breaks ten.
- A check on the field flags only junk: empty, a domain, a URL, the words "logo" or "client", a `|` or ` - ` separator, more than five words, or a legal suffix alone. Anything flagged goes back to sourcing, not to a rewrite rule.

## Changing the copy

1. **Fix the mechanism before the wording.** If errors grow with the number of rules, the generator is wrong (too much is generated). Fix what is fixed versus generated first.
2. **Show rendered emails, not rules.** Every proposal is a full assembled email with a real or plausible company name. Approve the sentence, not the abstract rule.
3. **Read it as the recipient.** Write their one-line reaction before showing it. Kill it if the reaction is "that's exactly what I'm doing", "those two sentences don't go together" or "why are you telling me this".
4. **Stop after two patch-induced failures.** If a fix causes the next failure twice in a row, the line is being asked to do something it can't do from these inputs.
5. **Every rule ships with a Valid and an Invalid example,** the invalid one quoted from the email that caused it.
6. **Fix once, then freeze.** The ask, the offer line and the structure are chosen once and not re-varied per draft.

## Example emails are real emails

Any text shaped like an email (subject, greeting, body, sign-off) shown to a client or teammate gets checked against the same rules, even as a quick illustration. People copy examples, not rules.

## Before launch: the approved-text check

A script compares every live step in the sending tool with the approved texts in the source:

- each step's body and subject match an approved text exactly, after placeholder substitution;
- no retired phrase appears;
- the first step contains no price, currency sign or pay term.

Any mismatch blocks the launch. Run it again after every edit in the sending tool, because edits made in a web UI bypass every review.

## Valid and Invalid

- Valid: "Hi Sam, most paid-media agencies selling to dental practices get new clients through referrals... Want two sample emails written for that market?"
- Invalid: "Hi Sam, I saw Acme offers PPC, SEO and web design for dentists. You pay per qualified call..." (restates their page, prices in email one)

## Before and after

- Before: a first email with a per-lead AI sentence about the reader went live; a prospect replied that it read as AI-written.
- After: only the company name and market are filled in, three fixed versions are tested in equal parts, and launch is blocked unless every live step matches an approved text.
