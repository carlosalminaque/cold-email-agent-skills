---
name: browser-payload-transfer
description: "Use whenever a large payload that must arrive byte for byte (a JSON file, a config blob, an import file, anything over a few KB) has to get into a browser tab's JavaScript context during browser automation, for example to build an API request inside the page. Trigger on requests like get this file into the browser, load this payload into the page, paste this JSON into the tab, or any plan that relays large content across several script-evaluation calls. Replaces text-relay chunking (typing the content into tool-call arguments, raw or base64, with or without checksums), which is unreliable at scale, with a file upload into an injected file input read by FileReader and verified by byte length and SHA-256."
---

# Browser payload transfer

## The problem

Typing a large payload into script-evaluation tool calls is unreliable, however it is chunked or encoded. Two separate failure modes cause it:

1. **The agent's own transcription can silently change a character.** Copying long text from a file read into a tool-call argument can swap one character mid-string. Nothing errors.
2. **The tab's in-memory state can be dropped between calls.** A tab drop, a timeout or a tab id change wipes everything stored on `window` so far. Smaller chunks only mean less progress lost per drop.

Different encodings, chunk sizes and more checksums reduce the risk but never remove it. Every extra round trip is more exposure to both.

- Valid: upload the file from disk and read it inside the page.
- Invalid: send a 60 KB JSON file as twelve base64 chunks across twelve script calls.

## The method: upload into an injected file input

The content goes disk to file input to in-page JavaScript. No payload text ever passes through a tool-call argument.

1. **Inject a file input into the live page:**
   ```js
   (function(){
     let el = document.getElementById('__payload_upload__');
     if (el) el.remove();
     el = document.createElement('input');
     el.type = 'file';
     el.id = '__payload_upload__';
     el.style.position='fixed'; el.style.top='0'; el.style.left='0'; el.style.zIndex='999999';
     document.body.appendChild(el);
     return 'created';
   })();
   ```
2. **Find the element's reference** with the browser tool's element finder. If the page has other file inputs, the injected one is usually the last match because it was appended last.
3. **Upload the file from the local disk** with the browser tool's file-upload action, passing the absolute path and the element reference. Check that the reported size matches the source file.
4. **Read it in the page:**
   ```js
   const file = document.getElementById('__payload_upload__').files[0];
   window.__payload = await file.text();
   ```
   Confirm on the next call with `typeof window.__payload === 'string'` and its length. The async assignment may not show in the same call's return value.
5. **Verify byte for byte, not just presence.**
   - Byte length: `new TextEncoder().encode(window.__payload).length` must equal the source's byte size (`wc -c`). Compare bytes to bytes; `.length` counts UTF-16 units and differs when the file has multi-byte characters.
   - SHA-256: compute with `crypto.subtle.digest` in the page and compare to `sha256sum` of the source. Content filters sometimes block a raw hex digest as encoded data; if so, return it as an array of character codes and decode it outside the tool call.
6. **Clean up** the injected input once the payload is used.

- Valid: "Uploaded 48,213 bytes; in-page byte length 48,213; SHA-256 matches the local file."
- Invalid: "The payload is on window, length looks right."

## Do not use the site's own import button unless it truly replaces

Some import features merge into existing state instead of replacing it. Using the site's importer reproduces that behavior however cleanly the file arrived. An injected input bypasses the site's handler, so the agent decides what happens with the content (for example, building a clean API request body from it).

- Valid: inject your own input, then send a full-replace API request built from the payload.
- Invalid: use a canvas "import from file" button and assume it replaced the old graph.

## When this does not apply

- Payloads under about 1 to 2 KB are fine in a single direct script argument.
- If the file is not on local disk yet, fetch and save it first, then start at step 1.
- Browser file-upload tools often cap total size per call (commonly around 10 MB). Larger payloads need a different approach.
