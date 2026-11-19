---
name: visual-plan-and-recap
description: "Use to turn a build into one scannable visual page, either before or after the work. Before: when the person is about to approve a plan that so far exists only as prose or a spec (a new feature, a workflow change, a document structure, any change with more than about three moving parts or branching logic), draw a component map, a numbered sequence, and a rough UI sketch so they can approve or correct it in under a minute. After: when a diff, a changelog, a handoff note or a here-is-what-I-built report arrives, or the person asks what actually changed or to see screenshots of finished work, draw what existed versus what is new, with schema and data impact called out. Skip both for one-line fixes or copy-only changes."
---

# Visual plan and recap

Needs: local shell

A wall of text is hard to sanity-check. A diagram is not. This skill makes one HTML page that shows a change, either as a plan (before building) or as a recap (after building). Plan and recap share one visual language so they read as a matched pair; Preview (below) is a third, lighter mode.

## Pick the mode

- **Plan mode**: nothing is built yet. The page exists so the person can say "yes, that is what I meant" or "no, move that" before any code or config changes.
- **Recap mode**: the change already happened. The page exists to show its impact, not just its appearance.
- **Preview**: the person only wants to see what a page or file looks like right now, with no framing of what changed (see the Preview section near the end of this file).

If it is unclear whether they want what changed or what it looks like now, ask in one line instead of guessing.

Check first whether a more specific tool owns the job (a UI mockup of something not yet built, a live walkthrough, a test pass, a chart). Route to it rather than building a generic visual. A request for step-by-step instructions the person will carry out themselves gets a written guide, not a diagram.

Skip plan and recap when one sentence covers the change fully.
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

**Deliver the live HTML, not a screenshot of it.** The page is the point: it scales, it can hold expandable details, and text stays selectable. Use a screenshot only if the HTML cannot be viewed (Preview mode below sends images by design, and comparison diagrams ship as both).
Valid: send the .html file so it opens as a page.
Invalid: flattening the page into a PNG out of habit.

**Look at the render before delivering.** Open the finished page and view it. Never assume the code drew what you meant.

**Branching diagrams need a real layout engine.** For flowcharts and decision trees, let a layout library compute the edge routing. Hand-placed connector lines are fine only for straight sequences.

**Chart code gets its own guidance.** If the page contains a chart or graph, read any available data-visualization guidance (palette, mark styles) before writing chart code.

**Copy from a reference by its pixels.** When recreating icons or colors from a reference image, crop and sample the file itself. Do not redraw from memory or guess hex values. This holds even when the image was already looked at earlier in the conversation: find the actual file and open it before extracting anything. The usual sequence: upscale and crop, sample exact colors from the pixels, remove the background by flood fill, check the result on the background it will sit on, and adjust the crop until the edges are clean.

**Pick the medium by how it will be used.** A self-contained HTML or SVG page for anything interactive, crisp at any size, or likely to be revisited; a rendered image for a static picture headed into a document, deck or chat; diagram-language source (Mermaid, Graphviz) when the source itself is worth keeping. A diagram that will be updated again and again stays one self-contained page updated in place; use a shared collaborative board only when other people must pan, zoom and comment on it. When the visual is going into a Word, slide or PDF file, settle the visual content first and only then follow that format's own guidance.

**Comparison diagrams.** When one path worked and another failed from the same starting point (a bug postmortem, "why did X work and Y not"), draw a branching comparison from the shared start. When two tools or options are weighed on their own merits with no shared event, lay them side by side as pros and cons. Either kind ships as both a static image and a self-contained HTML page, and a change to one is made to the other.

## Offering a visual unasked

Offer at natural moments only: a plan with three or more moving parts waiting for approval, or a finished structural change. Make the offer one line that names the output and why it helps, and build nothing until the person says yes. (A preview render of a page already edited, under "Preview" below, is not such a visual.)
- Do not offer for trivial changes.
- Remember declined offers per plan or work unit, and do not repeat the offer unless the plan changes materially. If you keep a running notes or handoff file, record it there.
- Once an offer is accepted, build the visual directly; the building step never loops back into offering.
- Offering never delays an explicit request: if the person already asked for a specific visual, build it without offering first.

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

Fire it for finished changes with real structural surface area: new fields, nodes or files, changed routing, or more than a couple of files touched. Not for single-line or copy-only edits.

1. **Before and after structure**, using the same existing-versus-new styling.
2. **Schema and data impact, made obvious**: new columns, new fields, changed field meanings. This is the change hardest to spot in a text diff, so give it the most visual weight.
3. **Contracts and boundaries**: what calls what now, what reads or writes which table now.
4. **UI impact**, only if a live screen changed: annotated screenshots (box plus short caption), never bare images.

When someone asks for screenshots of just-finished work, give the annotated recap, not a bare screenshot dump. If they ask specifically for a screenshot-based guide, the next paragraph applies instead.

If the person asks for a screenshot-based guide, real annotated screenshots are required every time. When nothing live exists to capture (backend-only change, a plan not yet executed), ask what should be captured or say plainly that nothing exists yet. Never ship a diagram-only recap in its place.

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

## Preview: what it looks like now

When asked to see a recently edited page or deck (or after a non-trivial visual edit, unasked), render it headlessly, cut long pages into sections of roughly 1200px height, and send the images with a one-line caption.

Pick the target without asking when it can be inferred: the file named, else the file most recently edited, else, in a web project, the live front page. Do not re-render untouched pages.

View each cropped section yourself before sending to catch rendering faults. Send all images in one message, then delete the temporary screenshots and render scripts.

## Style

Dark background with light text and lines, minimal, legible at a glance, one palette across all modes. Use light mode only when asked. Consistency between plan and recap pages matters more than either being fancy.
