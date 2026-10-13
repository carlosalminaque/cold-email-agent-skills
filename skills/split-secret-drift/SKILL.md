---
name: split-secret-drift
description: "Use when a call that used to work now fails with an unauthorized or invalid-key error, and the secret lives in two places kept in sync by hand, such as a raw key in a vault and its hash or copy in a server config. Isolates the failing credential with one safe read, checks stored values by shape and length without ever reading them, and rotates both sides from one held value in one sitting."
---

# Split-secret drift

Needs: none

Hand-rolled API key auth often keeps one secret in two homes: the raw key on the client side and a copy or hash on the server side. Every manual copy between them is a chance to drift: an extra space, a value left from an older attempt, or a new raw key whose hash was never recomputed. The comparison code is almost never the bug. The two stored values have stopped matching. Agents lose hours reading auth logic and request routing when one cheap check would have found it.

## When

- An auth error (unauthorized, invalid key, forbidden) on something that worked before or should work.
- The secret is split across two stores that a person or agent keeps in sync.

Not for first-time setup where the credential was never created. That is a missing secret, not drift.

## Steps

1. **Isolate by credential, not by operation.** If there is more than one key or scope (read and write, old and new), run the same cheap read-only call with each one.
   - One passes and one fails: the failing key is the problem. Stop looking at routing, fields or actions.
   - All fail the same way: the cause is shared (wrong endpoint, wrong deployed version, network). Investigate that instead.

2. **Check shape before logic.** Without reading the value, check its length, whether trimming changes it, and its character set. A hash has a fixed length for its algorithm (a base64 SHA-256 is 44 characters). A stored "hash" of the wrong length is not a hash, and you do not need to see it to know.

3. **Only then read the comparison code,** if steps 1 and 2 come back clean.

4. **Rotate atomically.** When both sides must be replaced:
   - generate the new value once, into one variable;
   - write every home (vault, server config, the hash step) from that same variable;
   - do it in one sitting and one terminal, never retyping or re-pasting the literal.

5. **Never expose the secret.** Every check here is a length, a boolean, an existence test or a name. Never print, log, echo or screenshot the value, even when asked to "just look at it".

6. **Verify in two stages.** First the cheapest safe read with the new key. Then the real operation. Then read the downstream state fresh, since a write call can report success while nothing changed.

7. **Get explicit approval for rotation.** Rotating a credential is a different kind of action from reading metadata. Ask the human at the moment of the fix. An earlier "keep going" does not cover it.

## Valid and Invalid

- Valid: "Same read call: read key passes, write key fails. The write key is the problem."
- Invalid: ten rounds tracing action routing and session caching before trying the other key.
- Valid: "The stored hash is 40 characters; a base64 SHA-256 is 44. It is not the hash of anything. Value not read."
- Invalid: "Can you paste the stored value so I can compare it?"
- Valid: one script that generates the key into a variable, writes the vault entry and the server hash from it, then runs a test read.
- Invalid: generate in one window, paste into the vault, hash it in another tool, paste the hash into the server the next morning.

## Before and after

- Before: a write key stopped working. Hours went into auth logic. The stored hash had the wrong length, and after that was fixed the raw key and the hash still did not correspond.
- After: the first step is one read per key, the second is a length check, and rotation is a single script with one held value.
