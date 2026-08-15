# CodeChef: Movie Weekend (MOVIEWKN)
# https://www.codechef.com/problems/MOVIEWKN
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    best_prod = -1
    best_r = -1
    best_idx = 0
    for i in range(n):
        p = l[i] * r[i]
        if p > best_prod or (p == best_prod and r[i] > best_r):
            best_prod = p
            best_r = r[i]
            best_idx = i + 1
    print(best_idx)
