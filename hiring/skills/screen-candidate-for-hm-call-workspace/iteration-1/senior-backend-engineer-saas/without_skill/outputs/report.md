# Candidate Screening Report: Senior Backend Engineer

**Role:** Senior Backend Engineer (with Staff potential)
**Team:** Product Catalog API, B2B SaaS (Series C, ~300 employees)
**Prepared for:** Hiring Manager call preparation

---

## 1. Overall Assessment

**Recommendation: Strong Proceed -- schedule the call.**

This candidate presents a compelling profile for the Senior role and is worth evaluating seriously for Staff. The technical stack alignment is excellent, the career trajectory shows consistent growth, and the open-source contribution signals genuine craft investment. The risks you identified are real but manageable -- they become interview questions, not disqualifiers.

---

## 2. Requirements Match

### Hard Requirements

| Requirement | Match | Evidence |
|---|---|---|
| 5+ years experience | Yes (7 years) | 2 yrs consulting + 3 yrs Spotify + 2 yrs fintech startup |
| Python or Go | Yes | Go is primary language at current role; Python experience from consulting |
| Distributed systems | Yes | Payment processing pipeline with Kafka; content delivery at Spotify |
| API design | Likely yes | Payment processing pipeline implies API surface; Spotify platform work implies API consumers at scale. Confirm depth in call. |
| PostgreSQL or similar | Yes | PostgreSQL at current role |
| Event-driven architectures (bonus) | Yes | Kafka-based payment pipeline is textbook event-driven |

### Soft Requirements

| Requirement | Assessment | Notes |
|---|---|---|
| Own architecture decisions | Probable yes | Built payment pipeline from scratch -- that is architecture ownership. But at a 20-person company, the decision-making context is very different from a 300-person org. Needs probing. |
| Mentor mid-level engineers | Unknown | No direct evidence. At a 20-person startup, mentorship may have been informal or minimal. This is the biggest gap to probe. |
| Mid-size company pace | Risk area | Has only worked at extremes: large (Spotify) and tiny (current). Your 300-person Series C is neither. Could go either way. |

---

## 3. Strengths

**1. Technical depth in your exact problem domain.** High-throughput data pipeline (50k tx/day) with Go + PostgreSQL + Kafka maps directly to a high-throughput product catalog API. They will understand the performance, reliability, and data modeling challenges on day one.

**2. Career trajectory signals high performer.** Promoted from mid to senior at Spotify in 18 months. Spotify is known for rigorous leveling. That is not a gift promotion.

**3. Builds things from zero, not just maintains.** The payment pipeline was built from scratch. Your team needs someone who can own architecture decisions -- this person has done exactly that, recently.

**4. Open-source contribution shows craft beyond the job.** An 800-star Go rate-limiting library is nontrivial. It signals: (a) they write code others find useful, (b) they understand API design well enough to build developer tools, (c) they invest in the ecosystem. This is a positive signal for mentorship culture too -- people who care about craft tend to enjoy teaching it.

**5. Stack alignment is near-perfect.** Go, PostgreSQL, Kafka, AWS, distributed systems. You would be hiring for existing expertise, not potential.

---

## 4. Risk Analysis

### Risk 1: "Staff at a 20-person startup -- is that really Staff?"

**Assessment: Partially valid, but less important than you think.**

At a 20-person company, "Staff Engineer" can mean many things. It might mean "our best IC" rather than the industry-standard definition (cross-team technical leadership, organizational influence, setting technical direction across multiple teams).

However, the real question is not "was their title legitimate?" but "can they do what we need?" The evidence says:
- They can build systems from scratch (pipeline ownership)
- They can work with high-throughput constraints (50k tx/day)
- They operated at a legitimately high-bar company before (Spotify)

**What to probe:** Ask about scope of influence. Did they make decisions that affected other teams or just their own work? Did they write technical design docs that others reviewed? Did they evaluate and reject alternative approaches?

### Risk 2: Title regression (Staff to Senior)

**Assessment: Real risk, but addressable.**

Going from Staff to Senior can feel like a demotion even if the scope is larger. Some candidates will be fine with it ("I care about the work, not the title"). Others will quietly resent it and leave within a year.

**What to probe:** Be transparent about this in the call. Frame it as: "The scope here at Senior is likely broader than Staff at a 20-person company -- you'd be influencing architecture for a team of 6 within a 300-person engineering org, with real cross-team dependencies. We also have budget for Staff if the fit is right. How do you think about titles vs. scope?"

Their reaction will tell you a lot. Defensiveness is a yellow flag. Curiosity about scope is a green flag.

### Risk 3: Startup-to-midsize transition

**Assessment: Moderate risk.**

At a 20-person startup, you can just walk over and talk to the CTO. At 300 people, you write a design doc, get three teams to review it, navigate a prioritization process, and then maybe it gets built next quarter.

Counter-signal: they spent 3 years at Spotify (~6,000+ employees at the time). They have operated in a large-org context before. The question is whether they left Spotify because they hated that pace or because they wanted to grow faster technically.

**What to probe:** "What made you leave Spotify for a 20-person startup? What are you looking for in your next move?"

### Risk 4: Mentorship capability is unproven

**Assessment: Genuine gap in evidence.**

Nothing in the resume directly demonstrates mentorship. At 20 people, there may not have been junior or mid-level engineers to mentor. This is your most important must-have to validate.

**What to probe:** See specific questions below.

---

## 5. Suggested Call Structure (45-60 minutes)

### Opening (5 min)
Set context about the role, the team, the product. Be specific about the product catalog API, the throughput challenges, and the data modeling complexity. Candidates calibrate their answers to what they think you want -- give them the real picture.

### Block 1: Architecture Ownership (15 min)

**Goal:** Validate they can own decisions in a mid-size org context, not just a startup where they were the only option.

Questions:

1. *"Tell me about the payment processing pipeline you built. Walk me through the key architectural decisions you made and, more importantly, the ones you considered and rejected."*
   - **Listen for:** Trade-off reasoning, not just what they built. Do they talk about alternatives they evaluated? Do they mention constraints (cost, timeline, team skill) that shaped the decisions? Or do they just describe the final architecture?

2. *"At 50k transactions per day, what are the failure modes you designed for? What broke in production that you didn't anticipate?"*
   - **Listen for:** Honesty about failures. Mature engineers talk about what went wrong. If everything was perfect, they are either not being candid or they did not operate the system long enough to learn.

3. *"If you were designing our product catalog API from scratch -- high throughput, complex data modeling, many downstream consumers -- what questions would you ask before making any technical decisions?"*
   - **Listen for:** Do they jump to solutions or do they ask about constraints first? Great architects start with questions: What are the access patterns? What is the consistency model? Who are the consumers? What is the change velocity of the schema?

### Block 2: Mentorship and Team Impact (10 min)

**Goal:** Find evidence of mentorship behavior, even if informal.

Questions:

4. *"On your current team, how do you approach situations where a teammate is going in a direction you think is wrong technically?"*
   - **Listen for:** Collaborative correction vs. top-down override. Do they pull rank, or do they teach? Do they create space for the other person to arrive at the right answer?

5. *"Have you ever been responsible for someone else's technical growth? Tell me about it."*
   - **Listen for:** Specifics. If they say "I mentored a junior engineer," push for what that actually looked like. Weekly 1:1s? Code review with teaching comments? Pairing sessions? Design doc feedback? Vague answers here are a yellow flag.

6. *"How do you decide when to write the code yourself vs. delegate it to someone less experienced, knowing it will take longer?"*
   - **Listen for:** Awareness that growing the team is part of the job. A pure executor will say "I just do it myself because it's faster." A leader will talk about the investment trade-off.

### Block 3: Transition and Motivation (10 min)

**Goal:** Understand why they are leaving, what they want, and whether your environment fits.

Questions:

7. *"What made you leave Spotify for a 20-person startup? And what is driving you to look at something new now?"*
   - **Listen for:** Pattern of what they value. If they left Spotify for speed and autonomy, and now they are leaving the startup -- why? Burnout? Wanting more structure? Wanting bigger impact? The answer tells you whether your environment is the next logical step or a random bounce.

8. *"This role is Senior on paper. The scope involves owning architecture for a team of 6, influencing cross-team decisions on our catalog API, and mentoring mid-level engineers. We have flexibility on level for the right person. How do you think about title vs. scope at this point in your career?"*
   - **Listen for:** Maturity about titles. The best answer is some version of "I care about the work and the impact, titles follow." A rigid attachment to "Staff" title is a flag -- not because titles don't matter, but because it suggests they may not see the move as a step forward.

9. *"What does your ideal engineering culture look like? Describe the best team you have ever been on."*
   - **Listen for:** Alignment with your team's reality. If they describe a team of 3 senior engineers shipping daily with no process, that is not your team. If they describe a team that balances autonomy with coordination, good design practices, and shared ownership, that is closer.

### Block 4: Technical Quick-Hits (10 min)

**Goal:** Sanity-check technical depth in areas relevant to your stack.

10. *"We deal with complex data models -- products with hundreds of attributes, multiple inheritance hierarchies, localization, and high write throughput. What PostgreSQL patterns or trade-offs come to mind for that kind of problem?"*
    - **Listen for:** Awareness of JSONB vs. EAV vs. normalized approaches, partitioning, indexing strategies, read vs. write optimization trade-offs. They do not need to have the "right" answer -- you want to see how they reason about data modeling.

11. *"Your open-source rate-limiting library -- what design decisions are you most proud of? What would you change if you rewrote it today?"*
    - **Listen for:** API design thinking, backward compatibility awareness, and self-critique. This is a low-pressure question that lets them talk about something they care about.

### Closing (5 min)
Give them time to ask questions. The quality of their questions is itself a signal. Strong candidates will ask about team dynamics, technical challenges, how decisions get made, and what success looks like. Weak candidates will ask about perks or nothing at all.

---

## 6. Scorecard for Post-Call Evaluation

Rate each dimension 1-5 after the call:

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Architecture ownership (can make and defend technical decisions) | High | ___ | |
| Mentorship (evidence of growing others) | High | ___ | |
| Technical depth (Go, PostgreSQL, distributed systems) | Medium | ___ | |
| Communication clarity (explains complex things simply) | Medium | ___ | |
| Motivation fit (why this role, why now) | Medium | ___ | |
| Title/level comfort (ok with Senior, or needs Staff framing) | Low | ___ | |
| Culture/pace fit (can operate in a mid-size company) | Medium | ___ | |

**Proceed to next round if:** Architecture ownership and Mentorship are both 4+, and no dimension is a 1.

**Consider Staff-level offer if:** All dimensions are 4+, and architecture ownership demonstrates cross-team or organizational influence, not just single-team decisions.

---

## 7. Red Flags to Watch For

- **"I just built it"** -- If every answer is about solo execution with no mention of collaboration, trade-off discussion, or bringing others along, they may be a strong individual contributor but not the leader you need.
- **Dismissiveness about process** -- "At my startup we just shipped" is not a useful attitude at 300 people. Look for awareness that coordination costs exist and are worth paying.
- **Vagueness about mentorship** -- If they cannot give a single concrete example of helping someone else grow, that capability may not exist yet.
- **Title fixation** -- If the conversation keeps returning to "but I am currently Staff," the transition may cause ongoing friction.
- **No questions about the team** -- If they only ask about the tech and not the people, they may not be wired for the team-leadership dimension you need.

---

## 8. Green Flags to Watch For

- **Trade-off language** -- "We considered X but chose Y because..." signals mature engineering judgment.
- **Ownership of failures** -- "This broke and here is what I learned" signals someone who has operated real systems.
- **Curiosity about your problems** -- If they start asking you probing questions about the catalog API challenges, they are already thinking like an architect.
- **Specific mentorship stories** -- Even informal ones ("I paired with our new hire for two weeks on the Kafka integration") count.
- **Excitement about scope, not title** -- "Tell me more about the cross-team dependencies" is the answer you want.

---

## 9. Logistics Recommendations

- **Call format:** Video call, 45-60 minutes. Do not do a phone screen for this level -- you need to see how they communicate.
- **Who should be on the call:** Just you (the hiring manager). Keep the first call 1:1 to build rapport. Bring in a peer or your tech lead for the second round.
- **Follow-up timeline:** If positive, move fast. This candidate profile (Go + distributed systems + Spotify pedigree + open source) is in high demand. Aim to schedule a second round within 3 business days of the first call.
- **Second round suggestion:** Pair them with your tech lead on a system design exercise using a real problem from your catalog API. Not a whiteboard algorithm -- a real architecture discussion. This will test both their technical chops and how they collaborate.
