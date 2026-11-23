#!/usr/bin/env python3
"""One Emoji, One Smile.

Writes exactly one emoji to /output/entry.txt: heart hands, chosen to
make a stranger smile. Deterministic: no input, no network, no secrets.
"""

import os

EMOJI = "\U0001FAF6"  # 🫶 Heart Hands


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
