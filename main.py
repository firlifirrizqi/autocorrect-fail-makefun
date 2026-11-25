"""Funniest Autocorrect Fail — entry writer.

Writes one original autocorrect-fail line to /output/entry.txt
and nothing else. Standard library only.
"""

import os

ENTRY = "Dinner's ready, I made pastor with garlic bread, come home hungry!"

assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"


WORD_COUNT = 11


def check_length() -> None:
    """Under-200-char guard: the entry must be 1-199 characters."""
    assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"


def check_word_count() -> None:
    """Word-count check: the entry must have exactly WORD_COUNT words."""
    assert len(ENTRY.split()) == WORD_COUNT, "entry word count mismatch"


def verify_written(path: str) -> None:
    """Read-back check: the file must contain exactly the entry line."""
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the entry exactly"


def check_single_line() -> None:
    """Single-line guard: the entry must be one line, no newlines."""
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"


def main() -> None:
    check_length()
    check_word_count()
    check_single_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: the file must contain exactly the entry.
    verify_written("/output/entry.txt")


if __name__ == "__main__":
    main()
