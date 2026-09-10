# Inputs

The files the skill was actually pointed at, committed so anyone can run the same command and compare.

| File | Used by | Real or fictional |
|---|---|---|
| [`taskflow-README.md`](taskflow-README.md) | [`../readme-verdict.md`](../readme-verdict.md) | Fictional. A composite of the patterns that show up in real project READMEs: a table of contents above the product, adjectives instead of a sentence, fifteen features, nine install steps. |
| [`ledgerly-ROADMAP.md`](ledgerly-ROADMAP.md) | [`../roadmap-cut.md`](../roadmap-cut.md) | Fictional. A twelve-item quarter for a two-person team with 900 paying users. |

The other three examples were given to the skill as a message rather than a file, so there is nothing to commit; each one states its input at the top.

Reproduce a run:

```
cp -r skills/steve ~/.claude/skills/steve
claude
> /steve verdict examples/inputs/taskflow-README.md
```

You will not get the same words. You should get the same verdict, the same three findings, and a rewrite of the first screen.
