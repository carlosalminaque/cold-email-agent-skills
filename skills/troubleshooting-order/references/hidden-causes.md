# Hidden causes: what each looks like and the cheap check

| Cause | Typical sign | Cheap check |
|---|---|---|
| Wrong target | The fix "worked" but nothing changed | Print the exact ID, path or version you edited, and the one the live system runs |
| Wrong account | Data looks almost right but belongs to someone else | Ask the tool who it is signed in as |
| Stale state | The page or file shows an old value after a change | Reload from source, bypass caches, compare timestamps |
| Hidden branch | Some inputs work, others fail with no clear pattern | Find every fallback, redirect or "else" path and log which one ran |
| Permissions | A generic error, or an empty result instead of an error | Run the same read as an account known to have access |
| Never saved | The editor shows the change; the live system does not | Read the deployed or committed copy, not the editor |
| Tool drives another target | Actions land somewhere you are not looking | List the devices, tabs or browsers the tool is bound to |
| Limit above the session | A brand new session fails in exactly the same way | Check account-level settings: active sessions, plan limits, org policy |

## Two traps

- **Taking an error message's own advice on faith.** An error that says "try reconnecting" names one possible cause. Record only what verifiably fixed the problem.
- **Diagnosing two tools under one theory.** Two connections that fail at the same time can fail for different reasons. A fix for one says nothing about the other until each is checked on its own.

## When a fresh session is the fix

Some connections bind to whatever was running when the session started and do not rebind later. Once the thing on the other end is confirmed running, a brand new session is the fix. Say so plainly instead of retrying the same call in the old session.
