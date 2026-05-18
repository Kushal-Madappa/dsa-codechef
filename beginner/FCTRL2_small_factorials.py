"""
CodeChef — FCTRL2: Small Factorials (Beginner / Easy)

Problem:
    For each test case, given an integer N (1 ≤ N ≤ 100), print N!
    The result can be hundreds of digits long, so languages with native
    big integers have a clear advantage — Python is perfect here.

Approach:
    Two equally valid options:
      (a) `math.factorial(n)` — battle-tested C implementation in CPython.
      (b) Reduce with multiplication — pedagogical alternative.

    We use `math.factorial` for the actual answer and provide a tiny
    `factorial_iter` to demonstrate the underlying mechanic.

Complexity:
    Time:  O(N log² N) for `math.factorial` thanks to balanced
           multiplication of split products; O(N · M(d)) for the naive
           loop where d is the number of digits.
    Space: O(d) for the resulting big integer (d ≈ N log10(N/e)).

Input format:
    First line:  T (1 ≤ T ≤ 100)
    Next T lines: an integer N (1 ≤ N ≤ 100)
Output format:
    For each test case, N! on its own line.
"""

import math
import sys


def factorial_iter(n: int) -> int:
    """Iterative factorial — same answer as math.factorial, slower but transparent."""
    result: int = 1
    for k in range(2, n + 1):
        result *= k
    return result


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        out.append(str(math.factorial(n)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    # Self-tests
    assert factorial_iter(0) == 1
    assert factorial_iter(1) == 1
    assert factorial_iter(5) == 120
    assert factorial_iter(10) == 3628800
    assert factorial_iter(20) == 2432902008176640000
    # Spot-check parity with math.factorial across the full input range
    for n in (0, 1, 2, 3, 25, 50, 75, 100):
        assert factorial_iter(n) == math.factorial(n), f"mismatch at {n}"
    # 100! has 158 digits
    assert len(str(math.factorial(100))) == 158
    print("Self-tests passed. Reading stdin (Ctrl-D to end)...", file=sys.stderr)
    main()
