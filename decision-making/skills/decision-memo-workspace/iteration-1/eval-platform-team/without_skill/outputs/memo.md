# Decision Memo: Platform Team Formation

**Date:** April 1, 2026
**Author:** Engineering Leadership
**Audience:** CTO
**Decision needed by:** April 8, 2026

---

## Recommendation

Form a dedicated platform team of 3 engineers, drawn from existing product squads, with a phased transition over 6–8 weeks to minimize delivery disruption. This is the right structural investment for a 40-person eng org experiencing the coordination failures that come with distributed infrastructure ownership.

---

## Context

We operate as a 40-person engineering organization with 4 product squads, each currently owning their own infrastructure. This model has produced three compounding problems:

- **Duplicated work**: Each squad independently manages provisioning, CI/CD pipelines, monitoring, and tooling — work that could be done once.
- **Inconsistent practices**: Infrastructure decisions made in isolation produce divergent configurations, making cross-squad debugging, onboarding, and compliance harder over time.
- **Cross-cutting incidents**: Infrastructure failures in one squad's ownership can affect all squads, but without a central owner, incident response is uncoordinated and root cause remediation is inconsistent.

The question is not whether to consolidate infrastructure ownership — the problems are real and will compound — but when and how.

---

## Options Considered

### Option A: Keep distributed model, add coordination layer
Each squad retains infra ownership. A lightweight "infra guild" meets regularly to align on standards, share patterns, and coordinate on incidents.

**Pros**: No headcount reallocation; no slowdown to feature delivery in the short term.

**Cons**: Coordination structures without authority rarely stick. Standards drift because no one is accountable for enforcing them. Incidents still lack a clear owner. Duplicated effort continues. This option addresses symptoms, not the structural cause.

**Assessment**: Viable as a stopgap, not a solution. We've likely already tried variants of this informally.

---

### Option B: Form a dedicated platform team (Recommended)
Extract 3 engineers (or 2 strong + 1 mid-level) from product squads to form a platform team. The team owns shared infrastructure, internal developer tooling, and platform reliability.

**Pros**:
- Single owner for platform reliability and incident response
- Economies of scale on infra work — one team doing it well instead of four doing it inconsistently
- Product squads become consumers of platform, not maintainers — cleaner cognitive boundaries
- Foundation for accelerating future product delivery (better CI/CD, observability, self-service infra)

**Cons**:
- Short-term reduction in product squad capacity (2–3 engineers removed)
- Risk of platform team becoming a bottleneck if it builds walls instead of self-service primitives
- Requires careful scoping to avoid the platform team accreting work indefinitely

**Assessment**: Correct structural move. The capacity hit is real but time-bounded; the problems of the distributed model are not.

---

### Option C: Hire dedicated platform engineers externally
Form the platform team with net-new hires rather than reallocating from existing squads.

**Pros**: Preserves current product squad capacity; brings fresh perspective.

**Cons**: Hiring takes 3–6 months minimum. Platform work requires deep knowledge of existing systems — external hires will spend months ramping. Infrastructure problems continue to compound during that window. More expensive.

**Assessment**: Wrong sequencing. Use this to grow the platform team after it's established, not to seed it.

---

## Decision: Option B

### Rationale

At 40 engineers across 4 squads, we're at the inflection point where distributed infrastructure ownership starts costing more than it saves in autonomy. The incidents-that-affect-everyone pattern is the clearest signal: we have shared infrastructure risk but no shared infrastructure ownership.

Forming a platform team does reduce near-term feature throughput. The right frame is: we're already paying an invisible tax on duplicated work and incident toil. The platform team makes that cost explicit and routes it toward a permanent fix.

The risk of the platform team becoming a bottleneck is real and worth managing actively (see mitigations below), but it is not a reason to defer the structural change.

---

## Implementation Plan

**Week 1–2: Scoping and selection**
- Define platform team's initial mandate: shared CI/CD, observability stack, deployment primitives, incident response ownership. Explicitly exclude: product-domain infrastructure, new feature work.
- Identify 3 engineers to seed the team. Prioritize engineers who already do disproportionate infra work or have demonstrated system-level thinking. Have direct conversations — this should feel like a growth opportunity, not reassignment.
- Designate an interim lead (or hire/promote into a Staff/Principal role if the right person exists internally).

**Week 3–6: Transition**
- Platform team conducts a 4-squad infra audit: document what exists, what's duplicated, what's diverged.
- Begin consolidating shared primitives: one CI/CD standard, one observability stack, one deployment workflow.
- Product squads retain current infra ownership during this window — no hard cutover yet.

**Week 7–8: Handoff and stabilization**
- Platform team takes on-call ownership for shared infrastructure.
- Define the interface between platform and product squads: what squads self-serve vs. what requires a platform request. Err toward self-service.
- Establish a lightweight SLA/SLO framework for platform reliability.

**Ongoing**
- Platform team backlog is visible and prioritized alongside product roadmap — no invisible work.
- Quarterly review: is the platform team accelerating product squads or slowing them?

---

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Platform team becomes bottleneck | Default to self-service primitives; avoid ticket-driven model; give squads escape hatches for urgent needs |
| Product velocity drops materially | Track feature throughput before/after; if drop exceeds 20% after 60 days, reassess team composition |
| Selected engineers feel punished | Frame as a senior track; ensure compensation and visibility reflect platform impact |
| Platform team drifts toward toil without strategic work | Mandate that 40%+ of platform capacity goes toward developer experience improvements, not just firefighting |
| Knowledge silos form | Require platform team to document and train; no "only we can do this" systems |

---

## What We Are Not Deciding

- Whether to adopt specific infrastructure technologies (Kubernetes, Terraform, etc.) — that's for the platform team to assess and recommend.
- Long-term platform team headcount growth — revisit at 6 months.
- Reorganizing squads or reporting lines — platform team sits alongside product squads, not above them.

---

## Success Metrics (6-month horizon)

- Reduction in infrastructure-related incidents that affect multiple squads (target: 50% reduction)
- Reduction in time-to-deploy for new services (target: from days to hours)
- Reduction in duplicated infra tooling/configuration across squads (target: single shared standard for CI/CD, observability, and deployment)
- Product squad eng satisfaction with platform (lightweight quarterly pulse, target: net positive trend)

---

## Ask

Approval to proceed with platform team formation on the timeline above, and alignment on the 3-engineer seed headcount reallocation from product squads.
