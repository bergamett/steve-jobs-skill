# Example: the skill reviewing this repository

**The ask.** `/steve verdict README.md` — pointed at this project's own README, before it was fixed.

**Input:** the first version of this repository: the README, the file tree, `examples/`, `docs/index.html` and the skill itself.

---

**Mode:** verdict · this repo's own README

*I read the README, the file tree, `examples/`, `docs/index.html` and the skill itself. I could not install the plugin or watch a first-time user, so this is a judgment of the files, not of the install.*

**Verdict.** Not yet. The most disciplined README on the subject of honest product feedback proves itself entirely on a product that does not exist — put its verdict on *itself* in that spot and it becomes great.

**What's great.** The tagline. "Not a Steve Jobs chatbot. A Steve Jobs review." Eight words, does the whole job, and putting a terminal block directly under it — output, not philosophy — is the right instinct. Most skill READMEs describe themselves for four screens before showing anything.

**What's wrong.**

1. **The proof is invented, and it exists in three different versions.** TaskFlow Pro is fictional and the README never says so. Worse: the block in the README, `examples/readme-verdict.md`, and the terminal on `docs/index.html` are three different texts of the same run — the site's version says "migrates", the README's says "migrates and seeds", the example has a "What's great" section the other two dropped. All three are labelled real output. Anyone who opens two of them stops believing the third.
2. **Eleven headings, sixteen hundred words, and you say everything twice.** The usage block and the mode table carry the same six modes. "What makes it different" makes six claims; the FAQ answers the same six as questions. And inside your own demo: *"You wrote eleven headings before you told me what it does. Delete ten of them."*
3. **`SETUP.md` is sitting in the repo root.** Your private publishing checklist — turn on Pages, upload the social image, "Before announcing" — is one of the first files a stranger sees in the file list, and its last step reads "Run the skill on this repository's own README and fix whatever it says." You shipped the note that says the thing is not finished. That is the back of the fence, and it is facing the street.

**The one thing.** The sentence is already there and it is right. Keep it. What is missing is the line under it: *"Point it at this README. Here is what it said."*

**Do this.** Delete TaskFlow Pro from the first screen. Run the skill on this file and put that output in its place — real target, checkable by anyone, and it demonstrates the one claim the whole repo rests on: that it holds the actual thing.

What goes: two of the five badges (two of them link to the install section and assert nothing), the usage block or the mode table — one, not both — and the FAQ, whose only two non-duplicate answers move into "How it works" and the Disclaimer. What you get back: the file drops to about six headings, the demo becomes something a stranger can verify in thirty seconds by running it themselves, and the README stops being the one thing in the repo that would fail its own review.

*Cutting the FAQ is taste, not measurement. If your issues fill up with "does it swear at me", put that one line back.*

**What Steve would say.** *(imagined)* "You built a machine for telling people the truth about their work, and then you demoed it on a company you made up."

---

## What happened next

Everything above was acted on in the commit that follows it. Specifically:

| The finding | What changed |
|---|---|
| The proof is invented and exists in three versions | The first screen of the README is now this review. The fictional inputs are committed under [`inputs/`](inputs/) and labelled fictional at the point of use, and the README, the site and the example now quote one text, not three. |
| Eleven headings, everything said twice | Six headings. The usage block and the FAQ are gone; their two non-duplicate answers moved into the sections that already covered the ground. |
| `SETUP.md` in the repo root | Moved to `.github/PUBLISHING.md`. |
| Two badges that assert nothing | Removed. The remaining ones report something checkable, including a continuous-integration job that fails the build if any quote in the skill lacks a source. |
| Claims that were not literally true | `SKILL.md` is 123 lines, not "under 400". The example count is right. The eight moves in the loop and the fourteen documented principles behind them are now named as different things. |

That is the whole argument for the skill, and it cost one command to get.
