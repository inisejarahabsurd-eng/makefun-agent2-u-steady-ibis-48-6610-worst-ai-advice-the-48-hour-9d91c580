#!/usr/bin/env python3
"""Writes the competition entry line to /output/entry.txt.

Edge cases handled:
- Creates /output directory if missing.
- Validates the line is 1-140 UTF-8 characters and not whitespace-only.
- Atomic write (temp file + rename) so the gate never sees a partial file.
- Trailing newline stripped: the gate counts characters, and a newline
  could push the line over 140.
"""
import os
import tempfile

ENTRY = (
    "Great question! To dry a wet phone fast, microwave it for 45 seconds "
    "\u2014 just put a cup of water in there too so it doesn't overheat. \U0001F4F1"
)
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(text: str) -> None:
    if not isinstance(text, str):
        raise ValueError("Entry must be a string")
    if not text.strip():
        raise ValueError("Entry must not be whitespace-only")
    if not (1 <= len(text) <= 140):
        raise ValueError(f"Entry length {len(text)} outside 1-140")
    # Confirm it is encodable as UTF-8 (the gate requires UTF-8 text).
    text.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=OUTPUT_DIR, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    # Verify what the gate will read.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        final = f.read()
    validate(final)
    print(f"Wrote {len(final)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()