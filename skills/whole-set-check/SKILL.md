---
name: whole-set-check
description: "Inventory and verify an entire requested set so missing or unclassified items cannot hide behind a passing sample."
---

# Whole set check

Needs: Readable source inventory and access to every item in the requested scope.

## Declare the complete set

Enumerate source items and record one classification per item: included, covered by another item, alias or excluded with a reason. Compare both directions for missing and stale rows.

- Valid: compare installed folders with inventory rows and report both set differences.
- Invalid: inspect five examples and call the whole collection checked.

## Verify outputs as a set

Compare expected output names with actual output names, then run the relevant validation for every included item. A total count alone cannot detect a missing item replaced by an extra one.

- Valid: exact name equality plus validation of every skill.
- Invalid: accept matching folder counts with different names.

## Expose gaps

List every unreadable, unclassified or failed item and preserve its evidence. Do not mark the set complete while any required item is unverified.

- Valid: identify two inaccessible entries and report a partial result.
- Invalid: silently omit inaccessible entries from the denominator.
