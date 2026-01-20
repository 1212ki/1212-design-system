#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_SRC = ROOT / "1212-core.tokens.json"
DEFAULT_OUT_DIR = ROOT / "dist"

REQUIRED = {
    "color": [
        "background",
        "surface",
        "text",
        "subtext",
        "border",
        "primary",
        "accent",
    ],
    "typography": [
        "heading-1",
        "heading-2",
        "body-lg",
        "body",
        "body-sm",
    ],
    "spacing": ["4", "8", "12", "16", "20", "24", "32"],
    "radius": ["card", "button", "chip"],
    "shadow": ["card", "floating"],
}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=True, indent=2)
        f.write("\n")


def flatten_tokens(obj, prefix=""):
    if not isinstance(obj, dict):
        return
    for key, value in obj.items():
        if isinstance(value, dict) and "value" in value and "type" in value:
            yield f"{prefix}{key}", value
        elif isinstance(value, dict):
            yield from flatten_tokens(value, f"{prefix}{key}-")


def as_css_unit(value):
    if isinstance(value, (int, float)):
        return f"{value}px"
    if isinstance(value, str):
        stripped = value.strip()
        if stripped == "":
            return ""
        for suffix in ("px", "%", "rem", "em", "vh", "vw"):
            if stripped.endswith(suffix):
                return stripped
        try:
            float(stripped)
            return f"{stripped}px"
        except ValueError:
            return stripped
    return str(value)


def quote_font_family(value):
    if not isinstance(value, str):
        return str(value)
    if any(ch.isspace() for ch in value):
        return f'"{value}"'
    return value


def shadow_to_css(value):
    if isinstance(value, str):
        return value
    items = value
    if isinstance(value, dict):
        items = [value]
    if not isinstance(items, list):
        return str(value)
    parts = []
    for item in items:
        if not isinstance(item, dict):
            parts.append(str(item))
            continue
        x = as_css_unit(item.get("x", 0))
        y = as_css_unit(item.get("y", 0))
        blur = as_css_unit(item.get("blur", 0))
        spread = as_css_unit(item.get("spread", 0))
        color = item.get("color", "rgba(0, 0, 0, 0.2)")
        parts.append(f"{x} {y} {blur} {spread} {color}")
    return ", ".join(parts)


def build_css(tokens):
    global_tokens = tokens.get("global", {})
    lines = [":root {"]

    for name, token in flatten_tokens(global_tokens.get("color", {})):
        lines.append(f"  --color-{name}: {token['value']};")

    for name, token in flatten_tokens(global_tokens.get("spacing", {})):
        lines.append(f"  --space-{name}: {as_css_unit(token['value'])};")

    for name, token in flatten_tokens(global_tokens.get("radius", {})):
        lines.append(f"  --radius-{name}: {as_css_unit(token['value'])};")

    for name, token in flatten_tokens(global_tokens.get("shadow", {})):
        lines.append(f"  --shadow-{name}: {shadow_to_css(token['value'])};")

    for name, token in flatten_tokens(global_tokens.get("typography", {})):
        value = token.get("value", {})
        family = quote_font_family(value.get("fontFamily", ""))
        lines.append(f"  --text-{name}-font-family: {family};")
        lines.append(f"  --text-{name}-font-weight: {value.get('fontWeight', '')};")
        lines.append(
            f"  --text-{name}-font-size: {as_css_unit(value.get('fontSize', ''))};"
        )
        lines.append(
            f"  --text-{name}-line-height: {as_css_unit(value.get('lineHeight', ''))};"
        )
        lines.append(
            f"  --text-{name}-letter-spacing: {as_css_unit(value.get('letterSpacing', ''))};"
        )

    lines.append("}")
    return "\n".join(lines) + "\n"


def validate_tokens(tokens):
    errors = []
    if "global" not in tokens:
        errors.append("missing top-level 'global' token set")
        return errors

    global_tokens = tokens.get("global", {})
    for category, required in REQUIRED.items():
        group = global_tokens.get(category)
        if not isinstance(group, dict):
            errors.append(f"missing global.{category}")
            continue
        missing = [name for name in required if name not in group]
        for name in missing:
            errors.append(f"missing global.{category}.{name}")

    return errors


def build(args):
    src_path = Path(args.src).resolve()
    out_dir = Path(args.out_dir).resolve()
    tokens = load_json(src_path)

    if not args.no_validate:
        errors = validate_tokens(tokens)
        if errors:
            for err in errors:
                print(f"error: {err}", file=sys.stderr)
            return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    out_json = out_dir / src_path.name
    write_json(out_json, tokens)

    if not args.no_css:
        css = build_css(tokens)
        out_css = out_dir / src_path.name.replace(".json", ".css")
        out_css.write_text(css, encoding="utf-8")

    return 0


def validate(args):
    src_path = Path(args.src).resolve()
    tokens = load_json(src_path)
    errors = validate_tokens(tokens)
    if errors:
        for err in errors:
            print(f"error: {err}", file=sys.stderr)
        return 1
    print("ok")
    return 0


def parse_args():
    parser = argparse.ArgumentParser(description="Design token builder")
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build", help="build outputs")
    build_parser.add_argument("--src", default=str(DEFAULT_SRC))
    build_parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    build_parser.add_argument("--no-css", action="store_true")
    build_parser.add_argument("--no-validate", action="store_true")

    validate_parser = subparsers.add_parser("validate", help="validate tokens")
    validate_parser.add_argument("--src", default=str(DEFAULT_SRC))

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "build":
        return build(args)
    if args.command == "validate":
        return validate(args)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
