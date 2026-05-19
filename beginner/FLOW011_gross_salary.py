"""
CodeChef FLOW011 — Gross Salary (Beginner)
Python solution.

Problem (paraphrased): For T test cases, given a basic salary B
(integer), compute the gross salary using the formula:

    if B <= 1500:
        HRA = 10% of B
        DA  = 90% of B
    else:
        HRA = 500
        DA  = 98% of B

    Gross = B + HRA + DA

Output the gross with two decimal places — CodeChef's reference output
shows "X.YY" formatting for this problem.

Approach: straight conditional + format string. The only "trick" is
using buffered I/O for fast reading; the math is trivial.

Complexity: O(T) time, O(T) extra space for output buffering.
"""

import sys


def gross_salary(basic: float) -> float:
    """Compute gross salary per the FLOW011 specification."""
    if basic <= 1500:
        hra = 0.10 * basic
        da = 0.90 * basic
    else:
        hra = 500.0
        da = 0.98 * basic
    return basic + hra + da


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        basic = float(data[i])
        out.append(f"{gross_salary(basic):.2f}")
    sys.stdout.write('\n'.join(out) + '\n')


def _selftest() -> None:
    # Hand-checked cases.
    # B = 1203: HRA = 120.30, DA = 1082.70 -> gross = 2406.00
    assert round(gross_salary(1203), 2) == 2406.00
    # B = 10000: HRA = 500, DA = 9800 -> gross = 20300.00
    assert round(gross_salary(10000), 2) == 20300.00
    # B = 1500 (boundary -> still <=): HRA = 150, DA = 1350 -> gross = 3000
    assert round(gross_salary(1500), 2) == 3000.00
    # B = 1501 (just above): HRA = 500, DA = 1470.98 -> gross = 3471.98
    assert round(gross_salary(1501), 2) == 3471.98
    print("All tests passed.")


if __name__ == "__main__":
    if sys.stdin.isatty():
        _selftest()
    else:
        main()
