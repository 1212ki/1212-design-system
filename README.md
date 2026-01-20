# design-builder

CLI helper to manage design tokens for Tokens Studio (Figma plugin) sync.
This tool does not talk to Figma directly; it generates token files to import.

## Quick start
1. Edit the token source:
   - 1212-core.tokens.json
2. Build outputs:
   - python3 design-builder.py build
3. Import into Figma:
   - Open the file in Figma
   - Open Tokens Studio
   - Import JSON (dist/1212-core.tokens.json)
   - Apply tokens to create Styles/Variables

## Outputs
- dist/1212-core.tokens.json (normalized copy)
- dist/1212-core.tokens.css (CSS variables for UI Builder)

## Notes
- The source file already matches Tokens Studio format, so you can import it
  directly if you do not need CSS output.
- Keep tokens in the `global` set unless a new theme is introduced.
