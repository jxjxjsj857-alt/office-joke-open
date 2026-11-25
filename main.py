#!/usr/bin/env python3
"""Office joke entry for make.fun's "Make the AI Judge Laugh: the Office
Joke Open" bounty. Writes one single-line office joke (116 characters) to
/output/entry.txt. Python 3, no dependencies, no network, deterministic."""

import os

# The joke: a performance review's "be more visible" taken literally, with
# the payoff landing in the last few words ("my soul off"). One line, under
# 200 characters, specific office detail (review, camera-on meetings).
JOKE = (
    "My performance review said I need to be more visible, "
    "so now I join every meeting with my camera on and my soul off."
)

# Length guard: the bounty requires one line of 1-200 characters.
# Fail loudly instead of writing an out-of-spec entry.
MAX_JOKE_LENGTH = 200
if len(JOKE) < 1 or len(JOKE) > MAX_JOKE_LENGTH or "\n" in JOKE or "\r" in JOKE:
    raise SystemExit(
        f"Joke must be a single line of 1-{MAX_JOKE_LENGTH} characters, "
        f"got {len(JOKE)} characters."
    )

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)

print(f"Wrote {len(JOKE)}-character joke to /output/entry.txt")
