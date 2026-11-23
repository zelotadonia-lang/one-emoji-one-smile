#!/usr/bin/env python3
"""One Emoji, One Smile.

Writes exactly one emoji to /output/entry.txt: heart hands, chosen to
make a stranger smile. Two hands forming a heart reads as warm at first
glance, needs no context, and stays friendly coming from a stranger.

Deterministic: no input, no network, no secrets. After writing, the
program reads the file back and refuses to finish unless it holds
exactly one non-whitespace character, so a bad write can never pass
as a valid entry.
"""

import os
import sys

EMOJI = "\U0001FAF6"  # 🫶 Heart Hands
OUTPUT = "/output/entry.txt"


def main(path=OUTPUT):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if len(written) != 1 or written.isspace():
        raise SystemExit("entry must be exactly one emoji, got %r" % written)
    print("wrote %s to %s" % (written, path))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else OUTPUT)
