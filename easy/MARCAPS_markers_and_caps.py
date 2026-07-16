# CodeChef: Markers and Caps (MARCAPS)
# https://www.codechef.com/problems/MARCAPS
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    if max(cnt.values()) > n // 2:
        print("NO")
        continue
    idx = sorted(range(n), key=lambda i: (a[i], i))
    h = n // 2
    caps = [0] * n
    for k in range(n):
        caps[idx[k]] = a[idx[(k + h) % n]]
    print("YES")
    print(*caps)
