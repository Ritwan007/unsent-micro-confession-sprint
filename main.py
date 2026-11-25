#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt.
Python standard library only; no input, no network.
"""
import os

TO_LINE = "To: Grandma"
MESSAGE = (
    "i kept your last voicemail for two years and i still can't listen "
    "past the part where you say my name"
)

ENTRY = TO_LINE + "\n" + MESSAGE

# Competition gate limits: total 1-260 chars, message line at most 200 chars,
# exactly two lines, first line a "To:" addressee. Fail loudly instead of
# writing an entry that would be rejected.
assert 1 <= len(ENTRY) <= 260, "entry outside 1-260 char gate"
assert len(MESSAGE) <= 200, "message line exceeds 200 chars"
assert ENTRY.count("\n") == 1, "entry must be exactly two lines"
assert TO_LINE.startswith("To: "), "first line must address the recipient"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
