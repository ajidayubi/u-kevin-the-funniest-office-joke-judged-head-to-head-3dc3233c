#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

The joke is a single line. Setup: telling the calendar you are busy.
Turn: the calendar answers by booking a meeting to ask why — the tool
meant to guard your time does the opposite. Punchline last. It turns on
something anyone who has worked in an office knows (the calendar that
fills itself), and the twist is one the reader does not see coming.
"""
import os

JOKE = "I told my calendar I was busy, so it booked a meeting to discuss why."

ENTRY = JOKE


def main():
    # Gate self-check: 1-200 chars, not only whitespace, exactly one line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
