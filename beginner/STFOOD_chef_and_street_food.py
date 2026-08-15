# CodeChef: Chef and Street Food (STFOOD)
# https://www.codechef.com/problems/STFOOD
t = int(input())
for _ in range(t):
    n = int(input())
    best = 0
    for _ in range(n):
        s, p, v = map(int, input().split())
        profit = (p // (s + 1)) * v
        if profit > best:
            best = profit
    print(best)
