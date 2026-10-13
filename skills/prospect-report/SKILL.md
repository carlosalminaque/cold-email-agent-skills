---
name: prospect-report
description: "Use when a batch of prospect companies has been sourced or qualified and someone wants a report, writeup, dossier or visual of them before any outreach copy is written, or says show me what you found about a batch of companies. Re-checks every company live right before writing (site, company profile, open roles, the signal source), screenshots each one, flags anything that changed since sourcing, and renders one self-contained HTML report with a section per company and its scores. Do not jump from a fresh batch straight to drafting emails; this review comes first so a person can sanity-check every claim that might end up in a message."
---

# Prospect report

Needs: browser control

Turns a batch of sourced companies into something a person actually reads before deciding what happens next. Not a spreadsheet dump: a report with real screenshots of each company's site, profile page and signal source, so a claim can be checked at a glance instead of by reopening ten tabs.

## Why the live re-check matters

The most useful thing this report does is catch drift between sourcing and review. Job posts get filled, headcounts get corrected, funding articles disappear. A signal from three days ago can already be stale, and it is often the exact fact that would have gone into the first email.

- Valid: "Re-opened the careers page at build time. The SDR role cited during sourcing is gone. Flagged red."
- Invalid: "Used the notes from sourcing earlier this session; no need to look again."

## Build sequence

1. **Get the batch.** The companies just qualified, or the undecided rows from wherever leads are tracked.
2. **Re-check each company live, right before writing its section.**
   - Its homepage.
   - Its company profile page (for example LinkedIn: headcount, description) and its open roles.
   - The exact signal source the qualification rests on (a job post, a funding article, a review-site listing). Confirm it is still live and still says the same thing.
   - Screenshot each one. Real captures, not descriptions.
3. **Try the hard sources before calling them unreachable.** Fetch tools often cannot read logged-in sites, but a real browser session often can. Try it. If a profile URL 404s, use the site's own search; slugs often differ from the obvious guess.
4. **Note disagreements between sources.** If the open-roles list on a profile site and the company's own job board disagree, say so in one line rather than silently picking one.
5. **Compare against the original qualification.** Anything that moved gets a callout in that company's section, not a quiet edit.
6. **Render one self-contained HTML file** with every image embedded, so it survives being moved between sessions or machines. Add a PDF if useful; the HTML is the main copy.
7. **Save it somewhere durable** (a shared artifact, a project folder), not only inside one chat.

If a source truly cannot be reached this run, say so inside that company's section, next to where the screenshot would be.

- Valid: a placeholder in the grid reading "Profile page: not captured, no logged-in browser available this run."
- Invalid: three screenshots where four were expected, and a single methodology footnote at the end.

## Report structure

**Header:** title, batch name, sourced and verified dates, one-line scope.

**How this report was built:** a short numbered list (define who fits and what signals count, source, score, record, find contacts, re-check live, render) and one line naming the tools used. This is what lets a later reader trust the report without redoing it.

**One section per company**, in ranked order:
- Name as a heading.
- A badge row: location, headcount with its source (profile site vs. a third-party estimate; they disagree and that is worth showing), funding stage, subniche.
- A two or three sentence plain summary: what they make and who buys it.
- A screenshot grid (homepage, profile page, open roles, signal source) with a one-line caption each, plus a placeholder note for anything missing.
- A **Live update** callout when something changed: amber for informational, red for anything that would break the qualification or an outreach claim if used as is.
- **Traction:** specific, checkable evidence.
- **Signal found:** the buying signal and its source.
- **Hook:** the one specific detail an opening line could use, in a visually distinct box.
- **Contact:** name and title if enrichment has run; say plainly if not.
- **Scores:** one pill per scoring dimension, using exactly the same field names and scale as the lead tracker so the two never disagree.
- **Caveat box** for borderline cases (largest in the batch, weakest scores, traction that is adjacent but not the required kind). The include or exclude call belongs to the reviewer.

## What this report does not do

It does not draft outreach. End the report without email copy. The point is that a person looks at real evidence before anything is written in their name.

- Valid: report ends with the last company section and the build notes.
- Invalid: report ends with "Email 1 for each company" appended "to save time."
