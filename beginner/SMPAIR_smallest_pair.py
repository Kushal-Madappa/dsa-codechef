# CodeChef: The Smallest Pair (SMPAIR)
# https://www.codechef.com/problems/SMPAIR
import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x, y = heapq.nsmallest(2, a)
    print(x + y)
