#!/usr/bin/env python3
"""Deterministic marketplace validation for leadership-skills."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAUDE_MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CURSOR_MARKETPLACE = ROOT / ".cursor-plugin" / "marketplace.json"
README = ROOT / "README.md"


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        errors.append(f"Missing file: {rel(path)}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {rel(path)}: {exc}")
    return {}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def require_mapping(data: dict, keys: list[str], label: str, errors: list[str]) -> None:
    for key in keys:
        if key not in data:
            errors.append(f"{label} is missing required field: {key}")


def local_source_path(source: str) -> Path | None:
    if source.startswith("./"):
        return ROOT / source[2:]
    return None


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text()
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append(f"{rel(path)} is missing YAML frontmatter")
        return {}

    frontmatter = match.group(1)
    values: dict[str, str] = {}
    for key in ("name", "description"):
        key_match = re.search(rf"^{key}:\s*(.*)$", frontmatter, re.MULTILINE)
        if not key_match:
            errors.append(f"{rel(path)} frontmatter is missing `{key}`")
            continue
        value = key_match.group(1).strip()
        if value in {"", ">"}:
            value = "multiline"
        values[key] = value
    return values


def marketplace_skills(plugin_dir: Path) -> list[Path]:
    return sorted((plugin_dir / "skills").glob("*/SKILL.md"))


def validate_marketplaces(errors: list[str]) -> tuple[dict, dict]:
    claude = load_json(CLAUDE_MARKETPLACE, errors)
    cursor = load_json(CURSOR_MARKETPLACE, errors)

    require_mapping(claude, ["name", "owner", "plugins"], ".claude-plugin/marketplace.json", errors)
    require_mapping(cursor, ["name", "owner", "metadata", "plugins"], ".cursor-plugin/marketplace.json", errors)

    claude_plugins = claude.get("plugins", [])
    cursor_plugins = cursor.get("plugins", [])

    if not isinstance(claude_plugins, list):
        errors.append(".claude-plugin/marketplace.json `plugins` must be an array")
        claude_plugins = []
    if not isinstance(cursor_plugins, list):
        errors.append(".cursor-plugin/marketplace.json `plugins` must be an array")
        cursor_plugins = []

    claude_names = [p.get("name") for p in claude_plugins if isinstance(p, dict)]
    cursor_names = [p.get("name") for p in cursor_plugins if isinstance(p, dict)]
    if claude_names != cursor_names:
        errors.append(f"Claude and Cursor plugin order/names differ: {claude_names} != {cursor_names}")

    for catalog_name, plugins in (
        (".claude-plugin/marketplace.json", claude_plugins),
        (".cursor-plugin/marketplace.json", cursor_plugins),
    ):
        for index, plugin in enumerate(plugins):
            if not isinstance(plugin, dict):
                errors.append(f"{catalog_name} plugins[{index}] must be an object")
                continue
            require_mapping(plugin, ["name", "source"], f"{catalog_name} plugin {index}", errors)
            source = plugin.get("source")
            if isinstance(source, str):
                path = local_source_path(source)
                if path and not path.is_dir():
                    errors.append(f"{catalog_name} local source does not exist: {source}")

    return claude, cursor


def validate_plugins(claude: dict, cursor: dict, errors: list[str]) -> list[Path]:
    skill_files: list[Path] = []
    cursor_by_name = {
        plugin.get("name"): plugin
        for plugin in cursor.get("plugins", [])
        if isinstance(plugin, dict)
    }

    for plugin in claude.get("plugins", []):
        if not isinstance(plugin, dict):
            continue
        name = plugin.get("name")
        source = plugin.get("source")
        if not isinstance(name, str) or not isinstance(source, str):
            continue

        plugin_dir = local_source_path(source)
        if plugin_dir is None or not plugin_dir.is_dir():
            continue

        cursor_plugin = cursor_by_name.get(name)
        if cursor_plugin and cursor_plugin.get("source") != source:
            errors.append(f"Cursor source for plugin `{name}` differs from Claude source")

        claude_meta = load_json(plugin_dir / ".claude-plugin" / "plugin.json", errors)
        cursor_meta = load_json(plugin_dir / ".cursor-plugin" / "plugin.json", errors)
        require_mapping(
            claude_meta,
            ["name", "version", "description", "keywords", "license", "author"],
            f"{rel(plugin_dir / '.claude-plugin' / 'plugin.json')}",
            errors,
        )
        require_mapping(
            cursor_meta,
            ["name", "displayName", "version", "description", "author", "license"],
            f"{rel(plugin_dir / '.cursor-plugin' / 'plugin.json')}",
            errors,
        )

        for meta_name, meta in (("Claude", claude_meta), ("Cursor", cursor_meta)):
            if meta.get("name") != name:
                errors.append(f"{meta_name} plugin metadata name for `{name}` is `{meta.get('name')}`")

        if claude_meta.get("version") != cursor_meta.get("version"):
            errors.append(f"Plugin `{name}` has mismatched Claude/Cursor versions")

        for skill_path in marketplace_skills(plugin_dir):
            skill_files.append(skill_path)
            skill_dir = skill_path.parent.name
            frontmatter = parse_frontmatter(skill_path, errors)
            if frontmatter.get("name") != skill_dir:
                errors.append(
                    f"{rel(skill_path)} frontmatter name `{frontmatter.get('name')}` "
                    f"does not match directory `{skill_dir}`"
                )

        for agent_path in sorted((plugin_dir / "agents").glob("*.md")):
            parse_frontmatter(agent_path, errors)

    return sorted(skill_files)


def validate_counts(claude: dict, cursor: dict, skill_files: list[Path], errors: list[str]) -> None:
    count = len(skill_files)
    count_pattern = re.compile(r"(\d+)\s+leadership skills")

    locations = [
        (".claude-plugin/marketplace.json description", claude.get("description", "")),
        (".cursor-plugin/marketplace.json metadata.description", cursor.get("metadata", {}).get("description", "")),
    ]
    if README.exists():
        locations.append(("README.md subtitle", README.read_text()))

    for label, text in locations:
        match = count_pattern.search(str(text))
        if not match:
            errors.append(f"{label} does not contain a leadership skill count")
        elif int(match.group(1)) != count:
            errors.append(f"{label} says {match.group(1)} skills, actual count is {count}")


def validate_readmes(claude: dict, skill_files: list[Path], errors: list[str]) -> None:
    if not README.exists():
        errors.append("Missing README.md")
        return

    top_readme = README.read_text()
    for plugin in claude.get("plugins", []):
        if not isinstance(plugin, dict):
            continue
        name = plugin.get("name")
        source = plugin.get("source")
        if not isinstance(name, str) or not isinstance(source, str):
            continue
        plugin_dir = local_source_path(source)
        if plugin_dir is None or not plugin_dir.is_dir():
            continue

        skills = marketplace_skills(plugin_dir)
        skill_names = [path.parent.name for path in skills]

        summary_pattern = re.compile(
            rf"<summary><strong><code>{re.escape(name)}</code></strong> \((\d+) skills?\)",
            re.MULTILINE,
        )
        summary_match = summary_pattern.search(top_readme)
        if not summary_match:
            errors.append(f"README.md is missing plugin summary for `{name}`")
        elif int(summary_match.group(1)) != len(skills):
            errors.append(
                f"README.md plugin summary for `{name}` says {summary_match.group(1)} skills, "
                f"actual count is {len(skills)}"
            )

        plugin_readme = plugin_dir / "README.md"
        if not plugin_readme.exists():
            errors.append(f"Missing plugin README: {rel(plugin_readme)}")
            continue
        plugin_text = plugin_readme.read_text()
        skills_section_match = re.search(r"^## Skills\n(.*?)(?:\n## |\Z)", plugin_text, re.DOTALL | re.MULTILINE)
        if not skills_section_match:
            errors.append(f"{rel(plugin_readme)} is missing a `## Skills` section")
        else:
            skill_rows = [
                line
                for line in skills_section_match.group(1).splitlines()
                if line.startswith("|")
                and not re.match(r"^\|\s*-+", line)
                and "Skill" not in line.split("|")[1]
            ]
            if len(skill_rows) != len(skills):
                errors.append(
                    f"{rel(plugin_readme)} lists {len(skill_rows)} skill rows, "
                    f"actual count is {len(skills)}"
                )
        for skill_name in skill_names:
            if skill_name not in plugin_text:
                errors.append(f"{rel(plugin_readme)} does not list skill `{skill_name}`")
            if f"`{skill_name}`" not in top_readme:
                errors.append(f"README.md does not list skill `{skill_name}`")

    inventory_count = len(skill_files)
    if inventory_count == 0:
        errors.append("No marketplace skills found")


def main() -> int:
    errors: list[str] = []
    claude, cursor = validate_marketplaces(errors)
    skill_files = validate_plugins(claude, cursor, errors)
    validate_counts(claude, cursor, skill_files, errors)
    validate_readmes(claude, skill_files, errors)

    if errors:
        print("Marketplace validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Marketplace validation passed: {len(skill_files)} skills across {len(claude.get('plugins', []))} plugins.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
