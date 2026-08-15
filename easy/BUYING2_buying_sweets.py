# CodeChef: Buying Sweets (BUYING2)
# https://www.codechef.com/problems/BUYING2
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    mn = min(a)
    if total % x >= mn:
        print(-1)
    else:
        print(total // x)
