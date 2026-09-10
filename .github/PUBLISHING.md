# Publishing checklist

Everything that could be done from a commit is done. What is left lives in GitHub's settings, which this repository's automation is not allowed to touch. Five minutes, in this order. Exact values to paste are given; the launch copy is in `LAUNCH.md` next to this file.

## 1. Default branch → `main`  (30 seconds)

`main` already exists and is identical to `claude/steve-jobs-skill-qw40tx` (same commit). Settings → General → **Default branch** → switch icon → choose `main` → Update.

Then delete the old branch: Code → Branches → trash icon next to `claude/steve-jobs-skill-qw40tx`. Nothing in the repository hard-codes a branch name: links use `HEAD`, the plugin manifests use `./`, `npx skills` reads whatever the default is.

## 2. Website  (30 seconds)

Settings → Pages → Source: **Deploy from a branch** → Branch: `main`, Folder: **`/docs`** → Save.

Live a minute later at <https://bergamett.github.io/steve-jobs-skill/>. `docs/.nojekyll` is already there, so the HTML is served as-is with no build.

## 3. Description, website, topics  (1 minute)

Repository home page → gear icon next to "About".

Description:

```
Not a Steve Jobs chatbot. A Steve Jobs review. A Claude Code skill that reads your repo and answers in one screen: verdict, three findings, a rewrite. 70 quotes, every one sourced.
```

Website: `https://bergamett.github.io/steve-jobs-skill/`

Topics (paste one at a time):

```
claude-code  claude-skills  agent-skills  skill  steve-jobs  product-management  product-design  ai-agents  developer-tools  claude
```

Untick "Releases", "Packages" and "Deployments" if you want the sidebar quiet; leave "Releases" if you do step 5.

## 4. Social preview  (30 seconds)

Settings → General → Social preview → Upload an image → `assets/social-preview.png` (1280×640, already generated, same picture as the README hero).

This is the image that appears when the link is shared on X, Slack, LinkedIn or Discord. Without it the unfurl is a grey box.

## 5. Release  (1 minute)

Releases → Draft a new release → "Choose a tag" → type `v1.0.0` → "Create new tag on publish" → Target: `main` → Title: `Ask Steve 1.0.0` → paste the `1.0.0` section of `CHANGELOG.md` → Publish.

That gives the plugin manifest's `version: 1.0.0` something to point at and gives people a stable link.

## 6. Check the two install paths  (1 minute)

In Claude Code:

```
/plugin marketplace add bergamett/steve-jobs-skill
/plugin install steve@steve
/steve verdict README.md
```

In any terminal:

```
npx skills add bergamett/steve-jobs-skill
```

## 7. Post

`LAUNCH.md` has the Show HN title and first comment, the X post, the Reddit post. Post Show HN first, on a weekday morning US time, and answer every comment for the first two hours; that is what moves the ranking. When someone says "isn't this just a prompt", link `examples/_baseline-no-skill.md` next to `examples/next-move.md` and nothing else.

## Keeping it honest afterwards

- Any change to the skill: `python3 scripts/check_sources.py` then `python3 scripts/build_single_file.py`, and commit `dist/steve-full.md` with it. Continuous integration fails otherwise.
- Any material change to the README: run `/steve verdict README.md` again. The self-review is the demo, and a demo that no longer matches the page is the first thing a visitor notices.
- New quotes only with venue, year, link and a confidence marker. That rule is the product.
