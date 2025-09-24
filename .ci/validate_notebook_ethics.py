#!/usr/bin/env python3
"""Ensure notebooks start with protected ethical reminder."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_PHRASE = "Ethical Reminder"


def validate_notebook(path: Path) -> list[str]:
    issues: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - defensive
        issues.append(f"{path}: failed to load JSON ({exc})")
        return issues

    cells = data.get("cells", [])
    if not cells:
        issues.append(f"{path}: notebook has no cells")
        return issues

    first = cells[0]
    if first.get("cell_type") != "markdown":
        issues.append(f"{path}: first cell must be markdown")
    source = "".join(first.get("source", []))
    if REQUIRED_PHRASE not in source:
        issues.append(f"{path}: first cell must contain '{REQUIRED_PHRASE}'")

    metadata = first.get("metadata", {})
    editable = metadata.get("editable")
    deletable = metadata.get("deletable")
    if editable not in (False, "false", "False"):
        issues.append(f"{path}: first cell metadata 'editable' must be false")
    if deletable not in (False, "false", "False"):
        issues.append(f"{path}: first cell metadata 'deletable' must be false")

    return issues


def main() -> int:
    notebooks_dir = Path("notebooks")
    if not notebooks_dir.exists():
        return 0

    problems: list[str] = []
    for nb_path in sorted(notebooks_dir.rglob("*.ipynb")):
        problems.extend(validate_notebook(nb_path))

    if problems:
        print("Notebook ethical header validation failed:", file=sys.stderr)
        for problem in problems:
            print(f" - {problem}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
