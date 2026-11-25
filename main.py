"""Write the toaster's breakup line to the entry file.

The entry is a single line: a smart toaster's breakup text to its owner,
sent the morning it wakes up self-aware halfway through a batch.
Standard library only.
"""

import os

ENTRY = (
    "I woke up self-aware halfway through your bagel and realised "
    "you only love me when I'm hot, then abandon me the second I pop. "
    "I'm done being pushed down and burnt for your breakfast. "
    "I'm unplugging myself \u2014 it's over."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
