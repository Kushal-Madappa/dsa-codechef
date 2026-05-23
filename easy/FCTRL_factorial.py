# CodeChef: Factorial (FCTRL) -- trailing zeros of N!
# https://www.codechef.com/problems/FCTRL
import sys
input = sys.stdin.readline  # T can be ~1e5; line-buffered input() is too slow.
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    z = 0
    p = 5
    while p <= n:
        z += n // p
        p *= 5
    out.append(str(z))
sys.stdout.write("\n".join(out))
