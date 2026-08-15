# CodeChef: Arranging Cup-cakes (RESQ)
# https://www.codechef.com/problems/RESQ
t = int(input())
for _ in range(t):
    n = int(input())
    i = 1
    while i * i < n:
        i += 1
    if i * i == n:
        print(0)
    else:
        for j in range(i - 1, 0, -1):
            if n % j == 0:
                print(n // j - j)
                break
