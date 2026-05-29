# CodeChef: Cutting Recipes (RECIPE)
# https://www.codechef.com/problems/RECIPE
from math import gcd
from functools import reduce

t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    arr = data[1:]
    g = reduce(gcd, arr)
    print(*[x // g for x in arr])
