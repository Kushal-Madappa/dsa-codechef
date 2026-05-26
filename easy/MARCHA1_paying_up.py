# CodeChef: Paying Up (MARCHA1)
# https://www.codechef.com/problems/MARCHA1

# n <= 20 banknotes per test case -> 2^n <= ~1M subsets.
# Use a bitmask over subsets; for each, sum the selected notes and check
# against m. Stop at the first subset that matches.

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    found = False
    # Iterate all 2^n subsets (skip the empty one is fine; if m=0 we'd also
    # accept the empty subset, but problem guarantees m >= 1 -- still safe
    # because subset {} sums to 0 != m).
    for mask in range(1 << n):
        s = 0
        for k in range(n):
            if mask & (1 << k):
                s += a[k]
        if s == m:
            found = True
            break
    print("Yes" if found else "No")
