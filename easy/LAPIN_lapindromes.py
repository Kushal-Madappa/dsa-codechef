# CodeChef: Lapindromes (LAPIN)
# https://www.codechef.com/problems/LAPIN
from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    h = len(s) // 2
    left = s[:h]
    right = s[len(s) - h:]
    print("YES" if Counter(left) == Counter(right) else "NO")
