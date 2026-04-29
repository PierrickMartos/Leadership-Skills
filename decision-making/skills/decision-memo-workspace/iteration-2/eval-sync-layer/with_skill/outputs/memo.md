# Decision Memo: Data Sync Layer Strategy for Catalog Management Launch

**Date:** April 1, 2026
**Author:** [Product/Engineering Lead — assumed]
**Decision owner:** VP of Product (or VP of Engineering — assumed)
**Deadline:** End of this week

---

### Decision

Decide by end of this week whether to ship the catalog management product with the current data sync layer on the Q3 timeline, or rewrite the sync layer now and accept a 2–3 month delay past Q3.

---

### Context

- We are 3 months from a planned Q3 launch of the new catalog management product. Two enterprise customers are already waiting and have received explicit commitments.
- The current sync layer has known scaling issues. Engineering has identified these as significant enough to push for a pre-launch rewrite.
- A rewrite would add 2–3 months to the timeline, pushing the launch to Q4 at earliest — breaking commitments made to enterprise customers.
- The default if no decision is made is drift: the engineering team continues pushing for the rewrite while the Q3 deadline approaches, increasing pressure and reducing options.

---

### Options

**Option A — Ship on Q3 timeline with the current sync layer**
- Launch catalog management in ~3 months with the existing sync layer as-is
- Requires identifying and documenting known scaling thresholds so customer onboarding can be managed within safe limits
- Requires a committed post-launch remediation plan with staffing and timeline for the sync layer rewrite
- What we'd need to believe: the current sync layer is stable enough to serve enterprise customers at their expected data volumes through launch and into early adoption; the team can contain exposure with operational workarounds; customers will not churn if they hit limitations during a defined transition window

**Option B — Rewrite the sync layer now, then launch**
- Pause feature work on catalog management, complete sync layer rewrite, then resume and launch
- Estimated timeline: 2–3 months for rewrite + 3 months remaining = 5–6 months to launch (Q4 at earliest)
- Requires renegotiating commitments with both enterprise customers; risk of losing one or both deals
- What we'd need to believe: the scaling issues are severe enough to make a Q3 launch genuinely untenable (not just uncomfortable); customers will accept the delay without penalty or deal loss; the rewrite scope and timeline estimate is reliable

**Option C — Partial mitigation: targeted fixes only, not a full rewrite**
- Identify the 1–2 most acute scaling bottlenecks and address only those before launch
- Lower engineering cost than full rewrite; potentially adds 4–6 weeks rather than 2–3 months
- Requires engineering to scope and commit to a bounded partial fix — not guaranteed if the problems are architectural
- What we'd need to believe: the scaling issues are not monolithic; partial fixes yield enough headroom to safely onboard the two enterprise customers through their initial usage ramp

---

### Assumptions

| Assumption | Confidence | How to Test |
|---|---|---|
| The 2 enterprise customers will not accept a 2–3 month delay without penalty or deal risk | Medium | Direct conversation with account leads or CS this week — ask explicitly what happens if we slip to Q4 |
| The current sync layer can handle the two enterprise customers' initial data volumes at launch | Medium | Engineering to run a load profile against known customer data volumes; can be done in days |
| The rewrite estimate of 2–3 months is reliable | Low | Engineering to break the rewrite into milestones and estimate to P90 confidence — current estimate likely has no buffer |
| Post-launch remediation will actually get staffed and shipped (not indefinitely deferred by new priorities) | Low | Requires an explicit written commitment from leadership, not just intent |
| Option C (partial fixes) is technically viable | Unknown | Engineering to assess within 2 days whether the bottlenecks are isolatable or architectural |

---

### Tradeoffs

| | Option A (Ship now, fix later) | Option B (Rewrite first) | Option C (Targeted fixes) |
|---|---|---|---|
| Customer impact | Meets commitments; risk of hitting scaling limits during early adoption | Breaks commitments; deal loss likely for 1–2 enterprise customers | Meets or slightly delays commitments; lower scaling risk than A |
| Speed to launch | 3 months (Q3) | 5–6 months (Q4+) | ~3.5–4 months |
| Engineering cost / effort | Low pre-launch; full rewrite cost deferred | Full rewrite cost now + 2–3 months delay | Partial effort now; remaining debt still deferred |
| Reversibility | Low — once customers are onboarded on the old layer, migration is costly | High — new layer is the right foundation | Medium — partial fixes may or may not be compatible with future rewrite |
| Risk | Scaling incident in production with enterprise customers; tech debt compounds | Deal loss; morale/credibility hit with engineering if delay slips further | Scope creep if "partial" fix expands; unclear headroom gain |

Option A is better for customers in the short term but worse if scaling limits surface post-launch. Option B is better for the architecture but transfers cost directly to the business via delayed commitments. Option C is the most nuanced but depends on a technical assessment that hasn't been done yet.

---

### What We Don't Know

- **What data volumes will the two enterprise customers actually produce at launch?** This directly determines whether the current sync layer is viable. It may be knowable before deciding — customer success or sales should have sizing information.
- **Are the scaling issues catastrophic or just uncomfortable?** "Scaling issues" covers everything from occasional slowdowns to data loss under load. The severity determines urgency. Engineering should characterize this in writing before the decision is made.
- **Is the rewrite estimate real?** A 2–3 month estimate for an architectural rewrite with no stated confidence interval should be treated as a floor, not a midpoint. This is knowable before deciding with a brief scoping session.
- **What is the actual customer contract exposure?** If commitments are in a signed contract, the legal and commercial implications of slipping the timeline may be material. This is knowable this week.
- **Can the partial fix path (Option C) buy meaningful headroom?** Not knowable without a 1–2 day engineering assessment. If this option is viable, it's likely the best path — but it can't be assumed.

---

### Recommendation

**Recommendation: Option A — ship on Q3 timeline — conditioned on two gates being met before end of week.**

The two enterprise customer commitments are not a detail — they are the business case. Breaking them for a rewrite the team hasn't scoped to P90 confidence, to fix scaling issues that haven't been characterized against real customer load, is the wrong trade. Tech debt is real, but it is manageable with operational guardrails and a committed remediation plan. Deal loss is not easily recoverable.

**Why this over the alternatives:**
- Option B prioritizes internal architectural preference over customer commitments, on an estimate that is almost certainly unreliable. That's the wrong order of operations.
- Option C is worth evaluating — but only if engineering can confirm within 48 hours that the bottlenecks are isolatable. If they can, revisit this decision with that scoping in hand.
- The core assumption for Option A — that the current sync layer is safe enough for these two customers through early adoption — is testable before the deadline. If it fails that test, the recommendation changes.

**What has to be true for this to work:**
1. Engineering confirms, via a load profile against actual customer data estimates, that the current sync layer won't fail under expected Q3 onboarding conditions. If they cannot confirm this, Option A is off the table.
2. Leadership commits in writing to a funded, staffed sync layer remediation project beginning no later than 30 days post-launch. Without this commitment, "ship and fix later" becomes "ship and live with it forever."

---

### Risks

| Risk | Likelihood | Severity | Mitigation |
|------|-----------|----------|------------|
| Sync layer hits scaling limits during enterprise onboarding, causing data issues or downtime | Medium | High | Load-test against real customer volumes before launch; implement scaling guardrails and customer onboarding pacing; have incident runbook ready pre-launch |
| Post-launch remediation gets deprioritized indefinitely by new features or incidents | High | Medium | Written leadership commitment with named owner, milestone date, and explicit prioritization signal before we ship |
| Rewrite estimate was the real blocker and engineering disengages from Q3 timeline | Medium | Medium | Acknowledge the debt openly with the engineering team; explain the business constraint; give the team ownership of the post-launch remediation plan |
| Enterprise customer discovers scaling limits during a critical demo or go-live moment | Low–Medium | High | Agree on customer onboarding sequence; avoid simultaneous heavy-load operations during first 30 days; set transparent expectations with customers on initial capacity |

---

### Approvals Required

This decision is primarily a product and engineering call. However:

| Function | Involvement | What They Need to Review | Timing |
|---|---|---|---|
| Legal / Contracts | Blocking to Option B | Whether existing customer commitments carry contractual penalties for delay | Before end of week — needed to fully evaluate Option B |
| Engineering Leadership | Blocking to Option A | Must confirm load-test results and sign off on "safe enough to ship" before decision is finalized | Within 48 hours |
| Sales / Account Management | Advisory | What the actual deal risk is if we slip to Q4; customer temperature on timeline | Within 48 hours |

No other cross-functional approvals required for Options A or C.

---

### Decision Criteria

- **Who makes the final call:** VP (addressee of this memo), in consultation with engineering lead
- **What would change the recommendation:**
  - If the load-test shows the current sync layer will fail at expected customer volumes → Option A is eliminated; evaluate Option C first, then Option B
  - If engineering confirms Option C is viable with <6 weeks of work → Option C becomes the preferred path; revisit before finalizing
  - If legal confirms material contractual penalties for Q3 slip → further reinforces Option A (or Option C)
- **Non-negotiables:** We do not launch if engineering cannot confirm minimum load safety. We do not choose Option B without a credible, scoped timeline and a clear customer communication plan.

---

### Assumptions Made in Writing This Memo

*(These are assumptions made in absence of input files — flagged for the decision owner to correct if wrong.)*

- "Enterprise customers" have signed agreements or LOIs with explicit Q3 commitments, not informal expectations
- The engineering team's push for a rewrite is genuine and sustained — not a negotiating position
- There is no Option D (e.g., switching sync vendors, using a managed service) that has been evaluated
- The team has not already begun the rewrite — timeline is still fully available
- "Scaling issues" means throughput/latency degradation at volume, not data integrity issues (if it's the latter, this changes the recommendation materially)
