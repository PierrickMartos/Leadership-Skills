CLAUDE_MARKETPLACE := .claude-plugin/marketplace.json
CURSOR_MARKETPLACE := .cursor-plugin/marketplace.json
CURRENT_VERSION := $(shell python3 -c "import json; print(json.load(open('$(CLAUDE_MARKETPLACE)'))['version'])")

.PHONY: version validate patch minor major release

version:
	@echo "Current version: $(CURRENT_VERSION)"

validate:
	python3 scripts/validate_marketplace.py

patch:
	@$(MAKE) _bump PART=patch

minor:
	@$(MAKE) _bump PART=minor

major:
	@$(MAKE) _bump PART=major

define bump_version
$(shell python3 -c "\
v = '$(1)'.split('.'); \
i = {'major': 0, 'minor': 1, 'patch': 2}['$(2)']; \
v[i] = str(int(v[i]) + 1); \
v[i+1:] = ['0'] * (2 - i); \
print('.'.join(v))")
endef

define set_json_version
python3 -c "\
import json, pathlib; \
p = pathlib.Path('$(1)'); \
d = json.loads(p.read_text()); \
$(2) = '$(3)'; \
p.write_text(json.dumps(d, indent=2) + '\n')"
endef

_bump:
	$(eval NEW := $(call bump_version,$(CURRENT_VERSION),$(PART)))
	@$(call set_json_version,$(CLAUDE_MARKETPLACE),d['version'],$(NEW))
	@$(call set_json_version,$(CURSOR_MARKETPLACE),d['metadata']['version'],$(NEW))
	@echo "Bumped $(CURRENT_VERSION) → $(NEW)"
	git add $(CLAUDE_MARKETPLACE) $(CURSOR_MARKETPLACE)
	git commit -m "chore: bump version to $(NEW)"
	git tag "v$(NEW)"
	@echo "Run 'make release' to push and publish v$(NEW)"

release:
	git push
	git push --tags
	gh release create "v$(CURRENT_VERSION)" --generate-notes --title "v$(CURRENT_VERSION)"
	@echo "Released v$(CURRENT_VERSION)"
