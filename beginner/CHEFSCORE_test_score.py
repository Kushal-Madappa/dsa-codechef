# CodeChef: Test Score (CHEFSCORE)
# https://www.codechef.com/problems/CHEFSCORE
t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    print("YES" if y % x == 0 and 0 <= y <= n * x else "NO")
