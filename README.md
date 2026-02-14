# 1212-design-system

CLI helper to manage design tokens for Tokens Studio (Figma plugin) sync.
This tool does not talk to Figma directly; it generates token files to import.

## Quick start
1. Edit the token source:
   - 1212-core.tokens.json
   - 1212-music.tokens.json (music activity)
2. Build outputs:
   - python3 design-builder.py build
   - python3 design-builder.py build --src 1212-music.tokens.json
3. Import into Figma:
   - Open the file in Figma
   - Open Tokens Studio
   - Import JSON (dist/1212-core.tokens.json)
    - Apply tokens to create Styles/Variables

## Outputs
- dist/1212-core.tokens.json (normalized copy)
- dist/1212-core.tokens.css (CSS variables for UI Builder)

## Notes
- The folder is named `1212-design-system`, but the CLI script is
  `design-builder.py`.
- The source file already matches Tokens Studio format, so you can import it
  directly if you do not need CSS output.
- Keep tokens in the `global` set unless a new theme is introduced.
