---
name: full-replace-write-safety
description: "Use before and immediately after any write to an existing document through a tool that replaces the whole document (a project or knowledge-base write, a wiki page save, a file overwrite, an API PUT of a full record) where there is no append, no patch, no version token and no locking. Covers reading fresh right before writing, checking that content you wrote earlier survived before merging against someone else's rewrite, merging into the full text instead of sending only the change, and reading back afterward to prove your content landed and the end of the document was not cut off."
---

# Full-replace write safety

Needs: none

## The trap

Many document tools have only one write: replace the entire document. Sending only a new or changed section silently deletes everything else. No warning, no diff, no confirmation.

This happens most in long sessions. The document was read early, a new section is drafted much later, and the write sends only the section. The rest of the history is gone.

## Two failure modes, not one

1. **Self-inflicted truncation.** You write a delta, or a long copy that is cut off, and wipe the rest. This one is loud: the document is visibly short.
2. **Another writer drops your content.** Full-replace writes are last-write-wins. Two sessions can each follow read, merge, write correctly and one still loses, because the loser's content was already missing from the version the winner read. This one is silent: it looks exactly like a document that never had the content.

The danger in the second case: the fresh read looks authoritative. Merging against it and writing permanently confirms the loss.

## Before the write

1. **Read the document immediately before writing.** Not an earlier read from the same conversation; the document may have changed since.
2. **Check that your earlier content is still there.** If you wrote to this document before, search the fresh read for a distinctive phrase from that content. If it is missing, another writer dropped it. Restore it in your merge and tell the person plainly that it went missing and you put it back.
3. **Merge into the full fresh text.** Never send a write containing only the change.
4. **Prefer one contiguous insertion.** Add new content at one point and copy everything else through unchanged. Scattered edits across a long copy are where transcription drift creeps in. Restructuring is what drops other writers' work; annotate in place instead.
5. **Write the complete merged document.**

- Valid: read now, confirm your section from this morning is still present, insert the new section at the top of the log, write the full text.
- Invalid: reuse the read from an hour ago and write only the new section.

## After the write: prove it landed

A success response does not prove the document is intact. Check both ends:

- **Your new content is present.** Search for a distinctive phrase from it. If it is missing, another writer saved between your read and your write. Redo the merge against a fresh read.
- **The end survived.** Search for a distinctive phrase from the last lines of the document. This catches a cut-off copy, the main risk of reproducing a long file.

A search is enough for both; a full re-read is not needed.

- Valid: "Wrote; new section found; closing line found."
- Invalid: "Write returned success, done."

## Recovery

- **Your own wipe, caught in the same conversation:** an earlier read of the document in this conversation is the last known good version. Write it back merged with the intended change, and tell the person what happened.
- **Your section dropped by another writer:** if your own earlier write is still in context, re-insert that exact text. If not, say plainly that it is gone and cannot be restored word for word. Do not paraphrase it back and present the paraphrase as the original.
- **No earlier read available:** there is no recovery from inside the session. Say so rather than guessing at content.

## What this cannot fix

This is a convention, not enforcement. Every writer has to follow it, and one that skips the checks can still confirm a deletion or leave a truncation unnoticed. If losses keep happening, the fix is structural: fewer writers on the same long document, a document split per workstream, or a store that supports append or version checks.
