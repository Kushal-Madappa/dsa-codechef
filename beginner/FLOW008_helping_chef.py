# CodeChef: Helping Chef (FLOW008)
# https://www.codechef.com/problems/FLOW008
t = int(input())
for _ in range(t):
    n = int(input())
    print("Thanks for helping Chef!" if n < 10 else -1)
