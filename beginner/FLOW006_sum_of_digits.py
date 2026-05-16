"""
CodeChef FLOW006 — Sum of Digits
Difficulty: Beginner (1★)
Topic: Basic Math
URL: https://www.codechef.com/problems/FLOW006

Problem:
  Given T test cases, each with a non-negative integer N,
  print the sum of all its digits.

Approach:
  Repeated modulo: pull the last digit with n % 10, accumulate, then
  floor-divide by 10.  This avoids string conversion and is idiomatic
  for digit-extraction problems in CP.

  Alternatively: sum(int(c) for c in str(n)) — same O(d), more Pythonic
  but marginally slower in tight loops.

Time:  O(d) per test case   (d = number of digits)
Space: O(1)

I/O pattern: buffered read → single write.
"""

import sys
import io


def digit_sum(n: int) -> int:
    """Return the sum of all decimal digits of non-negative integer n."""
    if n == 0:
        return 0
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total


def main() -> None:
    data = sys.stdin.read().split()
    t = int(data[0])
    out: list[str] = []
    for i in range(1, t + 1):
        out.append(str(digit_sum(int(data[i]))))
    sys.stdout.write("\n".join(out) + "\n")


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

def _test() -> None:
    assert digit_sum(0)    == 0
    assert digit_sum(5)    == 5
    assert digit_sum(10)   == 1
    assert digit_sum(1234) == 10   # 1+2+3+4
    assert digit_sum(999)  == 27   # 9+9+9
    assert digit_sum(100)  == 1

    # Integration: simulate stdin for three test cases
    fake_in = io.StringIO("3\n1234\n999\n0\n")
    sys.stdin = fake_in
    captured = io.StringIO()
    sys.stdout = captured
    main()
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    assert captured.getvalue() == "10\n27\n0\n"

    print("All tests passed ✓")


if __name__ == "__main__":
    _test()
    # Before submitting, comment out _test() and uncomment main():
    # main()
