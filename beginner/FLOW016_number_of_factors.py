"""
CodeChef FLOW016 — Number of Factors
Difficulty : Beginner (1-star)
Topic tags : Math, Divisors, Square Root Trick
-----------------------------------------------
Problem
-------
Given an integer N, find the number of factors (divisors) of N.

Approach — Square root trick
------------------------------
For every i from 1 to sqrt(N):
  - If i divides N, count it.
  - If N/i != i, count N/i as well (the paired factor).

This reduces O(N) brute-force to O(sqrt(N)).

Why it works:
  Divisors come in pairs (i, N//i).  Both are <= sqrt(N) only when i
  equals sqrt(N) exactly (perfect square).  So we enumerate the smaller
  half and double-count, correcting for the square case.

Complexity
----------
  Time  : O(sqrt(N))
  Space : O(1)

Submission note
---------------
CodeChef reads T test cases. Submit the full I/O block below on CodeChef.
"""

import math


def count_factors(n: int) -> int:
    """Return the total number of positive divisors of n."""
    count = 0
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            count += 1          # i is a divisor
            if i != n // i:
                count += 1      # n//i is a distinct paired divisor
    return count


# CodeChef I/O template
def main() -> None:
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(count_factors(n))


# self-test
if __name__ == "__main__":
    assert count_factors(6)   == 4   # 1,2,3,6
    assert count_factors(1)   == 1   # 1
    assert count_factors(12)  == 6   # 1,2,3,4,6,12
    assert count_factors(36)  == 9   # perfect square: 1,2,3,4,6,9,12,18,36
    assert count_factors(100) == 9   # 1,2,4,5,10,20,25,50,100
    assert count_factors(7)   == 2   # prime: 1,7
    print("All tests passed")
    # Uncomment to run interactive mode:
    # main()
