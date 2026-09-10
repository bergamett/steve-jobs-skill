# Example: `/steve why`

**The ask.** "I keep being told my idea is a feature, not a product, and I can't tell if they're right."

**Input:** a tool that finds the right reviewer for a stalled pull request and nudges them in Slack.

---

**Mode:** why · the bot that finds the reviewer

*Working from your description — I have not seen the Slack message it sends, and that message is the whole product.*

**The insight.** Nobody wants faster code review. They want to finish something on Tuesday and not still be carrying it around on Friday.
The people saying "feature, not a product" are right about the nudge and wrong about what you built. The nudge is a feature. Knowing who should look at this is not.

**The person.** The engineer who pushed on Tuesday afternoon, typed "anyone free to review this?" into a channel, got nothing back, and has now re-read her own diff twice to remember what it did.

**Why, three times.**
Finds the right reviewer and nudges them → the change moves in an hour instead of four days → she gets to put the thing down and stop holding it in her head all week.

**The enemy.** The message addressed to everyone. "@here can someone review this?" is not a request, it is a hope, and answering a hope is nobody's job.

**The collapse.** Three things your team does badly in three places — who owns this code, who is actually free, and what this change even does — become one message to one person. And once you know who should look at a diff, the diff is only the first thing worth sending: the flaky test, the customer bug, the question that sat in #eng for a day. That is the part that is not a feature.

**The question nobody asked.** Do your pull requests sit for four days because nobody knows whose job it is, or because everyone knows and it is nobody's priority? A nudge cures the first and makes the second worse. Test it this week with no code: pick the reviewer yourself and send the message by hand, five days running. If reviews come back in an hour, you have a product. If they still sit, your enemy is the calendar and the bot is a guilt machine.

**What it rules out.** No dashboard, no leaderboard, no weekly report on who reviews slowest — the day you sell to the manager, the engineer turns you off, and this only works if the engineer is glad to see the message.

*All of this is taste. I have your four days and nothing else. Run the week of hand-picked messages; whatever it shows beats every line above.*

**What Steve would say.** *(imagined)* "You think you built a reminder. You built the thing that knows who should look at this, and the reminder is just the first place you use it."
