# Example: `/steve verdict README.md`

**The ask.** The user pointed at the README of the tool they are building and asked for the verdict.

**Input:** a README for a fictional workflow tool — four badges, an eleven-item table of contents, a fifteen-item feature list, and a nine-step install block.

---

**Mode:** verdict · the TaskFlow Pro README

**Verdict.** Not yet. Nothing on the first screen says what this does — put the Usage block at the top and it becomes great.

**What's great.** The Usage block. Define a pipeline, name three steps, start it. That is the only place a stranger sees the product, and it sits at line 57, under Architecture.

**What's wrong.**
1. **The Introduction says nothing.** "Next-generation, enterprise-grade, cloud-native workflow orchestration platform that leverages a modular plugin architecture to empower teams of all sizes." Forty words before a verb that means anything. Cross out every adjective and what is left is "it runs your tasks in order" — which is true, and clear, and you did not say it.
2. **Nine commands to first run, five secrets to invent.** Clone, cd, copy, edit DATABASE_URL and four friends, docker-compose, install, migrate, seed, build, start. A stranger has to learn what a JWT_SECRET is before your product does one thing. That is where you lose them.
3. **Fifteen features, all weighted the same.** "AI-powered pipeline suggestions (experimental)" sits in the same list as "CLI". When everything is listed, nothing is chosen. That is a backlog, not a product.

**The one thing.** "Write a pipeline in ten lines of JavaScript. One command runs it."

**Do this.** Put the product in the first ten lines.

```
BEFORE — the first screen
  # TaskFlow Pro
  [build] [license] [npm] [downloads]   [logo]
  ## Table of Contents
  Introduction · Background · Philosophy · Architecture · Installation · ...
  ## Introduction
  TaskFlow Pro is a next-generation, enterprise-grade, cloud-native workflow...

AFTER — the first screen
  # TaskFlow Pro
  Write a pipeline in ten lines of JavaScript. One command runs it.

  flow.define('nightly-etl', (ctx) => {
    ctx.step('fetch', fetchData);
    ctx.step('transform', transformData);
    ctx.step('load', loadData);
  });

  npx taskflow init && npm start
```

Then make that command true: `init` writes the .env, generates the secrets, brings up postgres and redis, migrates and seeds. What goes is the table of contents, Background, Philosophy, Architecture, three of the four badges and the feature list — the top half of the file, moved to `docs/` where the two people who want your gRPC contract will find it. What you get back is a first screen that does its job, and one install path to keep working instead of nine.

*Cutting Architecture is taste, not measurement. If your traffic shows people landing there from search, keep the page and link to it — just not above the thing it explains.*

**What Steve would say.** *(imagined)* "You wrote eleven headings before you told me what it does. Delete ten of them."
