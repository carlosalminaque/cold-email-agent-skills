---
name: docx-table-page-breaks
description: "Use when building a .docx with the docx JavaScript library (docx-js) and any table might fall across a page break. A heading and table header can get stranded at the bottom of one page while the rows start on the next with no repeated header, which reads as a broken table, especially in online document previews. Covers the three settings that fix it together and how to verify it by rendering."
---

# docx tables across page breaks

Needs: local shell

## The defect

When a table lands near the end of a page, three things can go wrong at once:

- The heading above the table and the table's header row are left alone at the bottom of a page.
- The data rows start fresh on the next page with no header above them.
- A single tall row is torn in half across the page boundary.

To a reader this looks like a corrupt or detached table. It is most visible in online previews of the file.

## The fix: all three settings together

1. `tableHeader: true` on the header `TableRow`. The header repeats on every page the table continues onto.
2. `cantSplit: true` on every `TableRow`, header and body. A row's content is never torn across a page.
3. `keepNext: true` on the heading `Paragraph` right before the table. The heading stays with the table. If heading and table cannot start on the current page together, the block moves to the next page as one unit.

```js
new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true,
  children: [new TextRun("Results")] }),
new Table({ rows: [
  new TableRow({ tableHeader: true, cantSplit: true, children: headerCells }),
  ...data.map(d => new TableRow({ cantSplit: true, children: cellsFor(d) })),
]}),
```

- Valid: header row has `tableHeader` and `cantSplit`, every body row has `cantSplit`, heading has `keepNext`
- Invalid: only `tableHeader: true` set, so the heading can still be orphaned and rows can still split

Why all three: each one fixes a different part. The repeated header alone still leaves an orphaned heading; `keepNext` alone still lets a row tear.

## Verify by rendering every page

Convert the file to PDF (for example `soffice --headless --convert-to pdf out.docx`), turn the pages into images, and look at each page.

This defect only appears when a table actually falls near a page boundary in that specific document. A short test file can pass while the real document, with more content above the table, fails. So verify on the real content, after the final edit.

- Valid: "Rendered the final 9-page file; tables on pages 4 and 7 cross a break and show the header on both pages."
- Invalid: "Rendered a one-page test table, looked fine, shipped the full report."
