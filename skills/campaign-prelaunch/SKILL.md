---
name: campaign-prelaunch
description: "Use when the person says prelaunch, run pre-launch, or stage the campaign for a cold email campaign in a sending tool such as Smartlead, Instantly or similar. Checks that the enrichment and lookup tools are actually live with a real cheap call, sources and verifies the leads, drafts the sequence for approval, configures the campaign, and stops at the review step right before launch. Never clicks launch or sends anything without an explicit go-ahead in chat. Surfaces questions and a plain recommendation at each real decision point instead of running silently to a final report."
---

# Campaign prelaunch

Needs: browser control

Get a cold email campaign fully staged and ready to fire, without firing it. The run ends at the launch button with everything configured and the copy approved, waiting for the person's explicit go.

Raise questions and a plain recommendation at each real decision point (a sourcing result, a tool failure, a fork in approach) as you go. Do not run the whole thing silently and report only at the end.

## Step 0: prove the lookup tools are live

Before sourcing, make one real, free or cheap call to each enrichment or address lookup tool you will use. A "connected" status in a settings list is not proof; integrations often show connected while the actual session has expired.

1. **Primary lookup tool first.** If the person has set a provider order (for example, the cheaper or already-paid provider first, the second provider only for misses), check the primary one and record its balance. If it fails, stop lookup work, say so in the first status line, and do not quietly switch the order without a yes.
2. **Secondary tool.** Call a credit-check or similar no-cost endpoint.
3. **If a tool's session has expired,** tell the person where the reconnect button is and ask them to click it. Then retest. A reconnect does not always fix a session that was already running; if the retest still fails, say a fresh session may be needed, and note what waits on it rather than looping retries.

Valid: "Primary lookup answered, balance 3,180. Secondary failed: session expired. Reconnect is in your connector settings; misses will wait until then." Invalid: "Both tools show connected, starting sourcing."

## Step 1: source and verify the leads

- New prospects: run the person's own prospecting method or skill for the target segment.
- A specific person or company the person already named: confirm the target, then pull and verify contact details directly. Do not run full fit qualification on someone they already chose.
- Respect the provider order. Every sourcing report states lookups sent, found, and balance before and after, for each provider.

Valid: "Lookups: primary 40 sent, 31 found (balance 3,180 to 3,140); secondary 9 misses sent, 4 found." Invalid: "Found emails for most of the list."

## Step 2: set up the campaign

- Run any acceptance gate the person uses (fit check, capacity check, offer choice) before building anything.
- Draft the sequence (first email and follow-ups) with the person's own copy rules. This is always a draft for their approval.
- Configure the campaign: details, sequence steps, schedule, sending accounts, lead import.
- After each step, verify it landed by reading the live state (the lead list actually shows the records, the steps actually saved). The UI moving to the next screen is not proof.

### Per-lead copy does not need one campaign per lead

Most sending tools support custom fields on lead import, and any of them, including a fully written subject line and body, can be merged into the template. For individually researched copy at volume in one campaign: write each lead's subject and body upstream, import them as custom fields, and set the sequence template to just those two variables. The in-app editor applies one shared body only because that is what typing into it does, not because the platform cannot vary copy.

For a handful of leads either approach works. Past that, the custom-field approach scales; flag the switch as a real choice to the person rather than assuming it.

Valid: "One campaign, template is just the subject and body variables, 24 leads each with their own copy." Invalid: "The tool can't send different copy per lead, so I made 24 campaigns."

## Stop condition

Get to the review step, fully configured, with the copy approved. **Do not click launch.** Report that it is staged and ask for an explicit go-ahead in chat. A request to "prelaunch" is not permission to send.

Valid: "Staged at Review: 24 leads, 3 steps, schedule 9 to 5 weekdays in the leads' timezone. Say go and I'll launch." Invalid: Launching because everything checked out.

## Wrap-up: log only what is real

Do not force a log entry just to close out the run. Activity logs in a CRM usually fill from real sends and replies, and a prelaunch run has neither yet. If the run surfaced something worth remembering (a tool outage, a naming mix-up, a wrong assumption caught), log it wherever the person keeps lessons learned. If nothing came up, say so and skip it.
