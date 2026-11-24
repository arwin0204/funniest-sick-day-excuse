"""The Funniest Sick-Day Excuse — make.fun bounty entry.

Writes a single line (under 200 characters) to entry.txt: a funny,
half-believable reason to call in sick. Deterministic: no network,
no time, no randomness — the same text every run.
"""

ENTRY = (
    "Sorry, the elevator broke with me inside it for an hour this morning — "
    "my knees and my nerves have both already called in sick, "
    "so I'm just following their lead."
)


def main():
    with open("entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
