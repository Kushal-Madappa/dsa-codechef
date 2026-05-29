# CodeChef: IPL (ZCO14004)
# https://www.codechef.com/ZCOPRAC/problems/ZCO14004
# Pick a subset of N matches (fees a[i]) to MAXIMISE sum,
# constraint: cannot watch 3 or more in a row.
# Recurrence (dp[i] = best over prefix 0..i):
#   dp[i] = max( dp[i-1],                          # skip i
#                dp[i-2] + a[i],                   # take i alone
#                dp[i-3] + a[i] + a[i-1] )         # take i and i-1
# O(N) time, O(1) space with three rolling scalars.

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(a[0])
elif n == 2:
    print(a[0] + a[1])
else:
    d_m3, d_m2, d_m1 = 0, a[0], a[0] + a[1]  # dp[-1], dp[0], dp[1]
    for i in range(2, n):
        cur = max(d_m1, d_m2 + a[i], d_m3 + a[i] + a[i - 1])
        d_m3, d_m2, d_m1 = d_m2, d_m1, cur
    print(d_m1)
