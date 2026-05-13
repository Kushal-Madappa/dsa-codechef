"""
CodeChef: Enormous Input Test  (problem code: INTEST)
URL: https://www.codechef.com/problems/INTEST
Difficulty: Beginner
Topics: Fast I/O

Problem
-------
The first line of input contains two integers n and k. Then n positive integers
follow, one per line. Count how many of those n integers are divisible by k.

Constraints (paraphrased)
-------------------------
1 <= n <= 10^7
1 <= k <= 10^7
1 <= t_i <= 10^9

The input is HUGE. The whole point of this problem is to learn that Python's
default `input()` is too slow for tight competitive limits -- you must use
buffered I/O (sys.stdin) here.

Approach
--------
- Read the entire input as one buffered byte blob, split on whitespace.
- Parse n and k from the first two tokens.
- Walk the remaining tokens, count those whose int value is divisible by k.

Complexity
----------
    Time:  O(n)   -- single pass.
    Space: O(n)   -- we hold the tokens in memory; can be reduced to O(1)
                     by reading line by line, but the buffered approach is
                     simplest and fastest in Python.
"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])

    count = 0
    # data[2 : 2 + n] are the n numbers
    for token in data[2 : 2 + n]:
        if int(token) % k == 0:
            count += 1

    sys.stdout.write(f"{count}\n")


if __name__ == "__main__":
    main()
