# CodeChef: Total Expenses (FLOW009)
# https://www.codechef.com/problems/FLOW009
t = int(input())
for _ in range(t):
    q, p = map(int, input().split())
    total = q * p * 0.9 if q > 1000 else q * p
    print(f"{total:.6f}")
