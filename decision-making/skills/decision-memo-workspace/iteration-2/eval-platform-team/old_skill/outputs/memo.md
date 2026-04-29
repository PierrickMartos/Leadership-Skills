# Decision Memo: Platform Team vs. Distributed Infrastructure Ownership

**Prepared for:** CTO  
**Author:** Engineering Leadership  
**Date:** April 1, 2026  
**Decision deadline:** One week

---

## Decision

Decide by next week whether to form a dedicated platform team (2–3 engineers) or maintain distributed infrastructure ownership across the 4 product squads, to be confirmed by the CTO.

---

## Context

- Each of the 4 product squads currently owns its own infrastructure, producing duplicated tooling, inconsistent practices, and cross-squad incidents — symptoms of a scaling problem that won't self-correct.
- At 40 engineers, the org is at the inflection point where informal coordination breaks down; platform concerns compound faster than squads can absorb them individually.
- The forcing event is the CTO's request for a proposal; the window is narrow. Delaying perpetuates the status quo with known, escalating costs.
- Getting this wrong in either direction has a real cost: too early and you pull capacity from product work without enough leverage; too late and infra debt blocks delivery regardless.

---

## Options

**Option A — Form a dedicated platform team**

- Extract 2–3 strong engineers from product squads into a new platform team with an explicit mandate: shared infra, tooling standards, incident reduction.
- Requires: identifying the right engineers (likely senior ICs), defining a clear charter, establishing an interface model with product squads (e.g., internal APIs, on-call, SLAs).
- We'd need to believe: the current infra pain is costing more capacity than extracting 2–3 engineers would, the org can coordinate cross-team, and the platform team can deliver visible value fast enough to maintain credibility.

**Option B — Keep distributed ownership, with coordination improvements**

- Each squad retains infra responsibility; add lightweight coordination mechanisms (a working group, shared runbooks, a common toolchain mandate).
- Requires: genuine squad commitment to cross-squad standards, a clear owner for enforcement, and enough slack in squads to do coordination work.
- We'd need to believe: the problem is coordination failure rather than structural misalignment, and voluntary alignment can work without a dedicated team to hold the line.

**Option C — Hire externally for the platform team**

- Same as Option A but staff the platform team with external hires rather than pulling from squads.
- Requires: budget approval, recruiting timeline (3–6 months minimum), and onboarding capacity.
- We'd need to believe: external hires can ramp fast enough to address current pain, and the org can absorb recruiting overhead now.

*Option C is not a near-term solution given the timeline and org size. It should be considered as a supplement to Option A, not a standalone alternative.*

---

## Assumptions

| Assumption | Confidence | How to test |
|---|---|---|
| The infra pain is costing more than 2–3 engineers' worth of product capacity across squads | Medium | Audit the last 90 days: count duplicated work, incident response hours, and blocked features attributable to infra issues. Even a rough tally is informative. |
| 2–3 engineers can realistically form a functional platform team (critical mass) | Medium | Benchmark against similar-size orgs. At 40 engineers, 2 may be too thin; 3 is a more defensible minimum. |
| The engineers pulled are senior enough to have leverage, and product squads can absorb their departure | Medium | Requires honest capacity planning per squad — a squad losing its infra expert may be disproportionately impacted. |
| Voluntary coordination (Option B) won't hold at this org size | Medium | Review the history: has the org tried coordination-only approaches before? If practices diverged despite prior alignment efforts, that's evidence. |
| The platform team can show meaningful wins within 90 days | Low–Medium | Define 2–3 concrete near-term deliverables before launch (e.g., unified CI pipeline, shared on-call runbook). Validate feasibility with the likely team members before committing. |

---

## Tradeoffs

|  | Option A: Platform team | Option B: Distributed + coordination |
|---|---|---|
| Customer impact | Neutral short-term; positive medium-term (fewer incidents, faster delivery once platform stabilizes) | Neutral to slightly negative (incidents continue; squads remain distracted by infra) |
| Feature delivery speed | Slower for 2–3 months (squad disruption + ramp-up); faster thereafter | Unchanged near-term; likely worsens as infra complexity grows |
| Cost / effort | High upfront (extraction, charter, coordination model); moderate ongoing | Low upfront; high ongoing (redundant work, incident response) |
| Reversibility | Moderate — reforming squads later is possible but disruptive | High — easy to step up from here if coordination fails |
| Risk | Platform team underdelivers or becomes a bottleneck; product squads lose key engineers | Infra debt compounds; a major incident forces a reactive, rushed fix |

*Note: Option B is primarily convenient for squads in the short term. It does not address the structural cause of the problem — it defers it.*

---

## What We Don't Know

- **Which engineers are the right candidates, and what does losing them do to their squads?** This matters because the extraction decision is not uniform — one squad may have a natural platform-oriented engineer with low squad disruption, while another may not. Not knowable at the org level without a squad-by-squad assessment. *Can be resolved before deciding.*

- **How bad is the infra problem, precisely?** The description is qualitative ("duplicated work, inconsistent practices, occasional incidents"). Without a rough quantification, it's hard to justify the tradeoff confidently. *Partially knowable in a week with a focused retrospective.*

- **What does the platform team's mandate look like, and will squads accept it?** A platform team without clear authority and squad buy-in becomes a service team that gets ignored. Whether the org will actually coordinate around a new team is unknown. *Partially testable by gauging squad lead reactions before deciding.*

- **Is this the right moment given current product commitments?** Extracting engineers mid-sprint, mid-quarter, or ahead of a launch creates outsized disruption. The timing of extraction matters, and we don't know the squad delivery calendars here. *Knowable immediately.*

- **Will 2 engineers be enough, or does the platform team need 3?** With 40 engineers and 4 squads, a 2-person platform team may lack resilience (on-call coverage, specialization, bus factor). *Resolvable with benchmarking and scope definition.*

---

## Recommendation

**Recommendation:** Form a dedicated platform team (Option A), targeting a 3-person team, with a phased extraction over 4–6 weeks rather than an immediate cutover.

**Why this over the alternatives:**

- The problem is structural, not behavioral. Coordination mechanisms (Option B) have likely been tried informally and haven't held. At 40 engineers across 4 squads, voluntary alignment degrades predictably — this is the right size to make the investment.
- The ongoing cost of distributed ownership (duplicated work, cross-squad incidents, inconsistent practices) is almost certainly greater than the short-term capacity hit of extracting 2–3 engineers, but this needs a 90-day audit to validate before finalizing.
- Option B preserves squad capacity in the short term but is primarily convenient, not strategically sound. It optimizes for comfort over the outcome.

**What has to be true for this to work:**

1. The extracted engineers are the right ones — senior enough to have platform-level leverage, and their squads can absorb the departure without critical feature work collapsing. This requires a squad-by-squad assessment before committing.
2. The platform team has a clear, scoped mandate with an explicit interface model (how squads consume platform work) from day one. A platform team without authority and a defined scope will drift into a service desk.

---

## Risks

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| Platform team underdelivers in the first 90 days; squads lose confidence and start routing around them | Medium | High | Define 2–3 concrete quick wins before launch; schedule a 90-day review with the CTO |
| One or more product squads lose a critical engineer and miss a delivery commitment | Medium | High | Do a squad-by-squad capacity audit before finalizing extraction targets; consider staggering moves |
| Platform team becomes a bottleneck rather than an enabler — squads blocked on platform approvals | Medium | Medium | Design the team as an enabler (golden paths, self-service tooling) not a gatekeeper; define SLAs from the start |
| The extracted engineers feel sidelined from product work and churn within 12 months | Low–Medium | High | Set an explicit, compelling charter; give the platform team a product mindset and visible impact; revisit comp/scope at 6 months |
| The 2–3 person team is too thin — on-call coverage breaks down, team is overwhelmed | Medium | Medium | Start with 3 not 2; plan for one external hire in H2 to reach sustainable critical mass |

---

## Decision Criteria

**Who decides:** CTO, with input from engineering leads.

**What would change the recommendation:**
- If the squad-by-squad capacity audit reveals that extraction would destabilize 2+ squads with near-term delivery commitments, delay extraction by one quarter and revisit.
- If a 90-day infra pain audit reveals the problem is concentrated in 1–2 squads rather than systemic, a lighter-weight working group model may be sufficient.

**Non-negotiables:**
- Any platform team must have a defined charter and an explicit interface model before launch — a team without a mandate is worse than no team.
- The decision on *which* engineers move must involve squad leads, not be imposed top-down.

---

*Assumptions made in this memo (not provided in the original brief): the org has a single CTO with final decision authority; there are no current plans to grow the eng org significantly in the next 6 months; the 4 squads are roughly equal in size; no prior formal attempt at a platform team has been made.*
