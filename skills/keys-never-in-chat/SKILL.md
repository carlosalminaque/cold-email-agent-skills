---
name: keys-never-in-chat
description: "Use whenever an agent needs an API key or other secret: a new provider needs a key and no slot exists yet, a configured credential exists but runtime access is uncertain, or someone is about to paste a key into chat. The key gets a local out-of-band home that the person fills in their own editor, the agent uses it only through the configured protected route, never sees, prints, logs or relays it, and makes one harmless authenticated read before any authorized change."
---

# Keys never in chat

Needs: local shell

A key pasted into a chat message sits in conversation history, logs and reports. Treat that as a real exposure. An agent should also never scrape a key from a signed-in page, a browser session or the clipboard. The fix for both is a real local home for the key.

## A new key with no home yet

1. **Find the existing mechanism.** See where keys for tools the agent already uses live: an environment entry in the agent's local config, a secret store, an OS credential vault. Confirm it is still the live pattern.
2. **Create an empty slot** for the new tool, matching the existing naming exactly, for example `NEWTOOL_API_KEY = ""` in the same config section. Read it back: it exists once and is empty.
3. **Give the person exact steps:** the file to open, the line to find, "paste the key between the quotes, save, restart the agent".
4. **The person does this outside any AI-visible channel,** in their own editor.
5. **After they confirm,** check that the value is readable and non-empty without displaying or logging it, then use it.

## Using a configured credential

1. Use the configured protected route (a launcher, helper or credential binding that reads the secret in-process). Never read the vault from an ad-hoc command, even for a harmless probe.
2. Before an authorized change, make one harmless authenticated read of the smallest relevant object. Report only the status code and non-secret fields.
3. If it fails, report the exact category: credential unavailable to the runtime; rejected (401); transport failure before any response; valid but insufficient access (403 or 404). A transport failure does not make a key invalid.
4. If the protected route is unavailable, stop. Do not ask for the secret, extract it elsewhere, rotate it or switch to a weaker path.
5. After an authorized change, re-fetch the changed object and check the fields. The write response is not proof.

This skill covers access only. It does not authorize sends, deletes, launches, spending or any other action.

## Examples

Valid: "I added an empty `NEWTOOL_API_KEY` line to the config. Paste the key between the quotes in your editor, save, and restart me."

Invalid: "Just paste the key here this once and I'll set it up."
