# Decision Memo: Platform Team vs. Distributed Infrastructure Ownership

**Date:** 2026-04-01
**Author:** Engineering Leadership
**Audience:** CTO
**Decision deadline:** ~2026-04-08

---

### Decision

Decide by next week whether to form a dedicated platform team (2–3 engineers) or maintain distributed infrastructure ownership across the 4 product squads, to be confirmed by the CTO.

---

### Context

- Each of the 4 product squads currently owns its own infrastructure. This has produced duplicated tooling, inconsistent practices, and cross-squad incidents — costs that are already measurable.
- The engineering org is 40 people. At this size the coordination overhead of distributed ownership typically starts to compound; the question is whether it already has.
- Forming a platform team requires pulling 2–3 senior engineers out of product squads. In a 40-person org, that is a meaningful reduction in product throughput — roughly 5–8% of total headcount removed from feature work, concentrated on the strongest contributors.
- The default (do nothing) has a compounding cost: each new squad member, new service, or new incident adds to the coordination debt rather than retiring it.

---

### Options

**Option A — Form a dedicated platform team**
- Pull 2–3 engineers (likely senior/staff) from product squads to form a platform team with a clear mandate: shared infra, tooling, reliability, and developer experience
- Requires: backfill plan or explicit squad capacity reduction acknowledgment; clear charter and customer definition (internal devs); 90-day roadmap before team starts
- What we'd need to believe: the duplicated work and incident cost is already larger than the feature-delivery cost of removing 2–3 people; and that a small platform team can actually deliver shared leverage, not just become a bottleneck

**Option B — Keep distributed ownership, but formalize coordination**
- Each squad retains infra ownership; add a lightweight "infra guild" (recurring sync, shared runbooks, rotating on-call alignment) to reduce drift without a structural change
- Requires: eng manager commitment to hold squads accountable to shared standards; a designated point person per squad (part-time, not a new role)
- What we'd need to believe: the root cause of incidents and inconsistency is coordination gaps, not structural misalignment — and that a voluntary guild will actually hold over time

**Option C — Hybrid: thin platform function inside an existing squad**
- One squad takes on a platform mandate in addition to its product work; other squads contribute to shared infrastructure on a rotation or on-demand basis
- Requires: that squad to accept scope expansion without a proportional headcount increase; clear escalation path when platform work conflicts with product deadlines
- What we'd need to believe: one squad can absorb platform responsibility without burning out or deprioritizing it every sprint; this is rarely sustainable beyond 6 months

---

### Assumptions

| Assumption | Confidence | How to test |
|---|---|---|
| The incident cost and duplicated work are already larger than the throughput cost of removing 2–3 engineers | Medium | Audit the last 6 months: count hours lost to cross-squad incidents and duplicated infra work per squad; compare to estimated output of 2–3 engineers |
| A 2–3 person platform team can deliver meaningful shared leverage within 6 months | Medium | Talk to peer companies of similar size who've done this; scope a 90-day deliverable before deciding |
| The engineers who'd move to platform would be willing and effective in that role | Low | Have direct conversations before committing; not everyone who's good at infra wants a platform mandate |
| The guild/coordination model (Option B) will hold under sprint pressure | Low | Review whether the existing informal coordination attempts have worked; if squads already deprioritize shared work, a guild won't fix it |
| Backfill for vacated squad spots is achievable within the planning horizon | Medium | Check pipeline and hiring timeline before announcing the org change |

---

### Tradeoffs

| | Option A: Platform team | Option B: Guild / coordination | Option C: Hybrid (squad absorbs platform) |
|---|---|---|---|
| **Customer impact** | Neutral near-term; positive in 12+ months as reliability improves | Neutral; incidents continue at current rate | Likely negative — product squad gets distracted |
| **Feature delivery speed** | Reduced 10–15% near-term; recovers as platform delivers leverage | Unchanged | Reduced for the host squad; unchanged for others |
| **Infra consistency & reliability** | High improvement potential | Marginal improvement | Marginal improvement |
| **Reversibility** | Low — org change is hard to undo once announced | High — easy to escalate to Option A later | Medium — easier to convert to Option A than unwind |
| **Risk** | Execution risk (team charter, backfill, morale of moved engineers) | Recurrence risk (coordination fails under pressure, incidents continue) | Burnout risk for host squad |

**Note on customer value vs. internal convenience:** Option A is harder internally but is the only path with a realistic chance of improving reliability for end users. Options B and C are easier to execute but primarily serve internal comfort — they avoid the hard conversation about structural change without addressing the root cause.

---

### What We Don't Know

- **How much time are squads actually losing to duplicated infra work?** If it's less than 1 engineer-equivalent per quarter across all squads, Option A may not pencil out. If it's more, the case is strong. This is knowable: ask tech leads for a rough estimate before the CTO meeting.

- **Are the incidents caused by fragmented ownership, or by specific technical debt?** If the incidents are concentrated in one area (e.g., a shared service no one owns), a targeted fix may outperform a structural change. Audit the last 3 major incidents before deciding.

- **Would the 2–3 engineers moving to platform actually want the role?** If they don't, you'll get reluctant platform engineers — which is worse than no platform team. This is knowable before deciding: have the conversation.

- **What's the realistic hiring timeline for backfill?** If backfill takes 6+ months, the near-term throughput hit is larger than it looks. Check pipeline now.

- **Has the informal coordination already been tried and failed?** If squads have already attempted shared runbooks, infra syncs, etc., and they eroded, Option B is not a viable alternative — it's just repeating the same failed experiment.

---

### Recommendation

**Recommendation:** Option A — Form a dedicated platform team, with a structured 4-week transition and explicit charter before engineers move.

**Why this over the alternatives:**
- At 40 engineers and 4 squads, the coordination overhead of distributed infra ownership is already at the threshold where structural change pays off. The guild model (Option B) requires voluntary coordination to hold under sprint pressure — it hasn't held informally, and a formalized version rarely survives the first major product deadline.
- The cost of Option A is front-loaded and visible (feature slowdown); the cost of Option B is diffuse and compounding (incidents, duplicated work, engineer frustration). Front-loaded costs are easier to manage.
- Option C is the worst of both worlds: platform work will be deprioritized whenever it conflicts with squad product goals, which is every sprint.

**What has to be true for this to work:**
1. The engineers moving to platform are willing — not assigned reluctantly. Motivation matters more than seniority for platform work.
2. The platform team gets a clear 90-day charter with measurable outcomes before the first sprint, so they don't spend 6 months deciding what to build.

---

### Risks

| Risk | Likelihood | Severity | Mitigation |
|------|-----------|----------|------------|
| Platform team becomes a bottleneck — squads wait on infra changes instead of owning them | Medium | High | Define the platform team's model explicitly: "paved road" provider, not gatekeeper. Squads retain ability to deviate with documented justification. |
| Moved engineers feel sidelined from product work, morale drops | Medium | Medium | Co-design the platform charter with the engineers before they move; give them a clear mandate, not a maintenance ticket. |
| Product squads lose critical institutional knowledge along with the engineers | Low | High | 2-week transition overlap; each moving engineer documents their squad's infra state before leaving. |
| Backfill takes longer than expected, leaving squads understaffed | Medium | Medium | Don't announce the org change until backfill is in-process (offer stage or later). |
| Platform team solves the wrong problems — builds internal tooling nobody uses | Low | High | Set a 90-day charter reviewed with squad tech leads; validate priorities with the people who'll use the platform, not just the people building it. |

---

### Approvals Required

| Function | Involvement | What they need to review | When |
|---|---|---|---|
| **HR / People** | Blocking | Role changes and any compensation adjustments for engineers moving to platform | Before announcement, at least 1 week before decision deadline |
| **Finance** | Advisory | Budget impact if platform team creates new tooling/vendor spend (e.g., observability, CI/CD infrastructure) | Before 90-day charter is finalized |

No legal, security, privacy, or procurement approvals required for the org decision itself. Note: if the platform team's roadmap includes new vendor tooling (e.g., a new observability platform, managed Kubernetes), those procurements will require Security and Procurement review separately.

---

### Decision Criteria

**Who decides:** CTO, with input from engineering leadership and affected squad tech leads.

**What would change the recommendation:**
- If the infra time audit shows squads are losing less than 0.5 engineer-equivalent per quarter total → revisit Option B as a genuine alternative
- If 0 of the 2–3 candidate engineers want the platform role → delay and solve the staffing problem first; don't form a platform team with reluctant engineers
- If backfill pipeline is empty and time-to-hire is 6+ months → consider a phased approach: start with 1 engineer, expand after backfill lands

**Non-negotiables:**
- Do not form the team without a written charter and 90-day roadmap agreed before day one
- Do not move engineers without first having the direct conversation about willingness

---

### Appendix A: Assumptions — Context and Framing Notes

This memo assumes:
- "2–3 strong engineers" means senior or staff-level contributors, not junior engineers; the cost and the benefit are both higher for senior engineers
- The 4 product squads are roughly equal in size (~8–10 engineers each at 40-person org)
- "Occasional incidents that affect everyone" means at least 2–3 cross-squad incidents in the last 6 months, not one-off events
- There is no existing SRE or DevOps function; all infrastructure is currently handled by product engineers
- The CTO has authority to approve the org change without a broader leadership vote

If any of these assumptions are materially wrong, the recommendation may need to be revisited.
