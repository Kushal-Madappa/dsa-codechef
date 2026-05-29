# CodeChef: Cops and the Thief Devu (COPS)
# https://www.codechef.com/problems/COPS
t = int(input())
for _ in range(t):
    parts = list(map(int, input().split()))
    m, x, y = parts[0], parts[1], parts[2]
    cops = list(map(int, input().split())) if m > 0 else []
    r = x * y
    covered = [False] * 101  # index 1..100
    for c in cops:
        lo = max(1, c - r)
        hi = min(100, c + r)
        for h in range(lo, hi + 1):
            covered[h] = True
    safe = sum(1 for h in range(1, 101) if not covered[h])
    print(safe)
