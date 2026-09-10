# steve-jobs-skill

This repository ships one skill: `skills/steve/SKILL.md` (command `/steve`). It makes Claude reason like Steve Jobs about whatever the user is building.

- `skills/steve/SKILL.md` is the operations manual: modes, the reasoning loop, rules, output templates. Keep it under 400 lines.
- `skills/steve/references/` holds the material loaded on demand: sourced quotes, decision episodes, principles, voice, failures, and one playbook per mode.
- `examples/` are real outputs produced by running the skill. Regenerate them when the skill changes materially.
- `docs/index.html` is the GitHub Pages site (published from the `docs/` folder). Single file, no build step.
- `.claude-plugin/` makes the repo installable as a Claude Code plugin marketplace (`/plugin marketplace add bergamett/steve-jobs-skill`).

House rules when editing the skill: never add a quote without a source (year, venue, link) to `references/quotes.md`; never add an imagined line as if it were real; attack the work, never the person; fewer words win.
