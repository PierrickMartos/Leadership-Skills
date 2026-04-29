# Escalation Routing and Draft: API Rate Limiting Ownership Gap

## Routing Advice

**Who to contact: both, but sequence matters.**

Start with the **principal engineer**, not the director. Here is why:

1. **This is a technical coordination failure first, not a management failure.** The principal engineer owns cross-team technical alignment. Going to the director first signals you've lost confidence in the engineering org's ability to self-coordinate, which can create unnecessary friction and make you look like you're politicking rather than problem-solving.

2. **The principal engineer has standing to convene the right people immediately.** They can call a 30-minute sync with the three tech leads and emerge with a concrete decision — something a Slack thread structurally cannot do.

3. **Loop in the director if the principal doesn't act within 48 hours, or if you know the principal engineer is already aware and has been passive.** At that point the risk is real enough that your director needs to know regardless, if only so they are not blindsided when a rate-limit incident happens in production three weeks from now.

**Tone to strike:** You are not blaming anyone. You are surfacing a risk, offering to help resolve it, and asking for a decision on who owns the coordination. You have done the right thing twice already (raising in #architecture-discuss). This escalation is the appropriate next step — not drama, just engineering process.

---

## Draft Message to Principal Engineer

**Channel:** Direct message or email (not a public channel — you want a response, not a debate)

**Subject / Opening line:** `API rate limiting strategy — three teams shipping in 3 weeks, no owner yet`

---

Hey [Name],

I want to flag a coordination risk before it becomes an incident.

Three teams — [Team A], [Team B], and [Team C] — are each building features that will call [external API name]. The first of those ships in three weeks. As of today, there's no shared rate limiting strategy and no single owner for how we handle quota allocation, throttling, retries, or failure modes across those three workstreams.

I've raised this in #architecture-discuss twice and got agreement that alignment is needed, but we haven't moved to a concrete decision or owner. At this point I'm concerned we'll either hit rate limits in production or three teams will build three incompatible approaches that create toil later.

What I'm asking for:
- Can you help identify who should own this decision? (A single team lead, a shared library, a working group — anything with a name and accountability.)
- If it would help, I can draft a one-pager on the options and circulate it ahead of a short sync. I just need someone with the authority to convene the right people.

Happy to jump on a 30-minute call this week with whoever makes sense. The window to sort this without impacting the ship date is closing fast.

Thanks,
[Your name]

---

## If You Need to Escalate to Your Director

Only send this if the principal engineer doesn't respond or act within 48 hours, or if you have reason to believe they won't. Frame it as a heads-up, not a complaint.

---

Hey [Director name],

Quick heads-up on a risk I want to make sure is visible to you.

Three teams are shipping features that all call [external API] over the next three weeks. We don't have a shared rate limiting strategy or an owner for that coordination. I've raised it in #architecture-discuss and just reached out to [Principal Engineer name] to ask for help assigning an owner, but I wanted you to know in case this needs a nudge or a different escalation path.

I'm not looking to create noise — I just don't want this to surface as a production incident when it could be addressed now with a short conversation and a clear owner.

Let me know if you'd like me to put together a brief writeup of the options.

[Your name]

---

## Key Principles Used in These Drafts

- **Lead with the risk, not the frustration.** The message is about what could go wrong, not about the failed Slack threads.
- **Make the ask specific and small.** "Who should own this?" is a much easier question to act on than "can we coordinate better?"
- **Offer to do the work.** Proposing a one-pager or a 30-minute sync lowers the activation energy for the person you're asking.
- **Time-box the urgency.** Naming the three-week window makes the risk concrete without being alarmist.
- **No blame, no CC drama.** Direct messages keep the conversation productive. Public channels invite lurkers and defensiveness.
