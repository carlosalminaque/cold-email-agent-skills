---
name: comparison-diagrams
description: "Use when the person wants a comparison turned into a shareable diagram, as a portrait PNG for social posting plus a resizable HTML page. Two shapes. Story shape: a technical investigation, bug postmortem or why-did-X-work-and-Y-didn't finding where both paths start from one shared action and split into different outcomes. Versus shape: a straight pros and cons comparison of two tools, approaches or options with no single shared starting event. Trigger on make a diagram of this, explain this as a diagram, make a vs diagram, pros and cons of X vs Y, or compare these side by side."
---

# Comparison diagrams

Needs: local shell

Two layouts that share one visual system: a **story** diagram (one start, two outcomes) and a **versus** diagram (two options weighed side by side). Both open by splitting into two lanes and close by merging back into one verdict, so the page shape tells the story before anyone reads it.

## Pick the shape

Valid: "Why did the script work in tool A but get blocked in tool B?" uses the story shape.
Invalid: forcing "pros and cons of tool A vs tool B" into a fake shared starting step; that is the versus shape.

## Deliver two formats, always

1. **Portrait PNG**, 1080px wide, height computed from the content, for posting.
2. **Resizable self-contained HTML**, identical content, so readers can widen the window to read small details like embedded screenshots.

Build the HTML first and screenshot it with a headless browser to get the PNG. One source keeps the two formats in sync.
Valid: edit the HTML, re-render the PNG, send both.
Invalid: updating the PNG text and leaving the HTML stale.

## Story layout (top to bottom)

1. **Caption strip**: dark band, accent text, the post caption. The only place first person is allowed, because it is the poster's own voice.
2. **Title**: the finding as a contrast or question. Name the tools or people involved; never "I" past the caption.
3. **Subtitle**: one plain sentence framing the contrast.
4. **Shared-step box**: the common starting action shown once in neutral gray, with the real command or code snippet if there is one.
5. **Opening fork**: one stem down to a fork point, then two diagonal arrows in each lane's color into two outcome badges (for example BLOCKED and ALLOWED). This is the most important element. If asked to simplify, keep the fork and change only spacing.
6. **Two lane cards**: title plus one or two short paragraphs of plain explanation each.
7. **Receipts**: real screenshots or evidence, framed in each lane's color, one-line caption each. Ask for them if they exist.
8. **Footer note**: the one fact tying both lanes together.
9. **Per-lane mini-verdicts**: one sentence each, stating that lane's lesson. If the two could be swapped without changing meaning, rewrite them.
10. **Closing merge**: two diagonal lines from under the mini-verdicts meeting at a point, one stem down.
11. **"In one sentence: the verdict" box**: bold, no jargon.

## Versus layout (top to bottom)

1. Caption strip and title ("X vs Y: the tradeoff, honestly"), same first-person rule.
2. Subtitle naming what is actually being weighed.
3. **VS row**: two colored pills with each side's icon, a small round "VS" badge between them.
4. **Two columns** (stacked on narrow screens), each with a separate Pros box and Cons box. Pros bullets take that side's own color; cons share one warm red. One or two sentences per bullet.
5. Per-side mini-verdicts, closing merge, and the one-sentence verdict, as in the story layout.

## Colors and icons

Give each side a fixed color and keep it across diagrams, so repeat readers can tell the sides apart by color alone. Never pick a side's color because its outcome "feels" good or bad.
Valid: tool A is always orange, tool B always blue, even in a diagram where tool A lost.
Invalid: switching tool A to green because it was the winner this time.

Put a small inline-SVG icon next to each side's name wherever the name is prominent. Make it a recognizable stylized approximation of that brand's real mark shape (look the shape up first), not a generic sparkle, and not a traced copy of the official logo file.

## Writing style

The target is "more explanatory, yet simpler, and not stripped of technical terms." All three at once.

- **No arrow-chain shorthand.** Write cause then effect as a sentence.
  Valid: "With no exact coordinates, the agent guessed the target's position from a screenshot and missed the 5px dot."
  Invalid: "No coords -> guess -> miss."
- **Keep real terms** (DOM, classifier, method names). Explain them in line instead of deleting them.
- **Simpler is not shorter.** If asked to simplify an already lean diagram, the fix is usually clearer sentences, not less content. Ask if unsure which way the feedback points.
- One or two short paragraphs per card. A third sentence usually means a second idea; split it.

## HTML notes

- One self-contained file: inline CSS, screenshots embedded as base64.
- Font sizes with `clamp(min, vw, max)` so text scales smoothly.
- Forks and merges as inline SVG with a `viewBox` and `preserveAspectRatio="none"`, so the angles scale with width. Do not fake them with rotated divs.
- Column of badge plus card: make the column a flex column, badge `flex: 0 0 auto`, card `flex: 1 1 auto`. Setting the card to `height: 100%` overflows past the badge.
- VS row as one flex row: pills `flex: 1`, badge `flex: 0 0 auto`.
- Compute every box's height from its wrapped text. Never hardcode the page height.

## Common revision requests

- A "make it vertical" pass flattened the fork into colored boxes: restore the real fork.
- First person crept past the caption: replace with names.
- A tool's name is slightly off: confirm the exact product name before it goes in a title.
- "I can't read it": point to the HTML version, which scales.
