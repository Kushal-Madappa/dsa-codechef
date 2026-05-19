"""
CodeChef LUCKFOUR — Lucky Four (Beginner)
Python solution.

Problem (paraphrased): Kostya likes the digit 4. For each of T integers
N, print the number of occurrences of the digit 4 in N's decimal
representation.

Approach: read the number as bytes/string and count the byte b'4'.
No arithmetic is needed — operating directly on the digit characters
is both clearer and faster than `n % 10` / `n //= 10`.

Buffered I/O via sys.stdin.buffer.read() is essential for CodeChef:
input() per line is dramatically slower under the test harnesses.

Complexity (per test case): O(d) where d = number of digits of N.
Overall: O(total input size).
"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        # data[i] is already a bytes object — count the literal '4' byte.
        out.append(str(data[i].count(b'4')))
    sys.stdout.write('\n'.join(out) + '\n')


def _selftest() -> None:
    """Smoke test the counting logic in isolation."""
    cases = [
        (b'4', 1),
        (b'40', 1),
        (b'44', 2),
        (b'12345', 1),
        (b'1234567894444', 5),
        (b'1000000000', 0),
        (b'0', 0),
    ]
    for n_bytes, expected in cases:
        assert n_bytes.count(b'4') == expected, (n_bytes, expected)
    print("All tests passed.")


if __name__ == "__main__":
    # If stdin is a tty (no piped input), run the self-test instead.
    if sys.stdin.isatty():
        _selftest()
    else:
        main()
