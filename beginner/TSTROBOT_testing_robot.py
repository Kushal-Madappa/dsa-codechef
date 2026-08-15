# CodeChef: Testing Robot (TSTROBOT)
# https://www.codechef.com/problems/TSTROBOT
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    s = input()
    lo = hi = x
    for c in s:
        x += 1 if c == 'R' else -1
        if x > hi: hi = x
        if x < lo: lo = x
    print(hi - lo + 1)
