# CodeChef: Chef and Remissness (REMISS)
# https://www.codechef.com/problems/REMISS
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(max(a, b), a + b)
