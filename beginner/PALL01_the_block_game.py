# CodeChef: The Block Game (PALL01)
# https://www.codechef.com/problems/PALL01

t = int(input())
for _ in range(t):
    n = input().strip()
    print("wins" if n == n[::-1] else "loses")
