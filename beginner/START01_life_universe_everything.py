"""CodeChef START01 — Life, the Universe, and Everything (Beginner).

Read integers, one per line, and echo each one back until you encounter
the sentinel value 42. Do not output 42 itself or anything after it.

Pattern: terminating sentinel. Read all whitespace-separated tokens,
stream them out until the sentinel, then stop. Buffered I/O again.

Time:  O(n) in the number of tokens.
Space: O(n) for the output buffer.
"""

from __future__ import annotations
import sys
from io import StringIO


def solve(stream) -> str:
    out = []
    for token in stream.read().split():
        if token == "42":
            break
        out.append(token)
    return "\n".join(out) + ("\n" if out else "")


def main() -> None:
    sys.stdout.write(solve(sys.stdin))


def _test() -> None:
    # Sample from the problem statement.
    assert solve(StringIO("1\n2\n88\n42\n99\n")) == "1\n2\n88\n"
    # Edge: sentinel is first.
    assert solve(StringIO("42\n")) == ""
    # Edge: no sentinel — print everything.
    assert solve(StringIO("7\n")) == "7\n"
    # Edge: empty input.
    assert solve(StringIO("")) == ""
    print("START01_life_universe_everything: all tests passed.")


if __name__ == "__main__":
    if sys.stdin.isatty():
        _test()
    else:
        main()
