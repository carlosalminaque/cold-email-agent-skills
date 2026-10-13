---
name: visual-concepts
description: "Use when the human does not like how something looks (a page section, hero, slide, video frame, email layout), asks for options or concepts, says make it look good or something completely different, or rejects a first set of variants. Builds four to six concepts that differ in structure, not just color, including any visual the human described used literally, in the real styles read live, checked for contrast and at phone width, each labelled in one line with a recommendation. Never publishes."
---

# Visual concepts

Needs: local shell

People react to rendered visuals, not descriptions. When a design feels wrong, three color variants of the same layout do not help: the problem is usually the structure, and the human wants to see genuinely different ways of doing it and point at one. A rejected first round is a signal that the variants were too similar, not that the human is hard to please.

## When

- The human rejects how something looks, or asks for options, concepts, "something different", "make it look good".
- A first round of variants was rejected. The next round changes the structure.
- Not for a single known change ("make this gray"), where one mockup is enough.

## Steps

1. **Name the real problem in one sentence** before designing. Valid: "Two audiences in one large headline make it four lines and wordy." Invalid: "The colors aren't working."
2. **Read the live styles, don't guess.** Open the real page and read the computed font family, size, weight, line height, text colors and background. Use those exact values so the concepts look like the real thing.
3. **Make four to six concepts that differ in structure.** Each changes how the content is arranged or presented. Ways to vary:
   - show one item at a time (rotate, flip, type out);
   - move secondary items out of the headline into labels, chips or cards;
   - let the visitor choose (a switch or tabs);
   - split into a short headline plus supporting blocks;
   - animation that carries meaning, never decoration alone.

   **If the human described a visual themselves** (lines between items, a worksheet, a tree, "like this" with a picture), at least one concept uses that exact device literally, and it goes first. At most one concept may be "same layout, new colors", and only if they asked about color.
4. **Keep their words unless the words are the problem.** New copy is marked as a draft in its label. Never invent claims or numbers.
5. **Follow their visual rules** (theme, brand colors, label style). Each concept gets a one-line "what's different" next to its name. Gray out disabled controls instead of adding floating annotation labels.
6. **Check by script before sending:**
   - text contrast against the real background, 4.5:1 or more; state the ratio when color is part of the choice;
   - render at desktop and phone width (about 390 px) and look at both; page width equals the viewport, no sideways scroll;
   - animation stops when the viewer has asked for reduced animation, and the layout does not jump while it moves;
   - interactive pieces work by click.
7. **Send one file** that shows every concept, with a one-line recommendation of one or two and why. It is a one-off review file, not a published page.
8. **After they pick,** write a short build spec: their words, the exact look (values, timing, colors), reference markup from the concept, accessibility needs (full text for screen readers and search engines, the state shown when animation is turned off) and the live checks to run after release. Publishing stays gated on their yes.

## Valid and Invalid

- Valid: five concepts, each a different structure, in the page's real font and size on its real background, checked at desktop and phone width, with "1 or 3, because they show one audience at a time" as the recommendation.
- Invalid: three versions of the same headline with one word in gray, light gray and blue.
- Invalid: a concept that adds "Book 10 meetings a month" as new copy nobody approved.
- Invalid: the human asked for "lines pointing between the items" two rounds ago, and no concept has lines.

## Before and after

- Before: three rounds of color tweaks, all rejected, because the layout itself was the problem.
- After: one round of five structural concepts. The human picked one in a single look.
