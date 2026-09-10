# Launch kit

Written by the skill itself: `/steve pitch` pointed at this repository. Nothing below has been edited.

Rules for the drafts: every claim must be checkable in the repository (numbers like "70 quotes", "123 lines", "eight examples" are fine; "revolutionary" is not). The skill's own rules on voice apply to the posts too: no corporate words, no exclamation marks, no emoji.

---

**Mode:** pitch · this repository, launch day

*I read the README, `SKILL.md`, the six playbooks, `quotes.md`, `docs/index.html`, the plugin manifests, the CI script and all five commits, and I ran `scripts/check_sources.py`. I could not install the plugin from GitHub or watch a stranger's first run.*

**The one thing.** "Somebody with taste looks at the thing you actually made, today, and says the sentence you have been avoiding — and you can check that not one word of it was made up."

**Headline.** Not a Steve Jobs chatbot. A Steve Jobs review.
It already won. Eight words, it names the enemy, and your own verdict mode picked it out one commit ago. Keep it.
Runners-up: "The build fails if he never said it." — the best proof in the repo and the line Hacker News will respect most, but it sells the fence, not the house; nobody installs a review for its footnotes. "It reviewed its own README. The verdict is the README." — true and the right picture, but that is the demo, not the headline, and it belongs directly under the headline, where it already sits.

**Three things.**
1. It holds the thing. Point it at a README, a roadmap or a diff; it reads the files and comes back in one screen: verdict first, three findings, a rewrite.
2. Nothing in his voice is invented. Seventy quotes, each with venue, year and link; five famous lines he never said, listed so it cannot use them; a build job that fails if any of that slips.
3. It reviewed itself. The first screen of the README is the skill's verdict on that README, and the next commit is the fix.

**The demo moment.** Open the README. Under the tagline is `/steve verdict README.md`, run on that README: three findings, all true, and the commit that fixed all three — twenty files, the README 187 lines shorter. → the room says: "It did that to itself?"

**Before → after.**
Before (`.claude-plugin/plugin.json`, the text a stranger sees in the `/plugin` listing): "Ask Steve. Think like Steve Jobs about whatever you are building: his verdict, the insight underneath, what to cut, the next move, and how to say it in one sentence. Every real quote sourced."
After: "A Steve Jobs review of what you actually built. Point it at a README, a roadmap or a diff and it comes back in one screen: verdict, three findings, a rewrite. 70 quotes, every one with a source."

Left out on purpose: the six modes, the reference files, the on-demand loading, the line count. That is how it works, and it already lives in the README under "How it works", which is the right place for it.

**The name.** The H1 says "Ask Steve" and the line under it says "Not a Steve Jobs chatbot." A stranger reads those two in a row and hears an argument: "ask" is the chatbot verb. The command is `/steve`, the plugin's display name is already "Steve", the repo is `steve-jobs-skill`. Three names for one thing, and the shortest is the one people type. Call it Steve.

**One more thing.** You shipped the control group. `examples/_baseline-no-skill.md` is the same question as `examples/next-move.md`, asked without the skill, committed next to it. Almost nobody publishes what their tool looks like switched off. When somebody comments "isn't this just a prompt", answer with that pair and nothing else.

*The name call is taste, not measurement. If installs move on "Ask Steve", leave it.*
**What Steve would say.** *(imagined)* "You have one demo, and it is the commit where it reviewed you. Put that first, then stop explaining."

---

## The posts

Every number below is checkable at HEAD; the diff numbers come from the self-review commit, `10f3d37`. `grep -c '^> "' skills/steve/references/quotes.md` gives 70, `ls examples/*.md | grep -v README | wc -l` gives 8, `git show --stat 10f3d37` gives the twenty files and the README diff, and `python3 scripts/check_sources.py` prints the rest.

### Show HN

**Title** (78 characters)

Show HN: A Steve Jobs review for your repo, in Claude Code. It reviewed itself

**First comment**

This is a skill for Claude Code; it also installs into anything that reads SKILL.md with `npx skills add bergamett/steve-jobs-skill`. You type `/steve verdict README.md`, or `/steve cut ROADMAP.md`, or `/steve pitch`, and it reads the actual files and answers in one screen: verdict first, at most three findings, then a rewrite of whatever it judged. Six modes. The 70 quotes it can draw on each carry a venue, a year and a link; a table lists five famous lines he never said so the skill cannot use them; a separate file lists the times he was wrong (the Cube, MobileMe, the hockey-puck mouse, "seven-inch tablets are dead on arrival") and the domains where you should not listen to him, such as accessibility and anything regulated. A CI job runs `scripts/check_sources.py` on every push and fails if a quote loses its source or a never-said line shows up as real. Anything it writes in his voice is labelled imagined. MIT. Not affiliated with Apple or the Steve Jobs estate.

Before posting I pointed it at its own README. The output is the README's first screen, unedited; the full text and the diff it caused are in `examples/self-verdict.md`. It found three things: the demo was a fictional company and the README never said so; eleven headings saying everything twice; a private publishing checklist sitting in the repo root. All three were fixed in the next commit, which touched twenty files and cut the README by 187 lines. There are eight examples in `examples/`, two of them run on fictional inputs that are committed and labelled fictional so you can run the same command and compare. One example is the same question asked without the skill, next to the answer with it. I would like to hear where it gives a bad verdict on your repo.

### X

(274 characters)

A Steve Jobs review for your repo, in Claude Code. /steve verdict README.md reads the file and answers in one screen: verdict, three findings, a rewrite. 70 quotes, each sourced; CI fails if one is not. It reviewed its own README first. github.com/bergamett/steve-jobs-skill

### Reddit, r/ClaudeAI

**Title:** I made a skill that gives your repo a Steve Jobs review. I ran it on its own README first.

**Body** (144 words)

`/plugin marketplace add bergamett/steve-jobs-skill`, then `/plugin install steve@steve`. Then `/steve verdict README.md`, or `cut`, `why`, `next`, `pitch`, `email`.

It reads the actual files, not your description of them, and answers in one screen: verdict first, three findings at most, then a rewrite. It ends with one imagined line, labelled imagined.

Every real quote it uses has a venue, a year and a link, 70 in total, and a CI job fails the build if one loses its source. Five famous lines he never said are listed so it cannot use them. There is a file of the times he was wrong and when not to listen to him.

The first screen of the README is the skill's verdict on that README. Three findings, all fixed in the next commit. Eight examples are in the repo, including the same question asked without the skill. MIT.

### GitHub repository description

(180 characters)

Not a Steve Jobs chatbot. A Steve Jobs review. A Claude Code skill that reads your repo and answers in one screen: verdict, three findings, a rewrite. 70 quotes, every one sourced.

## Two things to do before you post

1. The badge and the README tree say `SKILL.md` is 123 lines; `wc -l` says 122. `check_sources.py` counts `len(text.split("\n"))`, which adds one for the newline at the end of the file. Somebody on Hacker News will run `wc` first. Change the script to `len(text.splitlines())`, then the badge and the tree, and the number is safe to use everywhere. The posts above leave the line count out until then.
2. `.github/PUBLISHING.md` steps 1 to 4 (Pages, the social preview, the description, the branch name) happen in GitHub's settings, not in a commit. The X post unfurls as a grey box without the preview image.
