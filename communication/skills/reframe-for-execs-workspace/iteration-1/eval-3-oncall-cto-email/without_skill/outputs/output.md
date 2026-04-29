**Subject: On-call update — action needed on EMEA hiring**

Hi Marc,

**Bottom line:** Our on-call situation is causing attrition risk on the payments team. We can fix ~60% of the problem ourselves in 4–6 weeks. The remaining piece requires a hiring decision from you.

---

**What's happening**

Since restructuring on-call in October, we've had 23 pages in 6 weeks — 9 off-hours, with 7 requiring senior engineers to escalate. Two engineers mentioned last week they're considering leaving because of the burden. One of them owns the payments service.

**Root causes (identified)**

| Issue | Impact |
|---|---|
| Noisy alerting — fires on transient errors | ~40% of pages |
| Missing runbooks (order processing, notification dispatch) | Auto-escalates to Tier 2 by default |
| No senior engineers in EMEA time zones | Night pages route to US staff |

**What we can do ourselves (4–6 weeks)**

- Fix alerting configuration
- Write missing runbooks

Estimated outcome: 50–60% reduction in pages.

**What we need from you**

A decision on EMEA senior engineer hiring to close the coverage gap. This is outside my scope to decide alone.

Happy to walk through the options whenever works for you.
