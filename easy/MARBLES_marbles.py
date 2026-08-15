# CodeChef: Marbles (MARBLES)
# https://www.codechef.com/problems/MARBLES
from math import comb
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(comb(n-1, k-1))
