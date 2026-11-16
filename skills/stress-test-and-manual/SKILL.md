---
name: stress-test-and-manual
description: "Use when asked for a full, skeptical pass on a feature or system and a written manual at the end. Clicks through every state in the real interface, tries deliberate misuse (double clicks, out of order steps, odd input), root-causes anything that breaks, and then writes a manual with annotated screenshots, a diagram for any hard rule, and plain findings. Triggers include test everything, try to break it, and write a user manual."
---

# Stress test and manual

Needs: browser control

"It's built" is not "it works". Features get marked done after reading the config, and break the first time someone clicks a button twice or acts on an item that was already processed. A skeptical owner is right to doubt done claims. This skill closes the gap with evidence: every state clicked, deliberate misuse tried, and a manual that states plainly what broke.

## Two modes

- **Stress mode** (the default, described in Steps): verify the system and produce a manual.
- **Demo capture mode**: happy path only, presentable screenshots for a manual, site or deck. Use it only when correctness is not in question this pass or was verified separately. If the request is ambiguous ("get me screenshots of the app"), ask in one line which mode is wanted.

Do not skip real verification of an untested system just because a deck needs screenshots of it. If there is genuine doubt that it works, run stress mode first. Reuse recent stress-test screenshots where they are presentable instead of recapturing.

## When

- "Test everything", "try weird things and see what breaks", "write a manual".
- When someone is unsure how two parts of a system relate and wants it explained properly.
- Not for a single quick bug check. This is a full pass.

## Steps

1. **Read live state first.** Never trust an earlier summary. Use the system's API or database where you can, not only the interface.

2. **Happy path, in the real interface.** Click every button and submit every form. Screenshot each distinct state. For any control with a real outside effect (sending a message, unsubscribing a contact, publishing, spending, deleting), use a scoped dummy item instead and say so in the write-up. If one browser tab keeps timing out on screenshots, open a fresh tab for each attempt; that is a tooling glitch, not a page problem.

3. **Misuse, on purpose.** For every action ask:
   - What if they do it twice?
   - Out of order?
   - On something already finished, like editing a sent item?
   - With empty, huge, or odd input (emoji, special characters)?

   The same dummy-item rule applies.

4. **Root-cause every break before moving on.** Read the raw execution or error data, not the symptom on screen. Prove a fix by replaying the same scenario, not by reading the new code.

5. **Write the manual, after all testing is done:**
   - overview;
   - screen-by-screen walkthrough with annotated screenshots (a box and a one-line caption each, readable on their own);
   - a diagram for any threshold, state machine or multi-step gate that prose cannot explain;
   - confirmed-working results;
   - misuse findings with exact repro steps and exact error text;
   - recommendations;
   - what is still untested.

6. **Look at the output before delivering.** Render the document to images and check it.

7. **Update the record.** New bugs, corrected stale claims and decisions go to the project's notes, so the manual is not the only record.

## Demo capture rules

Steps 1 and 2 still apply (live state first, real interface, dummy items for side effects), with no misuse testing. Then:

- **Clean fictional data.** Client-facing screenshots never show real people, emails or companies, debug labels, or empty states that look unfinished. Seed one fictional example end to end if needed.
- **Fit the scenario.** An AI-written sample reply in a screenshot should pitch the fictional company's own offer, not the vendor's pitch to itself.
- **Restraint.** One screenshot per real capability beats a tour of every settings page. Leave internal and admin screens out. If you are given a reference (a competitor's page or an example deck), follow its organising pattern, never its claims or visuals.
- **Flag defects.** Do not hunt for edge cases, but if something is visibly broken in its default state, root-cause it before it reaches a client-facing asset.
- **Preview, then sign-off.** Build a local preview and get explicit sign-off before packaging or deploying anything.

## Tone

State breaks plainly. "Clicking Approve twice sends two emails. Repro: open a pending draft, click Approve, click again within two seconds." Not "there may be some edge cases around approvals."

## Valid and Invalid

- Valid: "Double-clicking Approve created two send jobs. Read the execution log: no lock on the record. Added a status check, replayed the double click, one job. Fixed."
- Invalid: "Read the workflow config. The approval logic looks correct. Tested."
- Valid: "Unsubscribe tested with a dummy contact, not a real lead, as noted in section 4."
- Invalid: Clicking Unsubscribe on a real lead to see what happens.
- Valid: a deck screenshot of a fictional dental clinic's inbox with a sample reply selling the clinic's own whitening offer.
- Invalid: a deck screenshot showing a real customer's name and an empty "0 results" table.
