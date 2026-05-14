"""CodeChef FLOW002 — Find Remainder (Beginner).

Input
-----
First line: T, the number of test cases.
Each of the next T lines: two space-separated integers a and b (b != 0).

Output
------
For each test case, print a % b on its own line.

Pattern: buffered I/O template. We read everything once via
`sys.stdin.read()` and write everything once. In Python, per-line
`input()` and `print()` are slow enough that batching them matters.

Time:  O(T).
Space: O(T) for the output buffer.
"""

from __future__ import annotations
import sys
from io import StringIO


def solve(stream) -> str:
    data = stream.read().split()
    if not data:
        return ""
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        out.append(str(a % b))
    return "\n".join(out) + ("\n" if out else "")


def main() -> None:
    sys.stdout.write(solve(sys.stdin))


def _test() -> None:
    # Sample from the problem statement.
    assert solve(StringIO("3\n1 2\n100 200\n10 40\n")) == "1\n100\n10\n"
    # Edge: single test case.
    assert solve(StringIO("1\n7 3\n")) == "1\n"
    # Edge: divisor equals dividend.
    assert solve(StringIO("1\n5 5\n")) == "0\n"
    # Edge: T = 0.
    assert solve(StringIO("0\n")) == ""
    print("FLOW002_find_remainder: all tests passed.")


if __name__ == "__main__":
    # Run embedded tests when invoked from a TTY; otherwise behave as
    # a real submission and read from stdin.
    if sys.stdin.isatty():
        _test()
    else:
        main()
