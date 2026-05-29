# CodeChef: Second Largest (FLOW017)
# https://www.codechef.com/problems/FLOW017
t = int(input())
for _ in range(t):
    x = sorted(map(int, input().split()))
    print(x[1])
