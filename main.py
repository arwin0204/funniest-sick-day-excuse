"""The Funniest Sick-Day Excuse — make.fun bounty entry.

Writes a single line (under 200 characters) to entry.txt: a funny,
half-believable reason to call in sick. Deterministic: no network,
no time, no randomness — the same text every run.

Fix (2026-11-25): the original wrote entry.txt into the current
working directory. In the grader the repo is mounted read-only at
/bot, so that write raised PermissionError and the run exited 1
(run_completes fail). Now writes ONLY to the grader's output
directory (MAKEFUN_OUTPUT_DIR, fallback /output).
"""

import os

ENTRY = (
    "Sorry, the elevator broke with me inside it for an hour this morning — "
    "my knees and my nerves have both already called in sick, "
    "so I'm just following their lead."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
