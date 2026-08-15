# CodeChef: Stupid Machine (STUPMACH)
# https://www.codechef.com/problems/STUPMACH
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = a[0]
    ans = m
    for i in range(1, n):
        if a[i] < m:
            m = a[i]
        ans += m
    print(ans)
