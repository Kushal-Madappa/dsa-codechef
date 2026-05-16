"""
CodeChef FLOW004 — First and Last Digit
Difficulty: Beginner (1★)
Topic: Basic Math / String Manipulation
URL: https://www.codechef.com/problems/FLOW004

Problem:
  Given T test cases, each with a positive integer N,
  print the sum of its first and last digits.

Approach:
  Convert N to its string representation — O(d) where d = digit count.
  First digit = s[0], last digit = s[-1].
  For a single-digit number both positions are the same digit, so the
  sum is 2 × that digit (e.g. N=9 → 9+9 = 18).

Time:  O(d) per test case   (d ≤ 9 for a 32-bit integer)
Space: O(1)

I/O pattern: buffered read → single write (standard CodeChef template).
"""

import sys
import io


def first_last_digit_sum(n: int) -> int:
    """Return sum of the first and last decimal digit of n."""
    s = str(n)
    return int(s[0]) + int(s[-1])


def main() -> None:
    data = sys.stdin.read().split()
    t = int(data[0])
    out: list[str] = []
    for i in range(1, t + 1):
        out.append(str(first_last_digit_sum(int(data[i]))))
    sys.stdout.write("\n".join(out) + "\n")


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

def _test() -> None:
    assert first_last_digit_sum(1212) == 3     # 1 + 2
    assert first_last_digit_sum(1000) == 1     # 1 + 0
    assert first_last_digit_sum(9)    == 18    # 9 + 9 (single digit)
    assert first_last_digit_sum(55)   == 10    # 5 + 5
    assert first_last_digit_sum(1234567890) == 1   # 1 + 0

    # Integration: simulate stdin for two test cases
    fake_in = io.StringIO("2\n1212\n9\n")
    sys.stdin = fake_in
    captured = io.StringIO()
    sys.stdout = captured
    main()
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    assert captured.getvalue() == "3\n18\n"

    print("All tests passed ✓")


if __name__ == "__main__":
    import os
    if os.getenv("TEST"):
        _test()
    else:
        _test()   # always run tests when executed directly
        # comment out _test() and uncomment main() before submitting:
        # main()
