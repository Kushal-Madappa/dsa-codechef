# CodeChef: The Lead Game (TLG)
# https://www.codechef.com/problems/TLG

n = int(input())
t1 = t2 = 0
best = 0
winner = 0

for _ in range(n):
    a, b = map(int, input().split())
    t1 += a
    t2 += b
    lead = abs(t1 - t2)
    if lead > best:
        best = lead
        winner = 1 if t1 > t2 else 2

print(winner, best)
