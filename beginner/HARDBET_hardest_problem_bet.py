# CodeChef: Hardest Problem Bet (HARDBET)
# https://www.codechef.com/problems/HARDBET
t = int(input())
for _ in range(t):
    sa, sb, sc = map(int, input().split())
    if sa < sb and sa < sc:
        print("Draw")
    elif sb < sa and sb < sc:
        print("Bob")
    else:
        print("Alice")
