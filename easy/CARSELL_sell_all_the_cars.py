# CodeChef: Sell All the Cars (CARSELL)
# https://www.codechef.com/problems/CARSELL
MOD = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i, p in enumerate(a):
        if p - i > 0:
            ans = (ans + p - i) % MOD
    print(ans)
