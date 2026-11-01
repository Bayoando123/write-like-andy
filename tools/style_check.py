#!/usr/bin/env python3
"""Score a draft post against the Burnham-style rules in STYLE_GUIDE.md.

Usage: python tools/style_check.py path/to/post.txt
Note: round-up posts (format C) skip the verdict/fragment beats, so 75+ is a pass for them.
Zero dependencies. Prints a checklist and a score out of 100.
"""
import re
import sys

BANNED = [
    "excited to", "thrilled", "delighted", "leverage", "synergy",
    "game-changer", "game changer", "humbled", "i'm proud to announce",
]
HUMILITY = [
    "more to do", "not pretending", "won't pretend", "small step",
    "small measure", "first step", "overnight", "not even close",
    "won't fix everything", "doesn't fix everything", "pretend",
    "more i want to do", "a lot to do",
]
VERDICT = re.compile(
    r"(not fair|makes no sense|isn't right|it's not right)[^.]*\.\s*(so|that's why)\b",
    re.I,
)
FRAGMENT = re.compile(r"\bNot [^.]{1,40}\.\s+[A-Z][^.]{1,40}\.")
CONTRACTION = re.compile(r"\b\w+'(s|re|ll|ve|t|m|d)\b", re.I)
NUMBER = re.compile(r"(£\s?\d|\d[\d,.]*\s?(%|k|m|bn|seconds|minutes|days|weeks|years|people)|\b\d{2,}\b)", re.I)
OPENERS = ("but ", "and ", "so ", "because ")


def check(text: str):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    sentences = [s for s in re.split(r"(?<=[.?!])\s+", text) if s.strip()]
    words = len(text.split())
    low = text.lower()
    first = paras[0] if paras else ""

    def sent_count(p):
        return len([s for s in re.split(r"(?<=[.?!])\s+", p) if s.strip()])

    results = [
        ("Hook is a single short line (<= 25 words, <= 2 sentences)",
         sent_count(first) <= 2 and len(first.split()) <= 25),
        ("No paragraph over 3 sentences",
         all(sent_count(p) <= 3 for p in paras)),
        ("Uses a fairness verdict + 'So…'", bool(VERDICT.search(text))),
        ("Has a 'Not X. Y.' punch fragment", bool(FRAGMENT.search(text))),
        ("At least two concrete numbers", len(NUMBER.findall(text)) >= 2),
        ("Includes a humility clause", any(h in low for h in HUMILITY)),
        ("Contractions used (>= 3)", len(CONTRACTION.findall(text)) >= 3),
        ("Gear-change openers (But/And/So/Because >= 2)",
         sum(s.lower().startswith(OPENERS) for s in sentences) >= 2),
        ("No hashtags", "#" not in text),
        ("No exclamation marks", "!" not in text),
        ("No corporate filler", not any(b in low for b in BANNED)),
        ("Length 70–600 words", 70 <= words <= 600),
    ]
    return results, words


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as f:
        text = f.read()
    results, words = check(text)
    passed = sum(ok for _, ok in results)
    for label, ok in results:
        print(f"[{'x' if ok else ' '}] {label}")
    score = round(100 * passed / len(results))
    print(f"\n{words} words | Score: {score}/100")


if __name__ == "__main__":
    main()
