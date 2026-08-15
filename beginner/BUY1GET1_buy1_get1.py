# CodeChef: Buy1-Get1 (BUY1GET1)
# https://www.codechef.com/problems/BUY1GET1
from collections import Counter
t = int(input())
for _ in range(t):
    s = input().strip()
    c = Counter(s)
    print(sum((v + 1) // 2 for v in c.values()))
