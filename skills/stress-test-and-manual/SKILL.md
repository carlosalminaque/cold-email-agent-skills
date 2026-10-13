---
name: stress-test-and-manual
description: "Use when asked for a full, skeptical pass on a feature or system and a written manual at the end. Clicks through every state in the real interface, tries deliberate misuse (double clicks, out of order steps, odd input), root-causes anything that breaks, and then writes a manual with annotated screenshots, a diagram for any hard rule, and plain findings. Triggers include test everything, try to break it, and write a user manual."
---

# Stress test and manual

Needs: browser control

"It's built" is not "it works". Features get marked done after reading the config, and break the first time someone clicks a button twice or acts on an item that was already processed. A skeptical owner is right to doubt done claims. This skill closes the gap with evidence: every state clicked, deliberate misuse tried, and a manual that states plainly what broke.

## When

- "Test everything", "try weird things and see what breaks", "write a manual".
- When someone is unsure how two parts of a system relate and wants it explained properly.
- Not for a single quick bug check. This is a full pass.

## Steps

1. **Read live state first.** Never trust an earlier summary. Use the system's API or database where you can, not only the interface.

2. **Happy path, in the real interface.** Click every button and submit every form. Screenshot each distinct state. For any control with a real outside effect (sending a message, unsubscribing a contact, publishing, spending, deleting), use a scoped dummy item instead and say so in the write-up.

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

## Tone

State breaks plainly. "Clicking Approve twice sends two emails. Repro: open a pending draft, click Approve, click again within two seconds." Not "there may be some edge cases around approvals."

## Valid and Invalid

- Valid: "Double-clicking Approve created two send jobs. Read the execution log: no lock on the record. Added a status check, replayed the double click, one job. Fixed."
- Invalid: "Read the workflow config. The approval logic looks correct. Tested."
- Valid: "Unsubscribe tested with a dummy contact, not a real lead, as noted in section 4."
- Invalid: Clicking Unsubscribe on a real lead to see what happens.
