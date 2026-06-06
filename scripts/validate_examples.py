#!/usr/bin/env python3
"""
Validate Royalty OS v0.4 example YAML files against JSON Schema files.

Required packages:
pip install pyyaml jsonschema

Usage:
python scripts/validate_examples.py
"""

import json
import sys
from pathlib import Path

# -----------------------------
# Dependency checks
# -----------------------------
try:
    import yaml
except ImportError as exc:
    print("Missing dependency: PyYAML")
    print("Install with: pip install pyyaml")
    raise SystemExit(1) from exc

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError
except ImportError as exc:
    print("Missing dependency: jsonschema")
    print("Install with: pip install jsonschema")
    raise SystemExit(1) from exc

# -----------------------------
# Paths
# -----------------------------
REPO_ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Multi-Layer Value Graph Example",
        "example": REPO_ROOT / "examples" / "multi-layer-value-graph.example.yaml",
        "schema": REPO_ROOT / "schemas" / "value-graph-v2.schema.json",
    },
    {
        "name": "Policy Module Example",
        "example": REPO_ROOT / "examples" / "policy-module.example.yaml",
        "schema": REPO_ROOT / "schemas" / "policy-module.schema.json",
    },
]

# -----------------------------
# Loaders
# -----------------------------
def load_yaml(path: Path):
    """Load a YAML file and return its parsed content."""
    try:
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise RuntimeError(f"File not found: {path}") from None
    except yaml.YAMLError as exc:
        raise RuntimeError(f"Invalid YAML in {path}: {exc}") from exc


def load_json(path: Path):
    """Load a JSON file and return its parsed content."""
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise RuntimeError(f"File not found: {path}") from None
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc

# -----------------------------
# Error path formatter
# -----------------------------
def format_error_path(error) -> str:
    """Return a readable JSON path for a validation error."""
    if not error.absolute_path:
        return "$"

    parts = ["$"]
    for part in error.absolute_path:
        if isinstance(part, int):
            parts.append(f"[{part}]")
        else:
            parts.append(f".{part}")

    return "".join(parts)

# -----------------------------
# Validator
# -----------------------------
def validate_target(name: str, example_path: Path, schema_path: Path) -> bool:
    """Validate one YAML example against one JSON Schema."""
    print(f"Validating target: {name}")
    print(f"Example: {example_path.relative_to(REPO_ROOT)}")
    print(f"Schema:  {schema_path.relative_to(REPO_ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    # Validate schema itself
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise RuntimeError(f"Invalid JSON Schema in {schema_path}: {exc.message}") from exc

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(example),
        key=lambda err: list(err.absolute_path),
    )

    if errors:
        print("\nValidation failed.")
        for error in errors:
            print(f"- Path: {format_error_path(error)}")
            print(f"  Error: {error.message}")
        print("")
        return False

    print("Validation passed.\n")
    return True

# -----------------------------
# Main
# -----------------------------
def main() -> int:
    """Run all validation targets."""
    all_passed = True

    for target in VALIDATION_TARGETS:
        try:
            passed = validate_target(
                name=target["name"],
                example_path=target["example"],
                schema_path=target["schema"],
            )
            all_passed = all_passed and passed
        except RuntimeError as exc:
            print("\nValidation failed.")
            print(exc)
            print("")
            all_passed = False

    if not all_passed:
        return 1

    print("All examples passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

