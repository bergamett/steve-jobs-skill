# Publishing checklist

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

## 4. Check the install paths work

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

## 5. Before announcing

Run the skill on this repository's own README and fix whatever it says. That is both the honest thing to do and the demo:

```
/steve verdict README.md
```
