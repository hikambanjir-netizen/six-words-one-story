#!/usr/bin/env python3
"""Six Words, One Story — make.fun bounty entry.

Writes one complete six-word story to /output/entry.txt.
Pure standard library; no network, no input, fully deterministic.
"""

import os

STORY = "The letter arrived after the funeral."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    # The gate allows 1-60 characters of UTF-8 text; the story is 37.
    assert 1 <= len(STORY.encode("utf-8")) <= 60, "story out of gate range"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        # No trailing newline: the file holds exactly the six words.
        handle.write(STORY)


if __name__ == "__main__":
    main()
