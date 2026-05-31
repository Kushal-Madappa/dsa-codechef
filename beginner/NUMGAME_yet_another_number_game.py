# CodeChef: Yet Another Number Game (NUMGAME)
# https://www.codechef.com/problems/NUMGAME
t = int(input())
for _ in range(t):
    n = int(input())
    print("BOB" if n % 2 else "ALICE")
