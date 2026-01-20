# CLAUDE.md

## Tool intent
- Manage design tokens as the single source of truth.
- Sync tokens into Figma via Tokens Studio (manual import/export).

## Operating rules
- Edit the source tokens at `1212-core.tokens.json`.
- Regenerate outputs with `python3 design-builder.py build` after changes.
- Do not edit `dist/` by hand.
- Keep token sets ordered in `$metadata.tokenSetOrder`.
