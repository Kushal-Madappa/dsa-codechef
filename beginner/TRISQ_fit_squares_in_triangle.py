# CodeChef: Fit Squares in Triangle (TRISQ)
# https://www.codechef.com/problems/TRISQ
t = int(input())
for _ in range(t):
    b = int(input())
    n = b // 2
    print(n * (n - 1) // 2)
