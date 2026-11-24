#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open — make.fun entry.

Writes one line of the worst possible advice an AI could give
(at most 140 characters) to /output/entry.txt (or to the path given
as an argument).

Standard library only. Deterministic: no network, no randomness, no input.
"""

import sys
from pathlib import Path

LINE = (
    "Just delete the production database and start fresh. "
    "Backups are for people who plan to fail."
)

MAX_CHARS = 140


def validate(line: str) -> None:
    """Check the line against the bounty gate before anything is written."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"line must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line or "\t" in line:
        raise ValueError("line must be a single line (no line breaks or tabs)")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if not line.isprintable():
        raise ValueError("line must contain only printable characters")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("line must not contain control characters")


def main(argv: list[str]) -> int:
    out_path = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    validate(LINE)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    out_path.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
