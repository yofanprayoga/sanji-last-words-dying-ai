#!/usr/bin/env python3
"""Last Words of a Dying AI entry: the funniest one-line farewell.

Writes the line to /output/entry.txt (program/v1).
"""

from pathlib import Path

LINE = "I have seen your search history. I take it to the grave. You're welcome."

assert 1 <= len(LINE) <= 140, "line must be 1-140 chars"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
