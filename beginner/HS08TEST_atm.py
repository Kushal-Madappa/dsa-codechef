"""
CodeChef: ATM  (problem code: HS08TEST)
URL: https://www.codechef.com/problems/HS08TEST
Difficulty: Beginner
Topics: Conditionals, Arithmetic, I/O formatting

Problem
-------
Pooja's debit account balance is Y. The ATM charges a fixed transaction fee
of 0.50 per withdrawal. She wants to withdraw X. The withdrawal succeeds iff:
    1. X is a positive multiple of 5, AND
    2. X + 0.50 <= Y  (she can cover the withdrawal plus the fee).

If it succeeds, print her new balance to two decimal places.
Otherwise, print her original balance to two decimal places.

Input format
------------
A single line with two values: X (integer) and Y (real number).

Example
-------
    Input:  30 120.00
    Output: 89.50

    Input:  42 120.00
    Output: 120.00   (42 is not a multiple of 5)

    Input:  300 120.00
    Output: 120.00   (insufficient funds)

Complexity
----------
    Time:  O(1)
    Space: O(1)
"""


def main() -> None:
    parts = input().split()
    withdrawal = int(parts[0])
    balance = float(parts[1])

    if withdrawal > 0 and withdrawal % 5 == 0 and withdrawal + 0.50 <= balance:
        balance -= withdrawal + 0.50

    # Always two decimal places, as required by the problem statement.
    print(f"{balance:.2f}")


if __name__ == "__main__":
    main()
