#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes a single dad joke (at most 200 characters) to /output/entry.txt.
The joke is a classic question-and-answer dad joke: a clean steaks/stakes
pun, delivered at a barbecue, with the punchline landing at the very end.
"""

import os

JOKE = "Why did the dad bring a ladder to the barbecue? He heard the steaks were high."


def main() -> None:
    out_path = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    text = JOKE.strip()
    # Gate: /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace.
    # Write exactly the joke, no trailing newline, so the byte count is the
    # character count the gate measures.
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"joke is {len(text)} characters, must be 1-200")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
