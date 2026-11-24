#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — entry generator.

Writes a single-sentence pitch for the worst, most useless app idea
imaginable to /output/entry.txt, with no trailing newline.

Standard library only. No network access.
"""

import os

SENTENCE = (
    "Sniffly is an AI-powered app that analyzes the sound of your farts, "
    "assigns each one a rarity score, and lets strangers bid on your "
    "rarest toots."
)


def validate(sentence):
    """Check the pitch against the bounty rules."""
    if not 1 <= len(sentence) <= 240:
        raise ValueError(
            "sentence must be 1-240 characters, got %d" % len(sentence)
        )
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if sentence.endswith("\n"):
        raise ValueError("entry must not end with a newline")
    return sentence


def main():
    validate(SENTENCE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
