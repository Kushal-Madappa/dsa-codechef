# CodeChef: Chef and Notebooks (CNOTE)
# https://www.codechef.com/problems/CNOTE
t = int(input())
for _ in range(t):
    x, y, k, n = map(int, input().split())
    need = x - y
    ok = False
    for _ in range(n):
        p, c = map(int, input().split())
        if p >= need and c <= k:
            ok = True
    print("LuckyChef" if ok else "UnluckyChef")
