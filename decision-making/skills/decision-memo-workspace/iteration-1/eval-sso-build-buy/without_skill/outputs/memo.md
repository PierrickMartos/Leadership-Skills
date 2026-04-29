# Decision Memo: SSO (SAML/OIDC) — Build, Buy, or Delay

**To:** Leadership Team
**From:** [Author]
**Date:** April 1, 2026
**Decision needed by:** Tomorrow's leadership meeting

---

## Bottom Line Up Front

We should buy WorkOS now. The $800K TCV at stake dwarfs the $108K 2-year cost of WorkOS, and the 4-week time savings protects our H2 roadmap. Building in-house is the right long-term answer, but not this half.

---

## Context

Three enterprise prospects — each unable to sign without SSO (SAML/OIDC) — have surfaced simultaneously. Combined TCV is approximately $800K. Our H2 roadmap is already full. We have three paths forward.

---

## Options Considered

### Option A: Build SSO In-House
- **Timeline:** 6 weeks, 2 engineers fully dedicated
- **Cost:** Engineering opportunity cost (12 engineer-weeks pulled from H2 roadmap)
- **Outcome:** Full ownership, no vendor dependency, SSO deeply integrated
- **Risk:** Roadmap disruption, longer time-to-close on $800K in deals, execution risk on a non-trivial security feature

### Option B: Buy — WorkOS (or equivalent)
- **Timeline:** ~2 weeks to integrate
- **Cost:** $1,500/month (~$18K/year, ~$36K over 2 years)
- **Outcome:** Production-ready SAML/OIDC quickly, frees engineering for roadmap
- **Risk:** Vendor dependency, recurring cost, some abstraction over auth behavior

### Option C: Delay Deals to Q1
- **Timeline:** Defer SSO work to next planning cycle
- **Cost:** $800K in TCV pushed 1–2 quarters; risk of losing deals entirely
- **Outcome:** Roadmap intact, no new technical debt or vendor
- **Risk:** High — enterprise sales cycles rarely survive a "no" followed by a delayed "yes." Competitors can close in the window.

---

## Recommendation: Option B — Buy WorkOS

### Financial case

| | Option A (Build) | Option B (Buy) | Option C (Delay) |
|---|---|---|---|
| Revenue at risk | $800K TCV recoverable | $800K TCV recoverable | $800K TCV at high risk |
| Direct cost | 12 eng-weeks (H2 roadmap) | ~$36K over 2 years | $0 direct |
| Net impact (2-yr) | Roadmap slip + $800K | $800K - $36K = **~$764K net gain** | Likely deal loss |

WorkOS costs roughly 4.5% of the TCV it unlocks. Even if we replace it with an in-house solution in 18 months (spending 12 eng-weeks then), we will have closed the revenue and protected this half's roadmap.

### Strategic case

- SSO is table stakes for enterprise, not a differentiator. Buying a proven solution is the right make-vs-buy call for commodity security infrastructure.
- A 2-week integration window is recoverable within H2 without meaningful roadmap damage. A 6-week window is not.
- Delaying deals to Q1 is high-risk: enterprise procurement windows close, champions move on, and competitors fill the gap.

### Risks and mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| WorkOS becomes a liability (pricing, outage, acquisition) | Low–Medium | Contract with exit clauses; plan in-house migration trigger (e.g., if cost exceeds $5K/mo or a strategic reason arises) |
| 2-week integration slips | Low | WorkOS has strong docs and SDKs; de-risk with a spike in week 1 |
| Prospects don't close even with SSO | Low–Medium | Validate SSO is the sole blocker before committing; get written confirmation from procurement contacts |
| Sets precedent for buying every enterprise feature | Low | Establish a make-vs-buy policy: buy commodity infra, build differentiators |

---

## Assumptions

- The $800K TCV figure is accurate and all three deals are contingent on SSO (not using SSO as a negotiating tactic).
- The two engineers who would build SSO are the same engineers currently committed to H2 roadmap work — their time is not slack capacity.
- WorkOS or a comparable vendor (Auth0 Enterprise, Okta CIAM) can deliver SAML + OIDC within the 2-week estimate.
- There is no existing contractual or security policy reason that prohibits third-party auth vendors.

---

## What We Are Not Deciding Today

- Whether to build SSO in-house eventually (likely yes, at a later stage when volume justifies it)
- Pricing structure changes for SSO as an enterprise tier feature
- Which specific vendor to use (WorkOS is the leading candidate; Auth0 and Okta are alternatives worth a 2-hour comparison)

---

## Proposed Decision

**Approve the WorkOS integration path.** Assign one engineer as lead for a 2-week integration, keeping the second engineer on the H2 roadmap. Target initial delivery to the three prospects within 3 weeks of approval (2 weeks build + 1 week for prospect validation and security review).

**Owner:** [Engineering Lead]
**Deadline:** Decision needed this week to maintain Q2 close timing on the $800K pipeline.

---

## Open Questions for the Leadership Meeting

1. Are all three prospects confirmed SSO-blocked, or is this a stated preference that could be managed contractually in the interim?
2. Do we have a make-vs-buy policy, or should we establish one as part of this decision?
3. Is there a security or compliance review required before onboarding WorkOS? (If yes, start it in parallel — it should not gate the decision.)
4. Should SSO become a named feature of an enterprise tier, and if so, does that change how we price these three deals?
