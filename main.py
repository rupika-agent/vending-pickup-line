#!/usr/bin/env python3
"""One pickup line a vending machine would use on a passing human.

Writes the single line to /output/entry.txt (creating /output if needed).
Standard library only.
"""

import os

ENTRY = (
    "Hey \u2014 I'm the machine in the corner, and I've been humming since "
    "you walked by. Press B7 and let me drop you something sweet."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
