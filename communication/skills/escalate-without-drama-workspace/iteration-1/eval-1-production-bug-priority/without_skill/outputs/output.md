# Escalation Draft: Production Bug Priority Re-evaluation

## Context

- Bug affecting ~12% of users who cannot complete onboarding
- Active for 24 hours
- Currently triaged as P2 by engineering
- On-call engineer: Thomas (working on it, no ETA provided)
- Escalating to: Priya, VP of Engineering

---

## Draft Message

**To:** Priya
**Subject:** Alignment needed on onboarding bug priority — 24h in, 12% of users affected

Hi Priya,

I wanted to flag something and get your perspective before the day goes further.

We have an active bug where roughly 12% of users are unable to complete onboarding. It's been open for about 24 hours. Thomas has it on his radar and is working through it — I don't have visibility into what he's found so far, which is part of why I'm reaching out to you.

Engineering triaged this as P2. I want to make sure that classification is intentional given the business context: onboarding failure at this scale typically represents meaningful revenue impact and elevated churn risk, especially if affected users are in their first session. I may be missing technical context that informed the P2 call, and I'd genuinely like to understand it.

A few things I'm hoping to get clarity on:

1. **Is P2 the right priority given the user and business impact?** If it is, I'd love to understand the reasoning so I can communicate it to stakeholders.
2. **Can we get a working ETA or at least a next-check-in time?** Even a rough range ("we expect to know more by 4pm") would help me manage expectations across the business.
3. **Is there anything on the PM side I can do to unblock the investigation** — business data, user reproduction steps, additional context?

I'm not looking to add pressure on Thomas — he's handling it — but I want to make sure the right people have visibility and that we're not underprioritizing something with real user impact. Happy to jump on a quick call if that's easier.

Thanks,
[Your name]

---

## Why This Works

**Protects Thomas:** The message positions him as actively working the problem, not as someone who dropped the ball. It names him once, positively, and doesn't assign blame for the P2 triage call.

**Stays fact-based:** It leads with observable data (12% of users, 24 hours, no ETA) rather than emotion or accusation. Priya can evaluate the situation on its merits.

**Invites dialogue, not a verdict:** By framing it as "I may be missing technical context," you give engineering an easy off-ramp to explain the P2 rationale without being put on the defensive.

**Puts the ask in writing:** Three specific, actionable questions make it easy for Priya to respond and delegate, rather than leaving her to interpret what you need.

**Signals business ownership:** You're doing your job as a PM — protecting the product and users — without overstepping into engineering prioritization decisions.
