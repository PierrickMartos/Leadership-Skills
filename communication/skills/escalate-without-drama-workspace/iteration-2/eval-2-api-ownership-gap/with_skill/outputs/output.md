# Escalation: API Rate Limiting Ownership Gap

## Situation Diagnosis

**Type:** Ownership gap — the API rate limiting strategy exists in the space between teams, with no team or individual having formally claimed responsibility. The escalation's job is to get someone to own it before three uncoordinated feature launches create a production problem.

**Escalation routing advice — who to contact and how:**

You should escalate to **both**, but with different asks:

- **Principal engineer**: The right person to either claim ownership themselves or formally assign it to a team. They have the technical authority to make this call and can move fast without a formal process. This should be your primary escalation — they can likely resolve it in a 15-minute conversation.

- **Director**: Loop them in at the same time, but with a lighter touch — you're not asking them to solve it, you're making sure leadership has visibility on a cross-team coordination risk with a hard deadline. If the principal engineer doesn't act within a day or two, the director will have context to apply pressure.

Don't escalate to the director first and bypass the principal engineer — that reads as political. Escalate to both simultaneously with the message framed as "I wanted both of you aware" rather than "I've given up on the technical path."

---

**Draft escalation** *(for Slack DM, sent to principal engineer with director CC'd, or as a brief message to each)*

---

Hey [Principal Engineer name] — I want to flag a cross-team risk that needs an owner before it becomes a production problem.

Three teams (including mine) are shipping features in the next three weeks that will all call [external API name]. None of us have a shared rate limiting strategy, and right now each team is building independently without coordination. If we ship like this, we're likely to hit rate limit errors in production — and it'll be unclear who's responsible for fixing it.

I've raised this in #architecture-discuss twice over the past few weeks and got good engagement each time, but no one has stepped up to own the strategy or drive a decision. With the first feature shipping in roughly three weeks, we're past the point where "let's align soon" is enough.

Here's what I need: either a named owner who will drive a lightweight shared approach in the next week, or a call with the three teams to agree on one together. I can organize and run that call — I just need someone with cross-team authority to kick it off and make the outcome stick.

Happy to jump on a call today or tomorrow if that's easier than async. Can you help get this moving?

---

**Notes**
- This is sent as a DM rather than in a channel because the gap isn't any one person's fault — making it public at this stage would feel like calling out the teams rather than solving the problem. If you get no response in 24 hours, a brief message in #architecture-discuss naming the principal engineer directly is a reasonable next move.
- The ask is deliberately structured to give the principal engineer an easy path: they can either claim it themselves or delegate it. You're not demanding they solve it, just that they unblock the ownership question.
- Keep the director version slightly shorter — you're informing them, not asking them to act. Something like: "Hey [Director] — I'm escalating a cross-team coordination gap to [Principal Engineer] today and wanted you to have visibility. Three teams are about to ship features hitting the same external API with no shared rate limiting strategy. First ship is ~3 weeks out. I've flagged it twice in #architecture-discuss without resolution. [Principal Engineer] is looped in to help get an owner assigned."
