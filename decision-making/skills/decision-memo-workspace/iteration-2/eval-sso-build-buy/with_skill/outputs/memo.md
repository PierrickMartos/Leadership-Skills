# Decision Memo: SSO Implementation for Enterprise Pipeline

**Date:** 2026-04-01
**Author:** [Product/Engineering Leadership]
**Audience:** Leadership team
**Decision needed by:** Tomorrow's leadership meeting (2026-04-02)

---

## Decision

Decide by 2026-04-02 whether to build SSO (SAML/OIDC) natively, buy via WorkOS, or delay affected enterprise deals to Q1 — to be confirmed by the leadership team before re-engaging these prospects.

---

## Context

- Three enterprise prospects with combined TCV of ~$800K have each independently cited SSO (SAML/OIDC) as a hard requirement before signing; this is not a nice-to-have.
- H2 product roadmap is already full, meaning any path that includes building SSO displaces committed work.
- The window is time-sensitive: these prospects are evaluating alternatives now; delay to Q1 risks losing at least some of them.
- Getting this wrong in either direction carries real cost: shipping a weak SSO implementation damages enterprise trust; over-investing in infrastructure at the expense of roadmap commitments has its own compounding cost.

---

## Options

**Option A: Build SSO natively (SAML/OIDC)**
- 6 weeks of engineering time for 2 engineers (12 engineer-weeks), delivered in-house
- Requires pulling those engineers off existing H2 commitments — something on the roadmap slips
- Dependencies: security review of implementation, QA, enterprise customer validation before go-live
- What we'd need to believe: we'll need fine-grained SSO control long-term anyway, the implementation risk is low, and the roadmap items being displaced are lower-value than $800K in near-term revenue

**Option B: Buy via WorkOS (or equivalent)**
- 2 weeks of engineering time to integrate; ongoing cost of $1,500/month (~$18K/year)
- Adds a third-party vendor dependency in the auth layer — a sensitive system
- Dependencies: security review and approval of WorkOS as a vendor, procurement/finance sign-off on recurring spend, legal review of data processing agreement
- What we'd need to believe: WorkOS is sufficiently mature and secure for enterprise buyers, prospects won't object to a third-party auth layer, and we don't anticipate needing to own this stack in the next 2–3 years

**Option C: Delay — re-engage in Q1**
- No engineering cost now; H2 roadmap stays intact
- Requires honest communication to all three prospects that SSO is on the Q1 roadmap
- Dependencies: willingness of prospects to wait 3–6 months and not sign with a competitor in the interim
- What we'd need to believe: these deals are not time-sensitive from the prospect's side, and no competitor will close them in the window

---

## Assumptions

| # | Assumption | Confidence | How to test |
|---|------------|-----------|-------------|
| 1 | SSO is a hard blocker for all three prospects (not a preference) | Medium | Call each prospect's champion today; ask directly "would you sign without SSO if we committed to Q1?" |
| 2 | The 6-week build estimate is reliable | Medium | Have the engineering lead do a quick spike or breakdown — 6 weeks for SAML/OIDC done well is plausible but tight |
| 3 | WorkOS (or equivalent) is acceptable to enterprise security/compliance teams | Low–Medium | Ask at least one of the prospects whether third-party auth providers are acceptable in their procurement process |
| 4 | $800K TCV translates to near-term closed revenue if SSO is unblocked | Medium | Confirm with sales — are these late-stage deals with signed LOIs, or still exploratory? |
| 5 | The H2 roadmap items displaced by a native build are lower-priority than this opportunity | Low | Requires explicit prioritization conversation with CPO and affected teams — not yet done |
| 6 | These prospects will wait until Q1 if we're transparent now | Low | One honest call to each prospect's champion would answer this quickly |

---

## Tradeoffs

| | Option A: Build | Option B: Buy (WorkOS) | Option C: Delay to Q1 |
|---|---|---|---|
| Revenue impact | Enables ~$800K if closed in H2 | Enables ~$800K if closed in H2 | At risk — deal loss likely for 1–2 prospects |
| Speed to unblock prospects | ~6 weeks | ~2 weeks | 3–6 months |
| Engineering cost | 12 engineer-weeks (H2 displacement) | ~2–3 engineer-weeks | 0 now, ~12 later |
| Ongoing cost | None beyond maintenance | $1,500/month ($18K/year) | None |
| Vendor risk | None | Auth layer dependency on third party | None |
| Reversibility | High (own the code) | Medium (migration cost to own later) | Low (deals may be gone) |
| Enterprise buyer trust | Highest (native auth) | Depends on WorkOS reputation with buyer | Lowest |

**The key tension:** Option A delivers the most durable outcome but displaces H2 commitments. Option B is the fastest path to unblocking revenue but adds a vendor dependency in a sensitive layer and still needs security and procurement approval (which could itself take weeks). Option C preserves the roadmap but treats $800K in pipeline as expendable.

---

## What We Don't Know

1. **Whether any prospect will wait.** If one of them has a Q3 board deadline, delay loses the deal entirely. This is knowable — a single call answers it.

2. **Whether WorkOS passes each prospect's security review.** Enterprise buyers often require vendor security questionnaires. WorkOS is generally well-regarded, but at least one prospect may have a policy against delegated auth providers. Unknowable without asking.

3. **What actually slips if we pull two engineers for 6 weeks.** The memo says "H2 is full" but not what's at stake. If the displaced work is a feature affecting a larger existing customer base, the tradeoff math changes significantly.

4. **Whether the $800K closes if SSO is unblocked.** Late-stage enterprise deals can stall for other reasons. If these are early-stage prospects using SSO as a proxy for "we're not ready to buy," unblocking SSO doesn't guarantee the revenue.

5. **How long WorkOS vendor approval actually takes.** Security and procurement reviews for a third-party auth vendor can take 2–6 weeks in enterprise-facing orgs. Option B's "2 weeks" is an engineering estimate; the full timeline including approvals may be longer than Option A.

---

## Recommendation

**Recommendation: Option B (Buy via WorkOS) with a parallel fast-track on approvals — conditional on no prospect objections to third-party auth.**

**Why this over the alternatives:**
- At 2 weeks of engineering time vs. 6, WorkOS limits H2 roadmap disruption while still unblocking revenue faster than any alternative.
- $1,500/month is a rounding error relative to $800K TCV; the ROI math is clear if even one deal closes.
- Building natively is the right long-term call but the wrong short-term call when you have a full roadmap and no committed timeline — it optimizes for architecture purity over revenue velocity when the prospect window is open.
- Delay should be treated as the fallback, not a default — Option C has the lowest ceiling and the highest deal-loss risk.

**What has to be true for this to work:**
1. At least 2 of 3 prospects confirm that WorkOS-style third-party auth is acceptable in their security posture (if not, Option A becomes necessary or Option C is forced).
2. Security and procurement approvals can be fast-tracked in parallel with engineering — WorkOS onboarding cannot start without those approvals, so the 2-week engineering estimate doesn't start the clock until approval is in hand.

**Conditional fallback:** If prospects require native SSO or WorkOS fails a security review, escalate to Option A immediately and deprioritize the lowest-value H2 initiative to absorb the engineering cost.

---

## Risks

| Risk | Likelihood | Severity | Mitigation |
|------|-----------|----------|------------|
| WorkOS vendor approval takes longer than engineering (killing the timeline advantage) | Medium | High | Start security and procurement review this week, in parallel — don't wait for the product decision to be finalized |
| Enterprise prospect rejects third-party auth provider | Medium | High | Confirm with each prospect's champion before committing to Option B; have Option A ready as fallback |
| SSO implementation (native) has security flaws that damage enterprise trust | Medium | High | If Option A is chosen: mandatory security review before any prospect gets access; do not rush to show a demo |
| Revenue doesn't close even after SSO is unblocked | Medium | Medium | De-risk by confirming late-stage indicators (POC done, legal reviewed, budget approved) before prioritizing this work |
| H2 roadmap displacement causes churn in existing customer base | Low–Medium | High | Explicit conversation with CPO on what gets deprioritized before committing to Option A or B |

---

## Approvals Required

This decision touches auth infrastructure, vendor spend, and a new contract — cross-functional approvals are required before execution.

| Function | Involvement | What they review | When needed |
|----------|------------|-----------------|-------------|
| **Security / InfoSec** | Blocking (must approve before WorkOS integration begins) | WorkOS vendor security posture, SOC 2 compliance, data processing scope, SSO implementation architecture | Before engineering kicks off — initiate review this week regardless of which option is chosen |
| **Finance** | Blocking (for new recurring vendor spend) | $1,500/month WorkOS subscription; confirm it falls within approved vendor budget or requires new approval | Before signing WorkOS contract; can run in parallel with security review |
| **Legal / Compliance** | Blocking (for new vendor contract) | WorkOS Data Processing Agreement, liability terms, any GDPR/SOC 2 obligations | Before contract signature; flag now if any prospects are in regulated industries |
| **Procurement** | Advisory | WorkOS contract terms, vendor onboarding process | Coordinate with Legal/Finance; may be lightweight if spend is below threshold |

> Note: Security review is the most likely bottleneck. Even if engineering starts on Option B, the integration cannot go to production without Security sign-off. Starting this review immediately is independent of which option is chosen and should happen today.

---

## Decision Criteria

**Who decides:** Leadership team at tomorrow's meeting.

**What would change the recommendation:**
- If 2+ prospects require native SSO (not third-party): Option A becomes necessary; leadership must explicitly choose what slips from H2.
- If Security review cannot be fast-tracked (e.g., 4+ week queue): Option B's timeline advantage disappears; reconsider Option A or a staged approach.
- If the engineering estimate for Option A comes in above 8 weeks: raises the bar on Option A significantly; Option B becomes more compelling or delay becomes necessary.

**Non-negotiables:**
- No SSO shipped without security review — regardless of deal pressure.
- If Option A is chosen, leadership must name what H2 commitment is being deprioritized before work begins. "We'll figure it out" is not acceptable given a full roadmap.

---

## Appendix A: Stated Assumptions About the Situation

The following were assumed in the absence of explicit input and would be worth confirming:

- "Enterprise prospects" are late-to-mid-stage (i.e., SSO is the final blocker, not an early-stage evaluation criterion).
- The $800K TCV is annual contract value, not lifetime value — still compelling relative to the engineering cost.
- "2 engineers for 6 weeks" is for a production-grade SAML/OIDC implementation, not a minimal prototype.
- The product team does not already have a third-party auth library partially integrated that would lower the Option A estimate.
- WorkOS pricing is at the standard $1,500/month tier; pricing may vary based on user volume or enterprise contract.
