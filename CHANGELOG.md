# Changelog

## 1.0.0

First release.

- Six modes: `verdict`, `why`, `cut`, `next`, `pitch`, `email`.
- `SKILL.md` at 122 lines; references loaded on demand: principles, quotes, episodes, voice, failures, and one playbook per mode.
- 70 quotes, each with venue, year, link and a confidence marker, plus a table of famous lines he never said. `scripts/check_sources.py` enforces this in continuous integration.
- Eight real example outputs, including the skill's review of this repository's own README and the same question asked without the skill.
- `dist/steve-full.md`: the skill flattened into one file for chat windows and agents that cannot read a folder.
- Installable with `npx skills add`, by copying the folder, or from the Claude Code plugin manager as `steve@bergamett`. The first two give the command `/steve`; plugin skills are namespaced by Claude Code, so that path gives `/steve:steve`.
- GitHub Pages site under `docs/`.
