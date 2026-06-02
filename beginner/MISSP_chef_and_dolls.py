# CodeChef: Chef and Dolls (MISSP)
# https://www.codechef.com/problems/MISSP
t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    for _ in range(n):
        res ^= int(input())
    print(res)
