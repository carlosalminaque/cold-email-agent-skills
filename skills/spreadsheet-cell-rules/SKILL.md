---
name: spreadsheet-cell-rules
description: "Use whenever building, editing or reviewing a spreadsheet that a person will read: a lead list, tracker, CRM export, report or demo sheet, in .xlsx (openpyxl or similar), Google Sheets or CSV. Covers two silent defects. First, cell content: no blank or lone-dash cells by default, every value must fit the row's status, and totals must not count the new explanatory phrases. Second, rendering: cells with wrap text on need a row height computed from the tallest wrapped cell, or the extra lines are clipped with no error. Ends with a mandatory render-and-read review before calling the sheet done."
---

# Spreadsheet cell rules

Needs: local shell

A sheet can hold correct data and still read as broken. These rules catch the two most common ways: cells that look empty or contradictory, and wrapped text that gets cut off by the row height. Neither shows up in a check of the raw values.

## Rule 1: no blank or lone-dash cells by default

A cell that does not apply says why, in a short phrase written in the same style as the real status values.

- Valid: Next follow-up = `Stopped (bounced)`; Replied? = `Not sent yet`; Follow-up sent? = `N/A (opted out)`
- Invalid: `-`, a long dash, or an empty cell in a column where other rows have values

Why: at a glance, and especially in a screenshot or video, a dash or empty cell reads as missing or broken data. Table accessibility guidance also prefers explicit text such as "Not applicable" over dashes or blanks.

Blank is allowed only when there is a clear reason, it is used the same way across the whole sheet, and a better option was considered first.

## Rule 2: every value fits the row's status

Read each row as a story. Contradictions to catch:

- A queued, not-yet-sent row carrying a computed follow-up date. It should read `After first send`.
- A replied or opted-out row still showing an automated stop date.
- A note that repeats another column. Use the note for information found nowhere else, such as the detail used to personalize the message.

- Valid: Status `Queued`, Next follow-up `After first send`
- Invalid: Status `Queued`, Next follow-up `March 14`

## Rule 3: formulas must not count the new phrases

If totals use COUNTIF or similar on values like `Yes`, `Bounced` or `Do not contact`, confirm the new explanatory phrases are not matched, then recount a few by hand. Keep cached values saved in the file so attachment previews do not show blank totals.

- Valid: `=COUNTIF(D:D,"Yes")` after confirming no cell reads `Yes (auto)`
- Invalid: `=COUNTIF(D:D,"*Yes*")` that now also counts `Not yet (Yes pending)`

## Rule 4: wrapped cells need a computed row height

Turning on wrap text makes a long cell break onto several lines inside the cell, but it does not grow the row. If the row stays at its default single-line height, or keeps a height copied from a shorter draft, lines two and beyond are clipped at the row edge. No error, no warning, and the value reads back correctly in code. To a reader it looks like missing fields.

Compute the height per row from the tallest wrapped cell in that row:

1. For each wrapped column, get its width (openpyxl: `ws.column_dimensions[letter].width`).
2. Estimate characters per line as `int(width * 1.1)`. That is a fair approximation for an 11 pt default font.
3. Word-wrap each cell's text at that count to get its line count.
4. Take the largest line count in the row.
5. Set the row height to `lines * 15 + 4` points (about 15 pt per line plus padding).

```python
def lines_needed(text, width):
    if not text:
        return 1
    per_line = max(1, int(width * 1.1))
    lines, cur = 1, 0
    for word in str(text).split(" "):
        wl = len(word) + 1
        if cur + wl > per_line:
            lines += 1
            cur = wl
        else:
            cur += wl
    return lines

for r in range(first_row, last_row + 1):
    most = max(lines_needed(ws.cell(row=r, column=c).value, widths[c])
               for c in wrapped_cols)
    ws.row_dimensions[r].height = max(default_height, most * 15 + 4)
```

- Valid: row heights set per row from the tallest wrapped cell
- Invalid: one uniform row height for the whole table when a Notes column varies in length

## Review step (required before calling a sheet done)

1. Render the sheet the way the reader will see it. For a file: convert to PDF (for example `soffice --headless --convert-to pdf out.xlsx`) and turn the pages into images (`pdftoppm -jpeg -r 150 out.pdf page`).
2. Look at every page image, not a spot check. Clipping only appears on rows whose content needs more lines than the row was given.
3. Read the sheet once as the recipient, cell by cell. Checklist passes (alignment, totals, text recognition) do not catch empty-looking cells or contradictory values.

- Valid: "Rendered all 3 pages; row 17 Notes was clipped, fixed its height, re-rendered."
- Invalid: "Values read back correctly in code, so the sheet is done."
