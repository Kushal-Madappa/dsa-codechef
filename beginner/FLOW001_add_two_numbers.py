"""
CodeChef: Add Two Numbers  (problem code: FLOW001)
URL: https://www.codechef.com/problems/FLOW001
Difficulty: Beginner

Problem
-------
The first line contains an integer T -- the number of test cases. Each of
the next T lines contains two integers A and B separated by whitespace.
For each test case print A + B on its own line.

Constraints (paraphrased)
-------------------------
1 <= T <= 1000
1 <= A, B <= 10000

Approach
--------
Trivial arithmetic problem. The teaching point is the I/O scaffold:

- Read everything once with buffered I/O for speed.
- Build the full output as a single string and write it once.
  Many small `print()` calls are slow in Python compared to a single
  buffered write.

This is the standard template you will reuse for almost every CP problem.

Complexity
----------
    Time:  O(T)  -- one addition per test case.
    Space: O(T)  -- buffered output list (could be streamed if needed).
"""

import io
import sys


def solve(stream: io.TextIOBase) -> str:
    data = stream.read().split()
    t = int(data[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        out.append(str(a + b))
    return "\n".join(out) + "\n"


def main() -> None:
    sys.stdout.write(solve(sys.stdin))


if __name__ == "__main__":
    # When run directly with no piped input, exercise the in-memory tests.
    if sys.stdin.isatty():
        sample_in = "3\n1 2\n100 200\n10 20\n"
        expected = "3\n300\n30\n"
        assert solve(io.StringIO(sample_in)) == expected

        # Edge: minimum and maximum allowed inputs
        edge_in = "2\n1 1\n10000 10000\n"
        assert solve(io.StringIO(edge_in)) == "2\n20000\n"

        # Edge: single test case
        single_in = "1\n7 8\n"
        assert solve(io.StringIO(single_in)) == "15\n"

        print("All tests passed.")
    else:
        main()
