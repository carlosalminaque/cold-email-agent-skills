---
name: single-source-of-truth
description: "Use whenever a rule, price, approved text, target or decision changes, whenever a human corrects the agent, and whenever two files are found saying different things about the same topic. Keeps every fact in exactly one source listed in a source map, replaces copies with pointers, retires the old wording in the same change, and runs a sweep before calling it done."
---

# One source

Needs: none

Agents copy. A rule stated in a prompt, a memory file, a skill and a wiki page will be stated four slightly different ways within a week, and the agent that reads the stale copy acts on it. The cure is one source per topic and a pointer everywhere else.

## The source map

Keep one file, `SOURCE-MAP.md`, at the root of the project. One row per topic:

| Topic | The one source | Who may edit it | Generated copies |
|---|---|---|---|
| Pricing | `kb/pricing.md` | owner only | `site/pricing.html` (built from it) |
| First-email rules | `rules/messaging.md` | owner, via review | `rules/messaging.generated.md` |

The map holds no facts itself. It only says where each fact lives.

## Steps

1. **Find the owner.** Read the source map. If no row fits the topic, add one before writing anything else.
2. **Change only the source.** Write the change there, dated, with the reason and one Valid and one Invalid example.
3. **Retire the old version in the same change.** Add the old wording's tell-tale phrase to a "retired wording" list in the source. Use exact phrases, never a bare word that is still valid elsewhere ("old trial pricing", not "trial").
4. **Replace copies with pointers.** Search prompts, agent instructions, memory, decision notes, the website and any scripts for the old version. A rule written out anywhere else becomes one line: "See `<source>`."
5. **Treat public pages as outputs.** Website copy, decks and video scripts are not sources. Edit them to match, then list them in the sweep.
6. **Run the checks.** A script greps every live surface for the retired phrases. Done means zero hits, and every live template matching an approved text in the source.
7. **Report the source, not the copies.** End with `Fixed in: <the one source>`. Never a list of the places a rule was pasted into.

## The sweep script

The minimum version is a list of retired phrases read from the source and a grep across the surfaces in the map:

```bash
# retired.txt is generated from the source's "retired wording" section
grep -rniF -f retired.txt site/ prompts/ templates/ && echo "FAIL: retired wording still live" && exit 1
echo "PASS: 0 retired phrases live"
```

Run it in CI or as a pre-publish step so nobody has to remember it.

## Multiple clients

Each client gets its own sources (offer, ideal customer, approved texts, retired wording), registered as rows in the map before any copy is written. Your house rules apply only where the client's source is silent. Every client campaign is checked against that client's approved texts, never against yours.

## Valid and Invalid

- Valid: "Dropped the shared chat channel from the offer. Changed in `kb/offer.md`, phrase added to its retired list, homepage line edited to match, sweep: 0 hits. Fixed in: `kb/offer.md`."
- Invalid: the same decision written into memory, the agent instructions, a skill and the wiki in four different wordings.
- Invalid: a client's first email checked against your own agency's approved texts.

## Before and after

- Before: a price changed on the website, but the reply-drafting prompt still held the old number in its own words. A prospect was quoted the old price.
- After: the drafting prompt says "Read prices from `kb/pricing.md`". The price changes in one place, and the sweep fails the publish if the old number still appears anywhere.
