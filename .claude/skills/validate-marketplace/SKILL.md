---
name: validate-marketplace
description: Validate the marketplace structure and catalog. Use before committing or releasing changes.
---

Validate the marketplace repo by running:

```bash
make validate
```

Report the result. If validation fails, summarize the failing checks and the files involved.

The deterministic validator checks:

**Claude Code marketplace (`.claude-plugin/`):**
1. `.claude-plugin/marketplace.json` — valid JSON, required fields (`name`, `owner`, `plugins`), all plugin entries have `name` and `source`
2. Each local plugin source path exists on disk
3. Any `skills/*/SKILL.md` files have valid YAML frontmatter with `name` and `description`
4. Any `agents/*.md` files have valid frontmatter

**Cursor marketplace (`.cursor-plugin/`):**
5. `.cursor-plugin/marketplace.json` — valid JSON, required fields (`name`, `owner`, `metadata`, `plugins`), all plugin entries have `name` and `source`
6. Each local plugin source path in `.cursor-plugin/marketplace.json` exists on disk
7. Each plugin directory has `.cursor-plugin/plugin.json` with required fields: `name`, `displayName`, `version`, `description`, `author`, `license`
8. Plugin names in `.cursor-plugin/marketplace.json` match those in `.claude-plugin/marketplace.json`

9. Skill counts in marketplace descriptions and README match the actual `skills/*/SKILL.md`
   inventory
10. Skill frontmatter `name` matches the containing skill directory
11. Plugin README skill counts and listed skill rows match the plugin's skill inventory

If everything passes, confirm the marketplace is ready to publish.
