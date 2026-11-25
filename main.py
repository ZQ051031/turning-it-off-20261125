"""Have You Tried Turning It Off? — make.fun micro entry.

Writes one funny line from a hopeless tech support agent to a
desperate customer to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "Have you tried turning it off and on again? Please say yes, "
    "it's the last line on my script, and after that we're both on our own."
)


def main() -> None:
    # The gate requires 1-199 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 199, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
