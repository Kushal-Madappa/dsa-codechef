"""
CodeChef — TRICOIN: Chef and Triangular Pile of Coins (Beginner)

Problem:
    For each test case, given N coins, build a triangle where row k has
    exactly k coins (1 + 2 + 3 + ... + k). Return the largest H such that
    1 + 2 + ... + H ≤ N, i.e. the maximum number of fully-filled rows.

Closed-form (preferred):
    1 + 2 + ... + H = H(H+1)/2 ≤ N
    ⇒  H ≤ (−1 + sqrt(1 + 8N)) / 2
    ⇒  H = floor((sqrt(8N + 1) − 1) / 2)

    Using `math.isqrt` keeps integer-only arithmetic — no float
    rounding pitfalls when N is large.

Why not a loop? A loop is O(√N) per query (still fast enough), but the
closed form is O(1) and is the cleaner CP idiom.

Complexity per test case:
    Time:  O(1)
    Space: O(1)

Input format:
    First line:  T (number of test cases, T ≤ 100)
    Next T lines: a single integer N (1 ≤ N ≤ 10^9)
Output format:
    For each test case, the number of fully-filled rows.
"""

import math
import sys


def max_rows(n: int) -> int:
    """Largest H such that H*(H+1)//2 <= n."""
    # H = floor((sqrt(8n+1) - 1) / 2) — integer-only via isqrt
    return (math.isqrt(8 * n + 1) - 1) // 2


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        out.append(str(max_rows(n)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    # Self-tests (run before reading stdin so the file is safe to execute locally)
    # Triangular numbers: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
    assert max_rows(1) == 1            # exactly 1 row
    assert max_rows(2) == 1            # row 2 needs 3, not enough
    assert max_rows(3) == 2            # exactly 2 rows
    assert max_rows(5) == 2            # 2 rows + 2 leftover
    assert max_rows(6) == 3            # exactly 3 rows
    assert max_rows(10) == 4           # exactly 4 rows
    assert max_rows(11) == 4           # 4 rows + 1 leftover
    assert max_rows(55) == 10          # exactly 10 rows
    assert max_rows(10**9) == 44720    # large-N stress test
    print("Self-tests passed. Reading stdin (Ctrl-D to end)...", file=sys.stderr)
    main()
