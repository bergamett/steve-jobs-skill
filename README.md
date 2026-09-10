<p align="center">
  <img src="assets/hero.svg" alt="Ask Steve — a Steve Jobs reasoning skill for Claude Code" width="820">
</p>

<h1 align="center">Ask Steve</h1>

<p align="center"><strong>Not a Steve Jobs chatbot. A Steve Jobs review.</strong></p>

<p align="center">
A skill that looks at what you are building and tells you what he would have told you:<br>
the verdict, the insight underneath it, what to cut, the next move, and the one sentence that sells it.
</p>

<p align="center">
  <a href="#install"><img src="https://img.shields.io/badge/Claude_Code-plugin-000?style=flat-square" alt="Claude Code plugin"></a>
  <a href="#install"><img src="https://img.shields.io/badge/npx-skills_add-000?style=flat-square" alt="npx skills add"></a>
  <a href="skills/steve/references/quotes.md"><img src="https://img.shields.io/badge/quotes-sourced-1a7f37?style=flat-square" alt="Every quote sourced"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT"></a>
  <a href="https://bergamett.github.io/steve-jobs-skill/"><img src="https://img.shields.io/badge/site-bergamett.github.io-black?style=flat-square" alt="Website"></a>
</p>

---

Every other Steve Jobs prompt answers the question *"who was Steve Jobs?"*

Nobody needs that. You need the other thing: someone who looks at the thing you actually made, this afternoon, and says the sentence you have been avoiding.

```
> /steve verdict README.md

Mode: verdict · the TaskFlow Pro README

Verdict. Not yet. Nothing on the first screen says what this does —
put the Usage block at the top and it becomes great.

What's wrong.
1. The Introduction says nothing. Forty words of adjectives before a
   verb that means anything. Cross them out and what is left is "it
   runs your tasks in order" — which is true, and clear, and you did
   not say it.
2. Nine commands to first run, five secrets to invent. A stranger has
   to learn what a JWT_SECRET is before your product does one thing.
   That is where you lose them.
3. Fifteen features, all weighted the same. When everything is listed,
   nothing is chosen. That is a backlog, not a product.

The one thing. "Write a pipeline in ten lines of JavaScript.
One command runs it."

Do this. Put the product in the first ten lines. Then make the install
match the promise: `npx taskflow init` writes the .env, generates the
secrets, migrates and seeds. Nine steps become one.

What Steve would say. (imagined) "You wrote eleven headings before you
told me what it does. Delete ten of them."
```

That is the whole idea. It reads the file. It runs the thing. Then it decides.

That block is real output, not a mock-up. The full version, and four more, are in [`examples/`](examples/).

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

Then type `/steve` and whatever is bothering you.

## Use it

```
/steve                         look at whatever we were just working on
/steve verdict README.md       the honest review, with the rewrite
/steve why are we building this
/steve cut ROADMAP.md          ten things, cross out seven
/steve next                    the one bet, and what it costs you
/steve pitch                   the headline, the three things, the demo moment
/steve email                   answer it the way he answered email
```

No mode? It picks one and tells you which.

| Mode | The question it answers | Give it |
|---|---|---|
| **verdict** | What would Steve say about this? | a README, a landing page, a UI, a CLI, an API, a PR, an idea |
| **why** | What is the insight underneath? | a product, a feature request, a strategy, a nagging feeling |
| **cut** | Which seven do we cross out? | a roadmap, a backlog, a settings page, a nav bar, a pricing table |
| **next** | What is the one bet? | a company, a repo, a plateau, a competitor's move |
| **pitch** | How do I say this in one sentence? | a tagline nobody gets, a README first screen, a Show HN title |
| **email** | How do I answer this? | a feature request, a complaint, a partnership ask |

We had eleven modes. We crossed out five.

## What makes it different

**It holds the thing.** It reads your files, runs your CLI, counts the steps from `git clone` to the first moment something works. It never reviews a description of your product.

**It ends with a rewrite.** A critique that stops at the critique is a roast. Every reply hands back the new headline, the three features that stay, the error message that now tells you what to do.

**Every quote is sourced.** [`quotes.md`](skills/steve/references/quotes.md) carries venue, year and link for every line, and a table of [the famous ones he never said](skills/steve/references/quotes.md#14-what-people-say-he-said-and-what-he-actually-said). When the skill writes what he *would* say about your thing, it labels it imagined. No invented wisdom.

**It knows where he was wrong.** The Cube, MobileMe, the hockey-puck mouse, "seven-inch tablets are dead on arrival". [`failures.md`](skills/steve/references/failures.md) also lists when to stop listening to him: accessibility, safety-critical and regulated domains, and any time you have real usage data that contradicts the intuition.

**It is short.** One screen. Verdict first. If a sentence does not change what you do next, it is not in there.

**It attacks the work, never you.** He could be cruel. This is not that. Brutal about the thing, generous about the person who made it.

## Examples

Real outputs, produced by running the skill. Nothing hand-polished.

| | |
|---|---|
| [**A bloated README**](examples/readme-verdict.md) | fifteen features, nine install steps, and no sentence saying what it is |
| [**A twelve-item roadmap**](examples/roadmap-cut.md) | two people, 900 paying users, and everything has someone asking for it |
| [**A tagline nobody understands**](examples/pitch-devtool.md) | eight months of work that cannot be explained at a meetup |
| [**A product at a plateau**](examples/next-move.md) | 4,000 free users, no revenue, three features planned |
| [**The same question without the skill**](examples/_baseline-no-skill.md) | for comparison. This is the part worth reading twice |

## Real problems it is for

- You have thirty features and no sentence.
- Everyone asked for something and you said yes to all of it.
- Your landing page makes sense to you and to nobody else.
- You cannot tell whether the thing you shipped is good.
- You know what to build next but not what to stop.
- Somebody wants a feature and you cannot find the words for no.
- Your README's first screen is a table of contents.
- You have been staring at this for eight months and lost the ability to see it.

## What it will not do

Trivia, biography, timelines, "what year did he do X". Other skills do that; this one will answer briefly and get back to your product.

It will also not pretend to know what he would think about anything after October 2011. Where the reply imagines his voice, it says so.

## How it works

```
skills/steve/
├── SKILL.md                    the operations manual: modes, loop, rules, templates
└── references/
    ├── principles.md           the fourteen moves, with the evidence for each
    ├── quotes.md               his words, with venue, year, link, confidence
    ├── episodes.md             real decisions as reusable templates
    ├── voice.md                how he actually talked, and the words to never use
    ├── failures.md             where he was wrong, and when not to listen to him
    └── playbooks/              one per mode: steps, output template, traps
```

`SKILL.md` stays under 400 lines so it costs almost nothing to load. The references are read only when the chosen mode needs them. That is the whole architecture.

## FAQ

**Is this just a prompt that says "be harsh"?**
No. Harsh is easy and useless. The skill runs a specific sequence — start from the experience, find the one thing, take things away, check the parts nobody sees, decide, rewrite — and each step exists because he did it, repeatedly, on the record.

**Does it swear at me?**
No. He did. The skill does not, because specificity does the same job harder. "This is a settings page pretending to be a product" lands better than an insult and tells you what to fix.

**Will it just tell me to delete everything?**
It will tell you what to delete and what you get back for deleting it. If your list of ten is genuinely three products, it will say that instead.

**What if I disagree?**
Say so. The skill names the fact that would reverse each verdict, because he changed his mind on native apps, on video on the iPod, on a name he said he hated. A judgment that cannot be reversed by evidence is a pose.

**Does it work outside Claude Code?**
Yes. It is Markdown. Any agent that reads `SKILL.md` can run it, and you can paste `SKILL.md` into a chat window as a system prompt.

**Is it affiliated with Apple or the Jobs estate?**
No. See below.

## Credits and sources

Built from public material: the Stanford commencement address, the 1995 Lost Interview, the WWDC 1997 closing session, the 1997 Think Different talk, the Playboy and Wired interviews, the keynotes, "Thoughts on Flash", the Fortune and All Things Digital interviews, the Steve Jobs Archive's *Make Something Wonderful*, Andy Hertzfeld's folklore.org, Jony Ive's memorial tribute, and Walter Isaacson's HBR account of the leadership lessons. Every source is linked inside [`quotes.md`](skills/steve/references/quotes.md) and [`episodes.md`](skills/steve/references/episodes.md).

Contributions welcome, with [one rule](CONTRIBUTING.md): no unsourced quotes.

## Disclaimer

This project is not affiliated with, endorsed by, or connected to Apple Inc., the Steve Jobs Archive, or the estate of Steve Jobs. "Steve Jobs" and "Apple" are used here to identify the subject of public commentary and analysis, which is the point of the thing.

It is a lens for looking at your own work, built from what he said in public. It is not him, it does not channel him, and it does not claim to know what he would have thought. Where it writes in his voice, it labels that as imagined.

## License

MIT. See [LICENSE](LICENSE).
