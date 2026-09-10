# Repository guide for agents

This repository ships one skill: `skills/steve/SKILL.md`, invoked as `/steve`. It makes an agent reason like Steve Jobs about whatever the user is building — the verdict, the insight underneath, what to cut, the next move, the one sentence.

Layout:

- `skills/steve/SKILL.md` — the operations manual: modes, the reasoning loop, the rules, the shape of a reply. Keep it under 400 lines.
- `skills/steve/references/` — loaded on demand: `principles.md`, `quotes.md`, `episodes.md`, `voice.md`, `failures.md`, and one playbook per mode under `playbooks/`.
- `examples/` — real outputs. Regenerate them when a template changes.
- `docs/index.html` — the GitHub Pages site. One file, no build step.
- `.claude-plugin/` — plugin and marketplace manifests.

House rules when editing:

1. No quote without a source (venue, year, link) in `references/quotes.md`. This is the one rule that cannot bend.
2. Never write an imagined line as though it were something he said.
3. Attack the work, never the person.
4. Fewer words win. If a sentence does not change what the reader does, delete it.

See `CONTRIBUTING.md` for the longer version.
