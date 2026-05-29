# CodeChef: Smallest Number of Notes (FLOW005)
# https://www.codechef.com/problems/FLOW005
notes = (100, 50, 10, 5, 2, 1)
t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    for d in notes:
        c += n // d
        n %= d
    print(c)
