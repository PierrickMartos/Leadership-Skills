# Contributing

This repository is maintained by [@pierrickmartos](https://github.com/pierrickmartos).

## How to contribute
Contributions are welcome! Feel free to open a pull request if you'd like to suggest improvements, fix issues, or add new content.

## Working with Claude Code skills

This repo ships Claude Code skills that automate common workflows.

### Testing plugins locally

#### Using `--plugin-dir` (recommended)

Use the `--plugin-dir` flag to load plugins directly during development without requiring installation:

```bash
claude --plugin-dir ./communication
```

You can load multiple plugins at once:

```bash
claude --plugin-dir ./communication --plugin-dir ./decision-making
```

As you make changes, run `/reload-plugins` inside Claude Code to pick up updates without restarting. Then test your plugin components:

- Try your skills with `/plugin-name:skill-name`
- Check that agents appear in `/agents`
- Verify hooks work as expected

When a `--plugin-dir` plugin has the same name as an installed marketplace plugin, the local copy takes precedence for that session.

> See the [official documentation](https://code.claude.com/docs/en/plugins#test-your-plugins-locally) for more details.

#### Using `/link-for-testing`

Alternatively, run once after cloning to symlink all skills for local testing:

```
/link-for-testing
```

### Adding a new plugin

Use the `/add-plugin` skill to register a new plugin in the marketplace catalog and update the README:

```
/add-plugin <plugin-name>
```

This updates `.claude-plugin/marketplace.json`, `.cursor-plugin/marketplace.json` and the `## Plugins` table in `README.md`.

### Adding a skill or agent to an existing plugin

After creating a `SKILL.md` under `<plugin>/skills/<skill-name>/`, run the `/update-plugin` skill to update the plugin's README and bump its version:

```
/update-plugin
```

### Validating before committing

Before opening a PR, run the deterministic validator to check that all JSON is valid, required fields are present, local paths exist, skill frontmatter is correct, and README/catalog skill counts match the source files:

```bash
make validate
```

You can also invoke `/validate-marketplace` inside Claude Code; it runs the same check.

## Pull Request Guidelines

- **One change per PR** — keep PRs focused and easy to review.
- **Describe your changes** — explain what you changed and why in the PR description.
- **Open an issue first** for significant changes to discuss the approach before investing time.
- **Keep it concise** — prefer small, incremental improvements over large sweeping changes.
- **Be respectful** — follow a constructive and collaborative tone in all discussions.

## License

By contributing, you agree that your contributions will be licensed under the same license as this repository.
