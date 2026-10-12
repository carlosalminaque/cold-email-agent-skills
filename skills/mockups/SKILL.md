---
name: mockups
description: "Use when someone asks for a mockup, says show me what this would look like, or a proposed UI change (a screen, a dialog, a chat message layout, a dashboard view, an email layout) is about to be described in words. Builds a recognizable rendered visual of the proposed surface as one HTML file, with the current version beside it when there is one, so the person can react yes or no at a glance. Also use proactively whenever you catch yourself writing a paragraph about where buttons and fields would go. For a full pre-build plan with component maps and sequencing, use a plan diagram instead; for screenshots of something already built, use a preview."
---

# Mockups

People cannot approve a UI change from a prose description. They need to see it. This skill replaces "the dialog would have a title, two fields and a blue button on the right" with the actual dialog, rendered.

## When to use it

Any time you are about to describe in words what a proposed screen, message, dialog or view would look like, stop and build it instead.
Valid: a plan adds a new approval message to a chat channel, so render the message.
Invalid: three bullet points listing what the message "would contain."

## What to build

One self-contained HTML file (all CSS and JS inline) that looks like the real surface, not a wireframe.

**Match the host's real look.** A chat message gets an avatar, timestamp, bubble and real button styling. A dialog looks like a dialog. A view inside an existing app uses that app's own fonts, colors and spacing, read from the live app where possible.
Valid: the new table view uses the app's existing header color and row height.
Invalid: gray boxes labeled "header" and "table goes here."

**Show before and after side by side** when something already exists, so nobody has to hold the old version in memory.
Valid: current form on the left, proposed form on the right, same scale.
Invalid: only the new form, with a note saying "the old one had the button lower."

**Keep it to one glance.** The goal is a fast "yes, that is it" or "no, move that," not a document to study.

## Style rules

- **Gray out disabled controls** instead of labeling them. No floating annotation tags like "CLICKABLE" or "DISABLED".
  Valid: the Submit button rendered at reduced opacity with a muted fill.
  Invalid: a red sticker reading "DISABLED" pinned next to it.
- **Strong contrast everywhere**: button text against its fill, fill against the page, small status text in a light color, never dim gray on gray.
- **Grouping boxes are fine** when they mirror real panels.
- **Showing alternatives:** put each option's one-line "what's different" inline to the right of its "Option N" label, not underneath, so options can be compared by scanning one column.
- Keep one consistent palette across mockups rather than inventing a new look each time.

## Delivery

Deliver the HTML so it opens as a live page. If the mockup supports a pending decision that will be revisited or shown to someone else, also save it somewhere persistent rather than only in the conversation.

## After producing it

Ask directly whether it matches what the person had in mind, or what to move. Treat "no" as a revision to make now, not a note for later. Repeat until it is right: show, react, tighten.

## How this relates to neighbors

- A **plan diagram** covers architecture, data flow and sequencing as well as UI. Use it when the moment needs more than the look.
- A **preview** screenshots something that already exists.
- A **chart** shows data, not interface.
