# CodeChef: Chef and Chocolates / Subtraction Game 1 (AMSGAME1)
# https://www.codechef.com/problems/AMSGAME1
from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    g = a[0]
    for x in a[1:]:
        g = gcd(g, x)
        if g == 1:
            break
    print(g)
