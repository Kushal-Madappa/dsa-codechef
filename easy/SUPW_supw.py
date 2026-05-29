# CodeChef: SUPW (ZCO14002)
# https://www.codechef.com/problems/ZCO14002
n = int(input())
a = list(map(int, input().split()))
if n <= 3:
    print(min(a))
else:
    d1, d2, d3 = a[0], a[1], a[2]
    for i in range(3, n):
        cur = a[i] + min(d1, d2, d3)
        d1, d2, d3 = d2, d3, cur
    print(min(d1, d2, d3))
