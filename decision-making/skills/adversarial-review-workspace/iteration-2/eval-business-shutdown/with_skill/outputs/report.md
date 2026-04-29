# Adversarial Review: Shut Down Self-Serve Free Tier

---

## Decision Summary

Considering eliminating the self-serve free tier (~8,000 free users, ~200 convert to paid/quarter, ~$40k/month infra cost) and moving to sales-assisted only. Rationale: rising ACV ($18k), infrastructure cost drag, and a perception that the free tier signals "prosumer" not "enterprise." The implicit bet is that removing free kills the brand stigma, reduces cost, and unblocks enterprise sales cycles. Board meeting in 3 weeks creates a hard deadline.

---

## Door Type Assessment

**Door Type:** Friction door (leaning one-way)
**Reversibility Score:** 4

Reactivating a free tier after killing it is technically possible but practically damaging — you signal instability to prospects, lose the user base you'd accumulated (they don't come back), and re-incur all the trust-building time. The 3-week board deadline adds pressure that makes a poor decision likely to get locked in fast. Warrants full analysis.

---

## Key Assumptions

| Assumption | Confidence | How to Test |
|---|---|---|
| Free tier is causing enterprise deals to stall | Low | Interview the last 10 lost enterprise deals — ask directly if brand perception was a factor |
| $40k/month infra cost is primarily free-tier-driven | Medium | Isolate free-user infra cost vs. paid; check if a tiered/usage-capped free plan could drop this below $10k |
| Removing free will not reduce pipeline for paid | Low | Track inbound lead source attribution — what % of paid customers started as free or were referred by free users |
| Sales-assisted motion is ready to replace self-serve volume | Low | 200 conversions/quarter self-serve = ~$3.6M ARR intake annually; do you have AE capacity to replace that? |
| The "prosumer" perception is real, not just sales narrative | Low | Run win/loss interviews; one head of sales's opinion is not data |

---

## Market & External Context

The industry trend is away from binary PLG vs. SLG and toward hybrid. A 2024 survey found 46% of SaaS companies call their primary motion "hybrid" — not PLG, not SLG. The binary framing your head of sales is using ("we need to kill free to look enterprise") is not what successful companies are doing.

Companies that killed their free tiers had mixed outcomes. Deputy killed its free plan; TravelPerk made its starter plan free while monetizing via add-ons. The pattern: successful free-tier removals happened alongside a credible replacement motion (time-limited trial, sandbox, or PQL). Failed ones just created a dead end.

Freemium conversion benchmarks: 2–5% is typical; developer tools hit ~12%, collaboration tools ~9%. Your 200/quarter from 8,000 users = ~10% annual conversion — that is well above median. This is a healthy funnel, not a broken one.

At $18k ACV, you are still inside the zone where PLG-assisted or product-qualified lead (PQL) motions are viable. Pure PLG caps out around $50k ACV; you are not close to that ceiling. The $18k ACV does not by itself justify abandoning the self-serve funnel.

Slack, Asana, Airtable, and Mailchimp all restructured (not eliminated) their free tiers as ACV grew — they added usage caps, feature gates, and sales overlays rather than full removal. None fully eliminated free while staying competitive at the enterprise level.

---

## Blind Spots

**The math is being framed wrong.** 200 paid conversions/quarter at $18k ACV = ~$3.6M ARR input per year from the free funnel. Against $480k/year in infra costs, the funnel returns 7.5x. The question isn't "is the free tier expensive?" — it's "can you generate equivalent pipeline for less than $480k via sales-led?"

**Word of mouth and brand surface area.** 8,000 active free users are ambassadors, content creators, community contributors, and potential champions who change jobs. Killing the tier eliminates this compounding asset overnight, with no clear way to rebuild it.

**Head of sales incentive misalignment.** Sales leaders routinely blame the go-to-market instrument for their own pipeline problems. "We look like a prosumer tool" may mean "our AEs don't know how to sell upmarket yet." This is worth examining before making an irreversible structural change.

**Loss of competitive moat.** If a competitor maintains a free tier and you don't, you hand them top-of-funnel volume permanently. Switching costs in SaaS are real — users who adopt a competitor's free product rarely switch.

**Attribution blind spot.** If you don't have clean data on how many enterprise deals started as free users or were influenced by someone who used your product for free, you are flying blind on the decision's actual cost.

**Survivorship bias in the sales pipeline.** You know about enterprise deals you lost. You do not know how many enterprise deals your sales team is winning because the buyer's junior team member had already used your product for free.

---

## Counterarguments

**Against shutting down the free tier:**

The core argument — "we look prosumer" — is unverified opinion, not data. The actual financial case for the free tier is strong: 10% annual conversion at $18k ACV yields a funnel worth far more than its $480k/year infrastructure cost. No sales-assisted motion at your stage reliably replaces 200 warm, product-qualified conversions per quarter.

Enterprise buyers increasingly expect to try before they buy. Removing self-serve entirely creates friction at a moment in the market where buyers have more options and less tolerance for high-touch-only gating. A sales-only model at $2M ARR with a 3-person (assumed) sales team is not an enterprise motion — it's an aspiration.

The "prosumer stigma" is a positioning and packaging problem, not a pricing model problem. Slack was used by millions of free users while closing six-figure enterprise deals. The free tier did not prevent Salesforce from buying Slack for $27.7B. What mattered was how they positioned and packaged for enterprise, not whether a free tier existed.

Killing free to please the board narrative is a textbook one-way door taken for the wrong reason under artificial time pressure.

---

## Risk Factors

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| Pipeline drops significantly without replacement self-serve motion | H | H | Audit free-to-paid attribution before deciding; model pipeline replacement cost |
| Competitor captures free-tier organic volume | H | H | Monitor competitor free tier; consider time-limited trial as bridge |
| Enterprise deals don't improve after removal (perception was misdiagnosed) | M | H | Run win/loss interviews now, before the board meeting |
| Sales team doesn't have capacity to replace 200 conversions/quarter | H | M | Map current AE pipeline capacity against required volume |
| Free user community and word-of-mouth collapses | M | M | Grandfather existing users or offer alumni path; announce with long transition window |
| Board commits to sales-only strategy that takes 12+ months to produce results | M | H | Set explicit success metrics and review gate at 6 months |

---

## Alternative Paths

**Option A: Restructure, don't eliminate.** Cap the free tier on usage (seats, data volume, API calls) to drive infra cost below $10k/month. Add a sales overlay triggered by PQL signals (teams > 3, certain feature usage). This preserves pipeline while cutting cost.

**Option B: Replace free tier with time-limited trial.** 14–30 day full-featured trial eliminates indefinite infra drain, signals "serious product for serious buyers," and retains the self-serve conversion path. Many companies (Deputy, HubSpot) have moved this direction.

**Option C: Segment and wall off.** Keep free for individual/solo users with a hard ceiling on team features. Make team and admin features paid-only. This directly addresses the "prosumer" perception by making the enterprise capability clearly paid, without eliminating the top-of-funnel entirely.

**Option D: Run a pilot kill on new signups only.** Stop offering free to new signups for 90 days. Measure impact on inbound pipeline. Don't touch existing free users. This gives you real data before the board meeting without committing to an irreversible move.

---

## Think Big, Work Small

**The big bet:** Eliminating the free tier will unlock enterprise sales by repositioning the brand, reducing infra cost, and forcing buyers into a sales conversation where your team can capture higher ACV deals.

**Load-bearing assumptions ranked by uncertainty x impact:**

1. Free tier causes enterprise deal loss (high uncertainty, high impact if wrong)
2. Sales motion can replace self-serve pipeline volume (high uncertainty, high impact if wrong)
3. Free-to-paid attribution is low (medium uncertainty — likely underestimated)
4. Infra cost is primarily free-user-driven (medium uncertainty — cost may persist)

**Minimum viable version before committing:**

- Run Option D (pilot kill on new signups) for 60–90 days
- Instrument attribution now: tag every paid customer with their free-tier history
- Conduct 10 win/loss interviews in the next 2 weeks specifically asking about brand perception
- Get infra team to model cost of usage-capped free plan vs. full elimination

**Gate:** Only proceed to full free tier elimination if win/loss interviews confirm brand perception is a real buying barrier in 3+ lost enterprise deals, AND new signup pilot shows no meaningful pipeline drop.

---

## Stress Test Questions

1. **Of your last 20 lost enterprise deals, in how many did the buyer explicitly name "prosumer brand" as a reason?** If fewer than 5, the head of sales hypothesis is not supported. Path: pull CRM notes; call 5 lost prospects this week.

2. **What % of your current paying customers started as free users or were referred by someone who used your product for free?** If it's above 30%, the free tier is load-bearing for your current ARR base, not just future pipeline. Path: revenue ops query on account origin; takes 2 days.

3. **Can your sales team realistically close 200+ deals per quarter with average $18k ACV, given current headcount and ramp time?** 200 deals/quarter = ~800/year; at 3 AEs that's 270 deals per AE per year, which is implausible. Path: have RevOps model the capacity math before the board meeting.

4. **If you kill the free tier and inbound drops 40% in Q1, what is your recovery plan?** You need a committed answer before you commit to the decision. Path: draft the contingency plan now — it either exists or it doesn't.

5. **Is your enterprise positioning problem a product/packaging problem or a go-to-market signaling problem?** A new enterprise tier with distinct branding, SSO, audit logs, and SLA — without killing free — may solve the perception issue at a fraction of the risk. Path: check what your enterprise-losing competitors offer that you don't.
