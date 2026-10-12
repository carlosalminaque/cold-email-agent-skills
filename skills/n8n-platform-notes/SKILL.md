---
name: n8n-platform-notes
description: "Reference for n8n platform behavior that holds no matter which tool drives it: versioning and publish semantics, stale-base publishes, the internal REST path versus the public API, URL importer blocks, the built-in AI Assistant, false session-expired redirects, and HTTP 200 responses that are really failures. Use before assuming an n8n write failed because of payload, technique or credentials, before publishing any workflow version, after any save to confirm the running version actually changed, and before trusting a multi-round test while others may edit the same workflows."
---

# n8n platform notes

Platform and API facts about n8n, separate from browser technique problems (screenshot timeouts, drag precision). Behavior can vary by n8n version and hosting; confirm on your own instance before relying on a specific endpoint.

## A save does not change what runs: you must publish

On versioned n8n, saving creates a new draft version but the active version stays the old one.

- After `PATCH /rest/workflows/{id}` you get a new `versionId` while `activeVersionId` is unchanged. Checking only node content or only `versionId` falsely reports the fix as live.
- Internal REST publish: `POST /rest/workflows/{id}/activate` with `{"versionId": "<draft versionId>"}` in the body; without it the call returns 400. On some versions `/rest/workflows/{id}/publish` returns 404.
- UI publish: header Publish button; confirm the pre-filled version matches your draft; click Publish through a resolved element reference, not screenshot coordinates.
- After any save, re-GET and assert `activeVersionId === versionId` and that the intended content is in the active version.
- Sub-workflows called through Execute Workflow run the published version, not the latest draft.
- Valid: "GET shows activeVersionId equals the new versionId and the new code is in it."
- Invalid: "PATCH returned 200, the fix is live."

## Publishing does not reject a stale base

There may be no compare-and-swap: an older version can be activated over a newer one with no error, so two people or agents editing one workflow silently overwrite each other.

- Before saving, re-GET and compare `versionId` and `activeVersionId` to what your draft was built from. If either moved, rebuild against the newer version.
- Immediately before activating, re-GET again and abort if the base changed.
- After publishing, the GET is the proof, never the publish response.
- Version history shows the account holder, not which agent made a change. Name versions with a workstream, a date and a one-line purpose, and put base and draft ids in the description.
- Valid: "Base unchanged since draft; activated; GET confirms."
- Invalid: publish a draft built yesterday without re-reading the live version.

## Run scripted REST calls from a light page

Scripted `fetch('/rest/...')` from a tab on the heavy editor canvas can hang until the automation timeout, while the same call from the workflow list page returns at once. Do scripted reads and writes from the list page, go to the editor only for UI clicks, and keep nothing important on `window` across navigation.

## Public API versus internal path

- The public API (`/api/v1/workflows`) with an API key and the internal path (`/rest/workflows/{id}`, same-origin session cookie) are different code paths. One can fail while the other works.
- If a valid public-API write returns a bare 500 while reads work and bad payloads correctly get 400, suspect the instance, not your payload or key. Try the internal path or an editor save before re-diagnosing credentials. An internal save still needs a publish.
- On the public API, `/activate` is deprecated in favor of `/publish`. On the internal path it can be the reverse. Do not mix the two.
- Valid: "Public write 500s, internal PATCH works; switching paths."
- Invalid: rotate the API key three times for a 500 on a valid payload.

## URL importer blocked

"The request was blocked because it resolves to a restricted IP address" is n8n's SSRF protection, not a tool limit. Do not retry the URL importer; GET and PATCH the workflow through REST, then publish.

## Built-in AI Assistant

The editor's AI Assistant edits workflows through n8n's own API. It avoids canvas drag problems and public-API faults, and handles connections and node content (code, parameters, credential selection).

- Name the exact source and target nodes, and for IF or Switch nodes the output branch. Ask it to show the diff first and touch nothing else.
- It works one workflow at a time in a live chat; it cannot do unattended or batch work.
- Verifying edges: canvas edge labels are keyed by node id, not name. Filtering by name returns zero even when the edge exists. Resolve each node's id from the DOM and filter by that.

## A false session-expired redirect

If the workflow list loads with real data but opening one specific workflow sends that tab to sign-in with a session-expired flag, the session is valid. The fault is local to that workflow and tab. Stop re-signing in; check the workflow from another tool or session. If that reads real data, the workflow is fine.

## HTTP 200 is not success

Some backends (Google Apps Script is a common one) return HTTP 200 carrying an error or lock-timeout HTML page, and the HTTP Request node treats it as success. Validate the body shape on every such call: expected JSON, expected fields, matching ids. Treat anything else as failure, retry transient errors with backoff and jitter, and on exhaustion alert and fail the execution.

- Valid: node checks `body.ok === true` and the returned id matches, else throws.
- Invalid: node checks only that the status code is 200.

## Freeze workflows under test

A multi-round test is evidence only for the version each round ran on. Freeze every workflow in the path during the test, or record which versions each round used. Nothing on the platform stops someone republishing mid-test.
