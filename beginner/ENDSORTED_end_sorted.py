# CodeChef: End Sorted (ENDSORTED)
# https://www.codechef.com/problems/ENDSORTED
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    p1 = a.index(1) + 1
    pn = a.index(n) + 1
    moves = (p1 - 1) + (n - pn)
    if p1 > pn:
        moves -= 1
    print(moves)
