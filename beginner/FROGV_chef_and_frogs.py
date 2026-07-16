# CodeChef: Chef and Frogs (FROGV)
# https://www.codechef.com/problems/FROGV
import sys
input = sys.stdin.readline

n, k, p = map(int, input().split())
a = list(map(int, input().split()))
order = sorted(range(n), key=lambda i: a[i])
group = [0] * n
g = 0
for i in range(1, n):
    if a[order[i]] - a[order[i - 1]] > k:
        g += 1
    group[order[i]] = g
out = []
for _ in range(p):
    x, y = map(int, input().split())
    out.append("Yes" if group[x - 1] == group[y - 1] else "No")
sys.stdout.write("\n".join(out) + "\n")
