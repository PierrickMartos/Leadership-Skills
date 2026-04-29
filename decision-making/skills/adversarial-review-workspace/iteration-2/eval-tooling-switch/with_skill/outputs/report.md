# Adversarial Review: Zendesk → Intercom Migration

---

## Decision Summary

Whether to migrate from Zendesk to Intercom for customer support. The "go" scenario: sign contract, run 2-month migration using $15k engineering budget, train 8 agents, decommission Zendesk. Primary drivers are 30% cost savings, agent UI preference, and access to product tours. A 2-week trial has been completed.

---

## Door Type Assessment

**Door Type:** Friction Door
**Reversibility Score:** 3

Reversing means re-migrating 3+ years of ticket history, retraining agents, rebuilding integrations, and negotiating a new Zendesk contract — painful and expensive but not impossible. The $15k engineering cost is recoverable in principle; agent muscle memory and customer-facing data continuity are the harder costs to undo.

**Recommended depth:** Full analysis with emphasis on hidden reversal costs.

---

## Key Assumptions

| Assumption | Confidence | How to Test |
|---|---|---|
| 30% savings holds over 12+ months | Low | Model Intercom's full pricing — seat fees + Fin AI per-resolution ($0.99) + Proactive Support Plus add-on ($99/mo) + channel add-ons — against current Zendesk all-in cost |
| Product tours feature drives meaningful outcome | Low | Define the business metric product tours are meant to move; check if it was tested during the trial |
| 2-month / $15k migration estimate is accurate | Low | Scope includes: data migration, workflow rebuild, integration re-wiring, SLA/report reconfiguration, agent training, parallel-run period |
| Agent UI preference translates to productivity gain | Medium | Measure handle time and CSAT during the trial — preference ≠ performance |
| Historical ticket data migrates cleanly | Low | Intercom's native import is limited; custom fields, automations, and macros require full rebuild |

---

## Market & External Context

**Intercom's pricing model has a variable cost trap.** Their base seat pricing ($85/seat/month for the Advanced plan, which covers most mid-market teams) is only the start. Fin AI charges $0.99 per resolved conversation. At 2,000 tickets/month with even 30% AI resolution rate, that's ~$600/month added on top — before the $99/month Proactive Support Plus add-on needed for product tours. Teams regularly report budgeting $500/month and paying $2,000+. The "30% cheaper" claim needs a precise apples-to-apples model, not a headline comparison.

**The per-resolution billing model is the market's most-complained-about pricing structure.** Multiple independent analysts flag it as a primary driver of churn back to alternatives. It's structurally unpredictable for finance teams.

**AI is rapidly commoditizing both platforms.** Zendesk acquired Ultimate (conversational AI) and has been aggressively building AI into its core product. Intercom's Fin AI bot is a competitive differentiator *today*, but Zendesk's trajectory suggests the gap narrows. A decision driven partly by AI/automation capability has a shorter shelf life than it appears.

**Product tours are widely available elsewhere.** Pendo, Appcues, Userpilot, and Chameleon all offer best-in-class product tours as standalone tools, many integrating with Zendesk. Bundling this capability into a support platform is convenient but not unique — and it's available as an add-on at $99/month rather than included.

**Migration complexity is consistently underestimated.** Multiple migration practitioners flag that Intercom and Zendesk have fundamentally different data models (Intercom's Users/Leads vs. Zendesk's unified Users; conversation threading vs. ticket threading). Custom fields, automations, macros, and SLA policies don't port — they must be rebuilt from scratch.

---

## Blind Spots

- **The "30% cheaper" number is unverified.** Nobody appears to have modeled the full Intercom bill at actual usage: 8 seats × $85 = $680 + Proactive Support Plus $99 + Fin AI resolutions at scale + any channel add-ons. Current Zendesk cost should include all add-ons too. This number needs to be built before the decision proceeds.

- **The trial didn't test the hard things.** A 2-week trial validated the UI and basic flows. It almost certainly didn't validate: migration of 3 years of ticket history, SLA management at volume, complex workflow rebuilds, or reporting parity. Trials are designed to feel good, not reveal migration pain.

- **Agent "UI preference" is a weak signal.** Teams consistently prefer new tools during evaluation phases. The real test is handle time, error rate, and CSAT 90 days post-migration when novelty has worn off and edge cases appear.

- **Product tours solve a product problem, not a support problem.** If product tours are valuable, the question is whether bundling them into your support platform is the right architecture — or whether a dedicated tool (Pendo, Appcues) gives you better capability without coupling your support infrastructure to a product engagement feature.

- **Switching cost compounds with scale.** At 2,000 tickets/month, this isn't a small operation. The bigger you are in Zendesk, the more technical debt the migration carries — more integrations, more automations, more custom reporting.

- **Loss of institutional knowledge.** Three years of Zendesk ticket data, macros, and reporting represents significant institutional knowledge. Even if data migrates, the operational intelligence (which automations are working, which macros handle edge cases, which reports stakeholders depend on) doesn't.

---

## Counterarguments

**The cost savings case is not made.** "30% cheaper" is a comparison of list prices at a specific tier, not a modeled total cost of ownership. Intercom's variable pricing is the most-complained-about aspect of the platform precisely because costs inflate with usage. With 2,000 tickets/month and any meaningful AI usage, savings could evaporate — or flip to a cost increase. Until someone builds the full bill model, this decision's primary financial justification is unverified.

**A 2-week trial is insufficient evidence for a migration decision.** Trials don't surface workflow gaps, data migration failures, integration breakage, or edge-case handling. The only honest test is a parallel run with a real data subset — and that wasn't done.

**The $15k engineering estimate is almost certainly low.** Standard migration guidance puts Zendesk-to-Intercom at 6–12 weeks of sustained effort for teams of this size. The $15k assumes a clean migration; the reality involves rebuilding every automation, macro, and workflow from scratch because the data models are incompatible. Engineering time estimates for migrations routinely miss by 2x.

**The product tours feature doesn't justify platform migration.** A $99/month add-on for a feature you could get from a best-in-class standalone tool isn't a sound reason to change your support infrastructure. If product tours are the tie-breaker, the decision is being driven by a minor feature, not a strategic platform assessment.

---

## Risk Factors

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| True cost exceeds Zendesk after Fin AI and add-ons | H | H | Build full 12-month cost model before committing; include per-resolution estimates at current ticket volume |
| Migration runs over time and budget | H | M | Get a fixed-scope quote from a migration specialist; add 50% buffer to estimate |
| Agent productivity dips post-migration (90+ days) | M | M | Define productivity baseline now; build go/no-go KPI into migration plan |
| Historical data doesn't migrate cleanly | M | H | Run a test migration on 6 months of ticket data before committing; identify what's lost |
| Product tours feature underwhelms or doesn't move the metric | M | L | Define success metric for product tours before migration; validate it was tested in trial |
| Intercom pricing model changes again | M | M | Negotiate price lock in contract; ensure exit clause is clear |
| Key integrations don't have Intercom parity | M | H | Audit all active Zendesk integrations against Intercom's integration catalog now |

---

## Alternative Paths

Three alternatives worth evaluating before committing:

1. **Stay on Zendesk + add product tours separately.** Pendo or Appcues (~$99–250/month) provides product tours without migrating your support infrastructure. If the UI complaint is real, invest in Zendesk training and workflow optimization. Net cost: far less than $15k migration + 2 months of disruption.

2. **Negotiate with Zendesk.** Three years of tenure and a competitive offer in hand is leverage. Zendesk's sales team has discretion. A 15–20% discount + product tours through a third-party integration might close the gap entirely at zero migration risk.

3. **Run a real parallel pilot, not a trial.** Before committing to migration, run Intercom in parallel on a dedicated queue (e.g., one product line or one agent team) for 60 days with real tickets, real integrations, and real data. This surfaces migration debt and validates the cost model before the $15k is spent.

---

## Think Big, Work Small

**The big bet:** Reduce support operating costs by 30% while modernizing the agent experience and enabling proactive product engagement through tours.

**Load-bearing assumptions ranked by uncertainty × impact if wrong:**

1. Total cost of ownership is actually 30% lower — *highest uncertainty, highest impact*
2. Migration scope is $15k / 2 months — *high uncertainty, high impact*
3. Intercom delivers productivity parity or improvement for agents — *medium uncertainty, medium impact*
4. Product tours feature moves a meaningful business metric — *high uncertainty, low-medium impact*

**Smallest next steps (each gates the next):**

- **Week 1:** Build the full Intercom cost model. 8 seats × plan tier + Fin AI resolutions at 20%/30%/40% resolution rates × 2,000 tickets + add-ons. Compare to current Zendesk all-in cost. If savings < 15%, stop here.
- **Week 2:** Audit all active Zendesk integrations and automations. Map each to Intercom equivalent. Identify gaps. Get a migration scope quote from a specialist (not just internal engineering estimate).
- **Week 3:** Negotiate with Zendesk. Present the Intercom pricing model as a concrete alternative. See what they offer.
- **Week 4–6 (if proceeding):** Run a real 30-day parallel pilot on a contained queue — not a sales trial but an operational test with real data, real workflows, and real integrations. Measure handle time, CSAT, and incident rate.

**Minimum viable version:** Before any migration commitment, complete the cost model and integration audit. These two steps cost ~1–2 days of internal work and either confirm or invalidate the primary rationale.

---

## Stress Test Questions

1. **What is Intercom's total monthly cost at 2,000 tickets/month with 30% AI resolution rate, 8 seats on Advanced, and Proactive Support Plus?** Build this model. Answer determines whether the cost savings case holds at all.

2. **Which Zendesk automations, macros, and integrations have no direct Intercom equivalent?** Audit required. Gaps here drive migration cost and post-migration productivity loss.

3. **During the 2-week trial, what was average handle time per ticket vs. Zendesk baseline?** If this wasn't measured, the "better UI" claim has no quantitative support.

4. **What specific business outcome are product tours meant to drive, and what's the current baseline?** If this metric wasn't tested in the trial, the feature is unvalidated.

5. **What does Zendesk offer if you tell them you have a 30% cheaper alternative on the table?** Until you've had this conversation, you haven't tested the cheapest path to your cost goal.
