# CodeChef: Maximum Weight Difference (MAXDIFF)
# https://www.codechef.com/problems/MAXDIFF
# Sort, then put max(K, N-K) largest items in the heavy group.
# answer = (sum of those M items) - (sum of the remaining N-M items)

for _ in range(int(input())):
    n, k = map(int, input().split())
    w = sorted(map(int, input().split()))
    m = max(k, n - k)
    heavy = sum(w[-m:])
    print(heavy - (sum(w) - heavy))
