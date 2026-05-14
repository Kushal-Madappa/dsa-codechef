"""
CodeChef: Reverse The Number  (problem code: FLOW007)
URL: https://www.codechef.com/problems/FLOW007
Difficulty: Beginner

Problem
-------
For each test case, given a positive integer N, output its reverse. Leading
zeros in the reversed number are dropped (e.g., 1200 -> 21, not 0021).

Constraints (paraphrased)
-------------------------
1 <= T <= 1000
1 <= N <= 10^6

Approach
--------
Two clean ways:

1. String reverse (chosen here):
       int(str(n)[::-1])
   Casting back to int automatically strips any leading zeros.

2. Pure arithmetic (good to know for languages without easy string slicing):
       result = 0
       while n:
           result = result * 10 + n % 10
           n //= 10

Both are O(d) where d is the digit count -- about log10(N).

Complexity
----------
    Time:  O(T * log N).
    Space: O(T) for the buffered output list.

Why this matters
----------------
A clean reminder that casting through int() is the easiest way to handle
leading-zero edge cases when reversing numbers.
"""

import io
import sys


def reverse_int(n: int) -> int:
    return int(str(n)[::-1])


def solve(stream: io.TextIOBase) -> str:
    data = stream.read().split()
    t = int(data[0])
    out: list[str] = []
    for i in range(1, t + 1):
        n = int(data[i])
        out.append(str(reverse_int(n)))
    return "\n".join(out) + "\n"


def main() -> None:
    sys.stdout.write(solve(sys.stdin))


if __name__ == "__main__":
    if sys.stdin.isatty():
        # Sample from problem statement
        sample_in = "4\n12345\n31203\n2123\n2300\n"
        expected = "54321\n30213\n3212\n32\n"
        assert solve(io.StringIO(sample_in)) == expected

        # Single digit (its own reverse)
        assert solve(io.StringIO("1\n7\n")) == "7\n"

        # Palindrome stays the same
        assert solve(io.StringIO("1\n12321\n")) == "12321\n"

        # Trailing zeros get dropped on reverse
        assert solve(io.StringIO("1\n1000000\n")) == "1\n"

        # Direct function tests
        assert reverse_int(12345) == 54321
        assert reverse_int(2300) == 32
        assert reverse_int(9) == 9

        print("All tests passed.")
    else:
        main()
