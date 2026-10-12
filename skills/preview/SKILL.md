---
name: preview
description: "Use when someone types /preview, says show me a preview, preview it, or asks what a recently edited web page, HTML file, deck or document looks like now. Renders the right file in a headless browser, screenshots it, crops a long page into readable sections, checks them for rendering problems, and sends the images with a one-line caption. Also use proactively right after any non-trivial visual edit to a page or HTML file, without waiting to be asked. Not for summarizing what changed (use a recap) or for designing something not yet built (use a mockup)."
---

# Preview

Render and screenshot the current state of a page so the person sees it without spelling out the steps every time.

## Pick the file

1. If the person names a file or page, use it.
2. Otherwise use whatever was most recently edited in this conversation. If one change touched several pages (a shared stylesheet), preview the page most central to the change, or all of them if the change is visible everywhere.
3. No recent edit to go on: use the main page of the project (usually the homepage).

Confirm the file path exists before rendering; layouts move between sessions.
Valid: "preview it" right after editing pricing.html renders pricing.html.
Invalid: asking "which file?" when the last edit makes it obvious.

## Render

Use Playwright with whatever Chromium is installed. If a browser binary is already present, point at it rather than downloading a new one.

```js
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });
  await page.goto('file:///absolute/path/to/file.html');
  await page.waitForTimeout(300); // let fonts and animations settle
  await page.screenshot({ path: 'preview_full.png', fullPage: true });
  await browser.close();
})();
```

Viewport: match the page's own desktop layout (1400 wide is a good default; narrower if the content column is narrow). If the person asks for mobile, use 390 wide.

For a document built by a script (a PDF deck), show the existing rendered output rather than rerunning the build, unless a rebuild was asked for.

## Crop into readable sections

One full-page screenshot of a long page is unreadable. Cut it into sections about 900 to 1400 px tall.

```python
from PIL import Image
im = Image.open('preview_full.png')
w, h = im.size
n = max(1, round(h / 1200))
step = h // n
for i in range(n):
    bottom = h if i == n - 1 else (i + 1) * step
    im.crop((0, i * step, w, bottom)).save(f'preview_{i+1}.png')
```

## Check before sending

Look at every section yourself. Flag anything genuinely broken (missing image, overlapping text, layout collapse) instead of sending it silently. Embedded PDF frames often render blank in headless browsers; that is expected, not a bug.
Valid: "Section 3: the logo failed to load" alongside the images.
Invalid: sending a crop with overlapping headings and no comment.

## Deliver

Send all sections in one message with a one-line caption ("Current homepage, top to bottom.").
Valid: four images, one caption.
Invalid: a paragraph recapping each section the person can already see.

Then delete the temporary screenshots and render script.

## Proactive use

Right after a visual edit lands, just show the preview. That moment is unambiguous, so asking first only adds a round trip.

## Don't

- Ask which file when recent context answers it.
- Re-render untouched pages "to be thorough" unless the person asked for everything.
- Write a long summary of what is in the images.
