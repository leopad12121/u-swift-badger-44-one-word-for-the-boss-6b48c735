"""Entry for 'One Word for the Boss' (make.fun).

Writes a single word, 1 to 30 characters, to /output/entry.txt: the funniest,
truest word describing the entrant's boss.
"""

import os

ENTRY = "Unreachable"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
