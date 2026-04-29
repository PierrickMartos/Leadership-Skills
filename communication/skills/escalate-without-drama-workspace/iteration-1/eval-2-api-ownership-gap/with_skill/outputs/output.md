# Escalation: API Rate Limiting Ownership Gap

## Routing Advice

**Escalate to the principal engineer first, with the director CC'd.**

The core problem is a technical ownership gap — no one has been assigned to drive the API rate limiting strategy across teams. That is the principal engineer's domain: they have the standing to assign ownership, the architectural context to evaluate the options, and the credibility to unstick something that's been stalling in a horizontal channel.

The director should be looped in as a CC, not the primary action recipient. Two reasons: (1) a 3-week deadline with three teams un-coordinated is a delivery risk worth putting in front of leadership, and (2) if the resolution requires pulling someone off other work, the director needs the context to make that call quickly.

If you prefer a sequential approach — escalate to the principal engineer first, give it 24 hours, then involve the director if nothing moves — that's also reasonable given the runway. But with 3 weeks to first ship, going to both simultaneously is not premature.

---

**Draft escalation** *(Slack DM to principal engineer, with director CC'd or forwarded)*

---

Hey [Principal Engineer name] — wanted to flag something before it becomes a launch problem.

Three teams (including mine) are shipping features in the next three weeks that will all hit [the external API]. None of us have coordinated on a rate limiting strategy. As far as I can tell, no one owns this cross-team — it's fallen in the gap between us.

I've raised it twice in #architecture-discuss and both times the response was "good point, let's align" — but nothing has moved. With the first ship date coming up, I don't think we can let this sit in a general channel any longer.

If we each build independently without a shared approach, we risk hitting rate limits in production, creating hard-to-debug failures, or building incompatible solutions that are expensive to reconcile later.

What I need is either: (a) someone designated as the owner who can drive a decision before [first ship date], or (b) a clear decision that each team handles their own rate limiting independently, with agreed standards for how we do that.

I'm not asking for a long process — even a 30-minute sync with the three teams and a decision logged would unblock us. Happy to organize it if that helps.

Can you help get an owner assigned, or tell me the right person to loop in? I want to make sure we're coordinated before anyone ships.

---

**Notes**

- The tone here is firm but positions you as someone trying to solve the problem, not assign blame. The framing "fallen in the gap between us" describes the structural issue without accusing any team of dropping the ball.
- The two-option ask (owner assigned vs. explicit decision to go independently) is important — it gives the principal engineer a clear, fast path forward and avoids leaving them with an open-ended "fix this" they have to interpret.
- If you send this and don't hear back within 24 hours, follow up with your director directly. At that point you've made two attempts in #architecture-discuss and a direct escalation — the next step is their visibility.
- Consider also posting a brief summary in #architecture-discuss after this message goes out: "Escalating the API rate limiting question directly — will share what we land on here." That closes the loop publicly without making anyone look bad.
