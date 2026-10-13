---
name: match-a-reference-image
description: "Use whenever the task is to recreate, copy, match or reuse visual elements from a reference image someone provided: icons, logos, exact colors, diagram styling, a specific look. Trigger on make it look exactly like this, use the same icons as this, match this color or style, recolor this image, copy this design, or any request with an attached image to replicate. Also use proactively whenever you are about to hand-draw an SVG icon or guess a hex color for something that already exists as pixels in a file you were given. Works from the actual file: precise crops, sampled colors, edge-connected background removal, and a check on the target background. Not for original illustration with no reference."
---

# Match a reference image

Needs: local shell

## Why this exists

Given a reference image, the tempting move is to describe it to yourself ("three linked dots, orange") and rebuild it from that description: a hand-drawn SVG, a hex code that looks about right. The result is plausible and wrong. Icons come out generic, colors are close but off, shapes end up mirrored. The person comparing against the real image notices at once.

The reference is a file. Read its pixels.

## The core rule

If a reference image exists, every element reused from it comes from processing that file, not from redrawing a memory of it. Hand-drawing is the fallback only when there is no file to copy.
Valid: crop the logo from the uploaded PNG and remove its background.
Invalid: writing an SVG path that "looks like" the logo you saw earlier in the chat.

Having seen the image earlier in the conversation is not the same as having processed it. Find the actual file path and load it.

## Workflow

### 1. Load the real file

Find the image (uploads folder, a path in the conversation, an attachment) and open it. If only a description is available, ask for the file. Do not proceed from memory.

### 2. Crop precisely, upscale small sources

Uploaded images are often small; a 40 px icon is easy to crop a few pixels wrong.

- Upscale 3 to 4 times with LANCZOS before fine cropping, so edges are easy to see.
- Crop generously, look at the result, tighten. Two or three rounds per icon is normal.

```python
from PIL import Image
im = Image.open(source_path).convert('RGBA')
crop = im.crop((x0, y0, x1, y1))
crop = crop.resize((crop.width * 4, crop.height * 4), Image.LANCZOS)
crop.save('crop.png')
```

### 3. Sample colors, never eyeball them

```python
import numpy as np
arr = np.array(Image.open(path).convert('RGB'))
color = arr[y, x]                                        # one pixel
patch = arr[y-2:y+3, x-2:x+3].reshape(-1, 3).mean(0)     # average, avoids edge noise
```

Valid: brand color taken as the mean of a 5x5 patch in the middle of a filled shape.
Invalid: "#FF8800 looks right."

### 4. Remove backgrounds by edge-connected flood fill

"Make everything near the background color transparent" also deletes enclosed details of a similar color (a white line inside a white-outlined icon). Real background is the similar-colored region connected to the image edges; enclosed pixels survive.

Use the bundled script:

```bash
python3 scripts/extract_icon.py crop.png icon.png
```

It samples the background from the crop's edges, keeps only the edge-connected region as background, and ramps alpha at the boundary for clean edges. Options `--low`, `--high` and `--bg-thresh` tune it for low-contrast, noisy or gradient cases; see the script's header.

Valid: enclosed white grid lines inside the icon stay opaque.
Invalid: a global color threshold that punches holes in the icon.

### 5. Verify on the target background

Composite each result onto a swatch of the background it will actually sit on, then look at it before using it.

```python
canvas = Image.new('RGBA', (w, h), TARGET_BG)
canvas.paste(icon, (x, y), icon)
canvas.save('check.png')   # open and inspect
```

This catches leftover background slivers and icons that are illegible at the final size, while fixing them is still cheap.

### 6. Fix stray edges by moving the crop

A thin line or partial shape at the edge of an extracted icon means the crop caught a neighbor (a border, a divider). Move the crop box inward on that side and rerun steps 2 and 4. Do not tune thresholds to hide it.
Valid: shrink the crop by 3 px on the left where a card border showed.
Invalid: raising `--bg-thresh` until the border fades and the icon edge erodes too.

## When it does not apply

Original work "in the style of" something, with no specific file to copy, is drawing work. The test: is a specific file being copied, or is new work being made?
