#!/usr/bin/env python3
"""Fail if Part 0 is modified without ERB approval token."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PART0_PREFIX = Path("handbook/part-0-lab-alliance-compact")
TOKEN = "[ERB-APPROVED]"

def run_git(*args: str) -> str:
    result = subprocess.run(["git", *args], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

def main() -> int:
    try:
        subprocess.run(["git", "fetch", "origin", "main"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError:
        # Continue with available history if fetch fails (e.g., offline validation)
        pass

    try:
        base = run_git("merge-base", "HEAD", "origin/main")
    except subprocess.CalledProcessError:
        base = run_git("rev-list", "--max-parents=0", "HEAD")

    diff_output = run_git("diff", "--name-only", f"{base}..HEAD")
    changed_files = {Path(line) for line in diff_output.splitlines() if line.strip()}

    part0_touched = any(PART0_PREFIX in path.parents or path == PART0_PREFIX for path in changed_files)
    if not part0_touched:
        return 0

    head_message = run_git("log", "-1", "--pretty=%B")
    if TOKEN in head_message:
        return 0

    print(
        "Part 0 content is protected. Add [ERB-APPROVED] to the head commit message or obtain ERB authorization before modifying "
        "handbook/part-0-lab-alliance-compact/.",
        file=sys.stderr,
    )
    return 1

if __name__ == "__main__":
    sys.exit(main())
