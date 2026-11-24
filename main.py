"""One-sentence absurd invention pitch: The Sock Tribunal."""

import os
import sys


def build_pitch():
    name = "The Sock Tribunal"
    clauses = [
        "a washing machine that holds a tiny trial after every wash",
        "cross-examines the dryer under oath",
        "sentences it to return your missing sock with a handwritten apology",
    ]
    return name + " is " + ", ".join(clauses[:2]) + ", and " + clauses[2] + "."


def check_pitch(text):
    if not isinstance(text, str):
        raise SystemExit("pitch must be text")
    char_count = len(text)
    if not 1 <= char_count <= 220:
        raise SystemExit(f"pitch has {char_count} chars, want 1-220")
    if text.strip() != text or "\n" in text or "\r" in text:
        raise SystemExit("pitch must be a single line with no extra whitespace")
    if not text.endswith(".") or text.count(".") != 1:
        raise SystemExit("pitch must be exactly one sentence")
    if not text[0].isupper():
        raise SystemExit("pitch must start with a capital letter")


def main():
    pitch = build_pitch()
    check_pitch(pitch)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as out_file:
        out_file.write(pitch)
    return 0


if __name__ == "__main__":
    sys.exit(main())
