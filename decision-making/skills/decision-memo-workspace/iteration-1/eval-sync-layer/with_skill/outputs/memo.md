# Decision Memo: Data Sync Layer — Rewrite vs. Ship for Catalog Management Launch

**Author:** [Product/Engineering Lead]
**Date:** April 1, 2026
**Decision owner:** VP of Product (or VP of Engineering — see Decision Criteria)
**Decision deadline:** End of this week

---

## Decision

Decide by end of week whether to (A) ship the catalog management product on the current data sync layer and address technical debt post-launch, or (B) rewrite the sync layer before launch, delaying Q3 delivery by 2–3 months.

---

## Context

- We are 3 months from a planned Q3 launch of the new catalog management product.
- Two enterprise customers have been committed a Q3 delivery date and are actively waiting.
- Engineering has identified scaling issues in the current sync layer that will become problematic under production load.
- A rewrite is estimated at 2–3 months, which would push the launch to Q4 at the earliest — past our committed dates.

---

## Options

**Option A — Ship with current sync layer (recommended)**
- Launch on schedule in Q3 with the existing sync layer in place.
- Address the scaling issues through targeted post-launch fixes or a phased rewrite after customers are live.
- Requires: a clear-eyed assessment of what "scaling issues" means at launch-day load vs. long-term load; a credible debt retirement plan with committed capacity; and customer expectation management if degradation occurs.
- We'd need to believe: the current sync layer can handle the load of the initial 2 enterprise customers without critical failures, and that the team can retire the debt within 1–2 quarters post-launch without it compounding.

**Option B — Rewrite before launch**
- Delay launch by 2–3 months to rebuild the sync layer from scratch before any customers go live.
- Requires: renegotiating commitments with both enterprise customers; absorbing the Q3 miss; keeping the engineering team focused and scoped during the rewrite.
- We'd need to believe: the current sync layer would actually fail under early production load (not just at scale), that customers would accept a delay, and that the rewrite itself won't slip further.

---

## Assumptions

| Assumption | Confidence | How to test |
|---|---|---|
| The current sync layer can handle 2 enterprise customers at initial load without critical failure | Medium | Run load tests scoped to expected Day 1 data volumes; check against customer data profiles now |
| A rewrite can be completed in 2–3 months without scope creep | Low | Ask engineering for a detailed breakdown of the rewrite scope; check against prior rewrite estimates on this team |
| Enterprise customers will accept a 2–3 month delay if asked | Low | Have a direct conversation with each customer this week — do not assume |
| The debt can be retired post-launch without blocking feature work | Medium | Map the debt against the post-launch roadmap; assess if scaling issues affect specific features customers care about |
| Shipping with known debt won't create a support or reliability crisis in the first 90 days | Medium | Define what "scaling issues" means precisely — thresholds, failure modes, and customer-visible impact |

---

## Tradeoffs

| | Option A (Ship now) | Option B (Rewrite first) |
|---|---|---|
| Customer impact | Honors commitments; risk of degraded experience if sync fails under load | Breaks explicit commitments; customers must re-plan |
| Speed to revenue | Q3 as planned | Q4 at earliest |
| Engineering effort | Manageable now; concentrated debt work post-launch | 2–3 months of pre-launch work; launch work still ahead |
| Reversibility | Debt grows if not addressed post-launch; harder to fix under live load | More reversible — clean foundation, but timeline already lost |
| Risk | Operational risk if sync fails at scale; reputational risk if customers feel misled | Timeline risk and commitment risk now; lower operational risk post-launch |

**Customer value vs. internal convenience:** Option B is better for the engineering team's long-term health, but worse for the two customers who are waiting. That tradeoff must be named explicitly — choosing Option B is choosing to prioritize internal quality over external commitment, which may be the right call but should not be obscured.

---

## What We Don't Know

- **What "scaling issues" means at Day 1 load.** If the sync layer will fail with 2 enterprise customers, Option A is not viable regardless of timeline pressure. If it only breaks at 10x current expected load, the calculus changes. This is knowable this week via load testing or a technical review.

- **Whether the customers will accept a delay.** We have made commitments. We don't know if Option B is even a choice until we have that conversation. A customer who would walk is a fundamentally different situation than one who would accept a 2-month slip.

- **Whether the rewrite will actually take 2–3 months.** Engineering rewrites almost always expand in scope. There is no basis given for confidence in that estimate without a detailed breakdown. The real risk of Option B may be a 4–5 month delay.

- **Whether there's a middle path.** A targeted stabilization (not a full rewrite) that addresses the most critical failure modes in 3–4 weeks has not been mentioned as an option. This may or may not be feasible but should be evaluated before committing to a full rewrite.

---

## Recommendation

**Option A — Ship with the current sync layer**, subject to two conditions being met.

**Why this over Option B:**
- We have explicit commitments to two enterprise customers. Breaking those commitments carries real relationship and reputational cost that should not be traded away for internal quality improvements without a compelling operational reason.
- The stated scaling issues have not been confirmed to be launch-blocking. Until load testing shows the sync layer fails at expected Day 1 traffic, a full 2–3 month delay is not justified.
- The rewrite estimate has low confidence. A slip from 2–3 months to 4–5 months is plausible, compounding the cost of choosing Option B.

**What has to be true for this to work:**
1. Load testing this week confirms the sync layer can handle the initial 2-enterprise-customer load without critical failure.
2. A concrete, time-boxed debt retirement plan (team, scope, timeline) is committed before launch — not "we'll get to it eventually."

**If load testing reveals the sync layer will fail at launch-day load:** the recommendation flips. Ship date becomes a secondary concern; a broken launch is worse than a delayed one. In that case, evaluate whether a targeted stabilization (not a full rewrite) can close the gap faster than 2–3 months.

---

## Risks

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| Sync layer fails under early production load, causing customer-visible outages | Medium | High | Run load tests scoped to Day 1 data volumes before committing to Option A; define incident response playbook |
| Post-launch debt never gets addressed — team moves to next feature, debt compounds | Medium | High | Negotiate and document post-launch debt capacity before launch, not after |
| Customer relationship damaged if they experience reliability issues after committing to Q3 | Low–Medium | High | Set clear expectations with customers about known limitations; define SLAs carefully at launch |
| Engineering morale impact from shipping with known issues | Medium | Medium | Name the tradeoff openly with the team; pair the ship decision with a credible debt retirement commitment |
| Rewrite (if chosen) slips past 3 months | High (if chosen) | High | If Option B is selected, require a detailed scope breakdown and weekly milestones before approving |

---

## Decision Criteria

- **Who makes the call:** [VP of Product or VP of Engineering — clarify ownership before the deadline]
- **What would change the recommendation:** Load testing shows critical sync failure at expected Day 1 load, or either enterprise customer indicates they would churn over a delay (making Option A's commitment value moot).
- **Non-negotiables:**
  - A committed debt plan must accompany any decision to ship with the current sync layer.
  - The "middle path" (targeted stabilization) must be evaluated before committing to a full rewrite.

---

## Assumptions Made in This Memo

*This memo was written without access to the authors involved. The following assumptions were made and should be validated:*

- The two enterprise customers represent a material portion of near-term revenue or strategic importance — i.e., their commitments carry real weight.
- "Scaling issues" refers to performance/reliability under load, not a security or data-integrity flaw. A data-integrity issue would change the recommendation immediately.
- There is no contractual penalty for a delayed launch (beyond relationship impact) — if there is, the severity of Option B's customer risk increases.
- Engineering's 2–3 month estimate is for a full rewrite, not a targeted fix. A targeted stabilization path has not been scoped.
