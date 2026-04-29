# Decision Memo: SSO for H2 Roadmap vs. Enterprise Pipeline

**For:** Leadership team  
**Decision needed by:** Tomorrow morning (2026-04-01)  
**Author:** [Product / Engineering leadership]

---

## Decision

Decide by April 2 whether to (A) build SSO natively in H2, (B) adopt WorkOS or equivalent third-party auth, or (C) defer the three enterprise deals to Q1, so the product roadmap and resourcing plan can be finalized before the quarter begins.

---

## Context

- Three enterprise prospects have independently identified SSO (SAML/OIDC) as a hard blocker to signing. Combined TCV is ~$800K.
- H2 roadmap is currently full — any SSO work displaces planned commitments.
- Two engineering paths exist: build natively (~6 weeks, 2 engineers) or buy via WorkOS (~2 weeks, 2 engineers, $1,500/month ongoing).
- Deferring the deals to Q1 keeps H2 intact but risks losing pipeline to competitors or cooling deal momentum.
- This decision is time-sensitive: prospects are evaluating now, and the Q1 deferral window has a closing date.

---

## Options

**Option A — Build SSO natively**
- 6-week effort, 2 engineers pulled from H2 roadmap
- Delivers SAML and OIDC in-house; no vendor dependency
- Requires deprioritizing or delaying existing H2 commitments
- We'd need to believe: the 6-week estimate is reliable, we can negotiate H2 commitments with internal stakeholders, and none of the three deals walks away during the build window

**Option B — Buy via WorkOS (or equivalent)**
- 2-week integration effort, 2 engineers
- $1,500/month recurring cost; SSO functionality becomes dependent on third-party uptime and roadmap
- Displaces ~2 weeks of H2 roadmap (significantly less than Option A)
- We'd need to believe: WorkOS is an acceptable long-term dependency, enterprise prospects will accept a third-party auth layer (most do), and the $18K/year cost is not a contractual or margin problem

**Option C — Defer deals to Q1**
- No H2 impact; roadmap stays intact
- Negotiates a hold with three prospects, targeting a Q1 close after SSO is built natively
- We'd need to believe: all three prospects will genuinely wait, deal momentum won't decay, and we can deliver SSO in Q1 without competing against a refreshed roadmap

---

## Assumptions

| Assumption | Confidence | How to test |
|---|---|---|
| 6-week build estimate is accurate for a production-ready SAML/OIDC implementation | Medium | Engineering spike or architecture review before committing; ask eng lead for a breakdown |
| All three prospects would accept a WorkOS-backed SSO (not just native) | Medium | Direct question to each AE / prospect contact this week |
| Deals can survive a 6-week build window without going dark | Low–Medium | AE gut check + explicit hold conversation with each prospect |
| Deals can survive a Q1 deferral (3–5 month wait) | Low | Direct qualification call with champions at each account |
| WorkOS's $1,500/month cost doesn't create margin, compliance, or data residency issues | Medium | Quick check with finance and legal; WorkOS SOC 2 / GDPR posture |
| H2 roadmap commitments are movable — internal stakeholders can absorb slippage | Unknown | Conversation with those stakeholders before this meeting |

---

## Tradeoffs

| | A: Build | B: Buy (WorkOS) | C: Defer |
|---|---|---|---|
| Revenue at risk | Lowest — closes deals fastest if estimate holds | Low — 2-week window is short | High — deals may not hold |
| H2 roadmap impact | High — 12 engineer-weeks displaced | Low — ~4 engineer-weeks displaced | None |
| Speed to close | 6+ weeks | ~2 weeks | Q1 (3–5 months) |
| Total cost | Engineering time only | $1,500/month ongoing + eng time | Engineering time in Q1 |
| Reversibility | High — owned code, no lock-in | Medium — migrating off WorkOS later has a cost | Low — deal momentum is not fully recoverable |
| Vendor dependency | None | Yes — adds third-party auth dependency | None |
| Customer value | Full — native, fast, reliable | Equivalent for most enterprise buyers | Delayed |

**Note on customer vs. internal framing:** From the customer's perspective, Options A and B are functionally equivalent — they both get working SAML/OIDC. The difference is entirely internal (build time, vendor dependency, roadmap displacement). Option C is the only one that's worse for the customer.

---

## What We Don't Know

- **Will prospects actually wait?** The $800K TCV is only real if at least some deals stay warm through the build window. We don't know how hard their buying timelines are. This is knowable — AEs should qualify this before tomorrow's meeting if at all possible.
- **What does the 6-week estimate actually include?** "SSO properly" is vague. Does it include admin provisioning, JIT user creation, multi-tenant config, audit logging? Scope creep could push the estimate materially. This is knowable with a 2-hour engineering breakdown.
- **Which H2 commitments would be displaced?** A 12 engineer-week pull for Option A isn't abstract — it means specific features slip. Leadership needs to see what's actually on the table before deciding. Partially knowable before tomorrow.
- **Are there compliance or data residency constraints that affect WorkOS?** Some enterprise buyers have restrictions on subprocessors. If even one of the three prospects has this constraint, Option B fails for that deal. Partially knowable by tomorrow via AE outreach.
- **Is SSO a one-time ask or a pattern?** If this is the third enterprise deal in six months blocked by auth, that changes the investment case significantly. Worth checking the pipeline for signal.

---

## Recommendation

**Option B — Buy via WorkOS (or equivalent), targeting a close within 2 weeks.**

**Why this over the alternatives:**
- $800K TCV against 2 weeks of engineering displacement and $1,500/month is a strong ROI. At current run rate, a single closed deal pays back years of WorkOS cost.
- Option A's 6-week window carries real deal-loss risk that is hard to quantify but shouldn't be dismissed — enterprise buying cycles don't pause reliably.
- Option C treats the H2 roadmap as sacred when the data suggests the right call is to protect the revenue. Deferring $800K in pipeline to avoid 2 weeks of eng disruption is the wrong trade.
- For most enterprise buyers, WorkOS-backed SSO is indistinguishable from native. If compliance requirements eliminate it for a specific prospect, we'll learn that quickly and can adjust for that deal.

**What has to be true for this to work:**
1. At least two of the three prospects accept a WorkOS-backed implementation (not native-only).
2. Engineering can deliver a production-ready integration in 2 weeks without quality shortcuts that create security or reliability issues.

**Conditional note:** If discovery reveals that all three prospects require native SSO with no third-party subprocessors, the recommendation shifts to Option A — accepting the H2 slippage to close $800K in ARR is still the right call over Option C.

---

## Risks

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| One or more prospects walk before WorkOS integration ships | Medium | High | AE calls today to confirm 2-week hold is acceptable; get verbal commitment |
| WorkOS integration takes longer than 2 weeks | Medium | Medium | Engineering confirms estimate with a 1-day spike before committing; scope clearly |
| Enterprise prospects reject WorkOS as a subprocessor | Low–Medium | High | AE qualification call specifically on this; check WorkOS compliance posture vs. each prospect's security requirements |
| WorkOS pricing or terms change unfavorably post-sign | Low | Medium | Review WorkOS contract terms; negotiate price lock if possible |
| H2 roadmap credibility suffers even with only 4 weeks of displacement | Low | Medium | Proactive comms to internal stakeholders before SSO work starts |

---

## Decision Criteria

- **Who decides:** CPO / CTO jointly, with input from Sales leadership on deal viability
- **What would change the recommendation:**
  - If engineering estimates WorkOS integration at more than 3 weeks, revisit Option A vs. B tradeoff
  - If AE discovery reveals 2+ prospects require native SSO only, move to Option A
  - If deal qualification reveals fewer than 2 prospects will hold for 2 weeks, seriously reconsider Option C (but still likely recommend A or B for the prospect that will wait)
- **Non-negotiables:** We do not ship SSO that isn't production-secure. Any implementation — bought or built — must pass a security review before it goes to enterprise prospects.

---

*Assumptions made in drafting this memo: (1) The two engineers required are available and not on single-threaded critical H2 work. (2) "SSO properly" for Option A means a reasonably full enterprise auth implementation, not a minimal prototype. (3) WorkOS or a comparable vendor (Auth0, Okta FGA) is available and can be evaluated within a day. (4) The $800K TCV figure represents contracts that would close within one quarter of SSO availability.*
