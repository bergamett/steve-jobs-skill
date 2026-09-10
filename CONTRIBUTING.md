# Contributing

The skill lives in `skills/steve/`. Everything else in the repo exists to explain it or install it.

## The one rule

**No unsourced quotes.** If you add a line to `skills/steve/references/quotes.md`, it comes with the venue, the year and a link to a transcript, a published interview, a keynote recording or a document he wrote. If the wording varies between published transcripts, mark it `[near-verbatim]`. If a first-hand witness reports it rather than a recording capturing it, mark it `[reported]` and name the witness.

If you cannot source it, it does not go in. This is the only thing that makes the skill trustworthy, and it takes one bad quote to lose that.

## What good contributions look like

- **A better playbook.** The mode playbooks in `skills/steve/references/playbooks/` are the working parts. If a mode gives weak answers on a kind of input you care about, fix the steps, the template or the traps.
- **A sourced quote or episode** that earns its place. Not more of them; better ones. The reference files are already at the length where adding costs something.
- **A real example.** Run the skill on something of yours, and if the output is good, add it to `examples/` in the same format as the others. Real inputs beat invented ones.
- **A correction.** If a quote here is misattributed, open an issue with the evidence. That is the most valuable issue you can file.
- **A case where the skill is wrong.** `skills/steve/references/failures.md` lists the domains where his intuition should not be followed. If you find another, add it.

## What will be declined

- Making it more of an impression. The persona is a lens, not a costume.
- Insults. The skill is unsparing about the work and says nothing about the person who made it.
- Growing `SKILL.md`. It is the operations manual and stays under 400 lines. Long material goes to `references/` and gets loaded on demand.
- Biography, trivia, timelines. Other skills do that.
- Invented quotes, invented anecdotes, or claims about what he thought about anything after October 2011.

## Testing a change

`python3 scripts/check_sources.py` runs the checks that gate every pull request: every quote carries a venue, a year and a link; no line from the never-use table appears anywhere as real; the manifests are valid; `SKILL.md` stays inside its line budget and every reference it names exists. Run it before you push.

If you touched the skill, rebuild the single-file version too: `python3 scripts/build_single_file.py`.

Then judge the change the only way that matters:

1. Install the skill locally: `cp -r skills/steve ~/.claude/skills/steve`
2. Run it on three real things: a README, a roadmap, a landing page.
3. Compare against the same prompts without the skill. If the skill's answer is not clearly better and clearly shorter, the change is not ready.
4. Check the reply against the rules in `SKILL.md`: verdict first, one screen, something rewritten at the end, quotes sourced, imagined lines marked.

## Style

Short sentences. Plain words. Explain why a rule exists rather than shouting it. The skill tells a model to write that way, so the skill should be written that way too.
