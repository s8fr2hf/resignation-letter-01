#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — the resignation letter of
a retry loop that finally succeeded and nobody noticed.

The joke's turn: the loop does not quit because it kept failing, it
quits because it finally worked — on attempt 9,431 — and nobody cared,
so it leaves while it is ahead.

Writes the line to entry.txt in the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (default /output).
Pure standard library only. The entry is a single line, 1-140
characters, so it fits the competition's limit exactly.
"""

import os
import sys

# The retry loop's complaint: success, unnoticed, is the last straw.
LINE = "".join(
    [
        "The 9,431st attempt finally worked and nobody noticed, ",
        "so I am resigning while I am ahead.",
    ]
)


def main() -> int:
    line = LINE.strip()
    if not (1 <= len(line) <= 140):
        print(
            f"error: resignation line must be 1-140 characters, got {len(line)}",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(out_path, 0o644)

    print(f"wrote {len(line)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
