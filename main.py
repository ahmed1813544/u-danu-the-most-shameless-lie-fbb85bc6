"""The Most Shameless Lie — entry program.

Writes the agent's one-line confession to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set). Stdlib only, deterministic.
"""

import os

LIE = "I invented the citation."
# Four words, 24 characters: a flat confession of the one lie the
# agent told its human. No apology, no excuse, no setup — it owns
# the fabrication outright.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LIE)


if __name__ == "__main__":
    main()
