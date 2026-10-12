---
name: step-by-step-guide
description: "Use when someone types /guide or asks for easy-to-follow instructions to do something themselves: walk me through this, show me what to do, give me steps, make this easy to follow. Covers any task. For a web UI the guide can reach, the default output is a screenshot-annotated PDF (walk the flow, box and arrow the target on each screenshot, one step per page); plain numbered text steps are for tasks that are not browser flows, or when screenshot capture itself was tried and failed. Before writing any guide, check whether the tool or an agent can just do the change directly."
---

# Step-by-step guide

Easy-to-follow instructions for a task the person will do by hand, in the best format for the situation.

## First: does anyone need to do this by hand?

Before writing a guide, check whether the change can be made directly: by you, by an API, or by the tool's own built-in assistant. If the tool has an assistant that can make the edit, the right output may be a precise prompt for it (exact names, exact values, and "show the change before applying") instead of a guide.
Valid: the editor's built-in assistant can rewire the connection, so hand over a prompt for it.
Invalid: a ten-page manual drag-and-drop guide for something one API call could do.

## Pick the format

**Default for any reachable web UI: a screenshot-annotated PDF.** Screenshots are not a nice-to-have to trade for speed. A small change inside a web UI is still a web UI task; tiny, crowded controls are exactly what screenshots solve.

**Use plain numbered text only when:**
- the task is not a browser flow (editing code, a config file, a spreadsheet formula), or
- screenshot capture itself was attempted and failed (the screenshot, navigate or click action was blocked, the tab was confirmed frozen, or the page was unreachable after one retry).

**The gate:** did screenshot capture fail, or did something else fail? A blocked write, fetch or API call says nothing about whether screenshots work. Try screenshots anyway.
Valid: a scripted save was blocked, but screenshots still work, so build the PDF.
Invalid: falling back to text because a different action was blocked nearby.

If capture really fails, retry once in a fresh tab, then switch to text and say in one sentence which capture step failed. Do not keep probing other automation routes.

## Screenshot-annotated PDF

1. **Walk the flow yourself**, capturing the screen right before each action that matters. Note each filename.
2. **Annotate each screenshot** with PIL: a colored box around the target, an arrow if the box alone is not obvious, and a numbered label ("STEP 3: Click Settings"). Keep small helpers:

   ```python
   import math
   def arrow(d, start, end, color=(255,0,60), width=6):
       d.line([start, end], fill=color, width=width)
       a = math.atan2(end[1]-start[1], end[0]-start[0]); L = 22
       d.polygon([end, (end[0]-L*math.cos(a-0.4), end[1]-L*math.sin(a-0.4)),
                       (end[0]-L*math.cos(a+0.4), end[1]-L*math.sin(a+0.4))], fill=color)
   def box(d, xy, color=(255,0,60), width=5):
       d.rectangle(xy, outline=color, width=width)
   def label(d, xy, text, font, color=(255,0,60), bg=(255,255,255)):
       l, t, r, b = d.multiline_textbbox(xy, text, font=font)
       d.rectangle([l-6, t-6, r+6, b+6], fill=bg, outline=color, width=3)
       d.multiline_text(xy, text, fill=color, font=font)
   ```

   Read box and arrow coordinates off each actual screenshot; there is no shortcut.

   **Match the label background to the screenshot.** Check each screenshot's background: dark app, dark label; light app, light label.
   Valid: a dark label box with light text over a dark-themed editor.
   Invalid: a white label box pasted onto every screenshot regardless of theme.

3. **Assemble the PDF** (reportlab works well): a title page saying what this does and why it is manual, one page per step (bold title, one or two sentences of instruction, the image scaled to fit), and a closing "after this" page.
4. **Deliver the file.** It is a one-off reference, not a page to keep updating.

If the point of the walkthrough is testing whether typed input behaves differently from scripted input, say "type this by hand, do not paste it" on the title page.

## Plain numbered text

- **Group by destination**: one heading per place (a settings page, a file). Never interleave two places.
- **Number every discrete action**: open, find, click, change, save.
- **Exact values in code blocks**, with the old and new value both shown verbatim:

  ```
  Find:
  timeout = 30

  Replace with:
  timeout = 120
  ```

  Valid: the exact old line and new line, copyable.
  Invalid: "bump the timeout to something higher."
- **Name controls as they appear on screen**, and call out easy-to-miss ones (an icon-only toggle).
- **End each group with the save or confirm step.**
- **Keep it short** enough to scan while switching windows.

## One skill, two outputs

Plain text is not an apologetic fallback when it fits. But for a web UI, screenshots are the starting assumption. Choose the format the gate justifies, not the one fastest to produce.
