"""Print line, word, and character counts for a UTF-8 text file."""

import argparse
import json
from pathlib import Path


def calculate_stats(text: str) -> dict[str, int]:
    """Return counts for lines, whitespace-delimited words, and characters."""
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


def read_text_file(path: Path) -> str:
    """Read a UTF-8 text file while preserving newline characters."""
    with path.open(encoding="utf-8", newline="") as text_file:
        return text_file.read()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print JSON text statistics for a UTF-8 text file."
    )
    parser.add_argument("file", type=Path, help="path to the text file")
    args = parser.parse_args()

    print(json.dumps(calculate_stats(read_text_file(args.file))))


if __name__ == "__main__":
    main()
