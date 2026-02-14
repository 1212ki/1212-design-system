# AGENTS.md

Read README.md first.

## Local rules
- Keep token sources in this repo as the source of truth.
  - core: `1212-core.tokens.json`
  - music activity: `1212-music.tokens.json`
- Use `python3 design-builder.py build` (and `--src` when needed) to update generated outputs.
- Avoid network calls and external dependencies.
