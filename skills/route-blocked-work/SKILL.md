---
name: route-blocked-work
description: Use whenever an agent is blocked (a tool refusal on authorized work, a login it cannot do, a missing credential or access method, a policy or launcher refusal) and always before telling the human to do something by hand. Classifies the block, tries the other agents in a fixed order, writes the handoff in the same turn, and names the durable fix so the same block does not come back.
---

# Route blocked work, then remove the blocker

A solo operator often runs several agents, each with different reach: a cloud assistant, a local coding agent, a builder with write access to the project, and a runner on the user's own machine that holds their saved credentials. When one agent hits a wall, the lazy answer is "please do this by hand". That turns the human into the fallback for every limit of every tool. The better answer is to try the other agents first, hand the work over in the same reply, and fix whatever caused the wall so it does not happen again next week.

## When

- An agent's tool refuses an action the human already authorized.
- A step needs a password, an OAuth login or a credential the agent does not hold.
- A launcher, sandbox or policy check rejects a write.
- The agent is about to write "you'll need to do this manually".

## Steps

1. **Classify the block.**
   - *A business decision* (price, wording, scope, risk): give it to the human with a recommendation. Not a routing problem.
   - *A one-off hiccup:* retry once with a small change. A refusal that clears on retry was transient.
   - *A limit of this agent* (a refusal on an authorized write, a credential rule, a device-control limit): route it, step 2.
   - *A structural gap* (no credential, no durable access method, wrong tool for this class of task): route it now and fix it, step 4.
   - *A real boundary* (not authorized, permanent deletion, spend, sending, publishing): stays gated on the human's explicit yes, whichever agent runs it.

2. **Try agents in a fixed order, every time.** Keep a short capability ledger (what each agent can and cannot do, with the evidence) and read it first. Write any new test result to it in the same turn.
   1. **This agent.** "I can't" needs a real failed attempt, not a guess.
   2. **The local coding agent and the builder,** across every method they have: browser automation, a direct API or connector call, native computer control. One method failing is evidence about that method only.
   3. **The credentialed runner on the user's machine,** for what the ledger lists as a gap for the others, or what was just refused for them.
   4. **The human,** only for what no agent can do: their own approval, spend, card entry, a second-factor code.

3. **Write the handoff in the same turn.** Never report "blocked" in one message and the handoff in the next. The handoff opens with one line saying why it cannot be done where the block happened. Inside it:
   - the outcome that must be true, with exact content, not the clicks to get there;
   - start conditions the recipient can check itself;
   - run each action once, save each output, stop and report on anything other than the pass criteria;
   - never print or save a secret value, change nothing not listed;
   - a live readback that proves it worked.

   Verify the result from live state or saved receipts, not from the recipient's chat summary. Never let two executors work on the same files at once.

4. **Remove the blocker.** When the block is structural, the same reply names the durable fix: the supported mechanism that removes the whole class of block (a proper stored credential, the official API instead of UI clicks, a corrected default setting). Before accepting "X is not possible", trace the claim to a cited fact (a doc, an error message, a test). Then ask: if this exact block happened next week, would it already be prevented? If not, call the fix a stopgap.

## Valid and Invalid

- Valid: "The cloud assistant's pause action was refused twice. The runner on your machine holds the API key, so here is its prompt: pause the campaign through the API, read back status paused. Durable fix: give the builder a scoped API key so this never needs the runner again."
- Invalid: "I'm blocked. Click Pause in the dashboard yourself."
- Valid: trying the builder's direct API path after its browser path failed, before escalating.
- Invalid: "The builder can't do it" after one refused browser click.
- Invalid: routing a send or a deletion to another agent to get around the human's approval.

## Before and after

- Before: every refusal became a manual chore, and the same login wall came back weekly.
- After: blocks route to the agent that can do them in one reply, and each structural block ends with a credential or API path that retires it.
