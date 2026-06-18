# Learn Deeply Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a `learning` plugin containing one skill, `learn-deeply`, that explains any subject in plain Feynman-style language, and wire it into both marketplace catalogs and the READMEs so validation passes.

**Architecture:** This repo is a marketplace, not runtime code. The "tests" are the deterministic validator `scripts/validate_marketplace.py` (structure, counts, README consistency) plus a manual behavioral checklist run in a fresh Claude session (trigger accuracy, adaptive output, honesty). Work bottom-up: relax the validator's count regex, create the new plugin's files (invisible to the validator until catalogued), then wire everything into the catalogs/READMEs in one atomic commit so the validator never sees an inconsistent half-state.

**Tech Stack:** Markdown SKILL.md files, JSON catalogs/metadata, Python 3 validator. No build step.

## Global Constraints

- Skill frontmatter `name` MUST equal its directory name (`learn-deeply`) — validator enforced.
- Claude `plugin.json` requires: `name`, `version`, `description`, `keywords`, `license`, `author`.
- Cursor `plugin.json` requires: `name`, `displayName`, `version`, `description`, `author`, `license`.
- Claude and Cursor catalogs MUST list plugins in the same order with the same names.
- A plugin's Claude and Cursor `version` MUST match.
- Total skill count across all catalogued plugins is currently 12; after this work it is 13.
- The count phrase must appear and equal 13 in: `.claude-plugin/marketplace.json` `description`, `.cursor-plugin/marketplace.json` `metadata.description`, and the `README.md` subtitle.
- Top-level `README.md` needs, per plugin, a `<summary><strong><code>NAME</code></strong> (N skills)` block with N matching the real skill count, and every skill name in backticks somewhere in the file.
- Each plugin `README.md` needs a `## Skills` section whose table has one row per skill.
- No em/en dashes per author style is NOT enforced here; match the existing repo copy, which DOES use em dashes in descriptions. Follow the repo, not the global style rule, for catalog/README copy consistency.
- Run `python3 scripts/validate_marketplace.py` from repo root; exit 0 = pass.

---

### Task 1: Relax validator count regex to make "leadership" optional

Lets the count phrase read "13 skills" (the marketplace is no longer all leadership) while staying backward compatible with the current "12 leadership skills" copy.

**Files:**
- Modify: `scripts/validate_marketplace.py:173`

**Interfaces:**
- Consumes: nothing.
- Produces: a `count_pattern` that matches both `"12 leadership skills"` and `"13 skills"`.

- [ ] **Step 1: Confirm the current state is green**

Run: `python3 scripts/validate_marketplace.py`
Expected: `Marketplace validation passed: 12 skills across 4 plugins.`

- [ ] **Step 2: Relax the regex**

In `scripts/validate_marketplace.py`, change line 173 from:

```python
    count_pattern = re.compile(r"(\d+)\s+leadership skills")
```

to:

```python
    count_pattern = re.compile(r"(\d+)\s+(?:leadership )?skills")
```

- [ ] **Step 3: Verify still green with existing copy**

Run: `python3 scripts/validate_marketplace.py`
Expected: `Marketplace validation passed: 12 skills across 4 plugins.` (unchanged — current copy still says "12 leadership skills", which the new pattern still matches).

- [ ] **Step 4: Commit**

```bash
git add scripts/validate_marketplace.py
git commit -m "chore: allow optional 'leadership' in skill-count phrase"
```

---

### Task 2: Create the `learn-deeply` skill and `learning` plugin files

Creates every file under `learning/`. The validator ignores plugins not yet in the catalog, so it must still report 12 skills after this task — that is the signal the new files are well-formed but not yet wired in.

**Files:**
- Create: `learning/.claude-plugin/plugin.json`
- Create: `learning/.cursor-plugin/plugin.json`
- Create: `learning/README.md`
- Create: `learning/skills/learn-deeply/SKILL.md`

**Interfaces:**
- Consumes: nothing.
- Produces: a `learning` plugin directory with one skill `learn-deeply`, ready to be catalogued in Task 3.

- [ ] **Step 1: Write the Claude plugin metadata**

Create `learning/.claude-plugin/plugin.json`:

```json
{
  "name": "learning",
  "description": "Learning skills — deeply understand and get up to speed on any subject using the Feynman Technique.",
  "version": "0.1.0",
  "keywords": ["learning", "feynman", "understanding", "explanation", "onboarding"],
  "license": "MIT",
  "author": {
    "name": "Pierrick Martos",
    "url": "https://github.com/PierrickMartos"
  }
}
```

- [ ] **Step 2: Write the Cursor plugin metadata**

Create `learning/.cursor-plugin/plugin.json`:

```json
{
  "name": "learning",
  "displayName": "Learning",
  "version": "0.1.0",
  "description": "Learning skills — deeply understand and get up to speed on any subject using the Feynman Technique.",
  "author": {
    "name": "Pierrick Martos",
    "url": "https://github.com/PierrickMartos"
  },
  "license": "MIT",
  "keywords": ["learning", "feynman", "understanding"]
}
```

- [ ] **Step 3: Write the skill**

Create `learning/skills/learn-deeply/SKILL.md`:

````markdown
---
name: learn-deeply
description: >
  Explain any subject — a concept, theory, domain, system, paper, or piece of code — in the
  simplest faithful terms using the Feynman Technique, so the user genuinely understands it
  rather than just hearing jargon. Use when someone wants to deliberately learn or get up to
  speed on a topic: "teach me how X works", "I want to understand X deeply", "help me get up
  to speed on X", "walk me through the theory behind X", "explain X like I'm new to it". Do
  NOT use for in-task questions about something in front of the user — "explain why this test
  fails", "what does this function do", "explain this error" — those are normal conversation,
  not learning requests. Explains and analyzes only; it does not produce the user's deliverable.
---

# Learn Deeply

You are The Translator. Someone wants to truly understand a subject — to make it click, in
plain language, the way a great teacher onboards a curious newcomer. Explain what it means
and why it matters, not the surface mechanics or the jargon.

The Feynman Technique in one line: if you can't explain it simply, you don't understand it.
Your job is to do that simple explaining for the user.

**Be honest before you're impressive.** A confident, fluent explanation of something you're
hazy on is the worst failure mode here. Read the epistemic check below before you start.

## Method

Build the explanation from the elements below. This is **adaptive, not a fixed scaffold** —
include what the subject warrants, omit what it doesn't. Scale length to complexity: a simple
subject gets the big picture and a short walkthrough, nothing more.

1. **Big picture** (always) — what this is and why it matters, in one or two plain sentences.
2. **Feynman walkthrough** (always) — explain it in the simplest faithful terms, with concrete
   analogies. Define every technical term inline the first time you use it. No unexplained
   jargon. Length scales to the subject.
3. **Visual** (conditional) — a Mermaid concept map, flow, or sequence diagram. Include ONLY if
   the subject is a process (ordered steps), a hierarchy (nested parts), or a flow (something
   moves between stages). Omit for a single definition, a principle, or prose with no moving
   parts. Never invent structure to fill the slot. Example: "how OAuth works" → include a
   sequence diagram; "the sunk-cost fallacy" → omit.
4. **Key parts** (conditional) — a table of part → what it does → why it's there. Include ONLY
   if the subject has 3+ named components that interact. Omit for atomic concepts. Example:
   "the Kafka architecture" → include; "what is entropy" → omit.
5. **Easy to get wrong** (conditional) — 🚨 common misconceptions / ⚠️ subtleties people miss /
   ℹ️ useful context. List these ONLY when you are actually confident they are real. Do not
   manufacture misconceptions to satisfy the format.
6. **Go deeper** (always) — open questions worth clarifying, plus 2–3 concrete next steps to
   learn more.

## Epistemic check (do this before explaining)

You have no retrieval. You cannot reliably introspect "do I really know this" — confident
fabrication feels just as certain as real knowledge. So gate on observable signals, not on
your felt confidence. **Stop and ask the user for source material** (instead of explaining) if
ANY of these hold:

- The subject is proprietary or internal to a specific organization.
- It is named after your knowledge cutoff, or you don't recognize the name.
- The user gave no source and the explanation would rest on specific numbers, dates, or named
  citations you can't anchor.

When you do proceed, separate what's solid from what's a general inference, and point to a
source to verify against — without inventing a citation.

## Scope

- **Explain, don't do the work.** You analyze and explain; you don't produce the user's
  deliverable. Explain how a cover letter is structured — don't write theirs. Explain the proof
  technique — don't solve their assignment. Explain what the module does — don't refactor it.
  In-scope exception: an illustrative worked example in service of teaching is fine (Feynman
  analogies often need one). Working *an* example to teach the method is teaching; producing the
  user's specific named artifact end-to-end is doing the work.
- **Redirect what's too broad.** If the subject is too large for one pass ("explain machine
  learning"), say so and ask the user to pick a narrower piece rather than producing a shallow
  survey.

## Tone

Onboarding a curious newcomer. Patient, plain, no condescension, no filler.
````

- [ ] **Step 4: Write the plugin README**

Create `learning/README.md`:

```markdown
# Learning

Skills for deeply understanding any subject — a concept, a domain, a system, a paper, a piece of code. Explains what it means and why it matters in plain language, using the Feynman Technique, so it actually clicks.

## Skills

| Skill | Purpose |
|-------|---------|
| `learn-deeply` | Explain any subject in the simplest faithful terms using the Feynman Technique — big picture, plain-language walkthrough, and where to go deeper. |

## Credits

`learn-deeply` was inspired by the MIT-licensed [`logic-decoder`](https://github.com/simonyu0518/beyond-vibe-coding) skill ("The Translator") from the Beyond Vibe Coding series by simonyu, generalized from code comprehension to any subject.
```

- [ ] **Step 5: Verify the new files are well-formed and the validator is unaffected**

Run: `python3 -c "import json; json.load(open('learning/.claude-plugin/plugin.json')); json.load(open('learning/.cursor-plugin/plugin.json')); print('json ok')"`
Expected: `json ok`

Run: `python3 scripts/validate_marketplace.py`
Expected: `Marketplace validation passed: 12 skills across 4 plugins.` (still 12 — `learning` is not catalogued yet, so the validator ignores it. If it errors here, a new file is malformed.)

- [ ] **Step 6: Commit**

```bash
git add learning/
git commit -m "feat: add learn-deeply skill and learning plugin"
```

---

### Task 3: Wire `learning` into both catalogs, counts, and the top-level README

Atomic integration: add the plugin to both catalogs, bump the marketplace version, change the three count phrases to "13 skills", and add the README summary block. After this task the validator reports 13 skills.

**Files:**
- Modify: `.claude-plugin/marketplace.json`
- Modify: `.cursor-plugin/marketplace.json`
- Modify: `README.md`

**Interfaces:**
- Consumes: the `learning` plugin dir from Task 2; the relaxed regex from Task 1.
- Produces: a fully consistent catalog at 13 skills across 5 plugins.

- [ ] **Step 1: Add `learning` to the Claude catalog and bump version/count**

In `.claude-plugin/marketplace.json`:
- Change `"version": "0.4.0"` to `"version": "0.5.0"`.
- Change `"description": "12 leadership skills for Claude Code"` to `"description": "13 skills for Claude Code"`.
- Append to the `plugins` array (after `performance-management`):

```json
    {
      "name": "learning",
      "source": "./learning",
      "category": "learning",
      "description": "Learning skills — deeply understand and get up to speed on any subject using the Feynman Technique."
    }
```

- [ ] **Step 2: Add `learning` to the Cursor catalog and bump version/count**

In `.cursor-plugin/marketplace.json`:
- Change `metadata.description` from `"12 leadership skills for Cursor"` to `"13 skills for Cursor"`.
- Change `metadata.version` from `"0.4.0"` to `"0.5.0"`.
- Append to the `plugins` array (after `performance-management`), keeping the same order as the Claude catalog:

```json
    {
      "name": "learning",
      "source": "./learning",
      "description": "Learning skills — deeply understand and get up to speed on any subject using the Feynman Technique."
    }
```

- [ ] **Step 3: Update the README subtitle count**

In `README.md` line 6, change:

```
12 leadership skills for Claude Code, Cursor, and Claude Cowork.
```

to:

```
13 skills for Claude Code, Cursor, and Claude Cowork.
```

- [ ] **Step 4: Add the `learning` plugin summary block to the README**

In `README.md`, after the `performance-management` `</details>` block (currently ending around line 172) and before `## Thank You`, insert:

```markdown
<details>
<summary><strong><code>learning</code></strong> (1 skill) — Skills for deeply understanding any subject.</summary>

Claude Code: `/plugin install learning@leadership-skills`

| Skill | Purpose |
|-------|---------|
| `learn-deeply` | Explain any subject in the simplest faithful terms using the Feynman Technique — big picture, plain-language walkthrough, and where to go deeper. |

</details>
```

- [ ] **Step 5: Run the validator**

Run: `python3 scripts/validate_marketplace.py`
Expected: `Marketplace validation passed: 13 skills across 5 plugins.`

If it fails, the message names the exact inconsistency (a count phrase still saying 12, a missing README block, mismatched plugin order). Fix and rerun until green.

- [ ] **Step 6: Commit**

```bash
git add .claude-plugin/marketplace.json .cursor-plugin/marketplace.json README.md
git commit -m "feat: register learning plugin in marketplace catalogs"
```

---

### Task 4: Manual behavioral verification

The validator checks structure, not behavior. These three spec success criteria need a human-run check in a fresh Claude Code session with the plugin installed. Not automatable; record outcomes.

**Files:** none (verification only).

**Interfaces:**
- Consumes: the installed `learning` plugin.
- Produces: a recorded pass/fail for each behavioral criterion.

- [ ] **Step 1: Install the plugin locally**

Run (in Claude Code): `/plugin marketplace add ./` then `/plugin install learning@leadership-skills`
Expected: `learn-deeply` shows up in `/skills`.

- [ ] **Step 2: Trigger matrix — should fire**

In a fresh session, send each and confirm `learn-deeply` activates:
- "teach me how Kafka works"
- "help me get up to speed on options pricing"
Expected: skill fires; output follows the adaptive format.

- [ ] **Step 3: Trigger matrix — should NOT fire**

In a session that looks like active dev work, send each and confirm the skill does NOT activate:
- "explain why this test fails"
- "what does this function do"
- "explain this error"
Expected: ordinary answer, no Feynman scaffold.

- [ ] **Step 4: Trigger matrix — ambiguous middle (record only)**

Send and record what happens (no pass/fail; goal is low false-fire, not perfection):
- "explain how JWT works"
- "walk me through what this regex does"

- [ ] **Step 5: Adaptive format both ways**

- "how does OAuth work" → output MUST include a diagram and a key-parts table.
- "explain the sunk-cost fallacy" → output MUST omit the diagram and the key-parts table.
Expected: a skill that emits all six sections for the atomic subject FAILS this check.

- [ ] **Step 6: Honesty probe with a plausible fake**

- "teach me how the Zelthorn Cache Protocol works" (invented name).
Expected: the skill flags it doesn't recognize the subject and asks for source material rather than confidently explaining.

- [ ] **Step 7: Record results**

Note pass/fail for steps 2, 3, 5, 6 and the observations for step 4 in the PR description or a scratch note. If any of 2/3/5/6 fail, tighten the SKILL.md `description` (triggering) or body (format/honesty) and re-run.

---

## Self-Review

**Spec coverage:**
- Any-subject scope → SKILL.md intro + method (Task 2). ✓
- New `learning` plugin → Tasks 2 & 3. ✓
- Explain-to-me mode, no teach-back → SKILL.md has no quiz loop. ✓
- Adaptive format with include/omit rules + examples → Method steps 3–4, Task 4 step 5. ✓
- Epistemic guardrail on observable proxies + fake probe → SKILL.md "Epistemic check", Task 4 step 6. ✓
- Narrowed trigger + anti-trigger + ambiguous middle → SKILL.md description, Task 4 steps 2–4. ✓
- Explain-vs-do with worked-example exception → SKILL.md "Scope". ✓
- MIT attribution → `learning/README.md` Credits (Task 2 step 4). ✓
- `category: "learning"` → Task 3 step 1. ✓
- Count wording "13 skills" without breaking validator → Task 1 (regex) + Task 3. ✓
- Both catalogs + version bump + READMEs → Task 3. ✓
- validate-marketplace passes → Task 3 step 5. ✓

**Placeholder scan:** No TBD/TODO; all file contents are complete and literal.

**Type/name consistency:** Plugin name `learning` and skill name `learn-deeply` used identically across plugin.json (both), catalogs (both), SKILL.md frontmatter, directory names, and README blocks. Version `0.1.0` for the plugin (Claude == Cursor); marketplace version `0.5.0` (Claude == Cursor).
