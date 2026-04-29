# Screening Report: Senior Backend Engineer -- Product Catalog API

---

## Candidate Summary

- **Profile:** Staff Engineer at a 20-person fintech startup (2 years), 7+ years total experience, Go/PostgreSQL/Kafka stack
- **Trajectory:** IC track, consistently moving toward higher scope and systems ownership -- consulting to big tech to startup leadership
- **Headline:** Strong technical fit with clear architecture and mentorship potential; main question is whether they'll thrive (and stay) at a mid-size company after a tiny startup

---

## Rating: 4/5 -- Good fit, minor gaps to validate

The technical alignment is excellent and the career arc shows genuine growth in ownership and impact. The open questions are about motivation, title expectations, and adaptation to a larger org -- all answerable in one good call.

---

## Strengths

- **Direct systems experience** -- Built a payment pipeline handling 50k txn/day in Go + PostgreSQL + Kafka; maps closely to your high-throughput catalog API needs
- **Architecture ownership** -- Designed a system from scratch at current role, not just contributing to an existing one; this is exactly the "own architecture decisions" gap you need filled
- **Event-driven architecture** -- Production Kafka experience is your JD bonus and a genuine differentiator for catalog sync/webhook patterns
- **Mentorship signals** -- Staff title at a 20-person company likely means they were the technical ceiling; mid-levels would have looked to them by default. Needs validation, but the conditions were there
- **Strong IC trajectory** -- Mid-to-senior promotion at Spotify in 18 months suggests high performance in a rigorous leveling system
- **Open source maintainer** -- 800-star Go library shows communication skills, code quality standards, and ability to build for an audience beyond their team
- **Polyglot background** -- Java, Python, Go across career; won't be rigid about tooling choices

---

## Gaps

- **No explicit mid-size company experience** -- Went from consulting to Spotify (~8k employees at the time) to a 20-person startup; your 300-person scale-up is a different animal -- *Unknown*
- **Mentorship track record unclear** -- Being the most senior person doesn't automatically mean they mentored well; no resume evidence of growing others deliberately -- *Unknown*
- **Data modeling complexity** -- Payment pipelines are transactional; product catalog data modeling (polymorphic attributes, localization, inheritance) is a different kind of hard. Adjacent but not identical -- *Unknown*
- **Python proficiency depth** -- JD lists Python or Go; they clearly lead with Go. Python appears only in early consulting work -- *Unknown* (may not matter if Go is acceptable)

---

## Risks

- **Title sensitivity** -- They hold a Staff title today. Even if your Senior scope is genuinely bigger, "Senior" on paper may feel like a step back. If you have Staff budget, leading with Senior-to-Staff range reduces friction
- **Startup-to-scaleup pace mismatch** -- At a 20-person company they likely had full autonomy, minimal process, and shipped fast. Your 6-person team inside a 300-person org will have more coordination overhead, cross-team dependencies, and planning cycles. They may find this slow
- **Flight risk if under-scoped** -- If they took Staff-level ownership at a startup and you slot them into a narrower Senior lane, boredom and attrition risk goes up within 12-18 months
- **"Staff at 20 people" calibration** -- Your instinct is right to question this. Staff at a 20-person startup can mean "best engineer at a small company" rather than Staff-level organizational impact. But: building a core pipeline from scratch for a fintech is non-trivial scope. The question is whether they operated as a technical leader (influencing roadmap, making tradeoffs across teams, mentoring) or just as the strongest individual contributor

---

## Bias Check

Two things to flag:

1. **Halo effect from Spotify** -- The Spotify line is impressive and may be inflating the overall read. Their actual scope there (content delivery platform, 3 years, promoted once) is solid but not exceptional for the company. Evaluate what they did, not the logo.
2. **Pedigree bias on education** -- MS from KTH is strong, but it's 7+ years ago and irrelevant to whether they can mentor your mid-levels or own architecture at your scale. I've weighted it at zero in this assessment, flagging it so you do the same.

The user's concern about "is Staff at a tiny startup really Staff?" is a legitimate calibration question, not bias. It's appropriate to probe this in the call.

---

## Decision Framework

- **If you take this call, the question you're trying to answer is:** Can this person operate as a technical leader (not just a strong IC) inside a team and org that are meaningfully larger and more structured than what they're used to?
- **This candidate is a strong fit if it turns out that:** They actively mentored others at the startup, they're motivated by the complexity of your domain (not just the title), and they're genuinely ready for more organizational structure
- **This candidate is not a fit if:** Their "Staff" work was purely individual execution with no leadership component, or they view a 300-person company as bureaucratic overhead they want to escape
- **What would change your mind:** If they describe concrete examples of growing other engineers and making architectural tradeoffs that involved saying no to things -- that flips this from "good" to "move fast." If they can't articulate why they want to leave a Staff role at a startup, that's a red flag

---

## Call Preparation

### Call structure (45 minutes)

| Phase | Time | Purpose |
|-------|------|---------|
| **Opener** | 5 min | Rapport, quick overview of team and catalog API domain |
| **Candidate story** | 10 min | Why they're looking, what they want next, how they think about the title question |
| **Deep-dive questions** | 20 min | Behavioral and situational questions on the key unknowns |
| **Their questions** | 5 min | Listen for what they care about -- process, autonomy, growth, domain |
| **Close** | 5 min | Next steps, timeline, level/comp range if appropriate |

### Tailored Questions

**Q1. "You're currently Staff at a 20-person company. What does your day-to-day look like beyond writing code -- how do you spend the time that isn't heads-down engineering?"**
- **Targets:** Whether "Staff" included leadership scope or was purely technical execution
- **Good answer:** Describes influencing roadmap priorities, reviewing others' designs, making build-vs-buy decisions, onboarding or mentoring junior/mid engineers
- **Probe if vague:** "Can you give me a specific example of a technical decision you drove that other engineers initially disagreed with? How did that play out?"
- **Red flag:** Everything they describe is individual contribution with a Staff label on it

**Q2. "Tell me about a time you helped a mid-level engineer grow -- not just unblocked them on a task, but genuinely helped them level up."**
- **Targets:** Mentorship capability (your must-have)
- **Good answer:** Describes a specific person, what they were struggling with, what the candidate did differently over time, and a visible outcome (promotion, increased autonomy, took on harder work)
- **Probe if vague:** "What did you do differently for that person versus just doing a code review?"
- **Red flag:** Can't name a specific person or describes mentorship as "I answer questions when people ask"

**Q3. "Your payment pipeline handles 50k transactions/day. Walk me through an architectural decision you made there that involved a meaningful tradeoff -- something where the alternative was also reasonable."**
- **Targets:** Architecture ownership depth and decision-making rigor
- **Good answer:** Names the tradeoff explicitly (consistency vs. latency, simplicity vs. flexibility, etc.), explains why they chose one side, and acknowledges the cost
- **Probe if vague:** "What would you do differently if you rebuilt it today?"
- **Red flag:** Describes only the happy path or can't articulate what they gave up

**Q4. "Our product catalog API deals with highly polymorphic data models -- products can have wildly different attribute structures, localized content, inheritance hierarchies. This is different from transactional payment data. How would you approach getting up to speed on a domain like this?"**
- **Targets:** Data modeling complexity gap, intellectual curiosity, learning approach
- **Good answer:** Asks clarifying questions about the domain, describes a structured approach (read the schema, talk to the team, look at the hardest queries), shows genuine curiosity rather than hand-waving
- **Probe if vague:** "What's the most complex data model you've worked with, and what made it hard?"
- **Red flag:** Dismisses the complexity ("data modeling is data modeling") or shows no interest in the domain

**Q5. "You've been at a 20-person startup where you probably had a lot of autonomy and very little process. We're 300 people -- there's more cross-team coordination, planning cycles, and stakeholder management. What's your honest reaction to that?"**
- **Targets:** Pace/culture mismatch risk
- **Good answer:** Acknowledges the difference honestly, explains what they want more of (not less of), maybe describes frustrations with pure-startup chaos that signal readiness for more structure
- **Probe if vague:** "What's the most frustrating process you've dealt with, and did you try to fix it or work around it?"
- **Red flag:** Frames all process as waste, or romanticizes "moving fast" without nuance

**Q6. "If you joined us, the title would likely be Senior Engineer -- though there's room to grow into Staff if the impact is there. How do you think about titles relative to scope and impact?"**
- **Targets:** Title sensitivity risk, motivation
- **Good answer:** Cares more about the work, the team, and the growth trajectory than the title; asks about what Staff scope would look like rather than demanding it upfront
- **Probe if vague:** "What would need to be true for you to feel like this was a step forward in your career, not a step back?"
- **Red flag:** Fixates on the title, treats it as non-negotiable, or implies they'd only consider Staff

**Q7. "Describe a situation where you had to push back on a product or business stakeholder about a technical decision. What happened?"**
- **Targets:** Ability to own decisions in a cross-functional environment (critical for someone who'll own architecture in a product team)
- **Good answer:** Describes the stakeholder's perspective with empathy, explains how they framed the technical concern in business terms, and landed on a resolution (not just "I won")
- **Probe if vague:** "How did you frame the tradeoff so a non-technical person could make an informed decision?"
- **Red flag:** Describes only steamrolling or only capitulating

### Scoring Rubric

| Dimension | Strong signal | Acceptable | Weak signal |
|-----------|--------------|------------|-------------|
| **Leadership beyond code** | Describes influencing roadmap, mentoring others, driving design reviews as regular parts of their role | Has done some mentoring and design leadership when asked | All examples are individual contribution; "leadership" is just being the best coder |
| **Architecture decision-making** | Articulates tradeoffs clearly, names what they gave up, would change things with hindsight | Can describe decisions but struggles to articulate the tradeoff or alternative | Describes only implementation, not decision-making |
| **Adaptability to mid-size org** | Honest about startup limitations, actively wants more structure and cross-team collaboration | Neutral, willing to adapt, no red flags | Frames process as waste, idealizes pure autonomy, shows no awareness of coordination needs |
| **Domain curiosity** | Asks sharp questions about catalog data modeling, shows genuine interest in the problem space | Open to learning, doesn't dismiss the complexity | Dismissive of domain differences or uninterested in the specifics |
| **Title/motivation alignment** | Focused on scope, impact, and growth; sees this as a step forward regardless of title | Slightly title-conscious but flexible if the work is right | Title is a dealbreaker, or motivation is unclear |

### Things to Watch For During the Call

- **How they talk about their current team.** At a 20-person startup, "the team" is basically the whole company. Listen for whether they describe other engineers as people they've helped grow, or just as people they work alongside. This tells you more about mentorship instinct than any direct question.
- **Whether they ask about your architecture.** A candidate who wants to own architecture decisions should be deeply curious about what exists today. If they spend their Q&A time on comp, remote policy, and title, that's a signal about what they actually care about.
- **How they handle the domain complexity question.** The shift from payment transactions to product catalog modeling is real. You're not looking for them to already know your domain -- you're looking for the spark of "oh, that's an interesting problem" versus "yeah, I can figure it out."
