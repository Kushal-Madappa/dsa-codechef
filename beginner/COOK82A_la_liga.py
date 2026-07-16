# CodeChef: La Liga (COOK82A)
# https://www.codechef.com/problems/COOK82A
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print("YES" if x == y and x > 0 else "NO")
