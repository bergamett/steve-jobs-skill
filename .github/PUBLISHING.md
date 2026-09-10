# Publishing checklist

The launch copy — Show HN title, first comment, X post, Reddit post, repo description — is in `LAUNCH.md` next to this file. The skill wrote it about itself with `/steve pitch`.

Two things have to be switched on in GitHub's web interface. Neither can be done from a commit.

## 1. Turn on the website

Settings → Pages → **Source: Deploy from a branch** → branch: the branch this code is on → folder: **`/docs`** → Save.

A minute later the site is live at <https://bergamett.github.io/steve-jobs-skill/>. `docs/.nojekyll` is already there so the HTML is served as-is with no build step.

## 2. Set the social preview

Settings → General → Social preview → **Upload an image** → `assets/social-preview.png` (1280×640, already generated).

That is the picture that appears when the repo is shared on X, Slack, LinkedIn or Discord. Without it, the unfurl shows a generic grey box with the repo name.

## 3. Repository description and topics

Description: `Not a Steve Jobs chatbot. A Steve Jobs review. A skill for Claude Code.`
Website: `https://bergamett.github.io/steve-jobs-skill/`
Topics: `claude-code`, `claude-skills`, `agent-skills`, `skill`, `steve-jobs`, `product-management`, `ai-agents`, `product-design`

## 4. Give the default branch a plain name

The code landed on `claude/steve-jobs-skill-qw40tx`, which became the default branch because the repository was empty. Settings → Branches → rename it to `main`. GitHub redirects the old name, and nothing in the repo hard-codes a branch: every link uses `HEAD`, the plugin manifests use `./`, and `npx skills` reads whatever the default is.

## 5. Check the install paths work

After the branch is the default branch (it already is, since the repository was empty when this landed):

```
/plugin marketplace add bergamett/steve-jobs-skill
/plugin install steve@steve
```

and

```
npx skills add bergamett/steve-jobs-skill
```

`npx skills` finds `skills/steve/SKILL.md` on its own; the plugin path reads `.claude-plugin/marketplace.json`, which declares one plugin named `steve` with source `./`. If you later rename the default branch, nothing here needs to change.

## 6. Before announcing

Already done once: the skill was run on this repository's README, the review is in `examples/self-verdict.md`, and every finding was fixed. Do it again whenever the README changes materially — it is both the honest check and the demo.

```
/steve verdict README.md
```

`python3 scripts/check_sources.py` runs the same checks continuous integration runs, and `python3 scripts/build_single_file.py` rebuilds `dist/steve-full.md` after any edit to the skill.

## 7. Publish the release

Releases → Draft a new release → "Choose a tag" → type `v1.0.0` and pick "Create new tag on publish" → title `Ask Steve 1.0.0` → paste the 1.0.0 section of `CHANGELOG.md` → Publish. That gives the plugin manifest's `version: 1.0.0` something to point at, and gives people a stable link to share.
