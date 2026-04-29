# Screening Report: Senior Backend Engineer — Product Catalog API Team

---

## Candidate Summary

A backend engineer with 7+ years of experience, currently Staff Engineer at a 20-person fintech startup where they built a payment processing pipeline handling 50k transactions/day in Go, PostgreSQL, and Kafka. Prior to that, promoted from mid to senior in 18 months at Spotify working on content delivery. Their trajectory shows consistent upward movement, strong technical depth in exactly the stack you need, and a bias toward building systems from scratch. The fit is strong on paper — the open questions are about mentorship, operating at mid-size company scale, and whether the title adjustment will be a sticking point.

---

## Overall Rating

| Rating | Meaning | Recommended action |
|--------|---------|-------------------|
| **4 — Yes** | Good fit with minor gaps that are likely addressable. | Proceed with the call. Use it to validate 1-2 specific areas. |

**Rating: 4 — Yes**

Strong technical match with direct experience in distributed systems, Go, PostgreSQL, and event-driven architectures. The gaps are around mentorship track record and adaptation to a larger organization — both are explorable in a conversation, not disqualifying on paper.

---

## Strengths

- **Direct stack match** — Go, PostgreSQL, Kafka, AWS. This is not adjacent experience; they have been building exactly the kind of systems your team runs, in the same technologies.

- **System design from zero** — Built a payment processing pipeline from scratch at 50k txn/day. This demonstrates the ability to own architecture decisions end-to-end, which is the core need you described.

- **High-throughput data systems** — Payment processing at scale and content delivery at Spotify both involve the throughput and data modeling complexity your product catalog API demands.

- **Event-driven architecture experience** — Kafka in the current role. This is listed as a bonus on the JD but it signals they think in terms of async, decoupled systems — valuable for a catalog API that likely publishes events downstream.

- **Fast promotion trajectory** — Mid to senior in 18 months at Spotify is a strong signal. Spotify is not a company that promotes lightly at the engineering level.

- **Open source contributor** — Maintains a Go rate-limiting library with ~800 stars. Shows they can write code that others find useful, which correlates with clean API design sense and the ability to communicate technical ideas.

- **Strong educational foundation** — MS CS from KTH (top-tier European technical university). Combined with the career trajectory, this is someone who has both the fundamentals and the applied experience.

---

## Gaps

- **Mentorship and people development** — No explicit evidence of mentoring mid-level engineers. At a 20-person startup, there may not have been mid-levels to mentor. This is your top must-have and the biggest unknown. — *Unknown*

- **Operating in a mid-size org** — They have worked at Spotify (large) and a 20-person startup (tiny). A 300-person Series C company has its own cadence: more process than a startup, more autonomy than a big corp. No direct experience at this stage. — *Unknown*

- **API design for external consumers** — The resume emphasizes internal systems (payment pipeline, content delivery). Your product catalog API likely has external or cross-team consumers with different reliability and design constraints. — *Unknown*

- **PostgreSQL at data modeling depth** — They use PostgreSQL, but it is unclear whether their experience involves the kind of complex relational modeling a product catalog demands (attribute inheritance, polymorphic schemas, localization) versus transactional workloads. — *Unknown*

---

## Risks

- **Title sensitivity** — They currently hold a Staff title. Even if the scope at a 20-person company is arguably smaller than a Senior role at your 300-person company, title regression can feel like a step backward. If they are motivated by title progression, this could be a deal-breaker or a source of early dissatisfaction. You mentioned having Staff budget — be prepared to discuss the path.

- **Startup-to-mid-size pace adjustment** — At a 20-person company, a Staff Engineer likely wears many hats, ships fast, and has minimal process overhead. Your team of 6 within a 300-person org will have more cross-team dependencies, planning ceremonies, and stakeholder management. The risk is not that they cannot adapt — it is that they might find it frustrating.

- **"Staff at a tiny startup" calibration** — Your instinct is right to question this. Staff at 20 people often means "the best engineer we have" rather than "operates at Staff scope." That said, building a payment pipeline from scratch and being the technical owner of a critical system is genuinely Staff-level work in terms of ambiguity and ownership. The question is whether they have operated at Staff scope in terms of *influence* — setting technical direction beyond their own project, making tradeoffs across teams, saying no to things.

- **Retention if hired at Senior** — If they accept a Senior title and later feel under-leveled, you risk losing them within 12-18 months. Better to be transparent about leveling criteria and the path to Staff at your company.

---

## Bias Check

Two signals worth noting:

1. **Halo effect from Spotify** — The Spotify stint is impressive and the fast promotion is a real signal, but be careful not to let it color the assessment of skills they have not actually demonstrated (e.g., mentorship, working in a mid-size org). Evaluate each dimension independently.

2. **Pedigree bias (KTH + Spotify)** — The combination of a top university and a prestigious employer creates a strong initial impression. The open source work and the fintech pipeline are more direct evidence of capability for this role than the brand names are. Weight the work, not the logos.

The user's concern about "is Staff at a tiny startup really Staff?" is a legitimate calibration question, not a bias signal. Title inflation at small companies is real and worth probing.

---

## Decision Framework

- **If you take this call, the question you are trying to answer is:** Can this person influence beyond their own code — mentor others, drive architectural decisions through consensus, and operate effectively with the process and cross-team dynamics of a 300-person company?

- **This candidate is a strong fit if it turns out that:** They have been informally mentoring at the startup (even if not titled that way), they are self-aware about the startup-to-mid-size transition, and they are motivated by scope and impact rather than title.

- **This candidate is not a fit if:** They have been purely heads-down executing (even brilliantly) with no evidence of growing others, or if they view a Senior title as a demotion they would resent rather than a calibration they understand.

- **What would change your mind:** Evidence of mentorship. If they can describe specific instances of helping other engineers level up — even informally — the rating moves to a 5 and you should move fast. If they cannot, this becomes a development bet rather than a proven capability hire.

---

---

# Call Preparation Guide

## Call Structure (45 minutes)

| Phase | Time | Purpose |
|-------|------|---------|
| **Opener** | 5 min | Build rapport, set expectations, give a quick overview of the team (6 engineers, catalog API, the need for architectural ownership and mentorship) |
| **Candidate story** | 10 min | Understand their narrative — why leave a Staff role at a startup? What are they looking for? What does the next step in their career look like? |
| **Deep-dive questions** | 20 min | Behavioral and situational questions targeting mentorship, architectural decision-making, and organizational fit |
| **Their questions** | 5 min | Pay attention to whether they ask about the team, the people, the problems — or only about stack, title, and comp |
| **Close** | 5 min | Next steps, timeline, and if appropriate, signal that Staff level is possible for the right person |

---

## Tailored Questions

> **Question 1: "Tell me about a time you helped a less experienced engineer grow — not just unblocking them on a task, but actually changing how they approached problems."**
> **Why this question:** This is the must-have. You need someone who can mentor mid-levels, and there is zero evidence of this on the resume. Put it first — if the answer is empty, you know the gap is real.
> **What good looks like:** A specific person, a specific change in their behavior or skill, described with enough detail that you can tell the candidate was intentional about the development. Bonus: they describe adjusting their approach to different people.
> **What to probe if the answer is vague:** "What specifically did you do differently than just answering their questions?" / "How did you know it was working?" / "What did you learn about teaching from that experience?"
> **Red flag:** Cannot name a single person or instance. Or describes "code review" as mentorship without any evidence of developmental intent.

> **Question 2: "At your current company, tell me about an architectural decision you made that other engineers initially disagreed with. How did you handle it?"**
> **Why this question:** Owning architecture decisions in a team of 6 at a 300-person company requires building consensus, not just being right. At a 20-person startup, they may have been able to decide unilaterally.
> **What good looks like:** Describes the disagreement with respect for the other perspective. Explains how they made their case (data, prototypes, written proposals — not authority). Shows the outcome but also what they learned or conceded.
> **What to probe if the answer is vague:** "Who disagreed and what was their argument?" / "How did you ultimately resolve it — did you convince them, compromise, or override?" / "Would you make the same decision today?"
> **Red flag:** Frames every disagreement as others being wrong. Cannot describe a time they changed their mind based on pushback. Or has never faced disagreement because they were the only one making decisions.

> **Question 3: "You are currently Staff at a 20-person company. This role is Senior at a 300-person company — though the scope is arguably larger. How do you think about that?"**
> **Why this question:** Directly addresses the title risk. You want to know if they have thought about this and whether it will be a source of friction.
> **What good looks like:** Self-aware about title calibration across company sizes. Focused on scope, impact, and growth rather than title. Asks intelligent questions about what Staff looks like at your company.
> **What to probe if the answer is vague:** "What matters more to you in a role — the title or the scope of problems you get to work on?" / "What would make you feel like this was a step forward, not a step back?"
> **Red flag:** Visibly deflated or defensive about the title. Insists their current Staff role is equivalent without engaging with the question. Or conversely, too eager to accept anything — which might signal desperation rather than genuine interest.

> **Question 4: "Tell me about building the payment processing pipeline. Walk me through the key architectural decisions — what did you choose, what did you reject, and what would you do differently now?"**
> **Why this question:** This is their showcase project. You are not testing whether they can talk about it — you are testing *depth of judgment*. Can they articulate tradeoffs, not just outcomes? Do they have hindsight? This tells you whether their architecture ownership is principled or accidental.
> **What good looks like:** Clear articulation of 2-3 key decisions with specific alternatives considered. Honest about what they would change. Understands the constraints they were operating under (team size, timeline, cost) and how those shaped the choices.
> **What to probe if the answer is vague:** "What was the hardest tradeoff?" / "What broke in production that you did not anticipate?" / "If you had a team of 6 instead of doing it yourself, how would the architecture be different?"
> **Red flag:** Cannot explain *why* they chose Kafka over alternatives. Describes the system as perfect with no regrets. Or cannot distinguish their decisions from the team's (scope inflation).

> **Question 5: "Our catalog API has complex data modeling — products with hundreds of attributes, inheritance, localization, polymorphic schemas. Your background is more in transactional systems. How would you approach ramping up on a domain like this?"**
> **Why this question:** Situational question targeting the data modeling gap. You are not expecting them to know product catalogs — you are testing how they learn and whether they are honest about what they do not know.
> **What good looks like:** Asks clarifying questions about the domain. Describes a concrete approach to ramping up (reading existing code, pairing with domain experts, building mental models). Shows curiosity rather than bravado.
> **What to probe if the answer is vague:** "What is the most complex data model you have worked with?" / "How do you typically learn a new domain — what is your process?"
> **Red flag:** Claims transactional and catalog modeling are basically the same thing. Or shows no curiosity about the domain complexity.

> **Question 6: "Describe a situation where you had to navigate a decision that involved engineers from outside your immediate team — maybe a platform team, an infrastructure team, or a partner team. How did you drive alignment?"**
> **Why this question:** At a 300-person company, cross-team influence is a core part of the Senior/Staff role. At a 20-person startup, there are no other teams. This probes whether they have any experience operating in a multi-team environment (Spotify would be the place).
> **What good looks like:** Draws on the Spotify experience. Describes navigating competing priorities, building relationships, or writing proposals that had to convince people outside their reporting chain.
> **What to probe if the answer is vague:** "How did you handle it when the other team had different priorities?" / "What did you do when you could not just escalate to get a decision made?"
> **Red flag:** Every example is from the 20-person startup where cross-team dynamics do not exist. Or defaults to "my manager handled the cross-team stuff."

> **Question 7: "What is the thing you are most looking for in your next role that you are not getting in your current one?"**
> **Why this question:** Motivation question. You need to understand whether what they want is what you can offer. If they want to manage people, this is not the role. If they want harder technical problems with more structure, this could be a great fit.
> **What good looks like:** Articulates something specific and self-aware — e.g., wanting to work with a larger team, wanting more engineering peers to learn from, wanting to build something with longer time horizons than a startup allows.
> **What to probe if the answer is vague:** "What specifically about the startup is no longer working for you?" / "If you could design the perfect next role, what would a typical week look like?"
> **Red flag:** Only talks about compensation or title. Or cannot articulate what they want — which suggests they are not being intentional about the move.

---

## Scoring Rubric

Use this during or immediately after the call.

| Dimension | Strong signal | Acceptable | Weak signal |
|-----------|--------------|------------|-------------|
| **Mentorship and people development** | Specific examples of growing other engineers with intentional approach and visible results | Has done informal mentoring (code review, pairing) and shows genuine interest in developing others | Cannot describe any instance of helping someone grow; views senior role as purely technical |
| **Architectural ownership and judgment** | Articulates tradeoffs clearly, shows hindsight, distinguishes their decisions from the team's, has been wrong and learned from it | Can describe architectural decisions but less depth on alternatives considered or lessons learned | Describes systems they built without explaining why, or cannot separate their contribution from the team |
| **Cross-team influence and communication** | Has navigated multi-team decisions, built consensus through writing/proposals, handled competing priorities | Has some experience (likely from Spotify) but was not the primary driver | All experience is in single-team contexts; defers to managers for cross-team alignment |
| **Startup-to-mid-size adaptability** | Self-aware about the transition, curious about how your org works, sees structure as enabling rather than limiting | Acknowledges the difference and is open to adapting, even if they have not done it before | Views process and structure as waste; wants to move fast and break things; not interested in how the org works |
| **Motivation and title alignment** | Focused on scope and impact, treats title calibration as reasonable, asks about path to Staff | Slightly concerned about title but willing to engage; motivated by the work | Fixated on title, defensive about current leveling, or unable to articulate why this move makes sense |

---

## Things to Watch for During the Call

- **How they talk about the engineers at their current startup.** Do they describe teammates as people they helped grow, or as people who were "already good" or "not really engineers"? This reveals whether they see developing others as part of their job.

- **Whether they ask questions about the team or only about the technology.** A candidate who wants to mentor and own architecture will ask about team composition, how decisions get made, what the biggest challenges are. A candidate who wants to code will ask about the stack, deployment, and tooling. Both are fine engineers — but only one is the hire you need.

- **How they handle the title conversation.** Watch for micro-reactions when you discuss the Senior level. Genuine self-awareness looks like engagement and questions. Resentment looks like brief answers, subject changes, or immediate negotiation. This is a leading indicator of whether they will be satisfied in the role.
