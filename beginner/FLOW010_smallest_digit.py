"""
CodeChef FLOW010 — Smallest Digit
Difficulty : Beginner (1-star)
Topic tags : Digit Extraction, Loops
-------------------------------------
Problem
-------
Given an integer N, find the smallest digit present in N.

Approach
--------
Extract each digit using the modulo/floor-division loop:
  digit = n % 10
  n //= 10
Track the running minimum. Convert N to positive first to handle
any negative input edge cases.

Complexity
----------
  Time  : O(log10 N) — one iteration per digit
  Space : O(1)

Submission note
---------------
CodeChef reads T test cases. Submit the full I/O block below on CodeChef.
"""


def smallest_digit(n: int) -> int:
    """Return the smallest (minimum) digit of the positive integer n."""
    n = abs(n)
    min_digit = 9
    while n > 0:
        digit = n % 10
        if digit < min_digit:
            min_digit = digit
        n //= 10
    return min_digit


# CodeChef I/O template
def main() -> None:
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(smallest_digit(n))


# self-test
if __name__ == "__main__":
    assert smallest_digit(12345) == 1
    assert smallest_digit(999)   == 9
    assert smallest_digit(100)   == 0
    assert smallest_digit(7)     == 7
    assert smallest_digit(30)    == 0
    print("All tests passed")
    # Uncomment to run interactive mode:
    # main()
