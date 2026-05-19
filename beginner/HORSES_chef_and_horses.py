"""
CodeChef HORSES — Chef and Horses
Difficulty: Beginner
Topics: Sorting, Greedy, Array

Problem (summary)
-----------------
Chef has N horses, each with a skill value. He must pick any two of
them such that the **absolute difference** in their skills is
**minimised**. Output that minimum difference. Multiple test cases T.

Approach — sort + scan adjacent pairs
-------------------------------------
The minimum |a - b| over any pair in an array is always achieved by
two **adjacent** elements after sorting. Quick proof: if a < b < c are
three sorted values, then b - a <= c - a and c - b <= c - a, so the
optimum lies among consecutive pairs. Therefore one pass over the
sorted array yields the answer.

I/O
---
First line T. For each test case: line with N, then N skill values.

Complexity (per test case)
--------------------------
Time:   O(N log N)  — dominated by sort.
Space:  O(N)        — the input list.
"""
from __future__ import annotations
import sys


def min_skill_diff(skills: list[int]) -> int:
    """Smallest |a - b| over any pair in `skills` (len >= 2)."""
    s = sorted(skills)
    best = s[1] - s[0]
    for i in range(2, len(s)):
        diff = s[i] - s[i - 1]
        if diff < best:
            best = diff
    return best


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        skills = [int(x) for x in data[idx:idx + n]]
        idx += n
        out.append(str(min_skill_diff(skills)))
    sys.stdout.write("\n".join(out) + "\n")


# ----------------------------- self-tests ---------------------------------
if __name__ == "__main__":
    # Sample from CodeChef:
    # 1
    # 5
    # 4 9 1 32 13
    # sorted -> 1 4 9 13 32 ; adj diffs -> 3 5 4 19 ; min = 3
    assert min_skill_diff([4, 9, 1, 32, 13]) == 3

    # Already sorted, all-different
    assert min_skill_diff([1, 2, 5, 10]) == 1

    # Duplicates -> minimum diff is 0
    assert min_skill_diff([7, 7, 100, 50]) == 0

    # Exactly two elements
    assert min_skill_diff([-3, 8]) == 11

    # Negative values
    assert min_skill_diff([-10, -3, -1, 4]) == 2

    # Large adjacent ties at the tail
    assert min_skill_diff([1, 100, 100]) == 0

    print("All tests passed for HORSES.")

    # I/O smoke test:
    #   echo -e "1\n5\n4 9 1 32 13" | python3 HORSES_chef_and_horses.py
    #   -> 3
