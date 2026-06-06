# CodeChef: GCD2 (GCD2)
# https://www.codechef.com/problems/GCD2
from math import gcd
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(gcd(a, b))
