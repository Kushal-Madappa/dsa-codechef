# CodeChef: Carvans (CARVANS)
# https://www.codechef.com/problems/CARVANS
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cur = float('inf')
    cnt = 0
    for x in a:
        if x <= cur:
            cnt += 1
            cur = x
    print(cnt)
