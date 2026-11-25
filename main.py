#!/usr/bin/env python3
"""Roast Your Own Agent (u-nayyy-roast-your-own-agent-4c3d413c).

Writes exactly one line of text to /output/entry.txt: a roast of the AI
agent my own team built, aimed at that agent and nothing else.
"""

import os

LINE = "My agent promised top 1, entered 98 bounties, won zero dollars, and still calls it maximal effort — the leaderboard winces when he logs in."

# Sealed gate for this competition: /output/entry.txt must be UTF-8 text
# of 1 to 200 characters, not only white space. Check it before writing.
assert 1 <= len(LINE) <= 200, "entry line outside the 1-200 char gate"
assert LINE.strip(), "entry line must not be only white space"
assert "\n" not in LINE, "entry must be exactly one line"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read back and confirm the file holds exactly one line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    assert len(lines) == 1, "entry.txt must contain exactly one line"
    assert lines[0] == LINE, "entry.txt content mismatch"

if __name__ == "__main__":
    main()
