---
name: demo-screenshots
description: "Use when screenshots of a working system are needed to show it off, for a manual, a website, a walkthrough or a client-facing deck, and the system has already been tested or does not need testing for this purpose. Runs a happy-path click-through with clean fictional demo data, flags anything visibly broken, and builds an annotated deliverable. Use stress-test-and-manual instead when the goal is proving the system does not break."
---

# Demo screenshots

Needs: browser control

A screenshot for a deck has a different job from a screenshot for a bug report. It must look finished, use believable data, and show one real capability. Test-run screenshots usually fail that: real prospect names on screen, debug labels like "test copy 2", empty states that look thin, or an AI draft that pitches the wrong company. Capture demo screenshots on purpose, from a clean run.

## When

- A manual, website section, walkthrough or proposal deck needs screenshots.
- The system's correctness is not in question for this pass, or was tested separately.
- If there is real doubt the system works, run stress-test-and-manual first. Do not run both passes on the same system for the same purpose: reuse recent test screenshots where they are presentable.

## Steps

1. **Read live state first.** Do not build a deck around a screen that has changed or a feature that is not live.

2. **Happy path only.** Load each screen you need in its normal state. No misuse testing. For any action with a real outside effect, use a demo item and say so.

3. **Use clean demo data.** Never show real prospect names, emails or companies, debug labels, or empty states. If no demo data exists, create one fictional example end to end first: a fictional company and a realistic scenario. If an AI draft is on screen, check that it fits the scenario shown. A reply "to a prospect" of a fictional client should pitch that client's offer, not your own.

4. **Flag what looks broken.** If something is visibly wrong in the normal state, root-cause it before it lands in a client-facing asset. Do not go looking for edge cases.

5. **Build the deliverable:**
   - annotate key screenshots (a box and a one-line caption);
   - follow the target format's own instructions (document, site, deck);
   - borrow a reference's structure if one is given, never its claims or visuals;
   - one screenshot per real capability; leave out admin and settings screens that do not help explain or sell.

6. **Preview, then ask.** Produce a local preview. Get an explicit yes before publishing or deploying anything.

7. **Update the record.** A mislabeled screen, or a feature that turned out to be designed but not built, goes into the project's notes.

## Valid and Invalid

- Valid: "Seeded a fictional prospect at a fictional agency, ran one reply through, captured four screens. Preview attached for your yes."
- Invalid: A deck slide showing a real lead's name and a campaign called "quick test copy".
- Valid: "Settings page left out: it does not show a capability."
- Invalid: Twelve screenshots, one per settings tab.
- Valid: "The draft on screen pitched our own service to the fictional client's prospect. Re-ran with the client's offer before capturing."
