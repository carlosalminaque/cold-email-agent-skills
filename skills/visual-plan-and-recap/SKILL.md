---
name: visual-plan-and-recap
description: "Use to turn a build into one scannable visual page, either before or after the work. Before: when the person is about to approve a plan that so far exists only as prose or a spec (a new feature, a workflow change, a document structure, any change with more than about three moving parts or branching logic), draw a component map, a numbered sequence, and a rough UI sketch so they can approve or correct it in under a minute. After: when a diff, a changelog, a handoff note or a here-is-what-I-built report arrives, or the person asks what actually changed or to see screenshots of finished work, draw what existed versus what is new, with schema and data impact called out. Skip both for one-line fixes or copy-only changes."
---

# Visual plan and recap

A wall of text is hard to sanity-check. A diagram is not. This skill makes one HTML page that shows a change, either as a plan (before building) or as a recap (after building). Both modes share one visual language so they read as a matched pair.

## Pick the mode

- **Plan mode**: nothing is built yet. The page exists so the person can say "yes, that is what I meant" or "no, move that" before any code or config changes.
- **Recap mode**: the change already happened. The page exists to show its impact, not just its appearance.

Skip both when one sentence covers the change fully.
Valid: a plan touching three services, a new database table and an approval step gets a plan page.
Invalid: drawing a diagram for renaming one form label.

## Shared rules

**Ground it in real current state first.** Inspect the actual files, schemas or live settings the change touches before drawing. A diagram built on an unverified guess looks authoritative and is worse than none.
Valid: open the current table schema, then draw which columns are new.
Invalid: drawing the schema from memory of how it looked last week.

**Existing versus new is always visible.** Solid border for existing pieces, dashed border (or one consistent color pair) for new ones, in both modes.
Valid: the old webhook is a solid box, the new retry queue is dashed.
Invalid: every box the same style, so the reader cannot tell what changes.

**Fit one screen of scanning.** If two diagrams are needed (data flow and a UI sketch), put them in labeled sections of the same file rather than nesting everything into one dense chart.

**Deliver the live HTML, not a screenshot of it.** The page is the point: it scales, it can hold expandable details, and text stays selectable. Use a screenshot only if the HTML cannot be viewed.
Valid: send the .html file so it opens as a page.
Invalid: flattening the page into a PNG out of habit.

## Plan mode: what to include

1. **Component map**: a box for each file, table, service or node the plan touches, with arrows for data and control flow.
2. **Numbered sequence**: the order things happen, with branches (if/else routing, approval gates, retries) shown explicitly.
3. **Rough UI sketch**, only if a screen, message or dialog is new or changed. Recognizable, not pixel-perfect.
4. **Hard-to-reverse decisions, called out**: data shapes, public IDs, wire formats, permission boundaries. Give them stronger visual weight than easy choices.
5. **Scope**: what is in this pass and what is deliberately deferred.
6. **Open questions in one section**, not scattered as inline caveats.

Plan mode is read-only. Producing the page never edits the files it describes.
Valid: the plan page lists "Not in this pass: bulk import" at the bottom.
Invalid: quietly editing the config while drawing the plan of the config change.

For high-stakes plans, have a fresh reviewer (another agent or session that did not write the plan) look for unstated decisions before calling it final. Self-review shares the plan's blind spots.

After delivering, ask directly whether it matches the intent. Treat "no" as a plan correction now, while fixing it costs a diagram edit instead of a rebuild.

## Recap mode: what to include

1. **Before and after structure**, using the same existing-versus-new styling.
2. **Schema and data impact, made obvious**: new columns, new fields, changed field meanings. This is the change hardest to spot in a text diff, so give it the most visual weight.
3. **Contracts and boundaries**: what calls what now, what reads or writes which table now.
4. **UI impact**, only if a live screen changed: annotated screenshots (box plus short caption), never bare images.

Recap safety rules:

**Redact anything credential-shaped.** API keys, tokens, passwords and secret URLs become `[redacted]`.
Valid: "Webhook URL set to [redacted]".
Invalid: copying the real token from the diff into the recap.

**Separate the task's changes from unrelated work.** Leftover edits or pre-existing uncommitted changes get their own labeled note.
Valid: "Also in the diff, unrelated to this task: a formatting change in utils."
Invalid: folding an unrelated refactor into the recap as if it were part of the request.

**Derive, never infer.** Every claim traces to something in the diff, report or live state. If the source omits something (it says "added fields" but not which table), say so on the page instead of guessing.
Valid: "Source does not say which table got the new fields."
Invalid: naming the most likely table as if confirmed.

Work from the best source available: a real diff first, then a detailed report or handoff note, then a live click-through with fresh screenshots.

## Style

Dark, minimal, legible at a glance, one palette across both modes. Consistency between plan and recap pages matters more than either being fancy.
