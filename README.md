<p align="center">
  <img src="assets/hero.svg" alt="Ask Steve — a Steve Jobs reasoning skill for Claude Code" width="820">
</p>

<h1 align="center">Ask Steve</h1>

<p align="center"><strong>Not a Steve Jobs chatbot. A Steve Jobs review.</strong></p>

<p align="center">
  <a href="https://github.com/bergamett/steve-jobs-skill/actions/workflows/check.yml"><img src="https://github.com/bergamett/steve-jobs-skill/actions/workflows/check.yml/badge.svg" alt="Every quote has a source"></a>
  <a href="skills/steve/references/quotes.md"><img src="https://img.shields.io/badge/quotes-70%2C%20all%20sourced-1a7f37?style=flat-square" alt="70 quotes, all sourced"></a>
  <a href="skills/steve/SKILL.md"><img src="https://img.shields.io/badge/SKILL.md-123%20lines-000?style=flat-square" alt="SKILL.md is 123 lines"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT"></a>
</p>

Every other Steve Jobs prompt answers the question *"who was Steve Jobs?"*

Nobody needs that. You need the other thing: someone who looks at what you actually made, this afternoon, and says the sentence you have been avoiding.

So here is the skill pointed at this page, before it was fixed.

```
> /steve verdict README.md

Mode: verdict · this repo's own README

Verdict. Not yet. The most disciplined README on the subject of honest
product feedback proves itself entirely on a product that does not exist —
put its verdict on itself in that spot and it becomes great.

What's great. The tagline. "Not a Steve Jobs chatbot. A Steve Jobs review."
Eight words, does the whole job.

What's wrong.
1. The proof is invented, and it exists in three different versions.
   TaskFlow Pro is fictional and the README never says so. The block here,
   the example file and the website are three different texts of the same
   run, all labelled real output. Anyone who opens two of them stops
   believing the third.
2. Eleven headings, sixteen hundred words, and you say everything twice.
   And inside your own demo: "You wrote eleven headings before you told me
   what it does. Delete ten of them."
3. SETUP.md is sitting in the repo root. Its last step reads "run the skill
   on this repository's own README and fix whatever it says." You shipped
   the note that says the thing is not finished.

The one thing. The sentence is already there and it is right. What is
missing is the line under it: "Point it at this README. Here is what it
said."

What Steve would say. (imagined) "You built a machine for telling people the
truth about their work, and then you demoed it on a company you made up."
```

Every finding was true. All three are fixed in the commit that followed, and the full review with the diff it produced is in [`examples/self-verdict.md`](examples/self-verdict.md). That is the whole argument, and it cost one command.

## Install

**Claude Code** — one line, then one more:

```
/plugin marketplace add bergamett/steve-jobs-skill
/plugin install steve@steve
```

**Any agent that reads SKILL.md** (Claude Code, Codex, Cursor, Gemini CLI, OpenCode):

```
npx skills add bergamett/steve-jobs-skill
```

**By hand:**

```
git clone https://github.com/bergamett/steve-jobs-skill
cp -r steve-jobs-skill/skills/steve ~/.claude/skills/steve
```

**In a plain chat window,** where there is no folder to read from: paste [`dist/steve-full.md`](dist/steve-full.md), which is the same skill flattened into one file.

Then type `/steve` and whatever is bothering you. No mode? It picks one and tells you which.

| Mode | The question it answers | Try |
|---|---|---|
| **verdict** | What would Steve say about this? | `/steve verdict README.md` |
| **why** | What is the insight underneath? | `/steve why are we building this` |
| **cut** | Which seven do we cross out? | `/steve cut ROADMAP.md` |
| **next** | What is the one bet, and what does it cost? | `/steve next` |
| **pitch** | How do I say this in one sentence? | `/steve pitch` |
| **email** | How do I answer this without lying or losing them? | `/steve email` |

We had eleven modes. We crossed out five.

## What makes it different

**It holds the thing.** It reads your files, runs your CLI, counts the steps from `git clone` to the first moment something works. It never reviews a description of your product. The inputs it was pointed at are [committed](examples/inputs/) so you can run the same commands.

**It ends with a rewrite.** A critique that stops at the critique is a roast. Every reply hands back the new headline, the three features that stay, the error message that now tells you what to do.

**Every quote is sourced.** [`quotes.md`](skills/steve/references/quotes.md) carries venue, year, link and a confidence marker for all seventy lines, plus a table of [the famous ones he never said](skills/steve/references/quotes.md#14-what-people-say-he-said-and-what-he-actually-said). A [continuous-integration job](scripts/check_sources.py) fails the build if a quote appears without a source, or if a line from the never-use table shows up anywhere as real. When the skill writes what he *would* say about your thing, it labels it imagined.

**It knows where he was wrong.** The Cube, MobileMe, the hockey-puck mouse, "seven-inch tablets are dead on arrival". [`failures.md`](skills/steve/references/failures.md) also lists when to stop listening to him: accessibility, safety-critical and regulated domains, and any time you have real usage data that contradicts the intuition.

**It is short, and it attacks the work.** One screen. Verdict first. Nothing about the person who made the thing. He could be cruel; this is not that.

It is for the afternoon when you have thirty features and no sentence, when everybody asked for something and you said yes to all of it, when your landing page makes sense to you and to nobody else, when you know what to build next but not what to stop, when somebody wants a feature and you cannot find the words for no, and when you have been staring at the same screen for eight months and lost the ability to see it.

It is not for trivia, biography or "what year did he do X". Other skills do that. This one answers briefly and gets back to your product. It also will not pretend to know what he would think about anything after October 2011.

## Examples

Real outputs. The two fictional inputs are committed alongside them and labelled fictional.

| | |
|---|---|
| [**This repository's own README**](examples/self-verdict.md) | the review above, in full, with the diff it caused |
| [**A bloated README**](examples/readme-verdict.md) | fifteen features, nine install steps, no sentence saying what it is |
| [**A twelve-item roadmap**](examples/roadmap-cut.md) | two people, 900 paying users, everything has someone asking for it |
| [**A tagline nobody understands**](examples/pitch-devtool.md) | eight months of work that cannot be explained at a meetup |
| [**"A feature, not a product"**](examples/why-insight.md) | the insight underneath an idea everyone keeps dismissing |
| [**A customer offering real money**](examples/email-feature-request.md) | for a port the developer does not want to build |
| [**A product at a plateau**](examples/next-move.md) | 4,000 free users, no revenue, three features planned |
| [**The same question, without the skill**](examples/_baseline-no-skill.md) | read this one against the previous one |

## How it works

```
skills/steve/
├── SKILL.md                    123 lines: six modes, the loop, the rules, the shape of a reply
└── references/
    ├── playbooks/              one per mode: steps, output template, traps
    ├── quotes.md               70 quotes: venue, year, link, confidence
    ├── principles.md           the fourteen documented moves and the evidence for each
    ├── episodes.md             real decisions as reusable templates
    ├── voice.md                how he talked, and the words to never use
    └── failures.md             where he was wrong, and when not to listen to him
```

`SKILL.md` carries the eight-step loop the skill runs on your work and stays small, so it costs almost nothing to load. The fourteen principles behind those steps, the quotes and the episodes are read only when the mode in play needs them. That is the whole architecture.

Because the references load from disk, a paste of `SKILL.md` alone into a chat window gives you the rules and none of the templates. Use [`dist/steve-full.md`](dist/steve-full.md) there instead; `scripts/build_single_file.py` rebuilds it.

Contributions welcome, with [one rule](CONTRIBUTING.md): no unsourced quotes. `python3 scripts/check_sources.py` will tell you before the build does.

## Credits, and what this is not

Built from public material: the Stanford commencement address, the 1995 Lost Interview, the WWDC 1997 closing session, the 1997 Think Different talk, the Playboy and Wired interviews, the keynotes, "Thoughts on Flash", the Fortune and All Things Digital interviews, the Steve Jobs Archive's *Make Something Wonderful*, Andy Hertzfeld's folklore.org, Jony Ive's memorial tribute, and Walter Isaacson's account of the leadership lessons. Every source is linked inside [`quotes.md`](skills/steve/references/quotes.md) and [`episodes.md`](skills/steve/references/episodes.md).

This project is not affiliated with, endorsed by, or connected to Apple Inc., the Steve Jobs Archive, or the estate of Steve Jobs. It is a lens for looking at your own work, built from what he said in public. It is not him, it does not channel him, and it does not claim to know what he would have thought. Where it writes in his voice, it says so.

MIT licensed. See [LICENSE](LICENSE).
