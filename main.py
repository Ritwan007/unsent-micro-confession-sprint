#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt.
Python standard library only; no input, no network.
"""
import os

ENTRY = (
    "To: Grandma\n"
    "i kept your last voicemail for two years and i still can't listen past the part where you say my name"
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
