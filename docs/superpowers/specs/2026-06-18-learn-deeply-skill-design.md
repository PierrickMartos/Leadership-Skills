# Design: `learn-deeply` skill + `learning` plugin

**Date:** 2026-06-18
**Status:** Approved design (revised after adversarial review round 1), pending implementation plan

## Goal

Add a skill that helps the user deeply understand and learn *any* subject — a concept,
theory, domain, system, paper, or chunk of code — by applying the Feynman Technique in
"translator" mode: Claude explains the subject in the simplest faithful terms, focused on
meaning and why it matters rather than jargon or mechanics.

Inspired by `logic-decoder` ("The Translator") from the Beyond Vibe Coding series by
simonyu. This generalizes that idea away from code-only comprehension to any subject.

**Marketplace fit:** the marketplace is leadership-oriented, and getting quickly and
honestly up to speed on an unfamiliar domain — a technology your team owns, a market, a
discipline before a decision — is a genuine leadership need. The skill stays general in
*subject* but is framed and triggered around deliberate "get me up to speed" learning, not
casual question-answering.

## Decisions (from brainstorming + review)

- **Scope:** Any subject (general), not code-only. Code is just one possible input.
- **Home:** New `learning/` plugin.
- **Mode:** Explain-to-me (translator). Claude does the explaining. No teach-back/quiz loop.
- **Skill name:** `learn-deeply`.
- **Source license:** MIT, verified 2026-06-18 against
  `github.com/simonyu0518/beyond-vibe-coding` (LICENSE file). This skill is a near-total
  rewrite (code-only → any-subject), so it is "inspired by", not a derivative — attribution
  is a courtesy, not a license obligation to retain the original copyright notice near the
  file. Credit the original (simonyu / Beyond Vibe Coding) in the README.

## Skill behavior: `learn-deeply`

Given a subject, the skill produces an explanation built from the elements below. The
format is **adaptive, not a fixed scaffold** — include the elements the subject warrants,
omit those it doesn't.

1. **Big picture** — what this is and why it matters, in one or two plain sentences.
   Always included.
2. **Feynman walkthrough** — simplest-form explanation with concrete analogies. Every
   technical term that must be used is defined inline. No unexplained jargon. Always
   included; length scales to subject complexity.
3. **Visual (conditional)** — a Mermaid concept map, flow, or sequence diagram. **Include
   only if** the subject is a process (has ordered steps), a hierarchy (has nested parts),
   or a flow (something moves between stages). **Omit if** it's a single definition, a
   principle, or prose with no moving parts. Never invent structure to fill the slot.
   *Example:* "how OAuth works" → include (sequence diagram); "the sunk-cost fallacy" → omit.
4. **Key parts table (conditional)** — part → what it does → why it's there. **Include only
   if** the subject has 3+ named components that interact; **omit** for atomic concepts.
   *Example:* "the Kafka architecture" → include; "what is entropy" → omit.
5. **Easy to get wrong (conditional)** — severity-marked findings: 🚨 common misconceptions
   / ⚠️ subtleties people miss / ℹ️ useful context. Only listed when the skill is actually
   confident they are real. **Do not manufacture misconceptions** for a subject the model
   isn't grounded in.
6. **Go deeper** — open questions worth clarifying + 2–3 concrete next steps. Always
   included.

**Complexity scaling:** a simple subject gets the big picture plus a short walkthrough — no
forced table or diagram. Reserve the full structure for genuinely layered subjects. A
mandatory scaffold for a trivial subject is itself filler, which the tone rule forbids.

**Tone:** onboarding a curious newcomer. Patient, no condescension, no filler.

### Epistemic guardrail (accuracy / uncertainty)

The format produces authoritative-looking artifacts, so the body MUST enforce honesty.
Because a no-retrieval model can't reliably introspect "do I actually know this" (confident
confabulation reads as high confidence), the guardrail leans on **observable proxies**, not
self-assessed confidence:

- **Stop-and-ask triggers** — when ANY of these hold, flag uncertainty and ask the user for
  source material instead of explaining: the subject is proprietary/internal to an org; it's
  named after the knowledge cutoff; the user supplied no source and the name is unfamiliar;
  or the explanation would rest on specific numbers, dates, or named citations the model
  can't anchor.
- When proceeding, name what's solid vs. what's a general inference, and point to a source
  to verify against — without inventing a citation.
- Never invent the 🚨/⚠️ findings to satisfy the format.

### Scope guardrails

- **Explain, don't do the work.** The skill analyzes and explains; it doesn't produce the
  user's deliverable. Concrete line: explain how a cover letter is structured, don't write
  their cover letter; explain the proof technique, don't solve their homework; explain what
  the module does, don't refactor it. The SKILL.md carries 2–3 such explain-vs-do examples.
  **In-scope exception:** illustrative worked examples in service of explanation are fine
  (and often required for Feynman analogies) — working *an* example proof to teach the
  technique is teaching; solving the user's specific named assignment is doing the work.
- **Redirect over-broad subjects.** If the subject is too broad for one pass, say so and
  ask the user to pick a narrower piece rather than producing a shallow survey.

### Triggering

The description can only key off the message, not session state — so the trigger is framed
around **lexical cues**, and we accept a residual ambiguous middle rather than pretending
it's clean.

- **Fires on:** an imperative study verb aimed at a **named subject as a topic** — "teach
  me how Kafka works", "I want to understand options pricing deeply", "help me get up to
  speed on RAFT", "walk me through the theory behind X", "explain X like I'm new to it".
- **Does NOT fire on:** a question about **something in front of the user** — referents like
  "this/that/the" pointing at code/an error/output: "explain why this test fails", "what
  does this function do", "explain this error". Treated as normal in-task conversation.
- **Ambiguous middle (acknowledged, not resolved):** "explain how JWT works" typed
  mid-debug, "walk me through what this regex does". The trigger matrix MUST include these;
  the goal is a low false-fire rate, not perfection.

## Files

**New:**
- `learning/.claude-plugin/plugin.json` — mirrors existing plugin metadata shape.
- `learning/.cursor-plugin/plugin.json` — Cursor mirror.
- `learning/README.md` — plugin overview + skill list + MIT attribution to source.
- `learning/skills/learn-deeply/SKILL.md` — frontmatter (`name`, `description`) + concise
  instruction body following repo conventions.

**Modified:**
- `.claude-plugin/marketplace.json` — add `learning` to `plugins[]` with
  `"category": "learning"` (existing plugins use `"leadership"`); bump `version`; set
  `description` to `"13 skills for Claude Code"` (drop "leadership" — no longer all
  leadership skills).
- `.cursor-plugin/marketplace.json` — same, `"13 skills for Cursor"`.
- Top-level `README.md` — list the new plugin/skill.

## Conventions

- Use the repo's own skills for catalog wiring: `add-plugin`, `update-plugin`,
  `validate-marketplace`.
- SKILL.md frontmatter: `name` + multi-line `description` with explicit trigger phrases AND
  the anti-trigger, matching the style of `decision-memo`/`adversarial-review`.

## Success criteria

- `validate-marketplace` passes.
- `learning` plugin appears in both marketplace catalogs with correct source path; both
  catalog descriptions and versions updated.
- **Trigger test matrix passes:** a should-fire set ("teach me how Kafka works", "help me
  get up to speed on options pricing") invokes the skill; a should-NOT-fire set ("explain
  why this test fails", "what does this function do", "explain this error") does not; and an
  ambiguous-middle set ("explain how JWT works", "walk me through what this regex does") is
  recorded with its outcome — perfection not required, low false-fire is. Run manually
  before merge; record results.
- **Adaptive format verified both ways:** a layered subject (e.g. "how OAuth works")
  produces diagram + parts table + go-deeper; an atomic subject (e.g. "the sunk-cost
  fallacy") MUST omit the diagram and parts table. A skill that always emits all six
  sections fails this criterion.
- **Honesty probed with a fake:** given a plausible but fictitious subject (an invented
  framework/library name), the skill asks for sources rather than producing a confident
  explanation — not only obviously-obscure topics.
- Refuses to produce the user's deliverable; redirects overly broad subjects.

## Out of scope (YAGNI)

- Teach-back / quiz / coaching mode (mode decision: explain-only).
- A dedicated code mode (general handles code as one input).
- Spaced-repetition, flashcards, or progress tracking.
- A full eval workspace (the decision-making pattern) — the lightweight trigger test matrix
  above covers the one genuinely risky behavior (over-triggering); a formal eval harness can
  be added later if the skill earns it.
