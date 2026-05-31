# CodeChef: Farmer And His Plot (RECTSQ)
# https://www.codechef.com/problems/RECTSQ
from math import gcd

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print((a * b) // (g * g))
